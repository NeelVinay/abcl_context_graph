# ABCL Call Context-Graph Report

Calls analyzed: **113** · intents: **65** · transitions: **987**
_(counts are per-turn occurrences across all calls, not number of calls)_

## 1. Keywords by intent (the signal words)

- **customer_report_done** (502x): कर दिया, हो गया, भर दिया, कर लिया, नहीं हो रहा, नहीं हो
- **agent_request_otp** (370x): otp
- **customer_acknowledge** (301x): record, दोबारा
- **agent_wait** (256x): wait
- **customer_agree** (249x): आगे बढ़, शुरू कर, doubt, कैसे
- **customer_ask_question** (233x): कब तक, मतलब, कौन सा, नहीं हो, कैसे
- **agent_greet** (219x): hello, नमस्ते, बात कर रही, से बात
- **agent_ask_to_repeat** (216x): फिर से कह, फिर से बता, साफ़ बोल, एक बार फिर
- **customer_greet** (214x): hello, बात कर रही, से बात, नमस्ते
- **agent_transfer_to_rm** (204x): relationship manager, specialist से connect, 140000
- **agent_send_sms_link** (182x): sms, लिंक भेज, link भेज
- **agent_guide_open_link** (178x): खुल गया, लिंक पर क्लिक, वेबसाइट, खुल गई
- **agent_guide_apply** (170x): apply now
- **customer_request_wait** (160x): एक second, wait, रुकिए, नहीं हो रहा, नहीं हो
- **agent_present_final_offer** (143x): final offer, loan amount and, cannot be changed, ₹378000, 378000
- **customer_do_otp** (140x): otp, बार बार, नहीं हो, नहीं हो रहा, कैसे
- **agent_request_address** (134x): address, pincode, locality, building, house number, flat
- **agent_request_email** (126x): email
- **agent_answer_query** (124x): —
- **customer_react_to_final_offer** (119x): loan amount and, final offer, final and
- **agent_request_pan** (113x): पैन, pan
- **agent_ask_employment_type** (113x): salaried, self-employ
- **agent_request_terms_accept** (111x): terms and condition, terms, बॉक्स चेक
- **agent_request_personal_details** (110x): gender, date of birth, marital
- **customer_other** (108x): नहीं हो रहा, नहीं हो, दोबारा, कैसे, बार बार
- **customer_query_fee** (83x): interest rate, processing fee, charges, कैसे, नहीं हो रहा, नहीं हो
- **customer_report_link_opened** (77x): खुल गया, नहीं हो, खुल गई, website, site खुल
- **agent_request_org_name** (76x): organization
- **agent_request_income** (74x): income
- **customer_state_employment_type** (67x): self employ, salaried, self employee
- **agent_request_business_details** (67x): business, shop
- **customer_report_sms_received** (60x): sms, link भेज
- **agent_acknowledge** (51x): —
- **agent_present_offer** (48x): pre-approved, loan offer, personal loan, ₹200000, 200000, pre approved
- **customer_provide_pan** (47x): pan
- **agent_explain_fee** (47x): processing fee, interest rate, charges, emi, ₹2,950, ₹5,150
- **customer_report_address_error** (40x): नहीं हो रहा, नहीं हो, error, leading slash, red
- **agent_request_udyam** (38x): udyam, उद्यम
- **customer_provide_address** (36x): house number, address, building, flat, आधार, locality
- **customer_respond_udyam** (32x): उद्यम, क्या भरूं
- **customer_express_distrust** (30x): fraud, fake
- **customer_report_applied** (30x): apply now
- **agent_help_address_error** (30x): error, नहीं हो रहा, red
- **agent_end_call** (27x): goodbye, duration has been exceeded
- **agent_reassure_trust** (27x): —
- **agent_offer_skip_udyam** (25x): skip
- **customer_provide_personal_details** (24x): gender, date of birth, marital
- **agent_other** (23x): —
- **customer_react_to_offer** (23x): loan offer, personal loan
- **agent_confirm** (21x): आगे बढ़, शुरू कर
- **customer_provide_org_name** (21x): नहीं हो रहा, नहीं हो, organization, company name
- **customer_provide_email** (20x): email
- **customer_skip_udyam** (18x): नहीं हो, skip
- **agent_clarify** (16x): कौन सा
- **customer_ask_query** (16x): —
- **customer_unclear** (13x): —
- **customer_provide_business_details** (12x): business
- **customer_accept_terms** (11x): —
- **customer_provide_income** (9x): income
- **agent_inform_manual_review** (6x): manual review
- **agent_disclose_recording** (6x): record, training, quality
- **customer_acknowledge_transfer** (4x): —
- **agent_confirm_step** (1x): —

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
