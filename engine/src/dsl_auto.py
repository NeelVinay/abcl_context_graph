"""Autonomous LLM decisions for all three improvement features.

The mechanical miners (dsl_mine) find CANDIDATES cheaply and safely. This module
is where the judgment happens — the decisions that previously went to a human
review queue. Three call sites, batched:

  decide_anchors()    feature 1 — keep/drop/reassign each mined intent word
  decide_openers()    feature 2 — which natural particle fits which say() line,
                       and where (including "none")
  propose_improvements()  feature 3 — open analytical brief over the evidence
                       pack; returns any number of new say() lines with triggers

Everything returned here is UNTRUSTED until src/dsl_guard.py has checked it. That
split is deliberate: the model decides, the code enforces. A generated line that
asserts a rate or breaks the client's language{} rules is discarded mechanically
no matter how good its rationale reads.
"""
from __future__ import annotations

import json

from src import dsl_guard, llm

# The DSL's own grammar. Without this the model can propose good copy but has no
# way to reason about WHERE it goes — which caused a real bug: it returned
# placement "append", the code appended after the state's routing, and all three
# generated lines became unreachable dead code that dsl_verify happily passed
# (it checks structure, not reachability).
_DSL_PRIMER = """\
THE PROMPT LANGUAGE (.raven) — you must understand this to place speech correctly:

  agent priya {
    language { | prose style rules }
    custom_guardrails { | prose hard rules }
    intents {
      intent_name {
        | prose description of when this intent fires
        | Anchors: "phrase one", "phrase two"     <- recognition phrases
      }
    }
    flow {
      global { on intent("x") -> handle_x(); }    <- routes valid in ANY state
      state_name() {
        | prose instruction to the model
        say("spoken line");                       <- what the agent says aloud
        if (session_var) { say("..."); } else { say("..."); }
        step { say("..."); on intent("x") -> y(); }   <- one retry attempt
        on intent("affirm") -> next_state();      <- conditional transition
        on intent("default") { say("..."); }      <- inline block, no jump
        -> other_state();                         <- unconditional transition
      }
    }
  }
  session { var_name: "{{injected_at_call_time}}" }

CRITICAL EXECUTION SEMANTICS:
- Statements run TOP TO BOTTOM within a state.
- `on intent(...) -> x();` and a bare `-> x();` are TERMINAL: once one runs,
  control leaves the state. ANY say() placed after the transitions is DEAD CODE
  and will never be spoken. New speech must go BEFORE the first transition.
- `on intent("default")` is the catch-all; if a state has transitions but no
  default and no fallthrough, an unmatched reply has undefined behaviour.
- `<<var>>` interpolates a session variable into spoken text. Only variables
  declared in session{} exist.
- `say()` text is spoken verbatim by TTS. `|` prose lines are instructions to
  the model, never spoken.
- A state is reachable only if something routes or jumps to it.
"""

# Shared preamble — the client's own rules, so generated copy matches the file.
_STYLE_RULES = """\
STYLE RULES (from the prompt's own language{} block — non-negotiable):
- Hinglish: Hindi in DEVANAGARI, but keep these ROMAN: loan, EMI, salary,
  interest rate, KYC, OTP, SMS, link, callback, approval, rejection, CIBIL,
  documents, offer, percent, rate of interest, Terms and Conditions, Proceed,
  Verify, Apply Now.
- FEMALE verb forms for the agent, always (मैं समझ सकती हूँ / भेज देती हूँ /
  कर रही हूँ). Never male forms.
- Address the caller as "आप" ONLY. Never sir/madam/ma'am. Use neutral
  imperatives (करें, चाहें, बताएं) — never करेंगे/बताएंगे/सकते हैं.
- Natural Hinglish, not literary Hindi: salary not वेतन, loan not ऋण,
  documents not दस्तावेज़, approval not स्वीकृति, payment not भुगतान.

COMPLIANCE (hard limit — this is a regulated lending product):
- NEVER state or imply a number: no rate, no amount, no fee, no tenure, no
  timeline. No digits, no spelled-out quantities, no percentages, no currency.
- NEVER promise an outcome: no "approval", "guaranteed", "instant", "ज़रूर मिलेगा".
- You may motivate, reassure, empathise, and reframe. You may not assert terms.
"""


def _batched(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


# --------------------------------------------------------------- feature 1 --
def decide_anchors(gaps: list, dsl, client_key: str, batch_size: int = 25) -> dict:
    """{decision_key: {"verdict": keep|drop|reassign, "target": intent|None,
    "reason": str}}

    Deliberately does NOT ask for extra invented phrasings. An earlier version did,
    collected them into a "_suggestions" key, and nothing ever read it — paying
    output tokens every run for a feature that didn't exist. If evidence-free
    phrasings are wanted later, they need their own surfaced, reviewable path."""
    results = {}
    for batch in _batched(gaps, batch_size):
        items = []
        for g in batch:
            it = dsl.intents.get(g.intent)
            items.append({
                "key": g.decision_key,
                "intent": g.intent,
                "intent_description": (it.prose[0] if it and it.prose else ""),
                "current_anchors": (it.anchors[:12] if it else []),
                "candidate_word": g.word,
                "appears_in_calls": g.call_count,
                "lift_vs_corpus": round(g.lift, 2),
                "real_examples": g.examples[:3],
            })
        prompt = f"""You are improving a Hindi/Hinglish voice-agent prompt for a loan \
application bot. Its intents each carry "anchor" phrases used to recognise what a \
customer said and route the call.

A mechanical miner found candidate words from REAL call transcripts. Judge each one.

For each candidate decide:
- "keep": this word genuinely signals this intent. Adding it improves recognition.
- "drop": it's a co-occurrence artifact, too generic, ambiguous across intents, or
  ASR garbage. Adding it would cause misrouting.
- "reassign": the word is real but belongs to a DIFFERENT existing intent (name it).

Be strict. A wrong anchor causes real misrouting on live calls — e.g. adding a
generic negation to an error-handling intent makes the bot give error instructions
to someone who merely said "no".

CANDIDATES:
{json.dumps(items, ensure_ascii=False, indent=1)}

EXISTING INTENTS you may reassign to: {', '.join(sorted(dsl.intents.keys()))}

Respond with ONLY this JSON:
{{"decisions": [{{"key": "...", "verdict": "keep|drop|reassign",
  "target": "intent_name or null", "reason": "<=10 words"}}]}}"""

        try:
            out = llm.ask_json(prompt, client_key, purpose="decide_anchors")
        except llm.LLMBadResponse:
            continue   # drop this batch rather than guess — see module docstring
        for dcn in llm.as_list(out, "decisions"):
            if dcn.get("key"):
                results[dcn["key"]] = dcn
    return results


# --------------------------------------------------------------- feature 2 --
def decide_openers(openers: list, dsl, client_key: str, batch_size: int = 20) -> dict:
    """{decision_key: {"verdict": use|skip, "particle": str|None, "reason": str}}

    This is the judgment the mechanical miner provably lacks: it happily proposes
    "हां, मुझे खेद है" (a condolence line) because it only knows the particle is
    frequent, not whether it fits."""
    results = {}
    by_line = {}
    for o in openers:
        by_line.setdefault(o.line_idx, []).append(o)

    lines = list(by_line.items())
    for batch in _batched(lines, batch_size):
        items = []
        for line_idx, cands in batch:
            from src import dsl_parse
            items.append({
                "line_id": line_idx,
                "state": dsl_parse.containing_state(dsl, line_idx),
                "current_line": cands[0].old_line,
                "options": [{"key": c.decision_key, "particle": c.particle,
                             "mechanism": c.mechanism,
                             "customers_use_it_in_calls": c.call_count,
                             "result": c.new_line}
                            for c in cands],
            })
        prompt = f"""You are making a Hindi/Hinglish voice-agent sound less scripted.

Real customers open turns with short acknowledgment particles (जी, हां, ठीक).
The agent mostly doesn't. A mechanical miner proposed adding/doubling a particle
on the lines below — but it only knows the particle is FREQUENT, not whether it
FITS. Your job is the fit judgment.

For each line, choose AT MOST ONE option, or "skip".

Choose "skip" when a lead-in would sound wrong — for example on a condolence
line ("मुझे खेद है"), an apology, or anywhere an acknowledgment particle would
read as flippant or as agreeing to something that wasn't said. Skipping is the
right answer often; do not feel obliged to pick one.

Consider what the customer JUST said (inferable from the state name) — the
particle should read as a natural response to that.

{_STYLE_RULES}

LINES:
{json.dumps(items, ensure_ascii=False, indent=1)}

Respond with ONLY this JSON:
{{"decisions": [{{"line_id": <int>, "chosen_key": "<key or null>",
  "reason": "<=10 words"}}]}}"""

        try:
            out = llm.ask_json(prompt, client_key, purpose="decide_openers")
        except llm.LLMBadResponse:
            continue
        for dcn in llm.as_list(out, "decisions"):
            key = dcn.get("chosen_key")
            if key:
                results[key] = {"verdict": "use", "reason": dcn.get("reason", "")}
    return results


# --------------------------------------------------------------- feature 3 --
def _silent_states(dsl) -> list:
    """States whose own prose forbids adding speech (see dsl_fix.SILENT_STATE_RE,
    reused here so this list can never drift out of sync with what the guard
    actually rejects). Computed over ALL states, not just the ones shown in
    relevant_states — the model may recognize a name from the DSL primer or an
    earlier proposal and target it even when its body isn't in view."""
    from src import dsl_fix
    return sorted(name for name, st in dsl.states.items()
                 if dsl_fix.SILENT_STATE_RE.search(st.body))


def propose_improvements(pack_text: str, dsl, client_key: str,
                         relevant_states: str) -> list:
    """Open analytical brief. Returns a list of proposals, each with one or more
    say() lines, a trigger, and a target state."""
    silent = _silent_states(dsl)
    silent_note = (
        f"OFF LIMITS — these states declare in their own prose that they may not "
        f"speak (a scripted single line, or none at all): {', '.join(silent)}. "
        f"Proposing a target_state from this list is a wasted proposal — it will "
        f"be rejected outright, not trimmed or moved. If the conversation moment "
        f"you want to address happens right before or after one of these (e.g. "
        f"sms_send is followed immediately by web_journey_start once the SMS is "
        f"actually sent), pick the nearest state that is NOT on this list instead."
        if silent else "")
    prompt = f"""You are improving the prompt for a Hindi/Hinglish outbound voice \
agent ("Priya") that helps customers apply for a pre-approved personal loan from \
Aditya Birla Capital. Below is real evidence from {pack_text.splitlines()[0]}.

Your job: read what customers ACTUALLY SAY on these calls, and write agent speech
that answers them convincingly.

The "WHAT CUSTOMERS ACTUALLY SAY" section below is your primary material. Those
are real, verbatim customer turns, counted across distinct calls. Take the things
customers genuinely ask and object to, and write responses that address them
directly, in their own terms — echoing the customer's actual framing lands far
better than generic reassurance.

PREFER content grounded in real customer speech over generic conversion copy.
A line that answers "मेरा CIBIL score कम है, मुझे मिलेगा क्या?" is worth more
than a line that says "there's no commitment" — the first responds to a real
person, the second could have been written without reading a single transcript.

Two different questions, do not confuse them:
  * "Do customers say this?" — descriptive, needs only a count. This is what
    licenses you to write an answer for it. Counts are given.
  * "Does saying this predict a lost call?" — causal, needs p<0.05. This only
    limits what you may CLAIM about cause in your rationale.
A theme with p>0.05 is still absolutely worth answering well if customers keep
raising it. Do NOT let a missing p-value stop you from addressing real speech.

=== EVIDENCE ===
{pack_text}

{_DSL_PRIMER}

=== RELEVANT CURRENT PROMPT STATES ===
{relevant_states}

{silent_note}

{_STYLE_RULES}

For each improvement propose:
- "answers_customer_quotes": REQUIRED for any line responding to customer speech.
  A list of the actual verbatim customer quotes (copied exactly from the section
  above) that this line is written to answer. This is how grounding is verified —
  a proposal whose lines address real customer speech but cites no quotes will be
  treated as ungrounded. Use an empty list ONLY for a purely structural change.
- "rationale": what in the evidence supports this (cite the numbers/quotes)
- "target_state": the state whose speech you are improving (must already exist)
- "trigger": one of
    * "existing" — speech that runs unconditionally in that state
    * "on_intent:<intent_name>" — only fires on an existing intent (list given)
    * "if:<session_var>" — only fires when an EXISTING session variable is set
  Do NOT invent a session variable, and do NOT propose anything time/date/season
  based — the data has no timestamps.
- "lines": one or more say() line strings — as many as the improvement genuinely
  needs. Each must obey the style and compliance rules above.
- "placement": where in the state the new speech belongs. Remember transitions
  are terminal, so this is a correctness question, not a preference:
    * "before_transitions" — after the state's existing say() lines but BEFORE
      its first `on intent(...)` / `->`. This is almost always what you want for
      speech that should actually be heard.
    * "state_start" — the very first thing the state says.
  Never ask for speech after a transition; it would be unreachable.

DO NOT RESTATE WHAT THE STATE ALREADY SAYS. Read the target state's existing
say() lines first. If it already introduces the agent, do not introduce her
again; if it already explains the offer, add the missing angle, not a reworded
version. A line that repeats its neighbour makes the agent sound broken, and it
will be rejected automatically. Add only what is genuinely absent.

Aim to cover the recurring things customers actually say — work down EVERY theme
listed in "WHAT CUSTOMERS ACTUALLY SAY" by call count, including the smallest ones,
and give each one a genuinely good answer, placed in the state where that
conversation happens. Several well-grounded changes are expected here, not one or
two — a proposal per theme is the default; skip one only if the prompt already
answers it well, and say so in your analysis. Spread proposals across whichever
states actually match each theme's moment in the call rather than stacking several
onto one convenient state — a state that already has 3-4 new lines added this run
is a sign to look for a better-fitting target for the next one, not to add a 5th.

Respond with ONLY this JSON:
{{"analysis": "<what customers are actually saying and where the prompt answers "
 "them poorly, 3-5 sentences>",
 "proposals": [{{"answers_customer_quotes": ["verbatim quote", "..."],
   "rationale": "...", "target_state": "...", "trigger": "...",
   "lines": ["..."], "placement": "before_transitions"}}]}}"""

    try:
        out = llm.ask_json(prompt, client_key, purpose="propose_improvements",
                           max_tokens=6000)
    except llm.LLMBadResponse:
        return []
    return out


def validate_buckets(buckets: dict, dsl, client_key: str,
                     samples_per_bucket: int = 6) -> dict:
    """Keep only the anchor-similarity buckets that genuinely represent their intent.

    This is the precision half of the alias fix. bucket_turns_by_anchors() gives
    good recall (13 previously-unminable intents on the ABCL corpus) but poor
    precision (~3 of 13 correct), and the errors are systematic rather than random:

      * POLARITY — "जी OTP मिल गया है" ("I GOT the OTP") lands in
        otp_not_received, because the negated and affirmative forms share almost
        every token. Cosine similarity structurally cannot see the flip.
      * TOPIC vs INTENT — "Two lakh का दिखा रहा है" (reporting an amount) lands
        in wants_more_amount; same subject, different act.

    Both are trivial for a model to spot and impossible for the embedding to, so
    one call gates all buckets at once. A rejected bucket is dropped entirely —
    mining words from a wrong bucket poisons that intent silently, which is worse
    than mining nothing for it."""
    if not buckets:
        return {}
    items = []
    for intent, by_call in buckets.items():
        it = dsl.intents.get(intent)
        texts = [t for t in by_call.values()][:samples_per_bucket]
        items.append({
            "intent": intent,
            "intent_means": (it.prose[0] if it and it.prose else ""),
            "intent_anchors": (it.anchors[:8] if it else []),
            "calls_in_bucket": len(by_call),
            "sample_turns": [t[:160] for t in texts],
        })

    prompt = f"""A mechanical step grouped real customer turns from call transcripts \
into buckets, one per intent, by embedding-similarity against each intent's own \
anchor phrases. Similarity matching is unreliable in two specific ways and your job \
is to catch them.

For each bucket, decide whether the sample turns REALLY are instances of that intent.

Reject a bucket when:
1. POLARITY IS INVERTED — the turns say the opposite of the intent. This is the
   most common failure. Example: an intent meaning "OTP did not arrive" whose
   samples say "OTP मिल गया है" ("I got the OTP"). Same words, opposite meaning.
   Check every bucket for this specifically.
2. SAME TOPIC, WRONG ACT — the turns are about the right subject but are not that
   intent. Example: an intent meaning "wants a higher amount" whose samples merely
   report the amount on screen ("Two lakh का दिखा रहा है").
3. The turns are ASR garble, or a mixed bag with no consistent meaning.

Accept only if most sample turns are genuinely that intent. Be strict — a wrong
bucket silently corrupts every word later mined from it, so rejecting a real
bucket is far cheaper than accepting a wrong one.

BUCKETS:
{json.dumps(items, ensure_ascii=False, indent=1)}

Respond with ONLY this JSON:
{{"verdicts": [{{"intent": "...", "verdict": "accept|reject",
  "reason": "<=12 words"}}]}}"""

    try:
        out = llm.ask_json(prompt, client_key, purpose="validate_buckets",
                           max_tokens=2000)
    except llm.LLMBadResponse:
        return {}          # drop them all rather than mine from unvalidated buckets
    verdicts = llm.as_list(out, "verdicts")
    keep = {v.get("intent") for v in verdicts
            if v.get("verdict") == "accept"}
    rejected = [(v.get("intent"), v.get("reason", ""))
                for v in verdicts if v.get("verdict") != "accept"]
    return {"accepted": {k: v for k, v in buckets.items() if k in keep},
            "rejected": rejected}


def verify_grounding(proposal: dict, calls: list) -> list:
    """Confirm the quotes a proposal claims to answer are REAL customer speech
    from this corpus, not paraphrases the model invented. Returns problems.

    Checked in code rather than trusted, for the same reason the compliance guard
    is: a citation that looks plausible and isn't traceable is worse than none,
    because it makes an ungrounded line appear evidence-backed."""
    quotes = proposal.get("answers_customer_quotes") or []
    if not quotes:
        return []          # structural change, nothing to verify
    haystack = "\n".join(
        t.get("text", "") for c in calls for t in c["turns"]
        if t.get("speaker") == "customer")
    problems = []
    for q in quotes:
        probe = (q or "").strip()
        if len(probe) < 8:
            # Too short to verify meaningfully AND too short to justify a line —
            # previously these were skipped silently, so a fragment counted as
            # grounding. Now they don't count as a citation at all.
            problems.append(f"cited quote too short to verify: {probe!r}")
            continue
        # Match the WHOLE quote. A 60-char prefix probe meant a model could copy
        # 60 real characters and fabricate the rest, and since the evidence pack
        # shows quotes up to 180 chars, over-60 was the common case. The pack
        # truncates what it shows, so allow the cited quote to be a prefix of a
        # real turn — but every character cited must be real.
        if probe not in haystack:
            problems.append(f"cited quote not found verbatim in customer speech: {probe[:70]!r}")
    return problems


# ------------------------------------------------------------ guard wrapper --
def screen_lines(lines, known_placeholders: set) -> tuple:
    """Run every generated line through the mechanical guard.
    Returns (accepted_lines, rejections) where rejections are (line, problems).

    Coerces a bare string to a single-element list first: iterating a string
    yields characters, and one-character "lines" pass every content check
    trivially (see make_usecase_edit for the reproduced 19-say() case)."""
    if isinstance(lines, str):
        lines = [lines]
    if not isinstance(lines, (list, tuple)):
        return [], [(repr(lines)[:60], ["'lines' was not a list of strings"])]
    ok, bad = [], []
    for ln in lines:
        if not isinstance(ln, str):
            bad.append((repr(ln)[:60], ["not a string"]))
            continue
        problems = dsl_guard.check_line(ln, known_placeholders)
        if problems:
            bad.append((ln, problems))
        else:
            ok.append(ln)
    return ok, bad
