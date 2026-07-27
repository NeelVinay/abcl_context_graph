"""Mine candidate turns for the 3 generic buckets that have zero coverage from the
gold bootstrap and can't be derived from an existing structured field (unlike
irate_frustrated, which comes straight from gold's sentiment=="frustrated"):
  disagree, callback_request, person_unavailable

Scans ALL cached calls (ABCL + JustDial), not just gold rows, since these signals
may have been folded into "other" or a different fine intent during original
labeling. Keyword-filtered candidates still need a human/Claude judgment pass before
being trusted as labels — this script only narrows the haystack.

    python -m scripts._mine_missing_bucket_candidates
"""
from __future__ import annotations

import json

import config

CUES = {
    "disagree": ["nahi chahiye", "nahi karna", "interested nahi", "not interested",
                 "mat karo", "nahi lena", "band karo", "cancel kar do"],
    "callback_request": ["baad mein call", "baad me call", "call back", "abhi busy",
                         "call later", "thodi der baad", "shaam ko call", "kal call"],
    "person_unavailable": ["ghar pe nahi", "abhi available nahi", "so rahe", "meeting mein",
                           "not available right now", "abhi nahi hai", "baad mein available"],
}


def mine():
    seen_calls = set()
    hits = {b: [] for b in CUES}
    for f in sorted(config.CACHE_DIR.glob("*.json")):
        c = json.loads(f.read_text())
        if c["call_id"] in seen_calls:
            continue
        seen_calls.add(c["call_id"])
        for t in c["turns"]:
            if t["speaker"] != "customer":
                continue
            low = t["text"].lower()
            for bucket, cues in CUES.items():
                if any(cue in low for cue in cues):
                    hits[bucket].append({"call_id": c["call_id"], "index": t["index"],
                                         "text": t["text"]})
                    break
    for b, rows in hits.items():
        print(f"\n=== {b}: {len(rows)} candidates ===")
        for r in rows[:200]:
            print(f"  [{r['call_id']} #{r['index']}] {r['text']}")
    out = config.DATA / "gold_generic" / "_candidates.json"
    out.write_text(json.dumps(hits, ensure_ascii=False, indent=2))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    mine()
