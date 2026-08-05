# Labeling guide — Generic cross-client calls (broad buckets) (Hinglish)

You are the TEACHER creating ground-truth labels. For EACH turn assign the single best `base_intent` from the list below, the signal `keywords` (verbatim spans copied from the turn text), the customer `sentiment`, and any `tool` call.

Rules:
- `base_intent` MUST be exactly one value from the list (or `other` if nothing fits — then add `suggested_intent` with a short new name).
- `keywords`: 1-5 short phrases COPIED VERBATIM from the turn text. No paraphrasing, no invented words, no names/PII, and NO number sequences (phone numbers, OTPs, spelled-out digits like 'नाइन डबल टू'). If nothing is salient, use [].
- `sentiment`: ONLY for customer turns, else null. One of: ['confused', 'distrustful', 'frustrated', 'happy', 'neutral', 'skeptical']. Use `neutral` if no clear emotion.
- `tool`: ONLY for agent turns where an actual system action is performed (not merely mentioned). One of: [] or null.
- Judge by MEANING and context, not keyword presence. The transcript is Hinglish (mixed Hindi/Devanagari + romanized English) and may have ASR errors.
- If a turn is unintelligible ASR garble (repeated/nonsensical tokens, no clear meaning), label `base_intent` = `other`, `keywords` = [], and move on — do NOT over-analyze it.

## Valid base intents (with example utterances)

- **greeting** (agent→`agent_greet`, customer→`customer_greet`)
    e.g. hello, sir? | नमस्ते, मैं बोल रही हूँ
- **agree** (agent→`agent_confirm`, customer→`customer_agree`)
    e.g. haan bolo | theek hai bataiye | जी करिए
- **disagree** (agent→`agent_acknowledge_decline`, customer→`customer_disagree`)
    e.g. mujhe nahi chahiye | interested nahi hoon abhi
- **ask_question** (agent→`agent_clarify`, customer→`customer_ask_question`)
    e.g. ye kaise hoga | iska matlab kya hai
- **answer_query** (agent→`agent_answer_query`, customer→`customer_ask_query`)
    e.g. मैं आपको बताती हूँ | let me explain that
- **confused_repeat** (agent→`agent_ask_to_repeat`, customer→`customer_unclear`)
    e.g. samajh nahi aaya | phir se boliye
- **callback_request** (agent→`agent_schedule_callback`, customer→`customer_request_callback`)
    e.g. abhi busy hoon baad mein call karo | thodi der baad call kijiye
- **person_unavailable** (agent→`agent_acknowledge_unavailable`, customer→`customer_report_unavailable`)
    e.g. woh abhi ghar pe nahi hain | meeting mein hain abhi
- **distrust_security** (agent→`agent_reassure_trust`, customer→`customer_express_distrust`)
    e.g. ye fraud toh nahi hai | mujhe bharosa nahi ho raha
- **irate_frustrated** (agent→`agent_de_escalate`, customer→`customer_express_frustration`)
    e.g. kab se sun raha hoon | itna complicated kyun hai
- **wait_hold** (agent→`agent_wait`, customer→`customer_request_wait`)
    e.g. ek minute wait kijiye | line par rahiye please
- **acknowledge** (agent→`agent_acknowledge`, customer→`customer_acknowledge`)
    e.g. जी ठीक है | ok noted | अच्छा
- **end_call** (agent→`agent_end_call`, customer→`customer_end`)
    e.g. aapke time ke liye dhanyawaad | thank you, goodbye

## Output format (per call): JSON
```json
{"call_id": "<id>", "turns": [
  {"index": 0, "speaker": "customer", "base_intent": "report_no_leads", "keywords": ["लीड नहीं आ"], "sentiment": "frustrated", "tool": null}
]}
```