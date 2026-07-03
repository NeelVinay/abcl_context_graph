# ABCL Call Context-Graph Report

Calls analyzed: **113** · intents: **65** · transitions: **987**
_(counts are per-turn occurrences across all calls, not number of calls)_

## 1. Keywords by intent (the signal words)

- **customer_report_done** (502x): कर दिया, complete, click, लिख, हो गया, right
- **agent_request_otp** (370x): otp, करें।, number, get, terms, verify
- **customer_acknowledge** (301x): बोलने, पढ़ते, loan, application, check, देर
- **agent_wait** (256x): मदद, आगे, समझ, दिक्कत, लिए।, लिंक
- **customer_agree** (249x): बोलिए, देखते, रहो, बोलो, आगे बढ़, आगे
- **customer_ask_question** (233x): बोलिए, air, person, real, bot, कब तक
- **agent_greet** (219x): hello, नमस्ते, बात कर रही, से बात, बोल, capital
- **agent_ask_to_repeat** (216x): फिर से कह, कीजिए, माफ़, फिर से बता, कृपया, कहेंगे
- **customer_greet** (214x): hello, बोलिए, आवाज़, बोलो, detail, बात कर रही
- **agent_transfer_to_rm** (204x): relationship manager, loan, offer, amount, हूँ।, करें।
- **agent_send_sms_link** (182x): sms, लिंक भेज, हूँ।, मदद, application, apply
- **agent_guide_open_link** (178x): खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं, करें।
- **agent_guide_apply** (170x): apply now, apply, करें।, now, देख, कृपया
- **customer_request_wait** (160x): काम, इधर, work, minute, open, एक second
- **agent_present_final_offer** (143x): final offer, loan, offer, amount, final, करें।
- **customer_do_otp** (140x): otp, verification, number, डाल, भेजा, भेजो
- **agent_request_address** (134x): address, pincode, locality, building, house number, flat
- **agent_request_email** (126x): email, बताएं।, जाए, personal, enter, कृपया
- **agent_answer_query** (124x): बोल, हूँ।, तरफ, आदित्य, बिरला, capital
- **customer_react_to_final_offer** (119x): loan, दिखा, उसमें, pay, lakh, two
- **agent_request_pan** (113x): पैन, page, number, बताएं।, जाए, कृपया
- **agent_ask_employment_type** (113x): salaried, self-employ, loan, offer, page, monthly
- **agent_request_terms_accept** (111x): terms and condition, terms, करें।, button, check, details
- **agent_request_personal_details** (110x): gender, date of birth, marital, करें।, बताएं।, कृपया
- **customer_other** (108x): kyc, चुका, करिए, normal, one, six
- **customer_query_fee** (83x): interest rate, interest, rate, कितना, point, दिखा
- **customer_report_link_opened** (77x): click, खुल गया, खुल, link, loan, number
- **agent_request_org_name** (76x): बताएं।, जाए, enter, registered, business, कृपया
- **agent_request_income** (74x): income, fill, monthly, self, net, बताएं।
- **customer_state_employment_type** (67x): self employ, self, employed, salaried, भाई, self employee
- **agent_request_business_details** (67x): business, बताएं।, जाए, enter, address, fill
- **customer_report_sms_received** (60x): message, whatsapp, दूसरा, भेज, connect, बोलिए
- **agent_acknowledge** (51x): करें।, process, complete, चाहें, मदद, बताइए।
- **agent_present_offer** (48x): pre-approved, loan offer, loan, offer, approved, amount
- **customer_provide_pan** (47x): pan, number, second, डाल, card, दूं
- **agent_explain_fee** (47x): processing fee, process, details, professional, समझ, interest rate
- **customer_report_address_error** (40x): number, building, code, pin, out, proceed
- **agent_request_udyam** (38x): udyam, करें।, page, number, mobile, details
- **customer_provide_address** (36x): house number, number, house, मांग, address, typing
- **customer_respond_udyam** (32x): उद्यम, number, registered, card, उससे, इंतज़ार
- **customer_express_distrust** (30x): process, complete, phone, person, real, बोल
- **customer_report_applied** (30x): click, login, apply, apply now, now, देख
- **agent_help_address_error** (30x): करें।, name, building, सही, चेक, दिक्कत
- **agent_end_call** (27x): हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त, call
- **agent_reassure_trust** (27x): sms, कृपया, तरफ, आगे, capital, हूँ।
- **agent_offer_skip_udyam** (25x): skip, number, बताएं।, जाए, click, application
- **customer_provide_personal_details** (24x): details, professional, number, mobile, enter, name
- **agent_other** (23x): call, relationship, manager, दूँ, नहीं।, chd
- **customer_react_to_offer** (23x): lakh, one, thousand, loan, amount, मिल
- **agent_confirm** (21x): apply, हूँ।, आगे, तैयार, guide, मदद
- **customer_provide_org_name** (21x): नहीं हो रहा, नहीं हो, name, option, उसमें, line
- **customer_provide_email** (20x): email, डाल, मांग, दूं, mail, डालना
- **customer_skip_udyam** (18x): number, एकदम, नहीं हो, उसमें, cancel, problem
- **agent_clarify** (16x): कृपया, आगे, बताएं, होगा।, खुल, submit
- **customer_ask_query** (16x): लाख, बोलिए, मिलेगा, पंद्रह, लेकर, साल
- **customer_unclear** (13x): बोल, sorry, आवाज़, बीस, सात, two
- **customer_provide_business_details** (12x): business, name, company, team, number, बोलो
- **customer_accept_terms** (11x): proceed, दोनों, बोलिए, check, दिए, click
- **customer_provide_income** (9x): income, monthly, लाख, self, type, net
- **agent_inform_manual_review** (6x): application, process, check, सही, देर, complete
- **agent_disclose_recording** (6x): record, training, quality, call, तरफ, loan
- **customer_acknowledge_transfer** (4x): call, बोलो, senior, देख, पूछना, कराओ
- **agent_confirm_step** (1x): now, details, button, proceed, click

## 2. Customer sentiment by intent

- **customer_report_done**: frustrated:1
- **customer_acknowledge**: frustrated:1
- **customer_agree**: confused:3 · skeptical:1
- **customer_ask_question**: frustrated:5 · confused:5
- **customer_request_wait**: frustrated:1
- **customer_do_otp**: frustrated:3 · confused:1
- **customer_other**: frustrated:6 · confused:1
- **customer_query_fee**: confused:2 · frustrated:1
- **customer_report_link_opened**: frustrated:1
- **customer_report_address_error**: frustrated:9
- **customer_respond_udyam**: confused:1
- **customer_express_distrust**: distrustful:5
- **customer_provide_org_name**: frustrated:3
- **customer_skip_udyam**: frustrated:1

## 3. Tool / API calls detected

_Inferred from the agent's words (a proxy, not real tool logs). Count = turns where the tool actually fired._

- **send_otp** ← `agent_request_otp` (233x)
- **transfer_to_rm** ← `agent_transfer_to_rm` (204x)
- **send_sms** ← `agent_send_sms_link` (149x)
- **push_to_crm** ← `agent_inform_manual_review` (6x)
