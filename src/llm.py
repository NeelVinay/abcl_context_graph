"""Thin, cached, logged Anthropic client — the ONLY place this project talks to an
LLM. Everything else in the improvement pipeline stays deterministic.

Design constraints, all deliberate:

  * **Never silently degrades.** No API key -> raises. A heuristic fallback that
    fakes a judgment call is worse than a hard failure, because the output looks
    identical either way and gets written into a production prompt.
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
import time
from pathlib import Path

import config

MODEL = "claude-sonnet-5"
_MAX_RETRIES = 1


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
    p = _cache_path(client_key)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(cache, indent=2, ensure_ascii=False))


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
             *, max_tokens: int = 4000, use_cache: bool = True):
    """Send `prompt`, expect JSON back. Returns the parsed object.

    Raises LLMUnavailable (no key/SDK) or LLMBadResponse (unparseable twice).
    Callers treat LLMBadResponse as "drop this batch", never as "assume a default"."""
    h = hashlib.sha1(prompt.encode("utf-8")).hexdigest()
    cache = _load_cache(client_key) if use_cache else {}
    if use_cache and h in cache:
        _log(client_key, {"ts": time.time(), "purpose": purpose, "hash": h,
                          "cached": True})
        return cache[h]

    client = _client()
    attempt_prompt = prompt
    last_err = None
    for attempt in range(_MAX_RETRIES + 1):
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
        text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
        _log(client_key, {
            "ts": time.time(), "purpose": purpose, "hash": h, "cached": False,
            "attempt": attempt, "model": MODEL,
            "in_tokens": resp.usage.input_tokens,
            "out_tokens": resp.usage.output_tokens,
        })
        try:
            parsed = _extract_json(text)
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


def call_count(client_key: str) -> dict:
    """Real usage numbers from the log — used by the CLI to report cost."""
    p = _log_path(client_key)
    if not p.exists():
        return {"calls": 0, "cached": 0, "in_tokens": 0, "out_tokens": 0}
    calls = cached = tin = tout = 0
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
    return {"calls": calls, "cached": cached, "in_tokens": tin, "out_tokens": tout}
