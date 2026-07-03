# ABCL / JustDial Call Context Graphs

Turns call-center recordings into **context graphs** — visual maps of how calls actually
flow (intents, keywords, dispositions, outcomes). The whole pipeline runs **locally, no
paid API at runtime** (customer audio/PII stays on-machine).

Two stages:
1. **Speech-to-text** — `mp3` recordings → plain-text transcripts (Whisper + diarization).
2. **Graph build** — transcripts → intents/keywords → a **top-down flow tree** and/or the
   classic **process graph (DFG)**, plus `report.md` / `turns.md` / `intents.md`.

Two domains are supported, each with its own trained intent model (auto-selected by the
transcript's filename):
- **ABCL** — loan-application calls (the original `data/transcripts/*.txt`, JSON format).
- **JustDial** — lead-generation support calls (`data/audio_transcripts/LCS-*.txt`, from `leads_mp3_data`).

---

## Setup (one-time)

```bash
cd abcl-context-graph
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**System binaries** (needed for audio + graph rendering):
```bash
brew install ffmpeg graphviz          # macOS
# sudo apt install ffmpeg graphviz    # Linux
```

**HuggingFace token** — only needed if you will **transcribe audio** (the diarization model
is gated). Not needed just to build graphs from existing transcripts.
```bash
huggingface-cli login                 # paste a free read token; answer 'n' to git-credential
```
Then accept the terms (once) on these two gated models while logged into the same account:
- https://huggingface.co/pyannote/speaker-diarization-3.1
- https://huggingface.co/pyannote/segmentation-3.0

First transcription run downloads ~3–4 GB of models (Whisper large-v3, pyannote, aligner).

---

## 1. Transcribe recordings (mp3 → transcript)

```bash
python run_transcribe.py --limit 100
```
- Reads `.mp3` from `~/Downloads/leads_mp3_data` → writes plain-text (`Agent:`/`Customer:`,
  one turn per line) to `data/audio_transcripts/<id>.txt`.
- **Skip-if-exists** (resumable): re-running skips files already done. Use `--overwrite` to redo.
- Flags: `--limit N`, `--src DIR`, `--overwrite`, `--gpu-device auto|mps|cpu`.
- **Note:** transcription is CPU-bound on Apple Silicon (~2–3× realtime) — a full ~100-call
  batch takes hours. Keep the Mac awake/plugged in; the run is resumable if interrupted.

---

## 2. Build the graph (transcript → flow tree / process graph)

Two entry points, each with a `--data` selector (`mp3` = JustDial audio, `txt` = ABCL text):

```bash
python make_flowchart.py --data mp3     # top-to-bottom call-flow tree
python make_graph.py     --data txt     # classic process graph (DFG)
```
- Builds **only from existing transcripts** by default (no transcription).
- Add `--transcribe` (mp3 only) to transcribe first, `--limit N` to cap it.
- `make_flowchart` extra: `--all-flows` shows every flow (very wide at scale; default folds
  rare flows into "+N other flows" for readability).
- Each build takes ~2–3 min (it re-runs the intent model over every turn).

The correct intent model is chosen automatically: `LCS-*` transcripts → JustDial model,
everything else → ABCL model.

---

## Where the outputs are

Everything lands under **`data/output/`**, one subfolder per dataset:

```
data/output/
├── mp3/         # JustDial (audio) results
├── txt/         # ABCL (text) results
└── original/    # frozen original demo (do not overwrite)
```
Each folder contains:
- `flow_tree.png` — the top-down call-flow tree (start → branches → colored outcomes).
- `master_graph.png` / `master_graph.json` — the classic process graph.
- `report.md` — keywords + sentiment + tool calls, per intent.
- `turns.md` — every turn: speaker · intent · sentiment · tool · keywords.
- `intents.md` — glossary of the intents present in that dataset, with descriptions + counts.

---

## How it works (brief)

- **Transcription:** WhisperX (`large-v3`) + silero VAD + pyannote diarization + word-level
  alignment → per-turn `Agent:`/`Customer:` text. A domain prompt, audio clean-up, per-file
  language detection, and repetition guards improve noisy Hinglish phone audio. All in `src/transcribe.py`.
- **Intents:** a small local classifier (sentence-embeddings + logistic regression),
  **distilled** from Claude-labeled gold — trained once at dev time, runs 100% locally after.
  `src/distill.py`, models in `data/models/` (`intent_clf.pkl` = ABCL, `justdial_clf.pkl` = JustDial).
- **Keywords:** corpus-driven — terms that recur across calls (PII-safe by construction).
- **Dispositions:** semantic classification of *why* the call happened, used as the top
  branch of the flow tree (`src/dispositions.py`).
- **Graph:** per-call traces merged into a weighted graph (`src/merge.py`), rendered as a
  flow tree (`src/flowtree.py` + `src/flowstages.py`) or DFG (`src/visualize.py`).

---

## Quick reference

| Task | Command |
|---|---|
| Transcribe up to 100 recordings | `python run_transcribe.py --limit 100` |
| Flow tree from audio | `python make_flowchart.py --data mp3` |
| Flow tree from ABCL text | `python make_flowchart.py --data txt` |
| Process graph (DFG) from audio | `python make_graph.py --data mp3` |
| Show every flow (no folding) | `python make_flowchart.py --data mp3 --all-flows` |
| Transcribe then build in one go | `python make_flowchart.py --data mp3 --transcribe --limit 100` |

(If `python` isn't the venv's, use `.venv/bin/python`.)
