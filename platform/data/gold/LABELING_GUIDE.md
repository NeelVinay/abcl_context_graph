# Labeling guide — ABCL loan-application calls (Hinglish)

You are the TEACHER creating ground-truth labels. For EACH turn assign the single best `base_intent` from the list below, the signal `keywords` (verbatim spans copied from the turn text — the words that reveal the intent), the customer `sentiment`, and any `tool` call.

Rules:
- `base_intent` MUST be exactly one value from the list (or `other` if nothing fits — then add `suggested_intent` with a short new name).
- `keywords`: 1-5 short phrases COPIED VERBATIM from the turn text. No paraphrasing, no invented words, no names/PII. If nothing is salient, use [].
- `sentiment`: ONLY for customer turns, else null. One of: ['confused', 'distrustful', 'frustrated', 'happy', 'neutral', 'skeptical']. Use `neutral` if no clear emotion.
- `tool`: ONLY for agent turns where an actual system action is performed (not merely mentioned). One of: ['push_to_crm', 'send_otp', 'send_sms', 'transfer_to_rm'] or null.
- Judge by MEANING and context, not keyword presence. The transcript is Hinglish (mixed Hindi/Devanagari + romanized English) and may have ASR errors.

## Valid base intents (with example utterances)

- **skip_udyam** (agent→`agent_offer_skip_udyam`, customer→`customer_skip_udyam`)
    e.g. skip anyway कर देता हूँ | नीचे skip option पर click कर दीजिए
- **udyam_verification** (agent→`agent_request_udyam`, customer→`customer_respond_udyam`)
    e.g. udyam number और registered mobile भरें | ये udyam verification page है
- **enter_pan** (agent→`agent_request_pan`, customer→`customer_provide_pan`)
    e.g. अपना PAN number भरें | PAN card number डाल दिया
- **mobile_otp** (agent→`agent_request_otp`, customer→`customer_do_otp`)
    e.g. mobile number डालकर get OTP करें | OTP डालकर verify कर दिया
- **enter_email** (agent→`agent_request_email`, customer→`customer_provide_email`)
    e.g. अपना email address दर्ज करें | email भर दिया
- **enter_income** (agent→`agent_request_income`, customer→`customer_provide_income`)
    e.g. net monthly income टाइप करें | मेरी monthly income इतनी है
- **organization_name** (agent→`agent_request_org_name`, customer→`customer_provide_org_name`)
    e.g. organization name के field में company का नाम enter करें | अपनी company या firm का नाम डालिए
- **business_details** (agent→`agent_request_business_details`, customer→`customer_provide_business_details`)
    e.g. business का नाम और address भरें | self employed हूँ अपना business है
- **employment_type** (agent→`agent_ask_employment_type`, customer→`customer_state_employment_type`)
    e.g. salaried या self employed चुनिए | मैं self employed हूँ
- **accept_terms** (agent→`agent_request_terms_accept`, customer→`customer_accept_terms`)
    e.g. terms and condition के box check करके proceed करें | दोनों box check कर दिए
- **click_apply** (agent→`agent_guide_apply`, customer→`customer_report_applied`)
    e.g. apply now button पर click करें | apply हो गया है
- **manual_review** (agent→`agent_inform_manual_review`, customer→`customer_acknowledge`)
    e.g. application manual review के लिए जाएगी
- **final_offer** (agent→`agent_present_final_offer`, customer→`customer_react_to_final_offer`)
    e.g. ये final offer page है, loan amount और tenure दिख रहा है
- **address_error** (agent→`agent_help_address_error`, customer→`customer_report_address_error`)
    e.g. address red में आ रहा है, हो नहीं रहा | error आ रहा है address में | extra space या slash हटा दीजिए
- **enter_address** (agent→`agent_request_address`, customer→`customer_provide_address`)
    e.g. अपना address आधार के अनुसार भरें | house number, building name, street भरिए | pincode डाल दीजिए
- **recording_disclosure** (agent→`agent_disclose_recording`, customer→`customer_acknowledge`)
    e.g. ये call training और quality purpose के लिए record हो रही है
- **present_offer** (agent→`agent_present_offer`, customer→`customer_react_to_offer`)
    e.g. आपके लिए pre approved personal loan offer है
- **send_sms_link** (agent→`agent_send_sms_link`, customer→`customer_report_sms_received`)
    e.g. मैं आपको SMS में link भेज रही हूँ | link मिल गया है
- **open_link** (agent→`agent_guide_open_link`, customer→`customer_report_link_opened`)
    e.g. link पर click करें website खुलेगी | site खुल गई है
- **personal_details** (agent→`agent_request_personal_details`, customer→`customer_provide_personal_details`)
    e.g. नाम, gender, date of birth भरें | ये basic details का page है
- **transfer_to_rm** (agent→`agent_transfer_to_rm`, customer→`customer_acknowledge_transfer`)
    e.g. अब मैं आपको relationship manager से connect कर रही हूँ | हाँ connect करो
- **end_call** (agent→`agent_end_call`, customer→`customer_acknowledge`)
    e.g. call end कर रही हूँ, goodbye | धन्यवाद, कॉल यहीं समाप्त करती हूँ
- **greeting** (agent→`agent_greet`, customer→`customer_greet`)
    e.g. नमस्ते, मैं प्रिया बोल रही हूँ | क्या मैं अमित जी से बात कर रही हूँ | hello हाँ जी
- **wait_hold** (agent→`agent_wait`, customer→`customer_request_wait`)
    e.g. एक second wait करिए please | मैं इंतज़ार कर रही हूँ
- **processing_fee** (agent→`agent_explain_fee`, customer→`customer_query_fee`)
    e.g. processing fee ₹2,950 deduct होगी | approximate EMI ₹5,150 बनेगी | interest rate ten point nine nine percent है
- **reassure_trust** (agent→`agent_reassure_trust`, customer→`customer_express_distrust`)
    e.g. क्या ये कोई fraud तो नहीं है | नहीं, ये बिल्कुल genuine है, आप निश्चिंत रहें
- **clarify_repeat** (agent→`agent_ask_to_repeat`, customer→`customer_unclear`)
    e.g. माफ़ कीजिए, क्या आप फिर से कहेंगे? | थोड़ा साफ़ बोलेंगे?
- **ask_question** (agent→`agent_clarify`, customer→`customer_ask_question`)
    e.g. locality का मतलब क्या है | इसमें क्या भरना है
- **answer_query** (agent→`agent_answer_query`, customer→`customer_ask_query`)
    e.g. interest rate के बारे में बता दीजिए | मैं आपको समझा देती हूँ | आपका सवाल समझ गई
- **agree** (agent→`agent_confirm`, customer→`customer_agree`)
    e.g. जी आप शुरू कर सकते हैं | हाँ आगे बढ़िए
- **report_done** (agent→`agent_confirm_step`, customer→`customer_report_done`)
    e.g. हो गया | भर दिया है | कर दिया
- **acknowledge** (agent→`agent_acknowledge`, customer→`customer_acknowledge`)
    e.g. जी ठीक है | अच्छा | हम्म ठीक है

## Output format (per call): JSON
```json
{"call_id": "<id>", "turns": [
  {"index": 0, "speaker": "customer", "base_intent": "greeting", "keywords": ["hello"], "sentiment": "neutral", "tool": null},
  {"index": 1, "speaker": "agent", "base_intent": "send_sms_link", "keywords": ["sms", "link", "भेज"], "sentiment": null, "tool": "send_sms"}
]}
```