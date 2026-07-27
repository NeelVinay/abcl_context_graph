"""Diagnose keyword coverage on the STT transcripts: how many curated phrases match,
and what salient terms a data-driven extractor would surface."""
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import extract as E

files = sorted(Path("data/audio_transcripts").glob("*.txt"))
all_text = []
turns_total = 0
for f in files:
    turns = E._load_turns(f)
    turns_total += len(turns)
    all_text.extend(t["text"] for t in turns)
corpus = "\n".join(all_text).lower()
print(f"{len(files)} calls, {turns_total} turns, {len(corpus)} chars\n")

# 1) curated-phrase coverage
all_phrases = []
for name, kws, _ in E.INTENT_LIBRARY:
    all_phrases += kws
hits = [p for p in all_phrases if p.lower() in corpus]
print(f"curated INTENT phrases: {len(all_phrases)} total, {len(hits)} appear at all")
print("  matched:", ", ".join(sorted(set(hits))) or "(none)")
print()

# 2) what salient terms actually dominate (data-driven candidate keywords)
toks = re.findall(r"[a-zA-Zऀ-ॿ]+", corpus)
cand = [w for w in toks if len(w) >= 3 and w not in E._FILLERS]
top = Counter(cand).most_common(40)
print("top 40 frequent content tokens (candidate keywords):")
print("  " + ", ".join(f"{w}({c})" for w, c in top))
print()

# 3) bigrams
words = [w for w in toks if w not in E._FILLERS]
bigrams = Counter(zip(words, words[1:]))
print("top 20 bigrams:")
print("  " + ", ".join(f"{a} {b}({c})" for (a, b), c in bigrams.most_common(20)))
print()

# 4) PROTOTYPE: corpus-driven vocab — terms in >=2 calls, not stopwords (PII-safe)
from src.stopwords import STOPWORDS  # noqa: E402
STOP = E._FILLERS | STOPWORDS
df = Counter()
for f in files:
    seen = {w for t in E._load_turns(f) for w in re.findall(r"[a-zA-Zऀ-ॿ]+", t["text"].lower())
            if len(w) >= 3 and w not in STOP}
    df.update(seen)
vocab = {w: d for w, d in df.items() if d >= 2}
ranked = sorted(vocab.items(), key=lambda x: -x[1])
print(f"corpus vocab (>=2 calls, stopword-filtered): {len(vocab)} terms")
print("  " + ", ".join(f"{w}({d})" for w, d in ranked[:45]))
