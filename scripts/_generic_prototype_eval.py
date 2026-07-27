"""Diagnose WHY logistic regression collapses cross-domain (18-25% train-abcl-test-jd
and vice versa, vs 71% mixed-CV) and test whether a different local approach closes
the gap — still 100% local at inference, still zero Claude at runtime.

Hypothesis: logistic regression on [cur_embed, prev_embed, speaker, position] partly
learns a domain fingerprint (prev_text and position are heavily flow-specific — ABCL's
"position 0.3" means something totally different from JustDial's), which is a shortcut
that vanishes on a genuinely unseen domain. Two things to isolate:
  (A) drop prev_text/position, keep ONLY the current-turn embedding
  (B) swap the learned linear classifier for a nearest-centroid / prototype classifier
      on that embedding — can't overfit a domain-specific decision boundary the way a
      trained linear model can

Variants compared, all scored on the SAME honest cross-domain splits:
  v1  logreg,   cur+prev+speaker+pos   (baseline, already run in dev conversation)
  v2  logreg,   cur only
  v3  centroid, cur only               (trained on real transcripts from ONE domain)
  v4  centroid, cur only, HAND-WRITTEN ANCHORS ONLY (zero real transcript data at all
      — the src/generic_taxonomy.py example utterances, expandable via offline Claude
      augmentation later)

    python -m scripts._generic_prototype_eval
"""
from __future__ import annotations

import numpy as np

from src.distill import DOMAINS, load_dataset, featurize, _make_clf, _embed
from src.generic_taxonomy import INTENT_LIBRARY


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

    samples = load_dataset(DOMAINS["generic"]["gold"])
    for s in samples:
        s["domain"] = _domain_of(s["call_id"])

    for train_dom, test_dom in [("abcl", "justdial"), ("justdial", "abcl")]:
        train = [s for s in samples if s["domain"] == train_dom]
        test = [s for s in samples if s["domain"] == test_dom]

        Xtr_full, ytr, _ = featurize(train, model)
        Xte_full, yte_all, _ = featurize(test, model)
        keep = [i for i, y in enumerate(yte_all) if y in set(ytr)]
        dropped_labels = sorted(set(yte_all) - set(ytr))
        Xte_full, yte = Xte_full[keep], yte_all[keep]

        print(f"\n### train={train_dom} ({len(train)}) -> test={test_dom} "
              f"({len(yte)} scorable{', dropped '+str(dropped_labels) if dropped_labels else ''}) ###")

        # v1: logreg, full features (reference — matches earlier run)
        clf = _make_clf(); clf.fit(Xtr_full, ytr)
        n, acc, f1 = _score(list(yte), list(clf.predict(Xte_full)))
        print(f"  v1 logreg  cur+prev+spk+pos        n={n}  acc={acc:.3f}  macro-F1={f1:.3f}")

        # cur-only embeddings (first 384 dims of the stacked feature = cur embedding)
        d = model.get_sentence_embedding_dimension()
        Xtr_cur, Xte_cur = Xtr_full[:, :d], Xte_full[:, :d]

        # v2: logreg, cur-only
        clf2 = _make_clf(); clf2.fit(Xtr_cur, ytr)
        n, acc, f1 = _score(list(yte), list(clf2.predict(Xte_cur)))
        print(f"  v2 logreg  cur-only                n={n}  acc={acc:.3f}  macro-F1={f1:.3f}")

        # v3: centroid, cur-only, real transcripts from train domain
        pred3 = centroid_classify(Xtr_cur, list(ytr), Xte_cur)
        n, acc, f1 = _score(list(yte), pred3)
        print(f"  v3 centroid cur-only (real data)   n={n}  acc={acc:.3f}  macro-F1={f1:.3f}")

    # v4: centroid, hand-written anchors ONLY (zero real transcript data at all),
    # scored against BOTH domains' full turn sets — the true zero-shot-per-client case.
    anchor_texts, anchor_labels = [], []
    for name, _, examples in INTENT_LIBRARY:
        for ex in examples:
            anchor_texts.append(ex)
            anchor_labels.append(name)
    anchor_emb = _embed(anchor_texts, model)
    print(f"\n### v4: centroid, HAND-WRITTEN ANCHORS ONLY "
          f"({len(anchor_texts)} anchor phrases, {len(set(anchor_labels))} buckets, "
          f"zero real transcript data) ###")
    for dom in ("abcl", "justdial"):
        test = [s for s in samples if s["domain"] == dom]
        Xte_full, yte_all, _ = featurize(test, model)
        d = model.get_sentence_embedding_dimension()
        Xte_cur = Xte_full[:, :d]
        keep = [i for i, y in enumerate(yte_all) if y in set(anchor_labels)]
        dropped_labels = sorted(set(yte_all) - set(anchor_labels))
        Xte_cur, yte = Xte_cur[keep], [yte_all[i] for i in keep]
        pred4 = centroid_classify(anchor_emb, anchor_labels, Xte_cur)
        n, acc, f1 = _score(list(yte), pred4)
        print(f"  test={dom:<10} n={n}  acc={acc:.3f}  macro-F1={f1:.3f}"
              f"{'  dropped '+str(dropped_labels) if dropped_labels else ''}")


if __name__ == "__main__":
    run()
