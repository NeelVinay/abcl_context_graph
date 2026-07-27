# ABCL Call Context-Graph Report

Calls analyzed: **116** · intents: **59** · transitions: **569**
_(counts are per-turn occurrences across all calls, not number of calls)_

## 1. Keywords by intent (the signal words)

- **customer_greet** (191x): hello, से बात, बोलिए, बोला, बोलो, loan
- **agent_greet** (147x): नमस्ते, बात कर रही, से बात, आदित्य, बोल, समझ
- **customer_agree** (109x): phone, बोलिए, ऐसे, busy, शुरू कर, शुरू
- **customer_ask_question** (109x): reason, काम, loan, करनी, approval, issue
- **customer_acknowledge** (106x): thank, record, call, available, message, person
- **customer_other** (94x): भैया, अरे, हिंदी, कैसे, आदित्य, बोल
- **agent_wait** (81x): इंतज़ार, wait, कृपया, otp, बताएं, जाए
- **agent_answer_query** (79x): loan, offer, शुरू, application, process, sorry
- **agent_guide_open_link** (78x): link, sms, click, process, जिसमें, try
- **agent_send_sms_link** (76x): sms, application, link, click, process, शुरू
- **agent_request_otp** (71x): otp, click, check, number, mobile, बताएं
- **agent_present_offer** (68x): pre-approved, loan offer, loan, approved, offer, आदित्य
- **agent_ask_to_repeat** (64x): there, still, बोल, कीजिए, माफ़, फिर से कह
- **customer_do_otp** (48x): sms, number, mobile, डाल, otp, best
- **agent_acknowledge** (44x): call, धन्यवाद, समझ, समय, उपलब्ध, sure
- **agent_guide_apply** (41x): apply now, apply, click, now, screen, button
- **agent_other** (39x): कृपया, समय, बताएं, time, available, ज़रूर
- **customer_report_done** (36x): already, रखा, कर दिया, कैसे, button, proceed
- **customer_request_wait** (35x): call, कृपया, line, hold, रखा, callback
- **agent_end_call** (33x): thank, goodbye, application, time, already, समझ
- **customer_query_fee** (31x): interest, कितना, उसको, offer, check, पूरा
- **agent_explain_fee** (30x): interest rate, आदित्य, कैपिटल, बिरला, offer, शुरू
- **customer_report_address_error** (29x): phone, चार, internet, इधर, problem, आगे
- **customer_report_sms_received** (24x): link भेज, link, भेज, समय, इतना, sms
- **customer_report_link_opened** (21x): नहीं हो रहा, नहीं हो, open, choose, app, link
- **agent_request_pan** (20x): पैन, number, बताएं, page, जाए, fill
- **agent_request_personal_details** (20x): gender, date of birth, marital, enter, बताएं, page
- **customer_react_to_offer** (13x): लाख, पांच, loan, बोलिए, इतना, चुका
- **agent_reassure_trust** (13x): call, connect, sorry, sms, capital, aditya
- **agent_present_final_offer** (13x): loan, offer, मदद, समझ, चाहेंगे, final offer
- **customer_react_to_final_offer** (13x): दिखा, lakh, one, thousand, fifty, loan
- **customer_express_distrust** (12x): fraud, आदित्य, बोल, बिरला, हमको, लाख
- **customer_respond_udyam** (11x): fill, form, किधर, process, उद्यम, number
- **customer_unclear** (10x): call, minute, उसको, बोलिए, four, बोलते
- **agent_transfer_to_rm** (10x): relationship manager, help, सही, relationship, manager, मदद
- **customer_skip_udyam** (9x): call, loan, number, ध्यान, phone, हमको
- **agent_request_terms_accept** (9x): click, button, बताएं, जाए, proceed, terms and condition
- **agent_confirm** (8x): शुरू कर, शुरू, मदद, ज़रूर, कृपया, पूरा
- **agent_request_email** (8x): email, enter, बताएं, जाए, personal, मदद
- **customer_report_applied** (6x): apply now, apply, now, click, button, रहो
- **customer_provide_pan** (6x): pan, number, mobile, enter, name, कैसे
- **agent_help_address_error** (6x): कृपया, button, proceed, refresh, देखें, sorry
- **agent_request_address** (6x): address, pincode, locality, building, house number, fill
- **agent_request_udyam** (6x): udyam, number, mobile, enter, page, उद्यम
- **customer_state_employment_type** (4x): job, self employ, employed, self, दूसरा, professional
- **agent_clarify** (4x): details, fill, मदद, आगे, चाहते, बढ़ना
- **agent_ask_employment_type** (4x): salaried, self-employ, loan, offer, page, समझ
- **agent_request_business_details** (3x): बताएं, जाए, fill, address, pincode, business
- **customer_provide_business_details** (3x): company, business, उनको
- **agent_request_org_name** (2x): call, connect, sorry, enter, बताएं, जाए
- **customer_provide_address** (2x): apply
- **customer_ask_query** (2x): कैसे, loan, मिलेगा, पंद्रह, जानकारी, सिर्फ़
- **customer_provide_org_name** (1x): personal, company, reject
- **customer_provide_email** (1x): email, registered
- **customer_provide_personal_details** (1x): fill, detail
- **agent_request_income** (1x): income, बताएं, जाए, fill, net
- **agent_offer_skip_udyam** (1x): number, there, sure, assist, anything

## 2. Customer sentiment by intent

- **customer_agree**: happy:1
- **customer_ask_question**: frustrated:2 · confused:2
- **customer_other**: frustrated:6 · confused:1
- **customer_report_done**: confused:1 · frustrated:1
- **customer_query_fee**: confused:1
- **customer_report_address_error**: frustrated:8
- **customer_report_link_opened**: frustrated:2
- **customer_react_to_final_offer**: frustrated:1
- **customer_express_distrust**: distrustful:1
- **customer_provide_pan**: confused:1
- **customer_ask_query**: confused:1

## 3. Tool / API calls detected

_Inferred from the agent's words (a proxy, not real tool logs). Count = turns where the tool actually fired._

- **send_sms** ← `agent_send_sms_link` (62x)
- **send_otp** ← `agent_request_otp` (49x)
- **transfer_to_rm** ← `agent_transfer_to_rm` (10x)
