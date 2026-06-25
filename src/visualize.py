"""Stage 6: visualize the master graph.

`text_summary` needs no dependencies and always works.
`render_graphviz` produces the picture (needs the `dot` binary + graphviz pkg);
nodes are color-coded by speaker and show a sample phrasing. Fails gracefully.
"""
from __future__ import annotations

import math
import re
import textwrap

import config
from src import analyze


def _safe_id(node_id: str) -> str:
    """Graphviz treats ':' as port syntax, so map node ids to a safe token."""
    return re.sub(r"[^0-9A-Za-z_]", "_", node_id)


def _wrap(text: str, width: int = 42) -> str:
    """Wrap a long utterance across lines so nodes don't overflow horizontally."""
    return "\n".join(textwrap.wrap(text, width=width)) or text

_SPEAKER_COLOR = {"agent": "#cfe8ff", "customer": "#fff2cc"}  # blue / yellow


def text_summary(g, calls: list[dict]) -> str:
    lines = []
    lines.append(f"Nodes: {g.number_of_nodes()}   Edges: {g.number_of_edges()}   Calls: {len(calls)}")
    lines.append("")
    path, n = analyze.happy_path(calls)
    lines.append(f"HAPPY PATH ({n} calls):")
    lines.append("  " + " -> ".join(path))
    lines.append("")
    lines.append("TOP TRANSITIONS:")
    for a, b, c in analyze.top_transitions(g):
        lines.append(f"  {c:>3}x  {a} -> {b}")
    lines.append("")
    lines.append("DROP-OFF POINTS (-> END):")
    for a, c in analyze.drop_off_nodes(g):
        lines.append(f"  {c:>3}x  {a}")
    lines.append("")
    lines.append("KEYWORDS (busiest intents):")
    for node, c, kws in analyze.node_keywords(g):
        lines.append(f"  {node}  ({c}x): {', '.join(kws[:5])}")
    lines.append("")
    lines.append("OUTCOMES:")
    for outcome, c in analyze.outcome_distribution(calls).most_common():
        lines.append(f"  {c:>3}x  {outcome}")
    return "\n".join(lines)


def _main_path_edges(g):
    """The single most-taken path from START: greedily follow the highest-count
    next-step (skipping already-visited nodes to avoid looping) until END/dead-end."""
    if not g.has_node(config.START):
        return set()
    path, cur, seen = set(), config.START, {config.START}
    while True:
        outs = [(b, d["count"]) for _, b, d in g.out_edges(cur, data=True) if b not in seen]
        if not outs:
            break
        nxt = max(outs, key=lambda x: x[1])[0]
        path.add((cur, nxt))
        seen.add(nxt)
        cur = nxt
        if cur == config.END:
            break
    return path


def _friction_edges(edge_items):
    """Friction = a step repeating (self-loop) or two steps ping-ponging (A<->B)."""
    eset = {(a, b) for a, b, _ in edge_items}
    fr = set()
    for a, b, _ in edge_items:
        if a == b or (b, a) in eset:
            fr.add((a, b))
    return fr


def _main_path_sequence(g):
    """Ordered node list of the most-taken path: START .. END."""
    if not g.has_node(config.START):
        return []
    seq, cur, seen = [config.START], config.START, {config.START}
    while True:
        outs = [(b, d["count"]) for _, b, d in g.out_edges(cur, data=True) if b not in seen]
        if not outs:
            break
        nxt = max(outs, key=lambda x: x[1])[0]
        seq.append(nxt)
        seen.add(nxt)
        cur = nxt
        if cur == config.END:
            break
    return seq


def render_graphviz(g, out_path_no_ext: str, min_count: int = 2, top_k: int = 2,
                    shape: str = "ellipse", show_phrasings: bool = False) -> str | None:
    """Natural left-to-right layout: graphviz ranks by flow and minimises crossings,
    using as much space as needed so connections are easy to follow.
    GREEN = most-taken path (wins conflicts) · RED = friction · BLACK = other context.
    """
    try:
        from graphviz import Digraph
    except Exception as e:  # noqa: BLE001
        print(f"[viz] graphviz python package not available ({e}) - skipping image.")
        return None

    edges = [(a, b, d) for a, b, d in g.edges(data=True) if d["count"] >= min_count]
    if not edges:
        edges = [(a, b, d) for a, b, d in g.edges(data=True)]
    if top_k and top_k > 0:
        from collections import defaultdict
        by_src = defaultdict(list)
        for e in edges:
            by_src[e[0]].append(e)
        edges = []
        for _, lst in by_src.items():
            lst.sort(key=lambda e: e[2]["count"], reverse=True)
            edges.extend(lst[:top_k])

    seq = _main_path_sequence(g)
    main_path = set(zip(seq, seq[1:]))
    drawn = {(a, b): d for a, b, d in edges}
    for ab in main_path:
        if g.has_edge(*ab):
            drawn[ab] = g[ab[0]][ab[1]]
    edge_items = [(a, b, d) for (a, b), d in drawn.items()]
    friction = _friction_edges(edge_items)
    keep = {n for ab in drawn for n in ab}
    max_c = max((d["count"] for d in drawn.values()), default=1)
    path_nodes = set(seq)
    friction_nodes = {n for ab in friction for n in ab}

    dot = Digraph("context_graph", format="png")
    # wider spacing so many arrows converging on one node don't overlap:
    # nodesep = gap between nodes in a rank, ranksep = gap between ranks (room for splines)
    dot.attr(rankdir="LR", splines="true", nodesep="0.9", ranksep="1.6",
             concentrate="false", sep="+10", esep="+6")
    dot.attr("node", fontname="Helvetica", fontsize="10", margin="0.1,0.06")
    dot.attr("edge", fontname="Helvetica", fontsize="9", color="black")

    for node in keep:
        d = g.nodes[node]
        speaker = d.get("speaker")
        intent = d.get("intent", node)
        count = d.get("count", 0)
        kws = d.get("keywords", [])
        tool = d.get("tool")
        fill = "#d9f2d9" if tool else _SPEAKER_COLOR.get(speaker, "#e8e8e8")  # tool calls = green
        label = f"{intent}\n({count})"
        if tool:
            label += f"\n[tool: {tool}]"
        if show_phrasings and kws:
            label += f'\n"{kws[0][:34]}"'
        if node in (config.START, config.END):
            nsh, nst = "box", "filled"
        else:
            nsh = shape
            nst = "rounded,filled" if shape == "box" else "filled"
        if node in path_nodes:
            border, bw = "darkgreen", "2.5"
        elif node in friction_nodes:
            border, bw = "red", "2.5"
        else:
            border, bw = "#999999", "1"
        dot.node(_safe_id(node), label, shape=nsh, style=nst, fillcolor=fill,
                 color=border, penwidth=bw)

    for a, b, d in edge_items:
        base = 1 + 4 * math.log1p(d["count"]) / math.log1p(max_c)
        if (a, b) in main_path:
            color, pw = "darkgreen", base + 1.5
        elif (a, b) in friction:
            color, pw = "red", base + 1
        else:
            color, pw = "black", base
        dot.edge(_safe_id(a), _safe_id(b), label=str(d["count"]),
                 penwidth=f"{pw:.2f}", color=color)
    try:
        dot.render(out_path_no_ext, cleanup=True)
        return f"{out_path_no_ext}.png"
    except Exception as e:  # noqa: BLE001
        print(f"[viz] could not render image ({e}). Install the dot binary: brew install graphviz")
        return None
