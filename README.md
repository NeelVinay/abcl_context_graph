# Call Context Graphs

This project does two things with call-center recordings:

1. **Analytics** — an executive flow chart, a keyword and sentiment report, a
   per-turn breakdown, and an intent glossary, for any client. Fully local.
2. **Prompt improvement** — reads a client's call transcripts plus the `.raven`
   prompt their voice agent runs on, and writes back an improved prompt: more
   customer phrasing recognized, more natural delivery, and new lines answering
   things customers repeatedly ask that the prompt had no response for. Every
   change ships with the real evidence behind it.

Both run through **one local LLM backend with no API key required** — it uses
the Claude Code CLI already installed on this machine. Set `ANTHROPIC_API_KEY`
instead and it uses that transparently; nothing else changes.

## Quick start

Three commands, run from this folder:

```bash
./load-transcripts ~/Downloads/your_calls        # pull transcripts in
./load-prompt ~/Downloads/your_prompt.raven       # pull the prompt in
./run-pipeline                                     # graph -> analysis -> OUTPUT/
```

That's the whole workflow. See **[`commands.md`](commands.md)** for the full
reference — what each command does, its flags, and exactly where every file
lands.

## Where things are

```
INPUT/                  Drop your files here.
  transcripts/            call transcripts (.txt or .json)
  prompt/                  the ONE .raven prompt to improve

OUTPUT/                  Always the result of the LATEST ./run-pipeline run.
  Improved_Prompt.raven    <- paste this into NuPlay
  Original_Prompt.raven    what you started with, unchanged
  Changes.diff             before/after, line by line
  Change_Rationale.md      every change, with the evidence behind it
  Run_Log.txt              full log, if something looks off
  Context_Graph/
    Context_Graph.png       the call-flow chart
    Report.md                keywords, sentiment, stage breakdown
    Turns.md                  every call, turn by turn
    Intent_Glossary.md       what each intent means

commands.md              The 3-command reference. Start here for normal use.
DEMO.md                  Talking-points script for walking someone through a run.
load-transcripts          }
load-prompt                } the 3 commands (executable scripts, repo root)
run-pipeline               }

engine/                  Everything else: code, dependencies, internal data.
  README.md                Full technical documentation — client detection,
                            onboarding a new client, the compliance guards,
                            everything below the surface of the 3 commands.
  improve                  Advanced/testing tool — improves an arbitrary prompt
                            file directly, bypassing INPUT/OUTPUT.
  reset                    Wipes a client back to zero (archived, not deleted) —
                            for proving run-pipeline regenerates from scratch.
  src/                      All pipeline logic.
  data/                     Per-client transcript stores, trained models, and
                            (gitignored) run-time caches/logs.
  tests/, scripts/          Test fixtures; eval scripts and retired one-offs.
```

`INPUT/` is never modified by any command; only its contents are gitignored (the
folders themselves persist via `.gitkeep`, so a fresh clone still has somewhere
to drop files). `OUTPUT/` is fully rebuilt on every `./run-pipeline` run — it
never holds a mix of old and new results, and there is only ever one active
client's data in it at a time.

## One-time environment setup

```bash
brew install graphviz          # macOS, rendering engine
# sudo apt install graphviz    # Linux

python3 -m venv .venv
source .venv/bin/activate
pip install -r engine/requirements.txt
```

The first run downloads the embedding models used for classification (roughly
1–2 GB, a few minutes). Subsequent runs are immediate. No `ANTHROPIC_API_KEY`
is required — the pipeline uses the local Claude Code CLI automatically.

## Where data goes

The analytics half runs entirely locally — customer audio and transcripts never
leave the machine. Prompt improvement is different: its evidence pack and
candidate examples include real, verbatim customer speech (call transcripts),
which is why both `INPUT/transcripts/` and the internal `engine/data/` transcript
stores are gitignored rather than committed. See **[`engine/README.md`](engine/README.md#security-and-pii)**
for the full detail on what is and isn't sent anywhere, and the compliance guards
that check every generated line before it can be written.

## More detail

- **[`commands.md`](commands.md)** — the 3-command reference for day-to-day use.
- **[`DEMO.md`](DEMO.md)** — stage-by-stage talking points for walking someone
  through a live run, plus the questions people tend to ask and honest answers.
- **[`engine/README.md`](engine/README.md)** — full technical documentation:
  how a client is detected, onboarding a genuinely new client, how the
  executive chart is built, the compliance guards on generated prompt copy,
  and the lower-level entry points (`run_client.py`, `run_improve.py`, `run.py`)
  the 3 top-level commands call underneath.
