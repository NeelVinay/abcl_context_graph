"""Measure the cost of dropping diarization (speaker-from-audio) in favour of
speaker-from-text. Three grouped-CV numbers on the JustDial coarse gold:
  1. intent accuracy WITH the speaker feature (current pipeline)
  2. intent accuracy WITHOUT the speaker feature (what we'd have if diarization is gone)
  3. speaker (agent/customer) accuracy predicted FROM TEXT+context (the replacement)
"""
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.model_selection import GroupKFold  # noqa: E402
from sentence_transformers import SentenceTransformer  # noqa: E402

import config  # noqa: E402
from src.distill import load_dataset  # noqa: E402
from src.extract import EMBED_MODEL  # noqa: E402

GOLD = config.DATA / "gold_justdial" / "labels_coarse.jsonl"

print("loading dataset + embedding model ...", flush=True)
samples = load_dataset(GOLD)
model = SentenceTransformer(EMBED_MODEL)
cur = np.asarray(model.encode([s["text"] for s in samples], normalize_embeddings=True, batch_size=64))
prev = np.asarray(model.encode([s["prev_text"] or "" for s in samples], normalize_embeddings=True, batch_size=64))
spk = np.array([[1.0 if s["speaker"] == "agent" else 0.0] for s in samples])
pos = np.array([[s["pos"]] for s in samples])
y_intent = np.array([s["label"] for s in samples])
y_speaker = np.array([s["speaker"] for s in samples])
groups = np.array([s["call_id"] for s in samples])
print(f"{len(samples)} turns, {len(set(y_intent))} intents, "
      f"speaker split: {dict(zip(*np.unique(y_speaker, return_counts=True)))}", flush=True)


def cv_acc(X, y):
    gkf = GroupKFold(n_splits=5)
    correct = total = 0
    for tr, te in gkf.split(X, y, groups):
        clf = LogisticRegression(max_iter=2000, C=10.0, class_weight="balanced")
        clf.fit(X[tr], y[tr])
        p = clf.predict(X[te])
        correct += (p == y[te]).sum()
        total += len(te)
    return correct / total


X_with = np.hstack([cur, prev, spk, pos])          # current: text + context + SPEAKER
X_without = np.hstack([cur, prev, pos])             # no speaker input
X_speaker = np.hstack([cur, prev, pos])             # predict speaker from text+context

acc_intent_with = cv_acc(X_with, y_intent)
acc_intent_without = cv_acc(X_without, y_intent)
acc_speaker = cv_acc(X_speaker, y_speaker)

print("\n================ RESULTS (5-fold grouped CV) ================", flush=True)
print(f"1. Intent accuracy WITH speaker feature (current):  {acc_intent_with:.3f}", flush=True)
print(f"2. Intent accuracy WITHOUT speaker feature:         {acc_intent_without:.3f}", flush=True)
print(f"   -> intent accuracy lost by dropping diarization: {acc_intent_with-acc_intent_without:+.3f}", flush=True)
print(f"3. Speaker (agent/customer) accuracy FROM TEXT:     {acc_speaker:.3f}", flush=True)
# majority-class baseline for speaker (how hard is the speaker task?)
maj = max(np.unique(y_speaker, return_counts=True)[1]) / len(y_speaker)
print(f"   (speaker majority-class baseline:                {maj:.3f})", flush=True)
