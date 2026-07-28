"""Turn accepted findings/candidates into actual line-anchored edits, apply them
bottom-up so earlier edits never shift a later edit's line numbers, and run
dsl_verify before ever returning the result. Nothing here is written to disk by
this module itself — see run_improve.py for the CLI that does that, gated on
verify() passing.

Four strategies. The first three only ever ADD text (a new anchor, a corrected
ordinal, a new route) and never touch existing say() lines. NATURAL_OPENER is
the first strategy that reworks existing speech, and is scoped narrowly because
of that — see src/dsl_mine.py's module docstring for what was tested and
rejected before landing on this shape (full vocabulary substitution, unrestricted
reduplication mining), and why it stays propose-only forever, same as new
intents / retry steps / splitting an ambiguous default:

  ADD_ANCHORS       an accepted src.dsl_mine.AnchorGap -> append the word to that
                     intent's existing `| Anchors:` line, exact file formatting.
  NATURAL_OPENER    an accepted src.dsl_mine.NaturalOpener -> prepend or double a
                     real customer particle (जी/हां/...) as a say() line's
                     leading word. Never mid-sentence, never a verb, never a
                     compliance-adjacent line, never a bot-initiated line (see
                     dsl_parse.containing_state). Always propose-only.
  REWRITE_ORDINAL    a guardrail_count_mismatch finding -> substitute the ordinal
                     word in custom_guardrails{} prose to match the real step count.
  ADD_GLOBAL_ROUTE   an unrouted_intent finding where handle_<intent>() already
                     exists -> insert a correctly-aligned route into global{}.

Both REWRITE_ORDINAL and ADD_GLOBAL_ROUTE had ZERO real targets on every ABCL
prompt tested (the guardrail already resolves correctly; every intent is already
routed) — they exist as infrastructure for prompts that do have these defects, not
because this specific file needs them today.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from src import dsl_audit, dsl_mine, dsl_parse, dsl_verify

ANCHOR_LINE_RE = dsl_parse.ANCHOR_LINE_RE
ON_INTENT_RE = dsl_parse.ON_INTENT_RE


@dataclass
class Edit:
    kind: str
    ref: str                 # decision_key or finding description, for CHANGES.md
    anchor_line: int         # 0-indexed line in the ORIGINAL text
    mode: str                # "replace_line" | "insert_after"
    new_text: str            # exact full line(s) of new content, no trailing \n
    rationale: str = ""
    evidence: list = field(default_factory=list)
    old_say_text: str | None = None   # set only for edits that reword an existing
                                       # say() line — passed through to
                                       # dsl_verify.verify's allow_say_changes so
                                       # says_preserved permits exactly this line


# --------------------------------------------------------------------- ADD_ANCHORS --
def _find_anchor_line(d: dsl_parse.DSL, intent_name: str) -> int | None:
    it = d.intents.get(intent_name)
    if it is None:
        return None
    for i in range(it.line_start, it.line_end + 1):
        if ANCHOR_LINE_RE.search(d.lines[i]):
            return i
    return None


def make_add_anchors_edit(d: dsl_parse.DSL, gap: "dsl_mine.AnchorGap") -> Edit | None:
    """Single-gap version — safe ONLY when at most one accepted gap targets a given
    intent in the same run. See make_add_anchors_edits_batch for why: two edits
    computed independently both read the SAME original Anchors line and each
    write a full replacement line, so applying both means the second silently
    overwrites the first (apply_edits does blind line replacement, and multiple
    edits sharing one anchor_line is exactly the case it doesn't merge). Kept for
    single-accept callers and tests; run_improve.py must use the batch version
    whenever more than one gap could land on the same intent in one run — which
    is the normal case for "accept several at once"."""
    return _add_anchors_edit_for(d, gap.intent, [gap.word],
                                 [f'"{gap.word}" ({gap.call_count} calls, {gap.lift:.2f}x)'],
                                 gap.examples, gap.decision_key)


def make_add_anchors_edits_batch(d: dsl_parse.DSL, gaps: list) -> list:
    """Group accepted AnchorGap items by intent and emit ONE edit per intent,
    adding all their words together. This is the correct way to apply more than
    one accepted anchor gap in a single run — see make_add_anchors_edit's
    docstring for the bug this avoids (verified: it was real, not hypothetical —
    accepting 3 words each for affirm/query_fee/address_error in one run silently
    kept only the last word per intent until this existed)."""
    from collections import defaultdict
    by_intent = defaultdict(list)
    for g in gaps:
        by_intent[g.intent].append(g)

    out = []
    for intent, group in by_intent.items():
        words = [g.word for g in group]
        rationale_bits = [f'"{g.word}" ({g.call_count} calls, {g.lift:.2f}x)' for g in group]
        evidence = [ex for g in group for ex in g.examples]
        ref = "+".join(g.decision_key for g in group)
        e = _add_anchors_edit_for(d, intent, words, rationale_bits, evidence, ref)
        if e:
            out.append(e)
    return out


def _add_anchors_edit_for(d: dsl_parse.DSL, intent: str, words: list,
                          rationale_bits: list, evidence: list, ref: str) -> Edit | None:
    line_idx = _find_anchor_line(d, intent)
    if line_idx is None:
        return None
    original = d.lines[line_idx]
    m = ANCHOR_LINE_RE.search(original)
    if not m:
        return None
    existing = dsl_parse.ANCHOR_ITEM_RE.findall(m.group(1))
    new_words = [w for w in words if w not in existing]
    if not new_words:
        return None   # all already there — idempotent no-op
    indent = original[:len(original) - len(original.lstrip())]
    new_list = existing + new_words
    quoted = ", ".join(f'"{a}"' for a in new_list)
    new_line = f"{indent}| Anchors: {quoted}"
    return Edit(
        kind="ADD_ANCHORS", ref=ref, anchor_line=line_idx,
        mode="replace_line", new_text=new_line,
        rationale=f"{intent}: " + ", ".join(rationale_bits),
        evidence=evidence,
    )


# ------------------------------------------------------------------ NATURAL_OPENER --
def make_opener_edit(d: dsl_parse.DSL, cand: "dsl_mine.NaturalOpener") -> Edit:
    """One edit per accepted NaturalOpener candidate — deliberately NOT batched
    like make_add_anchors_edits_batch. Two candidates can legitimately target the
    same line (e.g. "जी" vs "हां" as the opener); accepting both in one run must
    conflict, not silently combine into "जी हां, ..." — apply_edits' existing
    ConflictingEditsError (built for the anchor same-line bug) already catches
    this correctly as long as these stay unmerged, one Edit per candidate."""
    return Edit(
        kind="NATURAL_OPENER", ref=cand.decision_key,
        anchor_line=cand.line_idx, mode="replace_line",
        new_text=d.lines[cand.line_idx].replace(cand.old_line, cand.new_line, 1),
        rationale=f'"{cand.particle}" {cand.mechanism} ({cand.call_count} calls, '
                  f"real customer opener frequency)",
        evidence=cand.examples,
        old_say_text=cand.old_line,
    )


# ------------------------------------------------------------------ USECASE --
def make_usecase_edit(d: dsl_parse.DSL, proposal: dict) -> Edit | None:
    """An LLM improvement proposal -> an Edit inserting one or more say() lines
    into the target state, optionally wrapped in an on-intent or if() branch.

    Purely additive: this never rewrites existing speech, so says_preserved stays
    intact without needing allow_say_changes. Multi-line works because
    apply_edits' insert_after puts the whole block in as one element and the
    final "\\n".join expands it correctly."""
    state_name = proposal.get("target_state")
    st = d.states.get(state_name)
    if st is None:
        return None
    lines = [l for l in proposal.get("lines", []) if l and l.strip()]
    if not lines:
        return None

    # Insert BEFORE the state's first transition, not before its closing brace.
    # In this dialect a state's routing (`on intent(...) -> x();`) and its
    # unconditional gotos (`-> y();`) are terminal: once one runs, control has
    # left the state. Anything appended after them is dead code that can never
    # be spoken. Found by simulation — the first version inserted at line_end and
    # produced three perfectly good, completely unreachable lines, which
    # dsl_verify passed because it checks structure, not reachability.
    close_idx = st.line_end
    body_indent = "        "   # states open at 6, bodies at 8 (see dsl_parse docstring)
    for i in range(st.line_start + 1, close_idx):
        stripped = d.lines[i].strip()
        if stripped and not stripped.startswith("//"):
            body_indent = d.lines[i][:len(d.lines[i]) - len(d.lines[i].lstrip())]
            break

    insert_after_idx = close_idx - 1
    depth = 0
    for i in range(st.line_start, close_idx):
        line = d.lines[i]
        code = line.split("//", 1)[0]
        if depth == 1 and i > st.line_start:
            stripped = code.strip()
            if ON_INTENT_RE.search(stripped) or dsl_parse.GOTO_RE.search(stripped):
                insert_after_idx = i - 1   # sits ahead of the first transition
                break
        depth += code.count("{") - code.count("}")

    # "state_start" puts it ahead of all existing speech; the default
    # "before_transitions" keeps it after the existing say() lines. Either way it
    # lands before the first transition — a placement past one is never honoured,
    # because that speech could not be reached.
    if (proposal.get("placement") or "").strip() == "state_start":
        for i in range(st.line_start + 1, close_idx):
            stripped = d.lines[i].split("//", 1)[0].strip()
            if stripped and not stripped.startswith("|"):
                insert_after_idx = min(i - 1, insert_after_idx)
                break

    trigger = (proposal.get("trigger") or "existing").strip()
    say_stmts = [f'{body_indent}say("{l}");' for l in lines]

    if trigger.startswith("on_intent:"):
        intent = trigger.split(":", 1)[1].strip()
        if intent not in d.intents:
            return None          # never emit a route to an undefined intent
        inner = [f'{body_indent}  say("{l}");' for l in lines]
        block = [f'{body_indent}on intent("{intent}") {{'] + inner + [f"{body_indent}}}"]
    elif trigger.startswith("if:"):
        var = trigger.split(":", 1)[1].strip()
        if var not in _session_vars(d):
            return None          # never gate on a variable that doesn't exist
        inner = [f'{body_indent}  say("{l}");' for l in lines]
        block = [f"{body_indent}if ({var}) {{"] + inner + [f"{body_indent}}}"]
    else:
        block = say_stmts

    return Edit(
        kind="USECASE", ref=f"usecase:{state_name}",
        anchor_line=insert_after_idx, mode="insert_after",
        new_text="\n".join(block),
        # NOT truncated. The rationale is the audit trail for a change to
        # customer-facing copy — it cites the specific numbers and quotes behind
        # the decision, and it runs ~1000 chars. An earlier [:300] cap silently
        # cut ~70% of it, leaving mid-sentence fragments in CHANGES.md.
        rationale=proposal.get("rationale", ""),
        evidence=lines,
    )


def _session_vars(d: dsl_parse.DSL) -> set:
    m = re.search(r"session\s*\{(.*?)\n\s*\}", d.text, re.S)
    if not m:
        return set()
    return set(re.findall(r"^\s*(\w+)\s*:", m.group(1), re.M))


# ------------------------------------------------------------------ REWRITE_ORDINAL --
_ORDINAL_WORD = {v: k for k, v in dsl_audit.ORDINALS.items()}


def make_rewrite_ordinal_edit(d: dsl_parse.DSL, finding) -> Edit | None:
    """finding: a dsl_audit.Finding with kind == 'guardrail_count_mismatch'."""
    if not finding.evidence:
        return None
    guardrail_text = finding.evidence[0]
    # locate the exact line in the file (guardrail prose lines are single physical
    # lines in this dialect, so a substring search is reliable)
    line_idx = None
    for i, line in enumerate(d.lines):
        if guardrail_text[:60] in line:
            line_idx = i
            break
    if line_idx is None:
        return None
    m = re.search(r"real step count is (\d+)", finding.detail) or \
        re.search(r"escalates on attempt (\d+)", finding.detail)
    if not m:
        return None
    correct_num = int(m.group(1))
    correct_word = _ORDINAL_WORD.get(correct_num)
    if not correct_word:
        return None
    old_line = d.lines[line_idx]
    wrong_word_match = None
    for word in dsl_audit.ORDINALS:
        if re.search(rf"\b{word}\b", old_line):
            wrong_word_match = word
            break
    if not wrong_word_match:
        return None
    new_line = re.sub(rf"\b{wrong_word_match}\b", correct_word, old_line, count=1)
    return Edit(
        kind="REWRITE_ORDINAL", ref=f"guardrail:{finding.where}", anchor_line=line_idx,
        mode="replace_line", new_text=new_line,
        rationale=f"guardrail said '{wrong_word_match}', real step count needs "
                  f"'{correct_word}'",
    )


# ----------------------------------------------------------------- ADD_GLOBAL_ROUTE --
def make_add_global_route_edit(d: dsl_parse.DSL, intent_name: str) -> Edit | None:
    handler = f"handle_{intent_name}"
    if handler not in d.states:
        return None
    if intent_name in d.global_routes:
        return None   # already routed — idempotent no-op

    # find the global{} block
    global_start = None
    for i, line in enumerate(d.lines):
        if re.match(r"^\s*global\s*\{", line):
            global_start = i
            break
    if global_start is None:
        return None
    close = dsl_parse._block_span(d.lines, global_start)
    route_lines = list(range(global_start + 1, close))
    if not route_lines:
        return None

    # match the file's real alignment: arrows start one column past the longest
    # "on intent("x")" header in this run (see dsl_parse module docstring / the
    # file-format spec this was built against)
    indent = d.lines[route_lines[0]][:len(d.lines[route_lines[0]]) -
                                     len(d.lines[route_lines[0]].lstrip())]
    headers = [f'on intent("{m.group(1)}")'
              for line in route_lines
              for m in [ON_INTENT_RE.search(d.lines[line])] if m]
    new_header = f'on intent("{intent_name}")'
    width = max([len(h) for h in headers] + [len(new_header)])
    new_line = f'{indent}{new_header:<{width}} -> {handler}();'

    insert_at = close - 1   # just before the closing '}' of global{}
    return Edit(
        kind="ADD_GLOBAL_ROUTE", ref=f"unrouted:{intent_name}", anchor_line=insert_at,
        mode="insert_after", new_text=new_line,
        rationale=f'"{intent_name}" is defined and {handler}() exists, but nothing '
                  f"routes to it",
    )


# --------------------------------------------------------------------- application --
class ConflictingEditsError(Exception):
    """Two or more edits target the same replace_line — blind line replacement
    would silently keep only one and drop the rest. Found this exact way: three
    accepted anchor-gap edits for the same intent each independently overwrote
    the previous one, and every earlier test happened to accept only one item
    per intent, so nothing caught it until a real multi-accept run. Callers that
    might legitimately produce more than one edit for one intent (e.g. accepting
    several anchor gaps at once) must pre-merge them — see
    dsl_fix.make_add_anchors_edits_batch — rather than rely on apply_edits to
    reconcile conflicting edits, which it deliberately refuses to do."""


def apply_edits(text: str, edits: list) -> str:
    """Bottom-up (descending anchor_line) so earlier line numbers stay valid."""
    replace_lines = [e.anchor_line for e in edits if e.mode == "replace_line"]
    dupes = {ln for ln in replace_lines if replace_lines.count(ln) > 1}
    if dupes:
        conflicting = [e.ref for e in edits if e.mode == "replace_line" and e.anchor_line in dupes]
        raise ConflictingEditsError(
            f"{len(dupes)} line(s) targeted by more than one edit — refusing to "
            f"silently drop any of them: {conflicting}. Merge same-target edits "
            f"before calling apply_edits (e.g. dsl_fix.make_add_anchors_edits_batch "
            f"for anchor additions).")

    lines = text.splitlines()
    for e in sorted(edits, key=lambda e: -e.anchor_line):
        if e.mode == "replace_line":
            lines[e.anchor_line] = e.new_text
        elif e.mode == "insert_after":
            lines.insert(e.anchor_line + 1, e.new_text)
    out = "\n".join(lines)
    if text.endswith("\n") and not out.endswith("\n"):
        out += "\n"
    return out


def apply_and_verify(dsl_path, edits: list, token_budget: int | None = None):
    """Returns (new_text, VerifyResult). Caller decides whether to write it —
    this never touches disk. allow_say_changes for dsl_verify is derived
    automatically from the edits themselves (Edit.old_say_text) — only the exact
    lines a run's own accepted edits intentionally reword are ever permitted to
    change; says_preserved stays maximally strict for everything else."""
    d = dsl_parse.parse(dsl_path)
    old_text = d.text
    new_text = apply_edits(old_text, edits)
    allow_say_changes = [e.old_say_text for e in edits if e.old_say_text]
    result = dsl_verify.verify(old_text, new_text, token_budget=token_budget,
                               allow_say_changes=allow_say_changes)
    return new_text, result
