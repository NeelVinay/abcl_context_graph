"""Stage 4: merge per-call graphs into one weighted master DiGraph.

Built by MANUAL INCREMENT (not nx.compose, which overwrites edge weights).

Nodes are ACTION-ORIENTED, actor-aware intents (agent_request_pan,
customer_provide_pan), so the flow reads sensibly. Each node accumulates:
  - keywords      : the short signal phrases ('the intent words')
  - sentiments    : Counter of customer sentiment on that intent
  - tool          : the system/API call this intent represents (if any)
Each call is a 'case', each intent an 'activity' -> a frequency-annotated
directly-follows graph (process-mining view).
"""
from __future__ import annotations

from collections import Counter

import networkx as nx

import config

MAX_KEYWORDS = 15  # cap signal phrases stored per node


def _touch_node(g, node, turn=None):
    if not g.has_node(node):
        g.add_node(node, count=0, calls=set(), keywords=[], sentiments=Counter(),
                   speaker=(turn or {}).get("speaker"),
                   base_intent=(turn or {}).get("base_intent"),
                   tool=(turn or {}).get("tool"), tool_count=0)


def _add_keywords(g, node, kws):
    bucket = g.nodes[node]["keywords"]
    for k in kws:
        if k not in bucket and len(bucket) < MAX_KEYWORDS:
            bucket.append(k)


def build_master(calls):
    g = nx.DiGraph()
    for call in calls:
        cid = call["call_id"]
        seq = [config.START]
        for t in call["turns"]:
            node = t["intent"]
            _touch_node(g, node, t)
            _add_keywords(g, node, t.get("keywords", []))
            if t.get("sentiment"):
                g.nodes[node]["sentiments"][t["sentiment"]] += 1
            if t.get("tool"):
                g.nodes[node]["tool"] = t["tool"]
                g.nodes[node]["tool_count"] += 1  # actual times the tool fired
            seq.append(node)
        seq.append(config.END)
        _touch_node(g, config.START)
        _touch_node(g, config.END)

        for node in seq:
            g.nodes[node]["count"] += 1
            g.nodes[node]["calls"].add(cid)
        for a, b in zip(seq, seq[1:]):
            if not g.has_edge(a, b):
                g.add_edge(a, b, count=0, calls=set())
            g[a][b]["count"] += 1
            g[a][b]["calls"].add(cid)
    _add_transition_probs(g)
    return g


def _add_transition_probs(g):
    for n in g.nodes:
        out_edges = list(g.out_edges(n, data=True))
        total = sum(d["count"] for *_, d in out_edges) or 1
        for _, _, d in out_edges:
            d["transition_prob"] = round(d["count"] / total, 3)
