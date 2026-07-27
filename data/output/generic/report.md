# ABCL Call Context-Graph Report

Calls analyzed: **52** · intents: **48** · transitions: **316**
_(counts are per-turn occurrences across all calls, not number of calls)_

## 1. Keywords by intent (the signal words)

- **agent_answer_query** (199x): order, deliver, समझ, कोशिश, मिल, मदद
- **customer_ask_question** (168x): shipping, product, actually, order, deliver, july
- **customer_other** (125x): कोशिश, details, दिख, कीजिए, पहुंच, order
- **agent_acknowledge** (113x): order, deliver, समझ, मदद, कोशिश, call
- **customer_acknowledge** (74x): deliver, issue, जाए, जल्दी, thank you so much, thank
- **agent_greet** (57x): नमस्ते, assistant, मिंत्रा, service, welcome, मदद
- **agent_wait** (43x): order, समझ, line, status, check, delivery
- **customer_agree** (43x): दिक्कत, way, thank, sure, बिल्कुल, धन्यवाद
- **agent_transfer_to_rm** (43x): line, कृपया, रहिए, बने, agent, call
- **agent_ask_to_repeat** (41x): फिर से कह, कीजिये, माफ़, माफ़, फिर से बता, समझ
- **agent_request_pan** (29x): order, deliver, delivery, priority, देख, समझ
- **agent_clarify** (28x): मदद, नमस्ते, order, चाहते, issue, किस
- **customer_greet** (26x): hello, नमस्ते, हिंदी, connect, customer, any
- **customer_express_distrust** (21x): app, time, दिखा, shipping, चुका, मदद
- **customer_ask_query** (18x): order, पूछना, नहीं हो, मिंत्रा, deliver, delivery
- **agent_reassure_trust** (15x): order, deliver, कोशिश, पूरी, priority, मदद
- **agent_other** (14x): deliver, समझ, status, delivery, shipped, लगा
- **agent_end_call** (12x): call, मदद, सही, मिलेगा, form, मिंत्रा
- **agent_confirm** (10x): कृपया, चाह, निश्चिंत, रहें, बिल्कुल, मीरा
- **agent_help_address_error** (10x): delivery, problem, related, return, red, order
- **customer_request_wait** (9x): जल्दी, देखो, इसको, ऐसे, जल्द, बजे
- **agent_request_org_name** (9x): help, call, मदद, सही, बेहतर, agent
- **customer_query_fee** (9x): actually, exchange, four, five, seven, three
- **customer_report_done** (9x): got, show, four, nine, twelve, three
- **customer_report_address_error** (8x): emergency, call, complaint, पांच, raise, order
- **agent_present_offer** (7x): order, deliver, समझ, status, कोशिश, let
- **agent_request_terms_accept** (7x): order, line, check, कृपया, रहिए, list
- **agent_send_sms_link** (6x): order, deliver, समझ, shipped, मिल, status
- **customer_provide_pan** (6x): order, receive, मिला, exchange, कुर्ता, नहीं हो रहा
- **customer_unclear** (5x): deliver, status, twenty, update, fourth, july
- **agent_request_address** (4x): order, deliver, मदद, priority, location, flat
- **customer_provide_address** (3x): order, registered, want, place, where, location
- **agent_present_final_offer** (3x): order, delivery, out, निश्चिंत, रहें, deliver
- **customer_react_to_final_offer** (3x): five, one, three, deliver, पूरे, नहीं हो
- **agent_request_business_details** (2x): order, मदद, shipped, मिल, बजे, deliver
- **customer_do_otp** (2x): मिलेगा, number, call, जाए, निकल, उनको
- **customer_report_link_opened** (2x): मीरा, shoes, ordered, class, order
- **customer_respond_udyam** (2x): मिल, agent, number, location, पता
- **customer_skip_udyam** (1x): cancel, मिला, दूंगा
- **customer_react_to_offer** (1x): बजे, ऐसा, possible
- **customer_provide_org_name** (1x): —
- **customer_acknowledge_transfer** (1x): time, इतना, लगता
- **agent_request_udyam** (1x): assistant, order, delivery, agent, contact
- **agent_inform_manual_review** (1x): order, deliver, समझ, check, कोशिश
- **agent_disclose_recording** (1x): समझ, urgency, double
- **customer_state_employment_type** (1x): काम

## 2. Customer sentiment by intent

- **customer_ask_question**: frustrated:14 · confused:4
- **customer_other**: frustrated:4 · happy:1
- **customer_acknowledge**: happy:1
- **customer_express_distrust**: frustrated:1 · confused:1
- **customer_ask_query**: frustrated:2
- **customer_report_address_error**: confused:1
- **customer_provide_pan**: frustrated:1 · distrustful:1
- **customer_react_to_final_offer**: frustrated:1

## 3. Tool / API calls detected

_Inferred from the agent's words (a proxy, not real tool logs). Count = turns where the tool actually fired._

- **transfer_to_rm** ← `agent_transfer_to_rm` (43x)
- **push_to_crm** ← `agent_inform_manual_review` (1x)
