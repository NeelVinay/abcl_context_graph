# ABCL / JustDial Call Context Graphs

Turns call-center recordings into **visual analytics** — flow charts, context graphs, and
SOP overlays that show how calls actually progress. The whole pipeline runs **100% locally**;
customer audio and transcripts never leave the machine.

Two domains are supported, each with its own trained intent model (auto-selected by filename):
- **ABCL** — loan-application outbound calls (uuid-named `.txt` transcripts).
- **JustDial** — lead-generation support calls (`LCS-*.txt`, from `leads_mp3_data`).

---

## ⚡ Quick start — ABCL SOP call-flow chart (no transcription needed)

The `data/test_100/` transcripts and extraction cache are **already committed**.
After a one-time environment setup you can generate the C-suite SOP chart in ~1–2 min.

### One-time setup

```bash
# 1. System binary (rendering engine)
brew install graphviz          # macOS
# sudo apt install graphviz    # Linux

# 2. Python environment
cd abcl-context-graph
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# ↑ downloads torch + sentence-transformers (~1–2 GB, takes ~10 min first time)
```

> **First run** also auto-downloads the multilingual embedding model
> (`paraphrase-multilingual-MiniLM-L12-v2`, ~500 MB, cached to `~/.cache/sentence-transformers/`).
> Subsequent runs are instant.

### Generate the SOP chart

```bash
# C-suite exec view (collapsed form steps, percentages, clean layout)
python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop-exec

# Detailed view (every individual SOP step, full skeleton including zero-count branches)
python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop
```

Output: `data/output/test_100_sop/sop_exec.png` (or `sop_flow.png` for the detailed view).

### What you do NOT need for the SOP chart
| Requirement | Needed? |
|---|---|
| `ffmpeg` | ✗ No — only for transcribing audio |
| HuggingFace token | ✗ No — only for pyannote diarization |
| Pyannote / WhisperX | ✗ No — only for transcribing audio |
| Audio / MP3 files | ✗ No — transcripts are in `data/test_100/` |
| Re-labeling / training | ✗ No — intent model is in `data/models/` |

---

## What each output shows

### SOP call-flow chart (`--graph sop-exec` / `--graph sop`)
A **fixed ABCL procedure skeleton** (decision diamonds, labeled branches, colored terminals)
with real call data overlaid as edge counts and percentages.

- **`sop-exec`** — C-suite presentation view: granular form steps collapsed into summary
  boxes (e.g. all 5 personal-detail fields → one "Personal Details" node), zero-count
  branches hidden, percentages on every edge, 150 DPI, bold green main path.
- **`sop`** — Full detailed view: every individual SOP node and branch, including steps
  that had zero calls in the dataset (useful for auditing coverage).

The **green path** is the greedy main path — at each decision point it follows the branch
with the most calls, showing the single most common end-to-end journey.

### Flow tree (`--graph flow`, default)
Top-down call-flow tree driven purely by the data. Shows how calls actually branch by
disposition (callback / not-interested / proceeding / etc.) then by intent sequence.

### Process graph / DFG (`--graph dfg`)
Classic directly-follows process graph — every intent-to-intent transition weighted by
call count.

---

## Setup for transcription (optional — only if you have new audio)

All of the above works **without** this section. Only do this if you are transcribing
new `.mp3` recordings.

**Additional system binary:**
```bash
brew install ffmpeg             # macOS
# sudo apt install ffmpeg       # Linux
```

**HuggingFace token** (diarization model is gated):
```bash
huggingface-cli login          # paste a free read token; answer 'n' to git-credential
```
Accept the terms (once) while logged in:
- `pyannote/speaker-diarization-3.1`
- `pyannote/segmentation-3.0`

First transcription run downloads ~3–4 GB of models (Whisper large-v3, pyannote, aligner).

### Transcribe recordings
```bash
python run_transcribe.py --limit 100
# Reads .mp3 from ~/Downloads/leads_mp3_data
# Writes Agent:/Customer: plain-text to data/audio_transcripts/<id>.txt
# Resumable: re-running skips files already done. --overwrite to redo.
```
Note: transcription is CPU-bound on Apple Silicon (~2–3× realtime). A 100-call batch
takes hours. Keep the Mac awake and plugged in; the run is resumable.

---

## All pipeline commands

```bash
# -- SOP flow charts (ABCL, from committed test_100 data) ---------------------
python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop-exec
python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop

# -- Flow tree / DFG (any transcript directory) --------------------------------
python run.py --all --src data/test_100  --out data/output/test_100  --graph flow
python run.py --all --src data/audio_transcripts --out data/output/mp3 --graph flow

# -- Transcribe new audio then build chart in one go --------------------------
python make_flowchart.py --data mp3 --transcribe --limit 100
```

---

## Quick reference

| Task | Command |
|---|---|
| **SOP exec chart (C-suite)** | `python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop-exec` |
| SOP detailed chart | `python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop` |
| Flow tree from ABCL test data | `python run.py --all --src data/test_100 --out data/output/test_100 --graph flow` |
| Flow tree from JustDial audio transcripts | `python run.py --all --src data/audio_transcripts --out data/output/mp3 --graph flow` |
| Transcribe up to 100 recordings | `python run_transcribe.py --limit 100` |
| Transcribe then build flow tree | `python make_flowchart.py --data mp3 --transcribe --limit 100` |

---

## Output locations

```
data/output/
├── test_100_sop/    # ABCL SOP charts (sop_exec.png, sop_flow.png)
├── test_100/        # ABCL flow tree + report from the 116-call test set
├── mp3/             # JustDial (audio transcripts) results
└── original/        # frozen original demo (do not overwrite)
```

Each folder contains:
- `sop_exec.png` / `sop_flow.png` — SOP call-flow overlaid with real call counts (sop modes only).
- `flow_tree.png` — top-down call-flow tree (start → branches → colored outcomes).
- `report.md` — keywords + sentiment + tool calls, per intent.
- `turns.md` — every turn: speaker · intent · sentiment · tool · keywords.
- `intents.md` — glossary of the intents present in that dataset, with descriptions + counts.

---

## How it works

- **Dispositions:** call-level classification of *why* a call happened — lightweight
  prototype matching via sentence embeddings (no API, `src/dispositions.py`). ABCL and
  JustDial have separate prototype sets; routing is by call-id prefix (`LCS-*` = JustDial).
- **SOP skeleton:** fixed ABCL procedure DAG defined in `src/sop_flow.py` — each call is
  walked through the skeleton using its disposition + intents + outcome to produce an
  edge-count overlay.
- **Intents:** local classifier (sentence-embeddings + logistic regression) distilled from
  Claude-labeled gold data. Trained once, runs fully locally. Models in `data/models/`.
- **Keywords:** corpus-driven — terms that recur across calls (PII-safe by construction).
- **Flow tree:** per-call traces merged into a weighted DAG, rendered top-to-bottom
  (`src/flowtree.py`). Main path = greedy walk (fattest branch at each step).
- **Transcription:** WhisperX (`large-v3`) + pyannote diarization → per-turn
  `Agent:`/`Customer:` text (`src/transcribe.py`). Only needed for new audio.

---

## Security / PII

- All processing is **local** — no data is sent to any API at runtime.
- `data/test_100/` and `data/audio_transcripts/` contain real customer transcripts — treat
  as confidential, do not share or upload.
- The HF token lives at `~/.cache/huggingface/token` — never echo or commit it.
- Keywords are corpus-frequency filtered and contain no PII by design.
