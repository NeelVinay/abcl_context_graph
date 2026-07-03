"""Human-readable glossary -> data/output/intents.md. Covers the action-oriented
intents, the sentiment labels, and the tool/API calls the extractor can emit.
Source of truth: ACTIONS / SENTIMENT_LEXICON / TOOL_MAP in src/extract.py."""
from __future__ import annotations

import config
from src.extract import ACTIONS, INTENT_DESC, SENTIMENT_LEXICON, TOOL_RULES
from src.justdial_coarse import INTENT_DESC as JD_INTENT_DESC

# merged description lookup across both domains (JD names don't collide with ABCL)
_ALL_DESC = {**INTENT_DESC, **JD_INTENT_DESC}

SENTIMENT_DESC = {
    "distrustful": "Customer suspects a scam / fraud, reluctant to share info ('access nahi dena')",
    "frustrated": "Customer stuck or annoyed (errors, repeated retries, 'kab tak')",
    "confused": "Customer doesn't understand what to do or what a field means",
    "skeptical": "Customer doubtful / seeking reassurance ('pakka?', 'sahi me?')",
    "happy": "Customer pleased / satisfied",
}

TOOL_DESC = {
    "send_sms": "Agent triggers an SMS (e.g. application/resume link)",
    "send_otp": "OTP sent for mobile/email verification",
    "transfer_to_rm": "Hand-off to a relationship manager / specialist",
    "push_to_crm": "Application pushed to CRM (e.g. for manual review)",
    "fetch_from_crm": "Offer / data fetched from CRM (e.g. final offer)",
}


def _humanize(action: str) -> str:
    """Real description if we have one, else fall back to the reformatted name."""
    if action in _ALL_DESC:
        return _ALL_DESC[action]
    parts = action.split("_")
    who = parts[0].capitalize() if parts[0] in ("agent", "customer") else "Flow"
    rest = " ".join(parts[1:]) if parts[0] in ("agent", "customer") else " ".join(parts)
    return f"{who}: {rest}"


def write_glossary(path=None, graph=None):
    """Glossary of the intents/sentiments/tools. When `graph` is given, list ONLY what
    actually appears in THIS dataset (so intents.md matches turns.md/report.md); without
    it, fall back to the full static taxonomy."""
    path = path or (config.OUTPUT_DIR / "intents.md")

    present_intents = present_tools = present_sents = None
    if graph is not None:
        nodes = [(n, d) for n, d in graph.nodes(data=True)
                 if n not in (config.START, config.END)]
        nodes.sort(key=lambda x: -x[1].get("count", 0))          # busiest first
        present_intents = [(n, d.get("count", 0)) for n, d in nodes]
        present_tools = {d.get("tool") for _, d in nodes if d.get("tool")}
        present_sents = set()
        for _, d in nodes:
            present_sents |= set((d.get("sentiments") or {}).keys())

    scope = "present in this dataset" if graph is not None else "action-oriented, actor-aware"
    out = ["# Glossary\n",
           f"What each intent, sentiment, and tool label means ({scope}). "
           "Source of truth: `src/extract.py`.\n"]

    if present_intents is not None:
        out.append(f"## Intents present in this dataset ({len(present_intents)})\n")
        out.append("| Intent | Meaning | Turns |")
        out.append("|---|---|---|")
        for name, cnt in present_intents:
            out.append(f"| `{name}` | {_humanize(name)} | {cnt} |")
    else:
        out.append("## Intents (action-oriented, actor-aware)\n")
        out.append("| Intent | Meaning |")
        out.append("|---|---|")
        seen = set()
        for base, pair in ACTIONS.items():
            for speaker in ("agent", "customer"):
                name = pair.get(speaker)
                if name and name not in seen:
                    seen.add(name)
                    out.append(f"| `{name}` | {_humanize(name)} |")
    out.append("")

    out.append("## Customer sentiment labels\n")
    out.append("| Sentiment | Meaning |")
    out.append("|---|---|")
    for sentiment, _ in SENTIMENT_LEXICON:
        if present_sents is None or sentiment in present_sents:
            out.append(f"| `{sentiment}` | {SENTIMENT_DESC.get(sentiment, '—')} |")
    out.append("| `neutral` | No strong sentiment detected (default) |")
    out.append("")

    tool_rows = [(base, tool, verbs) for base, (tool, verbs) in TOOL_RULES.items()
                 if present_tools is None or tool in present_tools]
    out.append("## Tool / API calls (INFERRED from agent speech)\n")
    if present_tools is not None and not tool_rows:
        out.append("_No tool/API calls were inferred in this dataset._\n")
    else:
        out.append("_Not from real tool logs — inferred only when the agent's words show "
                   "the action is performed (a tool noun + a do/send verb). A proxy, not an "
                   "observed event._\n")
        out.append("| Tool | Meaning | Fires on intent | Required verb |")
        out.append("|---|---|---|---|")
        for base, tool, verbs in tool_rows:
            vb = ", ".join(verbs) or "(intent itself is the action)"
            out.append(f"| `{tool}` | {TOOL_DESC.get(tool, '—')} | `{base}` | _{vb}_ |")
    out.append("")
    return _write(path, out)


def _write(path, out):
    path.write_text("\n".join(out))
    return path


if __name__ == "__main__":
    p = write_glossary()
    print(f"Wrote {p}")
    print(p.read_text())
