# What changed in final.raven

Every change below was derived from real call transcripts. Quotes are verbatim.

## Summary

| Change type | Count | What it does |
|---|---|---|
| Recognition phrases | 3 | The agent now understands more of what callers actually say, so these turns route to the right handler instead of falling through to the generic default. |
| Conversational delivery | 34 | A short acknowledgement particle real callers use, added as a lead-in. The wording of the line itself is unchanged — this only affects how scripted the agent sounds. |
| New agent speech | 6 | A new line answering something callers repeatedly say. The agent had no response for this before. |
| _Rejected by safety checks_ | 33 | Proposed but blocked — see the end of this file |

---

# Recognition phrases  (3)

_The agent now understands more of what callers actually say, so these turns route to the right handler instead of falling through to the generic default._

### 1. `affirm` now also recognises: **तैयार**

**Why:** affirm: "तैयार" (2 calls, 1.36x)

**Heard on real calls:**
> हां ठीक है बताओ कैसे करना है? हां हां तैयार हूं एकदम.
> बोलो. हां हां शुरू ticket का. हां. हमको लोगों के ज़रूरी आए तब बोलता आए तो ले लेगा. हां भेज दियो हमें

### 2. `hold` now also recognises: **wait**, **रुकिए**, **second**, **stay**, **रुको**, **waiting**, **रुक**

**Why:** hold: "wait" (24 calls, 2.61x), "रुकिए" (11 calls, 2.69x), "second" (9 calls, 2.20x), "stay" (5 calls, 2.10x), "रुको" (4 calls, 1.96x), "waiting" (2 calls, 1.96x), "रुक" (2 calls, 1.96x)

**Heard on real calls:**
> हां हां ma'am wait. Ma'am open अभी मतलब open हो रहा है. Wait wait. hello. हां ma'am एक minute एक min
> Sir waiting please आ रहा है please waiting.
> Something wait weight patience.

### 3. `self_employed` now also recognises: **employee**, **उद्यम**

**Why:** self_employed: "employee" (4 calls, 4.40x), "उद्यम" (4 calls, 1.76x)

**Heard on real calls:**
> Self employee.
> Self employee.
> जी. हमारा self employee.

---

# Conversational delivery  (34)

_A short acknowledgement particle real callers use, added as a lead-in. The wording of the line itself is unchanged — this only affects how scripted the agent sounds._

### **जी** added as a lead-in — in 25 place(s)

Real callers open turns with "जी" in 175 calls. Only the lead-in is added; no existing wording changed.

<details><summary>the lines it was added to</summary>

- `say("जी, एक बार अपना internet connection check करके link दोबारा try करें — खुल जाए तो बताएं।");`
- `say("जी, यह basic details का page है। सबसे पहले अपना पैन number fill करें और हो जाए तो बताएं।");`
- `say("जी, अब पैन के अनुसार full name enter करें, फिर gender, date of birth और marital status select करें — हो ज`
- `say("जी, अब अपना personal email address enter करें और हो जाए तो बताएं।");`
- `say("जी, अब address fill करें — flat या house number, building, street, locality और pincode — सब हो जाए तो बता`
- `say("जी, यह Professional और Employment details का page है — offer fetch करने के लिए ज़रूरी है। पहले employment`
- `say("जी, Salaried मतलब जहाँ monthly salary account में आती है; Self-Employed मतलब खुद का business या practice।`
- `say("जी, Monthly income fill करें — यह आपकी net take-home salary है (tax, bonus, benefits छोड़कर)। हो जाए तो ब`
- `say("जी, अब अपनी organization का नाम enter करें और हो जाए तो बताएं।");`
- `say("जी, अब अपनी official email ID enter करें और हो जाए तो बताएं।");`
- `say("जी, अब organization का address और office pincode (6 digits) fill करें — सब हो जाए तो बताएं।");`
- `say("जी, Net monthly income fill करें — अपनी approximate monthly business earnings। हो जाए तो बताएं।");`
- `say("जी, अब business या company का registered नाम enter करें और हो जाए तो बताएं।");`
- `say("जी, अब business का address और business pincode (6 digits) fill करें — सब हो जाए तो बताएं।");`
- `say("जी, Proceed के बाद Udyam Verification page आएगा — Udyam number और registered mobile number enter करके Sub`
- `say("जी, यह final page है जहाँ आप अपना loan amount और offer देख सकते हैं। क्या आपको loan amount और final offer`
- `say("जी, कोई issue लग रहा है — एक minute, मैं आपको Relationship Manager से connect कर देती हूँ जो help करेंगे।`
- `say("जी, मैं समझती हूँ — पर जो amount आपकी profile पर eligible होगा वही screen पर show होगा, और वहीं से आप अपन`
- `say("जी, Page को एक बार refresh या reload करें — फिर बताएं।");`
- `say("जी, ज़रूर। आप कौन सा दिन और समय prefer करेंगे? हम 10 AM से 7 PM, साथों दिन available रहते हैं।");`
- `say("जी, कोई specific time बता दीजिए।");`
- `say("जी, बिल्कुल! कृपया जल्दी से complete कर दें। धन्यवाद।<EOC/>");`
- `say("जी, मैं प्रिया हूँ, Aditya Birla Capital की तरफ से बोल रही हूँ।");`
- `say("जी, यह बताने के लिए धन्यवाद, यह तो अच्छी बात है — उम्मीद है आप हमारी services से ख़ुश हैं। हम पर भरोसा कर`
- `say("जी, यह बताने के लिए धन्यवाद — मैं इसे हमारी team तक escalate कर देती हूँ। आपके time के लिए धन्यवाद जी।<EO`

</details>

### **हां** added as a lead-in — in 9 place(s)

Real callers open turns with "हां" in 579 calls. Only the lead-in is added; no existing wording changed.

<details><summary>the lines it was added to</summary>

- `say("हां, कोई बात नहीं — हम उन्हें बाद में contact करेंगे। आपका समय देने के लिए धन्यवाद।<EOC/>");`
- `say("हां, कोई बात नहीं, अपना ख़याल रखियेगा। Goodbye.<EOC/>");`
- `say("हां, बढ़िया! आप home screen पर आ गए — नीचे Apply Now button दिखेगा, उस पर click करें, फिर बताएं।");`
- `say("हां, कोई बात नहीं, मैं आपको दोबारा SMS भेज रही हूँ — कुछ ही seconds में आ जाएगा, आ जाए तो बताएं।");`
- `say("हां, कोई बात नहीं — मैं आपको हमारे Relationship Manager से connect कर रही हूँ जो आपकी पूरी help करेंगे, ए`
- `say("हां, कोई बात नहीं — मैं आपको हमारे Relationship Manager से connect कर रही हूँ जो आपकी help करेंगे, एक mom`
- `say("हां, बढ़िया! अब मैं आपको Relationship Manager से connect कर देती हूँ जो आपका KYC process संभालेंगे — कृपय`
- `say("हां, कोई बात नहीं, आपका समय देने के लिए धन्यवाद — आपका दिन शुभ हो।<EOC/>");`
- `say("हां, कोई बात नहीं, आपका समय देने के लिए धन्यवाद — आपका दिन शुभ हो।<EOC/>");`

</details>

---

# New agent speech  (6)

_A new line answering something callers repeatedly say. The agent had no response for this before._

### 1. New line in `loan_intro()`

**The agent will now say:**

> यह offer पहले से आपकी profile के आधार पर pre-select किया गया है, इसलिए सिर्फ़ apply करने से आपकी eligibility या CIBIL पर कोई असर नहीं पड़ता — पूरी details उसी link पर देख लें।

**Why:** eligibility_doubt appears in 14 calls (6%) right at the offer-presentation moment — customers worry a CIBIL check will kill the pre-approval or that the shown amount is too good to be true. This is descriptive grounding only (p=1.0, not causal) but the doubt is real and unanswered today; loan_intro currently states the amount but never addresses the CIBIL/pre-approval trust question, which is a genuinely different angle from the amount/rate line the state already covers.

### 2. New line in `loan_intro_persuade()`

**The agent will now say:**

> अगर rate को लेकर सोच रहे हैं — यह पूरी तरह personalized offer है, actual details उसी page पर दिखेंगे, अभी कोई final commitment नहीं करना।

**Why:** cost_and_terms is the single largest theme (58 calls, 25%), and the KNOWN TRAP confirms rate objectors actually complete BETTER than baseline (22.7% vs 31.4%) — so this is not about preventing drop-off, it is about answering the most common question well without ever stating a number, since compliance forbids stating rate/amount. Placed in loan_intro_persuade because this is where a 'rate ज़्यादा है'-driven disagree lands, and the state currently only has a generic 'daily needs' reassurance with no rate-specific angle.

### 3. New line in `loan_intro_persuade()`

**The agent will now say:**

> अभी सिर्फ़ eligibility check हो रहा है, कोई final decision अभी नहीं लेना — पूरी जानकारी देखने के बाद ही आगे बढ़ें।

**Why:** wants_time (14 calls, 6%) includes real worry about what happens after committing and whether terms lock in permanently. Not causally significant (p=0.5376 for the broader busy_or_later theme) but recurring and currently unaddressed in loan_intro_persuade, which only reassures on the 'daily needs' angle, not on the 'nothing is locked in yet' angle.

### 4. New line in `handle_has_loan_unspecified()`

**The agent will now say:**

> यह process अलग और सिर्फ़ इसी offer के लिए है — अगर कहीं और से पहले से apply किया है, तो भी दोबारा से कोई असर नहीं पड़ेगा, यह बस कुछ ही मिनट का है।

**Why:** already_engaged (14 calls, 6%) is customers worried this call duplicates something already in progress elsewhere (app, PhonePe, branch). handle_has_loan_unspecified already asks if they still want to hear the offer, but never reassures that this specific process is separate and won't conflict with or repeat anything already done — that's the missing angle.

### 5. New line in `handle_security_concern()`

**The agent will now say:**

> यह call भी आपके Aditya Birla Capital से existing relationship के आधार पर ही किया जा रहा है — कोई personal detail share नहीं करनी, सिर्फ़ verification के लिए OTP इस्तेमाल होता है।

**Why:** trust_or_fraud (7 calls, 3%; not causally significant, p=0.1799, trust_doubt actually does better than baseline) is currently only answered from the SMS-link angle ('https lock, ABCL domain verify करें') — but several quotes show the doubt is about the call/agent itself, not the link. Add the missing angle: reassurance that the call itself rides on an existing ABCL relationship and never asks for sensitive data beyond OTP.

### 6. New line in `handle_agent_query()`

**The agent will now say:**

> मैं एक digital assistant हूँ, जो अभी आपकी loan application में मदद कर रही हूँ।

**Why:** is_it_a_bot is small (3 calls, 1%) but the question is asked pointedly and directly, and handle_agent_query currently sidesteps it entirely — it states the agent's name and company but never actually answers whether she is a bot or a person, which is exactly what all three quotes ask.

---

# Rejected by safety checks  (33)

_These were proposed and then blocked automatically. Nothing here reached the prompt._

- **anchor bucket for 'wants_more_amount'** — Samples report shown amount, don't demand higher; one inverted
- **anchor bucket for 'identity_confirm'** — "बोलिए/बोलो" means go ahead, not confirming identity
- **anchor bucket for 'salaried'** — Mostly questions asking about salary, not stating employment
- **anchor bucket for 'prior_attempt_failed'** — Unrelated/garbled turns, no consistent prior-attempt meaning
- **anchor bucket for 'security_concern'** — About link not opening, not fraud/scam suspicion
- **anchor bucket for 'sms_not_received'** — Polarity inverted: SMS arrived, not missing
- **anchor bucket for 'otp_not_received'** — Polarity inverted: OTP received, not missing
- **anchor bucket for 'identity_deny'** — Mixed bag; turns don't say wrong number/not the lead
- **anchor bucket for 'has_loan_unspecified'** — Turns don't state already having an existing loan
- **anchor 'बोलिए' -> affirm** — Generic filler meaning 'go on/tell me', low lift
- **anchor 'ज़रूर' -> affirm** — Weak evidence, likely substring match of ज़रूरी/ज़रूरत
- **anchor 'welcome' -> affirm** — Means 'you're welcome', not an affirmation
- **anchor 'चलिए' -> affirm** — Weak evidence, ambiguous discourse filler word
- **anchor 'line' -> hold** — Weak lift, ambiguous with 'on the line' presence
- **anchor 'just' -> hold** — Generic filler word, high cross-intent misroute risk
- **anchor 'बने' -> hold** — Fragment of fixed IVR script, generic verb form
- **anchor 'कृपया' -> hold** — Generic 'please', appears across all intents
- **anchor 'रखा' -> hold** — Generic verb 'kept', IVR-script co-occurrence artifact
- **anchor 'रहें' -> hold** — Generic verb ending, common outside hold context
- **anchor 'close' -> hold** — Generic, risks misrouting to tech/app-issue speech
- **anchor 'put' -> hold** — Generic English verb, IVR-script artifact
- **anchor 'speaking' -> hold** — Generic word, IVR-script co-occurrence artifact
- **anchor 'व्यक्ति' -> hold** — Generic noun 'person', IVR-script artifact
- **anchor 'back' -> hold** — Generic, 'back button' risks tech_issue misroute
- **anchor 'hit' -> hold** — Generic, 'hit button' risks tech_issue misroute
- **anchor 'उन्होंने' -> hold** — Generic pronoun, no intent-specific meaning
- **anchor 'almost' -> hold** — Generic word, IVR-script co-occurrence artifact
- **anchor 'जाइए' -> hold** — Standalone जाइए means 'go', opposite of hold
- **anchor 'private' -> self_employed** — Ambiguous: 'private job' actually means salaried
- **anchor 'दूं' -> self_employed** — Generic verb ending, co-occurrence artifact
- **anchor 'open' -> tech_issue** — Too generic, used across countless unrelated contexts
- **proposal for 'sms_send'** — sms_send() declares in its own prose that it must not add speech (matched 'Speak ONLY')
- **proposal for 'sms_send'** — sms_send() declares in its own prose that it must not add speech (matched 'Speak ONLY')

