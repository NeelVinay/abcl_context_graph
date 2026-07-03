"""Stage: turn call recordings (mp3) into plain-text transcripts.

100% local, no paid API (customer PII stays on-machine):
  - WhisperX `large-v3` (silero VAD)  -> speech to text  (Hinglish: lang="hi")
  - pyannote speaker-diarization-3.1  -> who-spoke-when -> Agent / Customer labels

Output is a plain transcript, one turn per line (the format the manager asked for):

    Agent: नमस्ते, क्या मैं ... से बात कर रही हूँ?
    Customer: हाँ बोलिए।

One `<lead-id>.txt` per recording in data/audio_transcripts/. Resumable: a file
whose transcript already exists is skipped (unless --overwrite).

  python run_transcribe.py                 # up to 100 recordings from config.AUDIO_SRC
  python run_transcribe.py --limit 5       # quick batch
  python run_transcribe.py FILE [FILE...]  # specific recordings (validation)
"""
from __future__ import annotations

import argparse
import re
import signal
import subprocess
import tempfile
import time
from contextlib import contextmanager
from pathlib import Path


class _Timeout(Exception):
    pass


@contextmanager
def _time_limit(seconds: int):
    """Raise _Timeout if the block runs longer than `seconds` (main-thread only, Unix)."""
    def _handler(signum, frame):  # noqa: ANN001
        raise _Timeout(f"exceeded {seconds}s")
    old = signal.signal(signal.SIGALRM, _handler)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)

# WhisperX / pyannote checkpoints predate torch 2.6's `weights_only=True` default.
# These are trusted models shipped by the packages, so restore the legacy behavior.
# (Must be patched before any model is loaded.)
import torch

_ORIG_TORCH_LOAD = torch.load


def _patched_torch_load(*args, **kwargs):
    # Force (not setdefault): Lightning passes weights_only=True explicitly.
    kwargs["weights_only"] = False
    return _ORIG_TORCH_LOAD(*args, **kwargs)


torch.load = _patched_torch_load

import config  # noqa: E402

# ---- model / decoding settings (proven during Stage 0) ----
MODEL_SIZE = "large-v3"          # `small` produces word-salad on noisy Hinglish phone audio
LANG = "hi"                      # Hindi/Hinglish; Devanagari + English mixed
COMPUTE_TYPE = "int8"            # CPU-friendly; CTranslate2 has no MPS path on Mac

# Domain prompt: primes Whisper with the JustDial vocabulary it otherwise garbles
# phonetically (leads/category/rating/etc.). A natural bilingual sentence works better
# than a raw word list. Kept short (Whisper's prompt window is ~224 tokens).
JUSTDIAL_PROMPT = (
    "यह JustDial का customer support call है। Business owner leads, inquiry, category, "
    "pincode, rating, reviews, feedback, contract, response को लेकर बात कर रहे हैं। "
    "Agent customer support, ticket, area, location, renewal की help करता है।"
)

ASR_OPTIONS = {                  # tame Whisper's repetition / silence hallucinations
    "condition_on_previous_text": False,
    "no_speech_threshold": 0.6,
    "repetition_penalty": 1.15,  # discourage looping ("जी जी जी जी ...")
    "no_repeat_ngram_size": 3,   # hard-block any 3-gram from repeating
    "initial_prompt": JUSTDIAL_PROMPT,   # (#1) domain vocabulary hint
    "beam_size": 5,              # (#4) modest beam (8 hung on long garbled non-Hindi audio)
}

# Safety net: a single pathological call (garbled non-Hindi audio) can send Whisper's
# decoder into a near-infinite loop and freeze the whole batch. Cap per-file wall time;
# on timeout we skip that call and continue.
MAX_SECONDS_PER_FILE = 600

# (#2) Audio clean-up: light denoise + telephone-band filter + volume normalization,
# applied via ffmpeg before Whisper sees the audio. Helps noisy phone recordings.
CLEAN_AUDIO = True
_FFMPEG_FILTER = "highpass=f=100,lowpass=f=3800,afftdn=nf=-25,dynaudnorm=g=5"

# (#3) Per-file language detection: some calls are Telugu/Tamil, not Hindi — forcing
# Hindi on them produces garble. Auto-detect per file and route the aligner accordingly.
AUTO_LANG = True

# Whisper hallucinates these on silence/noise (YouTube training artifacts) — drop a turn
# that is essentially nothing but these phrases.
_HALLUCINATION_PHRASES = [
    "सब्सक्राइब", "subscribe", "thanks for watching", "thank you for watching",
    "please subscribe", "देखने के लिए धन्यवाद", "share कर दिया जाएगा से",
]

# Scripted phrases only the calling agent says — strong signal for Agent vs Customer.
_AGENT_MARKERS = [
    "aditya birla", "birla", "capital", "कैपिटल", "बोल रही हूँ", "बोल रहा हूँ",
    "बात कर रही", "बात कर रहा", "केवाईसी", "kyc",
]


# ----------------------------- text hygiene -----------------------------
def _collapse_repeats(text: str, max_phrase: int = 4) -> str:
    """Squash Whisper's loops: a word repeated many times ('जी जी जी ...') OR a short
    phrase repeated back-to-back ('नहीं हुआ नहीं हुआ ...'). Keeps natural single-word
    doublings ('हाँ हाँ') but removes loop-like runs. Decoding penalties reduce these
    at generation time; this is the text-level safety net for survivors."""
    words = text.split()
    out: list[str] = []
    i, n = 0, len(words)
    while i < n:
        best_len, best_reps = 1, 1
        for plen in range(1, max_phrase + 1):
            if i + 2 * plen > n:
                break
            phrase = words[i:i + plen]
            reps, j = 1, i + plen
            while words[j:j + plen] == phrase:
                reps += 1
                j += plen
            if reps >= 2 and reps * plen > best_reps * best_len:
                best_len, best_reps = plen, reps
        if best_len == 1 and best_reps >= 3:        # word loop -> keep 2 ("बड़ी बड़ी")
            out.extend(words[i:i + 1] * 2)
            i += best_reps
        elif best_len >= 2 and best_reps >= 2:       # phrase loop -> keep 1
            out.extend(words[i:i + best_len])
            i += best_len * best_reps
        else:
            out.append(words[i])
            i += 1
    return " ".join(out)


def _is_hallucination(text: str) -> bool:
    """True if a segment is just a known hallucination or a single word repeated."""
    t = text.strip().lower()
    if not t:
        return True
    words = t.split()
    if len(words) >= 4 and len(set(words)) == 1:   # "तो तो तो तो"
        return True
    for p in _HALLUCINATION_PHRASES:
        t = t.replace(p.lower(), "")
    leftover = re.sub(r"[\s।.,!?\-]+", "", t)
    return len(leftover) < 3


# ----------------------------- audio pre-processing (#2) -----------------------------
def _clean_audio(path: Path):
    """Run ffmpeg to denoise + band-filter + normalize -> 16k mono wav in a temp file.
    Returns the temp path (caller deletes) or None if ffmpeg fails (falls back to raw)."""
    tmp = Path(tempfile.gettempdir()) / f"_clean_{path.stem}.wav"
    cmd = ["ffmpeg", "-y", "-i", str(path), "-af", _FFMPEG_FILTER,
           "-ar", "16000", "-ac", "1", str(tmp)]
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        return tmp
    except Exception:  # noqa: BLE001 — any ffmpeg issue -> use raw audio
        return None


# ----------------------------- model loading -----------------------------
_MODELS: dict = {}


def _pick_gpu_device(requested: str) -> str:
    """Resolve the diarization/alignment device: honour explicit cpu, else use Apple
    GPU (mps) when available — measured ~3.8x faster than CPU with identical output."""
    if requested and requested != "auto":
        return requested
    try:
        import torch
        if torch.backends.mps.is_available():
            return "mps"
    except Exception:  # noqa: BLE001
        pass
    return "cpu"


def load_models(model_size: str = MODEL_SIZE, gpu_device: str = "auto") -> dict:
    """Load (once) the Whisper model (CPU), and the aligner + diarizer (GPU/MPS if available).
    Transcription stays on CPU: CTranslate2 int8 beats MLX/MPS for Whisper on this machine."""
    if _MODELS:
        return _MODELS
    import whisperx
    from whisperx.diarize import DiarizationPipeline
    dev = _pick_gpu_device(gpu_device)
    # (#3) language=None lets Whisper detect per file (Telugu/Tamil calls don't get forced to Hindi)
    asr_lang = None if AUTO_LANG else LANG
    print(f"[load] WhisperX {model_size} (cpu/{COMPUTE_TYPE}, silero VAD, "
          f"lang={asr_lang or 'auto'}) ...")
    t0 = time.time()
    asr = whisperx.load_model(model_size, device="cpu", compute_type=COMPUTE_TYPE,
                              vad_method="silero", language=asr_lang, asr_options=ASR_OPTIONS)
    print(f"[load]   done in {time.time() - t0:.0f}s")
    print(f"[load] Hindi alignment model on {dev} (word-level timestamps) ...")
    t0 = time.time()
    align_model, align_meta, align_dev = None, None, dev
    try:
        align_model, align_meta = whisperx.load_align_model(language_code=LANG, device=dev)
        print(f"[load]   done in {time.time() - t0:.0f}s")
    except Exception as e:  # noqa: BLE001 — retry on CPU, else segment-level labels
        print(f"[load]   {dev} align failed ({type(e).__name__}); retrying on cpu")
        try:
            align_model, align_meta = whisperx.load_align_model(language_code=LANG, device="cpu")
            align_dev = "cpu"
        except Exception:  # noqa: BLE001
            align_dev = "cpu"
    print(f"[load] pyannote diarization pipeline (device={dev}) ...")
    t0 = time.time()
    try:
        diar = DiarizationPipeline(device=dev)        # uses HF token stored on disk
    except Exception as e:  # noqa: BLE001 — fall back to CPU diarization
        print(f"[load]   {dev} diarization failed ({type(e).__name__}); using cpu")
        diar = DiarizationPipeline(device="cpu")
    print(f"[load]   done in {time.time() - t0:.0f}s")
    _MODELS.update(whisperx=whisperx, asr=asr, diar=diar, align_dev=align_dev,
                   align_model=align_model, align_meta=align_meta,
                   aligners={LANG: (align_model, align_meta)})  # per-language aligner cache
    return _MODELS


def _aligner_for(lang: str, models: dict):
    """Return (model, meta) for a language, loading + caching on demand. None if
    that language has no WhisperX aligner (caller falls back to segment-level labels)."""
    cache = models["aligners"]
    if lang in cache:
        return cache[lang]
    try:
        m, meta = models["whisperx"].load_align_model(language_code=lang,
                                                      device=models.get("align_dev", "cpu"))
        cache[lang] = (m, meta)
    except Exception:  # noqa: BLE001 — no aligner for this language
        cache[lang] = (None, None)
    return cache[lang]


# ----------------------------- core steps -----------------------------
def _speaker_by_overlap(start: float, end: float, diar_df) -> str | None:
    """Diarization speaker whose region overlaps this [start,end] segment the most."""
    best, best_ov = None, 0.0
    for row in diar_df.itertuples():
        ov = max(0.0, min(end, row.end) - max(start, row.start))
        if ov > best_ov:
            best_ov, best = ov, row.speaker
    return best


def _segments_to_turns(segments: list[dict], diar_df) -> list[tuple[str, str]]:
    """Assign each segment its dominant speaker, drop hallucinations, then merge
    consecutive same-speaker segments into one turn. Returns [(raw_speaker, text)]."""
    labeled = []
    for seg in segments:
        text = seg["text"].strip()
        if _is_hallucination(text):
            continue
        spk = _speaker_by_overlap(seg["start"], seg["end"], diar_df) or "SPEAKER_00"
        labeled.append((spk, text))

    turns: list[tuple[str, str]] = []
    for spk, text in labeled:
        if turns and turns[-1][0] == spk:
            turns[-1] = (spk, f"{turns[-1][1]} {text}")
        else:
            turns.append((spk, text))
    return turns


# Word-timing/diarization on mono cross-talk audio is noisy, so we smooth:
MAX_WORD_DUR = 1.5   # a word longer than this is a stretched-alignment artifact (Latin
                     # English in the Hindi aligner) -> its timestamp is unreliable
MEDIAN_W = 2         # median-filter half-window over the per-word speaker sequence
MIN_RUN = 2          # speaker runs shorter than this get folded into their neighbour


def _median_filter(seq: list[str], w: int) -> list[str]:
    """Replace each element with the majority of its [-w, +w] neighbourhood."""
    n = len(seq)
    out = list(seq)
    for i in range(n):
        win = seq[max(0, i - w):min(n, i + w + 1)]
        out[i] = max(set(win), key=win.count)
    return out


def _aligned_to_turns(aligned_result: dict, diar_df) -> list[tuple[str, str]]:
    """Build clean turns from per-WORD speakers + smoothing.

    Each aligned word gets the diarization speaker its own timestamp overlaps most.
    Words with no/implausible timing inherit a neighbour. The per-word speaker sequence
    is then smoothed (median filter + minimum-run merge) so turns don't flip mid-sentence
    on a single noisy word. Returns [(raw_speaker, text)] or [] if no words."""
    words: list[tuple[str | None, str]] = []
    for seg in aligned_result.get("segments", []):
        segw = seg.get("words") or []
        if not segw:                        # segment had nothing alignable
            txt = (seg.get("text") or "").strip()
            if txt:
                words.append((_speaker_by_overlap(seg.get("start", 0.0),
                                                  seg.get("end", 0.0), diar_df), txt))
            continue
        for w in segw:
            token = (w.get("word") or "").strip()
            if not token:
                continue
            s, e = w.get("start"), w.get("end")
            reliable = s is not None and e is not None and (e - s) <= MAX_WORD_DUR
            spk = _speaker_by_overlap(s, e, diar_df) if reliable else None
            words.append((spk, token))
    if not words:
        return []

    # fill unreliable/missing speakers from neighbours (forward then backward)
    spk_seq = [w[0] for w in words]
    last = None
    for i, s in enumerate(spk_seq):
        if s is None:
            spk_seq[i] = last
        else:
            last = s
    nxt = None
    for i in range(len(spk_seq) - 1, -1, -1):
        if spk_seq[i] is None:
            spk_seq[i] = nxt
        else:
            nxt = spk_seq[i]
    spk_seq = [s or "SPEAKER_00" for s in spk_seq]

    spk_seq = _median_filter(spk_seq, MEDIAN_W)
    # fold short runs into the previous speaker, then smooth once more
    i = 0
    while i < len(spk_seq):
        j = i
        while j < len(spk_seq) and spk_seq[j] == spk_seq[i]:
            j += 1
        if i > 0 and (j - i) < MIN_RUN:
            for k in range(i, j):
                spk_seq[k] = spk_seq[i - 1]
        i = j
    spk_seq = _median_filter(spk_seq, MEDIAN_W)

    turns: list[tuple[str, str]] = []
    for spk, (_, token) in zip(spk_seq, words):
        if turns and turns[-1][0] == spk:
            turns[-1] = (spk, f"{turns[-1][1]} {token}")
        else:
            turns.append((spk, token))
    # drop any turn that is only a hallucination / single repeated word
    return [(s, t) for s, t in turns if not _is_hallucination(t)]


def _map_speakers(turns: list[tuple[str, str]], diar_df) -> dict[str, str]:
    """Decide which raw cluster is Agent vs Customer.

    Primary signal: scripted agent markers (only the agent says "Aditya Birla
    Capital", "बोल रही हूँ", etc.). Tiebreak: total speaking time (agents talk more).
    """
    speakers = list(dict.fromkeys(s for s, _ in turns))
    if not speakers:
        return {}
    talk = {s: 0.0 for s in speakers}
    for row in diar_df.itertuples():
        if row.speaker in talk:
            talk[row.speaker] += row.end - row.start
    marker_hits = {s: 0 for s in speakers}
    for spk, text in turns:
        low = text.lower()
        marker_hits[spk] += sum(1 for m in _AGENT_MARKERS if m in low)

    agent = max(speakers, key=lambda s: (marker_hits[s], talk.get(s, 0.0)))
    return {s: ("Agent" if s == agent else "Customer") for s in speakers}


def _render(turns: list[tuple[str, str]], mapping: dict[str, str]) -> str:
    """Plain transcript, one turn per line: 'Agent: ...' / 'Customer: ...'."""
    return "\n".join(f"{mapping.get(spk, 'Customer')}: {text}" for spk, text in turns)


def transcribe_file(path: Path, models: dict, out_dir: Path,
                    overwrite: bool = False) -> str:
    """Transcribe + diarize one recording -> write <stem>.txt. Returns a status string."""
    out_path = out_dir / f"{path.stem}.txt"
    if out_path.exists() and not overwrite:
        return f"skip (exists): {out_path.name}"

    whisperx = models["whisperx"]
    # (#2) clean the audio first (denoise/filter/normalize); fall back to raw on any failure
    clean_tmp = _clean_audio(path) if CLEAN_AUDIO else None
    audio = whisperx.load_audio(str(clean_tmp or path))
    dur = len(audio) / 16000.0

    try:
        with _time_limit(MAX_SECONDS_PER_FILE):   # a pathological call can't freeze the batch
            result = models["asr"].transcribe(audio, batch_size=4)
            lang = result.get("language", LANG)    # (#3) language Whisper detected for this file
            # drop silence/noise hallucination segments BEFORE alignment (can't bleed into turns)
            segments = [s for s in result["segments"]
                        if not _is_hallucination((s.get("text") or "").strip())]
            diar_df = models["diar"](audio, min_speakers=1, max_speakers=2)  # 1:1 calls

            # Align with the DETECTED language's aligner; non-aligned languages -> segment-level.
            turns, how = [], "segment"
            align_model, align_meta = _aligner_for(lang, models)
            if segments and align_model is not None:
                try:
                    aligned = whisperx.align(segments, align_model, align_meta,
                                             audio, models.get("align_dev", "cpu"),
                                             return_char_alignments=False)
                    turns = _aligned_to_turns(aligned, diar_df)
                    how = "word"
                except Exception:  # noqa: BLE001 — fall back below
                    turns = []
            if not turns:  # fallback: coarse segment-level assignment
                turns = _segments_to_turns(segments, diar_df)
                how = "segment"
    except _Timeout:
        return f"SKIPPED (timeout >{MAX_SECONDS_PER_FILE}s): {path.name}"
    finally:
        if clean_tmp:
            clean_tmp.unlink(missing_ok=True)

    turns = [(s, _collapse_repeats(t)) for s, t in turns]   # squash Whisper loops
    turns = [(s, t) for s, t in turns if not _is_hallucination(t)]
    mapping = _map_speakers(turns, diar_df)
    out_path.write_text(_render(turns, mapping), encoding="utf-8")
    return f"ok: {out_path.name}  ({dur:.0f}s, {len(turns)} turns, {how}-level, lang={lang})"


# ----------------------------- batch driver -----------------------------
def _gather(src: Path, limit: int | None) -> list[Path]:
    files = sorted(src.rglob("*.mp3"))
    return files[:limit] if limit else files


def run(files: list[Path], out_dir: Path, model_size: str, gpu_device: str,
        overwrite: bool) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Transcribing {len(files)} recording(s) -> {out_dir}\n")
    models = load_models(model_size, gpu_device)
    t_start = time.time()
    for i, path in enumerate(files, 1):
        t0 = time.time()
        try:
            status = transcribe_file(path, models, out_dir, overwrite)
        except Exception as e:  # noqa: BLE001 — one bad file shouldn't kill the batch
            status = f"FAILED: {path.name} ({type(e).__name__}: {e})"
        elapsed = time.time() - t0
        done = i
        avg = (time.time() - t_start) / done
        eta = avg * (len(files) - done)
        print(f"[{i}/{len(files)}] {status}  [{elapsed:.0f}s, eta {eta/60:.0f}m]")
    print(f"\nDone in {(time.time() - t_start)/60:.1f}m. Transcripts in {out_dir}")


# ----------------------------- parallel driver -----------------------------
# Each worker process loads its own models once (initializer) and pulls files off a
# shared queue. Transcription is CPU-bound, so N workers use the otherwise-idle cores;
# diarization/alignment share the single GPU (brief, so contention is minor).
# RAM is the limit: each worker's stack is ~5GB, so on a 16GB machine keep workers<=2.
_W: dict = {}


def _pool_init(model_size, gpu_device, out_dir, overwrite):
    global _W
    _W = {"models": load_models(model_size, gpu_device),
          "out_dir": Path(out_dir), "overwrite": overwrite}


def _pool_task(path_str):
    p = Path(path_str)
    try:
        return transcribe_file(p, _W["models"], _W["out_dir"], _W["overwrite"])
    except Exception as e:  # noqa: BLE001 — isolate per-file failure
        return f"FAILED: {p.name} ({type(e).__name__}: {e})"


def run_parallel(files: list[Path], out_dir: Path, model_size: str, gpu_device: str,
                 overwrite: bool, workers: int) -> None:
    import multiprocessing as mp
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Transcribing {len(files)} recording(s) with {workers} workers -> {out_dir}\n")
    ctx = mp.get_context("spawn")   # macOS default; re-imports module so torch patch applies
    t_start = time.time()
    with ctx.Pool(workers, initializer=_pool_init,
                  initargs=(model_size, gpu_device, str(out_dir), overwrite)) as pool:
        for i, status in enumerate(pool.imap_unordered(_pool_task, [str(f) for f in files]), 1):
            avg = (time.time() - t_start) / i
            eta = avg * (len(files) - i)
            print(f"[{i}/{len(files)}] {status}  [eta {eta/60:.0f}m]", flush=True)
    print(f"\nDone in {(time.time() - t_start)/60:.1f}m. Transcripts in {out_dir}")


def main() -> None:
    ap = argparse.ArgumentParser(description="mp3 call recordings -> plain-text transcripts")
    ap.add_argument("files", nargs="*", help="specific .mp3 files (default: scan AUDIO_SRC)")
    ap.add_argument("--src", default=str(config.AUDIO_SRC), help="folder of recordings to scan")
    ap.add_argument("--limit", type=int, default=100, help="max recordings when scanning")
    ap.add_argument("--model", default=MODEL_SIZE, help="whisper model size")
    ap.add_argument("--gpu-device", default="auto",
                    help="device for diarization+alignment: auto (mps if available) | mps | cpu")
    ap.add_argument("--workers", type=int, default=1,
                    help="parallel worker processes (16GB RAM -> keep <=2; 1 = sequential)")
    ap.add_argument("--overwrite", action="store_true", help="re-transcribe existing outputs")
    args = ap.parse_args()

    if args.files:
        files = [Path(f) for f in args.files]
    else:
        files = _gather(Path(args.src), args.limit)
    if not files:
        raise SystemExit(f"No .mp3 files found (src={args.src}).")
    if args.workers > 1:
        run_parallel(files, config.AUDIO_TRANSCRIPTS_DIR, args.model, args.gpu_device,
                     args.overwrite, args.workers)
    else:
        run(files, config.AUDIO_TRANSCRIPTS_DIR, args.model, args.gpu_device, args.overwrite)


if __name__ == "__main__":
    main()
