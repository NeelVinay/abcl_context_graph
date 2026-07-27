"""Bootstrap data/gold_generic/labels.jsonl from ALREADY Claude-labeled ABCL +
JustDial gold, at zero new labeling cost.

We don't need a new client to start testing the generic (broad-bucket) model —
data/gold/labels.jsonl (ABCL, 6k+ turns) and data/gold_justdial/labels.jsonl
(JustDial, ~1k turns) are real Claude-quality labels sitting on disk already. Every
row whose fine base_intent has a clean 1:1 generic-bucket match (see
src/generic_taxonomy.ABCL_FINE_TO_GENERIC / JUSTDIAL_FINE_TO_GENERIC) is recoded and
kept; everything else (client-specific procedural steps like enter_pan, raise_request,
processing_fee ...) is dropped rather than dumped into "other".

    python -m src.generic_bootstrap

This does NOT cover every generic bucket — see the module docstring in
src/generic_taxonomy.py for which 4 buckets have zero coverage until a targeted
Claude pass or a real new client fills them in.
"""
from __future__ import annotations

import json
from collections import Counter

import config
from src.generic_taxonomy import ABCL_FINE_TO_GENERIC, JUSTDIAL_FINE_TO_GENERIC

OUT_PATH = config.DATA / "gold_generic" / "labels.jsonl"

SOURCES = [
    ("abcl", config.DATA / "gold" / "labels.jsonl", ABCL_FINE_TO_GENERIC),
    ("justdial", config.DATA / "gold_justdial" / "labels.jsonl", JUSTDIAL_FINE_TO_GENERIC),
]

# irate_frustrated has no clean fine-intent equivalent in either taxonomy — it's a
# SENTIMENT, not an intent, in the original gold. Any customer turn gold already
# marked sentiment=="frustrated" is real signal for this bucket regardless of its
# fine base_intent. Applied AFTER the fine->generic mapping (so it can ADD rows the
# mapping dropped) but BEFORE MANUAL_LABELS (so a hand-verified label always wins —
# e.g. a turn that's frustrated in tone but whose primary content is "the right
# person isn't available" should keep that label, not get overwritten here).
FRUSTRATED_BUCKET = "irate_frustrated"

# Hand-verified real turns for the 3 buckets that got ZERO rows from the fine->generic
# mapping (disagree, callback_request, person_unavailable have no matching fine
# intent in either taxonomy). Found via scripts/_mine_missing_bucket_candidates.py and
# src/dispositions.py's not_interested/callback_requested-tagged calls, then read and
# labeled by hand (Claude, offline) — the same "teacher" role Claude plays for the
# full batch-labeling workflow, just done directly for this small, targeted gap
# instead of a full batch pass. call_id/index must match an existing data/cache/*.json
# turn for src.distill.load_dataset to pick these up.
MANUAL_LABELS = [
    # --- disagree: real ABCL decline turns (fine taxonomy has no "disagree" intent) ---
    ("66f076f7-1147-4c57-b88c-7f8e7fa1604d-transcript", 3, "disagree",
     ["नहीं मुझे loan नहीं चाहिए"], "neutral"),
    ("94446627-ae27-4892-88e8-48a11a04acc4-transcript", 2, "disagree",
     ["phone ही मत करो", "मदद नहीं चाहिए"], "frustrated"),
    ("94446627-ae27-4892-88e8-48a11a04acc4-transcript", 4, "disagree",
     ["हमको नहीं चाहिए", "phone मत करो"], "frustrated"),
    ("963f1b24-a8c5-4190-a715-471fba82499c-transcript", 2, "disagree", ["No"], "neutral"),
    ("996c0786-7fc3-4133-99c0-97a61c3a9689-transcript", 2, "disagree", ["नहीं"], "neutral"),
    ("996c0786-7fc3-4133-99c0-97a61c3a9689-transcript", 4, "disagree", ["No"], "neutral"),
    # --- callback_request: real "busy right now / call me later" turns ---
    ("9b48167b-2ef8-4566-accd-1893c06aa579-transcript", 10, "callback_request",
     ["अभी time नहीं है"], "neutral"),
    ("ec29250d-d35a-46bf-b4fc-a77cf1e5de16-transcript", 11, "callback_request",
     ["बाद में call करता हूं"], "neutral"),
    # --- person_unavailable: rare in this dataset (outbound calls mostly reach the
    # target directly) — only one clean real example found; relies more heavily on
    # src/synthetic_anchors.py until a new client's data adds real coverage.
    ("78dbd7a8", 60, "person_unavailable", ["manager", "Line पर busy"], "frustrated"),
]


def _load(path):
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text().splitlines() if l.strip()]


def bootstrap() -> tuple[int, dict]:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rows_by_key: dict = {}
    stats = {}
    for domain, path, mapping in SOURCES:
        rows = _load(path)
        kept, dropped, frustrated_added = Counter(), 0, 0
        for r in rows:
            key = (r["call_id"], r["index"])
            bucket = mapping.get(r["base_intent"])
            if bucket is None:
                dropped += 1
            else:
                kept[bucket] += 1
                rows_by_key[key] = {**r, "base_intent": bucket, "_source_domain": domain,
                                    "_source_intent": r["base_intent"]}
            if r.get("sentiment") == "frustrated":
                if key not in rows_by_key:
                    frustrated_added += 1
                rows_by_key[key] = {**r, "base_intent": FRUSTRATED_BUCKET,
                                    "_source_domain": domain, "_source_intent": r["base_intent"]}
        stats[domain] = {"total": len(rows), "kept": sum(kept.values()), "dropped": dropped,
                         "by_bucket": dict(kept), "frustrated_added": frustrated_added}

    manual = 0
    for call_id, index, bucket, keywords, sentiment in MANUAL_LABELS:
        rows_by_key[(call_id, index)] = {
            "call_id": call_id, "index": index, "speaker": "customer",
            "base_intent": bucket, "keywords": keywords, "sentiment": sentiment,
            "tool": None, "_source_domain": "abcl", "_source_intent": "_manual",
        }
        manual += 1
    stats["manual"] = manual

    kept_rows = list(rows_by_key.values())
    OUT_PATH.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in kept_rows))
    return len(kept_rows), stats


if __name__ == "__main__":
    n, stats = bootstrap()
    print(f"Wrote {n} rows -> {OUT_PATH}\n")
    all_buckets = Counter()
    for domain, s in stats.items():
        if domain == "manual":
            print(f"[manual] {s} hand-verified rows added "
                  f"(disagree/callback_request/person_unavailable)")
            continue
        print(f"[{domain}] {s['total']} gold rows -> kept {s['kept']}, dropped {s['dropped']} "
              f"(no generic-bucket match), +{s['frustrated_added']} added via "
              f"sentiment==frustrated -> {FRUSTRATED_BUCKET}")
        for b, c in sorted(s["by_bucket"].items(), key=lambda x: -x[1]):
            print(f"    {c:>5}  {b}")
        all_buckets.update(s["by_bucket"])
    # frustrated + manual rows aren't in by_bucket above; recount from the actual file
    all_buckets = Counter()
    for line in OUT_PATH.read_text().splitlines():
        if line.strip():
            all_buckets[json.loads(line)["base_intent"]] += 1
    print("\nCombined bucket coverage:")
    for b, c in sorted(all_buckets.items(), key=lambda x: -x[1]):
        print(f"  {c:>5}  {b}")
    from src.generic_taxonomy import INTENT_LIBRARY
    zero = [name for name, _, _ in INTENT_LIBRARY if name not in all_buckets]
    if zero:
        print(f"\nZero coverage (need a targeted Claude pass or a new client): {zero}")
