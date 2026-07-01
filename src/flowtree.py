"""Phase A: build a top-to-bottom call-FLOW TREE from call traces.

Each call becomes a sequence of coarse flow STAGES (src/flowstages). We merge the calls
into a prefix tree (trie): shared opening stages share one trunk, and the tree branches
wherever calls diverge — so every distinct flow is a root-to-leaf path. Loops are removed
by collapsing repeats (a tree is acyclic by construction), which is what de-hairballs it.

Neatness without losing flows: at each node, rare child branches are folded into a single
"+N other flows" STUB, so every call is still represented but the picture stays tidy.

Returns a networkx DiGraph (a tree) ready for visualize.visualize_flow().
"""
from __future__ import annotations

import networkx as nx

from src.dispositions import DISPOSITION_LABEL, primary_disposition
from src.flowstages import DROP_STAGES, STAGE_LABEL, stage_of

DISP_PREFIX = "@"   # marks a disposition token in a trace, e.g. "@no_leads"


def call_to_stages(call: dict, collapse: str = "first", with_disposition: bool = True) -> list[str]:
    """Turn a call's fine intents into a short stage sequence (a 'flow').

    Drops back-channel/unclassified stages, then collapses to keep the tree shallow:
      collapse="first" (default): keep each stage's FIRST occurrence only -> a flow becomes
        a milestone path (e.g. open -> qa -> application -> transfer), not every back-and-forth.
      collapse="consecutive": keep full order, only merge adjacent repeats (deeper, detailed).
    with_disposition: prepend the call's primary disposition (@no_leads, ...) as the first
      branch, so the tree branches by WHY the call happened (Phase B).
    """
    stages = [stage_of(t.get("base_intent")) for t in call["turns"]]
    stages = [s for s in stages if s not in DROP_STAGES]
    seq: list[str] = []
    if collapse == "first":
        seen = set()
        for s in stages:
            if s not in seen:
                seen.add(s)
                seq.append(s)
    else:
        for s in stages:
            if not seq or seq[-1] != s:
                seq.append(s)
    if with_disposition:
        seq = [DISP_PREFIX + primary_disposition(call)] + seq
    return seq


def _node_meta(token: str) -> tuple[str, str]:
    """(kind, label) for a trace token — disposition (@...) vs conversation stage."""
    if token.startswith(DISP_PREFIX):
        key = token[len(DISP_PREFIX):]
        return "disposition", DISPOSITION_LABEL.get(key, key)
    return "stage", STAGE_LABEL.get(token, token)


def build_flow_tree(calls: list[dict], top_k: int = 3, min_count: int = 1) -> nx.DiGraph:
    """Build the flow tree. Each node id is the stage-path to it (unique per branch).
    Node attrs: stage, label, count (#calls through here), kind (root|stage|outcome|stub).

      top_k     : keep at most this many real child branches per node
      min_count : a child taken by fewer than this many calls is folded into the stub
    """
    g = nx.DiGraph()
    ROOT = "()"
    g.add_node(ROOT, stage="__start__", label="Call start", count=len(calls), kind="root")

    # child key = (parent_id, stage); value = list of call indices flowing into it
    for ci, call in enumerate(calls):
        stages = call_to_stages(call)
        outcome = call.get("outcome", "other")
        node = ROOT
        path: tuple[str, ...] = ()
        for st in stages:
            path = path + (st,)
            child = str(path)
            if not g.has_node(child):
                kind, label = _node_meta(st)
                g.add_node(child, stage=st, label=label, count=0, kind=kind)
            if not g.has_edge(node, child):
                g.add_edge(node, child, count=0)
            g.nodes[child]["count"] += 1
            g[node][child]["count"] += 1
            node = child
        # terminal outcome leaf
        leaf = str(path + ("=" + outcome,))
        if not g.has_node(leaf):
            g.add_node(leaf, stage=outcome, label=outcome, count=0, kind="outcome")
        if not g.has_edge(node, leaf):
            g.add_edge(node, leaf, count=0)
        g.nodes[leaf]["count"] += 1
        g[node][leaf]["count"] += 1

    _prune(g, ROOT, top_k, min_count)
    return g


def _prune(g: nx.DiGraph, root: str, top_k: int, min_count: int) -> None:
    """Fold each node's weak/excess child branches into a single '+N other flows' stub.
    top_k <= 0 disables folding entirely (show EVERY flow)."""
    if top_k <= 0 and min_count <= 1:
        return  # expand all flows, no folding
    for node in list(g.nodes):
        if not g.has_node(node):        # already folded as part of an ancestor's stub
            continue
        children = list(g.successors(node))
        if len(children) <= 1:
            continue
        children.sort(key=lambda c: g[node][c]["count"], reverse=True)
        keep, fold = [], []
        for i, c in enumerate(children):
            if i < top_k and g[node][c]["count"] >= min_count:
                keep.append(c)
            else:
                fold.append(c)
        if len(fold) <= 1:
            continue  # nothing meaningful to collapse
        folded_calls = sum(g[node][c]["count"] for c in fold)
        for c in fold:
            _remove_subtree(g, c)
        stub = f"{node}|stub"
        g.add_node(stub, stage="__stub__", label=f"+{len(fold)} other flows",
                   count=folded_calls, kind="stub")
        g.add_edge(node, stub, count=folded_calls)


def _remove_subtree(g: nx.DiGraph, node: str) -> None:
    for child in list(g.successors(node)):
        _remove_subtree(g, child)
    if g.has_node(node):
        g.remove_node(node)


def main_flow_path(g: nx.DiGraph) -> set:
    """Edges on the single MOST-COMMON complete flow = the highest-count outcome leaf,
    traced back to the root. (Not a greedy fattest-edge walk, which can pick a path no
    single call actually took and breaks ties arbitrarily.)"""
    root = next((n for n, d in g.nodes(data=True) if d.get("kind") == "root"), None)
    if root is None:
        return set()
    leaves = [n for n in g.nodes
              if g.out_degree(n) == 0 and g.nodes[n].get("kind") != "stub"]
    if not leaves:
        return set()
    best = max(leaves, key=lambda n: g.nodes[n].get("count", 0))
    edges, cur = set(), best
    while cur != root:                      # tree -> unique parent path back to root
        preds = list(g.predecessors(cur))
        if not preds:
            break
        edges.add((preds[0], cur))
        cur = preds[0]
    return edges
