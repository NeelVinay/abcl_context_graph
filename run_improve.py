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
        for idx in accept_ids:
            if not (1 <= idx <= len(queue_now)):
                print(f"  ! [{idx}] out of range (queue currently has {len(queue_now)} items), skipped")
                continue
            item = queue_now[idx - 1]
            dsl_mine.save_decision(client_key, item.decision_key, accepted=True)
            if isinstance(item, dsl_mine.AnchorGap):
                e = dsl_fix.make_add_anchors_edit(d, item)
                if e:
                    accepted_edits.append(e)
            else:
                print(f"  ! [{idx}] uncovered cluster accepted for tracking (won't be "
                      f"re-proposed), but produces no edit — write a name + say() answer "
                      f"by hand, then add it to the prompt directly")
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


def _write_changes_md(dsl_path: Path, edits: list, out_path: Path) -> None:
    lines = [f"# Changes — {dsl_path.name}\n"]
    for e in edits:
        lines.append(f"## {e.kind}")
        lines.append(f"- {e.rationale}")
        if e.evidence:
            lines.append("- evidence:")
            for ev in e.evidence:
                lines.append(f"  - {ev}")
        lines.append("")
    changes_path = out_path.parent / "CHANGES.md"
    changes_path.write_text("\n".join(lines))
    print(f"Wrote {changes_path}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("dsl_path", help="path to the .raven prompt")
    ap.add_argument("--client", required=True, help="client key, e.g. abcl")
    ap.add_argument("--budget", type=int, default=None, help="token ceiling")
    ap.add_argument("--apply", action="store_true", help="write in place (default: dry run)")
    ap.add_argument("--accept", default=None, help="comma-separated queue item numbers to accept")
    ap.add_argument("--reject", default=None, help="comma-separated queue item numbers to reject")
    args = ap.parse_args()
    run(args.dsl_path, args.client, args.budget, args.apply, args.accept, args.reject)


if __name__ == "__main__":
    main()
