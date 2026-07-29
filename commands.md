# Commands

Three commands. Run them from the repo root.

## 1. Load the transcripts

```
./load-transcripts ~/Downloads/your_calls
```

Pulls every `.txt`/`.json` file from that folder into `INPUT/transcripts/`
(replacing whatever was there), works out which client they belong to, and
registers them. Already have files sitting in `INPUT/transcripts/`? Run it with
no argument to just (re-)register those.

Replaces by default — this project works with one client's data at a time, so a
fresh load is the new active set, not an addition to the old one. Need to add
without replacing? `./load-transcripts --append`.

Does **not** build the context graph or touch the prompt — just gets the
transcripts in. That happens in step 3.

## 2. Load the prompt

```
./load-prompt ~/Downloads/your_prompt.raven
```

Pulls that file into `INPUT/prompt/` (replacing whatever was there), renames it
to something clean once its client is known, and checks: does it parse as valid
`.raven`, can its client be identified, are that client's transcripts already
loaded. Reports readiness — doesn't run any analysis. No argument = re-check
whatever's already in `INPUT/prompt/`.

## 3. Run everything

```
./run-pipeline
```

The real command. Builds the context graph from the loaded transcripts, analyzes
it, and improves the prompt — start to finish, one shot. Writes everything into
`OUTPUT/`, which is fully rebuilt every run.

First run against a new prompt+transcript combination makes live calls to the
local Claude Code CLI (a few minutes, no API key needed). Re-running the same
inputs is near-instant — decisions are cached.

---

## Where things go

```
INPUT/
  transcripts/     <- your loaded call transcripts (.txt or .json)
  prompt/           <- the ONE .raven prompt file

OUTPUT/                          <- always the result of the LATEST run
  Improved_Prompt.raven           <- paste this into NuPlay
  Original_Prompt.raven           what you started with, unchanged
  Changes.diff                    line-by-line before/after
  Change_Rationale.md             every change, with the evidence behind it
  Run_Log.txt                     full log, if something looks off
  Context_Graph/
    Context_Graph.png             the call-flow chart
    Report.md                     keywords, sentiment, stage breakdown
    Turns.md                      every call, turn by turn
    Intent_Glossary.md            what each intent means

engine/                          Everything else — code, dependencies, internal
                                  data. Not part of the normal workflow.
```

Neither `INPUT/` file is ever modified by any of the 3 commands. `OUTPUT/` is
disposable — every `./run-pipeline` run replaces it completely.

## Other tools (not part of the normal workflow)

- **`./engine/reset <client>`** — wipes a client's loaded transcripts, cache, and
  output back to zero (archived first, never deleted) — for proving
  `./run-pipeline` genuinely regenerates everything from scratch.
- **`./engine/improve <path>`** — runs just the improvement stage against an
  arbitrary prompt file, without going through `INPUT/`/`OUTPUT/`. Useful for
  one-off testing.
- **`engine/README.md`** — the full technical documentation: how client detection
  works, onboarding a genuinely new client, the compliance guards, everything.
