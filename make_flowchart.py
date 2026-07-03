"""Generate the top-to-bottom FLOW TREE (flowchart) from a chosen dataset.

  python make_flowchart.py --data mp3     # from the audio recordings
  python make_flowchart.py --data txt     # from the original text transcripts
  python make_flowchart.py --data mp3 --all-flows   # expand every flow (wide at scale)

Readable-by-default (folds rare flows into "+N other flows"); --all-flows shows them all.
Output: <dataset>/flow_tree.png  (data/output_audio for mp3, data/output_txt for txt)
"""
import argparse

from pipeline import generate

ap = argparse.ArgumentParser(description="Build the call-flow tree (flowchart).")
ap.add_argument("--data", choices=["mp3", "txt"], required=True,
                help="mp3 = audio recordings, txt = original transcripts")
ap.add_argument("--all-flows", action="store_true",
                help="show every flow (no folding) — can be very wide on large datasets")
ap.add_argument("--transcribe", action="store_true",
                help="(mp3 only) transcribe recordings first; off by default (uses existing transcripts)")
ap.add_argument("--limit", type=int, default=None,
                help="with --transcribe: max recordings to transcribe")
args = ap.parse_args()

# default: readable folding; --all-flows: full expansion
extra = ["--flow-top-k", "0"] if args.all_flows else ["--flow-top-k", "3", "--flow-min-count", "2"]
generate(args.data, "flow", extra, transcribe=args.transcribe, limit=args.limit)
