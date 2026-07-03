"""Shared helper for the two viz entry points (make_flowchart.py / make_graph.py).

Dataset selector:
  mp3  -> transcripts in data/audio_transcripts (produced from leads_mp3_data recordings).
  txt  -> the original text transcripts in data/transcripts.

By default this builds ONLY from transcripts that already exist — it does NOT transcribe
(transcription is the slow, heavy Whisper step). To transcribe first, pass transcribe=True
with an optional limit; use run_transcribe.py directly for large/overnight runs.

Outputs go to a per-dataset folder so nothing clobbers the committed demo in data/output.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import config

# Single output home, one subfolder per dataset:
#   data/output/mp3/  <- JustDial audio recordings
#   data/output/txt/  <- original ABCL text transcripts
DATASETS = {
    "mp3": {"src": config.AUDIO_TRANSCRIPTS_DIR, "out": config.OUTPUT_DIR / "mp3",
            "audio": config.AUDIO_SRC},
    "txt": {"src": config.TRANSCRIPTS_DIR,       "out": config.OUTPUT_DIR / "txt",
            "audio": None},
}


def _transcribe(audio_src: Path, limit: int | None) -> None:
    """Explicitly transcribe recordings (skip-if-exists). Only runs when asked."""
    mp3s = list(Path(audio_src).rglob("*.mp3"))
    if not mp3s:
        print(f"No .mp3 files found in {audio_src}.")
        return
    n = min(limit, len(mp3s)) if limit else len(mp3s)
    print(f"Transcribing up to {n} recording(s) (already-done ones are skipped)...")
    subprocess.run([sys.executable, "run_transcribe.py", "--limit", str(n)],
                   cwd=config.ROOT, check=True)


def generate(dataset: str, graph: str, extra: list[str] | None = None,
             transcribe: bool = False, limit: int | None = None) -> None:
    """dataset: 'mp3' | 'txt'.  graph: 'flow' | 'dfg' | 'both'.
    Builds from EXISTING transcripts by default. transcribe=True runs Whisper first
    (mp3 only); limit caps how many recordings to transcribe."""
    cfg = DATASETS[dataset]
    if transcribe and cfg["audio"]:
        _transcribe(cfg["audio"], limit)
    n = len(list(Path(cfg["src"]).glob("*.txt")))
    if n == 0:
        raise SystemExit(f"No transcripts in {cfg['src']}. "
                         f"{'Run with --transcribe to create them.' if cfg['audio'] else ''}")
    print(f"Building {graph} graph from {n} existing transcript(s) in {cfg['src']}")
    cmd = [sys.executable, "run.py", "--all",
           "--src", str(cfg["src"]), "--out", str(cfg["out"]), "--graph", graph]
    cmd += extra or []
    subprocess.run(cmd, cwd=config.ROOT, check=True)
    print(f"\nDone. Outputs in {cfg['out']}")
