"""Parse a .raven DSL agent prompt into a structured object.

This is the front half of the automated prompt-improvement loop (see run_improve.py):
before anything can audit or patch a prompt, it has to actually understand its
structure rather than treat it as text. Deliberately tolerant — this parses the
dialect as it is actually written today (see abcl-sop-content-v4.raven), not a
formal grammar, and records line spans so a patch can be applied surgically.

What it extracts:
  intents{}     -> name, prose lines, anchor phrases, line span
  flow{}        -> states: say() lines, step{} count, transitions, $$objection/$$entry
  global{}      -> intent -> handler routing
  tools{}       -> declared tool names
  guardrails    -> the custom_guardrails prose lines (audited for consistency)

Not a validator: parse() reports what IS there. src/dsl_audit.py decides what's wrong.

Routes are depth-aware: `State.intent_routes` holds only routes at the state's own
top level (depth 1 — directly inside the state's braces); anything nested one level
deeper (inside a `step {}` or an inline `on intent("x") { ... }` block) goes into
`State.nested_routes` instead. This is what lets `default_equals_affirm` (see
dsl_audit.py) tell apart a real defect — `default` and `affirm` routed to the same
target at the SAME level — from a state that was already fixed by nesting a
clarifier, where the top-level `default` has no target at all (it opens a block)
and the nested `default` inside that block is a different, later decision.
Referential-integrity checks (does this route point at a real state/intent) should
still scan `intent_routes + nested_routes` combined — nesting doesn't make a
dangling reference valid.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

SAY_RE = re.compile(r'say\("((?:[^"\\]|\\.)*)"')
ON_INTENT_RE = re.compile(r'on\s+intent\("([^"]+)"\)\s*(?:->\s*(\w+)\s*\(\s*\))?')
GOTO_RE = re.compile(r'->\s*(\w+)\s*\(\s*\)')
TOOL_CALL_RE = re.compile(r'tool\.(\w+)\s*\(')
ANCHOR_LINE_RE = re.compile(r'\|\s*Anchors?:\s*(.+)$')
ANCHOR_ITEM_RE = re.compile(r'"([^"]*)"')


@dataclass
class Intent:
    name: str
    prose: list = field(default_factory=list)
    anchors: list = field(default_factory=list)
    line_start: int = 0
    line_end: int = 0


@dataclass
class State:
    name: str
    is_entry: bool = False
    is_objection: bool = False
    says: list = field(default_factory=list)
    step_count: int = 0
    # (intent_name | "default", target_state_or_None) — None target = inline block.
    # TOP-LEVEL ONLY (depth 1, directly inside the state) — see module docstring.
    intent_routes: list = field(default_factory=list)
    # same shape as intent_routes, but for anything nested one level deeper
    # (inside step{} or an inline on-intent block)
    nested_routes: list = field(default_factory=list)
    gotos: list = field(default_factory=list)     # unconditional -> target()
    tool_calls: list = field(default_factory=list)
    line_start: int = 0
    line_end: int = 0
    body: str = ""


@dataclass
class DSL:
    path: Path
    text: str
    intents: dict = field(default_factory=dict)
    states: dict = field(default_factory=dict)
    global_routes: dict = field(default_factory=dict)
    tools: list = field(default_factory=list)
    guardrails: list = field(default_factory=list)

    @property
    def lines(self) -> list:
        return self.text.splitlines()

    def all_says(self) -> list:
        return SAY_RE.findall(self.text)


def _block_span(lines: list, open_idx: int) -> int:
    """Given the index of a line containing the opening '{' of a block, return the
    index of the line holding its matching '}'. Brace-counting, quote-aware enough
    for this dialect (say() strings can contain braces in theory; none do today)."""
    depth = 0
    started = False
    for i in range(open_idx, len(lines)):
        line = lines[i]
        # strip // comments so a commented brace never shifts the count
        code = line.split("//", 1)[0]
        for ch in code:
            if ch == "{":
                depth += 1
                started = True
            elif ch == "}":
                depth -= 1
        if started and depth <= 0:
            return i
    return len(lines) - 1


def _find_top_block(lines: list, name: str) -> tuple:
    """Locate a top-level named block, e.g. 'intents' / 'flow' / 'custom_guardrails'.
    Returns (start_idx, end_idx) inclusive, or (None, None)."""
    pat = re.compile(rf"^\s*{re.escape(name)}\s*\{{")
    for i, line in enumerate(lines):
        if pat.match(line):
            return i, _block_span(lines, i)
    return None, None


def _parse_intents(lines: list, start: int, end: int) -> dict:
    intents = {}
    i = start + 1
    entry_re = re.compile(r"^\s*(\w+)\s*\{")
    while i < end:
        m = entry_re.match(lines[i])
        if not m:
            i += 1
            continue
        name = m.group(1)
        close = _block_span(lines, i)
        it = Intent(name=name, line_start=i, line_end=close)
        for j in range(i + 1, close):
            raw = lines[j].strip()
            am = ANCHOR_LINE_RE.search(raw)
            if am:
                it.anchors = ANCHOR_ITEM_RE.findall(am.group(1))
            elif raw.startswith("|"):
                it.prose.append(raw.lstrip("| ").strip())
        intents[name] = it
        i = close + 1
    return intents


def _parse_states(lines: list, start: int, end: int) -> tuple:
    """Returns (states, global_routes)."""
    states = {}
    global_routes = {}
    state_re = re.compile(r"^\s*(\w+)\s*\(\s*\)\s*\{")
    i = start + 1
    pending_objection = False
    pending_entry = False
    while i < end:
        raw = lines[i]
        stripped = raw.strip()
        if stripped.startswith("$$objection"):
            pending_objection = True
            i += 1
            continue
        if stripped.startswith("$$entry"):
            pending_entry = True
            i += 1
            continue
        # the global{} routing block
        if re.match(r"^\s*global\s*\{", raw):
            close = _block_span(lines, i)
            for j in range(i + 1, close):
                gm = ON_INTENT_RE.search(lines[j])
                if gm and gm.group(2):
                    global_routes[gm.group(1)] = gm.group(2)
            i = close + 1
            continue
        m = state_re.match(raw)
        if not m:
            i += 1
            continue
        name = m.group(1)
        close = _block_span(lines, i)
        body = "\n".join(lines[i:close + 1])
        st = State(
            name=name, line_start=i, line_end=close, body=body,
            is_objection=pending_objection, is_entry=pending_entry,
        )
        pending_objection = False
        pending_entry = False
        st.says = SAY_RE.findall(body)
        st.step_count = len(re.findall(r"^\s*step\s*\{", body, flags=re.M))
        st.tool_calls = TOOL_CALL_RE.findall(body)

        # Depth-aware route collection. `depth` counts braces seen so far in the
        # state; a line's OWN route pattern is attributed to the depth in effect
        # BEFORE that line's braces are counted, so the line "on intent("default") {"
        # itself is depth 1 (it belongs to the state's top level — it's the one
        # that OPENS depth 2), while everything inside that block is depth 2.
        depth = 0
        for line in body.splitlines():
            line_depth = depth
            if line_depth == 1:
                om = ON_INTENT_RE.search(line)
                if om:
                    st.intent_routes.append((om.group(1), om.group(2)))
                elif "on intent" not in line:
                    for tgt in GOTO_RE.findall(line):
                        st.gotos.append(tgt)
            elif line_depth > 1:
                om = ON_INTENT_RE.search(line)
                if om:
                    st.nested_routes.append((om.group(1), om.group(2)))
                elif "on intent" not in line:
                    for tgt in GOTO_RE.findall(line):
                        st.gotos.append(tgt)   # nested gotos still tracked flat (unchanged behaviour)
            code = line.split("//", 1)[0]
            depth += code.count("{") - code.count("}")
        states[name] = st
        i = close + 1
    return states, global_routes


def parse(path) -> DSL:
    path = Path(path)
    text = path.read_text()
    lines = text.splitlines()
    dsl = DSL(path=path, text=text)

    s, e = _find_top_block(lines, "intents")
    if s is not None:
        dsl.intents = _parse_intents(lines, s, e)

    s, e = _find_top_block(lines, "flow")
    if s is not None:
        dsl.states, dsl.global_routes = _parse_states(lines, s, e)

    s, e = _find_top_block(lines, "tools")
    if s is not None:
        for j in range(s + 1, e):
            tm = re.match(r"\s*(\w+)\s*\(", lines[j])
            if tm:
                dsl.tools.append(tm.group(1))

    s, e = _find_top_block(lines, "custom_guardrails")
    if s is not None:
        for j in range(s + 1, e):
            raw = lines[j].strip()
            if raw.startswith("|"):
                dsl.guardrails.append(raw.lstrip("| ").strip())

    return dsl


if __name__ == "__main__":
    import sys
    d = parse(sys.argv[1])
    print(f"intents: {len(d.intents)}   states: {len(d.states)}   "
          f"global routes: {len(d.global_routes)}   tools: {len(d.tools)}")
    print(f"say() lines: {len(d.all_says())}   guardrail lines: {len(d.guardrails)}")
    print("\nobjection states (name, steps):")
    for n, s in d.states.items():
        if s.is_objection:
            print(f"  {n}: {s.step_count} step(s)")
