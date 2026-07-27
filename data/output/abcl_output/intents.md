# Glossary

What each intent, sentiment, and tool label means (present in this dataset). Source of truth: `src/extract.py`.

## Intents present in this dataset (63)

| Intent | Meaning | Turns |
|---|---|---|
| `customer_report_done` | Customer reports they finished the step | 502 |
| `agent_request_otp` | Agent asks the customer to enter and verify the OTP | 370 |
| `customer_acknowledge` | Customer acknowledgement / back-channel | 301 |
| `agent_wait` | Agent asks the customer to wait / is checking | 256 |
| `customer_agree` | Customer agrees to proceed | 249 |
| `customer_ask_question` | Customer asks a question | 233 |
| `agent_greet` | Agent's opening greeting | 219 |
| `agent_ask_to_repeat` | Agent asks the customer to repeat | 216 |
| `customer_greet` | Customer's opening / picks up | 214 |
| `agent_transfer_to_rm` | Agent hands off to a Relationship Manager for KYC | 204 |
| `agent_send_sms_link` | Agent sends the SMS with the application link | 182 |
| `agent_guide_open_link` | Agent guides the customer to open the link/website | 178 |
| `agent_guide_apply` | Agent guides the customer to tap Apply Now / start the form | 170 |
| `customer_request_wait` | Customer asks the agent to hold on | 160 |
| `agent_present_final_offer` | Agent presents the final loan offer (amount, tenure) | 143 |
| `customer_do_otp` | Customer enters/verifies the OTP | 140 |
| `agent_request_address` | Agent asks the customer to fill their address / pincode | 134 |
| `agent_request_email` | Agent asks the customer to enter their email | 126 |
| `agent_answer_query` | Agent answers the customer's question | 124 |
| `customer_react_to_final_offer` | Customer reacts to the final offer | 119 |
| `agent_request_pan` | Agent asks the customer to fill their PAN number | 113 |
| `agent_ask_employment_type` | Agent asks salaried vs self-employed | 113 |
| `agent_request_terms_accept` | Agent asks the customer to accept terms & conditions | 111 |
| `agent_request_personal_details` | Agent asks for name, gender, DOB, marital status | 110 |
| `customer_other` | Customer turn with no clear intent (often unintelligible ASR) | 108 |
| `customer_query_fee` | Customer asks about fees, EMI, or interest rate | 83 |
| `customer_report_link_opened` | Customer confirms the link/page opened | 77 |
| `agent_request_org_name` | Agent asks for the organization/company name | 76 |
| `agent_request_income` | Agent asks the customer to enter monthly income | 74 |
| `customer_state_employment_type` | Customer states their employment type | 67 |
| `agent_request_business_details` | Agent asks for business details (self-employed) | 67 |
| `customer_report_sms_received` | Customer confirms the SMS/link arrived | 60 |
| `agent_acknowledge` | Agent acknowledgement / back-channel | 51 |
| `agent_present_offer` | Agent pitches the pre-approved loan offer | 48 |
| `customer_provide_pan` | Customer fills/confirms their PAN | 47 |
| `agent_explain_fee` | Agent explains processing fee / EMI / interest rate | 47 |
| `customer_report_address_error` | Customer reports the address field is erroring | 40 |
| `agent_request_udyam` | Agent asks for Udyam number (business registration) | 38 |
| `customer_provide_address` | Customer fills their address details | 36 |
| `customer_respond_udyam` | Customer responds about Udyam registration | 32 |
| `customer_express_distrust` | Customer suspects fraud/scam or has a security concern | 30 |
| `customer_report_applied` | Customer confirms they clicked Apply / started | 30 |
| `agent_help_address_error` | Agent helps resolve an address field error | 30 |
| `agent_end_call` | Agent closes the call | 27 |
| `agent_reassure_trust` | Agent reassures the customer it's genuine | 27 |
| `agent_offer_skip_udyam` | Agent offers to skip Udyam (goes to manual review) | 25 |
| `customer_provide_personal_details` | Customer fills their personal details | 24 |
| `agent_other` | Agent turn with no clear intent (often unintelligible ASR) | 23 |
| `customer_react_to_offer` | Customer reacts to the loan offer (interest, doubt, refusal) | 23 |
| `agent_confirm` | Agent confirms / agrees to proceed | 21 |
| `customer_provide_org_name` | Customer provides the organization name | 21 |
| `customer_provide_email` | Customer enters their email | 20 |
| `customer_skip_udyam` | Customer chooses to skip Udyam | 18 |
| `agent_clarify` | Agent clarifies or re-explains | 16 |
| `customer_ask_query` | Customer asks the agent a question | 16 |
| `customer_unclear` | Customer's turn was unclear / asked to repeat | 13 |
| `customer_provide_business_details` | Customer provides business details | 12 |
| `customer_accept_terms` | Customer accepts the terms & conditions | 11 |
| `customer_provide_income` | Customer enters their income | 9 |
| `agent_inform_manual_review` | Agent informs the application goes to manual review | 6 |
| `agent_disclose_recording` | Agent discloses the call is recorded for quality/training | 6 |
| `customer_acknowledge_transfer` | Customer acknowledges the transfer to RM | 4 |
| `agent_confirm_step` | Agent confirms a step is done, moves on | 1 |

## Customer sentiment labels

| Sentiment | Meaning |
|---|---|
| `distrustful` | Customer suspects a scam / fraud, reluctant to share info ('access nahi dena') |
| `frustrated` | Customer stuck or annoyed (errors, repeated retries, 'kab tak') |
| `confused` | Customer doesn't understand what to do or what a field means |
| `skeptical` | Customer doubtful / seeking reassurance ('pakka?', 'sahi me?') |
| `neutral` | No strong sentiment detected (default) |

## Tool / API calls (INFERRED from agent speech)

_Not from real tool logs — inferred only when the agent's words show the action is performed (a tool noun + a do/send verb). A proxy, not an observed event._

| Tool | Meaning | Fires on intent | Required verb |
|---|---|---|---|
| `send_sms` | Agent triggers an SMS (e.g. application/resume link) | `send_sms_link` | _भेज, send, share कर, कर रही हूँ, कर दिया_ |
| `send_otp` | OTP sent for mobile/email verification | `mobile_otp` | _भेज, send, आएगा, आ रहा, generate, get otp, प्राप्त_ |
| `transfer_to_rm` | Hand-off to a relationship manager / specialist | `transfer_to_rm` | _(intent itself is the action)_ |
| `push_to_crm` | Application pushed to CRM (e.g. for manual review) | `manual_review` | _(intent itself is the action)_ |
