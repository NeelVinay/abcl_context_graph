# Glossary

What each intent, sentiment, and tool label means (present in this dataset). Source of truth: `src/extract.py`.

## Intents present in this dataset (57)

| Intent | Meaning | Turns |
|---|---|---|
| `customer_greet` | Customer's opening / confirms who they are | 191 |
| `agent_greet` | Agent's opening / identifies the business | 147 |
| `customer_agree` | Customer agrees to proceed | 109 |
| `customer_ask_question` | Customer asks a question | 109 |
| `customer_acknowledge` | Customer acknowledgement / agreement / back-channel | 106 |
| `customer_other` | Customer turn with no clear intent (often unintelligible ASR) | 94 |
| `agent_wait` | Agent asks the customer to wait / is checking | 81 |
| `agent_answer_query` | Agent answers the customer's question | 79 |
| `agent_guide_open_link` | Agent guides the customer to open the link/website | 78 |
| `agent_send_sms_link` | Agent sends the SMS with the application link | 76 |
| `agent_request_otp` | Agent asks the customer to enter and verify the OTP | 71 |
| `agent_present_offer` | Agent pitches the pre-approved loan offer | 68 |
| `agent_ask_to_repeat` | Agent asks the customer to repeat / didn't catch it | 64 |
| `customer_do_otp` | Customer enters/verifies the OTP | 48 |
| `agent_acknowledge` | Agent acknowledgement / back-channel (ok, achha, noted) | 44 |
| `agent_guide_apply` | Agent guides the customer to tap Apply Now / start the form | 41 |
| `agent_other` | Agent turn with no clear intent (often unintelligible ASR) | 39 |
| `customer_report_done` | Customer reports they finished the step | 36 |
| `customer_request_wait` | Customer asks the agent to hold on a moment | 35 |
| `agent_end_call` | Agent closes the call | 33 |
| `customer_query_fee` | Customer asks about fees, EMI, or interest rate | 31 |
| `agent_explain_fee` | Agent explains processing fee / EMI / interest rate | 30 |
| `customer_report_address_error` | Customer reports the address field is erroring | 29 |
| `customer_report_sms_received` | Customer confirms the SMS/link arrived | 24 |
| `customer_report_link_opened` | Customer confirms the link/page opened | 21 |
| `agent_request_pan` | Agent asks the customer to fill their PAN number | 20 |
| `agent_request_personal_details` | Agent asks for name, gender, DOB, marital status | 20 |
| `customer_react_to_offer` | Customer reacts to the loan offer (interest, doubt, refusal) | 13 |
| `agent_reassure_trust` | Agent reassures the customer it's genuine (not fraud) | 13 |
| `agent_present_final_offer` | Agent presents the final loan offer (amount, tenure) | 13 |
| `customer_react_to_final_offer` | Customer reacts to the final offer | 13 |
| `customer_express_distrust` | Customer suspects fraud / is reluctant to share info | 12 |
| `customer_respond_udyam` | Customer responds about Udyam registration | 11 |
| `customer_unclear` | Customer's turn was unclear / asked to repeat | 10 |
| `agent_transfer_to_rm` | Agent hands off to a Relationship Manager for KYC | 10 |
| `customer_skip_udyam` | Customer chooses to skip Udyam | 9 |
| `agent_request_terms_accept` | Agent asks the customer to accept terms & conditions | 9 |
| `agent_confirm` | Agent confirms / agrees to proceed | 8 |
| `agent_request_email` | Agent asks the customer to enter their email | 8 |
| `customer_report_applied` | Customer confirms they clicked Apply / started | 6 |
| `customer_provide_pan` | Customer fills/confirms their PAN | 6 |
| `agent_help_address_error` | Agent helps resolve an address field error | 6 |
| `agent_request_address` | Agent asks the customer to fill their address / pincode | 6 |
| `agent_request_udyam` | Agent asks for Udyam number (business registration) | 6 |
| `customer_state_employment_type` | Customer states their employment type | 4 |
| `agent_clarify` | Agent clarifies or re-explains a step | 4 |
| `agent_ask_employment_type` | Agent asks salaried vs self-employed | 4 |
| `agent_request_business_details` | Agent asks for business details (self-employed) | 3 |
| `customer_provide_business_details` | Customer provides business details | 3 |
| `agent_request_org_name` | Agent asks for the organization/company name | 2 |
| `customer_provide_address` | Customer fills their address details | 2 |
| `customer_ask_query` | Customer asks the agent a question | 2 |
| `customer_provide_org_name` | Customer provides the organization name | 1 |
| `customer_provide_email` | Customer enters their email | 1 |
| `customer_provide_personal_details` | Customer fills their personal details | 1 |
| `agent_request_income` | Agent asks the customer to enter monthly income | 1 |
| `agent_offer_skip_udyam` | Agent offers to skip Udyam (goes to manual review) | 1 |

## Customer sentiment labels

| Sentiment | Meaning |
|---|---|
| `distrustful` | Customer suspects a scam / fraud, reluctant to share info ('access nahi dena') |
| `frustrated` | Customer stuck or annoyed (errors, repeated retries, 'kab tak') |
| `confused` | Customer doesn't understand what to do or what a field means |
| `happy` | Customer pleased / satisfied |
| `neutral` | No strong sentiment detected (default) |

## Tool / API calls (INFERRED from agent speech)

_Not from real tool logs — inferred only when the agent's words show the action is performed (a tool noun + a do/send verb). A proxy, not an observed event._

| Tool | Meaning | Fires on intent | Required verb |
|---|---|---|---|
| `send_sms` | Agent triggers an SMS (e.g. application/resume link) | `send_sms_link` | _भेज, send, share कर, कर रही हूँ, कर दिया_ |
| `send_otp` | OTP sent for mobile/email verification | `mobile_otp` | _भेज, send, आएगा, आ रहा, generate, get otp, प्राप्त_ |
| `transfer_to_rm` | Hand-off to a relationship manager / specialist | `transfer_to_rm` | _(intent itself is the action)_ |
