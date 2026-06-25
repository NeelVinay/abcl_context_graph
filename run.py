"""Entry point for the ABCL context-graph pipeline.

  python run.py --all            process all transcripts in data/transcripts/
  python run.py --extract PATH   process one transcript
  python run.py --mock           demo on fake data (no transcripts)
  python run.py --taxonomy       discover the intent taxonomy from mock

Flags: --min-count N  --top-k N  --shape {ellipse,box,circle}  --words-on-graph

Outputs (data/output/): master_graph.png (structure), master_graph.json (data),
report.md (choice of words + per-turn intent capture).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import networkx as nx

import config
from src import visualize
from src.merge import build_master

_BUNDLE = {"b": "unset"}  # lazily-built embedding model, shared across all calls


def _get_bundle():
    if _BUNDLE["b"] == "unset":
        from src import distill
        if distill.MODEL_PATH.exists():
            _BUNDLE["b"] = None   # distilled model handles classification; no rule-bundle needed
        else:
            from src.extract import build_model_bundle
            _BUNDLE["b"] = build_model_bundle()
    return _BUNDLE["b"]


def _load_or_extract(path) -> dict:
    """Return cached extraction if present, else extract and cache it."""
    from src.extract import extract_call
    call_id = Path(path).stem[:8]
    cache = config.CACHE_DIR / f"{call_id}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    call = extract_call(path, bundle=_get_bundle())
    cache.write_text(json.dumps(call, indent=2, ensure_ascii=False))
    return call


def _serialize(g: nx.DiGraph) -> dict:
    """node-link JSON; convert provenance sets to sorted lists so it's JSON-safe."""
    h = g.copy()
    for _, d in h.nodes(data=True):
        if isinstance(d.get("calls"), set):
            d["calls"] = sorted(d["calls"])
    for _, _, d in h.edges(data=True):
        if isinstance(d.get("calls"), set):
            d["calls"] = sorted(d["calls"])
    return nx.node_link_data(h)


def _write_outputs(g, calls, args) -> None:
    from src.glossary import write_glossary
    from src.report import write_report, write_turns
    out_json = config.OUTPUT_DIR / "master_graph.json"
    out_json.write_text(json.dumps(_serialize(g), indent=2, ensure_ascii=False))
    rpt = write_report(g, calls)
    turns = write_turns(calls)
    gls = write_glossary()
    print(visualize.text_summary(g, calls))
    img = visualize.render_graphviz(
        g, str(config.OUTPUT_DIR / "master_graph"),
        min_count=args.min_count, top_k=args.top_k,
        shape=args.shape, show_phrasings=args.words_on_graph,
    )
    print(f"\nWrote {out_json}")
    print(f"Wrote {rpt}   <- keywords + sentiment + tool calls (aggregated)")
    print(f"Wrote {turns}   <- per-turn intent capture (every agent/customer turn)")
    print(f"Wrote {gls}   <- glossary of what each intent means")
    if img:
        print(f"Wrote {img}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mock", action="store_true", help="demo on fake calls (no transcripts)")
    ap.add_argument("--taxonomy", action="store_true", help="discover intent taxonomy from mock")
    ap.add_argument("--extract", metavar="PATH", help="extract ONE real transcript")
    ap.add_argument("--all", action="store_true", help="extract ALL transcripts in data/transcripts/")
    ap.add_argument("--min-count", type=int, default=config.MIN_EDGE_COUNT,
                    help="only draw transitions taken by at least this many calls (higher = cleaner)")
    ap.add_argument("--top-k", type=int, default=2,
                    help="keep only each step's top-K most common next-steps (0 = all)")
    ap.add_argument("--shape", choices=["ellipse", "box", "circle"], default="ellipse",
                    help="node shape on the graph (ellipse is the clean default)")
    ap.add_argument("--words-on-graph", action="store_true",
                    help="put a sample phrase on each node (off by default; words live in report.md)")
    args = ap.parse_args()

    if args.taxonomy:
        from tests.mock_data import MOCK_CALLS
        from src.taxonomy import TAXONOMY_PATH, discover_taxonomy
        tax = discover_taxonomy(MOCK_CALLS)
        print("Discovered taxonomy (intent -> count):")
        for intent, n in sorted(tax.items(), key=lambda x: -x[1]):
            print(f"  {n:>3}x  {intent}")
        print(f"\nSaved to {TAXONOMY_PATH}")
        return

    if args.all:
        files = sorted(p for p in config.TRANSCRIPTS_DIR.iterdir()
                       if p.suffix.lower() in (".txt", ".json"))
        if not files:
            raise SystemExit(f"No transcripts in {config.TRANSCRIPTS_DIR} — drop .txt/.json files there.")
        print(f"Processing {len(files)} transcript(s) ...\n")
        calls = [_load_or_extract(p) for p in files]
        _write_outputs(build_master(calls), calls, args)
        return

    if args.extract:
        call = _load_or_extract(args.extract)
        _write_outputs(build_master([call]), [call], args)
        return

    if args.mock:
        from tests.mock_data import MOCK_CALLS as calls
        _write_outputs(build_master(calls), calls, args)
        return

    raise SystemExit("Pick a mode: --all | --extract PATH | --mock | --taxonomy")


if __name__ == "__main__":
    main()
