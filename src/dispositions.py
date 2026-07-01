"""Phase B: call-level DISPOSITION detection (the manager's "different flows").

IMPORTANT: the manager's examples (not_interested, already_has_loan, language_barrier)
were from the LOAN context. These leads_mp3_data calls are LEAD-GENERATION / business-
listing SUPPORT calls — mined from the real transcripts, the actual dispositions are about
the lead service ("loan" never appears; "leads" dominates). This lexicon is therefore
data-grounded from the transcripts, not the loan examples.

A disposition = the customer's main reason/theme for the call. It's detected per call from
the transcript text (lightweight phrase matching, no model) and used as the EARLY branch
node in the flow tree, so the tree branches by disposition like the manager wants.

NOTE: trigger phrases below are a first draft from a handful of transcripts; VALIDATE and
expand against the full set once the 30-call run finishes (this module is not yet wired in).
"""
from __future__ import annotations

# Ordered by priority: earlier = stronger/more specific. Each disposition -> trigger phrases
# (Hindi / Hinglish / English variants as they actually appear in the ASR text, lowercased).
# Order = priority (earlier wins ties). Domain-specific lead complaints rank above the
# generic ones so a "lead problem" isn't mislabeled as a generic technical issue.
DISPOSITIONS = [
    ("no_leads", "No / fewer leads coming", [
        "लीड नहीं आ", "लीड नहीं आई", "लीड नहीं मिल", "लीड नहीं रही", "लीड कम आ", "लीड कम हो",
        "लीड्स नहीं", "leads नहीं", "no leads", "लीड बंद", "लीड का इशू", "लीड की प्रॉब्लम",
        "लीड को लेके", "लीड को लेकर", "लीड नहीं आ रही", "नहीं आ रही है लीड", "एक भी लीड नहीं",
    ]),
    ("irrelevant_leads", "Wrong / irrelevant leads", [
        "रॉंग लीड", "wrong lead", "गलत लीड", "रॉंग आ रही", "रॉंग एरिया", "गलत एरिया",
        "wrong location", "रॉंग लोकेशन", "irrelevant", "मतलब की नहीं", "काम की नहीं",
        "रॉंग नीड", "गलत नीड",
    ]),
    ("roi_complaint", "No value / money wasted / refund", [
        "पैसा वेस्ट", "पैसा बर्बाद", "पैसा वापस", "रिफंड", "refund", "काम नहीं आया",
        "वैल्यू नहीं", "value नहीं", "बिजनेस नहीं", "फायदा नहीं", "रुपिया", "रुपए",
        "पैसा देश हो", "पैसे का", "मेंबरशिप",
    ]),
    ("cancel_churn", "Wants to cancel / stop service", [
        "बंद कर", "बंद करना", "बंद करो", "cancel", "कैंसिल", "deactivate", "सर्विस बंद",
        "बंद करवा",
    ]),
    ("rating_issue", "Rating / review concern", [
        "rating", "रेटिंग", "review", "रिव्यू", "रेटिंग कम", "रेटिंग कारती",
    ]),
    ("coverage_issue", "Category / pincode / area coverage", [
        "category", "कैटेगरी", "pincode", "पिन कोड", "पिनकोड", "एरिया कवर", "लोकेशन डाला",
    ]),
    ("technical_issue", "App / system error", [
        # narrow: only genuine app/system errors, NOT generic "problem/issue"
        "app नहीं", "एप नहीं", "app में", "एप्लिकेशन में दिक", "एरर आ", "error आ",
        "नहीं चल रहा", "not working", "नहीं खुल", "लॉगिन", "login", "otp नहीं", "ओटीपी नहीं",
        "वेबसाइट नहीं", "site नहीं",
    ]),
    ("not_interested", "Not interested", [
        "interested नहीं", "इंटरेस्ट नहीं", "नहीं चाहिए", "नहीं लेना", "टाइम पास", "मना कर",
    ]),
]

# agent-side resolution signals (map to how the call ended, not the customer's issue)
RESOLUTION = {
    "raised_request": ["request डाल", "रिक्वेस्ट डाल", "raise कर", "रेज कर", "चेक करवा",
                       "मेंशन कर रही", "टाइम दीजिए", "थोड़ा time", "24", "48", "next का करेंगे"],
    "transferred": ["team", "टीम", "transfer", "ट्रांसफर", "senior", "सीनियर",
                    "relationship", "आरएम", "department", "विभाग"],
}

DISPOSITION_LABEL = {key: label for key, label, _ in DISPOSITIONS}
DISPOSITION_LABEL["none"] = "No clear disposition"

# COARSE, well-separated disposition buckets for SEMANTIC matching. The fine lead
# complaints (no-leads / wrong-leads / no-ROI) don't separate on noisy Hinglish ASR — they
# all read as "my leads aren't working" — so they're merged into one reliable `lead_issue`.
# (Fine-grained splitting would need labeled data + a trained classifier; see plan Phase B+.)
DISPOSITION_PROTOTYPES = {
    "lead_issue": ["मुझे लीड नहीं आ रही है", "leads नहीं मिल रहे हैं", "बहुत कम लीड आ रहे हैं",
                   "जो लीड आ रही है वो गलत है", "रॉंग एरिया की लीड आ रही है",
                   "लीड को लेकर problem है", "इतना पैसा देकर भी लीड का फायदा नहीं हुआ",
                   "लीड का इशू है", "एक भी लीड नहीं मिली"],
    "rating_issue": ["मेरी rating कम है", "reviews की वजह से problem है", "rating बढ़ानी है",
                     "negative review आ गया"],
    "coverage_issue": ["मेरा pincode area cover नहीं है", "category सही नहीं है",
                       "मेरी location की problem है", "गलत category में हूँ"],
    "technical_issue": ["app नहीं चल रहा", "website पर error आ रहा है", "login नहीं हो रहा",
                        "OTP नहीं आ रहा"],
    "cancel_disinterest": ["मुझे ये service बंद करनी है", "subscription cancel कर दो",
                           "मुझे interest नहीं है", "अब मुझे ये नहीं चाहिए"],
}

DISPOSITION_LABEL.update({
    "lead_issue": "Lead problem (none / wrong / low-value)",
    "rating_issue": "Rating / review concern",
    "coverage_issue": "Category / area coverage",
    "technical_issue": "App / system error",
    "cancel_disinterest": "Cancel / not interested",
})

_EMBED = {"model": None, "centroids": None, "keys": None}


def _ensure_embedder():
    if _EMBED["model"] is not None:
        return
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from src.extract import EMBED_MODEL
    m = SentenceTransformer(EMBED_MODEL)
    keys, cents = [], []
    for k, protos in DISPOSITION_PROTOTYPES.items():
        emb = m.encode(protos, normalize_embeddings=True)
        cents.append(np.asarray(emb).mean(axis=0))
        keys.append(k)
    _EMBED.update(model=m, centroids=np.vstack(cents), keys=keys)


def assign_dispositions(calls: list[dict], threshold: float = 0.30) -> None:
    """Set call['disposition'] for every call via SEMANTIC similarity to prototypes.
    Uses the CUSTOMER's turns (the complaint); below threshold -> 'none'. Batched."""
    import numpy as np
    _ensure_embedder()
    texts = []
    for c in calls:
        cust = " ".join(t["text"] for t in c.get("turns", []) if t.get("speaker") == "customer")
        texts.append(cust or " ".join(t["text"] for t in c.get("turns", [])))
    embs = np.asarray(_EMBED["model"].encode(texts, normalize_embeddings=True))
    sims = embs @ _EMBED["centroids"].T          # cosine (both normalized)
    for c, row in zip(calls, sims):
        best = int(row.argmax())
        c["disposition"] = _EMBED["keys"][best] if row[best] >= threshold else "none"


def detect_dispositions(call: dict) -> list[tuple[str, int]]:
    """Return [(disposition, hit_count)] present in the call, strongest first.
    Ties break by DISPOSITIONS priority order (domain-specific lead complaints first)."""
    text = " ".join(t.get("text", "") for t in call.get("turns", [])).lower()
    scored = []
    for prio, (key, _label, phrases) in enumerate(DISPOSITIONS):
        hits = sum(text.count(p.lower()) for p in phrases)
        if hits:
            scored.append((key, hits, prio))
    scored.sort(key=lambda x: (-x[1], x[2]))   # most hits, then higher priority
    return [(k, h) for k, h, _ in scored]


def primary_disposition(call: dict) -> str:
    """The single dominant disposition for the early flow-tree branch (or 'none').
    Prefers the semantic result from assign_dispositions() if present; else lexicon."""
    if "disposition" in call:
        return call["disposition"]
    scored = detect_dispositions(call)
    return scored[0][0] if scored else "none"
