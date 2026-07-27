"""Unsupervised sub-clustering WITHIN a broad bucket (e.g. all "ask_question" turns)
— no per-client taxonomy, no LLM. Works for any client's data because it only uses:
  1. the embedding model already used to train/run the classifier
  2. distance-threshold clustering (decides cluster COUNT itself, per client/bucket —
     nothing hand-tuned), same idea src/canonicalize.py already uses for taxonomy
     discovery, applied one level deeper (inside one bucket, not across all labels)
  3. corpus-driven keyword extraction (src/extract.build_keyword_vocab's approach)
     to auto-NAME each cluster from its own content, instead of a written label

This is the client-agnostic alternative to a hand-built keyword list (like
src/sop_flow.py's ABCL-specific QUERY_TYPES) or a fresh Claude labeling pass — it
costs nothing per new client, but the cluster names are blunter ("top keywords"
rather than a clean phrase) since nothing is reading for meaning.
"""
from __future__ import annotations

from collections import Counter

import numpy as np


def discover_subclusters(texts: list[str], embed_model, embed_prefix: str = "",
                         distance_threshold: float | None = None, min_cluster_size: int = 5
                         ) -> list[int]:
    """Cluster `texts` by cosine distance between embeddings. Returns a cluster id
    per text (same order as input); ids below min_cluster_size are folded into -1
    ("misc / too small to be its own bucket").

    distance_threshold=None (default): auto-select rather than a fixed magic number
    — different clients/domains/embedding models pack their embedding space at
    different densities (measured: Myntra's Hinglish delivery-complaint sentences
    go from 34 clusters to 1 between threshold 0.15 and 0.2 — a fixed threshold
    tuned for one client is not safe to reuse for another). Sweeps a range and picks
    the threshold that maximizes the number of clusters meeting min_cluster_size —
    i.e. the most SPECIFIC split that's still statistically meaningful, found fresh
    for every call rather than hand-tuned once and reused blindly.
    """
    from sklearn.cluster import AgglomerativeClustering

    if len(texts) < min_cluster_size * 2:
        return [-1] * len(texts)   # not enough volume to cluster meaningfully at all

    enc_texts = [embed_prefix + t for t in texts] if embed_prefix else texts
    emb = embed_model.encode(enc_texts, normalize_embeddings=True, show_progress_bar=False)

    if distance_threshold is None:
        best_thresh, best_score = 0.3, (-1, -1)
        for thresh in np.arange(0.05, 0.45, 0.025):
            clust = AgglomerativeClustering(n_clusters=None, distance_threshold=float(thresh),
                                            metric="cosine", linkage="average")
            labels = clust.fit_predict(emb)
            sizes = Counter(labels)
            n_big = sum(1 for n in sizes.values() if n >= min_cluster_size)
            covered = sum(n for n in sizes.values() if n >= min_cluster_size)
            # maximize (# meaningful clusters), tie-break by how much of the data they cover
            score = (n_big, covered)
            if score > best_score:
                best_score, best_thresh = score, float(thresh)
        distance_threshold = best_thresh

    clust = AgglomerativeClustering(
        n_clusters=None, distance_threshold=distance_threshold,
        metric="cosine", linkage="average",
    )
    labels = clust.fit_predict(emb)

    sizes = Counter(labels)
    return [int(lab) if sizes[lab] >= min_cluster_size else -1 for lab in labels]


def label_clusters(texts: list[str], cluster_ids: list[int], top_n: int = 2) -> dict[int, str]:
    """Auto-name each cluster from its OWN most distinctive recurring words —
    frequent inside this cluster, not just frequent overall (so "order"/"deliver",
    which show up everywhere in an e-commerce bucket, don't dominate every label)."""
    from src.stopwords import STOPWORDS
    import re
    WORD_RE = re.compile(r"[a-zA-Zऀ-ॣ]+")

    by_cluster: dict[int, list[str]] = {}
    for t, c in zip(texts, cluster_ids):
        by_cluster.setdefault(c, []).append(t)

    global_df = Counter()
    for t in texts:
        seen = {w.lower() for w in WORD_RE.findall(t) if len(w) >= 3 and w.lower() not in STOPWORDS}
        global_df.update(seen)
    n_docs = len(texts)

    labels = {}
    for c, members in by_cluster.items():
        if c == -1:
            labels[c] = "misc / other questions"
            continue
        local_df = Counter()
        for t in members:
            seen = {w.lower() for w in WORD_RE.findall(t) if len(w) >= 3 and w.lower() not in STOPWORDS}
            local_df.update(seen)
        # distinctiveness score: how much MORE common in this cluster than overall
        scored = sorted(local_df.items(),
                        key=lambda kv: -(kv[1] / len(members)) / max(global_df[kv[0]] / n_docs, 1e-6))
        top_words = [w for w, _ in scored[:top_n]]
        labels[c] = " / ".join(top_words) if top_words else f"cluster {c}"
    return labels


if __name__ == "__main__":
    import json
    import config
    from sentence_transformers import SentenceTransformer
    from src.distill import DOMAINS, embed_prefix_for

    gold = {(r["call_id"], r["index"]): r
            for r in (json.loads(l) for l in (config.DATA / "gold_generic" / "labels.jsonl")
                     .read_text().splitlines() if l.strip())}
    texts = []
    for f in sorted(config.CACHE_DIR.glob("GEN-myntra-*.json")):
        c = json.loads(f.read_text())
        for t in c["turns"]:
            g = gold.get((c["call_id"], t["index"]))
            if g and g["base_intent"] == "ask_question" and t["speaker"] == "customer":
                texts.append(t["text"])

    embed_model = DOMAINS["generic"]["embed_model"]
    prefix = embed_prefix_for(embed_model)
    model = SentenceTransformer(embed_model)
    cluster_ids = discover_subclusters(texts, model, prefix)
    labels = label_clusters(texts, cluster_ids)

    print(f"{len(texts)} Myntra ask_question turns -> {len(set(cluster_ids))} clusters\n")
    counts = Counter(cluster_ids)
    for c, n in counts.most_common():
        print(f"=== cluster {c}: \"{labels[c]}\"  ({n} turns) ===")
        for t, cid in zip(texts, cluster_ids):
            if cid == c:
                print(f"    {t[:80]}")
        print()
