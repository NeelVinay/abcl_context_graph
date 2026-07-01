# Glossary

What each intent, sentiment, and tool label means. Source of truth: `src/extract.py`.

## Intents (action-oriented, actor-aware)

| Intent | Meaning |
|---|---|
| `agent_greet` | Agent: greet |
| `customer_greet` | Customer: greet |
| `agent_disclose_recording` | Agent: disclose recording |
| `customer_acknowledge` | Customer: acknowledge |
| `agent_present_offer` | Agent: present offer |
| `customer_react_to_offer` | Customer: react to offer |
| `agent_send_sms_link` | Agent: send sms link |
| `customer_report_sms_received` | Customer: report sms received |
| `agent_guide_open_link` | Agent: guide open link |
| `customer_report_link_opened` | Customer: report link opened |
| `agent_guide_apply` | Agent: guide apply |
| `customer_report_applied` | Customer: report applied |
| `agent_request_otp` | Agent: request otp |
| `customer_do_otp` | Customer: do otp |
| `agent_request_pan` | Agent: request pan |
| `customer_provide_pan` | Customer: provide pan |
| `agent_request_personal_details` | Agent: request personal details |
| `customer_provide_personal_details` | Customer: provide personal details |
| `agent_request_email` | Agent: request email |
| `customer_provide_email` | Customer: provide email |
| `agent_request_address` | Agent: request address |
| `customer_provide_address` | Customer: provide address |
| `agent_help_address_error` | Agent: help address error |
| `customer_report_address_error` | Customer: report address error |
| `agent_ask_employment_type` | Agent: ask employment type |
| `customer_state_employment_type` | Customer: state employment type |
| `agent_request_income` | Agent: request income |
| `customer_provide_income` | Customer: provide income |
| `agent_request_business_details` | Agent: request business details |
| `customer_provide_business_details` | Customer: provide business details |
| `agent_request_org_name` | Agent: request org name |
| `customer_provide_org_name` | Customer: provide org name |
| `agent_request_udyam` | Agent: request udyam |
| `customer_respond_udyam` | Customer: respond udyam |
| `agent_offer_skip_udyam` | Agent: offer skip udyam |
| `customer_skip_udyam` | Customer: skip udyam |
| `agent_request_terms_accept` | Agent: request terms accept |
| `customer_accept_terms` | Customer: accept terms |
| `agent_inform_manual_review` | Agent: inform manual review |
| `agent_present_final_offer` | Agent: present final offer |
| `customer_react_to_final_offer` | Customer: react to final offer |
| `agent_transfer_to_rm` | Agent: transfer to rm |
| `customer_acknowledge_transfer` | Customer: acknowledge transfer |
| `agent_explain_fee` | Agent: explain fee |
| `customer_query_fee` | Customer: query fee |
| `agent_reassure_trust` | Agent: reassure trust |
| `customer_express_distrust` | Customer: express distrust |
| `agent_answer_query` | Agent: answer query |
| `customer_ask_query` | Customer: ask query |
| `agent_clarify` | Agent: clarify |
| `customer_ask_question` | Customer: ask question |
| `agent_ask_to_repeat` | Agent: ask to repeat |
| `customer_unclear` | Customer: unclear |
| `agent_wait` | Agent: wait |
| `customer_request_wait` | Customer: request wait |
| `agent_confirm` | Agent: confirm |
| `customer_agree` | Customer: agree |
| `agent_confirm_step` | Agent: confirm step |
| `customer_report_done` | Customer: report done |
| `agent_acknowledge` | Agent: acknowledge |
| `agent_end_call` | Agent: end call |

## Customer sentiment labels

| Sentiment | Meaning |
|---|---|
| `distrustful` | Customer suspects a scam / fraud, reluctant to share info ('access nahi dena') |
| `frustrated` | Customer stuck or annoyed (errors, repeated retries, 'kab tak') |
| `confused` | Customer doesn't understand what to do or what a field means |
| `skeptical` | Customer doubtful / seeking reassurance ('pakka?', 'sahi me?') |
| `happy` | Customer pleased / satisfied |
| `neutral` | No strong sentiment detected (default) |

## Tool / API calls (INFERRED from agent speech)

_Not from real tool logs — inferred only when the agent's words show the action is performed (a tool noun + a do/send verb). A proxy, not an observed event._

| Tool | Meaning | Fires on intent | Required verb |
|---|---|---|---|
| `send_sms` | Agent triggers an SMS (e.g. application/resume link) | `send_sms_link` | _भेज, send, share कर, कर रही हूँ, कर दिया_ |
| `send_otp` | OTP sent for mobile/email verification | `mobile_otp` | _भेज, send, आएगा, आ रहा, generate, get otp, प्राप्त_ |
| `transfer_to_rm` | Hand-off to a relationship manager / specialist | `transfer_to_rm` | _(intent itself is the action)_ |
| `push_to_crm` | Application pushed to CRM (e.g. for manual review) | `manual_review` | _(intent itself is the action)_ |
