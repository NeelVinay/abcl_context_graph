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


def build_flow_tree(calls: list[dict], top_k: int = 3, min_count: int = 1,
                    with_disposition: bool = True) -> nx.DiGraph:
    """Build the flow tree. Each node id is the stage-path to it (unique per branch).
    Node attrs: stage, label, count (#calls through here), kind (root|stage|outcome|stub).

      top_k            : keep at most this many real child branches per node
      min_count        : a child taken by fewer than this many calls is folded into the stub
      with_disposition : prepend the call-level disposition branch. Set False for a
                         domain with no disposition classifier of its own (e.g. a new
                         generic-pipeline client) — leaving it True there would add a
                         single uninformative "No clear disposition" node to every call.
    """
    g = nx.DiGraph()
    ROOT = "()"
    g.add_node(ROOT, stage="__start__", label="Call start", count=len(calls), kind="root")

    # child key = (parent_id, stage); value = list of call indices flowing into it
    for ci, call in enumerate(calls):
        stages = call_to_stages(call, with_disposition=with_disposition)
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


def build_stage_dag(calls: list[dict], with_disposition: bool = True,
                    min_count: int = 1) -> nx.DiGraph:
    """A DAG over coarse STAGES, not a tree: each stage/disposition/outcome is ONE
    node reused across every call that passes through it, so paths reconverge
    (e.g. two different journeys that both hit "wait" share the same "wait" node)
    instead of forking into new copies per branch. This is what gives a compact,
    structured SOP-style diagram instead of a sprawling per-path tree — matching
    src/sop_flow.py's fixed-skeleton diagram, but built from real data rather than
    a hand-authored skeleton, so it works for any client.

    min_count: edges taken by fewer than this many calls are dropped (decluttering;
    there's no tree to fold into a stub here, so weak edges are just omitted).
    """
    g = nx.DiGraph()
    ROOT = "__start__"
    g.add_node(ROOT, stage="__start__", label="Call Start", count=len(calls), kind="root")

    edge_counts: dict = {}
    node_counts: dict = {}
    node_kind_label: dict = {}
    for call in calls:
        seq = call_to_stages(call, with_disposition=with_disposition)
        outcome = call.get("outcome", "other")
        full = seq + ["=" + outcome]
        prev = ROOT
        for tok in seq + ["=" + outcome]:
            if tok not in node_kind_label:
                if tok.startswith("="):
                    node_kind_label[tok] = ("outcome", tok[1:])
                else:
                    node_kind_label[tok] = _node_meta(tok)
            node_counts[tok] = node_counts.get(tok, 0) + 1
            edge_counts[(prev, tok)] = edge_counts.get((prev, tok), 0) + 1
            prev = tok

    for tok, (kind, label) in node_kind_label.items():
        g.add_node(tok, stage=tok.lstrip("=@"), label=label,
                   count=node_counts.get(tok, 0), kind=kind)
    for (a, b), c in edge_counts.items():
        if c < min_count:
            continue
        g.add_edge(a, b, count=c)
    # min_count can strand a rare node with zero surviving edges (e.g. a bucket that
    # only ever got 1-2 calls) — floating, edge-less nodes look broken, not "pruned",
    # so drop them rather than render an unconnected box.
    isolated = [n for n in g.nodes if n != ROOT and g.degree(n) == 0]
    g.remove_nodes_from(isolated)
    return g


def greedy_main_path(g: nx.DiGraph) -> set:
    """Cycle-safe greedy walk for a DAG (unlike main_flow_path, which assumes a
    tree): from the root, follow the heaviest outgoing edge, stopping if it would
    revisit an already-visited node (a real DAG can have back-edges/cycles)."""
    root = next((n for n, d in g.nodes(data=True) if d.get("kind") == "root"), None)
    if root is None:
        return set()
    edges, cur, visited = set(), root, {root}
    while True:
        kids = [c for c in g.successors(cur) if c not in visited]
        if not kids:
            break
        nxt = max(kids, key=lambda c: g[cur][c]["count"])
        edges.add((cur, nxt))
        cur = nxt
        visited.add(cur)
    return edges


def main_flow_path(g: nx.DiGraph) -> set:
    """GREEDY 'where most calls go': from the root, at each step follow the child with the
    most calls (ignoring the '+N other flows' stub), until a leaf. This is the modal
    journey step-by-step — intuitive even when no single full path dominates (which is the
    case with sparse/varied data, where a most-common-complete-path highlight is arbitrary)."""
    root = next((n for n, d in g.nodes(data=True) if d.get("kind") == "root"), None)
    if root is None:
        return set()
    edges, cur = set(), root
    while True:
        kids = [c for c in g.successors(cur) if g.nodes[c].get("kind") != "stub"]
        if not kids:
            break
        nxt = max(kids, key=lambda c: g[cur][c]["count"])   # fattest real branch
        edges.add((cur, nxt))
        cur = nxt
    return edges
