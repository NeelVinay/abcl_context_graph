"""Executive flow chart for the Myntra calls, using the REAL Claude-labeled gold
intents (data/gold_generic/labels.jsonl) rather than the raw cache's base_intent —
the cache was populated by extract_call()'s classifier routing, which has no Myntra-
aware model yet and silently falls back to the ABCL classifier's guesses. The gold
labels are the actual ground truth from the labeling pass, so the chart should be
built from those.

Also sets disposition="none" for every call: src/dispositions.py's disposition
prototypes are ABCL/JustDial-specific (loan objections, lead complaints) and have no
Myntra entry — letting assign_dispositions() run on Myntra calls would silently
apply the wrong domain's prototypes. Skipping it just gives every call the same
"No clear disposition" root branch, which is honest (no disposition signal exists
for this domain yet) rather than a wrong one.

    python -m scripts._myntra_exec_chart
"""
from __future__ import annotations

import json

import config
from src.flowtree import build_stage_dag, greedy_main_path
from src.visualize import visualize_exec
from src.report import write_report, write_turns
from src.glossary import write_glossary
from src.merge import build_master
from src.generic_taxonomy import ACTIONS

TRANSFER_CUES = ["specialized team", "expert agent", "connect कर", "connect कर रही",
                 "transferring your call"]


def _outcome(turns: list[dict]) -> str:
    text = " ".join(t["text"] for t in turns).lower()
    if any(c.lower() in text for c in TRANSFER_CUES):
        return "transferred"
    if turns and turns[-1].get("base_intent") == "end_call":
        return "completed"
    return "incomplete"


def load_myntra_calls() -> list[dict]:
    gold = {}
    for line in (config.DATA / "gold_generic" / "labels.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        r = json.loads(line)
        gold[(r["call_id"], r["index"])] = r

    calls = []
    for f in sorted(config.CACHE_DIR.glob("GEN-myntra-*.json")):
        c = json.loads(f.read_text())
        turns = []
        for t in c["turns"]:
            g = gold.get((c["call_id"], t["index"]))
            base = g["base_intent"] if g else "other"
            pair = ACTIONS.get(base, {})
            turns.append({
                **t,
                "base_intent": base,
                "intent": pair.get(t["speaker"], f"{t['speaker']}_{base}"),
                "sentiment": g.get("sentiment") if g else t.get("sentiment"),
                "tool": g.get("tool") if g else t.get("tool"),
                "keywords": g.get("keywords", []) if g else t.get("keywords", []),
            })
        calls.append({
            "call_id": c["call_id"], "turns": turns,
            "outcome": _outcome(turns), "disposition": "none",
        })
    return calls


def run():
    calls = load_myntra_calls()
    print(f"{len(calls)} Myntra calls loaded with gold-label intents")
    from collections import Counter
    print("outcomes:", Counter(c["outcome"] for c in calls))

    out_dir = config.GENERIC_OUTPUT_DIR
    # with_disposition=False: Myntra has no disposition classifier of its own (those
    # prototypes are ABCL/JustDial-specific) — skip it rather than show one
    # uninformative "No clear disposition" node on every call.
    # build_stage_dag (not build_flow_tree): reconverging DAG over coarse stages —
    # the structured, SOP-like look — instead of a per-path tree.
    dag = build_stage_dag(calls, with_disposition=False, min_count=3)
    main = greedy_main_path(dag)
    img = visualize_exec(dag, str(out_dir / "myntra_exec"), title="Myntra — Call Flow",
                         main_edges=main)
    print(f"Wrote {img}" if img else "Exec chart render skipped (graphviz unavailable)")

    old = out_dir / "myntra_flow_tree.png"
    if old.exists():
        old.unlink()
        print(f"Removed old-style {old} — myntra_exec.png is now the only chart")

    g = build_master(calls)
    rpt = write_report(g, calls, out_dir / "myntra_report.md")
    turns_md = write_turns(calls, out_dir / "myntra_turns.md")
    gls = write_glossary(out_dir / "myntra_intents.md", g)
    print(f"Wrote {rpt}")
    print(f"Wrote {turns_md}")
    print(f"Wrote {gls}")


if __name__ == "__main__":
    run()
