"""Fast offline iteration on turn-assembly using cached model outputs (/tmp/stt_debug.pkl)."""
import pickle
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import transcribe  # noqa: E402

data = pickle.loads(Path("/tmp/stt_debug.pkl").read_bytes())


def overlap_spk(s, e, diar):
    best, bo = None, 0.0
    for r in diar:
        ov = max(0.0, min(e, r["end"]) - max(s, r["start"]))
        if ov > bo:
            bo, best = ov, r["speaker"]
    return best


def words_of(aligned):
    out = []
    for seg in aligned.get("segments", []):
        ws = seg.get("words") or []
        if not ws:
            out.append((seg.get("start"), seg.get("end"), (seg.get("text") or "").strip()))
            continue
        for w in ws:
            tok = (w.get("word") or "").strip()
            if tok:
                out.append((w.get("start"), w.get("end"), tok))
    return out


def medfilt(seq, w):
    out = list(seq)
    n = len(seq)
    for i in range(n):
        win = seq[max(0, i - w):min(n, i + w + 1)]
        out[i] = max(set(win), key=win.count)
    return out


def assign_turns(aligned, diar, max_word_dur=1.5, med_w=2, min_run=3):
    words = words_of(aligned)
    # 1. per-word speaker; unreliable (no time / stretched English) -> None
    raw = []
    for s, e, tok in words:
        spk = None if (s is None or e is None or (e - s) > max_word_dur) else overlap_spk(s, e, diar)
        raw.append([spk, tok])
    # 2. carry-forward then backward to fill None
    last = None
    for r in raw:
        if r[0] is None:
            r[0] = last
        else:
            last = r[0]
    nxt = None
    for r in reversed(raw):
        if r[0] is None:
            r[0] = nxt
        else:
            nxt = r[0]
    seq = [r[0] or "SPEAKER_00" for r in raw]
    # 3. median filter to kill isolated single-word flips
    seq = medfilt(seq, med_w)
    # 4. min-run: relabel runs shorter than min_run to the previous speaker
    i = 0
    while i < len(seq):
        j = i
        while j < len(seq) and seq[j] == seq[i]:
            j += 1
        if i > 0 and (j - i) < min_run:
            for k in range(i, j):
                seq[k] = seq[i - 1]
        i = j
    seq = medfilt(seq, med_w)  # one more pass to merge after relabel
    # 5. group into turns
    turns = []
    for spk, (_, tok) in zip(seq, raw):
        if turns and turns[-1][0] == spk:
            turns[-1] = (spk, f"{turns[-1][1]} {tok}")
        else:
            turns.append((spk, tok))
    return [(s, t) for s, t in turns if not transcribe._is_hallucination(t)]


import os
MW = int(os.environ.get("MW", "1"))
MR = int(os.environ.get("MR", "2"))
print(f"### params: med_w={MW} min_run={MR}\n")
for name, d in data.items():
    diar = d["diar"]
    turns = assign_turns(d["aligned"], diar, med_w=MW, min_run=MR)
    mapping = transcribe._map_speakers(turns, type("D", (), {"itertuples": lambda self: (type("R", (), r)() for r in diar)})())
    # simpler mapping: build from diar dict directly
    talk = {}
    for r in diar:
        talk[r["speaker"]] = talk.get(r["speaker"], 0.0) + (r["end"] - r["start"])
    hits = {}
    for spk, txt in turns:
        low = txt.lower()
        hits[spk] = hits.get(spk, 0) + sum(1 for m in transcribe._AGENT_MARKERS if m in low)
    spks = list(dict.fromkeys(s for s, _ in turns))
    agent = max(spks, key=lambda s: (hits.get(s, 0), talk.get(s, 0.0))) if spks else None
    mp = {s: ("Agent" if s == agent else "Customer") for s in spks}
    print("=" * 70)
    print(f"{name}  ({len(turns)} turns)")
    for spk, txt in turns:
        print(f"{mp[spk]}: {txt}")
    print()
