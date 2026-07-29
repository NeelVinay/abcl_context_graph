"""Stage 5: simple analysis over the calls / master graph.

POC-level (pure stdlib + networkx). Nodes are speaker-qualified ("agent:intent" /
"customer:intent"), so paths and transitions show WHO spoke at each turn.
Upgradeable to pm4py later with no schema change.
"""
from __future__ import annotations

from collections import Counter

import config


def _step(turn: dict) -> str:
    return turn["intent"]  # already action-oriented + actor-aware (e.g. agent_request_pan)


def variants(calls: list[dict]) -> Counter:
    """Count distinct full speaker:intent paths (a 'variant' = one full conversation path)."""
    c: Counter = Counter()
    for call in calls:
        path = tuple(_step(t) for t in call["turns"])
        c[path] += 1
    return c


def happy_path(calls: list[dict]) -> tuple[tuple[str, ...], int]:
    v = variants(calls)
    return v.most_common(1)[0] if v else ((), 0)


def outcome_distribution(calls: list[dict]) -> Counter:
    return Counter(call.get("outcome", "other") for call in calls)


def top_transitions(g, n: int = 12) -> list[tuple[str, str, int]]:
    edges = [
        (a, b, d["count"])
        for a, b, d in g.edges(data=True)
        if a != config.START and b != config.END
    ]
    return sorted(edges, key=lambda e: e[2], reverse=True)[:n]


def drop_off_nodes(g, n: int = 5) -> list[tuple[str, int]]:
    """Nodes most often followed directly by END (where calls die)."""
    drops = [(a, d["count"]) for a, b, d in g.edges(data=True) if b == config.END]
    return sorted(drops, key=lambda e: e[1], reverse=True)[:n]


def node_keywords(g, top: int = 8) -> list[tuple[str, int, list]]:
    """Busiest intents with their signal keywords (the 'intent words')."""
    nodes = [(n, d) for n, d in g.nodes(data=True) if n not in (config.START, config.END)]
    nodes.sort(key=lambda x: x[1].get("count", 0), reverse=True)
    return [(n, d.get("count", 0), d.get("keywords", [])) for n, d in nodes[:top]]
