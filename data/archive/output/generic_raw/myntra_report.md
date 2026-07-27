# ABCL Call Context-Graph Report

Calls analyzed: **52** · intents: **28** · transitions: **188**
_(counts are per-turn occurrences across all calls, not number of calls)_

## 1. Keywords by intent (the signal words)

- **agent_answer_query** (217x): processing में है, 30 July तक deliver, complaint register, processing stage पर है, shipping details अभी show नहीं, HRX Sliders
- **customer_ask_question** (164x): shipping हो ही नहीं है, अभी तक मुझे नहीं मिला है, मेरा exchange है, delivery attempt fail, we will deliver it soon, कल तक भी नहीं मिला तो
- **customer_express_frustration** (116x): तीस July तक, ship हुआ नहीं, birthday है मेरी बेटी, अभी तक नहीं हुआ है, details भी नहीं दिख रही, दो दिन हो गए
- **agent_de_escalate** (87x): निराश हैं, priority पर resolve, माफी चाहती हूँ, fast-track करने, wait करना मुश्किल, delay परेशान करने वाला
- **agent_wait** (76x): line पर बने रहिए, status check कर रही हूँ, expert agent से connect, Transferring your call now, Please stay on the line, check कर रही हूँ
- **agent_end_call** (67x): feedback form, call के लिए धन्यवाद, शुक्रिया, दिन शुभ हो, Thank you for calling, Have a great day
- **agent_clarify** (66x): किस order के बारे में, क्या issue है, किसी और चीज़ में मदद, EMI के बारे, Hindi or English only, speak with an expert agent
- **customer_other** (60x): English, english क्यों, मराठी में भी, मराठी or बंगाली, class में बैठा हूं, transfer the call
- **customer_ask_query** (53x): ले नहीं पाई थी, घर पर ही नहीं, order ID है, दो order किया है, gentle cleaner, दोनों
- **agent_greet** (52x): नमस्ते, Welcome to मिंत्रा, service assistant, मीरा, मदद कर सकती हूं, How may I help you
- **customer_acknowledge** (45x): ठीक है करवाइए, जल्दी से deliver हो जाए, बिल्कुल बिल्कुल, हां. नहीं, ठीक है, ठीक है, Ok, ठीक है
- **agent_ask_to_repeat** (37x): फिर से कह सकते हैं, फिर से बता सकते हैं, I didn't quite get that, not sure I understand, I noticed you're silent, शांत हो गए
- **agent_acknowledge** (32x): internal team को notify, निश्चिंत रहें, और कोई help, बात समझ रही हूँ, समझ सकती हूँ, मैं समझ
- **customer_greet** (23x): Hello, नमस्ते madam, hello, am I audible, Hello ma'am
- **customer_end** (22x): thank you so much, Thank you so much, thank you, नहीं thank you, Thank you, धन्यवाद
- **customer_agree** (13x): Yes कीजिए, Alright, हां हां बिल्कुल, Exactly, हां, हां जी, भेज दीजिए
- **customer_unclear** (11x): मतलब, क्या मतलब, क्या, क्या problem से, ठीक नहीं था, can you repeat
- **customer_request_callback** (11x): you contact me, let me know, you call me, call call me, call करने का बोल, मेरा number दो
- **agent_reassure_trust** (9x): digital assistant हूँ, calls नहीं करती हूँ, कोई बात नहीं हुई है, re-checked the latest system status, I can confirm, virtual assistant हूँ
- **customer_express_distrust** (7x): दूसरे number पर, call back, बात हुआ है, बात की है क्या, Are you sure, delivery delayed on the app
- **agent_other** (6x): चुप हो गए, वहाँ हैं, Transferring your call now, are you still there, क्या आप अभी भी वहां हैं
- **customer_disagree** (6x): second second August, को चाहिए, मुझे second August को चाहिए, यह delivery, कल contact करूंगी, पांच छह item बाहर purchase करूंगी
- **customer_request_wait** (5x): एक minute रुकिए, एक minute, एक second
- **agent_confirm** (4x): बिल्कुल, बताइए, ठीक है
- **agent_acknowledge_decline** (2x): Hindi or English only, self pickup, not supported
- **customer_report_unavailable** (2x): not free, nobody is there

## 2. Customer sentiment by intent

- **customer_ask_question**: neutral:102 · frustrated:40 · skeptical:15 · confused:7
- **customer_express_frustration**: frustrated:116
- **customer_other**: confused:40 · neutral:17 · frustrated:3
- **customer_ask_query**: neutral:31 · frustrated:19 · skeptical:2 · confused:1
- **customer_acknowledge**: neutral:43 · happy:2
- **customer_greet**: neutral:23
- **customer_end**: neutral:14 · happy:8
- **customer_agree**: neutral:10 · frustrated:3
- **customer_unclear**: confused:11
- **customer_request_callback**: frustrated:9 · neutral:2
- **customer_express_distrust**: skeptical:4 · distrustful:3
- **customer_disagree**: frustrated:6
- **customer_request_wait**: neutral:5
- **customer_report_unavailable**: neutral:2

## 3. Tool / API calls detected

_Inferred from the agent's words (a proxy, not real tool logs). Count = turns where the tool actually fired._

_(no tool calls detected)_
