"""Generic cross-client taxonomy — broad, domain-agnostic intent buckets.

Unlike src/extract.py (ABCL) and src/justdial_taxonomy.py (JustDial), this taxonomy
is NOT tied to one client's call flow. It exists to test whether a single distilled
local model can generalize across clients when trained on a diverse, multi-client
transcript set labeled against a small set of broad buckets, instead of one
fine-grained taxonomy per client.

Precedent for "broad beats fine" already lives in this repo: src/justdial_coarse.py
collapsed JustDial's 24-intent fine taxonomy into ~7 buckets after the fine model
only scored ~32% CV on noisy ASR. This module applies that lesson from the start,
across clients, rather than after the fact for one.

Same shape as extract.INTENT_LIBRARY / ACTIONS so it plugs into src/labeling.py and
src/distill.py unchanged. sentiment_lexicon is intentionally shared with ABCL/JustDial
(src/extract.SENTIMENT_LEXICON) — the emotional-signal words (fraud, frustrated,
confused ...) are themselves fairly client-agnostic.

How a new client enters this taxonomy:
  1. Drop that client's transcripts (plain-text Agent:/Customer: turns, same format
     src/transcribe.py produces) into data/generic_transcripts/, named
     GEN-<client>-<call_id>.txt so labeling.py's `owns` check routes them here
     instead of the ABCL or JustDial gold sets.
  2. python -m src.labeling emit generic     -> writes batches + LABELING_GUIDE.md
  3. Label each batch (Claude, offline/dev-time only — never in the production path)
  4. python -m src.labeling assemble generic -> merges into data/gold_generic/labels.jsonl
  5. python -m src.distill eval generic      -> grouped CV accuracy against gold
  6. python -m src.distill train generic     -> data/models/generic_clf.pkl

No taxonomy edits are needed per new client — that is the entire point of keeping
the bucket list broad and fixed.
"""
from __future__ import annotations

# (base_intent, keyword cues, example utterances) — deliberately broad, deliberately
# NOT tied to any one client's domain vocabulary (no loan/lead-gen specific terms here).
INTENT_LIBRARY = [
    ("greeting", ["hello", "नमस्ते", "namaste", "hi sir", "hi maam"],
     ["hello, sir?", "नमस्ते, मैं बोल रही हूँ"]),
    ("agree", ["हाँ", "जी", "theek hai", "बताइए", "ok karo", "proceed karo", "go ahead"],
     ["haan bolo", "theek hai bataiye", "जी करिए"]),
    ("disagree", ["नहीं चाहिए", "interested नहीं", "nahi chahiye", "not interested", "mat karo"],
     ["mujhe nahi chahiye", "interested nahi hoon abhi"]),
    ("ask_question", ["क्या", "कैसे", "कौन सा", "मतलब", "what", "how", "kya matlab"],
     ["ye kaise hoga", "iska matlab kya hai"]),
    ("answer_query", [],
     ["मैं आपको बताती हूँ", "let me explain that"]),
    ("confused_repeat", ["समझ नहीं", "फिर से बोलो", "repeat", "dobara bolo", "sorry?", "haan?"],
     ["samajh nahi aaya", "phir se boliye"]),
    ("callback_request", ["baad mein call", "abhi busy", "call back", "फुर्सत नहीं", "call later"],
     ["abhi busy hoon baad mein call karo", "thodi der baad call kijiye"]),
    ("person_unavailable", ["so rahe hain", "ghar pe nahi", "meeting mein", "abhi available nahi"],
     ["woh abhi ghar pe nahi hain", "meeting mein hain abhi"]),
    ("distrust_security", ["fraud", "scam", "धोखा", "फ्रॉड", "genuine hai kya", "bharosa nahi"],
     ["ye fraud toh nahi hai", "mujhe bharosa nahi ho raha"]),
    ("irate_frustrated", ["arre", "kab se", "बार बार", "itna time", "seedha bolo", "pareshan"],
     ["kab se sun raha hoon", "itna complicated kyun hai"]),
    ("wait_hold", ["एक मिनट", "रुकिए", "wait", "hold", "line पर रहिए"],
     ["ek minute wait kijiye", "line par rahiye please"]),
    ("acknowledge", [],
     ["जी ठीक है", "ok noted", "अच्छा"]),
    ("end_call", ["धन्यवाद", "thank you", "goodbye", "call end"],
     ["aapke time ke liye dhanyawaad", "thank you, goodbye"]),
]
INTENT_BY_NAME = {name: kws for name, kws, _ in INTENT_LIBRARY}

# base_intent -> action-oriented, actor-aware names (same convention as the other taxonomies)
ACTIONS = {
    "greeting": {"agent": "agent_greet", "customer": "customer_greet"},
    "agree": {"agent": "agent_confirm", "customer": "customer_agree"},
    "disagree": {"agent": "agent_acknowledge_decline", "customer": "customer_disagree"},
    "ask_question": {"agent": "agent_clarify", "customer": "customer_ask_question"},
    "answer_query": {"agent": "agent_answer_query", "customer": "customer_ask_query"},
    "confused_repeat": {"agent": "agent_ask_to_repeat", "customer": "customer_unclear"},
    "callback_request": {"agent": "agent_schedule_callback", "customer": "customer_request_callback"},
    "person_unavailable": {"agent": "agent_acknowledge_unavailable", "customer": "customer_report_unavailable"},
    "distrust_security": {"agent": "agent_reassure_trust", "customer": "customer_express_distrust"},
    "irate_frustrated": {"agent": "agent_de_escalate", "customer": "customer_express_frustration"},
    "wait_hold": {"agent": "agent_wait", "customer": "customer_request_wait"},
    "acknowledge": {"agent": "agent_acknowledge", "customer": "customer_acknowledge"},
    "end_call": {"agent": "agent_end_call", "customer": "customer_end"},
}

# plain-English description per action-intent (for intents.md glossary)
INTENT_DESC = {
    "agent_greet": "Agent's opening greeting", "customer_greet": "Customer's opening / picks up",
    "agent_confirm": "Agent confirms / agrees to proceed", "customer_agree": "Customer agrees to proceed",
    "agent_acknowledge_decline": "Agent acknowledges a decline/refusal", "customer_disagree": "Customer declines or is not interested",
    "agent_clarify": "Agent clarifies or re-explains", "customer_ask_question": "Customer asks a question",
    "agent_answer_query": "Agent answers the customer's question", "customer_ask_query": "Customer asks the agent a question",
    "agent_ask_to_repeat": "Agent asks the customer to repeat", "customer_unclear": "Customer's turn was unclear / asked to repeat",
    "agent_schedule_callback": "Agent offers/schedules a callback", "customer_request_callback": "Customer asks to be called back later",
    "agent_acknowledge_unavailable": "Agent acknowledges the right person isn't available",
    "customer_report_unavailable": "Customer reports the right person can't come to the phone",
    "agent_reassure_trust": "Agent reassures the customer it's genuine", "customer_express_distrust": "Customer suspects fraud/scam or has a security concern",
    "agent_de_escalate": "Agent tries to de-escalate an irate/frustrated customer", "customer_express_frustration": "Customer is irate, impatient, or frustrated",
    "agent_wait": "Agent asks the customer to wait / is checking", "customer_request_wait": "Customer asks the agent to hold on",
    "agent_acknowledge": "Agent acknowledgement / back-channel", "customer_acknowledge": "Customer acknowledgement / back-channel",
    "agent_end_call": "Agent closes the call", "customer_end": "Customer closes / ends the call",
}

# Deliberately empty: tool/API actions are wildly client-specific (SMS vs ticket vs
# email vs CRM push). A generic cross-client taxonomy should not assume any of them.
TOOL_RULES: dict = {}

# ---------------------------------------------------------------------------------
# Bootstrap mappings: recode ALREADY Claude-labeled ABCL/JustDial gold (data/gold,
# data/gold_justdial) straight into these broad buckets, with ZERO new Claude calls.
# Only fine intents with a clean, honest 1:1 semantic match are mapped — a fine intent
# that's really a client-specific procedural step (enter_pan, mobile_otp, raise_request,
# processing_fee ...) has no broad analog and is deliberately left OUT rather than
# forced into "other", which would just dilute that bucket. See src/generic_bootstrap.py.
#
# Known gap: neither ABCL nor JustDial's fine taxonomy captures disagree,
# callback_request, person_unavailable, or irate_frustrated as their OWN base_intent
# (irate-ish signal only exists as a customer *sentiment* in ABCL, not an intent) — so
# those 4 generic buckets get zero rows from this bootstrap. They need either a small
# targeted Claude pass over the existing transcripts, or a genuinely new client.
ABCL_FINE_TO_GENERIC = {
    "greeting": "greeting", "wait_hold": "wait_hold", "acknowledge": "acknowledge",
    "ask_question": "ask_question", "answer_query": "answer_query", "agree": "agree",
    "clarify_repeat": "confused_repeat", "end_call": "end_call",
    "reassure_trust": "distrust_security", "other": "other",
}
JUSTDIAL_FINE_TO_GENERIC = {
    "greeting": "greeting", "agree": "agree", "ask_question": "ask_question",
    "answer_query": "answer_query", "acknowledge": "acknowledge",
    "clarify_repeat": "confused_repeat", "wait_hold": "wait_hold",
    "end_call": "end_call", "other": "other",
}
