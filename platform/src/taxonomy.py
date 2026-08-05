"""Stage 1: discover + lock the canonical intent taxonomy.

Hybrid approach:
  - collect the raw intents that appear across a sample of calls
  - fold synonyms via canonicalize.build_canonical_map -> canonical labels
  - LOCK the result to data/output/taxonomy.json
  - extraction (Stage 2) is then constrained to this vocabulary, so every call
    speaks the same language and the per-call graphs overlap cleanly

In the real pipeline the raw intents come from running ~TAXONOMY_SAMPLE_SIZE
transcripts through Claude (free-form intent extraction). Here we can also derive
them from already-extracted calls or from mock data, since the folding logic is
identical either way.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

import config
from src import canonicalize

TAXONOMY_PATH = config.OUTPUT_DIR / "taxonomy.json"


def collect_raw_intents(calls: list[dict]) -> Counter:
    c: Counter = Counter()
    for call in calls:
        for t in call["turns"]:
            c[t["intent"]] += 1
    return c


def discover_taxonomy(calls: list[dict]) -> dict:
    """Discover, lock, and save the canonical taxonomy. Returns {intent: count}."""
    counts = collect_raw_intents(calls)
    mapping = canonicalize.build_canonical_map(list(counts.keys()), counts)
    taxonomy: Counter = Counter()
    for raw, total in counts.items():
        taxonomy[mapping[raw]] += total
    save_taxonomy(taxonomy)
    return dict(taxonomy)


def save_taxonomy(taxonomy: Counter, path: Path = TAXONOMY_PATH) -> None:
    data = {"intents": sorted(taxonomy.keys()), "counts": dict(taxonomy)}
    path.write_text(json.dumps(data, indent=2))


def load_taxonomy(path: Path = TAXONOMY_PATH) -> list[str] | None:
    if not path.exists():
        return None
    return json.loads(path.read_text())["intents"]


if __name__ == "__main__":
    from tests.mock_data import MOCK_CALLS

    tax = discover_taxonomy(MOCK_CALLS)
    print("Discovered taxonomy (intent -> count):")
    for intent, n in sorted(tax.items(), key=lambda x: -x[1]):
        print(f"  {n:>3}x  {intent}")
    print(f"\nSaved to {TAXONOMY_PATH}")
