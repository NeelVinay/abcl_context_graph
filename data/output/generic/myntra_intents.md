# Glossary

What each intent, sentiment, and tool label means (present in this dataset). Source of truth: `src/extract.py`.

## Intents present in this dataset (26)

| Intent | Meaning | Turns |
|---|---|---|
| `agent_answer_query` | Agent answers the customer's question | 217 |
| `customer_ask_question` | Customer asks a question | 164 |
| `customer_express_frustration` | Customer: express frustration | 116 |
| `agent_de_escalate` | Agent: de escalate | 87 |
| `agent_wait` | Agent asks the customer to wait / is checking | 76 |
| `agent_end_call` | Agent closes the call | 67 |
| `agent_clarify` | Agent clarifies or re-explains a step | 66 |
| `customer_other` | Customer turn with no clear intent (often unintelligible ASR) | 60 |
| `customer_ask_query` | Customer asks the agent a question | 53 |
| `agent_greet` | Agent's opening / identifies the business | 52 |
| `customer_acknowledge` | Customer acknowledgement / agreement / back-channel | 45 |
| `agent_ask_to_repeat` | Agent asks the customer to repeat / didn't catch it | 37 |
| `agent_acknowledge` | Agent acknowledgement / back-channel (ok, achha, noted) | 32 |
| `customer_greet` | Customer's opening / confirms who they are | 23 |
| `customer_end` | Customer: end | 22 |
| `customer_agree` | Customer agrees to proceed | 13 |
| `customer_unclear` | Customer's turn was unclear / asked to repeat | 11 |
| `customer_request_callback` | Customer: request callback | 11 |
| `agent_reassure_trust` | Agent reassures the customer it's genuine (not fraud) | 9 |
| `customer_express_distrust` | Customer suspects fraud / is reluctant to share info | 7 |
| `agent_other` | Agent turn with no clear intent (often unintelligible ASR) | 6 |
| `customer_disagree` | Customer: disagree | 6 |
| `customer_request_wait` | Customer asks the agent to hold on a moment | 5 |
| `agent_confirm` | Agent confirms / agrees to proceed | 4 |
| `agent_acknowledge_decline` | Agent: acknowledge decline | 2 |
| `customer_report_unavailable` | Customer: report unavailable | 2 |

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

_No tool/API calls were inferred in this dataset._

