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

# SEMANTIC disposition prototypes, PER DOMAIN. A call is matched (zero-shot, no training)
# to the closest domain-appropriate bucket. Dispositions are ROUTED by domain in
# assign_dispositions so JustDial buckets never leak onto ABCL calls and vice-versa.

# --- JustDial (lead-gen support): why a business owner is complaining ---
JUSTDIAL_PROTOTYPES = {
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

# --- ABCL (loan-application resume): how/why the loan call went ---
ABCL_PROTOTYPES = {
    "proceeding_application": ["हाँ link भेज दीजिए", "मैं apply करना चाहता हूँ",
                              "हो गया भर दिया", "आगे बताइए", "ठीक है शुरू करते हैं"],
    "not_interested": ["मुझे loan नहीं चाहिए", "मुझे interest नहीं है", "अभी loan नहीं लेना",
                       "नहीं चाहिए मुझे"],
    # NOTE: previously included generic "other bank" phrasing — split out below into
    # has_loan_unspecified, since a loan from an unnamed/different lender is a distinct
    # scenario from an ABCL-specific existing loan (matches the DSL's own distinction).
    "already_has_loan": ["मेरा पहले से आपकी company से loan चल रहा है",
                         "पहले Aditya Birla से loan लिया हुआ है",
                         "already आपकी तरफ से loan मिल चुका है",
                         "आपकी company से पहले भी loan लिया था"],
    "has_loan_unspecified": ["मेरे पास पहले से एक loan है", "मैंने दूसरी जगह से loan ले लिया",
                             "किसी और bank से ले लिया", "already loan चल रहा है मेरा",
                             "पहले से loan है मेरे पास"],
    "prior_attempt_failed": ["पहले try किया था reject हो गया",
                             "पहले भी apply किया था कुछ नहीं मिला",
                             "loan amount नहीं दिखा था पहले",
                             "पहले call में कुछ नहीं मिला था"],
    "wants_more_amount": ["मुझे ज़्यादा loan चाहिए", "इतना कम amount क्यों",
                          "amount बढ़ा सकते हैं क्या", "aur zyada loan chahiye",
                          "ye kam hai mujhe zyada chahiye"],
    "callback_requested": ["अभी busy हूँ बाद में call करें", "कल बात करते हैं",
                           "अभी time नहीं है", "बाद में call करना"],
    "wrong_person": ["ये मेरा number नहीं है", "आप galat number पे call कर रहे हैं",
                     "मैं वो व्यक्ति नहीं हूँ", "ये किसी और का number है"],
    "tech_or_otp_issue": ["OTP नहीं आया", "link नहीं खुल रहा", "page पे error आ रहा है",
                          "app नहीं चल रहा", "SMS नहीं मिला"],
    "call_audio_issue": ["आवाज़ नहीं आ रही आपकी", "आवाज़ टूट रही है", "आवाज़ clear नहीं आ रही",
                         "line cut हो रही है", "network issue लग रहा है call में",
                         "आपकी आवाज़ साफ़ नहीं है"],
    "security_concern": ["ये fraud तो नहीं है", "fake link तो नहीं", "scam तो नहीं है",
                         "genuine है क्या", "भरोसा नहीं हो रहा"],
    "language_barrier": ["मुझे हिंदी नहीं आती", "english में बात करो",
                         "मेरी language में बोलिए"],
}

DISPOSITION_PROTOTYPES = {"justdial": JUSTDIAL_PROTOTYPES, "abcl": ABCL_PROTOTYPES}

DISPOSITION_LABEL.update({
    # JustDial
    "lead_issue": "Lead problem (none / wrong / low-value)",
    "rating_issue": "Rating / review concern",
    "coverage_issue": "Category / area coverage",
    "technical_issue": "App / system error",
    "cancel_disinterest": "Cancel / not interested",
    # ABCL
    "proceeding_application": "Proceeding with application",
    "not_interested": "Not interested",
    "already_has_loan": "Already has THIS loan from ABCL specifically",
    "has_loan_unspecified": "Already has a loan, lender unspecified / elsewhere",
    "prior_attempt_failed": "Tried before on an earlier call, no offer / rejected",
    "wants_more_amount": "Pushes for a higher loan amount than offered",
    "callback_requested": "Callback requested",
    "wrong_person": "Wrong person / number",
    "tech_or_otp_issue": "Tech / OTP / link issue",
    "call_audio_issue": "Phone line / voice quality issue (not app/page)",
    "security_concern": "Fraud / security concern",
    "language_barrier": "Language barrier",
})


def _domain_of(call: dict) -> str:
    """JustDial calls are LCS-* ; everything else is ABCL."""
    return "justdial" if str(call.get("call_id", "")).startswith("LCS") else "abcl"


_EMBED: dict = {"model": None, "by_domain": {}}


def _ensure_embedder():
    if _EMBED["model"] is not None:
        return
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from src.extract import EMBED_MODEL
    m = _EMBED["model"] = SentenceTransformer(EMBED_MODEL)
    for domain, protos in DISPOSITION_PROTOTYPES.items():
        keys, cents = [], []
        for k, examples in protos.items():
            emb = m.encode(examples, normalize_embeddings=True)
            cents.append(np.asarray(emb).mean(axis=0))
            keys.append(k)
        _EMBED["by_domain"][domain] = {"keys": keys, "centroids": np.vstack(cents)}


def assign_dispositions(calls: list[dict], threshold: float = 0.30) -> None:
    """Set call['disposition'] via SEMANTIC similarity to that call's DOMAIN prototypes
    (ABCL vs JustDial, routed by call_id). Uses customer turns; below threshold -> 'none'."""
    import numpy as np
    _ensure_embedder()
    texts, domains = [], []
    for c in calls:
        cust = " ".join(t["text"] for t in c.get("turns", []) if t.get("speaker") == "customer")
        texts.append(cust or " ".join(t["text"] for t in c.get("turns", [])))
        domains.append(_domain_of(c))
    embs = np.asarray(_EMBED["model"].encode(texts, normalize_embeddings=True))
    for c, emb, dom in zip(calls, embs, domains):
        d = _EMBED["by_domain"][dom]
        sims = emb @ d["centroids"].T
        best = int(sims.argmax())
        c["disposition"] = d["keys"][best] if sims[best] >= threshold else "none"


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
