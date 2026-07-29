"""Thin, cached, logged Anthropic client — the ONLY place this project talks to an
LLM. Everything else in the improvement pipeline stays deterministic.

Design constraints, all deliberate:

  * **Never silently degrades.** No usable backend -> raises. A heuristic fallback
    that fakes a judgment call is worse than a hard failure, because the output
    looks identical either way and gets written into a production prompt. "Usable
    backend" means an API key *or* a local Claude Code CLI (see PROVIDER_ENV); what
    is never allowed is inventing a decision with no model in the loop.
  * **Cached on the prompt hash.** Re-running the improver costs nothing and
    produces identical decisions, which is what makes an autonomous run
    idempotent rather than a fresh roll of the dice each time.
  * **Every call logged** to llm_calls.jsonl with purpose + token counts, so
    "how sparingly are we actually using this" is answerable with a number
    instead of an impression.
  * **Strict JSON, one retry.** A malformed response is retried once with the
    parse error fed back; if it fails again the batch is DROPPED and logged, not
    guessed at. Guessing here means fabricated prompt edits.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import time
from pathlib import Path

import config

MODEL = "claude-sonnet-5"
_MAX_RETRIES = 1

# Which backend actually answers.
#   "api"        — the Anthropic SDK, needs ANTHROPIC_API_KEY.
#   "claude-cli" — shells out to the locally-installed Claude Code binary, which
#                  authenticates through the user's existing session. No key needed.
#   "auto"       — prefer the key if one is set, else the CLI. This is what lets the
#                  pipeline run end-to-end on a machine that has never had a key,
#                  instead of hard-failing at the first decision point.
PROVIDER_ENV = "ABCL_LLM_PROVIDER"
_CLI = "claude"
_CLI_TIMEOUT_S = 300


class LLMUnavailable(RuntimeError):
    """No API key, or the SDK isn't installed. Deliberately fatal — see module docstring."""


class LLMBadResponse(RuntimeError):
    """Model returned something unparseable twice running. The caller drops that batch."""


class LLMAuthError(LLMUnavailable):
    """Key is present but rejected — typo'd, revoked, or wrong environment.
    Subclasses LLMUnavailable so the CLI's existing handler catches it and prints
    setup guidance rather than a stack trace."""


def _client():
    try:
        import anthropic
    except ImportError as e:  # noqa: BLE001
        raise LLMUnavailable(
            "the `anthropic` package is not installed — `pip install anthropic`") from e
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        raise LLMUnavailable(
            "ANTHROPIC_API_KEY is not set. This pipeline will not fall back to a "
            "heuristic: a fake judgment that looks like a real one is worse than "
            "no run at all.")
    return anthropic.Anthropic(api_key=key)


def resolve_provider() -> str:
    """Decide which backend answers, and fail loudly if neither is available."""
    p = (os.environ.get(PROVIDER_ENV) or "auto").strip().lower()
    if p not in ("auto", "api", "claude-cli"):
        raise LLMUnavailable(
            f"{PROVIDER_ENV}={p!r} is not a known provider "
            f"(expected 'auto', 'api', or 'claude-cli')")
    if p == "api":
        return "api"
    if p == "claude-cli":
        if not shutil.which(_CLI):
            raise LLMUnavailable(
                f"{PROVIDER_ENV}=claude-cli but the `{_CLI}` binary is not on PATH")
        return "claude-cli"
    if os.environ.get("ANTHROPIC_API_KEY"):
        return "api"
    if shutil.which(_CLI):
        return "claude-cli"
    raise LLMUnavailable(
        "no LLM backend available: ANTHROPIC_API_KEY is unset and the `claude` CLI "
        "is not on PATH. Install Claude Code or set a key — this pipeline will not "
        "fall back to a heuristic, because a fake judgment that looks like a real "
        "one is worse than no run at all.")


def _ask_claude_cli(prompt: str) -> tuple[str, int, int]:
    """One-shot the local Claude Code binary in print mode. Returns (text, in, out).

    Run from an empty temp directory on purpose: `claude` picks up CLAUDE.md from
    its working directory, and this repo's own instructions have no business
    leaking into a prompt that asks the model to judge customer speech.

    Tools are denied and the turn count capped rather than the agent being told to
    behave: this must be a completion, not an agent that can read the filesystem.
    The cap is NOT 1 — verified that a 25KB evidence prompt legitimately reports
    num_turns=3, so `--max-turns 1` fails every large call with error_max_turns
    while small ones pass, which reads exactly like a flaky model instead of a
    misconfigured flag.
    """
    exe = shutil.which(_CLI)
    if not exe:
        raise LLMUnavailable(f"the `{_CLI}` binary is not on PATH")
    cmd = [exe, "-p", "--model", MODEL, "--output-format", "json",
           "--max-turns", "8",
           "--disallowed-tools", "Bash", "Edit", "Write", "Read",
           "WebFetch", "WebSearch"]
    with tempfile.TemporaryDirectory() as neutral_cwd:
        try:
            proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                                  cwd=neutral_cwd, timeout=_CLI_TIMEOUT_S)
        except subprocess.TimeoutExpired as e:
            raise LLMBadResponse(
                f"`{_CLI}` did not answer within {_CLI_TIMEOUT_S}s") from e
    if proc.returncode != 0:
        tail = (proc.stderr or proc.stdout or "").strip()[-400:]
        # A CLI that is installed but not logged in fails here. That is an auth
        # problem, not a bad response, so it must not be retried.
        if "login" in tail.lower() or "authenticat" in tail.lower():
            raise LLMAuthError(f"`{_CLI}` is not authenticated — run `{_CLI}` once "
                               f"interactively to log in. ({tail})")
        raise LLMUnavailable(f"`{_CLI}` exited {proc.returncode}: {tail}")
    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise LLMBadResponse(
            f"`{_CLI}` did not emit JSON envelope: {proc.stdout[:200]!r}") from e
    if payload.get("is_error"):
        raise LLMBadResponse(f"`{_CLI}` reported an error: "
                             f"{str(payload.get('result'))[:300]}")
    text = payload.get("result")
    if not isinstance(text, str) or not text.strip():
        raise LLMBadResponse(f"`{_CLI}` returned an empty result field")
    usage = payload.get("usage") or {}
    # Report the billed input honestly: the CLI carries its own system prompt, and
    # most of that arrives as cache reads rather than fresh input tokens.
    in_tok = (usage.get("input_tokens", 0)
              + usage.get("cache_read_input_tokens", 0)
              + usage.get("cache_creation_input_tokens", 0))
    return text, in_tok, usage.get("output_tokens", 0)


def _cache_path(client_key: str) -> Path:
    return config.CLIENTS_DIR / client_key / "llm_cache.json"


def _log_path(client_key: str) -> Path:
    return config.CLIENTS_DIR / client_key / "llm_calls.jsonl"


def _load_cache(client_key: str) -> dict:
    p = _cache_path(client_key)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text())
    except Exception:  # noqa: BLE001
        return {}


def _save_cache(client_key: str, cache: dict) -> None:
    """Atomic write. A plain write_text can be interrupted mid-flush, and
    _load_cache treats an unparseable file as EMPTY — silently turning every
    previously-cached decision back into a paid API call with no warning.
    Temp-file + os.replace makes the swap all-or-nothing."""
    import os
    import tempfile
    p = _cache_path(client_key)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as fh:
            json.dump(cache, fh, indent=2, ensure_ascii=False)
        os.replace(tmp, p)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


def _prompts_dir(client_key: str) -> Path:
    return config.CLIENTS_DIR / client_key / "prompts_sent"


def _save_prompt(client_key: str, purpose: str, h: str, prompt: str,
                 response: str | None = None) -> Path:
    """Write the fully-rendered prompt (and the response) to disk.

    Only the sha1 was recorded before, which made the single most important thing
    about this pipeline unauditable: these prompts carry ~97 verbatim customer
    turns with their call IDs, and there was no way to review what had actually
    been sent. Written on every call, cached or live.

    Contains real customer speech, so it is gitignored — same treatment as
    data/clients/*/transcripts/."""
    p = _prompts_dir(client_key)
    p.mkdir(parents=True, exist_ok=True)
    f = p / f"{purpose}-{h[:10]}.txt"
    body = prompt
    if response is not None:
        body += ("\n\n" + "=" * 70 + "\nRESPONSE\n" + "=" * 70 + "\n" + response)
    f.write_text(body)
    return f


def _log(client_key: str, record: dict) -> None:
    p = _log_path(client_key)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def _extract_json(text: str):
    """Models like to wrap JSON in prose or a ```json fence. Pull out the first
    balanced {...} or [...] block rather than requiring a bare document."""
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
        text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    for opener, closer in (("{", "}"), ("[", "]")):
        start = text.find(opener)
        if start == -1:
            continue
        depth = 0
        in_str = False
        esc = False
        for i in range(start, len(text)):
            ch = text[i]
            if esc:
                esc = False
                continue
            if ch == "\\":
                esc = True
                continue
            if ch == '"':
                in_str = not in_str
                continue
            if in_str:
                continue
            if ch == opener:
                depth += 1
            elif ch == closer:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(text[start:i + 1])
                    except json.JSONDecodeError:
                        break
    raise LLMBadResponse(f"no parseable JSON in response: {text[:200]!r}")


def ask_json(prompt: str, client_key: str, purpose: str,
             *, max_tokens: int = 4000, use_cache: bool = True,
             expect: type = dict):
    """Send `prompt`, expect JSON back. Returns the parsed object.

    Raises LLMUnavailable (no key/SDK) or LLMBadResponse (unparseable twice).
    Callers treat LLMBadResponse as "drop this batch", never as "assume a default"."""
    h = hashlib.sha1(prompt.encode("utf-8")).hexdigest()
    cache = _load_cache(client_key) if use_cache else {}
    if use_cache and h in cache:
        cached = cache[h]
        # A cache written before the shape check existed, hand-edited, or
        # half-written by a crash can hold the wrong type. Treat it as a miss
        # rather than handing a caller something it will crash on.
        if isinstance(cached, expect):
            _save_prompt(client_key, purpose, h, prompt,
                         json.dumps(cached, ensure_ascii=False, indent=1))
            _log(client_key, {"ts": time.time(), "purpose": purpose, "hash": h,
                              "cached": True})
            return cached

    provider = resolve_provider()
    client = _client() if provider == "api" else None
    attempt_prompt = prompt
    last_err = None
    for attempt in range(_MAX_RETRIES + 1):
        if provider == "api":
            try:
                resp = client.messages.create(
                    model=MODEL, max_tokens=max_tokens,
                    messages=[{"role": "user", "content": attempt_prompt}],
                )
            except Exception as e:  # noqa: BLE001
                name = type(e).__name__
                if "Authentication" in name or "PermissionDenied" in name:
                    raise LLMAuthError(
                        f"ANTHROPIC_API_KEY was rejected by the API ({e}). Check the "
                        f"key is correct, active, and has access to {MODEL}.") from e
                raise
            text = "".join(b.text for b in resp.content
                           if getattr(b, "type", "") == "text")
            in_tok, out_tok = resp.usage.input_tokens, resp.usage.output_tokens
        else:
            # max_tokens has no CLI equivalent; Sonnet's default output ceiling is
            # far above anything this pipeline asks for, so nothing is lost.
            text, in_tok, out_tok = _ask_claude_cli(attempt_prompt)
        _save_prompt(client_key, purpose, h, attempt_prompt, text)
        _log(client_key, {
            "ts": time.time(), "purpose": purpose, "hash": h, "cached": False,
            "attempt": attempt, "model": MODEL, "provider": provider,
            "in_tokens": in_tok, "out_tokens": out_tok,
        })
        try:
            parsed = _extract_json(text)
            # Shape check BEFORE caching. Two reasons this is not optional:
            #  * _extract_json falls back to bracket-matching, so prose containing
            #    an unrelated brace pair ("Sure, {as requested} here is...") makes
            #    it return a LIST where every caller does .get() — an
            #    AttributeError that took down the whole run.
            #  * without it, a wrong-shaped response gets written to llm_cache.json
            #    and poisons that prompt hash permanently.
            if not isinstance(parsed, expect):
                raise LLMBadResponse(
                    f"expected JSON {expect.__name__}, got {type(parsed).__name__}")
        except LLMBadResponse as e:  # noqa: BLE001
            last_err = e
            attempt_prompt = (
                f"{prompt}\n\nYour previous response could not be parsed as JSON "
                f"({e}). Respond with ONLY valid JSON, no prose, no code fence.")
            continue
        if use_cache:
            cache[h] = parsed
            _save_cache(client_key, cache)
        return parsed

    raise LLMBadResponse(f"unparseable after {_MAX_RETRIES + 1} attempts: {last_err}")


def as_list(obj, key: str) -> list:
    """Read `obj[key]` as a list of dicts, tolerating anything the model emits.

    The outer response can be a valid dict while a field inside it is the wrong
    type — `{"decisions": null}` is a natural way for a model to express an empty
    batch, and `{"proposals": "none this time"}` is a plausible slip. Both used to
    raise AttributeError mid-run (iterating a string yields characters, then
    .get() fails on each one)."""
    if not isinstance(obj, dict):
        return []
    v = obj.get(key)
    if not isinstance(v, (list, tuple)):
        return []
    return [x for x in v if isinstance(x, dict)]


def call_count(client_key: str) -> dict:
    """Real usage numbers from the log — used by the CLI to report cost."""
    p = _log_path(client_key)
    if not p.exists():
        return {"calls": 0, "cached": 0, "in_tokens": 0, "out_tokens": 0,
                "providers": []}
    calls = cached = tin = tout = 0
    providers: dict[str, int] = {}
    for line in p.read_text().splitlines():
        try:
            r = json.loads(line)
        except Exception:  # noqa: BLE001
            continue
        if r.get("cached"):
            cached += 1
        else:
            calls += 1
            tin += r.get("in_tokens", 0)
            tout += r.get("out_tokens", 0)
            # Records written before provider logging existed have no such key.
            prov = r.get("provider", "api")
            providers[prov] = providers.get(prov, 0) + 1
    return {"calls": calls, "cached": cached, "in_tokens": tin, "out_tokens": tout,
            "providers": sorted(providers.items(), key=lambda kv: -kv[1])}
