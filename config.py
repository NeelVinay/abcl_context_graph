"""Central configuration for the ABCL context-graph pipeline."""
from pathlib import Path

# --- Paths ---
ROOT = Path(__file__).parent
DATA = ROOT / "data"
TRANSCRIPTS_DIR = DATA / "transcripts"   # drop raw transcripts here
CACHE_DIR = DATA / "cache"               # cached per-call LLM extractions
OUTPUT_DIR = DATA / "output"             # master graph json + visuals

# --- Speech-to-text (Stage: mp3 recordings -> plain-text transcripts) ---
AUDIO_SRC = Path.home() / "Downloads" / "leads_mp3_data"  # raw call recordings (.mp3)
AUDIO_TRANSCRIPTS_DIR = DATA / "audio_transcripts"        # plain-text STT output (Agent:/Customer:)

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

for _d in (TRANSCRIPTS_DIR, CACHE_DIR, OUTPUT_DIR, AUDIO_TRANSCRIPTS_DIR):
    _d.mkdir(parents=True, exist_ok=True)
