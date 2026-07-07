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


def _load_or_extract(path, vocab=None) -> dict:
    """Return cached extraction if present, else extract and cache it.
    When a corpus `vocab` is supplied, keywords depend on it, so we always re-extract
    (the cache may hold stale keywords) — extraction is fast with the local model."""
    from src.extract import extract_call
    call_id = Path(path).stem                       # full stem: unique for LCS-* STT names
    cache = config.CACHE_DIR / f"{call_id}.json"
    legacy = config.CACHE_DIR / f"{call_id[:8]}.json"   # old hex-named demo cache
    if vocab is None:
        if cache.exists():
            return json.loads(cache.read_text())
        if legacy.exists():
            return json.loads(legacy.read_text())
    call = extract_call(path, bundle=_get_bundle(), vocab=vocab)
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
    out_dir = Path(args.out) if getattr(args, "out", None) else config.OUTPUT_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    out_json = out_dir / "master_graph.json"
    out_json.write_text(json.dumps(_serialize(g), indent=2, ensure_ascii=False))
    rpt = write_report(g, calls, out_dir / "report.md")
    turns = write_turns(calls, out_dir / "turns.md")
    gls = write_glossary(out_dir / "intents.md", g)   # dataset-aware: only intents present
    print(visualize.text_summary(g, calls))
    print(f"\nWrote {out_json}")
    print(f"Wrote {rpt}   <- keywords + sentiment + tool calls (aggregated)")
    print(f"Wrote {turns}   <- per-turn intent capture (every agent/customer turn)")
    print(f"Wrote {gls}   <- glossary of what each intent means")
    mode = getattr(args, "graph", "flow")
    if mode in ("sop", "sop-exec"):
        from src.dispositions import assign_dispositions
        from src import sop_flow
        assign_dispositions(calls)
        if mode == "sop":
            sop = sop_flow.render(calls, str(out_dir / "sop_flow"))
            if sop:
                print(f"Wrote {sop}   <- ABCL SOP call-flow (fixed procedure + real call counts)")
        else:
            sop = sop_flow.render_exec(calls, str(out_dir / "sop_exec"))
            if sop:
                print(f"Wrote {sop}   <- ABCL SOP exec view (collapsed, C-suite clean)")
        return
    if mode in ("flow", "both"):
        from src.dispositions import assign_dispositions
        assign_dispositions(calls)     # semantic call-level disposition for the early branch
        from src.flowtree import build_flow_tree
        # flow tree prunes on CALL counts (not edge counts), so use its own small defaults
        tree = build_flow_tree(calls, top_k=args.flow_top_k, min_count=args.flow_min_count)
        ftree = visualize.visualize_flow(tree, str(out_dir / "flow_tree"))
        if ftree:
            print(f"Wrote {ftree}   <- top-to-bottom call-flow tree")
    if mode in ("dfg", "both"):
        img = visualize.render_graphviz(
            g, str(out_dir / "master_graph"),
            min_count=args.min_count, top_k=args.top_k,
            shape=args.shape, show_phrasings=args.words_on_graph,
        )
        if img:
            print(f"Wrote {img}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mock", action="store_true", help="demo on fake calls (no transcripts)")
    ap.add_argument("--taxonomy", action="store_true", help="discover intent taxonomy from mock")
    ap.add_argument("--extract", metavar="PATH", help="extract ONE real transcript")
    ap.add_argument("--all", action="store_true", help="extract ALL transcripts in data/transcripts/")
    ap.add_argument("--src", metavar="DIR", help="directory to read transcripts from with --all "
                    "(default: data/transcripts; use data/audio_transcripts for STT output)")
    ap.add_argument("--out", metavar="DIR", help="directory to write outputs to "
                    "(default: data/output; keeps the STT graph separate from the demo graph)")
    ap.add_argument("--min-count", type=int, default=config.MIN_EDGE_COUNT,
                    help="only draw transitions taken by at least this many calls (higher = cleaner)")
    ap.add_argument("--top-k", type=int, default=2,
                    help="keep only each step's top-K most common next-steps (0 = all)")
    ap.add_argument("--shape", choices=["ellipse", "box", "circle"], default="ellipse",
                    help="node shape on the graph (ellipse is the clean default)")
    ap.add_argument("--words-on-graph", action="store_true",
                    help="put a sample phrase on each node (off by default; words live in report.md)")
    ap.add_argument("--graph", choices=["flow", "dfg", "both", "sop", "sop-exec"], default="flow",
                    help="flow = flow tree (default); dfg = process graph; "
                    "sop = fixed ABCL SOP call-flow with real call counts overlaid; "
                    "sop-exec = C-suite view (collapsed form steps, no zero-count branches)")
    ap.add_argument("--flow-top-k", type=int, default=0,
                    help="flow tree: max branches per node before folding into a stub "
                    "(0 = show EVERY flow, no folding)")
    ap.add_argument("--flow-min-count", type=int, default=1,
                    help="flow tree: fold child flows taken by fewer than this many calls")
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
        src = Path(args.src) if args.src else config.TRANSCRIPTS_DIR
        files = sorted(p for p in src.iterdir()
                       if p.suffix.lower() in (".txt", ".json"))
        if not files:
            raise SystemExit(f"No transcripts in {src} — drop .txt/.json files there.")
        print(f"Processing {len(files)} transcript(s) ...\n")
        # Build the corpus keyword vocabulary from the parsed turn texts (not raw files,
        # so speaker labels don't leak), then extract with it.
        from src.extract import build_keyword_vocab, _load_turns
        vocab = build_keyword_vocab(" ".join(t["text"] for t in _load_turns(p)) for p in files)
        print(f"Keyword vocabulary: {len(vocab)} recurring terms\n")
        calls = [_load_or_extract(p, vocab=vocab) for p in files]
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
