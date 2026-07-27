# Call Context Graphs

This project turns call center recordings into visual analytics: an executive flow
chart, a keyword and sentiment report, a per-turn breakdown, and an intent glossary,
for any client. The pipeline runs entirely locally. Customer audio and transcripts
never leave the machine, and the only component that ever touches an external model
is an offline labeling step used when onboarding a new client, which never runs in
production.

## Quick start

```bash
python run_client.py <folder of transcripts>
```

That is the whole interface for normal use. Point it at a folder of transcripts and
it will:

1. Detect which client the calls belong to, either from the filenames or from the
   content of the calls themselves.
2. Use that client's own taxonomy and trained model if one exists (currently ABCL,
   JustDial, and Myntra), or fall back to a shared, broad taxonomy if the client is
   new.
3. Write everything to a single folder: `data/output/<client>_output/`.

Running it again for the same client regenerates that same folder. By default, the
transcripts given are treated as that client's full, current set and replace
whatever was there before. Pass `--append` to add the new transcripts to the
client's existing set instead of replacing it.

```bash
python run_client.py data/clients/abcl/transcripts               # regenerate ABCL's output
python run_client.py ~/Downloads/new_client_batch --client acme   # force a client name
python run_client.py ~/Downloads/more_myntra_calls --client myntra --append
```

### One time environment setup

```bash
brew install graphviz          # macOS, rendering engine
# sudo apt install graphviz    # Linux

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The first run downloads the embedding models used for classification (roughly 1 to
2 GB combined, a few minutes). Subsequent runs are immediate.

---

## What you get

Each run writes four files into `data/output/<client>_output/`:

- `<client>_exec.png`: the executive flow chart. A title banner, right angle
  routing, colored terminal nodes by outcome, and a bold green line through the
  single most common journey. For ABCL this follows its hand authored procedure
  skeleton; for every other client it is built directly from the data.
- `report.md`: keywords, sentiment, and tool calls, grouped by intent.
- `turns.md`: every turn of every call, with its intent, sentiment, tool, and
  keywords.
- `intents.md`: a glossary of the intents present in that run, with descriptions and
  counts.

---

## Repository layout

```
run_client.py       The one command described above.
run.py               Lower level entry point behind it (see "Advanced usage").
run_transcribe.py    Transcribe raw .mp3 recordings into plain text (optional).
config.py            Paths and pipeline settings.

src/                 All pipeline logic.
  clients.py            Client registry and detection. Start here to see what
                         defines a client, or to add one directly instead of
                         relying on auto-detection.
  extract.py             Per-call extraction: parses a transcript, classifies
                          each turn, and produces the structured call record.
  distill.py              Trains and runs the local classifiers.
  generic_taxonomy.py     The broad, client-agnostic taxonomy used by clients
                           with no fine-grained taxonomy of their own.
  generic_bootstrap.py    Builds the shared "generic" gold set from existing
                           client data at no extra labeling cost.
  flowtree.py             Builds the flow tree and the reconverging stage graph
                           used for the executive chart.
  visualize.py            Renders both chart styles.
  sop_flow.py             ABCL's fixed, hand authored procedure skeleton.
  ...                     see individual file docstrings for the rest.

scripts/
  eval/                Scripts that measure the generic pipeline's accuracy,
                        including honest held out, cross client tests.
  legacy/               Retired one off scripts and the pre run_client.py entry
                        points, kept for reference.

data/
  clients/<name>/transcripts/   The current, persistent transcript set for each
                                 client. This is what run_client.py reads from
                                 and writes to.
  cache/                Cached per-call extractions, shared across clients and
                        keyed by call ID.
  gold*/                Labeling workspaces: batches to label, labeled batches,
                        and the assembled gold label files.
  models/               Trained classifiers.
  output/<name>_output/ Where each client's four output files land.
  archive/              Superseded data kept for provenance only. Not part of
                        the active pipeline. See "What moved to archive" below.
```

---

## Known clients

| Client | Detected by | Taxonomy | Model |
|---|---|---|---|
| ABCL | content signature ("Aditya Birla Capital", "Priya") | its own, fine grained | `data/models/intent_clf.pkl` |
| JustDial | filename prefix `LCS-` | its own, fine grained | `data/models/justdial_clf.pkl` |
| Myntra | content signature ("मिंत्रा", "मीरा") | shared broad taxonomy | `data/models/generic_clf.pkl` |

ABCL is the only client with a hand authored procedure skeleton (`src/sop_flow.py`),
since it is the only call flow that has been mapped out step by step. Every other
client, known or new, gets its executive chart built directly from the data (see
"How the executive chart works" below).

Adding a new known client, so it is recognized automatically instead of needing
`--client` every time, means adding one entry to `src/clients.py`. See that file's
docstring.

---

## Generalizing to a new client

A client with no taxonomy of its own is not blocked. It is automatically routed
through `generic_taxonomy.py`, a small set of broad, client agnostic buckets:
greeting, agree, disagree, ask_question, answer_query, confused_repeat,
callback_request, person_unavailable, distrust_security, irate_frustrated,
wait_hold, acknowledge, end_call, and a fallback `other`.

There is a precedent in this repository for broad categories outperforming fine
ones: `src/justdial_coarse.py` collapsed JustDial's 24 intent taxonomy down to about
seven buckets after the fine grained model scored only about 32 percent
cross-validation accuracy on noisy speech-to-text output. The generic taxonomy
applies that same lesson from the outset, across clients rather than within one.

Claude is used only offline, to help generate training labels when a client needs
better accuracy than the shared model alone provides. It is never part of the
production or inference path. The model that actually classifies calls is always
the local scikit-learn classifier in `data/models/`.

### Embedding model

The generic domain uses `intfloat/multilingual-e5-base`, rather than the smaller
`paraphrase-multilingual-MiniLM-L12-v2` used by ABCL and JustDial's own models. In a
controlled comparison, this measurably improved cross-domain accuracy, by six to
nine points, with no other change. Text encoded with this model must be prefixed
with `"query: "` for both training and inference; `src/distill.embed_prefix_for`
handles this automatically, and the prefix is stored alongside the trained model so
inference always matches training.

### Bootstrapping a shared model without new labeling

Before any new client is added, the shared gold set is bootstrapped from data that
already exists, at no additional labeling cost (`src/generic_bootstrap.py`):

- Existing ABCL and JustDial gold labels are recoded into the broad buckets
  wherever a clean, honest mapping exists. Fine grained, client specific intents,
  such as a PAN card entry step, are left out rather than forced into an unrelated
  bucket.
- The `irate_frustrated` bucket has no equivalent fine intent in either source
  taxonomy. It is derived directly from the existing sentiment field instead, since
  frustration was already being captured there.
- A small number of hand verified real examples fill in buckets that otherwise have
  sparse coverage, such as `disagree` and `callback_request`.

### Onboarding a genuinely new client

1. Collect transcripts, plain text with `Agent:` / `Customer:` prefixes, or the JSON
   turn format `src/transcribe.py` also produces. No new taxonomy or code is
   required.
2. Run `python run_client.py <folder>`. If the client is not recognized, it is
   assigned a slug from the folder name (or from `--client`), given its own
   persistent transcript store under `data/clients/<slug>/`, and processed through
   the shared generic taxonomy immediately. This alone already produces a usable,
   if imperfect, output folder.
3. If accuracy for this client needs to improve, label a batch of its own
   transcripts and fold that into the shared model:

```bash
python -m src.labeling emit generic
# label each data/gold_generic/_tolabel/batch_*.json offline, following
# data/gold_generic/LABELING_GUIDE.md, and write results to _labeled/
python -m src.labeling assemble generic
python -m src.distill eval generic     # honest accuracy check, see below
python -m src.distill train generic
```

`src.labeling.assemble` merges new labels into the existing gold file rather than
overwriting it, so labeling one client never discards another client's data.

### How well this actually generalizes

A mixed cross-validation number across all onboarded clients overstates how well
the model will do on a client it has never seen, since the model can partly learn
to recognize which client it is looking at rather than the underlying intent. The
honest test holds one client's calls out entirely, trains on the rest, and scores
only against the held out client. The scripts in `scripts/eval/` do exactly this.

Measured this way, across ABCL, JustDial, and Myntra: a client with no data of its
own in training scores roughly 28 to 48 percent accuracy, depending on how
different its calls are from the others already in the model. Once even a modest
amount of that client's own real, labeled data is added, accuracy for that client
rises to roughly 68 to 71 percent. Both figures come from held out evaluation, not
from training and testing on the same pool.

The practical implication: a shared taxonomy and pipeline remove the need to design
a new taxonomy for each client, but they do not remove the need for some real,
labeled data from that client before the model is reliable on it.

### How the executive chart works for a client with no fixed skeleton

`src/flowtree.build_stage_dag` builds a directed graph over the same small set of
coarse stages used elsewhere in the pipeline, but calls that pass through the same
stage share a single node rather than each forking into its own branch. This lets
different call journeys reconverge, which is what gives the chart its compact,
structured appearance without a hand authored skeleton behind it.
`src/visualize.visualize_exec` renders that graph in the same visual style as ABCL's
chart: a title banner, right angle routing, colored terminal nodes by outcome, and a
bold green main path.

### Sharpening a broad bucket for one client

A bucket like `ask_question` is deliberately generic so it works across clients,
but it can be too coarse for a single client's own reporting needs.
`src/subcluster.py` finds structure inside a broad bucket for one client without a
hand built taxonomy and without an external model call: it clusters the turns in
that bucket by embedding similarity, with the distance threshold chosen
automatically rather than fixed in advance, since the right threshold varies by
client and by dataset. The resulting clusters are genuinely meaningful, but their
automatically generated names are drawn from raw recurring words rather than
written for clarity, so a brief manual review of each cluster is recommended before
using the labels in a client facing report.

### Known limitation

`src/labeling.build_guide` currently assumes the transcript is in Hinglish, which is
accurate for every client onboarded so far. If a client's calls are in a different
language, that assumption needs to become taxonomy aware before labeling.

---

## Advanced usage

`run_client.py` covers normal use. For finer control, `run.py` is the pipeline it
runs underneath, and can be called directly:

```bash
# ABCL's fixed procedure skeleton, C-suite view
python run.py --all --src data/clients/abcl/transcripts --out data/output/abcl_output --graph sop-exec

# Full detailed skeleton, including zero-count branches
python run.py --all --src data/clients/abcl/transcripts --out data/output/abcl_output --graph sop

# Data-driven flow tree instead of the executive chart
python run.py --all --src data/clients/justdial/transcripts --out data/output/justdial_output --graph flow

# Process graph (directly-follows graph)
python run.py --all --src data/clients/abcl/transcripts --out data/output/abcl_output --graph dfg

# Demo on synthetic data, no real transcripts needed
python run.py --mock
python run.py --taxonomy
```

Flags: `--min-count N`, `--top-k N`, `--shape {ellipse,box,circle}`,
`--words-on-graph`.

`scripts/legacy/` holds the pre `run_client.py` entry points
(`make_flowchart.py`, `make_graph.py`, `pipeline.py`) and a handful of older, one off
debugging scripts. They still run, via `python -m scripts.legacy.<name>`, but are not
the documented workflow.

---

## Transcribing new audio (optional)

Only needed when starting from `.mp3` recordings rather than existing transcripts.

```bash
brew install ffmpeg             # macOS
# sudo apt install ffmpeg       # Linux

huggingface-cli login          # paste a free read token, answer 'n' to git-credential
```

While logged in, accept the terms once for `pyannote/speaker-diarization-3.1` and
`pyannote/segmentation-3.0`. The first transcription run downloads roughly 3 to 4 GB
of models (Whisper large-v3, pyannote, and the aligner).

```bash
python run_transcribe.py --limit 100
# Reads .mp3 from ~/Downloads/leads_mp3_data
# Writes Agent:/Customer: plain text to data/clients/justdial/transcripts/<id>.txt
# Resumable: re-running skips files already done. Use --overwrite to redo them.
```

Transcription is CPU bound on Apple Silicon, at roughly two to three times real
time. Keep the machine awake and plugged in for a large batch; the run is resumable
if interrupted.

---

## What moved to archive

`data/archive/` holds data that is no longer part of the active pipeline, kept only
for provenance:

- `test_100/`: an earlier, separate 116 call ABCL sample used for an early demo
  chart. It does not overlap with the 113 calls that actually back the current
  ABCL model (`data/clients/abcl/transcripts/`, matched against `data/gold/`) and is
  not used by anything today.
- `output/`: output folders from before the unified `<client>_output/` convention
  (`original`, `txt`, `mp3`, `test_100_sop`, `test_100_sop_v2`, `generic_raw`).
  Their content has been regenerated into `data/output/abcl_output/`,
  `data/output/justdial_output/`, and `data/output/myntra_output/`.

Nothing here is deleted; it is moved out of the way of normal browsing. Git history
also has the original locations if needed.

---

## Security and PII

- All processing is local. No data is sent to any API at runtime.
- `data/clients/*/transcripts/` contain real customer transcripts and should be
  treated as confidential. Do not share or upload them.
- The HuggingFace token lives at `~/.cache/huggingface/token`. Never echo or commit
  it.
- Keywords are filtered by corpus frequency and contain no PII by design.
