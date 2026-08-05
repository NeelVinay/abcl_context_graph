"""Phase A: map fine action-intents -> a small set of coarse FLOW STAGES.

The per-turn intents (~30 of them) are too granular to make a readable tree, so for the
top-to-bottom flow view we collapse them into ~10 stages. The fine intents are still used
everywhere else (report.md, glossary); only the flow tree uses this abstraction.

Keyed by BASE intent (speaker-agnostic) — a question is the same stage whether the agent
or customer is speaking.
"""
from __future__ import annotations

# base_intent -> stage
STAGE_OF = {
    "greeting": "open",
    "recording_disclosure": "disclose",
    # offer / terms / fees
    "present_offer": "offer",
    "final_offer": "offer",
    "processing_fee": "offer",
    "accept_terms": "offer",
    # questions & answers
    "answer_query": "qa",
    "ask_question": "qa",
    # trust / objections
    "reassure_trust": "objection",
    # application flow (everything that's filling the form / driving the journey)
    "send_sms_link": "application",
    "open_link": "application",
    "click_apply": "application",
    "mobile_otp": "application",
    "enter_pan": "application",
    "personal_details": "application",
    "enter_email": "application",
    "enter_address": "application",
    "address_error": "application",
    "employment_type": "application",
    "enter_income": "application",
    "business_details": "application",
    "organization_name": "application",
    "udyam_verification": "application",
    "skip_udyam": "application",
    # friction (waiting / repeating / clarifying)
    "wait_hold": "wait",
    "clarify_repeat": "wait",
    # routing
    "transfer_to_rm": "transfer",
    "manual_review": "transfer",
    # close
    "end_call": "close",
    # low-signal back-channel — dropped from traces (see DROP_STAGES)
    "agree": "ack",
    "report_done": "ack",
    "acknowledge": "ack",
    # --- JustDial COARSE buckets (justdial_clf.pkl) -> their own stages ---
    "complaint": "jd_complaint",
    "agent_handle": "jd_handle",
    "resolution": "jd_resolution",
    "question": "qa",
    "open": "open",
    "backchannel": "ack",
    # --- generic cross-client taxonomy (src/generic_taxonomy.py) buckets that don't
    # already share a name with an ABCL/JustDial fine intent above. Without these, a
    # turn labeled e.g. "irate_frustrated" falls through to "other" -> DROP_STAGES,
    # silently vanishing from the tree — exactly the signal an exec chart most needs.
    "irate_frustrated": "frustration",
    "disagree": "decline",
    "distrust_security": "objection",     # same trust/objection stage as reassure_trust
    "confused_repeat": "wait",            # same wait/clarify stage as clarify_repeat
    "callback_request": "callback",
    "person_unavailable": "unavailable",
}

# stages filtered out of the trace entirely: pure back-channel ("ack") and unclassified
# model-uncertainty turns ("other") — both add noise/branches without flow meaning.
DROP_STAGES = {"ack", "other"}

# human-friendly labels for rendering
STAGE_LABEL = {
    "open": "Greeting",
    "disclose": "Recording disclosure",
    "offer": "Offer / terms / fees",
    "qa": "Questions & answers",
    "objection": "Trust / objection",
    "application": "Application steps",
    "wait": "Wait / clarify",
    "transfer": "Transfer to RM",
    "close": "Call close",
    "other": "Other",
    # JustDial coarse stages
    "jd_complaint": "Customer complaint",
    "jd_handle": "Agent investigates / explains",
    "jd_resolution": "Raise request / transfer",
    # generic cross-client stages
    "frustration": "Frustration / escalation",
    "decline": "Decline / refusal",
    "callback": "Callback requested",
    "unavailable": "Person unavailable",
}


def stage_of(base_intent: str | None) -> str:
    return STAGE_OF.get(base_intent or "", "other")
