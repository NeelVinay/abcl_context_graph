# Glossary

What each intent, sentiment, and tool label means (present in this dataset). Source of truth: `src/extract.py`.

## Intents present in this dataset (13)

| Intent | Meaning | Turns |
|---|---|---|
| `agent_investigate_explain` | Agent checks the account and explains how leads/ratings/category work, or advises improvements | 221 |
| `customer_other` | Customer turn with no clear intent (often unintelligible ASR) | 186 |
| `agent_other` | Agent turn with no clear intent (often unintelligible ASR) | 155 |
| `customer_complaint` | Customer raises a problem — leads not coming, wrong/irrelevant leads, no ROI, low rating, coverage, or wants to cancel | 137 |
| `customer_acknowledge` | Customer acknowledgement / agreement / back-channel | 112 |
| `customer_ask_question` | Customer asks a question | 66 |
| `agent_greet` | Agent's opening / identifies the business | 61 |
| `agent_ask` | Agent asks the customer a question to investigate | 53 |
| `agent_acknowledge_complaint` | Agent acknowledges the customer's complaint before addressing it | 53 |
| `agent_raise_request` | Agent logs a request/ticket, promises follow-up, or transfers to a team | 41 |
| `agent_acknowledge` | Agent acknowledgement / back-channel (ok, achha, noted) | 40 |
| `customer_respond` | Customer responds to the agent's explanation or questions | 29 |
| `customer_greet` | Customer's opening / confirms who they are | 28 |

## Customer sentiment labels

| Sentiment | Meaning |
|---|---|
| `frustrated` | Customer stuck or annoyed (errors, repeated retries, 'kab tak') |
| `confused` | Customer doesn't understand what to do or what a field means |
| `happy` | Customer pleased / satisfied |
| `neutral` | No strong sentiment detected (default) |

## Tool / API calls (INFERRED from agent speech)

_No tool/API calls were inferred in this dataset._

