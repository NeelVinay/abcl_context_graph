# Demo run-book

Everything runs from one command. No API key — it uses the local Claude Code CLI.
See `COMMANDS.md` for the full command reference; this doc is the talking-points
version for walking someone through it live.

## The command

**VS Code:** `⇧⌘P` → `Tasks: Run Task` → **3. Run pipeline (full run)**

It is also the default build task, so `⇧⌘B` runs it directly.

**Terminal:** `./bin/run-pipeline`

| | time |
|---|---|
| normal run (decisions cached) | **~45 s** |
| `./platform/reset abcl && ./bin/run-pipeline` (forces a genuine from-scratch run) | ~8 min |

Reads `intake/transcripts/` and `intake/prompt/`; neither is ever modified. Writes
everything to `deliverables/`, fully rebuilt each run.

---

## What to say, stage by stage

### Stage 1 — Context graph (225 real ABCL calls)

> "We take the client's raw call transcripts and build a context graph — what
> customers actually say, where calls die, which intents fire."

Open **`deliverables/Context_Graph/Context_Graph.png`** — the call flow with real volumes.

The number that carries the story — **most of the loss is at the very start**:

| stage | calls | fail rate |
|---|---|---|
| the pitch (pre-SMS) | 47 | **68%** |
| SMS sent, link not opened | 27 | 52% |
| link opened | 10 | 50% |
| OTP stage | 55 | 15% |
| deep in the form | 90 | 13% |

**Two-thirds of the calls that die, die during the opening pitch**, before the SMS
is even sent. Get a customer past OTP and failure drops to ~14% — the funnel isn't
leaking, it's collapsing at the opening.

Corpus is 229 ABCL calls: the 225 current transcripts plus a few historical
extractions, scoped to this client only.

**Corpus-hygiene note** (worth knowing, not worth reading aloud in the demo): the
historical-extraction fallback identifies ABCL calls by what they're *not* — not
JustDial, not synthetic — rather than a positive ABCL signature. A stale cache entry
left behind by a deleted duplicate transcript can silently count toward the wrong
client's corpus. This happened once already: 52 Myntra calls were briefly counted as
ABCL "historical" calls, and the model caught it unprompted in its own rationale
("delivery/shipping complaints from an unrelated vertical leaking into this
corpus"), correctly excluding that content. It's fixed now — if a future run's
evidence pack ever mentions an off-topic theme, that self-report is the tell; check
`CHANGES-*.md` before trusting the numbers.

### Stage 2 — The LLM reads the graph and rewrites the prompt

> "The graph becomes an evidence pack. The model gets the evidence and the current
> prompt, and decides what to change. Three kinds of change."

| | what it does |
|---|---|
| **Recognition phrases** (3) | The agent *understands* more of what callers say — those turns now route to the right handler instead of the generic default |
| **Conversational delivery** (29) | Real caller particles (`जी`) added as lead-ins so it stops sounding scripted. Scripted wording unchanged |
| **New agent speech** (4) | Answers to things callers repeatedly say that the prompt had **no response for at all** |

### Stage 3 — Before / after

The script prints the diff. Full patch at `deliverables/Changes.diff`.

### Stage 4 — The reasoning

Open **`deliverables/Change_Rationale.md`**. This is the piece worth dwelling on —
every change carries its evidence. The strongest example:

> **New line in `handle_security_concern()`**
> "यह कोई fraud नहीं है — Aditya Birla Capital एक RBI-registered NBFC है…"
>
> **Why:** `trust_or_fraud` appears in 7 calls, and customers use the exact word
> *fraud* three separate times — but the state only mentioned https/domain and never
> mirrored that word.

---

## The two things that make it defensible

**1. It refuses more than it accepts.** 32 proposals were blocked automatically —
see *Rejected by safety checks* at the end of `deliverables/Change_Rationale.md`. Nothing there
reached the prompt. The compliance guard rejects any generated line containing a
digit, `%`, `₹`, or a rate/amount/timeline claim, because that is the
regulated-lending boundary and it is enforced in code, not trusted to the model.

**2. It doesn't fall for correlations.** The rate/fee objection *looks* like the
big loss driver — 58 of 229 calls. But customers who raise it actually complete
**better** than baseline (22.7% incomplete vs 31.4%). The evidence pack states that
outright, and the model correctly wrote the line as "most-asked question" rather
than "retention fix" — its own words in the rationale. Same for `network`, which
correlates weakly and non-significantly (Fisher p=0.08).

---

## Questions you'll probably get

**"Is a model really making these decisions, or is it rules?"**
Both, deliberately. Mining candidates is mechanical and cheap. Judging them is the
model. Show `platform/data/clients/abcl/prompts_sent/` — the fully rendered prompts *and*
responses are on disk. `llm_calls.jsonl` logs every call with token counts. If they
want to see it live: `./platform/reset abcl && ./bin/run-pipeline` forces every decision to be
a fresh model call instead of a cache hit.

**"What does it cost?"**
11 model calls per full run, ~448K in / 52K out tokens. Re-runs are free — responses
cache on the prompt hash, which also makes runs idempotent rather than a fresh roll
of the dice.

**"Can it break the prompt?"**
A structural verifier gates the write: braces balanced, no dangling routes, new
intents fully wired, token budget, and existing `say()` lines preserved. If it
fails, nothing is written. A timestamped `.bak` is taken first regardless.

**"Does this work for other clients?"**
The graph stage does, today — `myntra` (52 calls) and `justdial` (115) are already
onboarded internally, and an unknown client routes through a shared broad taxonomy
with nothing hand-built first. The improver stage needs that client's own `.raven`
prompt, which only ABCL has so far: drop their transcripts into
`intake/transcripts/` and their prompt into `intake/prompt/`, then `./bin/run-pipeline` —
the client is auto-detected from what's actually in there. This project works with
one client's data at a time, so loading a different client's transcripts replaces
whatever was loaded before, not adds to it.

---

## Own these up front

Better to raise them than be caught by them.

- **Corpus is small for some intents.** Several anchor buckets hold only 3–4 calls
  and get rejected at validation. Accuracy here is limited by transcript volume, not
  by the method — which is why the jump from 113 to 225 transcripts changed the
  pre-SMS failure rate from 70% to 38%. Early numbers on this data move a lot; quote
  the direction, not the decimal.
- **No call timestamps.** Records carry only `call_id / language / outcome / turns`,
  so anything seasonal or time-of-day can't be gated on yet. The evidence pack says
  this explicitly so the model doesn't invent a pattern the data can't support.
- **One institutional claim needs a human sign-off.** The fraud line asserts
  "RBI-registered NBFC". True, but it is a *regulatory* claim, and the compliance
  guard only screens rates/amounts/timelines — not institutional statements. Legal
  should approve that specific sentence. This is a real gap in the guard, and worth
  naming as the next thing to close.
- **One pre-existing bug is reported, not fixed:** `global` routes
  `intent("silence")` to `silence_check()`, which doesn't exist in the prompt. The
  verifier flags it and deliberately leaves it alone — the improver doesn't silently
  repair things it wasn't asked to touch.
