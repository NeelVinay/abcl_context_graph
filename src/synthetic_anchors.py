"""Synthetic multi-domain anchor phrases for the `generic` broad-bucket taxonomy.

Generated OFFLINE, ONCE, by Claude — not per new client, not at inference time. The
point: src/generic_taxonomy.py's hand-written examples (28 phrases, effectively just
ABCL's own register) and the real ABCL/JustDial gold data (2 domains) are not diverse
enough for the embedding model to separate "the concept of agreement" from "the
vocabulary of loans" or "the vocabulary of lead-gen support" — see
scripts/_generic_prototype_eval.py, which measured 18-32% cross-domain accuracy no
matter the classifier (logreg, centroid, hand-written anchors alone).

This adds phrasing for the SAME 13 broad buckets across 5 domains ABCL/JustDial never
touch (insurance, logistics, telecom, healthcare, ed-tech), so the model sees each
bucket in enough different registers to learn the abstract concept instead of a
domain fingerprint. This is a ONE-TIME offline augmentation step when building/
refreshing the generic model — a genuinely new client still gets scored by whatever
model already exists, no per-client Claude pass required.

See scripts/_generic_synthetic_eval.py for the before/after measurement.
"""
from __future__ import annotations

# (domain, base_intent, phrase)
SYNTHETIC_ANCHORS = [
    # --- insurance (policy renewal / claim) ---
    ("insurance", "greeting", "नमस्ते, मैं आपकी insurance policy को लेकर बात कर रही हूँ"),
    ("insurance", "greeting", "hello sir, calling from the policy renewal team"),
    ("insurance", "agree", "हाँ renew कर दीजिए"),
    ("insurance", "agree", "ok proceed with the renewal"),
    ("insurance", "disagree", "मुझे renew नहीं करवाना अभी"),
    ("insurance", "disagree", "not interested in renewing this year"),
    ("insurance", "ask_question", "claim process kitne din lega?"),
    ("insurance", "ask_question", "premium kitna badhega renewal mein?"),
    ("insurance", "answer_query", "मैं आपको claim process समझा देती हूँ"),
    ("insurance", "answer_query", "renewal premium मैं अभी बता देती हूँ"),
    ("insurance", "confused_repeat", "sorry, phir se boliye claim ka process"),
    ("insurance", "confused_repeat", "samajh nahi aaya, dobara batayein"),
    ("insurance", "callback_request", "abhi busy hoon, baad mein call kijiye insurance ke liye"),
    ("insurance", "callback_request", "call me back this evening about the policy"),
    ("insurance", "person_unavailable", "policy holder abhi ghar pe nahi hain"),
    ("insurance", "person_unavailable", "the policy holder is travelling right now"),
    ("insurance", "distrust_security", "ye insurance call genuine hai kya, fraud toh nahi?"),
    ("insurance", "distrust_security", "is this a real insurance company calling?"),
    ("insurance", "irate_frustrated", "kab se insurance ke bare mein sun raha hoon, seedha bolo kya karna hai"),
    ("insurance", "irate_frustrated", "this is taking forever, just tell me the premium"),
    ("insurance", "wait_hold", "ek minute wait kijiye policy details check kar rahi hoon"),
    ("insurance", "wait_hold", "hold on, checking your policy record"),
    ("insurance", "acknowledge", "ji theek hai, samajh gaya"),
    ("insurance", "acknowledge", "ok noted, got it"),
    ("insurance", "end_call", "dhanyawaad, aapka din shubh ho"),
    ("insurance", "end_call", "thank you, have a good day"),

    # --- logistics (delivery / courier tracking) ---
    ("logistics", "greeting", "नमस्ते, मैं आपके parcel को लेकर call कर रही हूँ"),
    ("logistics", "greeting", "hi, this is regarding your delivery"),
    ("logistics", "agree", "हाँ ठीक है भेज दो"),
    ("logistics", "agree", "yes that works, go ahead and deliver"),
    ("logistics", "disagree", "नहीं मुझे delivery reschedule नहीं करनी"),
    ("logistics", "disagree", "no, don't reschedule the delivery"),
    ("logistics", "ask_question", "parcel kab tak aayega?"),
    ("logistics", "ask_question", "kitna time lagega delivery mein?"),
    ("logistics", "answer_query", "delivery 2-3 din mein ho jayegi"),
    ("logistics", "answer_query", "it'll arrive by tomorrow evening"),
    ("logistics", "confused_repeat", "samajh nahi aaya, dobara batayein tracking wala"),
    ("logistics", "confused_repeat", "sorry, can you repeat the delivery date?"),
    ("logistics", "callback_request", "thodi der baad call karo delivery ke baare mein"),
    ("logistics", "callback_request", "call me back in an hour, I'm driving"),
    ("logistics", "person_unavailable", "woh abhi available nahi hain parcel receive karne"),
    ("logistics", "person_unavailable", "he's not home right now to receive it"),
    ("logistics", "distrust_security", "ye delivery scam toh nahi hai?"),
    ("logistics", "distrust_security", "is this courier company even real?"),
    ("logistics", "irate_frustrated", "bar bar delivery late ho rahi hai, bahut pareshan hoon"),
    ("logistics", "irate_frustrated", "this is the third delay, I'm really frustrated"),
    ("logistics", "wait_hold", "line par rahiye, tracking details dekh rahi hoon"),
    ("logistics", "wait_hold", "please hold, checking the tracking status"),
    ("logistics", "acknowledge", "achha ok noted"),
    ("logistics", "acknowledge", "alright, understood"),
    ("logistics", "end_call", "thank you, aapke time ke liye dhanyawaad"),
    ("logistics", "end_call", "thanks, goodbye"),

    # --- telecom (broadband / mobile plan support) ---
    ("telecom", "greeting", "नमस्ते, मैं आपके broadband connection के बारे में बात कर रही हूँ"),
    ("telecom", "greeting", "hello, calling about your mobile plan"),
    ("telecom", "agree", "हाँ upgrade कर दो plan"),
    ("telecom", "agree", "yes go ahead and upgrade it"),
    ("telecom", "disagree", "मुझे plan upgrade नहीं चाहिए"),
    ("telecom", "disagree", "I don't want to upgrade the plan"),
    ("telecom", "ask_question", "naya plan mein kya milega?"),
    ("telecom", "ask_question", "what's included in the new plan?"),
    ("telecom", "answer_query", "मैं आपको नए plan के benefits बता देती हूँ"),
    ("telecom", "answer_query", "let me explain what the new plan includes"),
    ("telecom", "confused_repeat", "kya bola aapne, plan wala part?"),
    ("telecom", "confused_repeat", "sorry, could you repeat the plan details?"),
    ("telecom", "callback_request", "abhi meeting mein hoon, later call karo"),
    ("telecom", "callback_request", "I'm in a meeting, call me back later"),
    ("telecom", "person_unavailable", "account holder abhi busy hain"),
    ("telecom", "person_unavailable", "the account owner is not available right now"),
    ("telecom", "distrust_security", "aap asli telecom company se ho na, fraud nahi ho"),
    ("telecom", "distrust_security", "is this really the telecom provider calling?"),
    ("telecom", "irate_frustrated", "kitni baar bolu network issue hai, thik karo"),
    ("telecom", "irate_frustrated", "I've complained three times already, fix this"),
    ("telecom", "wait_hold", "thoda ruko, account check kar rahi hoon"),
    ("telecom", "wait_hold", "one moment, pulling up your account"),
    ("telecom", "acknowledge", "hmm thik hai"),
    ("telecom", "acknowledge", "okay, that's fine"),
    ("telecom", "end_call", "goodbye, dhanyawaad call ke liye"),
    ("telecom", "end_call", "thanks for calling, goodbye"),

    # --- healthcare (appointment reminder / clinic) ---
    ("healthcare", "greeting", "नमस्ते, ये क्लिनिक से appointment reminder call है"),
    ("healthcare", "greeting", "hello, this is a reminder call from the clinic"),
    ("healthcare", "agree", "हाँ मैं आ जाऊंगा appointment पर"),
    ("healthcare", "agree", "yes I'll be there for the appointment"),
    ("healthcare", "disagree", "मैं appointment पर नहीं आ पाऊंगा, cancel कर दीजिए"),
    ("healthcare", "disagree", "I can't make it, please cancel the appointment"),
    ("healthcare", "ask_question", "doctor available honge kya us din?"),
    ("healthcare", "ask_question", "will the doctor be available that day?"),
    ("healthcare", "answer_query", "जी doctor available रहेंगे"),
    ("healthcare", "answer_query", "yes, the doctor will be available then"),
    ("healthcare", "confused_repeat", "thoda clearly boliye please"),
    ("healthcare", "confused_repeat", "sorry, what time was the appointment again?"),
    ("healthcare", "callback_request", "abhi nahi baat kar sakta appointment ke baare mein, shaam ko call karo"),
    ("healthcare", "callback_request", "call me back this evening about the appointment"),
    ("healthcare", "person_unavailable", "patient abhi doctor ke paas hain baat nahi kar sakte"),
    ("healthcare", "person_unavailable", "the patient is with another doctor right now"),
    ("healthcare", "distrust_security", "ye clinic ka genuine call hai kya?"),
    ("healthcare", "distrust_security", "is this really calling from the hospital?"),
    ("healthcare", "irate_frustrated", "itni der se wait kar raha hoon appointment ke liye"),
    ("healthcare", "irate_frustrated", "I've been waiting for this appointment for weeks"),
    ("healthcare", "wait_hold", "ek second, appointment slot dekh rahi hoon"),
    ("healthcare", "wait_hold", "hold on, checking the appointment slot"),
    ("healthcare", "acknowledge", "ji achha"),
    ("healthcare", "acknowledge", "alright, understood"),
    ("healthcare", "end_call", "thank you appointment ke liye, goodbye"),
    ("healthcare", "end_call", "thanks, see you at the appointment"),

    # --- ed-tech (course enrollment counselor) ---
    ("edtech", "greeting", "नमस्ते, मैं आपके course enrollment को लेकर बात कर रही हूँ"),
    ("edtech", "greeting", "hi, calling about your course enrollment"),
    ("edtech", "agree", "हाँ enroll कर दीजिए मुझे"),
    ("edtech", "agree", "yes go ahead and enroll me"),
    ("edtech", "disagree", "मुझे course join नहीं करना अभी"),
    ("edtech", "disagree", "I don't want to join the course right now"),
    ("edtech", "ask_question", "course ki fees kitni hai?"),
    ("edtech", "ask_question", "what's the fee for this course?"),
    ("edtech", "answer_query", "course fees मैं आपको बता देती हूँ"),
    ("edtech", "answer_query", "let me tell you the course fee"),
    ("edtech", "confused_repeat", "phir se bataiye enrollment steps"),
    ("edtech", "confused_repeat", "sorry, can you repeat the enrollment steps?"),
    ("edtech", "callback_request", "abhi busy hoon course ke baare mein baad mein baat karte hain"),
    ("edtech", "callback_request", "let's talk about the course later, I'm busy now"),
    ("edtech", "person_unavailable", "student abhi class mein hai baat nahi kar sakta"),
    ("edtech", "person_unavailable", "he's in class right now, can't talk"),
    ("edtech", "distrust_security", "ye course wala scam toh nahi hai?"),
    ("edtech", "distrust_security", "is this course enrollment thing even legit?"),
    ("edtech", "irate_frustrated", "bahut complicated hai enrollment process, jaldi batao"),
    ("edtech", "irate_frustrated", "this enrollment process is way too complicated"),
    ("edtech", "wait_hold", "wait कीजिए, seat availability check कर रही हूँ"),
    ("edtech", "wait_hold", "hold on, checking seat availability"),
    ("edtech", "acknowledge", "ok theek hai samajh gaya"),
    ("edtech", "acknowledge", "got it, that's clear"),
    ("edtech", "end_call", "dhanyawaad course ke baare mein baat करने के लिए"),
    ("edtech", "end_call", "thanks for the info, goodbye"),
]
