"""RETIRED: superseded by run_client.py. Kept for reference.

Generate the process GRAPH (the original DFG / master_graph) from a chosen dataset.

  python -m scripts.legacy.make_graph --data mp3     # from the audio recordings
  python -m scripts.legacy.make_graph --data txt     # from the original text transcripts

Output: data/output/<dataset>/master_graph.png
"""
import argparse

from scripts.legacy.pipeline import generate

ap = argparse.ArgumentParser(description="Build the process graph (DFG).")
ap.add_argument("--data", choices=["mp3", "txt"], required=True,
                help="mp3 = audio recordings, txt = original transcripts")
ap.add_argument("--transcribe", action="store_true",
                help="(mp3 only) transcribe recordings first; off by default (uses existing transcripts)")
ap.add_argument("--limit", type=int, default=None,
                help="with --transcribe: max recordings to transcribe")
args = ap.parse_args()

generate(args.data, "dfg", transcribe=args.transcribe, limit=args.limit)
