"""Stage 3: fold synonymous intents into a single canonical label.

This is what makes per-call graphs actually OVERLAP: "verify name" and
"confirm identity" must collapse to ONE node or the graphs fragment into noise.

3-stage cascade, each stage degrades gracefully if its dependency is missing so
this module runs offline today:
  1. string normalization + fuzzy match   (rapidfuzz if installed, else stdlib difflib)
  2. semantic clustering                   (sentence-transformers if installed, else skipped)
  3. canonical naming / tie-break          (LLM hook later; for now: most-frequent label)

Two modes:
  - discovery (build_canonical_map): no taxonomy -> cluster labels freely + name clusters
  - mapping   (map_to_taxonomy)    : taxonomy given -> map each label to nearest locked intent
"""
from __future__ import annotations

import re
from collections import Counter

# --- optional dependency: fuzzy string similarity --------------------------------
try:
    from rapidfuzz import fuzz

    def _sim(a: str, b: str) -> float:
        return fuzz.token_set_ratio(a, b) / 100.0

    _FUZZY_BACKEND = "rapidfuzz"
except Exception:  # noqa: BLE001
    from difflib import SequenceMatcher

    def _sim(a: str, b: str) -> float:
        return SequenceMatcher(None, a, b).ratio()

    _FUZZY_BACKEND = "difflib (stdlib fallback)"

STRING_CUTOFF = 0.88   # >= this normalized-string similarity -> same intent
EMBED_CUTOFF = 0.72    # >= this cosine similarity -> merge clusters (if embeddings on)


def normalize(label: str) -> str:
    """Lowercase snake_case form: 'Confirm Identity' -> 'confirm_identity'."""
    s = label.strip().lower()
    s = re.sub(r"[\s\-]+", "_", s)
    s = re.sub(r"[^a-z0-9_]", "", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s


def _string_clusters(labels: list[str]) -> list[list[str]]:
    """Greedy clustering of labels by normalized-string similarity."""
    clusters: list[list[str]] = []
    reps: list[str] = []  # normalized representative per cluster
    for raw in labels:
        n = normalize(raw)
        for i, rep in enumerate(reps):
            if _sim(n, rep) >= STRING_CUTOFF:
                clusters[i].append(raw)
                break
        else:
            clusters.append([raw])
            reps.append(n)
    return clusters


def _embed_merge(clusters: list[list[str]]) -> list[list[str]]:
    """Merge string-clusters that are semantically similar. No-op if
    sentence-transformers is not installed (string-only mode)."""
    try:
        from sentence_transformers import SentenceTransformer, util
    except Exception:  # noqa: BLE001
        return clusters
    if len(clusters) < 2:
        return clusters
    reps = [normalize(c[0]).replace("_", " ") for c in clusters]
    model = SentenceTransformer("all-MiniLM-L6-v2")
    emb = model.encode(reps, convert_to_tensor=True, normalize_embeddings=True)
    sim = util.cos_sim(emb, emb)

    parent = list(range(len(clusters)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            if float(sim[i][j]) >= EMBED_CUTOFF:
                parent[find(i)] = find(j)

    merged: dict[int, list[str]] = {}
    for i, c in enumerate(clusters):
        merged.setdefault(find(i), []).extend(c)
    return list(merged.values())


def _canonical_name(cluster: list[str], counts: Counter) -> str:
    """Most frequent label in the cluster, normalized. (LLM naming can replace this.)"""
    best = max(cluster, key=lambda x: counts.get(x, 0))
    return normalize(best)


def build_canonical_map(labels: list[str], counts: Counter | None = None) -> dict:
    """DISCOVERY mode -> {raw_label: canonical_label}."""
    counts = counts or Counter(labels)
    uniq = list(dict.fromkeys(labels))
    clusters = _embed_merge(_string_clusters(uniq))
    mapping = {}
    for cluster in clusters:
        name = _canonical_name(cluster, counts)
        for raw in cluster:
            mapping[raw] = name
    return mapping


def map_to_taxonomy(labels: list[str], taxonomy: list[str], counts: Counter | None = None) -> dict:
    """MAPPING mode -> map each label to the nearest LOCKED taxonomy intent.
    Falls back to the label's normalized form (acts like UNKNOWN -> new label)."""
    norm_tax = {normalize(t): t for t in taxonomy}
    mapping = {}
    for raw in dict.fromkeys(labels):
        n = normalize(raw)
        if n in norm_tax:
            mapping[raw] = norm_tax[n]
            continue
        best, score = None, 0.0
        for tnorm in norm_tax:
            s = _sim(n, tnorm)
            if s > score:
                best, score = tnorm, s
        mapping[raw] = norm_tax[best] if score >= STRING_CUTOFF else n
    return mapping


def apply_map(calls: list[dict], mapping: dict) -> list[dict]:
    """Return new calls with every turn's intent replaced by its canonical label."""
    out = []
    for call in calls:
        out.append({
            **call,
            "turns": [
                {**t, "intent": mapping.get(t["intent"], normalize(t["intent"]))}
                for t in call["turns"]
            ],
        })
    return out


if __name__ == "__main__":
    # Demo: messy labels -> canonical map. Shows string folding; semantic folding
    # ("verify name" -> "confirm_identity") needs sentence-transformers installed.
    print(f"fuzzy backend: {_FUZZY_BACKEND}")
    demo = [
        "confirm_identity", "Confirm Identity", "verify name", "identity check",
        "greeting", "greet customer",
        "price_objection", "price objection", "EMI too high",
        "transfer_to_rm", "transfer to RM",
    ]
    mapping = build_canonical_map(demo)
    print("\nraw label                     -> canonical")
    for raw, canon in mapping.items():
        print(f"  {raw:<28} -> {canon}")
