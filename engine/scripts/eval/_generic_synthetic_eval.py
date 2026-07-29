"""Does offline-generated synthetic multi-domain diversity close the cross-client
generalization gap found in scripts/_generic_prototype_eval.py (18-32% no matter the
classifier, with zero real data from the target domain)?

Compares, scored on REAL ABCL and REAL JustDial turns, with ZERO real data from
either domain used in training (the true "brand new client" simulation):
  baseline  centroid on src/generic_taxonomy.py hand-written anchors only (28 phrases,
            1 register — this is what scripts/_generic_prototype_eval.py's v4 measured)
  synth     centroid on hand-written + src/synthetic_anchors.py (5 extra domains,
            ~155 more phrases, still zero ABCL/JustDial data)
  synth_lr  logistic regression trained on the same synthetic-only pool

    python -m scripts._generic_synthetic_eval
"""
from __future__ import annotations

import numpy as np

from src.distill import DOMAINS, load_dataset, featurize, _make_clf, _embed
from src.generic_taxonomy import INTENT_LIBRARY
from src.synthetic_anchors import SYNTHETIC_ANCHORS


def _domain_of(call_id: str) -> str:
    return "justdial" if call_id.startswith("LCS-") else "abcl"


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
    f1s = []
    for lab in labels:
        prec = tp[lab] / (tp[lab] + fp[lab]) if (tp[lab] + fp[lab]) else 0.0
        rec = tp[lab] / (tp[lab] + fn[lab]) if (tp[lab] + fn[lab]) else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
        f1s.append(f1)
    return n, (correct / n if n else 0.0), (sum(f1s) / len(f1s) if f1s else 0.0)


def centroid_classify(train_emb, train_y, test_emb):
    labels = sorted(set(train_y))
    cents = np.stack([train_emb[[i for i, y in enumerate(train_y) if y == lab]].mean(axis=0)
                      for lab in labels])
    cents = cents / np.linalg.norm(cents, axis=1, keepdims=True)
    sims = test_emb @ cents.T
    idx = sims.argmax(axis=1)
    return [labels[i] for i in idx]


def run():
    from sentence_transformers import SentenceTransformer
    from src.extract import EMBED_MODEL
    model = SentenceTransformer(EMBED_MODEL)

    hand_texts = [ex for name, _, exs in INTENT_LIBRARY for ex in exs]
    hand_labels = [name for name, _, exs in INTENT_LIBRARY for ex in exs]
    synth_texts = [p for _, _, p in SYNTHETIC_ANCHORS]
    synth_labels = [b for _, b, _ in SYNTHETIC_ANCHORS]

    hand_emb = _embed(hand_texts, model)
    combo_emb = _embed(hand_texts + synth_texts, model)
    combo_labels = hand_labels + synth_labels
    print(f"hand-written anchors: {len(hand_texts)}  |  hand+synthetic: {len(hand_texts) + len(synth_texts)}")

    lr = _make_clf()
    d = model.get_sentence_embedding_dimension()
    lr.fit(combo_emb, combo_labels)

    samples = load_dataset(DOMAINS["generic"]["gold"])
    for s in samples:
        s["domain"] = _domain_of(s["call_id"])

    for dom in ("abcl", "justdial"):
        test = [s for s in samples if s["domain"] == dom]
        Xte_full, yte_all, _ = featurize(test, model)
        Xte_cur = Xte_full[:, :d]

        print(f"\n### test={dom} ({len(test)} turns) ###")

        keep = [i for i, y in enumerate(yte_all) if y in set(hand_labels)]
        yte = [yte_all[i] for i in keep]
        pred_base = centroid_classify(hand_emb, hand_labels, Xte_cur[keep])
        n, acc, f1 = _score(yte, pred_base)
        print(f"  baseline  centroid, hand-written only ({len(hand_texts)} phrases)   "
              f"n={n}  acc={acc:.3f}  macro-F1={f1:.3f}")

        keep2 = [i for i, y in enumerate(yte_all) if y in set(combo_labels)]
        yte2 = [yte_all[i] for i in keep2]
        pred_synth = centroid_classify(combo_emb, combo_labels, Xte_cur[keep2])
        n, acc, f1 = _score(yte2, pred_synth)
        print(f"  synth     centroid, hand+synthetic ({len(hand_texts)+len(synth_texts)} phrases)   "
              f"n={n}  acc={acc:.3f}  macro-F1={f1:.3f}")

        pred_lr = list(lr.predict(Xte_cur[keep2]))
        n, acc, f1 = _score(yte2, pred_lr)
        print(f"  synth_lr  logreg, hand+synthetic                              "
              f"n={n}  acc={acc:.3f}  macro-F1={f1:.3f}")


if __name__ == "__main__":
    run()
