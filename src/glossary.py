"""Human-readable glossary -> data/output/intents.md. Covers the action-oriented
intents, the sentiment labels, and the tool/API calls the extractor can emit.
Source of truth: ACTIONS / SENTIMENT_LEXICON / TOOL_MAP in src/extract.py."""
from __future__ import annotations

import config
from src.extract import ACTIONS, SENTIMENT_LEXICON, TOOL_RULES

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
    parts = action.split("_")
    who = parts[0].capitalize() if parts[0] in ("agent", "customer") else "Flow"
    rest = " ".join(parts[1:]) if parts[0] in ("agent", "customer") else " ".join(parts)
    return f"{who}: {rest}"


def write_glossary(path=None):
    path = path or (config.OUTPUT_DIR / "intents.md")
    out = ["# Glossary\n",
           "What each intent, sentiment, and tool label means. "
           "Source of truth: `src/extract.py`.\n"]

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
        out.append(f"| `{sentiment}` | {SENTIMENT_DESC.get(sentiment, '—')} |")
    out.append("| `neutral` | No strong sentiment detected (default) |")
    out.append("")

    out.append("## Tool / API calls (INFERRED from agent speech)\n")
    out.append("_Not from real tool logs — inferred only when the agent's words show "
               "the action is performed (a tool noun + a do/send verb). A proxy, not an "
               "observed event._\n")
    out.append("| Tool | Meaning | Fires on intent | Required verb |")
    out.append("|---|---|---|---|")
    for base, (tool, verbs) in TOOL_RULES.items():
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
