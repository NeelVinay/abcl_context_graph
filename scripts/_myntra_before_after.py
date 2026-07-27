"""Isolate Myntra-only accuracy inside the grouped CV (some real Myntra calls in
train, held-out Myntra calls in test — the realistic "after adding real data"
scenario) vs the zero-Myntra-data baseline already measured in
scripts/_generic_holdout_eval.py (45.8% / 0.349 macro-F1).

    python -m scripts._myntra_before_after
"""
from __future__ import annotations

from sklearn.model_selection import GroupKFold

from src.distill import DOMAINS, load_dataset, featurize, _make_clf, embed_prefix_for


def _domain_of(call_id: str) -> str:
    if call_id.startswith("LCS-"):
        return "justdial"
    if call_id.startswith("GEN-myntra"):
        return "myntra"
    return "abcl"


def _score(y_true, y_pred):
    n = len(y_true)
    correct = sum(t == p for t, p in zip(y_true, y_pred))
    return n, correct / n if n else 0.0


def run():
    from sentence_transformers import SentenceTransformer
    embed_model = DOMAINS["generic"]["embed_model"]
    prefix = embed_prefix_for(embed_model)
    model = SentenceTransformer(embed_model)

    samples = load_dataset(DOMAINS["generic"]["gold"])
    for s in samples:
        s["domain"] = _domain_of(s["call_id"])
    X, y, groups = featurize(samples, model, prefix)

    gkf = GroupKFold(n_splits=5)
    myntra_true, myntra_pred = [], []
    all_true, all_pred = [], []
    for tr, te in gkf.split(X, y, groups):
        clf = _make_clf()
        clf.fit(X[tr], y[tr])
        pred = clf.predict(X[te])
        all_true += list(y[te]); all_pred += list(pred)
        for i, p in zip(te, pred):
            if samples[i]["domain"] == "myntra":
                myntra_true.append(y[i]); myntra_pred.append(p)

    n, acc = _score(all_true, all_pred)
    print(f"ALL DOMAINS (mixed CV):        n={n:<5} accuracy={acc:.3f}")
    n, acc = _score(myntra_true, myntra_pred)
    print(f"MYNTRA ONLY (held-out calls,")
    print(f"  but model trained WITH some")
    print(f"  real Myntra data):           n={n:<5} accuracy={acc:.3f}")
    print(f"\nvs. zero-Myntra-data baseline (scripts/_generic_holdout_eval.py): "
          f"n=1193  accuracy=0.458")


if __name__ == "__main__":
    run()
