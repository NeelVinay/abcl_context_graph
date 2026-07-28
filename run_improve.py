"""CLI entry point for the automated DSL prompt improvement loop. No LLM at any
stage — see src/dsl_audit.py, src/dsl_mine.py, src/dsl_fix.py, src/dsl_verify.py
for the pieces this wires together, and /Users/neelvinay/.claude/plans/
i-want-you-to-toasty-spindle.md for the design rationale and the evidence behind
every scope decision below.

  python run_improve.py <prompt.raven> --client abcl
      Audit + review queue only. Any fully-mechanical fix (a guardrail ordinal
      that doesn't match the real step count, an intent whose handler exists but
      isn't routed) is auto-applied — these need no human judgment at all. A
      ranked queue of real customer phrases the prompt handles poorly is printed
      for review; nothing from the queue is applied without --accept.

  python run_improve.py <prompt.raven> --client abcl --accept 1,3
      Additionally accept queue items 1 and 3. An accepted anchor-gap item
      becomes a real edit (appends the word to that intent's Anchors line). An
      accepted uncovered-cluster item is recorded (so it stops being re-proposed)
      but produces NO edit — naming a new intent and writing its answer needs a
      person; see the plan for why this boundary is not negotiable.

  --apply       write the result in place (default: write <name>.improved.raven,
                a dry run, plus CHANGES.md either way)
  --budget N    token ceiling; verify() will refuse to write over budget
  --reject 2,5  mark queue items as rejected (never re-proposed), no edit made

Every run's edits are gated on src.dsl_verify.verify() passing with ZERO blocking
failures — including on a prompt that already has a pre-existing defect (e.g. a
route to an undefined state): the gate will correctly refuse to write ANYTHING,
even a perfectly good new anchor, until that defect is fixed too. This is by
design, not a bug — see the turnfix.raven test in the plan's evidence log.
"""
from __future__ import annotations

import argparse
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")   # numpy/sklearn cosine-sim overflow noise, harmless

from src import dsl_audit, dsl_fix, dsl_mine


def _parse_ids(raw: str | None) -> list:
    if not raw:
        return []
    return [int(x.strip()) for x in raw.split(",") if x.strip()]


def run(dsl_path: str, client_key: str, budget: int | None, apply_to_disk: bool,
       accept_raw: str | None, reject_raw: str | None) -> None:
    dsl_path = Path(dsl_path)
    d, calls, findings = dsl_audit.audit(dsl_path, client_key)

    print(f"Client: {client_key}")
    print(f"Prompt: {dsl_path}  ({len(d.intents)} intents, {len(d.states)} states)")
    by_sev = {}
    for f in findings:
        by_sev[f.severity] = by_sev.get(f.severity, 0) + 1
    sev_str = "  ".join(f"{n} {s}" for s, n in by_sev.items()) or "none"
    print(f"Audit: {len(findings)} finding(s) — {sev_str}")
    print()

    # ---- fully-mechanical auto fixes: no human judgment needed at all ----
    auto_edits = []
    for f in findings:
        if f.kind == "guardrail_count_mismatch":
            e = dsl_fix.make_rewrite_ordinal_edit(d, f)
            if e:
                auto_edits.append(e)
        elif f.kind == "unrouted_intent" and f"handle_{f.where}" in d.states:
            e = dsl_fix.make_add_global_route_edit(d, f.where)
            if e:
                auto_edits.append(e)

    if auto_edits:
        print(f"AUTO-APPLIED ({len(auto_edits)}) — no judgment needed, purely mechanical")
        for e in auto_edits:
            print(f"  ~ {e.kind}: {e.rationale}")
        print()
    else:
        print("AUTO-APPLIED (0) — nothing mechanically broken found")
        print()

    # ---- process --reject first, so rejected items never get accepted below ----
    reject_ids = _parse_ids(reject_raw)
    if reject_ids:
        queue_now = dsl_mine.build_queue(d, calls, client_key)
        for idx in reject_ids:
            if 1 <= idx <= len(queue_now):
                dsl_mine.save_decision(client_key, queue_now[idx - 1].decision_key, accepted=False)

    # ---- process --accept ----
    accept_ids = _parse_ids(accept_raw)
    accepted_edits = []
    if accept_ids:
        queue_now = dsl_mine.build_queue(d, calls, client_key)
        accepted_gaps = []   # collected, then batched per-intent below — see
                             # dsl_fix.make_add_anchors_edits_batch: applying more
                             # than one accepted anchor for the SAME intent as
                             # separate edits silently drops all but the last one
        for idx in accept_ids:
            if not (1 <= idx <= len(queue_now)):
                print(f"  ! [{idx}] out of range (queue currently has {len(queue_now)} items), skipped")
                continue
            item = queue_now[idx - 1]
            dsl_mine.save_decision(client_key, item.decision_key, accepted=True)
            if isinstance(item, dsl_mine.AnchorGap):
                accepted_gaps.append(item)
            elif isinstance(item, dsl_mine.NaturalOpener):
                # one edit per candidate, deliberately not batched — two
                # candidates can legitimately target the same line (e.g. जी vs
                # हां as the opener); accepting both in one run must conflict via
                # apply_edits' ConflictingEditsError, not silently combine
                accepted_edits.append(dsl_fix.make_opener_edit(d, item))
            else:
                print(f"  ! [{idx}] uncovered cluster accepted for tracking (won't be "
                      f"re-proposed), but produces no edit — write a name + say() answer "
                      f"by hand, then add it to the prompt directly")
        accepted_edits = dsl_fix.make_add_anchors_edits_batch(d, accepted_gaps) + accepted_edits
        if accepted_edits:
            print(f"\nACCEPTED THIS RUN ({len(accepted_edits)})")
            for e in accepted_edits:
                print(f"  + {e.kind}: {e.rationale}")
        print()

    # ---- remaining review queue (decisions just saved above are now excluded) ----
    remaining = dsl_mine.build_queue(d, calls, client_key)
    print(f"PROPOSED — review ({len(remaining)})")
    print(dsl_mine.render_queue(remaining))

    # Written EVERY run, unconditionally — this is the thing meant to live in the
    # repo and be opened in an editor, not just scroll past in a terminal. Always
    # reflects the current file + data state, same folder as the prompt and
    # anchor_decisions.json.
    queue_md_path = dsl_path.parent / "review_queue.md"
    queue_md_path.write_text(dsl_mine.render_queue_markdown(remaining, client_key, dsl_path.name))
    print(f"\nWrote {queue_md_path}")

    all_edits = auto_edits + accepted_edits
    if not all_edits:
        print("Nothing to write this run.")
        return

    new_text, result = dsl_fix.apply_and_verify(dsl_path, all_edits, token_budget=budget)
    print(result.render())
    if not result.ok:
        print("\nVerification FAILED — nothing written. Fix the blocking issue(s) above "
              "(they may be pre-existing defects unrelated to this run's edits) and re-run.")
        return

    if apply_to_disk:
        dsl_path.write_text(new_text)
        out_path = dsl_path
        print(f"\nApplied in place: {out_path}")
    else:
        out_path = dsl_path.with_name(dsl_path.stem + ".improved" + dsl_path.suffix)
        out_path.write_text(new_text)
        print(f"\nWrote {out_path} (dry run — pass --apply to write in place)")

    _write_changes_md(dsl_path, all_edits, out_path)


def _edit_headline(e) -> str:
    """A human-readable one-liner for a change, so the reader knows what they're
    looking at before reading any rationale."""
    import re as _re
    if e.kind == "ADD_ANCHORS":
        m = _re.match(r"(\w+):", e.rationale or "")
        intent = m.group(1) if m else "intent"
        words = _re.findall(r'"([^"]+)"', e.rationale or "")
        return f"`{intent}` now also recognises: " + ", ".join(f"**{w}**" for w in words)
    if e.kind == "NATURAL_OPENER":
        m = _re.match(r'"([^"]+)"\s+(\w+)', e.rationale or "")
        p = m.group(1) if m else "particle"
        how = "doubled" if m and m.group(2) == "reduplicate" else "added as a lead-in"
        return f"**{p}** {how}"
    if e.kind == "USECASE":
        return f"New line in `{e.ref.split(':', 1)[-1]}()`"
    return e.kind


_KIND_INFO = {
    "ADD_ANCHORS": (
        "Recognition phrases",
        "The agent now understands more of what callers actually say, so these "
        "turns route to the right handler instead of falling through to the "
        "generic default."),
    "NATURAL_OPENER": (
        "Conversational delivery",
        "A short acknowledgement particle real callers use, added as a lead-in. "
        "The wording of the line itself is unchanged — this only affects how "
        "scripted the agent sounds."),
    "USECASE": (
        "New agent speech",
        "A new line answering something callers repeatedly say. The agent had no "
        "response for this before."),
}


def _write_changes_md(dsl_path: Path, edits: list, out_path: Path,
                      discarded: list | None = None) -> None:
    from collections import defaultdict
    by_kind = defaultdict(list)
    for e in edits:
        by_kind[e.kind].append(e)

    lines = [f"# What changed in {dsl_path.name}", ""]
    lines.append("Every change below was derived from real call transcripts. "
                 "Quotes are verbatim.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Change type | Count | What it does |")
    lines.append("|---|---|---|")
    for kind, group in sorted(by_kind.items()):
        title, why = _KIND_INFO.get(kind, (kind, ""))
        lines.append(f"| {title} | {len(group)} | {why} |")
    if discarded:
        lines.append(f"| _Rejected by safety checks_ | {len(discarded)} | "
                     f"Proposed but blocked — see the end of this file |")
    lines.append("")

    for kind, group in sorted(by_kind.items()):
        title, why = _KIND_INFO.get(kind, (kind, ""))
        lines.append("---")
        lines.append("")
        lines.append(f"# {title}  ({len(group)})")
        lines.append("")
        lines.append(f"_{why}_")
        lines.append("")
        if kind == "NATURAL_OPENER":
            # One Edit per line is required by the applier (each targets a
            # different line number, and same-line edits must conflict rather
            # than merge). But 33 near-identical entries is unreadable, so
            # collapse the REPORT by particle — the edits themselves are
            # untouched.
            import re as _re
            from collections import defaultdict as _dd
            by_particle = _dd(list)
            for e in group:
                m = _re.match(r'"([^"]+)"\s+(\w+)', e.rationale or "")
                by_particle[(m.group(1) if m else "?",
                             m.group(2) if m else "insert")].append(e)
            for (particle, mech), es in sorted(by_particle.items(),
                                               key=lambda kv: -len(kv[1])):
                how = ("doubled (callers repeat it)" if mech == "reduplicate"
                       else "added as a lead-in")
                lines.append(f"### **{particle}** {how} — in {len(es)} place(s)")
                lines.append("")
                n_calls = _re.search(r"\((\d+) calls", es[0].rationale or "")
                if n_calls:
                    lines.append(f"Real callers open turns with \"{particle}\" in "
                                 f"{n_calls.group(1)} calls. Only the lead-in is "
                                 f"added; no existing wording changed.")
                    lines.append("")
                lines.append("<details><summary>the lines it was added to</summary>")
                lines.append("")
                for e in es:
                    lines.append(f"- `{e.new_text.strip()[:110]}`")
                lines.append("")
                lines.append("</details>")
                lines.append("")
            continue

        for i, e in enumerate(group, 1):
            lines.append(f"### {i}. {_edit_headline(e)}")
            lines.append("")
            if e.kind == "USECASE":
                lines.append("**The agent will now say:**")
                lines.append("")
                for ev in e.evidence:
                    lines.append(f"> {ev}")
                lines.append("")
                lines.append("**Why:** " + (e.rationale or "—"))
            elif e.kind == "NATURAL_OPENER":
                lines.append(f"**Why:** {e.rationale}")
                if e.evidence:
                    lines.append("")
                    lines.append("**Callers who talk this way:**")
                    for ev in e.evidence[:2]:
                        lines.append(f"> {ev}")
            else:
                lines.append(f"**Why:** {e.rationale}")
                if e.evidence:
                    lines.append("")
                    lines.append("**Heard on real calls:**")
                    for ev in e.evidence[:3]:
                        lines.append(f"> {ev}")
            lines.append("")
    if discarded:
        # Failures are shown, never silently swallowed: if the model is
        # systematically producing non-compliant copy, that must be visible.
        lines.append("---")
        lines.append("")
        lines.append(f"# Rejected by safety checks  ({len(discarded)})")
        lines.append("")
        lines.append("_These were proposed and then blocked automatically. Nothing "
                     "here reached the prompt._")
        lines.append("")
        for what, problems in discarded:
            lines.append(f"- **{what}** — {'; '.join(problems)}")
        lines.append("")
    changes_path = out_path.parent / "CHANGES.md"
    lines.append("")
    changes_path.write_text("\n".join(lines))
    print(f"Wrote {changes_path}")


def run_auto(dsl_path: str, client_key: str, budget: int | None) -> None:
    """Fully autonomous: transcripts + prompt in, improved prompt out. The LLM
    makes every judgment call; the code enforces correctness and compliance.

    No human gates. What remains is mechanical self-checking — a generated line
    that breaks the client's language{} rules or asserts a loan term is discarded
    by src/dsl_guard.py before it can be applied, and the whole run is gated on
    dsl_verify passing so a bad generation can never write a broken prompt."""
    from src import dsl_auto, dsl_evidence, dsl_guard, llm

    dsl_path = Path(dsl_path)
    d, calls, findings = dsl_audit.audit(dsl_path, client_key)
    known_placeholders = dsl_fix._session_vars(d)

    print(f"Client: {client_key}")
    print(f"Prompt: {dsl_path}  ({len(d.intents)} intents, {len(d.states)} states)")
    print(f"Corpus: {len(calls)} calls")
    # A wrong --client silently mines ANOTHER client's transcripts into this
    # prompt (verified: `input.raven --client justdial` loaded 115 JustDial calls
    # and produced 83 candidates). The path is only a hint, but a mismatch is
    # nearly always a typo, so say so loudly rather than emit plausible junk.
    parts = {p.lower() for p in dsl_path.resolve().parts}
    if not calls:
        print(f"\n  !! No calls loaded for client {client_key!r} — nothing to mine. "
              f"Check the --client key.")
        return
    if "clients" in parts and client_key.lower() not in parts:
        print(f"\n  !! WARNING: this prompt sits under a different client directory "
              f"than --client {client_key!r}. That client's transcripts will be mined "
              f"into it. Ctrl-C now if that is not intended.")
    print()

    all_edits = []
    discarded = []

    # ---- feature 1: intent recognition words ----
    # INTENT_ALIASES only bridges a handful of the DSL's intents to classifier
    # labels (the two taxonomies were built for different purposes). Bucketing by
    # each intent's own anchors covers the rest — but embedding similarity can't
    # see negation, so every bucket is gated by the LLM before anything is mined
    # from it. See dsl_mine.bucket_turns_by_anchors for the measured failure modes.
    print("[1/3] anchors: bucketing turns by intent anchors "
          "(covers intents no classifier label maps to)")
    raw_buckets = dsl_mine.bucket_turns_by_anchors(d, calls)
    validated = dsl_auto.validate_buckets(raw_buckets, d, client_key)
    extra = validated.get("accepted", {}) if validated else {}
    for intent, reason in (validated.get("rejected", []) if validated else []):
        discarded.append((f"anchor bucket for {intent!r}",
                          [reason or "bucket rejected by LLM as not this intent"]))
    print(f"      {len(raw_buckets)} bucket(s) found, {len(extra)} passed validation")

    gaps = dsl_mine.mine_anchor_gaps(d, calls, client_key, extra_buckets=extra)
    print(f"      {len(gaps)} mined candidates -> asking LLM to judge each word")
    decisions = dsl_auto.decide_anchors(gaps, d, client_key)
    keep, reassigned = [], 0
    for g in gaps:
        dcn = decisions.get(g.decision_key)
        if not dcn:
            continue
        if dcn.get("verdict") == "keep":
            keep.append(g)
        elif dcn.get("verdict") == "reassign" and dcn.get("target") in d.intents:
            g.intent = dcn["target"]
            keep.append(g)
            reassigned += 1
        else:
            discarded.append((f"anchor {g.word!r} -> {g.intent}",
                              [dcn.get("reason", "dropped by LLM")]))
    anchor_edits = dsl_fix.make_add_anchors_edits_batch(d, keep)
    all_edits += anchor_edits
    print(f"      kept {len(keep)} ({reassigned} reassigned), "
          f"dropped {len(gaps) - len(keep)} -> {len(anchor_edits)} edit(s)")

    # ---- feature 2: natural particles ----
    openers = dsl_mine.mine_natural_openers(d, calls)
    print(f"[2/3] particles: {len(openers)} mined candidates -> asking LLM for fit")
    odecisions = dsl_auto.decide_openers(openers, d, client_key)
    chosen = [o for o in openers if o.decision_key in odecisions]
    # one edit per line max — the LLM picks at most one option per line, but guard
    # against a malformed response proposing two for the same line
    seen_lines, opener_edits = set(), []
    for o in chosen:
        if o.line_idx in seen_lines:
            continue
        problems = dsl_guard.check_structure(o.old_line, o.new_line)
        if problems:
            discarded.append((f"particle {o.particle!r} on line {o.line_idx}", problems))
            continue
        seen_lines.add(o.line_idx)
        opener_edits.append(dsl_fix.make_opener_edit(d, o))
    all_edits += opener_edits
    print(f"      LLM chose {len(chosen)} of {len(openers)} -> {len(opener_edits)} edit(s)")

    # ---- feature 3: contextual persuasion ----
    print("[3/3] persuasion: building evidence pack -> open analytical brief")
    pack = dsl_evidence.build_pack(calls, d, client_key)
    pack_text = dsl_evidence.render_pack(pack)
    relevant = _relevant_states_text(d, pack)
    out = dsl_auto.propose_improvements(pack_text, d, client_key, relevant)
    proposals = llm.as_list(out, "proposals")
    if isinstance(out, dict) and out.get("analysis"):
        print(f"\n      LLM analysis: {out['analysis']}\n")
    usecase_edits = []
    accepted_lines_by_state: dict = {}
    for p in proposals:
        ungrounded = dsl_auto.verify_grounding(p, calls)
        if ungrounded:
            # surfaced, not silently dropped — a fabricated citation is exactly
            # the failure mode that would make this system untrustworthy
            discarded.append((f"proposal for {p.get('target_state')!r}", ungrounded))
            continue
        good, bad = dsl_auto.screen_lines(p.get("lines", []), known_placeholders)
        for ln, probs in bad:
            discarded.append((f"generated line {ln[:60]!r}", probs))
        if not good:
            continue

        # Redundancy: compare against speech ALREADY in the target state, plus
        # anything an earlier proposal this run already added there. Without the
        # second part, two proposals targeting one state can each be fine alone
        # and still make the agent say the same thing twice.
        st = d.states.get(p.get("target_state"))
        existing = list(st.says) if st else []
        existing += accepted_lines_by_state.get(p.get("target_state"), [])
        kept = []
        for ln in good:
            probs = dsl_guard.check_redundancy(ln, existing)
            if probs:
                discarded.append((f"generated line {ln[:60]!r}", probs))
                continue
            kept.append(ln)
            existing.append(ln)
        if not kept:
            continue
        accepted_lines_by_state.setdefault(p.get("target_state"), []).extend(kept)
        p["lines"] = kept
        try:
            e = dsl_fix.make_usecase_edit(d, p)
        except dsl_fix.SpeechForbiddenError as ex:
            discarded.append((f"proposal for {p.get('target_state')!r}", [str(ex)]))
            continue
        if e:
            usecase_edits.append(e)
        else:
            discarded.append((f"proposal for {p.get('target_state')!r}",
                              ["unknown state, undefined intent, or unknown session var"]))
    all_edits += usecase_edits
    print(f"      {len(proposals)} proposal(s) -> {len(usecase_edits)} edit(s) after guard")

    # ---- apply ----
    print()
    if not all_edits:
        print("No changes to apply.")
        _report_cost(client_key, llm)
        return

    backup = dsl_path.with_suffix(dsl_path.suffix + ".bak")
    backup.write_text(d.text)
    print(f"Backup: {backup}")

    new_text, result = dsl_fix.apply_and_verify(dsl_path, all_edits, token_budget=budget)
    print(result.render())
    if not result.ok:
        print("\nVerification FAILED — nothing written.")
        _report_cost(client_key, llm)
        return

    dsl_path.write_text(new_text)
    print(f"\nApplied {len(all_edits)} edit(s) in place: {dsl_path}")
    _write_changes_md(dsl_path, all_edits, dsl_path, discarded=discarded)
    _report_cost(client_key, llm)


def _relevant_states_text(d, pack, max_chars: int = 6000) -> str:
    """The states worth showing the model: the pitch/early-funnel ones where the
    evidence says calls actually die, plus the objection handlers."""
    wanted = ["start", "self_intro", "loan_intro", "loan_intro_persuade", "sms_send",
              "handle_fee_query", "handle_security_concern", "handle_agent_query",
              "handle_prior_attempt_failed", "handle_has_loan_unspecified"]
    out = []
    for name in wanted:
        st = d.states.get(name)
        if st:
            out.append(st.body)
    text = "\n\n".join(out)
    return text[:max_chars]


def _report_cost(client_key: str, llm) -> None:
    stats = llm.call_count(client_key)
    print(f"\nLLM usage: {stats['calls']} live call(s), {stats['cached']} cached, "
          f"{stats['in_tokens']} in / {stats['out_tokens']} out tokens")


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dsl_path", help="path to the .raven prompt")
    ap.add_argument("--client", required=True, help="client key, e.g. abcl")
    ap.add_argument("--budget", type=int, default=None, help="token ceiling")
    ap.add_argument("--apply", action="store_true", help="write in place (default: dry run)")
    ap.add_argument("--accept", default=None, help="comma-separated queue item numbers to accept")
    ap.add_argument("--reject", default=None, help="comma-separated queue item numbers to reject")
    ap.add_argument("--auto", action="store_true",
                    help="fully autonomous LLM run: decides and applies all three "
                         "features with no human review")
    args = ap.parse_args()
    if args.auto:
        from src import llm
        try:
            # --auto with no --budget skipped the token check entirely, so
            # repeated runs could grow the prompt without bound (~+1000 tokens
            # each, and there is no convergence check). Default to 25% headroom.
            budget = args.budget
            if budget is None:
                try:
                    from src import dsl_verify as _dv
                    # measured, not len/4 — that heuristic is ASCII-centric and
                    # underestimates Devanagari badly (13,276 real tokens came out
                    # as 10,689), producing a default ceiling BELOW the input.
                    cur = _dv._count_tokens(Path(args.dsl_path).read_text())
                    if cur:
                        budget = int(cur * 1.25)
                        print(f"(no --budget given; capping at {budget} tokens, "
                              f"25% over the current {cur})")
                except OSError:
                    budget = None
            run_auto(args.dsl_path, args.client, budget)
        except llm.LLMUnavailable as e:
            # A missing key is a setup step, not a crash — show what to do, not a
            # stack trace. Still exits non-zero so CI/scripts notice.
            print(f"\n{'=' * 68}")
            print("Cannot run --auto: no LLM access configured.")
            print("=" * 68)
            print(f"\n{e}\n")
            print("To enable it:")
            print("    export ANTHROPIC_API_KEY=sk-ant-...")
            print(f"    python3 {Path(__file__).name} {args.dsl_path} "
                  f"--client {args.client} --auto\n")
            print("Everything except the three LLM judgment calls works without a "
                  "key. To see the mechanical half (mining + audit + review queue),\n"
                  "drop --auto:")
            print(f"    python3 {Path(__file__).name} {args.dsl_path} "
                  f"--client {args.client}\n")
            raise SystemExit(2)
    else:
        run(args.dsl_path, args.client, args.budget, args.apply, args.accept, args.reject)


if __name__ == "__main__":
    main()
