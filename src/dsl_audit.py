"""Deterministic audit of a DSL prompt against a client's real call data.

This is the diagnosis half of the automated improvement loop. It produces a
structured findings list; src/dsl_patch.py turns findings into edits. Nothing here
calls an LLM or guesses — every finding is either a structural fact about the DSL
or a measurable fact about the transcripts, so findings can be trusted and diffed
run over run.

Findings carry a `severity`:
  bug      structural defect, mechanically certain (e.g. a route to a state that
           does not exist)
  risk     a strong smell that is mechanically detectable but needs judgment to
           confirm (e.g. an unclear reply routed the same as explicit consent)
  gap      the data shows something the prompt has no handling for
  review   surfaced for a human/LLM to judge; deliberately NOT asserted as wrong

Design note: checks are written to be honest about their own certainty. Anything
requiring interpretation is `risk`/`review`, never `bug`, so an automated patch
step can be configured to act only on what is provably broken.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field, asdict

import config
from src import dsl_parse

ORDINALS = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5}

# DSL intent name -> observed (context-graph) intent names, where the two vocabularies
# genuinely differ and no name-token match can bridge them. Kept explicit rather than
# guessed: a wrong alias silently produces a wrong frequency, and a wrong frequency is
# what drives (or suppresses) an escalation_burn finding. Anything absent here is
# reported as "frequency unknown" instead of being approximated.
#
# Each entry below was verified by reading a real sample of the observed intent's
# turns, not assumed from the names looking similar. Five candidate aliases were
# tested and REJECTED — kept here, not silently dropped, so the same mistake isn't
# re-made on a future edit:
#   sms_not_received -> customer_report_sms_received   SYSTEMATICALLY INVERTED.
#       Sampled turns ("अभी आ गया", "message आ गया madam") mean the SMS ARRIVED —
#       the opposite of what sms_not_received means. Using this would report
#       sms_not_received's frequency as high specifically WHEN it's rare.
#   already_applied -> customer_report_done   WRONG CONCEPT, not just imprecise.
#       538 occurrences; sampled turns ("हो गया", "click किया मैं", "लिख दिया")
#       mean "I completed this form FIELD", not "I already completed this entire
#       application before this call." Using it would report already_applied at
#       roughly a 15x inflated, meaningless frequency.
#   security_concern -> customer_express_distrust   WRONG CONCEPT for a meaningful
#       share of the bucket. Read all 42 sampled turns: a real chunk ("आप AI हो या
#       real person हो", "क्या आप एक AI हो या इंसान") is actually is_bot_query
#       traffic — a DIFFERENT intent this DSL already distinguishes — not fraud/
#       security doubt. Conflating them would silently merge two intents the
#       prompt author deliberately kept separate.
#   salaried / self_employed -> customer_state_employment_type   UNDISTINGUISHABLE.
#       Both DSL intents map to the SAME single observed label, so both would
#       report the identical count — not imprecise, actively misleading, since it
#       implies a distinction the data can't actually support.
INTENT_ALIASES = {
    "abcl": {
        "repeat_request": ["customer_unclear"],
        "query_fee": ["customer_query_fee"],
        "address_error": ["customer_report_address_error"],
        # Verified by reading 15 real samples ("बोलिए", "कर दो", "आगे बढ़कर") —
        # genuinely on-topic agreement/proceed phrases, no mixed signal found.
        "affirm": ["customer_agree"],
        # Verified by reading 8 real samples — all "एक minute ma'am open कर रहा
        # है" / "wait wait" / "मुझे दो minute दीजिए". Matches the intent's own
        # description ("Brief pause, staying on the line") exactly. 195 turns.
        "hold": ["customer_request_wait"],
    },
}

# Candidates examined and DELIBERATELY REJECTED. Recorded so nobody re-adds them
# from name similarity — every one of these looked plausible until real samples
# were read. The rule this whole table follows: a number that's wrong is worse
# than no number, because it silently drives findings and mined anchors.
#
#   security_concern / is_bot_query <- customer_express_distrust
#       42 turns, but a mixed bucket: only 17% are AI/bot questions, ~35% are
#       genuine fraud worry ("यह कोई fraud तो नहीं है?"), and the rest is network
#       trouble, CIBIL doubts and link failures. Too impure for either intent.
#   already_applied <- customer_report_applied
#       36 turns, all clean — but they mean "I just clicked Apply Now", i.e. form
#       progress, NOT "I already have an application with you". Opposite meaning.
#   wants_more_amount <- customer_react_to_final_offer / customer_ask_query
#       Both mostly narrate what's on screen or ask payment questions; only ~2 in
#       7 sampled turns actually ask for a higher amount.
#   salaried / self_employed <- customer_state_employment_type
#       One label covers BOTH, so it cannot map to either without inventing a
#       split the classifier never made.


@dataclass
class Finding:
    kind: str
    severity: str
    where: str            # state / intent name, or "-"
    detail: str
    evidence: list = field(default_factory=list)
    line: int = 0


# ---------------------------------------------------------------- structural --
def audit_structure(d: dsl_parse.DSL) -> list:
    out = []
    intent_names = set(d.intents)
    state_names = set(d.states)

    referenced_intents = set(d.global_routes)
    targeted_states = set(d.global_routes.values())

    # Referential-integrity checks (does this reference point at something real)
    # combine intent_routes + nested_routes: nesting changes what a route MEANS
    # (see dsl_parse's default_equals_affirm distinction) but doesn't make a
    # dangling reference valid, so a route to a bogus intent/state is a bug at
    # any depth.
    for name, st in d.states.items():
        all_routes = st.intent_routes + st.nested_routes
        for intent, target in all_routes:
            if intent != "default":
                referenced_intents.add(intent)
            if target:
                targeted_states.add(target)
        targeted_states.update(st.gotos)

    # 1. route to an intent that was never defined
    for name, st in d.states.items():
        for intent, _ in st.intent_routes + st.nested_routes:
            if intent != "default" and intent not in intent_names:
                out.append(Finding(
                    "undefined_intent_ref", "bug", name,
                    f'state routes on intent("{intent}") but no such intent is defined',
                    line=st.line_start + 1))
    for intent in d.global_routes:
        if intent not in intent_names:
            out.append(Finding(
                "undefined_intent_ref", "bug", "global",
                f'global routes on intent("{intent}") but no such intent is defined'))

    # 2. route to a state that does not exist
    for name, st in d.states.items():
        all_routes = st.intent_routes + st.nested_routes
        for tgt in [t for _, t in all_routes if t] + st.gotos:
            if tgt not in state_names:
                out.append(Finding(
                    "missing_state", "bug", name,
                    f"transitions to {tgt}() which is not defined",
                    line=st.line_start + 1))
    for intent, tgt in d.global_routes.items():
        if tgt not in state_names:
            out.append(Finding(
                "missing_state", "bug", "global",
                f'intent("{intent}") routes to {tgt}() which is not defined'))

    # 3. intent defined but never routed anywhere — dead weight in the prompt
    for name in intent_names - referenced_intents:
        out.append(Finding(
            "unrouted_intent", "risk", name,
            "intent is defined but never routed from global{} or any state; "
            "it can classify but can never change behaviour",
            line=d.intents[name].line_start + 1))

    # 4. state never reachable
    for name, st in d.states.items():
        if not st.is_entry and name not in targeted_states:
            out.append(Finding(
                "unreachable_state", "risk", name,
                "state is never targeted by any transition and is not the entry state",
                line=st.line_start + 1))

    # 5. an unclear reply routed identically to explicit consent.
    #    Mechanically crisp and it is exactly the loan_intro() defect: when
    #    default and affirm land on the same target, ambiguity is silently
    #    treated as a yes.
    for name, st in d.states.items():
        routes = {i: t for i, t in st.intent_routes if t}
        if "default" in routes and "affirm" in routes and routes["default"] == routes["affirm"]:
            out.append(Finding(
                "default_equals_affirm", "risk", name,
                f'unclear replies and explicit "affirm" both route to '
                f'{routes["default"]}() — an ambiguous answer is treated as consent',
                line=st.line_start + 1))

    # 6. objection state that escalates after very few attempts.
    #    Compared against the median across objection states rather than a
    #    hardcoded number, so the norm is learned from the prompt itself.
    objections = {n: s for n, s in d.states.items() if s.is_objection}
    if len(objections) >= 3:
        counts = sorted(s.step_count for s in objections.values())
        median = counts[len(counts) // 2]
        for name, st in objections.items():
            escalates = any("connect_rm" == t for t in st.gotos)
            if escalates and st.step_count < median:
                out.append(Finding(
                    "fast_escalation", "risk", name,
                    f"objection escalates to connect_rm() after only {st.step_count} "
                    f"step(s); median across objection states is {median}",
                    line=st.line_start + 1))

    # 7. guardrail prose that names an ordinal attempt count, surfaced next to the
    #    real step count so a mismatch is visible. NOT asserted as wrong — the
    #    guardrail may legitimately describe something else.
    for g in d.guardrails:
        for word, num in ORDINALS.items():
            m = re.search(rf"\ba {word}\b ([a-z/]+(?: [a-z/]+)?) failure", g)
            if not m:
                continue
            topic = m.group(1)
            for name, st in objections.items():
                if any(k in name for k in topic.replace("/", " ").split()):
                    if st.step_count + 1 != num:
                        out.append(Finding(
                            "guardrail_count_mismatch", "review", name,
                            f'guardrail says escalation on the {word} {topic} failure '
                            f'(={num}), but {name}() escalates on attempt '
                            f"{st.step_count + 1}",
                            evidence=[g[:160]]))
    return out


# --------------------------------------------------------------- data-driven --
def _client_calls(client_key: str) -> list:
    """Every cached extraction belonging to this client, current or historical.
    Historical calls matter here: drop-off signal lives in calls that were never
    part of the labelled working set."""
    from src import clients as clientsmod
    known = {c.key: c for c in clientsmod.get_known_clients()}
    client = known.get(client_key)
    calls = []
    for f in sorted(config.CACHE_DIR.glob("*.json")):
        try:
            c = json.loads(f.read_text())
        except Exception:  # noqa: BLE001
            continue
        cid = c.get("call_id", "")
        if client and client.filename_prefix:
            if cid.startswith(client.filename_prefix):
                calls.append(c)
        elif client_key == "abcl":
            if not cid.startswith("LCS") and not cid.startswith("GEN"):
                calls.append(c)
        elif cid.startswith(f"GEN-{client_key}"):
            calls.append(c)
    return calls


def _intent_hit_counts(d: dsl_parse.DSL, calls: list, client_key: str = "") -> dict:
    """How often each DSL intent actually occurs in this client's calls.

    Counted from the trained per-turn classifier's labels already cached on every
    turn — NOT re-derived from the DSL's anchor phrases.

    Anchor-similarity counting was tried and rejected on evidence. Substring
    matching cannot work at all (anchors are romanized Hinglish, transcripts are
    largely Devanagari). Embedding similarity was then calibrated against known
    per-turn counts and no usable threshold exists: at 0.62 `query_fee` scored 22
    against a true 83 while `address_error` scored 532 against a true 40, and the
    two error in opposite directions at every threshold tested. A number that
    wrong is worse than no number, so frequency now comes from the classifier and
    intents it cannot be matched to are reported as unknown rather than guessed.

    DSL intent -> observed intent is matched on name tokens, which is reliable in
    one direction only: a hit is trustworthy, a miss just means "not established".

    Returns {dsl_intent_name: n_turns_or_None}. None = frequency not established.
    """
    from collections import Counter
    observed = Counter()
    for c in calls:
        for t in c["turns"]:
            if t.get("speaker") == "customer":
                observed[t.get("intent", "")] += 1
                observed["#base#" + str(t.get("base_intent", ""))] += 1

    aliases = INTENT_ALIASES.get(client_key, {})
    out = {}
    for name in d.intents:
        tok = name.lower()
        explicit = aliases.get(name)
        total = 0
        matched = False
        for obs, n in observed.items():
            if obs.startswith("#base#") or not obs:
                continue   # count action-intents only, so turns aren't double counted
            if explicit is not None:
                if obs in explicit:
                    total += n
                    matched = True
            elif tok in obs or obs.replace("customer_", "") == tok:
                total += n
                matched = True
        out[name] = total if matched else None
    return out


def audit_against_data(d: dsl_parse.DSL, calls: list, min_dropoff: int = 3,
                       hits: dict | None = None) -> list:
    out = []
    if not calls:
        return out

    hits = hits if hits is not None else {}

    # 8. intent the classifier never once produced for this client
    for name, it in d.intents.items():
        if hits.get(name) == 0:
            out.append(Finding(
                "intent_never_observed", "review", name,
                f"the trained classifier produced this intent 0 times across "
                f"{len(calls)} calls; it may be dead weight for this client",
                evidence=it.anchors[:4], line=it.line_start + 1))

    # 9. ESCALATION BURN: an intent that fires often in the real data AND whose
    #    handler hands off to a human after very few attempts. This is the check
    #    that matters most operationally — every one of those matches is a
    #    potential human transfer. A pure step-count heuristic does NOT catch it
    #    (several handlers legitimately escalate on the first step, e.g. an
    #    explicit request for a human), so volume is what separates a cheap
    #    escalation from an expensive one.
    total_cust_turns = sum(1 for c in calls for t in c["turns"]
                           if t.get("speaker") == "customer")
    for intent, target in d.global_routes.items():
        st = d.states.get(target)
        if not st or "connect_rm" not in st.gotos:
            continue
        n_turns = hits.get(intent)
        attempts = st.step_count + 1
        if n_turns is None:
            # frequency not established — surfaced, not asserted
            if attempts <= 2:
                out.append(Finding(
                    "escalation_unmeasured", "review", target,
                    f'{target}() escalates to a human after only {attempts} '
                    f'attempt(s), but intent("{intent}") could not be matched to any '
                    f"observed intent, so its real frequency is unknown",
                    line=st.line_start + 1))
            continue
        share = n_turns / total_cust_turns if total_cust_turns else 0
        if n_turns >= 20 and attempts <= 2:
            out.append(Finding(
                "escalation_burn", "risk", target,
                f'intent("{intent}") occurs {n_turns} times '
                f"({share:.1%} of customer turns) but {target}() escalates to a "
                f"human after only {attempts} attempt(s) — a high-frequency intent on "
                f"a short fuse drives avoidable transfers",
                evidence=[f"{n_turns} occurrences across {len(calls)} calls",
                          f"{st.step_count} step(s) before connect_rm()"],
                line=st.line_start + 1))

    # 10. where incomplete calls actually die
    incomplete = [c for c in calls if c.get("outcome") == "incomplete"]
    if incomplete:
        from collections import Counter
        last_agent = Counter()
        last_cust = Counter()
        for c in incomplete:
            a = [t for t in c["turns"] if t["speaker"] == "agent"]
            u = [t for t in c["turns"] if t["speaker"] == "customer"]
            if a:
                last_agent[a[-1].get("intent", "?")] += 1
            if u:
                last_cust[u[-1].get("intent", "?")] += 1
        for intent, n in last_agent.most_common(6):
            if n >= min_dropoff:
                out.append(Finding(
                    "dropoff_after_agent", "gap", intent,
                    f"{n} of {len(incomplete)} incomplete calls ended right after the "
                    f"agent's '{intent}' turn",
                    evidence=[f"{n}/{len(incomplete)} incomplete calls"]))
        for intent, n in last_cust.most_common(6):
            if n >= min_dropoff:
                samples = []
                for c in incomplete:
                    u = [t for t in c["turns"] if t["speaker"] == "customer"]
                    if u and u[-1].get("intent") == intent:
                        samples.append(u[-1]["text"][:90])
                out.append(Finding(
                    "dropoff_after_customer", "gap", intent,
                    f"{n} of {len(incomplete)} incomplete calls ended on a customer "
                    f"'{intent}' turn",
                    evidence=samples[:5]))

    # 11. Universal-intent coverage gap. Different from #3 (unrouted_intent) — the
    # intent tested here IS routed somewhere, just not broadly enough. A customer
    # can decline to continue at almost ANY point in a multi-step form journey, so
    # 'disagree' (or any similarly universal intent) needs either a global route
    # or broad local coverage across the states that route on intent at all. If
    # neither holds, an off-script decline mid-journey has no defined behaviour —
    # which directly contradicts a NEVER IMPROVISE-style guardrail, if the prompt
    # has one (checked generically, not by exact string).
    routing_states = [n for n, st in d.states.items() if st.intent_routes]
    if routing_states:
        for candidate in ("disagree",):
            if candidate not in d.intents or candidate in d.global_routes:
                continue
            handled_in = [n for n, st in d.states.items()
                         if any(i == candidate for i, _ in st.intent_routes)]
            coverage = len(handled_in) / len(routing_states)
            if coverage < 0.25:
                dead_ends = [n for n in routing_states
                            if not any(i == "default" for i, _ in d.states[n].intent_routes)
                            and not d.states[n].gotos]
                samples = []
                for c in calls:
                    for t in c["turns"]:
                        if t.get("speaker") == "customer" and t.get("base_intent") == candidate:
                            samples.append(t["text"][:90])
                        if len(samples) >= 4:
                            break
                    if len(samples) >= 4:
                        break
                out.append(Finding(
                    "no_fallback_dead_end", "gap", candidate,
                    f'intent("{candidate}") can plausibly occur at almost any point '
                    f"in the flow, but is not globally routed and is only explicitly "
                    f"handled in {len(handled_in)}/{len(routing_states)} states that "
                    f"route on intent at all ({len(dead_ends)} states have no "
                    f"default/fallthrough of any kind) — a decline mid-journey has "
                    f"no defined behaviour",
                    evidence=[f"handled only in: {', '.join(sorted(handled_in))}"] + samples))
    return out


def audit(dsl_path, client_key: str, with_data: bool = True) -> tuple:
    d = dsl_parse.parse(dsl_path)
    findings = audit_structure(d)
    calls = []
    if with_data:
        calls = _client_calls(client_key)
        hits = _intent_hit_counts(d, calls, client_key) if calls else {}
        findings += audit_against_data(d, calls, hits=hits)
    return d, calls, findings


SEV_ORDER = {"bug": 0, "risk": 1, "gap": 2, "review": 3}


def render(findings: list) -> str:
    lines = []
    for sev in ("bug", "risk", "gap", "review"):
        group = [f for f in findings if f.severity == sev]
        if not group:
            continue
        lines.append(f"\n=== {sev.upper()} ({len(group)}) ===")
        for f in group:
            loc = f" (line {f.line})" if f.line else ""
            lines.append(f"  [{f.kind}] {f.where}{loc}")
            lines.append(f"      {f.detail}")
            for ev in f.evidence:
                lines.append(f"        · {ev}")
    return "\n".join(lines) if lines else "No findings."


if __name__ == "__main__":
    import sys
    dsl_path = sys.argv[1]
    client_key = sys.argv[2] if len(sys.argv) > 2 else "abcl"
    d, calls, findings = audit(dsl_path, client_key)
    print(f"DSL: {dsl_path}")
    print(f"  {len(d.intents)} intents · {len(d.states)} states · "
          f"{len(d.all_says())} say() lines")
    print(f"Client '{client_key}': {len(calls)} cached calls")
    print(render(findings))
    print(f"\n{len(findings)} finding(s).")
