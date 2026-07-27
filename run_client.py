"""Single entry point: point it at a folder of raw call transcripts, for ANY
client, from ANY source, and it produces ONE output folder with everything —
executive flow chart, report, per-turn capture, and glossary.

  python run_client.py <folder>                    auto-detect the client, regenerate fresh
  python run_client.py <folder> --client myntra    force a specific client
  python run_client.py <folder> --append            add to the client's existing set instead
                                                     of replacing it

Client selection:
  1. --client NAME, if given: matches a known client (abcl / justdial / myntra) if
     the name matches one, else creates a new client with that name.
  2. Otherwise, auto-detected from the transcripts themselves — filename prefix
     first (e.g. JustDial's "LCS-"), then a content signature (e.g. ABCL's agent
     always says "Aditya Birla Capital", Myntra's always says "मिंत्रा"/"मीरा").
     See src/clients.py.
  3. If nothing matches, a new client is created, named after the input folder,
     and routed through the shared broad taxonomy (src/generic_taxonomy.py) — no
     taxonomy needs to be hand-built before a brand-new client can be processed.

Output: data/output/<client>_output/  — always the SAME folder for a given client.
Running this again just regenerates that folder fresh. The underlying transcript
set for a client is REPLACED by default (this run's input becomes the new full
set); pass --append to add these transcripts to what the client already has
instead of replacing it.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path

import config
from src import clients as clientsmod


def _slugify(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", name.strip().lower()).strip("_")
    return s or "client"


def _client_by_key_or_new(key: str) -> clientsmod.Client:
    known = {c.key: c for c in clientsmod.get_known_clients()}
    return known.get(key) or clientsmod.make_generic_client(key)


def _gather_transcripts(folder: Path) -> list:
    if not folder.is_dir():
        return []
    return sorted(p for p in folder.iterdir() if p.suffix.lower() in (".txt", ".json"))


def resolve_client(input_dir: Path, client_arg: str | None) -> clientsmod.Client:
    if client_arg:
        return _client_by_key_or_new(_slugify(client_arg))
    files = _gather_transcripts(input_dir)
    if not files:
        raise SystemExit(f"No .txt/.json transcripts found in {input_dir}")
    detected = clientsmod.detect_client_for_batch(files)
    if detected:
        return detected
    return clientsmod.make_generic_client(_slugify(input_dir.name))


def sync_transcripts(client: clientsmod.Client, input_dir: Path, append: bool) -> int:
    """Copy transcripts from input_dir into the client's persistent store. Returns
    the total number of transcripts now in that store. A no-op when input_dir IS
    already the client's own store (e.g. re-running directly against it)."""
    target = client.transcripts_dir
    target.mkdir(parents=True, exist_ok=True)
    if input_dir.resolve() != target.resolve():
        if not append:
            for f in target.iterdir():
                if f.is_file():
                    f.unlink()
        for f in _gather_transcripts(input_dir):
            shutil.copy2(f, target / f.name)
    return len(_gather_transcripts(target))


def extract_all(client: clientsmod.Client, transcripts: list) -> list:
    from src.extract import build_keyword_vocab, extract_call, _load_turns
    vocab = build_keyword_vocab(" ".join(t["text"] for t in _load_turns(p)) for p in transcripts)
    calls = []
    for p in transcripts:
        call_id = p.stem
        cache_path = config.CACHE_DIR / f"{call_id}.json"
        call = extract_call(p, client=client, vocab=vocab)
        cache_path.write_text(json.dumps(call, indent=2, ensure_ascii=False))
        calls.append(call)
    return calls


def build_outputs(client: clientsmod.Client, calls: list, out_dir: Path):
    from src.glossary import write_glossary
    from src.merge import build_master
    from src.report import write_report, write_turns

    out_dir.mkdir(parents=True, exist_ok=True)
    g = build_master(calls)

    write_report(g, calls, out_dir / "report.md", title=f"{client.label} — Context Graph Report")
    write_turns(calls, out_dir / "turns.md")
    write_glossary(out_dir / "intents.md", g)

    chart_path = out_dir / f"{client.key}_exec"
    if client.has_sop_skeleton:
        from src import sop_flow
        from src.dispositions import assign_dispositions
        assign_dispositions(calls)
        img = sop_flow.render_exec(calls, str(chart_path))
    else:
        from src.flowtree import build_stage_dag, greedy_main_path
        from src.visualize import visualize_exec
        dag = build_stage_dag(calls, with_disposition=client.has_dispositions,
                              min_count=max(2, len(calls) // 15))
        main = greedy_main_path(dag)
        img = visualize_exec(dag, str(chart_path), title=f"{client.label} — Call Flow",
                             main_edges=main)
    return img


def run(input_dir_arg: str, client_arg: str | None, append: bool) -> None:
    input_dir = Path(input_dir_arg).expanduser().resolve()
    if not input_dir.is_dir():
        raise SystemExit(f"{input_dir} is not a directory")

    client = resolve_client(input_dir, client_arg)
    n = sync_transcripts(client, input_dir, append)
    action = "appended to" if append else "replaced with this input"
    print(f"Client: {client.label}")
    print(f"Transcript set {action} — {n} transcript(s) now in {client.transcripts_dir}")

    transcripts = _gather_transcripts(client.transcripts_dir)
    calls = extract_all(client, transcripts)

    out_dir = config.OUTPUT_DIR / f"{client.key}_output"
    if out_dir.exists():
        shutil.rmtree(out_dir)
    img = build_outputs(client, calls, out_dir)

    print(f"\n{len(calls)} calls processed -> {out_dir}/")
    if img:
        print(f"  chart:    {img}")
    print(f"  report:   {out_dir / 'report.md'}")
    print(f"  turns:    {out_dir / 'turns.md'}")
    print(f"  glossary: {out_dir / 'intents.md'}")


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input_dir", help="folder of raw transcripts (.txt or .json), any client")
    ap.add_argument("--client", default=None,
                    help="force a client name instead of auto-detecting")
    ap.add_argument("--append", action="store_true",
                    help="add these transcripts to the client's existing set instead of "
                    "replacing it (default: replace)")
    args = ap.parse_args()
    run(args.input_dir, args.client, args.append)


if __name__ == "__main__":
    main()
