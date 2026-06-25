"""Fake per-call graphs (now with speaker + verbatim text) so merge/analyze/visualize
run with no LLM and no transcripts. Designed to show: overlap (shared edges, count>1),
a branch (price objection), a drop-off, and MULTIPLE phrasings per intent."""

# Reusable (speaker, intent, text) steps so nodes + phrasings overlap across calls.
g_greet    = ("agent",    "greeting",           "Namaste, main Priya bol rahi hoon Aditya Birla se")
c_confirm  = ("customer", "confirm_identity",   "Haan ji boliye")
a_reason   = ("agent",    "ask_loan_reason",    "Aapne loan mein interest dikhaya tha, kis cheez ke liye chahiye?")
c_purpose  = ("customer", "state_loan_purpose", "Ghar ki renovation ke liye")
a_offer    = ("agent",    "offer_details",      "Aapke liye humare paas accha personal loan offer hai")
c_agree    = ("customer", "agree",              "Theek hai, aage badhiye")
c_agree2   = ("customer", "agree",              "Haan ji kar dijiye")
a_transfer = ("agent",    "transfer_to_rm",     "Main aapko apne relationship manager se connect karti hoon")
c_obj      = ("customer", "price_objection",    "Interest rate thoda zyada lag raha hai")
c_obj2     = ("customer", "price_objection",    "EMI kaafi zyada ho rahi hai")
a_instal   = ("agent",    "offer_instalment",   "Hum EMI ko aur comfortable bana sakte hain")
c_notint   = ("customer", "not_interested",     "Nahi, mujhe abhi nahi chahiye")
c_wrong    = ("customer", "wrong_number",       "Aapne galat number par call kiya hai")


def _t(steps):
    return [
        {"index": i, "speaker": s, "intent": intent, "text": text,
         "entities": [], "key_phrases": [], "decision_note": None}
        for i, (s, intent, text) in enumerate(steps)
    ]


MAIN  = [g_greet, c_confirm, a_reason, c_purpose, a_offer, c_agree, a_transfer]
MAIN2 = [g_greet, c_confirm, a_reason, c_purpose, a_offer, c_agree2, a_transfer]
OBJ   = [g_greet, c_confirm, a_reason, c_purpose, a_offer, c_obj, a_instal, c_agree, a_transfer]
OBJ2  = [g_greet, c_confirm, a_reason, c_purpose, a_offer, c_obj2, a_instal, c_agree, a_transfer]
DROP  = [g_greet, c_confirm, a_reason, c_purpose, a_offer, c_obj, c_notint]
WRONG = [g_greet, c_wrong]

MOCK_CALLS = [
    {"call_id": "c01", "outcome": "transferred",    "turns": _t(MAIN)},
    {"call_id": "c02", "outcome": "transferred",    "turns": _t(MAIN2)},
    {"call_id": "c03", "outcome": "transferred",    "turns": _t(MAIN)},
    {"call_id": "c04", "outcome": "transferred",    "turns": _t(OBJ)},
    {"call_id": "c05", "outcome": "transferred",    "turns": _t(OBJ2)},
    {"call_id": "c06", "outcome": "not_interested", "turns": _t(DROP)},
    {"call_id": "c07", "outcome": "not_interested", "turns": _t(DROP)},
    {"call_id": "c08", "outcome": "dropped",        "turns": _t(WRONG)},
]
