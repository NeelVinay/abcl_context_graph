"""Central configuration for the ABCL context-graph pipeline."""
from pathlib import Path

# --- Paths ---
ROOT = Path(__file__).parent
DATA = ROOT / "data"
CACHE_DIR = DATA / "cache"               # cached per-call extractions (all clients, keyed by call_id)
OUTPUT_DIR = DATA / "output"             # <client>_output/ folders live here
ARCHIVE_DIR = DATA / "archive"           # superseded / legacy data, kept for provenance only

# --- Per-client persistent transcript stores (see src/clients.py) ---
# CLIENTS_DIR/<client_key>/transcripts/ holds the CURRENT full transcript set for
# that client. python run_client.py is the normal way to populate/update this;
# see its --append flag for adding to a client's set instead of replacing it.
CLIENTS_DIR = DATA / "clients"

# --- Legacy paths, kept only for src/transcribe.py and run.py's low-level flags ---
TRANSCRIPTS_DIR = CLIENTS_DIR / "abcl" / "transcripts"
AUDIO_SRC = Path.home() / "Downloads" / "leads_mp3_data"  # raw call recordings (.mp3)
AUDIO_TRANSCRIPTS_DIR = CLIENTS_DIR / "justdial" / "transcripts"  # plain-text STT output

# --- Models (confirm exact IDs against the claude-api reference when wiring extraction) ---
EXTRACTION_MODEL = "claude-sonnet-4-6"   # per-call extraction (cost-efficient, high volume)
REASONING_MODEL = "claude-opus-4-8"      # taxonomy discovery + canonical naming (harder reasoning)

# --- Pipeline knobs ---
TAXONOMY_SAMPLE_SIZE = 12      # how many transcripts to use when discovering the intent set
FUZZY_CUTOFF = 90             # rapidfuzz token_set_ratio threshold for trivial-variant folding
EMBED_MODEL = "all-mpnet-base-v2"
EMBED_SIM_THRESHOLD = 0.75   # cosine threshold for "same intent" during canonicalization
MIN_EDGE_COUNT = 15          # prune edges below this count when visualizing (raise for more calls)

# Special boundary nodes so first-step distribution and drop-offs are representable as edges.
START = "__START__"
END = "__END__"

for _d in (CACHE_DIR, OUTPUT_DIR, ARCHIVE_DIR, CLIENTS_DIR, TRANSCRIPTS_DIR, AUDIO_TRANSCRIPTS_DIR):
    _d.mkdir(parents=True, exist_ok=True)
