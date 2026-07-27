"""Real cross-client generalization test for the `generic` domain: train on one
source domain's turns, test on the OTHER domain's turns, entirely held out.

Mixed grouped-CV (src/distill.py cv_eval) still splits folds across both domains at
once, so a strong number there could just mean "learned ABCL well and JustDial well
separately" (a domain-aware shortcut), not real generalization. This script answers
the harder, more honest question: does a model that has NEVER seen domain B's calls
still classify domain B's broad-bucket turns well?

    python -m scripts._generic_holdout_eval
"""
from __future__ import annotations

import numpy as np

import config
from src.distill import DOMAINS, featurize, _make_clf, embed_prefix_for
from src.distill import load_dataset


def _domain_of(call_id: str) -> str:
    if call_id.startswith("LCS-"):
        return "justdial"
    if call_id.startswith("GEN-myntra"):
        return "myntra"
    return "abcl"


def _score(y_true, y_pred):
    from collections import Counter
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
    f1s, per_class = [], {}
    for lab in labels:
        prec = tp[lab] / (tp[lab] + fp[lab]) if (tp[lab] + fp[lab]) else 0.0
        rec = tp[lab] / (tp[lab] + fn[lab]) if (tp[lab] + fn[lab]) else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
        f1s.append(f1)
        per_class[lab] = (prec, rec, f1, tp[lab] + fn[lab])
    return {"n": n, "accuracy": correct / n if n else 0.0,
            "macro_f1": sum(f1s) / len(f1s) if f1s else 0.0, "per_class": per_class}


def run():
    from sentence_transformers import SentenceTransformer
    embed_model = DOMAINS["generic"]["embed_model"]
    prefix = embed_prefix_for(embed_model)
    print(f"embed_model={embed_model}  prefix={prefix!r}")
    gold_path = DOMAINS["generic"]["gold"]
    samples = load_dataset(gold_path)
    for s in samples:
        s["domain"] = _domain_of(s["call_id"])

    model = SentenceTransformer(embed_model)
    pairs = [
        ("abcl", "justdial"), ("justdial", "abcl"),
        # the real question: zero Myntra data in training (the "before" case) vs.
        # a model that's actually seen Myntra (measured separately by
        # `python -m src.distill eval generic`, which mixes all 3 domains in CV).
        ("abcl+justdial", "myntra"), ("myntra", "abcl+justdial"),
        # leave-one-domain-out: simulates "a 4th client we've never seen at all",
        # using 2 known domains' diversity as the only training signal.
        ("justdial+myntra", "abcl"), ("abcl+myntra", "justdial"),
    ]
    for train_dom, test_dom in pairs:
        train_doms = train_dom.split("+")
        test_doms = test_dom.split("+")
        train = [s for s in samples if s["domain"] in train_doms]
        test = [s for s in samples if s["domain"] in test_doms]
        Xtr, ytr, _ = featurize(train, model, prefix)
        Xte, yte, _ = featurize(test, model, prefix)
        # only score classes the training domain actually saw examples of
        train_classes = set(ytr)
        keep = [i for i, y in enumerate(yte) if y in train_classes]
        if len(keep) < len(yte):
            print(f"[{train_dom} -> {test_dom}] dropping {len(yte) - len(keep)} test rows "
                  f"whose label never appeared in {train_dom} training data "
                  f"({sorted(set(yte) - train_classes)})")
        Xte, yte = Xte[keep], yte[keep]

        clf = _make_clf()
        clf.fit(Xtr, ytr)
        ypred = clf.predict(Xte)
        s = _score(list(yte), list(ypred))
        print(f"\n===== train={train_dom} ({len(train)} turns) "
              f"-> test={test_dom} ({s['n']} scorable turns) =====")
        print(f"accuracy={s['accuracy']:.3f}  macro-F1={s['macro_f1']:.3f}")
        for lab, (p, r, f1, n) in sorted(s["per_class"].items(), key=lambda x: x[1][2]):
            print(f"  {f1:.2f} F1  (p={p:.2f} r={r:.2f}, n={n:>4})  {lab}")


if __name__ == "__main__":
    run()
