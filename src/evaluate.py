"""Metrics harness: score predicted base-intents + keywords against the gold labels.

Gold = Claude's labels (data/gold/labels.jsonl). Predictions can come from:
  - the current local extractor (cached base_intent)      -> baseline
  - the distilled student model                            -> after training
Same comparison either way, so improvements are measurable, not guessed.

Usage:
  python -m src.evaluate baseline   # score the current cache predictions vs gold
  python -m src.evaluate suggest    # dump the 'other' suggested_intents (Phase 4)
"""
from __future__ import annotations

import json
from collections import Counter, defaultdict

import config

GOLD_PATH = config.CACHE_DIR.parent / "gold" / "labels.jsonl"


def load_gold(path=None) -> dict:
    rows = {}
    for line in (path or GOLD_PATH).read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        rows[(r["call_id"], r["index"])] = r
    return rows


def load_cache_predictions() -> dict:
    """The current local extractor's base_intent per turn (the baseline)."""
    preds = {}
    for f in config.CACHE_DIR.glob("*.json"):
        c = json.loads(f.read_text())
        for t in c["turns"]:
            preds[(c["call_id"], t["index"])] = {
                "base_intent": t.get("base_intent"),
                "keywords": t.get("keywords", []),
            }
    return preds


def score_intents(gold: dict, pred: dict) -> dict:
    keys = [k for k in gold if k in pred]
    y_true = [gold[k]["base_intent"] for k in keys]
    y_pred = [pred[k]["base_intent"] for k in keys]
    n = len(keys)
    correct = sum(t == p for t, p in zip(y_true, y_pred))

    # per-class P/R/F1 (macro)
    labels = set(y_true) | set(y_pred)
    tp = Counter(); fp = Counter(); fn = Counter()
    for t, p in zip(y_true, y_pred):
        if t == p:
            tp[t] += 1
        else:
            fp[p] += 1; fn[t] += 1
    f1s = []
    per_class = {}
    for lab in labels:
        prec = tp[lab] / (tp[lab] + fp[lab]) if (tp[lab] + fp[lab]) else 0.0
        rec = tp[lab] / (tp[lab] + fn[lab]) if (tp[lab] + fn[lab]) else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
        f1s.append(f1)
        per_class[lab] = (prec, rec, f1, tp[lab] + fn[lab])
    macro_f1 = sum(f1s) / len(f1s) if f1s else 0.0

    # top confusions
    conf = Counter()
    for t, p in zip(y_true, y_pred):
        if t != p:
            conf[(t, p)] += 1

    return {"n": n, "accuracy": correct / n if n else 0.0, "macro_f1": macro_f1,
            "per_class": per_class, "confusions": conf.most_common(15)}


def score_keywords(gold: dict, pred: dict) -> dict:
    """Token-level precision/recall of predicted keywords vs gold keywords."""
    keys = [k for k in gold if k in pred]
    tp = fp = fn = 0
    covered = 0  # turns where we predicted >=1 keyword that gold also has
    gold_nonempty = 0
    for k in keys:
        g = {w.lower() for kw in gold[k]["keywords"] for w in kw.split()}
        p = {w.lower() for kw in pred[k]["keywords"] for w in kw.split()}
        tp += len(g & p); fp += len(p - g); fn += len(g - p)
        if g:
            gold_nonempty += 1
            if g & p:
                covered += 1
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn) if (tp + fn) else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0.0
    return {"precision": prec, "recall": rec, "f1": f1,
            "turn_coverage": covered / gold_nonempty if gold_nonempty else 0.0}


def print_report(tag: str, gold: dict, pred: dict) -> None:
    si = score_intents(gold, pred)
    sk = score_keywords(gold, pred)
    print(f"\n===== {tag} =====")
    print(f"turns scored: {si['n']}")
    print(f"INTENT  accuracy={si['accuracy']:.3f}  macro-F1={si['macro_f1']:.3f}")
    print(f"KEYWORD precision={sk['precision']:.3f} recall={sk['recall']:.3f} "
          f"f1={sk['f1']:.3f}  turn-coverage={sk['turn_coverage']:.3f}")
    print("\nworst intents (by F1, with >=10 gold examples):")
    worst = sorted([(lab, *v) for lab, v in si["per_class"].items() if v[3] >= 10],
                   key=lambda x: x[3])  # x[3]=f1
    for lab, prec, rec, f1, n in sorted(worst, key=lambda x: x[3])[:12]:
        print(f"  {f1:.2f} F1  (p={prec:.2f} r={rec:.2f}, n={n:>4})  {lab}")
    print("\ntop confusions (gold -> predicted):")
    for (t, p), c in si["confusions"][:10]:
        print(f"  {c:>3}x  {t}  ->  {p}")


def dump_suggestions() -> None:
    gold = load_gold()
    sugg = Counter()
    for r in gold.values():
        if r["base_intent"] == "other" and r.get("suggested_intent"):
            sugg[r["suggested_intent"]] += 1
    print(f"{sum(sugg.values())} 'other' turns -> {len(sugg)} suggested new intents:\n")
    for name, c in sugg.most_common():
        print(f"  {c:>3}x  {name}")


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "baseline"
    if cmd == "baseline":
        g = load_gold()
        print_report("BASELINE: current local extractor vs Claude gold",
                     g, load_cache_predictions())
    elif cmd == "suggest":
        dump_suggestions()
