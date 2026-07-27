# ABCL / JustDial Call Context Graphs

This project turns call center recordings into visual analytics: flow charts, context
graphs, and SOP overlays that show how calls actually progress. The pipeline runs
entirely locally. Customer audio and transcripts never leave the machine, and the only
component that ever touches an external model is the offline labeling step described
below, which never runs in production.

Three domains are currently supported:

- **ABCL**: loan application outbound calls (UUID named `.txt` transcripts).
- **JustDial**: lead generation support calls (`LCS-*.txt`, from `leads_mp3_data`).
- **Generic**: a cross client domain for onboarding any new client without building a
  fine grained taxonomy for it first. See "Generalizing to a new client" below.

Each domain has its own trained intent model, selected automatically by filename
convention.

---

## Quick start: ABCL SOP call flow chart (no transcription needed)

The `data/test_100/` transcripts and extraction cache are already committed. After a
one time environment setup, the executive SOP chart can be generated in one to two
minutes.

### One time setup

```bash
# 1. System binary (rendering engine)
brew install graphviz          # macOS
# sudo apt install graphviz    # Linux

# 2. Python environment
cd abcl-context-graph
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# downloads torch and sentence-transformers (roughly 1 to 2 GB, about 10 minutes the first time)
```

The first run also downloads the multilingual embedding model
(`paraphrase-multilingual-MiniLM-L12-v2`, about 500 MB, cached under
`~/.cache/sentence-transformers/`). Subsequent runs are immediate.

### Generate the SOP chart

```bash
# Executive view: collapsed form steps, percentages, clean layout
python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop-exec

# Detailed view: every individual SOP step, including zero-count branches
python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop
```

Output: `data/output/test_100_sop/sop_exec.png` (or `sop_flow.png` for the detailed
view).

### What is not needed for the SOP chart

| Requirement | Needed? |
|---|---|
| `ffmpeg` | No. Only required for transcribing audio. |
| HuggingFace token | No. Only required for pyannote diarization. |
| Pyannote / WhisperX | No. Only required for transcribing audio. |
| Audio / MP3 files | No. Transcripts are already in `data/test_100/`. |
| Re-labeling / training | No. The intent model is already in `data/models/`. |

---

## What each output shows

### SOP call flow chart (`--graph sop-exec` / `--graph sop`)

For ABCL, this is a fixed procedure skeleton (decision diamonds, labeled branches,
colored terminals) with real call data overlaid as edge counts and percentages.

- `sop-exec`: the executive presentation view. Granular form steps are collapsed into
  summary boxes (for example, all five personal detail fields become one "Personal
  Details" node), zero-count branches are hidden, every edge shows a percentage, and
  the single most common path is drawn as a bold green line.
- `sop`: the full detailed view, showing every SOP node and branch, including steps
  with zero calls in the dataset. Useful for auditing coverage.

The green path is a greedy walk: at each decision point it follows the branch with the
most calls, tracing the single most common end to end journey.

For any other domain, the same executive visual style is produced by a different
mechanism, since there is no hand authored skeleton to draw. See "Executive flow chart
for any client" below.

### Flow tree (`--graph flow`, default)

A top down call flow tree driven purely by the data. Shows how calls branch first by
disposition (callback, not interested, proceeding, and so on) and then by intent
sequence.

### Process graph / DFG (`--graph dfg`)

A classic directly follows process graph: every intent to intent transition, weighted
by call count.

---

## Setup for transcription (optional, only for new audio)

Everything above works without this section. Only follow it when transcribing new
`.mp3` recordings.

Additional system binary:

```bash
brew install ffmpeg             # macOS
# sudo apt install ffmpeg       # Linux
```

HuggingFace token (the diarization model is gated):

```bash
huggingface-cli login          # paste a free read token, answer 'n' to git-credential
```

While logged in, accept the terms once for:

- `pyannote/speaker-diarization-3.1`
- `pyannote/segmentation-3.0`

The first transcription run downloads roughly 3 to 4 GB of models (Whisper large-v3,
pyannote, and the aligner).

### Transcribe recordings

```bash
python run_transcribe.py --limit 100
# Reads .mp3 from ~/Downloads/leads_mp3_data
# Writes Agent:/Customer: plain text to data/audio_transcripts/<id>.txt
# Resumable: re-running skips files already done. Use --overwrite to redo them.
```

Transcription is CPU bound on Apple Silicon, at roughly two to three times real time.
A 100 call batch takes hours. Keep the machine awake and plugged in; the run is
resumable if interrupted.

---

## All pipeline commands

```bash
# SOP flow charts (ABCL, from the committed test_100 data)
python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop-exec
python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop

# Flow tree / DFG (any transcript directory)
python run.py --all --src data/test_100  --out data/output/test_100  --graph flow
python run.py --all --src data/audio_transcripts --out data/output/mp3 --graph flow

# Transcribe new audio, then build a chart in one step
python make_flowchart.py --data mp3 --transcribe --limit 100

# Generic (cross client) domain, see "Generalizing to a new client" for full context
python run.py --all --src data/generic_transcripts --out data/output/generic --graph flow
python -m src.labeling emit generic
python -m src.labeling assemble generic
python -m src.distill eval generic
python -m src.distill train generic
```

---

## Quick reference

| Task | Command |
|---|---|
| SOP executive chart (ABCL) | `python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop-exec` |
| SOP detailed chart (ABCL) | `python run.py --all --src data/test_100 --out data/output/test_100_sop --graph sop` |
| Flow tree from ABCL test data | `python run.py --all --src data/test_100 --out data/output/test_100 --graph flow` |
| Flow tree from JustDial audio transcripts | `python run.py --all --src data/audio_transcripts --out data/output/mp3 --graph flow` |
| Transcribe up to 100 recordings | `python run_transcribe.py --limit 100` |
| Transcribe then build a flow tree | `python make_flowchart.py --data mp3 --transcribe --limit 100` |
| Train the generic (cross client) model | `python -m src.distill train generic` |

---

## Output locations

```
data/output/
├── test_100_sop/    ABCL SOP charts (sop_exec.png, sop_flow.png)
├── test_100/        ABCL flow tree and report from the 116 call test set
├── mp3/             JustDial (audio transcripts) results
├── generic/         Cross client domain outputs, one chart per onboarded client
└── original/        Frozen original demo, do not overwrite
```

Each folder generally contains:

- `sop_exec.png` / `sop_flow.png` or `<client>_exec.png`: the call flow chart with real
  call counts overlaid.
- `flow_tree.png`: the top down call flow tree, where applicable.
- `report.md`: keywords, sentiment, and tool calls, per intent.
- `turns.md`: every turn, with speaker, intent, sentiment, tool, and keywords.
- `intents.md`: a glossary of the intents present in that dataset, with descriptions
  and counts.

---

## How it works

- **Dispositions**: call level classification of why a call happened, using lightweight
  prototype matching over sentence embeddings, with no external API call
  (`src/dispositions.py`). ABCL and JustDial each have their own prototype set;
  routing is by call ID prefix (`LCS-*` is JustDial).
- **SOP skeleton**: a fixed ABCL procedure DAG defined in `src/sop_flow.py`. Each call
  is walked through the skeleton using its disposition, intents, and outcome to
  produce an edge count overlay. This only applies to ABCL, since it is a hand
  authored skeleton for one specific call flow.
- **Intents**: a local classifier (sentence embeddings plus logistic regression)
  distilled from Claude labeled gold data. It is trained once and runs entirely
  locally afterward. Models live in `data/models/`.
- **Keywords**: corpus driven. Only terms that recur across multiple calls qualify,
  which makes the keyword list PII safe by construction.
- **Flow tree**: per call traces merged into a weighted tree, rendered top to bottom
  (`src/flowtree.py`). The main path is a greedy walk toward the heaviest branch at
  each step.
- **Executive flow chart**: for any domain, `src/flowtree.build_stage_dag` builds a
  compact directed graph over a small set of coarse stages, where calls that pass
  through the same stage share the same node instead of each branching into its own
  copy. `src/visualize.visualize_exec` renders this in the same visual style as the
  original ABCL executive chart. This is what makes the executive chart format
  reusable for any client, not only ABCL.
- **Transcription**: WhisperX (`large-v3`) with pyannote diarization produces per turn
  `Agent:` / `Customer:` text (`src/transcribe.py`). Only needed for new audio.

---

## Generalizing to a new client

A third domain, `generic`, sits alongside `abcl` and `justdial`. The first two each
have their own fine grained, hand built taxonomy. `generic`
(`src/generic_taxonomy.py`) instead uses one small set of broad, client agnostic
buckets, so the same shared model can be trained across multiple clients at once
rather than requiring a new taxonomy for every client.

The current bucket list is: greeting, agree, disagree, ask_question, answer_query,
confused_repeat, callback_request, person_unavailable, distrust_security,
irate_frustrated, wait_hold, acknowledge, and end_call, with a fallback `other`
category for anything that does not fit.

There is already a precedent in this repository for broad categories outperforming
fine ones: `src/justdial_coarse.py` collapsed JustDial's 24 intent taxonomy down to
about seven buckets after the fine grained model scored only about 32 percent
cross-validation accuracy on noisy speech-to-text output. The `generic` domain applies
that same lesson from the outset, across clients rather than within one.

Claude is used only offline, to help generate training labels. It is never part of the
production or inference path. The model that actually classifies calls is the local
scikit-learn classifier in `data/models/generic_clf.pkl`, in the same way `abcl` and
`justdial` already work.

### Embedding model

The `generic` domain uses `intfloat/multilingual-e5-base`, rather than the
`paraphrase-multilingual-MiniLM-L12-v2` model used by `abcl` and `justdial`. This was
a deliberate, measured choice: in a controlled comparison, switching to this model
improved cross-domain accuracy by six to nine points with no other change. Text
encoded with this model must be prefixed with `"query: "` for both training and
inference; this is handled automatically by `src/distill.embed_prefix_for` and is
stored alongside the trained model so inference always matches training.

### Bootstrapping a shared model without new labeling

Before any new client is added, the `generic` gold set is bootstrapped from data that
already exists, at no additional labeling cost:

- Existing ABCL and JustDial gold labels are recoded into the broad buckets wherever a
  clean, honest mapping exists (`src/generic_bootstrap.py`). Fine grained,
  client-specific procedural intents, such as a PAN card entry step, are left out
  rather than forced into an unrelated bucket.
- The `irate_frustrated` bucket has no equivalent fine intent in either source
  taxonomy. It is instead derived directly from the existing sentiment field, since
  frustration was already being captured there.
- A small number of hand verified real examples fill in buckets with otherwise sparse
  coverage, such as `disagree` and `callback_request`.

This produces a working shared model before a single new client transcript is
labeled.

### Onboarding a new client

1. Collect transcripts in plain text, one turn per line, using `Agent:` and
   `Customer:` prefixes, the same format `src/transcribe.py` already produces. No new
   taxonomy or code is required for a new client.
2. Name the files `GEN-<client>-<call_id>.txt` and place them in
   `data/generic_transcripts/` (`config.GENERIC_TRANSCRIPTS_DIR`). The `GEN-` prefix
   is what routes a call to the `generic` domain instead of the ABCL gold set.

```bash
# 1. Extract and cache raw turns, no labeling yet
python run.py --all --src data/generic_transcripts --out data/output/generic --graph flow

# 2. Emit labeling batches and a labeling guide for the generic taxonomy
python -m src.labeling emit generic

# 3. Label each data/gold_generic/_tolabel/batch_*.json file offline, and write the
#    labeled version to data/gold_generic/_labeled/, following the guide at
#    data/gold_generic/LABELING_GUIDE.md

# 4. Merge the newly labeled batches into the shared gold set
python -m src.labeling assemble generic

# 5. Evaluate how well the model has learned the broad buckets
python -m src.distill eval generic

# 6. Train the shared cross client model
python -m src.distill train generic
```

`src.labeling.assemble` merges new labels into the existing gold file rather than
overwriting it, so labeling one client never discards another client's data.

### How well this actually generalizes

A mixed cross-validation number across all onboarded clients overstates how well the
model will do on a client it has never seen, since the model can partly learn to
recognize which client it is looking at rather than the underlying intent. To measure
the honest number, evaluation should hold one client's calls out entirely, train on
the rest, and score only against the held out client.

Measured this way, across ABCL, JustDial, and Myntra: a client with no data of its own
in training scores roughly 28 to 48 percent accuracy, depending on how different that
client's calls are from the others already in the model. Once even a modest amount of
that client's own real, labeled data is added, accuracy for that client rises to
roughly 68 to 71 percent. Both figures come from held out evaluation, not from
training and testing on the same pool.

The practical implication is that broadening the taxonomy and the shared pipeline
removes the need to design a new taxonomy for each client, but it does not remove the
need for some real, labeled data from that client before the model is reliable on it.

### Executive flow chart for any client

`src/flowtree.build_stage_dag` builds a directed graph over the same small set of
coarse stages used for the flow tree, but unlike the flow tree, calls that pass
through the same stage share a single node rather than each forking into a new branch.
This keeps the chart compact and lets different call journeys reconverge, which is
what gives it the same structured, readable appearance as the original ABCL executive
chart, without relying on a hand authored skeleton. `src/visualize.visualize_exec`
renders this graph in that same visual style: a title banner, right angle routing,
colored terminal nodes by outcome, and a bold green main path through the most common
journey.

`scripts/_myntra_exec_chart.py` is a working example of this for the first onboarded
client, producing `data/output/generic/myntra_exec.png`.

### Sharpening a broad bucket for one client

A broad bucket such as `ask_question` is deliberately generic so it works across
clients, but it can be too coarse for a single client's own reporting needs.
`src/subcluster.py` provides an unsupervised way to find structure inside a broad
bucket for one client, without a hand built taxonomy and without an external model
call: it clusters the turns in that bucket by embedding similarity, with the distance
threshold selected automatically rather than fixed in advance, since the right
threshold varies by client and by dataset. The resulting clusters are genuinely
meaningful, but their automatically generated names are drawn from raw recurring
words rather than written for clarity, so a brief manual review of each cluster is
recommended before using the labels in a client facing report.

### Known limitation

`src/labeling.build_guide` currently assumes the transcript is in Hinglish, which is
accurate for every client onboarded so far. If a client's calls are in a different
language, that assumption needs to become taxonomy aware before labeling.

---

## Security and PII

- All processing is local. No data is sent to any API at runtime.
- `data/test_100/` and `data/audio_transcripts/` contain real customer transcripts and
  should be treated as confidential. Do not share or upload them.
- The HuggingFace token lives at `~/.cache/huggingface/token`. Never echo or commit it.
- Keywords are filtered by corpus frequency and contain no PII by design.
