"""Stage 2: per-call extraction (LOCAL Python backend - no API, data stays on machine).

Turns ONE transcript into a CallGraph dict (schema.py shape). Captures everything
the manager asked for, all locally:
  - ACTION-ORIENTED, actor-aware intents  (agent_request_pan -> customer_provide_pan)
  - SENTIMENT for customer turns          (skeptical / distrustful / frustrated ...)
  - TOOL / API calls                      (send_sms, send_otp, push_to_crm, transfer_to_rm ...)
  - KEYWORDS (short signal phrases)        instead of full sentences

Pipeline: parse -> clean (drop noise, merge fragments) -> classify base intent
(keyword rules + multilingual embedding) -> map to action intent + sentiment + tool
+ keywords. A Claude backend can replace the classify step later with zero downstream change.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

EMBED_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"  # multilingual: handles Hindi/Hinglish
EMBED_THRESHOLD = 0.45
MERGE_GAP_SEC = 4.0
MAX_KEYWORDS = 5

# --- base intent library: ordered SPECIFIC -> GENERAL (first keyword hit wins) ---
INTENT_LIBRARY = [
    ("skip_udyam", ["skip"], ["skip anyway कर देता हूँ", "नीचे skip option पर click कर दीजिए"]),
    ("udyam_verification", ["udyam", "उद्यम"], ["udyam number और registered mobile भरें", "ये udyam verification page है"]),
    ("enter_pan", ["pan", "पैन"], ["अपना PAN number भरें", "PAN card number डाल दिया"]),
    ("mobile_otp", ["otp"], ["mobile number डालकर get OTP करें", "OTP डालकर verify कर दिया"]),
    ("enter_email", ["email"], ["अपना email address दर्ज करें", "email भर दिया"]),
    ("enter_income", ["income"], ["net monthly income टाइप करें", "मेरी monthly income इतनी है"]),
    ("organization_name", ["organization", "organisation", "company name"], ["organization name के field में company का नाम enter करें", "अपनी company या firm का नाम डालिए"]),
    ("business_details", ["business", "shop", "office address"], ["business का नाम और address भरें", "self employed हूँ अपना business है"]),
    ("employment_type", ["salaried", "self employ", "self-employ", "self employee"], ["salaried या self employed चुनिए", "मैं self employed हूँ"]),
    ("accept_terms", ["terms and condition", "terms", "बॉक्स चेक", "proceed पर"], ["terms and condition के box check करके proceed करें", "दोनों box check कर दिए"]),
    ("click_apply", ["apply now"], ["apply now button पर click करें", "apply हो गया है"]),
    ("manual_review", ["manual review"], ["application manual review के लिए जाएगी"]),
    ("final_offer", ["final offer", "loan amount and", "cannot be changed", "final and"], ["ये final offer page है, loan amount और tenure दिख रहा है"]),
    # Placed BEFORE address_error: "आवाज़"/"awaaz" is a distinctive audio-only trigger,
    # checked first so a call-audio complaint doesn't fall into address_error's broader
    # "error"/"नहीं हो रहा" keywords (first-hit-wins).
    ("call_audio_issue", ["आवाज़ नहीं आ", "आवाज़ टूट", "आवाज़ clear नहीं", "line cut", "voice cut", "awaaz nahi", "awaaz clear nahi", "network issue"], ["आपकी आवाज़ टूट रही है थोड़ी", "network issue लग रहा है, आवाज़ साफ़ नहीं आ रही"]),
    ("address_error", ["red", "error", "नहीं हो रहा", "leading slash"], ["address red में आ रहा है, हो नहीं रहा", "error आ रहा है address में", "extra space या slash हटा दीजिए"]),
    ("enter_address", ["address", "pincode", "locality", "building", "house number", "flat", "आधार"], ["अपना address आधार के अनुसार भरें", "house number, building name, street भरिए", "pincode डाल दीजिए"]),
    ("recording_disclosure", ["record", "training", "quality"], ["ये call training और quality purpose के लिए record हो रही है"]),
    ("present_offer", ["pre approved", "pre-approved", "loan offer", "personal loan"], ["आपके लिए pre approved personal loan offer है"]),
    ("send_sms_link", ["sms", "लिंक भेज", "link भेज"], ["मैं आपको SMS में link भेज रही हूँ", "link मिल गया है"]),
    ("open_link", ["website", "वेबसाइट", "site खुल", "खुल गई", "खुल गया", "लिंक पर क्लिक"], ["link पर click करें website खुलेगी", "site खुल गई है"]),
    ("personal_details", ["gender", "date of birth", "marital"], ["नाम, gender, date of birth भरें", "ये basic details का page है"]),
    ("transfer_to_rm", ["relationship manager", "specialist से connect"], ["अब मैं आपको relationship manager से connect कर रही हूँ", "हाँ connect करो"]),
    ("end_call", ["goodbye", "call end", "समय समाप्त", "duration has been exceeded", "<chd"], ["call end कर रही हूँ, goodbye", "धन्यवाद, कॉल यहीं समाप्त करती हूँ"]),
    ("greeting", ["नमस्ते", "hello", "namaste", "बात कर रही", "से बात"], ["नमस्ते, मैं प्रिया बोल रही हूँ", "क्या मैं अमित जी से बात कर रही हूँ", "hello हाँ जी"]),
    ("wait_hold", ["एक second", "एक सेकंड", "एक मिनट", "रुकिए", "wait"], ["एक second wait करिए please", "मैं इंतज़ार कर रही हूँ"]),
    ("processing_fee", ["processing fee", "emi", "interest rate", "charges"], ["processing fee ₹2,950 deduct होगी", "approximate EMI ₹5,150 बनेगी", "interest rate ten point nine nine percent है"]),
    ("reassure_trust", ["fraud", "scam", "genuine", "भरोसा"], ["क्या ये कोई fraud तो नहीं है", "नहीं, ये बिल्कुल genuine है, आप निश्चिंत रहें"]),
    ("clarify_repeat", ["फिर से कह", "फिर से बता", "साफ़ बोल", "दोबारा बोल", "एक बार फिर"], ["माफ़ कीजिए, क्या आप फिर से कहेंगे?", "थोड़ा साफ़ बोलेंगे?"]),
    ("ask_question", ["मतलब", "क्या भरूं", "क्या डालूं", "कौन सा", "कैसे"], ["locality का मतलब क्या है", "इसमें क्या भरना है"]),
    ("answer_query", [], ["interest rate के बारे में बता दीजिए", "मैं आपको समझा देती हूँ", "आपका सवाल समझ गई"]),
    ("agree", ["शुरू कर", "आगे बढ़", "go ahead"], ["जी आप शुरू कर सकते हैं", "हाँ आगे बढ़िए"]),
    ("report_done", ["हो गया", "भर दिया", "कर दिया", "कर लिया", "मिल गया"], ["हो गया", "भर दिया है", "कर दिया"]),
    ("acknowledge", [], ["जी ठीक है", "अच्छा", "हम्म ठीक है"]),
]
INTENT_BY_NAME = {name: kws for name, kws, _ in INTENT_LIBRARY}

# --- (speaker, base intent) -> action-oriented, actor-aware intent name ---
ACTIONS = {
    "greeting": {"agent": "agent_greet", "customer": "customer_greet"},
    "recording_disclosure": {"agent": "agent_disclose_recording", "customer": "customer_acknowledge"},
    "present_offer": {"agent": "agent_present_offer", "customer": "customer_react_to_offer"},
    "send_sms_link": {"agent": "agent_send_sms_link", "customer": "customer_report_sms_received"},
    "open_link": {"agent": "agent_guide_open_link", "customer": "customer_report_link_opened"},
    "click_apply": {"agent": "agent_guide_apply", "customer": "customer_report_applied"},
    "mobile_otp": {"agent": "agent_request_otp", "customer": "customer_do_otp"},
    "enter_pan": {"agent": "agent_request_pan", "customer": "customer_provide_pan"},
    "personal_details": {"agent": "agent_request_personal_details", "customer": "customer_provide_personal_details"},
    "enter_email": {"agent": "agent_request_email", "customer": "customer_provide_email"},
    "enter_address": {"agent": "agent_request_address", "customer": "customer_provide_address"},
    "address_error": {"agent": "agent_help_address_error", "customer": "customer_report_address_error"},
    "call_audio_issue": {"agent": "agent_acknowledge_audio_issue", "customer": "customer_report_audio_issue"},
    "employment_type": {"agent": "agent_ask_employment_type", "customer": "customer_state_employment_type"},
    "enter_income": {"agent": "agent_request_income", "customer": "customer_provide_income"},
    "business_details": {"agent": "agent_request_business_details", "customer": "customer_provide_business_details"},
    "organization_name": {"agent": "agent_request_org_name", "customer": "customer_provide_org_name"},
    "udyam_verification": {"agent": "agent_request_udyam", "customer": "customer_respond_udyam"},
    "skip_udyam": {"agent": "agent_offer_skip_udyam", "customer": "customer_skip_udyam"},
    "accept_terms": {"agent": "agent_request_terms_accept", "customer": "customer_accept_terms"},
    "manual_review": {"agent": "agent_inform_manual_review", "customer": "customer_acknowledge"},
    "final_offer": {"agent": "agent_present_final_offer", "customer": "customer_react_to_final_offer"},
    "transfer_to_rm": {"agent": "agent_transfer_to_rm", "customer": "customer_acknowledge_transfer"},
    "processing_fee": {"agent": "agent_explain_fee", "customer": "customer_query_fee"},
    "reassure_trust": {"agent": "agent_reassure_trust", "customer": "customer_express_distrust"},
    "answer_query": {"agent": "agent_answer_query", "customer": "customer_ask_query"},
    "ask_question": {"agent": "agent_clarify", "customer": "customer_ask_question"},
    "clarify_repeat": {"agent": "agent_ask_to_repeat", "customer": "customer_unclear"},
    "wait_hold": {"agent": "agent_wait", "customer": "customer_request_wait"},
    "agree": {"agent": "agent_confirm", "customer": "customer_agree"},
    "report_done": {"agent": "agent_confirm_step", "customer": "customer_report_done"},
    "acknowledge": {"agent": "agent_acknowledge", "customer": "customer_acknowledge"},
    "end_call": {"agent": "agent_end_call", "customer": "customer_acknowledge"},
}

# plain-English description per action-intent name (for intents.md glossary)
INTENT_DESC = {
    "agent_greet": "Agent's opening greeting and self-introduction",
    "customer_greet": "Customer's opening / picks up the call",
    "agent_disclose_recording": "Agent discloses the call is recorded for quality/training",
    "agent_present_offer": "Agent pitches the pre-approved loan offer",
    "customer_react_to_offer": "Customer reacts to the loan offer (interest, doubt, refusal)",
    "agent_send_sms_link": "Agent sends the SMS with the application link",
    "customer_report_sms_received": "Customer confirms the SMS/link arrived",
    "agent_guide_open_link": "Agent guides the customer to open the link/website",
    "customer_report_link_opened": "Customer confirms the link/page opened",
    "agent_guide_apply": "Agent guides the customer to tap Apply Now / start the form",
    "customer_report_applied": "Customer confirms they clicked Apply / started",
    "agent_request_otp": "Agent asks the customer to enter and verify the OTP",
    "customer_do_otp": "Customer enters/verifies the OTP",
    "agent_request_pan": "Agent asks the customer to fill their PAN number",
    "customer_provide_pan": "Customer fills/confirms their PAN",
    "agent_request_personal_details": "Agent asks for name, gender, DOB, marital status",
    "customer_provide_personal_details": "Customer fills their personal details",
    "agent_request_email": "Agent asks the customer to enter their email",
    "customer_provide_email": "Customer enters their email",
    "agent_request_address": "Agent asks the customer to fill their address / pincode",
    "customer_provide_address": "Customer fills their address details",
    "agent_help_address_error": "Agent helps resolve an address field error",
    "customer_report_address_error": "Customer reports the address field is erroring",
    "agent_acknowledge_audio_issue": "Agent acknowledges the phone line/voice is unclear",
    "customer_report_audio_issue": "Customer reports the call audio/line is breaking or unclear",
    "agent_ask_employment_type": "Agent asks salaried vs self-employed",
    "customer_state_employment_type": "Customer states their employment type",
    "agent_request_income": "Agent asks the customer to enter monthly income",
    "customer_provide_income": "Customer enters their income",
    "agent_request_business_details": "Agent asks for business details (self-employed)",
    "customer_provide_business_details": "Customer provides business details",
    "agent_request_org_name": "Agent asks for the organization/company name",
    "customer_provide_org_name": "Customer provides the organization name",
    "agent_request_udyam": "Agent asks for Udyam number (business registration)",
    "customer_respond_udyam": "Customer responds about Udyam registration",
    "agent_offer_skip_udyam": "Agent offers to skip Udyam (goes to manual review)",
    "customer_skip_udyam": "Customer chooses to skip Udyam",
    "agent_request_terms_accept": "Agent asks the customer to accept terms & conditions",
    "customer_accept_terms": "Customer accepts the terms & conditions",
    "agent_inform_manual_review": "Agent informs the application goes to manual review",
    "agent_present_final_offer": "Agent presents the final loan offer (amount, tenure)",
    "customer_react_to_final_offer": "Customer reacts to the final offer",
    "agent_transfer_to_rm": "Agent hands off to a Relationship Manager for KYC",
    "customer_acknowledge_transfer": "Customer acknowledges the transfer to RM",
    "agent_explain_fee": "Agent explains processing fee / EMI / interest rate",
    "customer_query_fee": "Customer asks about fees, EMI, or interest rate",
    "agent_reassure_trust": "Agent reassures the customer it's genuine (not fraud)",
    "customer_express_distrust": "Customer suspects fraud / is reluctant to share info",
    "agent_answer_query": "Agent answers the customer's question",
    "customer_ask_query": "Customer asks the agent a question",
    "agent_clarify": "Agent clarifies or re-explains a step",
    "customer_ask_question": "Customer asks what to do / what a field means",
    "agent_ask_to_repeat": "Agent asks the customer to repeat / didn't catch it",
    "customer_unclear": "Customer's turn was unclear / asked to repeat",
    "agent_wait": "Agent asks the customer to wait / is checking",
    "customer_request_wait": "Customer asks the agent to hold on a moment",
    "agent_confirm": "Agent confirms / agrees to proceed",
    "customer_agree": "Customer agrees to proceed",
    "agent_confirm_step": "Agent confirms a step is done, moves on",
    "customer_report_done": "Customer reports they finished the step",
    "agent_acknowledge": "Agent acknowledgement / back-channel",
    "customer_acknowledge": "Customer acknowledgement / agreement / back-channel",
    "agent_end_call": "Agent closes the call",
}

# --- tool / API call inference (STRICT, intent-coupled) ---
# The transcript has NO real tool logs, so a tool call is INFERRED from the
# agent's speech. Two guards keep it honest:
#   1) intent-coupled — a tool can ONLY fire on its owning base intent, so it
#      can never attach to the wrong node (e.g. an address turn never = transfer).
#   2) verb-gated — for "send" tools we also require a do/send verb in the turn,
#      so a mere mention ("OTP डालकर verify करिए" = guidance) does NOT fire.
# Weak inference (final_offer -> fetch_from_crm) was removed entirely.
# Each entry: base_intent -> (tool, [required verbs]). Empty verbs = the intent
# itself is the action (its keyword match is already specific enough).
TOOL_RULES = {
    "send_sms_link":  ("send_sms",       ["भेज", "send", "share कर", "कर रही हूँ", "कर दिया"]),
    "mobile_otp":     ("send_otp",       ["भेज", "send", "आएगा", "आ रहा", "generate", "get otp", "प्राप्त"]),
    "transfer_to_rm": ("transfer_to_rm", []),
    "manual_review":  ("push_to_crm",    []),
}

# --- customer sentiment lexicon (priority order; both scripts) ---
SENTIMENT_LEXICON = [
    ("distrustful", ["fraud", "scam", "fake", "धोखा", "फ्रॉड", "bharosa nahi", "trust nahi", "access nahi",
                     "genuine", "asli", "real company", "सच में सही"]),
    ("frustrated", ["nahi ho raha", "ho nahi raha", "नहीं हो रहा", "नहीं हो", "kitni baar", "baar baar",
                    "बार बार", "dubara", "दोबारा", "red aa raha", "pareshan", "kab tak", "कब तक"]),
    ("confused", ["samajh nahi", "समझ नहीं", "matlab kya", "मतलब क्या", "kya karna", "kya bharu",
                  "क्या भरूं", "kaise karu", "कैसे", "kaun sa", "confuse", "samjha"]),
    ("skeptical", ["pakka", "sure hai kya", "doubt", "sahi me", "really", "kya ye sahi"]),
    ("happy", ["bahut badhiya", "bahut accha", "great", "perfect", "khush", "accha laga", "thank you so much"]),
]

_FILLERS = {
    "maam", "madam", "mam", "ji", "hai", "haan", "han", "ha", "ok", "okay", "yes", "theek", "thik",
    "kar", "raha", "rahi", "hun", "hoon", "hu", "main", "mein", "aap", "ye", "yeh", "wo", "kya", "aur",
    "to", "ka", "ki", "ke", "na", "bhi", "ho", "gaya", "please", "sir", "acha", "accha",
    "अच्छा", "जी", "हाँ", "हां", "है", "मैं", "आप", "ये", "और", "को", "का", "की", "के", "कर", "रहा", "रही",
    "हूं", "हूँ", "क्या", "ठीक",
}

ACK_WORDS = {"ok", "okay", "k", "ji", "haan", "han", "ha", "yes", "yeah", "theek", "thik", "sure",
             "hmm", "achha", "accha", "ठीक", "जी", "हां", "हाँ", "ओके"}
_MAAM = {"ma", "am", "maam", "mam", "madam"}


# ---------- noise ----------
def _is_presence_check(text):
    t = text.lower()
    return "अभी भी" in text and ("कॉल" in text or "लाइन" in text or "call" in t or "line" in t)


def _is_presence_ack(text):
    t = text.lower()
    return ("call पर" in t or "कॉल पर" in text or "लाइन पर" in text) and ("हूं" in text or "हूँ" in text or "hun" in t)


def _is_bare_ack(text):
    words = [w for w in re.sub(r"[^\wऀ-ॿ\s]", " ", text).split() if w.lower() not in _MAAM]
    return (not words) or (len(words) <= 3 and all(w.lower() in ACK_WORDS for w in words))


def _is_noise(text):
    return _is_presence_check(text) or _is_presence_ack(text) or _is_bare_ack(text)


# ---------- parse + merge ----------
def _load_plaintext(text):
    """Parse the STT plain-text format (one turn per line):
        Agent: ...
        Customer: ...
    Produced by src/transcribe.py. No timestamps (ts=None) — turns are already merged
    per speaker, so _merge_fragments is a no-op on them."""
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line or ":" not in line:
            continue
        label, _, content = line.partition(":")
        content = content.strip()
        if not content:
            continue
        label = label.strip().lower()
        if label.startswith("agent"):
            speaker = "agent"
        elif label.startswith("customer"):
            speaker = "customer"
        else:
            continue
        out.append({"speaker": speaker, "text": content, "ts": None})
    return out


def _load_turns(path):
    text = Path(path).read_text()
    if not text.lstrip().startswith(("[", "{")):   # not JSON -> STT plain-text transcript
        return _load_plaintext(text)
    data = json.loads(text)
    out = []
    for m in data:
        content = (m.get("content") or "").strip()
        if not content:
            continue
        speaker = "customer" if m.get("speaker") == "user" else "agent"
        ts = m.get("timestamp")
        try:
            epoch = datetime.fromisoformat(ts).timestamp() if ts else None
        except Exception:  # noqa: BLE001
            epoch = None
        out.append({"speaker": speaker, "text": content, "ts": epoch})
    return out


def _merge_fragments(turns):
    merged = []
    for t in turns:
        prev = merged[-1] if merged else None
        if (prev and prev["speaker"] == t["speaker"] and prev["ts"] is not None
                and t["ts"] is not None and (t["ts"] - prev["ts"]) <= MERGE_GAP_SEC):
            prev["text"] = (prev["text"] + " " + t["text"]).strip()
            prev["ts"] = t["ts"]
        else:
            merged.append(dict(t))
    return merged


# ---------- base-intent classification ----------
def _keyword_intent(text):
    low = text.lower()
    for name, kws, _ in INTENT_LIBRARY:
        if any(kw.lower() in low for kw in kws):
            return name
    return None


def build_model_bundle():
    try:
        from sentence_transformers import SentenceTransformer
    except Exception:  # noqa: BLE001
        return None
    model = SentenceTransformer(EMBED_MODEL)
    labels, texts = [], []
    for name, _, examples in INTENT_LIBRARY:
        for ex in examples:
            labels.append(name)
            texts.append(ex)
    emb = model.encode(texts, convert_to_tensor=True, normalize_embeddings=True)
    return (model, labels, emb)


def _embed_intent(text, bundle):
    from sentence_transformers import util
    model, labels, emb = bundle
    q = model.encode(text, convert_to_tensor=True, normalize_embeddings=True)
    sims = util.cos_sim(q, emb)[0].tolist()
    idx = max(range(len(sims)), key=lambda i: sims[i])
    return labels[idx] if sims[idx] >= EMBED_THRESHOLD else "other"


def base_intent(text, bundle=None):
    kw = _keyword_intent(text)
    if kw:
        return kw
    return _embed_intent(text, bundle) if bundle else "other"


# ---------- sentiment / tool / keywords / entities ----------
def detect_sentiment(text):
    low = text.lower()
    for sentiment, phrases in SENTIMENT_LEXICON:
        if any(p.lower() in low for p in phrases):
            return sentiment
    return "neutral"


def action_intent(speaker, base):
    if base in ACTIONS:
        return ACTIONS[base].get(speaker, f"{speaker}_{base}")
    from src.justdial_coarse import ACTIONS as JD_ACTIONS   # coarse JustDial buckets
    if base in JD_ACTIONS:
        return JD_ACTIONS[base].get(speaker, f"{speaker}_{base}")
    return f"{speaker}_{base}"


def tool_for(speaker, base, text):
    """Infer a tool/API call from the AGENT's speech, strictly. The tool must be
    OWNED by this turn's base intent (no wrong-node attachment) and, for send
    tools, a do/send verb must be present (no mere mentions). Returns None for
    customer turns. This is a PROXY from speech, not an observed tool event."""
    if speaker != "agent":
        return None
    rule = TOOL_RULES.get(base)
    if not rule:
        return None
    tool, verbs = rule
    if verbs and not any(v in text.lower() for v in verbs):
        return None
    return tool


_PAN_RE = re.compile(r"\b[A-Z]{5}[0-9]{4}[A-Z]\b")
_PIN_RE = re.compile(r"\b[1-9][0-9]{5}\b")
_AMT_RE = re.compile(r"₹\s?[\d,]+")


def _entities(text):
    ents = []
    ents += [{"type": "amount", "value": m} for m in _AMT_RE.findall(text)]
    ents += [{"type": "pan", "value": m} for m in _PAN_RE.findall(text)]
    ents += [{"type": "pincode", "value": m} for m in _PIN_RE.findall(text)]
    return ents


def _salient_tokens(text, n=2):
    toks = re.findall(r"[\wऀ-ॿ]+", text)
    cand = [w for w in toks if len(w) >= 4 and w.lower() not in _FILLERS]
    seen, uniq = set(), []
    for w in sorted(cand, key=len, reverse=True):
        if w.lower() not in seen:
            seen.add(w.lower())
            uniq.append(w)
    return uniq[:n]


# Devanagari LETTERS/matras only (ऀ-ॣ) — excludes the danda ।(।), double
# danda, Devanagari digits and punctuation, so keywords like "करें" don't come out as "करें।".
_WORD_RE = re.compile(r"[a-zA-Zऀ-ॣ]+")


def build_keyword_vocab(texts, min_calls=2, min_len=3):
    """Corpus-driven keyword vocabulary: content terms that recur across calls.

    A document = one call. We keep terms appearing in >= min_calls DIFFERENT calls and
    not in the stopword list. This adapts to whatever the calls are about (loan onboarding,
    lead-gen support, ...) without curating per-domain lists, and the >=min_calls rule is
    a built-in PII guard: a customer name/place is call-specific (in one call) so it never
    qualifies, while domain vocabulary (leads, rating, ...) recurs and does.

    `texts` is an iterable of full call transcripts (one string per call).
    Returns {term: num_calls} used as a salience score.
    """
    from src.stopwords import STOPWORDS
    df = Counter()
    for call_text in texts:
        seen = {w for w in _WORD_RE.findall(call_text.lower())
                if len(w) >= min_len and w not in STOPWORDS and w not in _FILLERS}
        df.update(seen)
    return {w: c for w, c in df.items() if c >= min_calls}


def extract_keywords(text, base, sentiment, entities, vocab=None):
    low = text.lower()
    kws = [kw for kw in INTENT_BY_NAME.get(base, []) if kw.lower() in low]
    if sentiment != "neutral":
        for s, phrases in SENTIMENT_LEXICON:
            if s == sentiment:
                kws += [p for p in phrases if p.lower() in low]
    kws += [e["value"] for e in entities]
    # Data-driven fill: recurring content terms present in this turn (highest call-spread
    # first). Replaces the old "salient token" fallback that grabbed names/filler (SALMAN).
    if vocab:
        present = {w for w in _WORD_RE.findall(low) if w in vocab}
        kws += sorted(present, key=lambda w: (-vocab[w], -len(w)))
    out, seen = [], set()
    for k in kws:
        if k.lower() not in seen:
            seen.add(k.lower())
            out.append(k)
    return out[:MAX_KEYWORDS]


# ---------- outcome ----------
def _outcome(base_intents, text=""):
    """How the call resolved. Order = priority.
      transferred     - handed to an RM / escalated
      completed       - clean close (goodbye)
      raised_request  - agent logged a request / promised a follow-up (the common
                        lead-support resolution that used to be mislabeled 'incomplete')
      incomplete      - none of the above (dropped without resolution)
    """
    s = set(base_intents)
    if "transfer_to_rm" in s or "final_offer" in s or "manual_review" in s:
        return "transferred"
    if "end_call" in s:
        return "completed"
    from src.dispositions import RESOLUTION
    low = text.lower()
    if any(p.lower() in low for p in RESOLUTION["raised_request"]):
        return "raised_request"
    return "incomplete"


# ---------- public API ----------
def extract_call(path, drop_noise=True, bundle=None, use_model=True, vocab=None):
    path = Path(path)
    raw = _load_turns(path)
    merged = _merge_fragments(raw)
    turns_in = [t for t in merged if not _is_noise(t["text"])] if drop_noise else merged

    # Prefer the distilled student model (trained on Claude's labels); fall back to
    # the keyword/embedding rules if no model is present. Route by domain: JustDial
    # transcripts (LCS-* names) use the JustDial model, everything else the ABCL model.
    model_bases = None
    if use_model:
        try:
            from src import distill
            is_justdial = path.stem.startswith("LCS")
            model_path = distill.DOMAINS["justdial"]["model"] if is_justdial else distill.MODEL_PATH
            if model_path.exists():
                model_bases = distill.predict_bases(turns_in, model_path=model_path)
        except Exception:  # noqa: BLE001
            model_bases = None
    if model_bases is None and bundle is None:
        bundle = build_model_bundle()

    out_turns, bases = [], []
    for i, t in enumerate(turns_in):
        speaker, text = t["speaker"], t["text"]
        base = model_bases[i] if model_bases is not None else base_intent(text, bundle)
        bases.append(base)
        sentiment = detect_sentiment(text) if speaker == "customer" else None
        tool = tool_for(speaker, base, text)
        ents = _entities(text)
        out_turns.append({
            "index": i,
            "speaker": speaker,
            "type": "tool_call" if tool else "action",
            "intent": action_intent(speaker, base),
            "base_intent": base,
            "keywords": extract_keywords(text, base, sentiment or "neutral", ents, vocab),
            "sentiment": sentiment if sentiment and sentiment != "neutral" else None,
            "tool": tool,
            "text": text,
            "entities": ents,
        })
    return {
        "call_id": path.stem,   # full stem: unique (stem[:8] collided for LCS-* names)
        "language": "hi-en",
        "outcome": _outcome(bases, " ".join(t["text"] for t in turns_in)),
        "turns": out_turns,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python -m src.extract <transcript.json>")
        sys.exit(1)
    call = extract_call(sys.argv[1])
    print(f"call_id={call['call_id']}  outcome={call['outcome']}  turns={len(call['turns'])}\n")
    for t in call["turns"]:
        extra = []
        if t["sentiment"]:
            extra.append(f"sentiment={t['sentiment']}")
        if t["tool"]:
            extra.append(f"tool={t['tool']}")
        print(f"  {t['index']:>2} {t['intent']:<34} {' '.join(extra)}")
        print(f"       keywords: {', '.join(t['keywords'])}")
