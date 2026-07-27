# Glossary

What each intent, sentiment, and tool label means (present in this dataset). Source of truth: `src/extract.py`.

## Intents present in this dataset (25)

| Intent | Meaning | Turns |
|---|---|---|
| `agent_answer_query` | Agent answers the customer's question | 243 |
| `customer_ask_question` | Customer asks a question | 147 |
| `customer_express_frustration` | Customer is irate, impatient, or frustrated | 144 |
| `agent_wait` | Agent asks the customer to wait / is checking | 78 |
| `agent_end_call` | Agent closes the call | 68 |
| `agent_de_escalate` | Agent tries to de-escalate an irate/frustrated customer | 63 |
| `agent_clarify` | Agent clarifies or re-explains | 56 |
| `agent_greet` | Agent's opening greeting | 55 |
| `customer_other` | Customer turn with no clear intent (often unintelligible ASR) | 53 |
| `agent_ask_to_repeat` | Agent asks the customer to repeat | 40 |
| `customer_acknowledge` | Customer acknowledgement / back-channel | 39 |
| `customer_ask_query` | Customer asks the agent a question | 39 |
| `agent_acknowledge` | Agent acknowledgement / back-channel | 32 |
| `customer_greet` | Customer's opening / picks up | 27 |
| `customer_end` | Customer closes / ends the call | 24 |
| `customer_agree` | Customer agrees to proceed | 16 |
| `customer_request_callback` | Customer asks to be called back later | 13 |
| `customer_disagree` | Customer declines or is not interested | 13 |
| `agent_reassure_trust` | Agent reassures the customer it's genuine | 13 |
| `customer_express_distrust` | Customer suspects fraud/scam or has a security concern | 9 |
| `customer_unclear` | Customer's turn was unclear / asked to repeat | 6 |
| `customer_request_wait` | Customer asks the agent to hold on | 6 |
| `agent_acknowledge_decline` | Agent acknowledges a decline/refusal | 4 |
| `agent_confirm` | Agent confirms / agrees to proceed | 3 |
| `customer_report_unavailable` | Customer reports the right person can't come to the phone | 2 |

## Customer sentiment labels

| Sentiment | Meaning |
|---|---|
| `distrustful` | Customer suspects a scam / fraud, reluctant to share info ('access nahi dena') |
| `frustrated` | Customer stuck or annoyed (errors, repeated retries, 'kab tak') |
| `confused` | Customer doesn't understand what to do or what a field means |
| `happy` | Customer pleased / satisfied |
| `neutral` | No strong sentiment detected (default) |

## Tool / API calls (INFERRED from agent speech)

_No tool/API calls were inferred in this dataset._

