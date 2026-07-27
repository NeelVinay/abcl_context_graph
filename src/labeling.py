"""Phase 0 of the distillation plan: produce Claude-quality labels for every turn.

Claude (the teacher) labels each segmented turn with the correct base intent,
keywords, sentiment, and tool. A small local model (the student) later trains to
imitate these labels. This module handles the I/O around that:

  build_guide(tax)  -> the labeling contract (taxonomy + examples) given to labelers
  emit_batches(tax) -> split that domain's cached calls into batch files to label
  assemble(tax)     -> validate labeler outputs and merge into <gold>/labels.jsonl

Three domains are supported via a Taxonomy object (they share the same cache dir but
own disjoint call sets):
  abcl      -> loan-application calls   (src/extract.py taxonomy, data/gold)
  justdial  -> lead-gen support calls   (src/justdial_taxonomy.py, data/gold_justdial)
  generic   -> any new client, broad cross-client buckets (src/generic_taxonomy.py,
               data/gold_generic) — see src/generic_taxonomy.py for how to onboard
               a new client's transcripts into this domain.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import config
from src import extract, generic_taxonomy, justdial_taxonomy


@dataclass
class Taxonomy:
    name: str
    intent_library: list
    actions: dict
    sentiment_lexicon: list
    tool_rules: dict
    gold_dir: Path
    owns: Callable[[str], bool]   # does this call_id/stem belong to this domain?

    @property
    def valid_base(self):
        return {n for n, _, _ in self.intent_library} | {"other"}

    @property
    def action_to_base(self):
        return {a: base for base, pair in self.actions.items() for a in pair.values()}

    @property
    def valid_sentiment(self):
        return {s for s, _ in self.sentiment_lexicon} | {"neutral"}

    @property
    def valid_tool(self):
        return {t for t, _ in self.tool_rules.values()} | {None}


ABCL = Taxonomy(
    name="ABCL loan-application calls",
    intent_library=extract.INTENT_LIBRARY, actions=extract.ACTIONS,
    sentiment_lexicon=extract.SENTIMENT_LEXICON, tool_rules=extract.TOOL_RULES,
    gold_dir=config.DATA / "gold",
    # NOT just "not JustDial" — that would also swallow new-client (GEN-*) transcripts.
    owns=lambda stem: not stem.startswith("LCS") and not stem.startswith("GEN-"),
)
JUSTDIAL = Taxonomy(
    name="JustDial lead-generation support calls",
    intent_library=justdial_taxonomy.INTENT_LIBRARY, actions=justdial_taxonomy.ACTIONS,
    sentiment_lexicon=extract.SENTIMENT_LEXICON, tool_rules=justdial_taxonomy.TOOL_RULES,
    gold_dir=config.DATA / "gold_justdial",
    owns=lambda stem: stem.startswith("LCS"),
)
GENERIC = Taxonomy(
    name="Generic cross-client calls (broad buckets)",
    intent_library=generic_taxonomy.INTENT_LIBRARY, actions=generic_taxonomy.ACTIONS,
    sentiment_lexicon=extract.SENTIMENT_LEXICON, tool_rules=generic_taxonomy.TOOL_RULES,
    gold_dir=config.DATA / "gold_generic",
    # Any client dropped in under the GEN-<client>-<id> naming convention — see
    # src/generic_taxonomy.py for onboarding a new client.
    owns=lambda stem: stem.startswith("GEN-"),
)
TAXONOMIES = {"abcl": ABCL, "justdial": JUSTDIAL, "generic": GENERIC}


def _dirs(tax: Taxonomy):
    return (tax.gold_dir / "_tolabel", tax.gold_dir / "_labeled",
            tax.gold_dir / "labels.jsonl", tax.gold_dir / "LABELING_GUIDE.md")


def build_guide(tax: Taxonomy) -> str:
    """Human/agent-readable labeling contract, generated from the live taxonomy."""
    out = [f"# Labeling guide — {tax.name} (Hinglish)\n",
           "You are the TEACHER creating ground-truth labels. For EACH turn assign the "
           "single best `base_intent` from the list below, the signal `keywords` "
           "(verbatim spans copied from the turn text), the customer `sentiment`, and any "
           "`tool` call.\n",
           "Rules:",
           "- `base_intent` MUST be exactly one value from the list (or `other` if nothing "
           "fits — then add `suggested_intent` with a short new name).",
           "- `keywords`: 1-5 short phrases COPIED VERBATIM from the turn text. No "
           "paraphrasing, no invented words, no names/PII, and NO number sequences "
           "(phone numbers, OTPs, spelled-out digits like 'नाइन डबल टू'). If nothing is "
           "salient, use [].",
           "- `sentiment`: ONLY for customer turns, else null. One of: "
           f"{sorted(tax.valid_sentiment)}. Use `neutral` if no clear emotion.",
           "- `tool`: ONLY for agent turns where an actual system action is performed "
           f"(not merely mentioned). One of: {sorted(t for t in tax.valid_tool if t)} or null.",
           "- Judge by MEANING and context, not keyword presence. The transcript is Hinglish "
           "(mixed Hindi/Devanagari + romanized English) and may have ASR errors.",
           "- If a turn is unintelligible ASR garble (repeated/nonsensical tokens, no clear "
           "meaning), label `base_intent` = `other`, `keywords` = [], and move on — do NOT "
           "over-analyze it.\n",
           "## Valid base intents (with example utterances)\n"]
    for name, kws, examples in tax.intent_library:
        pair = tax.actions.get(name, {})
        roles = f"agent→`{pair.get('agent','?')}`, customer→`{pair.get('customer','?')}`"
        ex = " | ".join(examples[:3])
        out.append(f"- **{name}** ({roles})\n    e.g. {ex}")
    out.append("\n## Output format (per call): JSON")
    out.append("```json")
    out.append('{"call_id": "<id>", "turns": [')
    out.append('  {"index": 0, "speaker": "customer", "base_intent": "report_no_leads", '
               '"keywords": ["लीड नहीं आ"], "sentiment": "frustrated", "tool": null}')
    out.append(']}')
    out.append("```")
    return "\n".join(out)


def _segmented_turns(call: dict) -> list[dict]:
    return [{"index": t["index"], "speaker": t["speaker"], "text": t["text"]}
            for t in call["turns"]]


def _owned_caches(tax: Taxonomy):
    """Cache files belonging to this domain (JD = LCS-*, ABCL = the rest)."""
    return [f for f in sorted(config.CACHE_DIR.glob("*.json")) if tax.owns(f.stem)]


def emit_batches(tax: Taxonomy, per_batch: int = 8, min_turns: int = 3) -> list[Path]:
    """Read this domain's cached extractions, write batch files of stripped turns.
    Skips near-empty calls (< min_turns) — nothing labelable there, just wasted tokens."""
    tolabel, _, _, guide = _dirs(tax)
    tolabel.mkdir(parents=True, exist_ok=True)
    calls, skipped = [], 0
    for f in _owned_caches(tax):
        c = json.loads(f.read_text())
        turns = _segmented_turns(c)
        if len(turns) < min_turns:
            skipped += 1
            continue
        calls.append({"call_id": c["call_id"], "turns": turns})
    if skipped:
        print(f"[{tax.name}] skipped {skipped} near-empty call(s) (< {min_turns} turns)")
    paths = []
    for i in range(0, len(calls), per_batch):
        batch = calls[i:i + per_batch]
        p = tolabel / f"batch_{i // per_batch:02d}.json"
        p.write_text(json.dumps(batch, ensure_ascii=False, indent=2))
        paths.append(p)
    guide.write_text(build_guide(tax))
    return paths


def _cache_text_index(tax: Taxonomy) -> dict:
    idx = {}
    for f in _owned_caches(tax):
        c = json.loads(f.read_text())
        for t in c["turns"]:
            idx[(c["call_id"], t["index"])] = t["text"]
    return idx


def assemble(tax: Taxonomy) -> tuple[int, list[str]]:
    """Validate every labeled batch and merge into <gold>/labels.jsonl.

    MERGES with whatever is already at labels_path (keyed by call_id+index) rather
    than overwriting it — the `generic` taxonomy's gold file also gets rows from
    src/generic_bootstrap.py (existing ABCL/JustDial gold recoded into broad
    buckets); a naive overwrite here would silently wipe those out every time a new
    client's batches are assembled. New rows for an existing key win (re-labeling
    a call replaces its old label)."""
    _, labeled_dir, labels_path, _ = _dirs(tax)
    existing_rows = []
    if labels_path.exists():
        existing_rows = [json.loads(l) for l in labels_path.read_text().splitlines() if l.strip()]
    rows_by_key = {(r["call_id"], r["index"]): r for r in existing_rows}
    rows, problems = [], []
    text_idx = _cache_text_index(tax)
    dropped_kw = 0
    for f in sorted(labeled_dir.glob("*.json")):
        try:
            data = json.loads(f.read_text())
        except Exception as e:  # noqa: BLE001
            problems.append(f"{f.name}: unreadable ({e})")
            continue
        for call in data:
            cid = call.get("call_id")
            for t in call.get("turns", []):
                b = t.get("base_intent")
                if b not in tax.valid_base:
                    b = tax.action_to_base.get(b)      # recover action-form labels
                if b not in tax.valid_base:
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
                row = {
                    "call_id": cid, "index": t["index"], "speaker": t["speaker"],
                    "base_intent": b, "keywords": kws,
                    "sentiment": t.get("sentiment"), "tool": t.get("tool"),
                    "suggested_intent": t.get("suggested_intent"),
                }
                rows.append(row)
                rows_by_key[(cid, t["index"])] = row
    labels_path.write_text("\n".join(json.dumps(r, ensure_ascii=False)
                                     for r in rows_by_key.values()))
    if dropped_kw:
        problems.append(f"(info) dropped {dropped_kw} non-verbatim keywords")
    return len(rows), problems


if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else "emit"
    dom = sys.argv[2] if len(sys.argv) > 2 else "abcl"
    tax = TAXONOMIES[dom]
    if cmd == "emit":
        per = int(sys.argv[3]) if len(sys.argv) > 3 else 8
        paths = emit_batches(tax, per)
        tolabel, _, _, guide = _dirs(tax)
        print(f"[{dom}] wrote {len(paths)} batch files to {tolabel}")
        print(f"[{dom}] wrote guide to {guide}")
    elif cmd == "assemble":
        n, probs = assemble(tax)
        _, _, labels_path, _ = _dirs(tax)
        print(f"[{dom}] assembled {n} labeled turns -> {labels_path}")
        for p in probs[:20]:
            print("  ", p)
