#!/usr/bin/env bash
#
# End-to-end demo: raw call transcripts -> context graph -> improved .raven prompt.
#
#   ./scripts/demo_e2e.sh                 # abcl, the pristine colleague prompt
#   CLIENT=myntra ./scripts/demo_e2e.sh   # another client
#   PROMPT=path/to/x.raven ./scripts/demo_e2e.sh
#
# The LLM backend is resolved by src/llm.py: an ANTHROPIC_API_KEY if one is set,
# otherwise the local `claude` CLI, which uses this machine's existing Claude Code
# session. No key is required.
#
# The input prompt is NEVER modified — it is copied into a demo working directory
# first, and the improver runs on the copy. Re-running is therefore safe and
# repeatable, which is the whole point when you are running it in front of someone.

set -euo pipefail

cd "$(dirname "$0")/.."
REPO="$PWD"

CLIENT="${CLIENT:-abcl}"
PROMPT="${PROMPT:-data/clients/$CLIENT/autorun/input.raven}"
RUN_DIR="data/clients/$CLIENT/demo"
GRAPH_DIR="data/output/${CLIENT}_output"
LOG_DIR="$RUN_DIR/logs"

BOLD=$'\033[1m'; CYAN=$'\033[1;36m'; GREEN=$'\033[1;32m'
RED=$'\033[1;31m'; DIM=$'\033[2m'; OFF=$'\033[0m'

step()  { printf '\n%s━━━ %s ━━━%s\n' "$CYAN" "$1" "$OFF"; }
info()  { printf '   %s\n' "$1"; }
ok()    { printf '   %s✓%s %s\n' "$GREEN" "$OFF" "$1"; }
die()   { printf '\n   %s✗ %s%s\n\n' "$RED" "$1" "$OFF" >&2; exit 1; }

# Known-harmless numeric warnings from sklearn/graphviz. Filtered from the screen
# so the demo reads clean, but every line still lands in the stage log — nothing is
# actually discarded.
NOISE='RuntimeWarning|ret = a @ b|Orthogonal edges do not currently handle|NotOpenSSLWarning|warnings\.warn|^ *$'

mkdir -p "$RUN_DIR" "$LOG_DIR"

# ---------------------------------------------------------------- 0. preflight
step "0/4  Preflight"

[ -d .venv ] && { . .venv/bin/activate; ok "venv activated ($(python3 --version 2>&1))"; } \
             || info "no .venv — using system python3 ($(python3 --version 2>&1))"

[ -f "$PROMPT" ] || die "input prompt not found: $PROMPT"
ok "input prompt: $PROMPT ($(wc -l < "$PROMPT" | tr -d ' ') lines)"

N_TRANSCRIPTS=$(find "data/clients/$CLIENT/transcripts" -type f \( -name '*.txt' -o -name '*.json' \) 2>/dev/null | wc -l | tr -d ' ')
[ "$N_TRANSCRIPTS" -gt 0 ] || die "no transcripts in data/clients/$CLIENT/transcripts"
ok "transcripts: $N_TRANSCRIPTS"

PROVIDER=$(python3 -c 'from src import llm; print(llm.resolve_provider())') \
  || die "no LLM backend: set ANTHROPIC_API_KEY, or install Claude Code so \`claude\` is on PATH"
ok "LLM backend: $PROVIDER"

# ------------------------------------------------------- 1. build context graph
GRAPH_JSON="$GRAPH_DIR/report.md"
if [ "${SKIP_GRAPH:-0}" = "1" ] && [ -f "$GRAPH_JSON" ]; then
  step "1/4  Context graph  (SKIP_GRAPH=1 — reusing the existing graph)"
  info "already built from $N_TRANSCRIPTS transcripts: $GRAPH_DIR"
  info "${DIM}the transcripts have not changed, so neither has the graph${OFF}"
else
  step "1/4  Context graph  ($N_TRANSCRIPTS transcripts -> flow chart + report)"
  info "${DIM}python run_client.py data/clients/$CLIENT/transcripts --client $CLIENT${OFF}"

  set +e
  python run_client.py "data/clients/$CLIENT/transcripts" --client "$CLIENT" \
    > "$LOG_DIR/1-graph.log" 2>&1
  rc=$?
  set -e
  grep -vE "$NOISE" "$LOG_DIR/1-graph.log" | sed 's/^/   /' || true
  [ $rc -eq 0 ] || die "graph build failed — see $LOG_DIR/1-graph.log"
fi

# --------------------------------------------------- 2. autonomous improvement
step "2/4  Prompt improvement  (LLM decides; runs on a COPY of the input)"

# Mark where the call log ends, so stage 4 can report THIS run's usage rather than
# every call ever made for this client — otherwise a cached run claims live calls.
CALL_LOG="data/clients/$CLIENT/llm_calls.jsonl"
LOG_OFFSET=0
[ -f "$CALL_LOG" ] && LOG_OFFSET=$(wc -l < "$CALL_LOG" | tr -d ' ')

# DEMO_FRESH=1 parks the response cache so every decision is a real model call.
# Use it if someone asks whether a model is genuinely in the loop. Costs ~7 minutes
# instead of ~10 seconds; the cache is restored on exit either way.
CACHE="data/clients/$CLIENT/llm_cache.json"
restore_cache() {
  [ -f "$CACHE.parked" ] || return 0
  # Merge rather than move back: the fresh run just paid for new entries, and
  # clobbering them would make the next demo slow again for no reason.
  python3 - "$CACHE" "$CACHE.parked" <<'PY'
import json, pathlib, sys
cur, parked = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
old = json.loads(parked.read_text()) if parked.stat().st_size else {}
new = json.loads(cur.read_text()) if cur.exists() and cur.stat().st_size else {}
cur.write_text(json.dumps({**old, **new}, indent=2, ensure_ascii=False))
PY
  rm -f "$CACHE.parked"
}
if [ "${DEMO_FRESH:-0}" = "1" ] && [ -f "$CACHE" ]; then
  mv "$CACHE" "$CACHE.parked"
  trap restore_cache EXIT
  info "DEMO_FRESH=1 — cache parked, every decision will be a live model call"
fi

cp "$PROMPT" "$RUN_DIR/before.raven"
cp "$PROMPT" "$RUN_DIR/demo.raven"
ok "pristine input copied — $PROMPT is not touched by this run"
info "${DIM}python run_improve.py $RUN_DIR/demo.raven --client $CLIENT --auto${OFF}"
info "${DIM}(first run calls the model and may take a few minutes; re-runs hit the cache)${OFF}"

set +e
python run_improve.py "$RUN_DIR/demo.raven" --client "$CLIENT" --auto \
  2>&1 | tee "$LOG_DIR/2-improve.log"
rc=${PIPESTATUS[0]}
set -e
[ $rc -eq 0 ] || die "improvement failed — see $LOG_DIR/2-improve.log"

# ------------------------------------------------------------ 3. before / after
step "3/4  What changed"

diff -u "$RUN_DIR/before.raven" "$RUN_DIR/demo.raven" > "$RUN_DIR/diff.patch" || true
ADDED=$(grep -c '^+[^+]' "$RUN_DIR/diff.patch" || true)
REMOVED=$(grep -c '^-[^-]' "$RUN_DIR/diff.patch" || true)

if [ "${ADDED:-0}" -eq 0 ] && [ "${REMOVED:-0}" -eq 0 ]; then
  info "no changes were applied — every candidate was rejected by the self-checks."
  info "that is a real outcome, not a failure. See the CHANGES file for why."
else
  ok "$ADDED line(s) added, $REMOVED changed/removed"
  printf '\n%s   ── first 40 diff lines (full patch: %s) ──%s\n' "$DIM" "$RUN_DIR/diff.patch" "$OFF"
  sed -n '4,44p' "$RUN_DIR/diff.patch" | sed 's/^/   /'
fi

# -------------------------------------------------------------- 4. the artifacts
step "4/4  Artifacts"

CHANGES="data/clients/$CLIENT/CHANGES-demo.md"
python3 - "$CALL_LOG" "$LOG_OFFSET" <<'PY'
import json, pathlib, sys
log, offset = pathlib.Path(sys.argv[1]), int(sys.argv[2])
rows = []
if log.exists():
    for line in log.read_text().splitlines()[offset:]:
        try:
            rows.append(json.loads(line))
        except Exception:
            pass
live = [r for r in rows if not r.get("cached")]
cached = len(rows) - len(live)
provs = sorted({r.get("provider", "api") for r in live})
tin = sum(r.get("in_tokens", 0) for r in live)
tout = sum(r.get("out_tokens", 0) for r in live)
where = f"  [{', '.join(provs)}]" if provs else ""
print(f"   LLM this run: {len(live)} live call(s), {cached} cache hit(s){where}")
if live:
    print(f"                 {tin:,} in / {tout:,} out tokens")
else:
    print("                 cached run — zero model calls, identical decisions")
PY

echo
info "${BOLD}Context graph${OFF}"
for f in "$GRAPH_DIR/${CLIENT}_exec.png" "$GRAPH_DIR/report.md" \
         "$GRAPH_DIR/turns.md" "$GRAPH_DIR/intents.md"; do
  [ -f "$f" ] && info "  $f"
done
echo
info "${BOLD}Prompt improvement${OFF}"
for f in "$RUN_DIR/before.raven" "$RUN_DIR/demo.raven" "$RUN_DIR/diff.patch" \
         "$CHANGES" "data/clients/$CLIENT/prompts_sent"; do
  [ -e "$f" ] && info "  $f"
done

printf '\n%s   Done.%s  Open the chart and the diff side by side:\n' "$GREEN" "$OFF"
printf '     open %s\n' "$GRAPH_DIR/${CLIENT}_exec.png"
printf '     open %s\n\n' "$CHANGES"

if [ "${DEMO_OPEN:-1}" = "1" ] && command -v open >/dev/null 2>&1; then
  [ -f "$GRAPH_DIR/${CLIENT}_exec.png" ] && open "$GRAPH_DIR/${CLIENT}_exec.png" || true
  [ -f "$CHANGES" ] && open "$CHANGES" || true
fi
