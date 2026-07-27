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


_OUTCOME_COLOR = {           # leaf colours by call outcome
    "transferred": "#cfe8ff", "completed": "#d9f2d9", "incomplete": "#ffd9d9",
    "raised_request": "#fff2cc",   # amber: agent logged a request / promised follow-up
}


def visualize_flow(tree, out_path_no_ext: str) -> str | None:
    """Render the call-flow TREE top-to-bottom (a clean flowchart, not the DFG hairball).
    Trunk at top -> branches downward into each flow -> outcome leaves at the bottom.
    GREEN = the single most-common flow. Edge thickness ∝ number of calls.
    """
    try:
        from graphviz import Digraph
    except Exception as e:  # noqa: BLE001
        print(f"[viz] graphviz python package not available ({e}) - skipping flow tree.")
        return None
    from src.flowtree import main_flow_path

    main = main_flow_path(tree)
    total = tree.nodes[next(n for n, d in tree.nodes(data=True) if d.get("kind") == "root")]["count"]
    max_c = max((d["count"] for *_, d in tree.edges(data=True)), default=1)

    dot = Digraph("flow_tree", format="png")
    # polyline (not ortho) + forcelabels keeps every edge count present and near its arrow
    dot.attr(rankdir="TB", splines="polyline", nodesep="0.4", ranksep="0.9",
             ordering="out", forcelabels="true")
    dot.attr("node", fontname="Helvetica", fontsize="10", shape="box",
             style="rounded,filled", margin="0.12,0.07")
    dot.attr("edge", fontname="Helvetica", fontsize="9")

    for n, d in tree.nodes(data=True):
        kind = d.get("kind")
        cnt = d.get("count", 0)
        pct = f"  ({100*cnt/total:.0f}%)" if total and kind != "root" else ""
        label = f"{d.get('label', n)}\\n{cnt} call{'s' if cnt != 1 else ''}{pct}"
        if kind == "root":
            fill, color, pw = "#333333", "#333333", "2"
            dot.node(_safe_id(n), label, fillcolor=fill, fontcolor="white", color=color, penwidth=pw)
            continue
        if kind == "outcome":
            fill, shape, border = _OUTCOME_COLOR.get(d.get("stage"), "#eeeeee"), "box", "#888888"
        elif kind == "stub":
            fill, shape, border = "#f0f0f0", "box", "#888888"
        elif kind == "disposition":     # the "why" branch — stand out
            fill, shape, border = "#ffe7c2", "box", "#d08b1f"
        else:
            fill, shape, border = "#eef3fb", "box", "#888888"
        style = "rounded,filled,dashed" if kind == "stub" else "rounded,filled"
        pw = "2" if kind == "disposition" else "1"
        dot.node(_safe_id(n), label, fillcolor=fill, shape=shape, style=style,
                 color=border, penwidth=pw)

    for a, b, d in tree.edges(data=True):
        c = d["count"]
        pw = 1 + 3.5 * math.log1p(c) / math.log1p(max_c)
        on_main = (a, b) in main
        # regular edge label renders reliably; polyline (not ortho) keeps it near the line
        dot.edge(_safe_id(a), _safe_id(b), label=f" {c} ", fontcolor="#333333",
                 penwidth=f"{pw + (1.5 if on_main else 0):.2f}",
                 color="darkgreen" if on_main else "#666666")
    try:
        dot.render(out_path_no_ext, cleanup=True)
        return f"{out_path_no_ext}.png"
    except Exception as e:  # noqa: BLE001
        print(f"[viz] could not render flow tree ({e}). Install graphviz: brew install graphviz")
        return None


# ---------------------------------------------------------------------------------
# UNIFIED exec-style chart — same visual grammar as the original ABCL sop_exec.png
# (src/sop_flow.render_exec: title banner, ortho right-angle routing, oval
# start/terminal nodes, rounded step boxes, bold green main path, percentages +
# counts on every edge, 150 DPI) but driven by the domain-agnostic flow TREE
# (src/flowtree.build_flow_tree) instead of ABCL's hand-authored fixed skeleton —
# so it works for ANY client's calls, not just ABCL's loan-application DAG.
# This is the ONLY chart style new client pipelines (generic domain) should use.
_EXEC_STYLE = {
    "start":    dict(shape="oval", style="filled", fillcolor="#1f3b5c", fontcolor="white"),
    "step":     dict(shape="box", style="rounded,filled", fillcolor="#dbe7f3", color="#33628f"),
    "stub":     dict(shape="box", style="rounded,filled,dashed", fillcolor="#eeeeee", color="#888888"),
    "success":  dict(shape="oval", style="filled", fillcolor="#1f3b5c", fontcolor="white"),
    "escalate": dict(shape="box", style="rounded,filled", fillcolor="#f8d7da", color="#b02a37"),
}

# outcome value -> which _EXEC_STYLE terminal look it gets (good/neutral vs. unresolved)
_EXEC_OUTCOME_KIND = {
    "transferred": "success", "completed": "success", "raised_request": "success",
    "callback": "success",
    "incomplete": "escalate", "dropped": "escalate", "not_interested": "escalate",
    "other": "escalate",
}


def visualize_exec(tree, out_path_no_ext: str, title: str, main_edges: set | None = None) -> str | None:
    """Render a flow graph — normally src.flowtree.build_stage_dag(), a compact
    reconverging DAG over coarse stages (the structured, SOP-like look) — in the
    sop_exec.png visual style. `title` is the chart heading, e.g. "Myntra — Call
    Flow". Pass `main_edges` explicitly (e.g. from flowtree.greedy_main_path for a
    DAG, or flowtree.main_flow_path for a tree); if omitted, assumes a cycle-free
    tree and computes it via main_flow_path."""
    import datetime
    try:
        from graphviz import Digraph
    except Exception as e:  # noqa: BLE001
        print(f"[viz] graphviz not available ({e})")
        return None

    if main_edges is None:
        from src.flowtree import main_flow_path
        main_edges = main_flow_path(tree)
    main = main_edges
    root = next(n for n, d in tree.nodes(data=True) if d.get("kind") == "root")
    total = tree.nodes[root]["count"]
    max_c = max((d["count"] for *_, d in tree.edges(data=True)), default=1)
    month_year = datetime.date.today().strftime("%B %Y")

    dot = Digraph("exec_flow", format="png")
    dot.attr(
        rankdir="TB",
        splines="ortho",
        nodesep="0.5",
        ranksep="0.8",
        ratio="compress",
        size="16,100",
        label=f"{title}\\n{total} calls  •  {month_year}",
        labelloc="t", fontsize="22", fontname="Helvetica-Bold",
        bgcolor="white",
        pad="0.6",
        dpi="150",
    )
    dot.attr("node", fontname="Helvetica", fontsize="13", margin="0.28,0.16",
             width="2.6", penwidth="1.5")
    dot.attr("edge", fontname="Helvetica", fontsize="9", arrowsize="0.9")

    for n, d in tree.nodes(data=True):
        kind = d.get("kind")
        cnt = d.get("count", 0)
        if kind == "root":
            dot.node(_safe_id(n), f"Call Start\\n{cnt} calls", **_EXEC_STYLE["start"])
            continue
        pct = f"{100 * cnt / total:.0f}%" if total else ""
        label = f"{d.get('label', n)}\\n{cnt} call{'s' if cnt != 1 else ''} ({pct})"
        if kind == "stub":
            style_kind = "stub"
        elif kind == "outcome":
            style_kind = _EXEC_OUTCOME_KIND.get(d.get("stage"), "escalate")
        else:   # "stage" or "disposition" — same rounded step-box look
            style_kind = "step"
        dot.node(_safe_id(n), label, **_EXEC_STYLE[style_kind])

    for a, b, d in tree.edges(data=True):
        c = d["count"]
        pct = f"{100 * c / total:.0f}%" if total else ""
        lbl = f"{c} calls ({pct})"
        if (a, b) in main:
            dot.edge(_safe_id(a), _safe_id(b), label=lbl,
                     penwidth="3.5", color="#1a6b2d", fontcolor="#1a6b2d")
        else:
            pw = 1.2 + 2.5 * math.log1p(c) / math.log1p(max_c)
            dot.edge(_safe_id(a), _safe_id(b), label=lbl,
                     penwidth=f"{pw:.2f}", color="#4a6b8a", fontcolor="#555555")

    try:
        dot.render(out_path_no_ext, cleanup=True)
        return f"{out_path_no_ext}.png"
    except Exception as e:  # noqa: BLE001
        print(f"[viz] exec chart render failed ({e})")
        return None


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
