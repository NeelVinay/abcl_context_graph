"""JustDial (lead-generation / business-listing support) taxonomy.

Parallel to the ABCL loan taxonomy in src/extract.py, but for the JustDial domain:
support/retention calls where a business owner complains about the leads they get
(or don't get) and the agent investigates, explains, raises a request, and retains.

Same shape as extract.INTENT_LIBRARY / ACTIONS so it plugs into the labeling +
distillation machinery. Derived from the leads_mp3_data transcripts.
"""
from __future__ import annotations

# (base_intent, keyword cues, example utterances) — mined from the transcripts
INTENT_LIBRARY = [
    # --- generic / conversational (shared shape with ABCL) ---
    ("greeting", ["hello", "नमस्ते", "namaste"],
     ["hello, sir?", "नमस्ते, मैं JustDial से बोल रही हूँ"]),
    ("identify_business", ["business", "बिजनेस", "firm", "आपका नाम"],
     ["क्या मैं ये business owner से बात कर रही हूँ?", "आपका business कौन सा है?"]),
    ("ask_question", ["क्या", "कैसे", "कौन सा", "मतलब"],
     ["इसका मतलब क्या है?", "ये कैसे होगा?"]),
    ("answer_query", [],
     ["मैं आपको बताती हूँ", "देखिए ऐसा है"]),
    ("acknowledge", [],
     ["जी ठीक है", "अच्छा", "हम्म ओके"]),
    ("agree", ["ठीक है", "हाँ", "जी", "बताइए"],
     ["हाँ बताइए", "जी ठीक है करिए"]),
    ("wait_hold", ["एक मिनट", "रुकिए", "wait", "hold", "line पर"],
     ["एक minute check कर रही हूँ", "line पर रहिए"]),
    ("clarify_repeat", ["फिर से", "समझ नहीं", "दोबारा", "repeat"],
     ["फिर से बताइए", "समझ नहीं आया"]),
    ("end_call", ["धन्यवाद", "thank you", "goodbye", "बात करने के लिए"],
     ["आपके time के लिए धन्यवाद", "thank you, goodbye"]),
    # --- JustDial domain: the customer's complaint ---
    ("report_no_leads", ["लीड नहीं आ", "inquiry नहीं", "customer नहीं मिल", "rate नहीं आ",
                         "लीड नहीं मिल", "एक भी"],
     ["मुझे लीड नहीं आ रही है", "एक भी customer नहीं मिला अभी तक"]),
    ("report_wrong_leads", ["out of area", "out of city", "गलत area", "दूसरी city",
                            "रॉंग", "location गलत"],
     ["जो inquiry आ रही है वो out of area है", "leads गलत location की आ रही हैं"]),
    ("roi_complaint", ["पैसा", "रुपए", "काम नहीं आया", "business नहीं", "फायदा नहीं",
                       "conversion नहीं", "refund", "महीना हो गया"],
     ["इतने पैसे दिए पर कोई business नहीं मिला", "3 महीने हो गए काम नहीं आया"]),
    ("rating_review_issue", ["rating", "रेटिंग", "review", "रिव्यू", "feedback", "score"],
     ["मेरी rating कम है", "reviews की वजह से problem है"]),
    ("category_area_coverage", ["category", "कैटेगरी", "area", "एरिया", "pincode", "route"],
     ["मेरी category सही नहीं है", "ये area cover नहीं हो रहा"]),
    # --- JustDial domain: the agent's handling ---
    ("explain_lead_mechanics", ["phone search", "targeted search", "google", "route",
                                "profile", "filter", "flow"],
     ["ये phone searches से आती है और वो targeted searches होती है",
      "आपकी category और rating के हिसाब से leads का flow होता है"]),
    ("check_account", ["check कर", "देख रहा हूँ", "contract check", "profile देख"],
     ["मैं आपका account check कर रहा हूँ", "आपके contract में देखती हूँ"]),
    ("raise_request", ["request डाल", "raise", "ticket", "24 hour", "highlight",
                       "change कर", "mention कर"],
     ["मैं आपके लिए request raise कर देती हूँ", "24 hours में team देख लेगी"]),
    ("guide_customer_support", ["customer support", "app से", "ticket डाल", "concern raise"],
     ["app में customer support option से ticket डालिए", "वहाँ से concern raise करें"]),
    ("advise_improvement", ["rating दीजिए", "photo upload", "review", "visibility",
                            "respond", "feedback दे"],
     ["photos upload कीजिए visibility के लिए", "हर lead पर जल्दी respond कीजिए"]),
    ("request_rating", ["rating link", "10 highest", "call को rating", "rating दीजे"],
     ["call के बाद rating link आएगी, 10 दीजिएगा", "मेरे call को 10 rating दीजिए"]),
    ("transfer_to_team", ["team", "टीम", "senior", "concern team", "department"],
     ["मैं आपको concern team से connect कर रही हूँ", "senior से बात करा देती हूँ"]),
    ("cancel_churn", ["बंद कर", "cancel", "नहीं चाहिए", "deactivate"],
     ["मुझे ये service बंद करनी है", "अब नहीं चाहिए cancel कर दो"]),
    ("technical_issue", ["app नहीं", "login", "error", "नहीं चल", "नहीं खुल"],
     ["app नहीं चल रहा", "login नहीं हो रहा error आ रहा है"]),
    ("renewal_upsell", ["advance feature", "boost", "promote", "renew", "upgrade", "package"],
     ["advance feature से आप business boost कर सकते हैं", "package upgrade कर लीजिए"]),
]

# base_intent -> action-oriented, actor-aware names
ACTIONS = {
    "greeting": {"agent": "agent_greet", "customer": "customer_greet"},
    "identify_business": {"agent": "agent_identify_business", "customer": "customer_confirm_business"},
    "ask_question": {"agent": "agent_clarify", "customer": "customer_ask_question"},
    "answer_query": {"agent": "agent_answer_query", "customer": "customer_ask_query"},
    "acknowledge": {"agent": "agent_acknowledge", "customer": "customer_acknowledge"},
    "agree": {"agent": "agent_confirm", "customer": "customer_agree"},
    "wait_hold": {"agent": "agent_wait", "customer": "customer_request_wait"},
    "clarify_repeat": {"agent": "agent_ask_to_repeat", "customer": "customer_unclear"},
    "end_call": {"agent": "agent_end_call", "customer": "customer_end"},
    "report_no_leads": {"agent": "agent_ack_no_leads", "customer": "customer_report_no_leads"},
    "report_wrong_leads": {"agent": "agent_ack_wrong_leads", "customer": "customer_report_wrong_leads"},
    "roi_complaint": {"agent": "agent_ack_roi", "customer": "customer_roi_complaint"},
    "rating_review_issue": {"agent": "agent_discuss_rating", "customer": "customer_report_rating_issue"},
    "category_area_coverage": {"agent": "agent_check_coverage", "customer": "customer_report_coverage_issue"},
    "explain_lead_mechanics": {"agent": "agent_explain_leads", "customer": "customer_ask_about_leads"},
    "check_account": {"agent": "agent_check_account", "customer": "customer_provide_info"},
    "raise_request": {"agent": "agent_raise_request", "customer": "customer_acknowledge"},
    "guide_customer_support": {"agent": "agent_guide_support", "customer": "customer_acknowledge"},
    "advise_improvement": {"agent": "agent_advise_improvement", "customer": "customer_acknowledge"},
    "request_rating": {"agent": "agent_request_rating", "customer": "customer_react_rating"},
    "transfer_to_team": {"agent": "agent_transfer_to_team", "customer": "customer_acknowledge_transfer"},
    "cancel_churn": {"agent": "agent_handle_cancel", "customer": "customer_request_cancel"},
    "technical_issue": {"agent": "agent_handle_tech", "customer": "customer_report_tech_issue"},
    "renewal_upsell": {"agent": "agent_pitch_renewal", "customer": "customer_react_renewal"},
}

# tool/API actions inferred from agent speech (intent-coupled, verb-gated) — minimal for JD
TOOL_RULES = {
    "raise_request":    ("raise_ticket",  ["request डाल", "raise", "ticket", "mention कर"]),
    "transfer_to_team": ("transfer_team", []),
}
