"""Coarse JustDial intent buckets.

The fine 24-intent taxonomy scored ~32% CV on the noisy JustDial ASR — too many small,
semantically-overlapping classes on low-quality text. This collapses them into a handful
of well-separated buckets that the model can actually distinguish. Applied to the existing
gold labels (no re-labeling): fine base_intent -> coarse bucket.
"""
from __future__ import annotations

FINE_TO_COARSE = {
    # customer states a lead/ROI/service complaint (the core reason for the call)
    "report_no_leads": "complaint",
    "report_wrong_leads": "complaint",
    "roi_complaint": "complaint",
    "rating_review_issue": "complaint",
    "category_area_coverage": "complaint",
    "technical_issue": "complaint",
    "cancel_churn": "complaint",
    # agent investigates / explains / advises / pitches (agent's substantive handling)
    "check_account": "agent_handle",
    "explain_lead_mechanics": "agent_handle",
    "advise_improvement": "agent_handle",
    "guide_customer_support": "agent_handle",
    "renewal_upsell": "agent_handle",
    "answer_query": "agent_handle",
    # agent logs a request / hands off (resolution actions)
    "raise_request": "resolution",
    "transfer_to_team": "resolution",
    "request_rating": "resolution",
    # questions
    "ask_question": "question",
    # openings / identity
    "greeting": "open",
    "identify_business": "open",
    # short back-channel / procedural
    "acknowledge": "backchannel",
    "agree": "backchannel",
    "wait_hold": "backchannel",
    "clarify_repeat": "backchannel",
    "end_call": "backchannel",
    # unintelligible
    "other": "other",
}

COARSE_LABEL = {
    "complaint": "Customer complaint (leads / ROI / rating / coverage / cancel)",
    "agent_handle": "Agent investigates / explains / advises",
    "resolution": "Agent raises request / transfers / asks rating",
    "question": "Customer asks a question",
    "open": "Greeting / identify business",
    "backchannel": "Acknowledge / agree / wait / repeat / close",
    "other": "Unintelligible ASR",
}

# coarse base -> readable, actor-aware action-intent names (parallel to extract.ACTIONS)
ACTIONS = {
    "complaint": {"agent": "agent_acknowledge_complaint", "customer": "customer_complaint"},
    "agent_handle": {"agent": "agent_investigate_explain", "customer": "customer_respond"},
    "resolution": {"agent": "agent_raise_request", "customer": "customer_acknowledge"},
    "question": {"agent": "agent_ask", "customer": "customer_ask_question"},
    "open": {"agent": "agent_greet", "customer": "customer_greet"},
    "backchannel": {"agent": "agent_acknowledge", "customer": "customer_acknowledge"},
    "other": {"agent": "agent_other", "customer": "customer_other"},
}


# readable, plain-English description per action-intent name (for intents.md)
INTENT_DESC = {
    "customer_complaint": "Customer raises a problem — leads not coming, wrong/irrelevant leads, no ROI, low rating, coverage, or wants to cancel",
    "agent_acknowledge_complaint": "Agent acknowledges the customer's complaint before addressing it",
    "agent_investigate_explain": "Agent checks the account and explains how leads/ratings/category work, or advises improvements",
    "customer_respond": "Customer responds to the agent's explanation or questions",
    "agent_raise_request": "Agent logs a request/ticket, promises follow-up, or transfers to a team",
    "customer_ask_question": "Customer asks a question",
    "agent_ask": "Agent asks the customer a question to investigate",
    "agent_greet": "Agent's opening / identifies the business",
    "customer_greet": "Customer's opening / confirms who they are",
    "agent_acknowledge": "Agent acknowledgement / back-channel (ok, achha, noted)",
    "customer_acknowledge": "Customer acknowledgement / agreement / back-channel",
    "agent_other": "Agent turn with no clear intent (often unintelligible ASR)",
    "customer_other": "Customer turn with no clear intent (often unintelligible ASR)",
}


def coarsen(base_intent: str) -> str:
    return FINE_TO_COARSE.get(base_intent, "other")
