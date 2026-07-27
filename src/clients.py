"""Client registry: the single place that answers "which taxonomy, which trained
model, which embedding config, and which chart style apply to THIS call".

Before this module existed, that routing was hardcoded in two places and only knew
about two clients: src/extract.py's extract_call() checked `stem.startswith("LCS")`
to pick ABCL vs JustDial's model, and action_intent() fell back through ABCL's
ACTIONS then JustDial's COARSE ACTIONS. A third client (Myntra) already existed in
practice (data/models/generic_clf.pkl, trained on real Myntra data) but nothing in
the live extraction path knew to route to it — a fresh Myntra transcript run through
extract_call() would have been silently classified with ABCL's loan-intent model.
This module is the fix: adding a new known client is a registry entry, not a code
change to extract.py.

Detection order for a given transcript:
  1. filename prefix (fast, exact — e.g. JustDial's "LCS-")
  2. content signature (a known client's calls open with a recognizable phrase,
     e.g. ABCL's agent always says "Aditya Birla Capital", Myntra's always says
     "मिंत्रा" / "मीरा")
  3. no match -> UNKNOWN, caller decides the client slug (e.g. from a folder name)
     and everything routes through the generic broad taxonomy.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

import config
from src import extract, generic_taxonomy, justdial_coarse, justdial_taxonomy

MODELS_DIR = config.DATA / "models"


@dataclass
class Client:
    key: str                      # stable slug: also the <key>_output/ folder name
    label: str                    # human-readable, for chart titles / README
    signature: list                # lowercase substrings checked against raw transcript text
    filename_prefix: Optional[str]  # fast-path exact match, e.g. "LCS-" (None if none)
    model_path: Path
    embed_model: str
    embed_prefix: str
    intent_library: list
    actions: dict
    intent_desc: dict
    sentiment_lexicon: list
    tool_rules: dict
    has_sop_skeleton: bool = False   # True only for ABCL's hand-authored fixed DAG
    has_dispositions: bool = False  # True if src/dispositions.py has a prototype set for this client
    transcripts_dir: Path = field(init=False)

    def __post_init__(self):
        self.transcripts_dir = config.CLIENTS_DIR / self.key / "transcripts"


def _abcl_client() -> Client:
    from src.distill import MODEL_PATH
    return Client(
        key="abcl", label="ABCL — loan application calls",
        signature=["aditya birla", "priya"], filename_prefix=None,
        model_path=MODEL_PATH, embed_model=extract.EMBED_MODEL, embed_prefix="",
        intent_library=extract.INTENT_LIBRARY, actions=extract.ACTIONS,
        intent_desc=extract.INTENT_DESC, sentiment_lexicon=extract.SENTIMENT_LEXICON,
        tool_rules=extract.TOOL_RULES, has_sop_skeleton=True, has_dispositions=True,
    )


def _justdial_client() -> Client:
    # "justdial" and "justdial_coarse" are two label granularities over the SAME
    # transcripts (see src/distill.py's DOMAINS), and both currently save to the
    # same data/models/justdial_clf.pkl — whichever was trained most recently is
    # what's actually on disk (today: the coarse one, per justdial_coarse.py's own
    # finding that the fine 24-intent model only scored ~32% CV on noisy ASR).
    # actions/intent_desc are merged across BOTH granularities so extraction is
    # correct regardless of which one the saved model currently predicts.
    return Client(
        key="justdial", label="JustDial — lead-generation support calls",
        signature=["justdial", "jd.com"], filename_prefix="LCS-",
        model_path=MODELS_DIR / "justdial_clf.pkl",
        embed_model=extract.EMBED_MODEL, embed_prefix="",
        intent_library=justdial_taxonomy.INTENT_LIBRARY,
        actions={**justdial_taxonomy.ACTIONS, **justdial_coarse.ACTIONS},
        intent_desc=justdial_coarse.INTENT_DESC, sentiment_lexicon=extract.SENTIMENT_LEXICON,
        tool_rules=justdial_taxonomy.TOOL_RULES, has_sop_skeleton=False, has_dispositions=True,
    )


def _myntra_client() -> Client:
    # Myntra has no fine-grained taxonomy of its own yet — it was onboarded straight
    # onto the broad generic taxonomy (see src/generic_bootstrap.py). It gets its
    # own registry entry (rather than falling through to UNKNOWN) purely so its
    # persistent transcript store and output folder are named "myntra", not a
    # slug guessed from whatever folder a new batch happens to arrive in.
    return Client(
        key="myntra", label="Myntra — e-commerce delivery support calls",
        signature=["myntra", "मिंत्रा", "मीरा"], filename_prefix=None,
        model_path=MODELS_DIR / "generic_clf.pkl",
        embed_model="intfloat/multilingual-e5-base", embed_prefix="query: ",
        intent_library=generic_taxonomy.INTENT_LIBRARY, actions=generic_taxonomy.ACTIONS,
        intent_desc=generic_taxonomy.INTENT_DESC, sentiment_lexicon=extract.SENTIMENT_LEXICON,
        tool_rules={}, has_sop_skeleton=False,
    )


# Known clients, checked in this order (first match wins). filename_prefix checks
# run before any signature checks, across ALL clients, since a prefix match is exact
# and cheap; signature checks (which require reading file content) run after.
KNOWN_CLIENTS: list = None  # populated lazily (needs distill import; see get_known_clients)


def get_known_clients() -> list:
    global KNOWN_CLIENTS
    if KNOWN_CLIENTS is None:
        KNOWN_CLIENTS = [_abcl_client(), _justdial_client(), _myntra_client()]
    return KNOWN_CLIENTS


def make_generic_client(slug: str, label: str | None = None) -> Client:
    """A client with no dedicated fine taxonomy: routes through the shared broad
    generic taxonomy and the shared generic_clf.pkl model, under its own slug/output
    folder. This is what a brand-new, never-seen-before client gets automatically."""
    return Client(
        key=slug, label=label or f"{slug} (generic taxonomy)",
        signature=[], filename_prefix=None,
        model_path=MODELS_DIR / "generic_clf.pkl",
        embed_model="intfloat/multilingual-e5-base", embed_prefix="query: ",
        intent_library=generic_taxonomy.INTENT_LIBRARY, actions=generic_taxonomy.ACTIONS,
        intent_desc=generic_taxonomy.INTENT_DESC, sentiment_lexicon=extract.SENTIMENT_LEXICON,
        tool_rules={}, has_sop_skeleton=False,
    )


def _read_head(path: Path, max_chars: int = 4000) -> str:
    try:
        return path.read_text(errors="ignore")[:max_chars].lower()
    except Exception:  # noqa: BLE001
        return ""


def detect_client_for_path(path: Path) -> Optional[Client]:
    """Detect the known client for ONE transcript file, or None if unrecognized."""
    path = Path(path)
    stem = path.stem
    clients = get_known_clients()

    for c in clients:
        if c.filename_prefix and stem.startswith(c.filename_prefix):
            return c

    text = _read_head(path)
    for c in clients:
        if c.signature and any(sig.lower() in text for sig in c.signature):
            return c
    return None


def detect_client_for_batch(paths: list) -> Optional[Client]:
    """Detect the client for a BATCH of transcripts (majority vote across a sample),
    used when onboarding/regenerating a whole folder rather than one call. Returns
    None if no known client matches convincingly."""
    from collections import Counter
    paths = list(paths)
    sample = paths[:20] if len(paths) > 20 else paths  # cap reads for large batches
    votes = Counter()
    for p in sample:
        c = detect_client_for_path(Path(p))
        if c is not None:
            votes[c.key] += 1
    if not votes:
        return None
    winner_key, winner_n = votes.most_common(1)[0]
    if winner_n / len(sample) < 0.5:   # not a convincing majority
        return None
    return next(c for c in get_known_clients() if c.key == winner_key)
