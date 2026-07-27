"""Does a bigger/better multilingual embedding model close the cross-client gap,
without any per-client labeled data?

Current model: paraphrase-multilingual-MiniLM-L12-v2 (118M params, 2020-era).
Candidates tested here:
  - paraphrase-multilingual-mpnet-base-v2  (278M, same family, known upgrade)
  - intfloat/multilingual-e5-base          (278M, modern, different architecture;
                                             uses "query: " prefix per its model card)

Same honest test as scripts/_generic_holdout_eval.py: train on ONE real domain
(logreg, current-turn embedding only — the best-performing local config found so
far), test on the domain never seen in training. If a bigger embedder captures
"agree"/"greeting"/etc. as abstract concepts rather than domain vocabulary, this
should show up as a real accuracy jump here, at ZERO per-client labeled data.

    python -m scripts._generic_embed_model_eval
"""
from __future__ import annotations

from collections import Counter

from src.distill import DOMAINS, load_dataset, _make_clf


def _domain_of(call_id: str) -> str:
    return "justdial" if call_id.startswith("LCS-") else "abcl"


def _score(y_true, y_pred):
    n = len(y_true)
    correct = sum(t == p for t, p in zip(y_true, y_pred))
    labels = set(y_true) | set(y_pred)
    tp, fp, fn = Counter(), Counter(), Counter()
    for t, p in zip(y_true, y_pred):
        if t == p:
            tp[t] += 1
        else:
            fp[p] += 1
            fn[t] += 1
    f1s = []
    for lab in labels:
        prec = tp[lab] / (tp[lab] + fp[lab]) if (tp[lab] + fp[lab]) else 0.0
        rec = tp[lab] / (tp[lab] + fn[lab]) if (tp[lab] + fn[lab]) else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
        f1s.append(f1)
    return n, (correct / n if n else 0.0), (sum(f1s) / len(f1s) if f1s else 0.0)


MODELS = [
    ("current: paraphrase-multilingual-MiniLM-L12-v2", "paraphrase-multilingual-MiniLM-L12-v2", ""),
    ("bigger:  paraphrase-multilingual-mpnet-base-v2", "paraphrase-multilingual-mpnet-base-v2", ""),
    ("modern:  intfloat/multilingual-e5-base", "intfloat/multilingual-e5-base", "query: "),
]


def run():
    from sentence_transformers import SentenceTransformer

    samples = load_dataset(DOMAINS["generic"]["gold"])
    for s in samples:
        s["domain"] = _domain_of(s["call_id"])

    for label, model_name, prefix in MODELS:
        print(f"\n########## {label} ##########")
        print("loading model (first use downloads it) ...")
        model = SentenceTransformer(model_name)
        texts = [prefix + s["text"] for s in samples]
        emb = model.encode(texts, normalize_embeddings=True, batch_size=32, show_progress_bar=False)
        for i, s in enumerate(samples):
            s["_emb"] = emb[i]

        for train_dom, test_dom in [("abcl", "justdial"), ("justdial", "abcl")]:
            train = [s for s in samples if s["domain"] == train_dom]
            test = [s for s in samples if s["domain"] == test_dom]
            import numpy as np
            Xtr = np.stack([s["_emb"] for s in train])
            ytr = [s["label"] for s in train]
            Xte_all = np.stack([s["_emb"] for s in test])
            yte_all = [s["label"] for s in test]
            keep = [i for i, y in enumerate(yte_all) if y in set(ytr)]
            Xte, yte = Xte_all[keep], [yte_all[i] for i in keep]

            clf = _make_clf()
            clf.fit(Xtr, ytr)
            pred = clf.predict(Xte)
            n, acc, f1 = _score(list(yte), list(pred))
            print(f"  train={train_dom:<9} test={test_dom:<9}  n={n:<5}  "
                  f"acc={acc:.3f}  macro-F1={f1:.3f}")


if __name__ == "__main__":
    run()
