"""Mechanical safety gate for an edited DSL prompt.

This is the piece that makes automated prompt editing trustworthy: every check
below is one that was run by hand during the manual improvement pass, and every
one is fully deterministic. An edit that fails any BLOCKING check must never be
written to disk or shipped, regardless of how good the reasoning behind it was.

Blocking checks:
  braces_balanced      the prompt still parses as balanced blocks
  says_preserved       no pre-existing say() line was removed or reworded
  no_dangling_routes   no route points at a state or intent that does not exist
  intent_wired         every intent added is defined AND routed AND has a handler
  token_budget         the result is within the caller's token ceiling

Advisory (reported, non-blocking):
  say_added / say_changed counts, token delta, state and intent deltas.

`says_preserved` is the important one. Scripted speech is the product; an LLM
rewriting a prompt can silently reword a line in a way no structural check would
catch, so existing say() text is treated as immutable unless the caller explicitly
allows a specific line to change.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from src import dsl_parse

SAY_RE = dsl_parse.SAY_RE


@dataclass
class VerifyResult:
    ok: bool
    blocking: list = field(default_factory=list)
    advisory: list = field(default_factory=list)

    def render(self) -> str:
        lines = ["PASS" if self.ok else "FAIL"]
        for b in self.blocking:
            lines.append(f"  BLOCKING: {b}")
        for a in self.advisory:
            lines.append(f"  note: {a}")
        return "\n".join(lines)


def _brace_balance(text: str):
    depth, line = 0, 1
    for ch in text:
        if ch == "\n":
            line += 1
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                return False, f"unmatched '}}' at line {line}"
    if depth != 0:
        return False, f"{depth} unclosed '{{' at end of file"
    return True, ""


def _count_tokens(text: str):
    try:
        import tiktoken
        return len(tiktoken.get_encoding("cl100k_base").encode(text))
    except Exception:  # noqa: BLE001
        return None


def _dangling_refs(d) -> list:
    """Routes/gotos pointing at a state or intent that doesn't exist."""
    if d is None:
        return []
    states = set(d.states)
    intents = set(d.intents)
    out = []
    for name, st in d.states.items():
        all_routes = st.intent_routes + st.nested_routes
        for tgt in [t for _, t in all_routes if t] + st.gotos:
            if tgt not in states:
                out.append(f"{name}() -> {tgt}()")
        for i, _ in all_routes:
            if i != "default" and i not in intents:
                out.append(f'{name}() on intent("{i}")')
    for i, tgt in d.global_routes.items():
        if tgt not in states:
            out.append(f'global intent("{i}") -> {tgt}()')
        if i not in intents:
            out.append(f'global intent("{i}") undefined')
    return out


def _dead_says(d) -> list:
    """say() texts sitting after a state's first top-level terminal transition.
    Only depth-1 transitions end the state — one inside an `on intent(...) { }`
    block or a `step { }` belongs to that inner scope, not the state itself."""
    if d is None:
        return []
    out = []
    for st in d.states.values():
        depth = 0
        seen_transition = False
        for i in range(st.line_start, min(st.line_end + 1, len(d.lines))):
            code = d.lines[i].split("//", 1)[0]
            stripped = code.strip()
            if depth == 1 and i > st.line_start:
                if seen_transition:
                    for s in dsl_parse.SAY_RE.findall(stripped):
                        out.append(s)
                elif (dsl_parse.ON_INTENT_RE.search(stripped)
                      or dsl_parse.GOTO_RE.search(stripped)):
                    # an inline `on intent(...) {` opens a block rather than
                    # jumping, so it does not end the state
                    if not stripped.endswith("{"):
                        seen_transition = True
            depth += code.count("{") - code.count("}")
    return out


def verify(old_text: str, new_text: str, token_budget: int | None = None,
           allow_say_changes: list | None = None) -> VerifyResult:
    res = VerifyResult(ok=True)
    allow = set(allow_say_changes or [])

    ok, msg = _brace_balance(new_text)
    if not ok:
        res.blocking.append(f"braces_balanced: {msg}")

    old_says = SAY_RE.findall(old_text)
    new_says = SAY_RE.findall(new_text)
    removed = [s for s in set(old_says) - set(new_says) if s not in allow]
    added = list(set(new_says) - set(old_says))
    if removed:
        res.blocking.append(
            f"says_preserved: {len(removed)} existing say() line(s) removed or "
            f"reworded, e.g. {removed[0][:70]!r}")
    res.advisory.append(f"say() lines: {len(old_says)} -> {len(new_says)} "
                        f"(+{len(added)} added)")
    for s in added[:6]:
        res.advisory.append(f"  + {s[:80]}")

    # structural integrity of the NEW text, and of the OLD text (to know which
    # intents are genuinely new). Both parsed properly via dsl_parse — this used
    # to call a function (`parse_text_fallback`) that never existed, so d_old was
    # always None and unused, and separately computed "old intents" with a
    # confused expression (`SAY_RE.sub(...) and {...}`) that happened to work by
    # accident but let say() BODIES leak into the old-intent name set, which could
    # make the intent_wired check below miss a genuinely unwired new intent.
    import tempfile
    import pathlib

    def _parse_text(text):
        with tempfile.NamedTemporaryFile("w", suffix=".raven", delete=False) as fh:
            fh.write(text)
            tmp = pathlib.Path(fh.name)
        try:
            return dsl_parse.parse(tmp)
        finally:
            tmp.unlink(missing_ok=True)

    d_new = _parse_text(new_text)
    d_old = _parse_text(old_text)

    states = set(d_new.states)
    intents = set(d_new.intents)
    dangling = _dangling_refs(d_new)
    # Only NEWLY-introduced breakage blocks. A defect that was already in the
    # caller's file (the real ABCL original ships a global route to an undefined
    # silence_check()) must not permanently wedge an autonomous run — otherwise
    # someone else's old bug means the tool can never improve anything. Same
    # rule already applied to unreachable_say. Pre-existing breakage is still
    # REPORTED, just as advisory.
    pre_existing = _dangling_refs(d_old)
    introduced = [x for x in dangling if x not in pre_existing]
    if introduced:
        res.blocking.append(
            f"no_dangling_routes: {len(introduced)} NEW broken reference(s): "
            + "; ".join(introduced[:4]))
    still_broken = [x for x in dangling if x in pre_existing]
    if still_broken:
        res.advisory.append(
            f"pre-existing broken reference(s) left untouched ({len(still_broken)}): "
            + "; ".join(still_broken[:3]))

    # any NEW intent must be fully wired: defined + routed + handler exists
    old_intents = set(d_old.intents)
    new_intent_names = intents - old_intents
    for i in sorted(new_intent_names):
        routed = i in d_new.global_routes or any(
            i == ri for st in d_new.states.values()
            for ri, _ in st.intent_routes + st.nested_routes)
        if not routed:
            res.blocking.append(
                f"intent_wired: new intent '{i}' is defined but never routed")

    # unreachable speech: a say() placed after a state's first terminal transition
    # can never run. Found the hard way — three well-written generated lines were
    # applied, passed every other check here, and were dead code. Only NEW
    # occurrences block, so a pre-existing quirk in a client's file doesn't
    # permanently wedge the pipeline.
    old_dead = _dead_says(d_old)
    new_dead = _dead_says(d_new)
    introduced = [s for s in new_dead if s not in old_dead]
    if introduced:
        res.blocking.append(
            f"unreachable_say: {len(introduced)} new say() line(s) placed after a "
            f"terminal transition and can never be spoken, e.g. {introduced[0][:60]!r}")

    n_old, n_new = _count_tokens(old_text), _count_tokens(new_text)
    if n_old is not None and n_new is not None:
        res.advisory.append(f"tokens: {n_old} -> {n_new} ({n_new - n_old:+d})")
        if token_budget is not None and n_new > token_budget:
            res.blocking.append(
                f"token_budget: {n_new} tokens exceeds budget of {token_budget}")
    else:
        res.advisory.append("tokens: tiktoken unavailable, budget not enforced")

    res.advisory.append(f"states: {len(states)}   intents: {len(intents)}")
    res.ok = not res.blocking
    return res


if __name__ == "__main__":
    import sys
    old = open(sys.argv[1]).read()
    new = open(sys.argv[2]).read()
    budget = int(sys.argv[3]) if len(sys.argv) > 3 else None
    print(verify(old, new, token_budget=budget).render())
