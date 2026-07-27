"""Stage 7: concise report — keywords, sentiment, tool calls, and per-call intent flow.

Captures what the manager asked for, kept short:
  1. KEYWORDS per intent (the 'intent words', not full sentences)
  2. CUSTOMER SENTIMENT per intent (happy / skeptical / distrustful ...)
  3. TOOL / API calls detected
  4. INTENT CAPTURE: each call's action-oriented flow (consecutive repeats collapsed)
Full per-turn detail stays in data/cache/<call>.json.
"""
from __future__ import annotations

from collections import Counter

import config

MAX_KEYWORDS_SHOWN = 6


def _collapse(seq):
    out = []
    for x in seq:
        if out and out[-1][0] == x:
            out[-1][1] += 1
        else:
            out.append([x, 1])
    return out


def write_report(g, calls, path=None, title="ABCL Call Context-Graph Report"):
    path = path or (config.OUTPUT_DIR / "report.md")
    out = []
    out.append(f"# {title}\n")
    out.append(f"Calls analyzed: **{len(calls)}** · intents: **{g.number_of_nodes()}** · "
               f"transitions: **{g.number_of_edges()}**")
    out.append("_(counts are per-turn occurrences across all calls, not number of calls)_\n")

    real = [(n, d) for n, d in g.nodes(data=True) if n not in (config.START, config.END)]
    real.sort(key=lambda x: x[1].get("count", 0), reverse=True)

    # 1. keywords per intent
    out.append("## 1. Keywords by intent (the signal words)\n")
    for n, d in real:
        kws = d.get("keywords", [])[:MAX_KEYWORDS_SHOWN]
        kw = ", ".join(kws) or "—"
        out.append(f"- **{n}** ({d.get('count', 0)}x): {kw}")
    out.append("")

    # 2. customer sentiment per intent
    out.append("## 2. Customer sentiment by intent\n")
    any_sent = False
    for n, d in real:
        sents = d.get("sentiments") or {}
        if sents:
            any_sent = True
            dist = " · ".join(f"{s}:{c}" for s, c in Counter(sents).most_common())
            out.append(f"- **{n}**: {dist}")
    if not any_sent:
        out.append("_(no non-neutral sentiment detected)_")
    out.append("")

    # 3. tool / API calls  (INFERRED from agent speech — see glossary; not real logs)
    out.append("## 3. Tool / API calls detected\n")
    out.append("_Inferred from the agent's words (a proxy, not real tool logs). "
               "Count = turns where the tool actually fired._\n")
    tools = [(n, d.get("tool"), d.get("tool_count", 0)) for n, d in real
             if d.get("tool") and d.get("tool_count", 0) > 0]
    if tools:
        for n, tool, c in sorted(tools, key=lambda x: -x[2]):
            out.append(f"- **{tool}** ← `{n}` ({c}x)")
    else:
        out.append("_(no tool calls detected)_")
    out.append("")

    path.write_text("\n".join(out))
    return path


def write_turns(calls, path=None):
    """Per-turn intent capture: EVERY agent/customer turn with its intent,
    sentiment, tool/API call, and keywords. This is the granular view the
    manager asked for ('intent capture at every turn')."""
    path = path or (config.OUTPUT_DIR / "turns.md")
    out = ["# Per-turn intent capture\n",
           "Every turn of every call — who spoke, the intent, sentiment, "
           "tool/API call, and the signal keywords.\n"]
    # fixed-width aligned columns (keywords last so Hindi width never breaks layout)
    hdr = f"{'#':<4}{'SPEAKER':<10}{'INTENT':<34}{'SENTIMENT':<12}{'TOOL':<14}KEYWORDS"
    for call in calls:
        turns = call["turns"]
        out.append(f"## Call {call['call_id']} ({call.get('outcome', '?')}) "
                   f"— {len(turns)} turns\n")
        out.append("```")
        out.append(hdr)
        out.append("-" * len(hdr))
        for t in turns:
            kws = ", ".join(t.get("keywords", [])) or "—"
            out.append(f"{t['index']:<4}{t['speaker']:<10}{t['intent']:<34}"
                       f"{(t.get('sentiment') or '—'):<12}{(t.get('tool') or '—'):<14}{kws}")
        out.append("```")
        out.append("")
    path.write_text("\n".join(out))
    return path
