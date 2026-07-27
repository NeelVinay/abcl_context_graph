"""Diagnose why a call collapses to few turns: is it diarization (audio) or our smoothing?"""
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import transcribe as T  # applies torch.load patch

F = sys.argv[1]
m = T.load_models()
wx = m["whisperx"]
audio = wx.load_audio(F)
dur = len(audio) / 16000.0
res = m["asr"].transcribe(audio, batch_size=4)
segs = [s for s in res["segments"] if not T._is_hallucination((s.get("text") or "").strip())]
diar = m["diar"](audio, min_speakers=1, max_speakers=2)

print(f"\n=== {Path(F).name}  ({dur:.0f}s audio) ===")
print(f"whisper segments (post-hallucination-filter): {len(segs)}")
# diarization speaker distribution
talk = {}
for r in diar.itertuples():
    talk[r.speaker] = talk.get(r.speaker, 0.0) + (r.end - r.start)
print(f"diarization: {len(diar)} segments, speakers found: {sorted(talk)}")
for spk, t in sorted(talk.items()):
    print(f"   {spk}: {t:.1f}s talk-time ({100*t/sum(talk.values()):.0f}%)")

# per-word RAW speaker (before smoothing)
aligned = wx.align(segs, m["align_model"], m["align_meta"], audio, m.get("align_dev", "cpu"),
                   return_char_alignments=False)
raw = []
for seg in aligned.get("segments", []):
    for w in (seg.get("words") or []):
        s, e = w.get("start"), w.get("end")
        if s is not None and e is not None and (e - s) <= T.MAX_WORD_DUR:
            raw.append(T._speaker_by_overlap(s, e, diar))
print(f"\nRAW per-word speaker counts (before smoothing): {Counter(x for x in raw if x)}")
turns = T._aligned_to_turns(aligned, diar)
print(f"AFTER smoothing -> {len(turns)} turns: {Counter(s for s, _ in turns)}")
