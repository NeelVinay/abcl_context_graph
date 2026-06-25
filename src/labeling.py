"""Phase 0 of the distillation plan: produce Claude-quality labels for every turn.

Claude (the teacher) labels each segmented turn with the correct base intent,
keywords, sentiment, and tool. A small local model (the student) later trains to
imitate these labels. This module just handles the I/O around that:

  build_guide()  -> the labeling contract (taxonomy + examples) given to labelers
  emit_batches() -> split cached calls into batch files for parallel labelers
  assemble()     -> validate labeler outputs and merge into data/gold/labels.jsonl

The unit of labeling is the SEGMENTED turn from extract_call (after merge + noise
drop), so the training pairs align exactly with what the student model sees.
"""
from __future__ import annotations

import json
from pathlib import Path

import config
from src.extract import INTENT_LIBRARY, ACTIONS, SENTIMENT_LEXICON, TOOL_RULES

GOLD_DIR = config.CACHE_DIR.parent / "gold"   # data/gold
TOLABEL_DIR = GOLD_DIR / "_tolabel"
LABELED_DIR = GOLD_DIR / "_labeled"
LABELS_PATH = GOLD_DIR / "labels.jsonl"
GUIDE_PATH = GOLD_DIR / "LABELING_GUIDE.md"

VALID_BASE = {name for name, _, _ in INTENT_LIBRARY} | {"other"}
# action-form name -> base name, so a labeler that wrote "customer_request_wait"
# (the action form) instead of "wait_hold" (the base form) is recovered, not dropped.
ACTION_TO_BASE = {a: base for base, pair in ACTIONS.items() for a in pair.values()}
VALID_SENTIMENT = {s for s, _ in SENTIMENT_LEXICON} | {"neutral"}
VALID_TOOL = {t for t, _ in TOOL_RULES.values()} | {None}


def build_guide() -> str:
    """Human/agent-readable labeling contract, generated from the live taxonomy."""
    out = ["# Labeling guide — ABCL loan-application calls (Hinglish)\n",
           "You are the TEACHER creating ground-truth labels. For EACH turn assign the "
           "single best `base_intent` from the list below, the signal `keywords` "
           "(verbatim spans copied from the turn text — the words that reveal the intent), "
           "the customer `sentiment`, and any `tool` call.\n",
           "Rules:",
           "- `base_intent` MUST be exactly one value from the list (or `other` if nothing fits — "
           "then add `suggested_intent` with a short new name).",
           "- `keywords`: 1-5 short phrases COPIED VERBATIM from the turn text. No paraphrasing, "
           "no invented words, no names/PII. If nothing is salient, use [].",
           "- `sentiment`: ONLY for customer turns, else null. One of: "
           f"{sorted(VALID_SENTIMENT)}. Use `neutral` if no clear emotion.",
           "- `tool`: ONLY for agent turns where an actual system action is performed "
           f"(not merely mentioned). One of: {sorted(t for t in VALID_TOOL if t)} or null.",
           "- Judge by MEANING and context, not keyword presence. The transcript is Hinglish "
           "(mixed Hindi/Devanagari + romanized English) and may have ASR errors.\n",
           "## Valid base intents (with example utterances)\n"]
    for name, kws, examples in INTENT_LIBRARY:
        pair = ACTIONS.get(name, {})
        roles = f"agent→`{pair.get('agent','?')}`, customer→`{pair.get('customer','?')}`"
        ex = " | ".join(examples[:3])
        out.append(f"- **{name}** ({roles})\n    e.g. {ex}")
    out.append("\n## Output format (per call): JSON")
    out.append("```json")
    out.append('{"call_id": "<id>", "turns": [')
    out.append('  {"index": 0, "speaker": "customer", "base_intent": "greeting", '
               '"keywords": ["hello"], "sentiment": "neutral", "tool": null},')
    out.append('  {"index": 1, "speaker": "agent", "base_intent": "send_sms_link", '
               '"keywords": ["sms", "link", "भेज"], "sentiment": null, "tool": "send_sms"}')
    out.append(']}')
    out.append("```")
    return "\n".join(out)


def _segmented_turns(call: dict) -> list[dict]:
    """Strip the local predictions; keep only what the labeler needs."""
    return [{"index": t["index"], "speaker": t["speaker"], "text": t["text"]}
            for t in call["turns"]]


def emit_batches(per_batch: int = 8) -> list[Path]:
    """Read all cached extractions, write batch files of stripped turns to label."""
    TOLABEL_DIR.mkdir(parents=True, exist_ok=True)
    calls = []
    for f in sorted(config.CACHE_DIR.glob("*.json")):
        c = json.loads(f.read_text())
        calls.append({"call_id": c["call_id"], "turns": _segmented_turns(c)})
    paths = []
    for i in range(0, len(calls), per_batch):
        batch = calls[i:i + per_batch]
        p = TOLABEL_DIR / f"batch_{i // per_batch:02d}.json"
        p.write_text(json.dumps(batch, ensure_ascii=False, indent=2))
        paths.append(p)
    GUIDE_PATH.parent.mkdir(parents=True, exist_ok=True)
    GUIDE_PATH.write_text(build_guide())
    return paths


def _cache_text_index() -> dict:
    """(call_id, index) -> turn text, from the cached extractions (the source text)."""
    idx = {}
    for f in config.CACHE_DIR.glob("*.json"):
        c = json.loads(f.read_text())
        for t in c["turns"]:
            idx[(c["call_id"], t["index"])] = t["text"]
    return idx


def assemble() -> tuple[int, list[str]]:
    """Validate every labeled batch and merge into labels.jsonl (one turn per line).
    Keywords not found verbatim in the source turn text are dropped (self-cleaning),
    so a minor labeler slip can't poison the gold data."""
    rows, problems = [], []
    text_idx = _cache_text_index()
    dropped_kw = 0
    for f in sorted(LABELED_DIR.glob("*.json")):
        try:
            data = json.loads(f.read_text())
        except Exception as e:  # noqa: BLE001
            problems.append(f"{f.name}: unreadable ({e})")
            continue
        for call in data:
            cid = call.get("call_id")
            for t in call.get("turns", []):
                b = t.get("base_intent")
                if b not in VALID_BASE:
                    b = ACTION_TO_BASE.get(b)   # recover action-form labels
                if b not in VALID_BASE:
                    problems.append(f"{cid} turn {t.get('index')}: bad base_intent "
                                    f"{t.get('base_intent')!r}")
                    continue
                src = (text_idx.get((cid, t["index"])) or "").lower()
                kws = []
                for k in t.get("keywords", []):
                    if k.lower() in src:
                        kws.append(k)
                    else:
                        dropped_kw += 1
                rows.append({
                    "call_id": cid, "index": t["index"], "speaker": t["speaker"],
                    "base_intent": b, "keywords": kws,
                    "sentiment": t.get("sentiment"), "tool": t.get("tool"),
                    "suggested_intent": t.get("suggested_intent"),
                })
    LABELS_PATH.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows))
    if dropped_kw:
        problems.append(f"(info) dropped {dropped_kw} non-verbatim keywords")
    return len(rows), problems


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "emit"
    if cmd == "emit":
        paths = emit_batches(int(sys.argv[2]) if len(sys.argv) > 2 else 8)
        print(f"Wrote {len(paths)} batch files to {TOLABEL_DIR}")
        print(f"Wrote guide to {GUIDE_PATH}")
    elif cmd == "assemble":
        n, probs = assemble()
        print(f"Assembled {n} labeled turns -> {LABELS_PATH}")
        if probs:
            print(f"{len(probs)} problems:")
            for p in probs[:20]:
                print("  ", p)
