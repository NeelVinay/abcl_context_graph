# Glossary

What each intent, sentiment, and tool label means (present in this dataset). Source of truth: `src/extract.py`.

## Intents present in this dataset (46)

| Intent | Meaning | Turns |
|---|---|---|
| `agent_answer_query` | Agent answers the customer's question | 199 |
| `customer_ask_question` | Customer asks a question | 168 |
| `customer_other` | Customer turn with no clear intent (often unintelligible ASR) | 125 |
| `agent_acknowledge` | Agent acknowledgement / back-channel (ok, achha, noted) | 113 |
| `customer_acknowledge` | Customer acknowledgement / agreement / back-channel | 74 |
| `agent_greet` | Agent's opening / identifies the business | 57 |
| `agent_wait` | Agent asks the customer to wait / is checking | 43 |
| `customer_agree` | Customer agrees to proceed | 43 |
| `agent_transfer_to_rm` | Agent hands off to a Relationship Manager for KYC | 43 |
| `agent_ask_to_repeat` | Agent asks the customer to repeat / didn't catch it | 41 |
| `agent_request_pan` | Agent asks the customer to fill their PAN number | 29 |
| `agent_clarify` | Agent clarifies or re-explains a step | 28 |
| `customer_greet` | Customer's opening / confirms who they are | 26 |
| `customer_express_distrust` | Customer suspects fraud / is reluctant to share info | 21 |
| `customer_ask_query` | Customer asks the agent a question | 18 |
| `agent_reassure_trust` | Agent reassures the customer it's genuine (not fraud) | 15 |
| `agent_other` | Agent turn with no clear intent (often unintelligible ASR) | 14 |
| `agent_end_call` | Agent closes the call | 12 |
| `agent_confirm` | Agent confirms / agrees to proceed | 10 |
| `agent_help_address_error` | Agent helps resolve an address field error | 10 |
| `customer_request_wait` | Customer asks the agent to hold on a moment | 9 |
| `agent_request_org_name` | Agent asks for the organization/company name | 9 |
| `customer_query_fee` | Customer asks about fees, EMI, or interest rate | 9 |
| `customer_report_done` | Customer reports they finished the step | 9 |
| `customer_report_address_error` | Customer reports the address field is erroring | 8 |
| `agent_present_offer` | Agent pitches the pre-approved loan offer | 7 |
| `agent_request_terms_accept` | Agent asks the customer to accept terms & conditions | 7 |
| `agent_send_sms_link` | Agent sends the SMS with the application link | 6 |
| `customer_provide_pan` | Customer fills/confirms their PAN | 6 |
| `customer_unclear` | Customer's turn was unclear / asked to repeat | 5 |
| `agent_request_address` | Agent asks the customer to fill their address / pincode | 4 |
| `customer_provide_address` | Customer fills their address details | 3 |
| `agent_present_final_offer` | Agent presents the final loan offer (amount, tenure) | 3 |
| `customer_react_to_final_offer` | Customer reacts to the final offer | 3 |
| `agent_request_business_details` | Agent asks for business details (self-employed) | 2 |
| `customer_do_otp` | Customer enters/verifies the OTP | 2 |
| `customer_report_link_opened` | Customer confirms the link/page opened | 2 |
| `customer_respond_udyam` | Customer responds about Udyam registration | 2 |
| `customer_skip_udyam` | Customer chooses to skip Udyam | 1 |
| `customer_react_to_offer` | Customer reacts to the loan offer (interest, doubt, refusal) | 1 |
| `customer_provide_org_name` | Customer provides the organization name | 1 |
| `customer_acknowledge_transfer` | Customer acknowledges the transfer to RM | 1 |
| `agent_request_udyam` | Agent asks for Udyam number (business registration) | 1 |
| `agent_inform_manual_review` | Agent informs the application goes to manual review | 1 |
| `agent_disclose_recording` | Agent discloses the call is recorded for quality/training | 1 |
| `customer_state_employment_type` | Customer states their employment type | 1 |

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
| `transfer_to_rm` | Hand-off to a relationship manager / specialist | `transfer_to_rm` | _(intent itself is the action)_ |
| `push_to_crm` | Application pushed to CRM (e.g. for manual review) | `manual_review` | _(intent itself is the action)_ |
