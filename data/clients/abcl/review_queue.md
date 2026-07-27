# Review queue — prompt.raven

_Generated 2026-07-27 · client `abcl` · 14 candidate(s), none applied yet_

Every quote below is verbatim from a real call — nothing here is generated. Apply an item with:

```
python run_improve.py <prompt.raven> --client abcl --accept N,M,K
```

| | count |
|---|---|
| Anchor gaps (word missing from an existing intent) | 9 |
| Uncovered clusters (no existing intent fits — needs a person) | 5 |
| — high confidence | 4 |
| — low confidence | 5 |

---

## [1] Add `"बोलिए"` to `affirm`'s recognized phrases

🟡 low confidence · anchor gap · **69 calls** · **1.21x** lift vs. overall corpus

> Common corpus-wide too, not just in this intent's calls — weigh the lift number before accepting.

Real customer turns:

> बोलिए madam क्या करना? है madam? देखते रहो. ठीक है. भिजवा क्या
>
> हां जी, हां जी. जी बोलिए. जी बोलिए.
>
> बोलिए madam बोलिए madam मैं एक दो मैं भी कभी busy रहता हूं ऐसे please phone मत किया करो वहां पर. Hel

**Accept:** `--accept 1`

---

## [2] Uncovered cluster — 55 turns, 41 calls

🔵 uncovered cluster · always needs a person — naming the intent and writing its answer can't be automated

Best guess: `affirm` (0.73)  ·  runner-up: `identity_confirm` (0.72)  ·  margin: **0.00**

Sample turns:

> यह बोलने के लिए पढ़ते यार.  
> <sub>`0139490a-e09f-4efe-bdb1-c91775067e5f-transcript`</sub>
>
> जी बोलिए.  
> <sub>`01cef530-c45c-4522-8149-9959675a2899-transcript`</sub>
>
> जी बोलिए.  
> <sub>`01cef530-c45c-4522-8149-9959675a2899-transcript`</sub>
>
> जी बराबर.  
> <sub>`08145c39-7eeb-406e-a3d2-8307c6632a89-transcript`</sub>
>
> डाल दिया  
> <sub>`1dfb93a4-17cc-46e1-a144-05023c0ccdfe-transcript`</sub>

**Track (no automatic edit possible):** `--accept 2` or `--reject 2`

---

## [3] Uncovered cluster — 55 turns, 32 calls

🔵 uncovered cluster · always needs a person — naming the intent and writing its answer can't be automated

Best guess: `affirm` (0.63)  ·  runner-up: `wants_more_amount` (0.63)  ·  margin: **0.00**

Sample turns:

> Just a second. हां जी ma'am.  
> <sub>`07ea36d9-16fc-4cef-ab7c-939240f1b969-transcript`</sub>
>
> हां जी ma'am बोलिए.  
> <sub>`08145c39-7eeb-406e-a3d2-8307c6632a89-transcript`</sub>
>
> हां ma'am बोलिए ma'am.  
> <sub>`08145c39-7eeb-406e-a3d2-8307c6632a89-transcript`</sub>
>
> हां देखेंगे ma'am देखेंगे.  
> <sub>`08145c39-7eeb-406e-a3d2-8307c6632a89-transcript`</sub>
>
> जी बोलिए ma'am.  
> <sub>`30f7f2d2-2282-44ac-9b96-2b1a364b4575-transcript`</sub>

**Track (no automatic edit possible):** `--accept 3` or `--reject 3`

---

## [4] Uncovered cluster — 32 turns, 27 calls

🔵 uncovered cluster · always needs a person — naming the intent and writing its answer can't be automated

Best guess: `identity_deny` (0.47)  ·  runner-up: `sms_not_received` (0.46)  ·  margin: **0.01**

Sample turns:

> Mobile number.  
> <sub>`16a9075f-33f9-4566-a6fe-4a673bd96d67-transcript`</sub>
>
> अभी फिर लिखा है enter full name, enter mobile number.  
> <sub>`16a9075f-33f9-4566-a6fe-4a673bd96d67-transcript`</sub>
>
> आप mobile number डालो.  
> <sub>`1dfb93a4-17cc-46e1-a144-05023c0ccdfe-transcript`</sub>
>
> अभी वह madam full name और enter mobile number आया.  
> <sub>`24d836c4-9077-42d9-a5af-5e27f4785b2c-transcript`</sub>
>
> कर दिया, mobile number भी डाल दिया.  
> <sub>`314982bf-be67-4d20-b42b-5b149057853f-transcript`</sub>

**Track (no automatic edit possible):** `--accept 4` or `--reject 4`

---

## [5] Uncovered cluster — 26 turns, 18 calls

🔵 uncovered cluster · always needs a person — naming the intent and writing its answer can't be automated

Best guess: `identity_confirm` (0.62)  ·  runner-up: `wants_more_amount` (0.60)  ·  margin: **0.01**

Sample turns:

> बोलिए madam बोलिए.  
> <sub>`0aed797d-2304-4c38-b3f8-7c8cb18aa900-transcript`</sub>
>
> Link खुल गया है madam.  
> <sub>`1dfb93a4-17cc-46e1-a144-05023c0ccdfe-transcript`</sub>
>
> Line पर हो madam अभी detail आगे detail मांग रहा है total.  
> <sub>`1dfb93a4-17cc-46e1-a144-05023c0ccdfe-transcript`</sub>
>
> डाला madam.  
> <sub>`1dfb93a4-17cc-46e1-a144-05023c0ccdfe-transcript`</sub>
>
> Process किया है madam आगे?  
> <sub>`1dfb93a4-17cc-46e1-a144-05023c0ccdfe-transcript`</sub>

**Track (no automatic edit possible):** `--accept 5` or `--reject 5`

---

## [6] Add `"कितना"` to `query_fee`'s recognized phrases

🟢 high confidence · anchor gap · **24 calls** · **2.89x** lift vs. overall corpus

Real customer turns:

> उसको interest कितना पड़ रहा है उसका? Interest Correct madam वह बात correct है. लेकिन मैं interest पू
>
> Ma'am मुझे यह बता सकते हैं कि कितना interest rate करेगा?
>
> Hello. हां, interest कितना है महीना के लिए?

**Accept:** `--accept 6`

---

## [7] Uncovered cluster — 23 turns, 19 calls

🔵 uncovered cluster · always needs a person — naming the intent and writing its answer can't be automated

Best guess: `address_error` (0.41)  ·  runner-up: `wants_more_amount` (0.39)  ·  margin: **0.03**

Sample turns:

> ठीक है ma'am PAN number वन दिया है. एक second.  
> <sub>`07ea36d9-16fc-4cef-ab7c-939240f1b969-transcript`</sub>
>
> हां madam, PAN card की return डाल दूं?  
> <sub>`1ea57f23-69de-49d3-85bf-14ba27500c3c-transcript`</sub>
>
> हां डाल दिया मैंने PAN number डाल दिया  
> <sub>`294cf852-c79b-4a17-814e-247198a60059-transcript`</sub>
>
> PAN number मांग  
> <sub>`3f381582-6f52-4d0d-ac8d-159b929012ce-transcript`</sub>
>
> अब PAN number में full name ऐसा दिखा रहा है.  
> <sub>`5e6f5156-d740-4411-ad42-6eb44f45d747-transcript`</sub>

**Track (no automatic edit possible):** `--accept 7` or `--reject 7`

---

## [8] Add `"fees"` to `query_fee`'s recognized phrases

🟢 high confidence · anchor gap · **7 calls** · **3.58x** lift vs. overall corpus

Real customer turns:

> जो quotation आप अगर बता दिए तो मैं इसके साथ apply कर ले सकता था. Direct apply कर लेंगे बोलो तो कैसा 
>
> और फिर interest क्या लगेगा? लेकिन इसमें तो interest बहुत लग रहा है ना? यह तो उन्नीस सौ पच्चीस होता र
>
> Hello. इसमें interest वगैरह कितना EMI कितनी आएगी? कितने महीने का है? Madam ब्याज ज़्यादा नहीं है? दो

**Accept:** `--accept 8`

---

## [9] Add `"कितने"` to `query_fee`'s recognized phrases

🟡 low confidence · anchor gap · **7 calls** · **1.91x** lift vs. overall corpus

> Common corpus-wide too, not just in this intent's calls — weigh the lift number before accepting.

Real customer turns:

> नहीं इसकी जानकारी तो चाहिए ma'am क्या rate है interest rate क्या है? कैसे है? मतलब last कितने जाती ह
>
> Ma'am इसका बताओ अपनी कर रहे हो उसका per month कितना आएगा कितने साल के लिए रहेगा?
>
> Hello. इसमें interest वगैरह कितना EMI कितनी आएगी? कितने महीने का है? Madam ब्याज ज़्यादा नहीं है? दो

**Accept:** `--accept 9`

---

## [10] Add `"address"` to `address_error`'s recognized phrases

🟡 low confidence · anchor gap · **7 calls** · **1.59x** lift vs. overall corpus

> Common corpus-wide too, not just in this intent's calls — weigh the lift number before accepting.

Real customer turns:

> इसमें address cannot have leading training space और consecutive space ऐसा लिखता है. school इसमें भी 
>
> हां हां. तो फिर से आगे नहीं हो रहा है. Address cannot have bleeding dialing space or constructive sp
>
> Email address डाल दिया, flat ना मकान का number डाल दिया, address डाल दिया. PIN code डाला, अभी procee

**Accept:** `--accept 10`

---

## [11] Add `"problem"` to `address_error`'s recognized phrases

🟢 high confidence · anchor gap · **5 calls** · **3.89x** lift vs. overall corpus

Real customer turns:

> इधर internet problem है.
>
> जो problem है ना surname मेरा आगे पीछे लिखा है आधार card मैंने PAN card
>
> हां. नहीं आ रहा है sir network का problem है. अभी रात आठ घंटे का बाद देखती हूं तब शायद network का pr

**Accept:** `--accept 11`

---

## [12] Add `"space"` to `address_error`'s recognized phrases

🟢 high confidence · anchor gap · **5 calls** · **4.54x** lift vs. overall corpus

Real customer turns:

> इसमें address cannot have leading training space और consecutive space ऐसा लिखता है. school इसमें भी 
>
> हां हां. तो फिर से आगे नहीं हो रहा है. Address cannot have bleeding dialing space or constructive sp
>
> Actually, address is not taking. Address cannot have a leading training space. Like that. दिक़्क़त P

**Accept:** `--accept 12`

---

## [13] Add `"ज़रूर"` to `affirm`'s recognized phrases

🟡 low confidence · anchor gap · **4 calls** · **1.36x** lift vs. overall corpus

> Common corpus-wide too, not just in this intent's calls — weigh the lift number before accepting.

Real customer turns:

> शुक्रिया, मेरा नाम ठीक से लेने के लिए. जी हां, आप मुझसे थोड़ी देर के लिए वार्तालाप कर सकते हैं. बताइ
>
> बात कर सकते हैं. हां ज़रूर कर सकते हैं.
>
> बोलो. हां हां शुरू ticket का. हां. हमको लोगों के ज़रूरी आए तब बोलता आए तो ले लेगा. हां भेज दियो हमें

**Accept:** `--accept 13`

---

## [14] Add `"चलिए"` to `affirm`'s recognized phrases

🟡 low confidence · anchor gap · **2 calls** · **1.36x** lift vs. overall corpus

> Common corpus-wide too, not just in this intent's calls — weigh the lift number before accepting.

Real customer turns:

> शुक्रिया, मेरा नाम ठीक से लेने के लिए. जी हां, आप मुझसे थोड़ी देर के लिए वार्तालाप कर सकते हैं. बताइ
>
> हां, बोलो ना. हां चलेगा madam. चलिए ठीक है madam. Thank you. ऐसा करने का madam.

**Accept:** `--accept 14`

---
