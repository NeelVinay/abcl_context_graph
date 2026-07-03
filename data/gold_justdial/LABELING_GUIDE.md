# Labeling guide — JustDial lead-generation support calls (Hinglish)

You are the TEACHER creating ground-truth labels. For EACH turn assign the single best `base_intent` from the list below, the signal `keywords` (verbatim spans copied from the turn text), the customer `sentiment`, and any `tool` call.

Rules:
- `base_intent` MUST be exactly one value from the list (or `other` if nothing fits — then add `suggested_intent` with a short new name).
- `keywords`: 1-5 short phrases COPIED VERBATIM from the turn text. No paraphrasing, no invented words, no names/PII, and NO number sequences (phone numbers, OTPs, spelled-out digits like 'नाइन डबल टू'). If nothing is salient, use [].
- `sentiment`: ONLY for customer turns, else null. One of: ['confused', 'distrustful', 'frustrated', 'happy', 'neutral', 'skeptical']. Use `neutral` if no clear emotion.
- `tool`: ONLY for agent turns where an actual system action is performed (not merely mentioned). One of: ['raise_ticket', 'transfer_team'] or null.
- Judge by MEANING and context, not keyword presence. The transcript is Hinglish (mixed Hindi/Devanagari + romanized English) and may have ASR errors.
- If a turn is unintelligible ASR garble (repeated/nonsensical tokens, no clear meaning), label `base_intent` = `other`, `keywords` = [], and move on — do NOT over-analyze it.

## Valid base intents (with example utterances)

- **greeting** (agent→`agent_greet`, customer→`customer_greet`)
    e.g. hello, sir? | नमस्ते, मैं JustDial से बोल रही हूँ
- **identify_business** (agent→`agent_identify_business`, customer→`customer_confirm_business`)
    e.g. क्या मैं ये business owner से बात कर रही हूँ? | आपका business कौन सा है?
- **ask_question** (agent→`agent_clarify`, customer→`customer_ask_question`)
    e.g. इसका मतलब क्या है? | ये कैसे होगा?
- **answer_query** (agent→`agent_answer_query`, customer→`customer_ask_query`)
    e.g. मैं आपको बताती हूँ | देखिए ऐसा है
- **acknowledge** (agent→`agent_acknowledge`, customer→`customer_acknowledge`)
    e.g. जी ठीक है | अच्छा | हम्म ओके
- **agree** (agent→`agent_confirm`, customer→`customer_agree`)
    e.g. हाँ बताइए | जी ठीक है करिए
- **wait_hold** (agent→`agent_wait`, customer→`customer_request_wait`)
    e.g. एक minute check कर रही हूँ | line पर रहिए
- **clarify_repeat** (agent→`agent_ask_to_repeat`, customer→`customer_unclear`)
    e.g. फिर से बताइए | समझ नहीं आया
- **end_call** (agent→`agent_end_call`, customer→`customer_end`)
    e.g. आपके time के लिए धन्यवाद | thank you, goodbye
- **report_no_leads** (agent→`agent_ack_no_leads`, customer→`customer_report_no_leads`)
    e.g. मुझे लीड नहीं आ रही है | एक भी customer नहीं मिला अभी तक
- **report_wrong_leads** (agent→`agent_ack_wrong_leads`, customer→`customer_report_wrong_leads`)
    e.g. जो inquiry आ रही है वो out of area है | leads गलत location की आ रही हैं
- **roi_complaint** (agent→`agent_ack_roi`, customer→`customer_roi_complaint`)
    e.g. इतने पैसे दिए पर कोई business नहीं मिला | 3 महीने हो गए काम नहीं आया
- **rating_review_issue** (agent→`agent_discuss_rating`, customer→`customer_report_rating_issue`)
    e.g. मेरी rating कम है | reviews की वजह से problem है
- **category_area_coverage** (agent→`agent_check_coverage`, customer→`customer_report_coverage_issue`)
    e.g. मेरी category सही नहीं है | ये area cover नहीं हो रहा
- **explain_lead_mechanics** (agent→`agent_explain_leads`, customer→`customer_ask_about_leads`)
    e.g. ये phone searches से आती है और वो targeted searches होती है | आपकी category और rating के हिसाब से leads का flow होता है
- **check_account** (agent→`agent_check_account`, customer→`customer_provide_info`)
    e.g. मैं आपका account check कर रहा हूँ | आपके contract में देखती हूँ
- **raise_request** (agent→`agent_raise_request`, customer→`customer_acknowledge`)
    e.g. मैं आपके लिए request raise कर देती हूँ | 24 hours में team देख लेगी
- **guide_customer_support** (agent→`agent_guide_support`, customer→`customer_acknowledge`)
    e.g. app में customer support option से ticket डालिए | वहाँ से concern raise करें
- **advise_improvement** (agent→`agent_advise_improvement`, customer→`customer_acknowledge`)
    e.g. photos upload कीजिए visibility के लिए | हर lead पर जल्दी respond कीजिए
- **request_rating** (agent→`agent_request_rating`, customer→`customer_react_rating`)
    e.g. call के बाद rating link आएगी, 10 दीजिएगा | मेरे call को 10 rating दीजिए
- **transfer_to_team** (agent→`agent_transfer_to_team`, customer→`customer_acknowledge_transfer`)
    e.g. मैं आपको concern team से connect कर रही हूँ | senior से बात करा देती हूँ
- **cancel_churn** (agent→`agent_handle_cancel`, customer→`customer_request_cancel`)
    e.g. मुझे ये service बंद करनी है | अब नहीं चाहिए cancel कर दो
- **technical_issue** (agent→`agent_handle_tech`, customer→`customer_report_tech_issue`)
    e.g. app नहीं चल रहा | login नहीं हो रहा error आ रहा है
- **renewal_upsell** (agent→`agent_pitch_renewal`, customer→`customer_react_renewal`)
    e.g. advance feature से आप business boost कर सकते हैं | package upgrade कर लीजिए

## Output format (per call): JSON
```json
{"call_id": "<id>", "turns": [
  {"index": 0, "speaker": "customer", "base_intent": "report_no_leads", "keywords": ["लीड नहीं आ"], "sentiment": "frustrated", "tool": null}
]}
```