# Per-turn intent capture

Every turn of every call — who spoke, the intent, sentiment, tool/API call, and the signal keywords.

## Call GEN-myntra-0187a2f3-146a-49fe-aa85-4608021e6b88 (completed) — 18 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, service assistant
1   customer  customer_ask_question             neutral     —             shipping हो ही नहीं है
2   agent     agent_wait                        —           —             line पर बने रहिए, status check कर रही हूँ
3   agent     agent_answer_query                —           —             processing में है, 30 July तक deliver, complaint register
4   customer  customer_express_frustration      frustrated  —             तीस July तक, ship हुआ नहीं
5   agent     agent_de_escalate                 —           —             निराश हैं, priority पर resolve
6   customer  customer_express_frustration      frustrated  —             birthday है मेरी बेटी, अभी तक नहीं हुआ है
7   agent     agent_de_escalate                 —           —             माफी चाहती हूँ, fast-track करने
8   customer  customer_express_frustration      frustrated  —             details भी नहीं दिख रही
9   agent     agent_answer_query                —           —             processing stage पर है, shipping details अभी show नहीं
10  customer  customer_acknowledge              neutral     —             ठीक है करवाइए
11  agent     agent_acknowledge                 —           —             internal team को notify
12  customer  customer_acknowledge              neutral     —             जल्दी से deliver हो जाए
13  agent     agent_acknowledge                 —           —             निश्चिंत रहें
14  customer  customer_end                      happy       —             thank you so much
15  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
16  customer  customer_acknowledge              happy       —             बिल्कुल बिल्कुल
17  agent     agent_end_call                    —           —             शुक्रिया, दिन शुभ हो
```

## Call GEN-myntra-0233cd8a-563a-4046-a4f5-9dd3914e3dda (completed) — 17 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, मीरा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order के बारे में, क्या issue है
3   customer  customer_ask_question             neutral     —             अभी तक मुझे नहीं मिला है
4   agent     agent_wait                        —           —             line पर बने रहिए
5   agent     agent_answer_query                —           —             HRX Sliders
6   agent     agent_answer_query                —           —             shipped हैं, आठ बजे तक मिल जाएगा
7   customer  customer_express_frustration      frustrated  —             दो दिन हो गए, अभी तक नहीं मिला
8   agent     agent_de_escalate                 —           —             wait करना मुश्किल
9   customer  customer_acknowledge              neutral     —             हां. नहीं
10  agent     agent_acknowledge                 —           —             और कोई help
11  customer  customer_express_frustration      frustrated  —             cancel कर दूंगा
12  agent     agent_de_escalate                 —           —             delay परेशान करने वाला, माफी
13  agent     agent_ask_to_repeat               —           —             फिर से कह सकते हैं
14  customer  customer_acknowledge              neutral     —             ठीक है, ठीक है
15  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
16  agent     agent_end_call                    —           —             Thank you for calling, Have a great day
```

## Call GEN-myntra-07d09941-fee0-44d8-997e-da85a495ee04 (completed) — 16 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             मेरा exchange है
2   customer  customer_ask_question             frustrated  —             delivery attempt fail, we will deliver it soon
3   agent     agent_answer_query                —           —             shipped है, कल तक deliver, complaint already register
4   customer  customer_express_frustration      frustrated  —             आज नहीं मिलेगा, कल मिलेगा
5   agent     agent_de_escalate                 —           —             झुंझलाहट होती है, भरोसा रखें
6   customer  customer_ask_question             skeptical   —             कल तक भी नहीं मिला तो
7   agent     agent_answer_query                —           —             immediately escalate, priority पर track
8   agent     agent_ask_to_repeat               —           —             फिर से कह सकते हैं
9   customer  customer_express_frustration      frustrated  —             delay नहीं होते थे, हमेशा
10  agent     agent_de_escalate                 —           —             माफी चाहती हूँ, delivery services को बेहतर
11  customer  customer_acknowledge              neutral     —             Ok, ठीक है
12  agent     agent_clarify                     —           —             किसी और चीज़ में मदद
13  customer  customer_acknowledge              neutral     —             बस यही था
14  agent     agent_end_call                    —           —             feedback form, धन्यवाद
15  agent     agent_end_call                    —           —             feedback form, धन्यवाद
```

## Call GEN-myntra-0f649c73-756b-404c-b8a3-cdf82c053800 (transferred) — 32 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             नमस्ते madam
2   agent     agent_clarify                     —           —             किस order के बारे में
3   customer  customer_ask_question             neutral     —             pickup किए, Stay free
4   customer  customer_express_frustration      frustrated  —             emergency, delay कर रहे हैं
5   agent     agent_answer_query                —           —             Stayfree Sanitary Napkins, आठ बजे तक deliver
6   customer  customer_express_frustration      frustrated  —             आज शाम ही
7   customer  customer_express_frustration      frustrated  —             जल्दी कीजिए
8   agent     agent_answer_query                —           —             रास्ते में है, location के पास पहुँचते ही
9   customer  customer_express_frustration      frustrated  —             अभी का अभी चाहिए
10  agent     agent_de_escalate                 —           —             urgency समझ सकती हूँ
11  customer  customer_other                    confused    —             —
12  agent     agent_ask_to_repeat               —           —             फिर से बता सकते हैं
13  customer  customer_other                    confused    —             —
14  agent     agent_answer_query                —           —             रास्ते में है, आठ बजे तक
15  customer  customer_express_frustration      frustrated  —             Emergency है
16  customer  customer_express_frustration      frustrated  —             अभी का अभी चाहिए
17  agent     agent_de_escalate                 —           —             urgency बिलकुल जायज़
18  customer  customer_express_frustration      frustrated  —             मेरा ही order drop करना चाहिए
19  agent     agent_acknowledge                 —           —             बात समझ रही हूँ
20  customer  customer_express_frustration      frustrated  —             देख लेना मैं क्या होएगा
21  agent     agent_answer_query                —           —             priority पर है, आठ बजे तक पहुँच जाएगा
22  customer  customer_express_frustration      frustrated  —             अभी का अभी चाहिए, दोपहर के पहले
23  agent     agent_answer_query                —           —             दोपहर तक ही order, fastest route पर है
24  customer  customer_ask_question             frustrated  —             contact को डाल दीजिए, दिल्ली agent
25  agent     agent_answer_query                —           —             out for delivery नहीं है, My Orders page
26  customer  customer_express_frustration      frustrated  —             अच्छी service नहीं दे सकते
27  agent     agent_de_escalate                 —           —             निराशा समझ सकती हूँ, expert agent से connect
28  customer  customer_agree                    neutral     —             Yes कीजिए
29  agent     agent_wait                        —           —             line पर बने रहिए, expert agent से connect
30  customer  customer_other                    confused    —             —
31  agent     agent_wait                        —           —             Transferring your call now
```

## Call GEN-myntra-11c29762-2ab5-47b5-a2f6-910176fde0d5 (transferred) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order के बारे में
3   customer  customer_ask_question             neutral     —             status नहीं update थी
4   agent     agent_wait                        —           —             line पर बने रहिए
5   agent     agent_answer_query                —           —             TAPOM Watch, 30 July तक deliver, complaint पहले से registered
6   customer  customer_ask_question             skeptical   —             क्या निश्चय
7   agent     agent_answer_query                —           —             मेरा मतलब था
8   agent     agent_ask_to_repeat               —           —             फिर से कह सकते हैं
9   customer  customer_express_frustration      frustrated  —             Twenty fourth को deliver होना था, thirtieth तक
10  agent     agent_de_escalate                 —           —             परेशान करने वाला है, माफी चाहती हूँ
11  customer  customer_express_frustration      frustrated  —             नेहरू place switch हो चुका है, इतना time
12  agent     agent_de_escalate                 —           —             नेहरू place पहुँचने के बाद भी delay
13  customer  customer_express_frustration      frustrated  —             birthday उसका आज था, gift
14  agent     agent_de_escalate                 —           —             birthday gift के लिए यह delay
15  customer  customer_express_frustration      frustrated  —             ऐसे थोड़ी ना होता है
16  agent     agent_de_escalate                 —           —             दिल से माफ़ी, expert agent से connect
17  customer  customer_end                      neutral     —             Thank you so much
18  agent     agent_end_call                    —           —             आपका बहुत बहुत
```

## Call GEN-myntra-13669124-51be-40fe-8933-86ece32f58e6 (transferred) — 74 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             Where is my order
2   agent     agent_wait                        —           —             Please stay on the line
3   agent     agent_answer_query                —           —             Track Pants, packed and ready for dispatch, delivered today
4   customer  customer_other                    confused    —             —
5   agent     agent_ask_to_repeat               —           —             I didn't quite get that
6   customer  customer_other                    confused    —             —
7   agent     agent_ask_to_repeat               —           —             not sure I understand
8   customer  customer_ask_question             neutral     —             where is my order
9   agent     agent_answer_query                —           —             packed है, dispatch होने के लिए तैयार, priority पर है
10  customer  customer_unclear                  confused    —             मतलब
11  agent     agent_answer_query                —           —             pack हो चुका है, warehouse से निकल जाएगा
12  customer  customer_ask_question             neutral     —             आज कब तक
13  agent     agent_answer_query                —           —             आज deliver हो जाएगा
14  customer  customer_ask_question             neutral     —             कितने बजे तक
15  agent     agent_answer_query                —           —             out for delivery होगा, delivery agent
16  agent     agent_ask_to_repeat               —           —             I noticed you're silent
17  customer  customer_express_frustration      frustrated  —             exact location, five hundred percent
18  agent     agent_acknowledge                 —           —             समझ सकती हूँ
19  customer  customer_other                    confused    —             —
20  agent     agent_answer_query                —           —             packed है और dispatch होने वाला, warehouse में है
21  customer  customer_other                    confused    —             —
22  customer  customer_ask_question             frustrated  —             थोड़ा जल्दी चाहिए, एक दो घंटे
23  agent     agent_answer_query                —           —             fastest route पर है, packed status में है
24  customer  customer_express_frustration      frustrated  —             थोड़ा जल्दी बहुत समझे
25  agent     agent_answer_query                —           —             priority पर है, dispatch होने की प्रक्रिया
26  agent     agent_ask_to_repeat               —           —             शांत हो गए
27  customer  customer_express_frustration      frustrated  —             क्या मदद आ रही हो भाई
28  agent     agent_answer_query                —           —             पूरी मदद करने की कोशिश, packed status में है
29  customer  customer_other                    confused    —             —
30  agent     agent_acknowledge                 —           —             मैं समझ
31  customer  customer_ask_question             frustrated  —             delivery boy का number भी नहीं मिला
32  agent     agent_answer_query                —           —             out for delivery हो जाता है, delivery boy का number
33  customer  customer_other                    confused    —             —
34  agent     agent_ask_to_repeat               —           —             कृपया बताइए
35  customer  customer_other                    confused    —             —
36  agent     agent_acknowledge                 —           —             मैं समझ सकती
37  customer  customer_other                    confused    —             —
38  agent     agent_acknowledge                 —           —             अपने item के बारे में
39  customer  customer_other                    confused    —             —
40  agent     agent_acknowledge                 —           —             —
41  customer  customer_acknowledge              neutral     —             हो जाएगा तब number मिलेगा
42  agent     agent_answer_query                —           —             out for delivery हो जाएगा, number मिल जाएगा
43  customer  customer_ask_question             neutral     —             कितनी process हो रहे हैं
44  agent     agent_answer_query                —           —             order अभी packed
45  customer  customer_ask_question             neutral     —             कितनी process और है
46  agent     agent_answer_query                —           —             pack हो चुका है, dispatch होगा, delivery agent के पास पहुँचेगा
47  customer  customer_ask_question             neutral     —             EMI
48  agent     agent_clarify                     —           —             EMI के बारे
49  customer  customer_ask_question             neutral     —             warehouse में नहीं ले सकता हूं
50  agent     agent_answer_query                —           —             self pickup संभव नहीं है
51  customer  customer_acknowledge              neutral     —             थोड़ा सा जल्दी चाहिए था
52  agent     agent_answer_query                —           —             urgency का पूरा ध्यान
53  customer  customer_unclear                  confused    —             क्या मतलब
54  agent     agent_answer_query                —           —             मेरा मतलब
55  customer  customer_acknowledge              neutral     —             कोई दिक्कत नहीं है
56  agent     agent_acknowledge                 —           —             समझ के लिए धन्यवाद
57  agent     agent_ask_to_repeat               —           —             अभी भी वहाँ हैं
58  customer  customer_other                    confused    —             —
59  agent     agent_ask_to_repeat               —           —             didn't quite understand
60  customer  customer_other                    confused    —             —
61  agent     agent_ask_to_repeat               —           —             didn't quite catch that
62  customer  customer_other                    neutral     —             English
63  agent     agent_answer_query                —           —             आप English में बात कर सकते हैं
64  customer  customer_other                    neutral     —             english क्यों
65  agent     agent_answer_query                —           —             जिस भी भाषा में चाहें
66  customer  customer_other                    neutral     —             मराठी में भी
67  agent     agent_clarify                     —           —             Hindi or English only, speak with an expert agent
68  customer  customer_other                    neutral     —             मराठी or बंगाली
69  agent     agent_clarify                     —           —             Hindi or English only, expert agent for better assistance
70  customer  customer_agree                    neutral     —             Alright
71  agent     agent_acknowledge                 —           —             Since you've agreed
72  customer  customer_other                    confused    —             —
73  agent     agent_wait                        —           —             Transferring your call now
```

## Call GEN-myntra-1624f301-ebc7-475c-9b05-4573cc4a69a7 (incomplete) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             skeptical   —             contacted you all twice, trolley bag
2   agent     agent_answer_query                —           —             Safari Trolley Bag, out for delivery, 24 hours
3   customer  customer_express_frustration      frustrated  —             nobody is calling, nobody is picking up
4   agent     agent_de_escalate                 —           —             माफी चाहती हूँ, definitely आपको मिल जाएगा
5   customer  customer_ask_question             skeptical   —             Yes or no
6   agent     agent_answer_query                —           —             जवाब 'हाँ' है, 24 hours में
7   agent     agent_clarify                     —           —             किसी और चीज़ में मदद
8   customer  customer_express_frustration      frustrated  —             delivery boy to contact me
9   agent     agent_answer_query                —           —             already out for delivery
10  customer  customer_acknowledge              neutral     —             मालूम है
11  agent     agent_acknowledge                 —           —             बात समझ गई
12  customer  customer_express_frustration      frustrated  —             out for delivery किधर है
13  agent     agent_answer_query                —           —             delivery team को notify
14  customer  customer_request_callback         neutral     —             you contact me, let me know
15  agent     agent_acknowledge                 —           —             निश्चिंत रहें
16  customer  customer_end                      happy       —             thank you
17  agent     agent_end_call                    —           —             बहुत धन्यवाद
18  customer  customer_request_callback         neutral     —             you call me, let me know
```

## Call GEN-myntra-167d6ba2-7af5-4630-8ac3-0f875af21ac6 (completed) — 21 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             यह एक मेरा order था
2   agent     agent_clarify                     —           —             problem delivery
3   customer  customer_other                    confused    —             —
4   agent     agent_clarify                     —           —             delivery से related है या return से
5   customer  customer_ask_question             neutral     —             nearest मेरे municipality पर आ चुका है, आज deliver हो जाता है
6   agent     agent_wait                        —           —             line पर बने रहिए
7   agent     agent_answer_query                —           —             नॉटिका Shirt, मुंशीपुलिया hub, कल तक deliver
8   agent     agent_answer_query                —           —             fastest route पर है
9   customer  customer_ask_question             neutral     —             आज नहीं हूं
10  agent     agent_answer_query                —           —             आज ही order चाहिए, कल तक
11  customer  customer_ask_question             neutral     —             आज जी जी
12  agent     agent_answer_query                —           —             आज ही delivery चाहिए, कल तक deliver होने की उम्मीद
13  customer  customer_ask_question             neutral     —             आज मिल जाता ज़्यादा बेहतर था
14  agent     agent_answer_query                —           —             बात समझ रही हूँ
15  customer  customer_express_frustration      frustrated  —             same repeat कर रहे हो
16  agent     agent_de_escalate                 —           —             परेशानी समझ रही हूँ, request note कर लेती हूँ
17  customer  customer_ask_question             frustrated  —             four five kilometer, ज़्यादा दूर नहीं है
18  agent     agent_answer_query                —           —             delivery process system के हिसाब से
19  customer  customer_end                      neutral     —             नहीं thank you
20  agent     agent_end_call                    —           —             स्वागत है, feedback form
```

## Call GEN-myntra-1963c4c5-46ea-4942-92b7-7670c3338580 (incomplete) — 15 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             अभी कहां पर आया
2   agent     agent_wait                        —           —             line पर बने रहिए, check कर रही हूँ
3   agent     agent_answer_query                —           —             shipped है, शाम आठ बजे तक
4   customer  customer_ask_question             neutral     —             कब तक मिल जाएगा
5   agent     agent_answer_query                —           —             शाम आठ बजे तक deliver
6   customer  customer_acknowledge              neutral     —             आठ
7   agent     agent_answer_query                —           —             आठ बजे तक
8   customer  customer_ask_question             neutral     —             order कहां आया है, कब तक आया है
9   customer  customer_other                    neutral     —             class में बैठा हूं
10  agent     agent_answer_query                —           —             आठ बजे तक deliver, class खत्म होने के बाद
11  customer  customer_ask_question             neutral     —             number मिल जाएंगे
12  agent     agent_answer_query                —           —             out for delivery नहीं है, details available नहीं
13  customer  customer_unclear                  confused    —             क्या
14  agent     agent_answer_query                —           —             out for delivery नहीं है
```

## Call GEN-myntra-21691136-c5b5-478e-ab9b-91979993fb3a (completed) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             I had ordered, Flip flop
2   agent     agent_answer_query                —           —             I understand you are asking about your order
3   customer  customer_express_frustration      frustrated  —             we have attempted the delivery, nobody has come
4   customer  customer_express_frustration      frustrated  —             wrong information, very false information
5   agent     agent_de_escalate                 —           —             I can understand how frustrating
6   customer  customer_express_frustration      frustrated  —             waiting since, twenty third of July
7   agent     agent_answer_query                —           —             shipped and is expected to reach you by tomorrow, complaint is already registered
8   agent     agent_acknowledge                 —           —             monitoring this closely
9   customer  customer_ask_question             frustrated  —             can it be delivered, by today
10  agent     agent_answer_query                —           —             fastest available route, expected to reach you by tomorrow
11  agent     agent_end_call                    —           —             feedback form via SMS
12  customer  customer_acknowledge              neutral     —             Ok fine
13  agent     agent_end_call                    —           —             feedback
14  customer  customer_acknowledge              neutral     —             Ok fine, no problem
15  agent     agent_end_call                    —           —             feedback form via SMS, Thank you for calling
16  agent     agent_end_call                    —           —             Thank you for calling
17  customer  customer_end                      neutral     —             Thank you
18  agent     agent_end_call                    —           —             Thank you for calling, Have a great day
```

## Call GEN-myntra-222cf3fe-d661-4d60-9258-f189fd83638a (completed) — 37 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order के बारे में, क्या issue है
3   customer  customer_ask_query                neutral     —             ले नहीं पाई थी, घर पर ही नहीं
4   customer  customer_ask_question             neutral     —             number दे दीजिए, बच्चे school लेकर जाना है
5   agent     agent_answer_query                —           —             out for delivery नहीं है, details उपलब्ध नहीं
6   agent     agent_acknowledge                 —           —             —
7   customer  customer_ask_question             neutral     —             कल आया था, ले नहीं पाई है
8   agent     agent_clarify                     —           —             कौन सा product, order ID
9   customer  customer_other                    confused    —             —
10  agent     agent_ask_to_repeat               —           —             समझ नहीं आया, product का नाम
11  customer  customer_agree                    neutral     —             हां हां बिल्कुल
12  agent     agent_wait                        —           —             order list check, line पर बने रहिए
13  customer  customer_other                    confused    —             —
14  agent     agent_answer_query                —           —             list में दो
15  customer  customer_request_wait             neutral     —             एक minute रुकिए
16  agent     agent_wait                        —           —             आराम से, line पर ही हूँ
17  customer  customer_acknowledge              neutral     —             ok ok ok
18  agent     agent_clarify                     —           —             order number share
19  agent     agent_other                       —           —             चुप हो गए, वहाँ हैं
20  customer  customer_ask_query                neutral     —             order ID है
21  agent     agent_ask_to_repeat               —           —             अधूरा लग रहा है, फिर से बता सकते हैं
22  customer  customer_other                    confused    —             —
23  agent     agent_answer_query                —           —             rarethread Kurta
24  customer  customer_other                    neutral     —             —
25  agent     agent_ask_to_repeat               —           —             अधूरा लग रहा है
26  customer  customer_express_frustration      frustrated  —             मैं बता रही हूं ना
27  customer  customer_other                    neutral     —             —
28  agent     agent_wait                        —           —             धन्यवाद, line पर बने रहिए
29  agent     agent_answer_query                —           —             out for delivery है, 24 hours में deliver
30  agent     agent_acknowledge                 —           —             —
31  customer  customer_ask_question             neutral     —             agent का number मिल जाएगा
32  agent     agent_answer_query                —           —             My Orders page
33  agent     agent_acknowledge                 —           —             —
34  customer  customer_end                      neutral     —             thank you
35  agent     agent_end_call                    —           —             feedback form, धन्यवाद
36  agent     agent_end_call                    —           —             एसएमएस पर
```

## Call GEN-myntra-25e87c49-b0ae-48b5-832c-1e677bb951df (incomplete) — 22 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order के बारे में, क्या issue है
3   customer  customer_ask_question             neutral     —             कभी तक आ जाएगा
4   agent     agent_answer_query                —           —             shipped है, शाम आठ बजे तक
5   customer  customer_ask_question             neutral     —             exact time बता सकते हो
6   agent     agent_answer_query                —           —             exact time slots, call करेंगे
7   customer  customer_ask_question             neutral     —             कितने बजे तक आएगा
8   agent     agent_answer_query                —           —             शाम आठ बजे तक, possible नहीं है
9   customer  customer_acknowledge              neutral     —             शाम आठ बजे तक
10  agent     agent_confirm                     —           —             बिल्कुल
11  customer  customer_express_frustration      frustrated  —             जल्दी चाहिए था
12  agent     agent_de_escalate                 —           —             जल्दी चाहिए, fastest route
13  agent     agent_ask_to_repeat               —           —             माफ़ कीजिये, फिर से बोल सकते हैं
14  customer  customer_express_frustration      frustrated  —             थोड़ा जल्दी चलेगा, मतलब नहीं रहेगा
15  customer  customer_ask_question             frustrated  —             जल्द से जल्द, कितना बजे तक
16  agent     agent_de_escalate                 —           —             समझ सकती हूँ, जल्दी चाहिए
17  customer  customer_express_frustration      frustrated  —             कम से कम चार पांच
18  agent     agent_de_escalate                 —           —             urgency समझ सकती हूँ, possible नहीं है
19  customer  customer_acknowledge              neutral     —             ठीक है चलेगा
20  agent     agent_acknowledge                 —           —             धन्यवाद
21  agent     agent_ask_to_repeat               —           —             क्षमा करें, फिर कह सकते हैं
```

## Call GEN-myntra-2633b770-5487-421c-9f84-01ee39c69eba (completed) — 16 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             आज आ सकता है क्या
2   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
3   agent     agent_answer_query                —           —             shipped है, शाम आठ बजे तक
4   customer  customer_express_frustration      frustrated  —             बार बार ऐसा ही होता, late delivery हुआ था
5   agent     agent_de_escalate                 —           —             परेशान हैं, माफी चाहती हूँ
6   customer  customer_ask_question             skeptical   —             नहीं आया तो
7   agent     agent_answer_query                —           —             फिक्र न करें, दोबारा contact कर सकते हैं
8   customer  customer_ask_query                neutral     —             दो order किया है, gentle cleaner
9   agent     agent_answer_query                —           —             दो product order किए हैं
10  customer  customer_ask_question             neutral     —             दोनों आज ही आऐंगे
11  agent     agent_wait                        —           —             check कर रही हूँ, line पर बने रहिए
12  agent     agent_answer_query                —           —             शाम आठ बजे तक deliver, निश्चिंत रहें
13  customer  customer_end                      neutral     —             धन्यवाद
14  agent     agent_end_call                    —           —             feedback form, धन्यवाद
15  agent     agent_end_call                    —           —             feedback form, धन्यवाद
```

## Call GEN-myntra-3024d521-a430-49f2-9821-7f9f3b6b791a (transferred) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             regarding one of my order
2   customer  customer_ask_question             neutral     —             when can I expect it
3   agent     agent_wait                        —           —             check the status, stay on the line
4   agent     agent_answer_query                —           —             currently processing, complaint has already been registered, expected to be delivered by 30 July
5   customer  customer_ask_question             frustrated  —             when can I expect, what is the date
6   agent     agent_answer_query                —           —             30 July
7   customer  customer_ask_question             neutral     —             speak in English
8   agent     agent_answer_query                —           —             speak in English, expected to be delivered by 30 July
9   customer  customer_express_frustration      frustrated  —             अरे यार, not getting delivered
10  agent     agent_de_escalate                 —           —             I completely
11  customer  customer_express_frustration      frustrated  —             got delayed, more than a week
12  customer  customer_ask_question             frustrated  —             current status, by what date
13  agent     agent_de_escalate                 —           —             delay is frustrating, expected to reach you by 30 July
14  customer  customer_other                    frustrated  —             transfer the call, higher management
15  agent     agent_clarify                     —           —             expert agent
16  customer  customer_agree                    neutral     —             Exactly
17  agent     agent_wait                        —           —             connecting you, stay on the line
18  agent     agent_wait                        —           —             Transferring your call, specialized team
```

## Call GEN-myntra-37fe88c1-3d17-4239-ac0d-973fb9c7e6c3 (incomplete) — 23 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   agent     agent_ask_to_repeat               —           —             still there
2   agent     agent_ask_to_repeat               —           —             say that again
3   agent     agent_ask_to_repeat               —           —             say that again
4   customer  customer_other                    neutral     —             हिंदी
5   agent     agent_greet                       —           —             नमस्ते, मदद कर सकती हूं
6   customer  customer_ask_question             confused    —             order नहीं रह रहा हूं
7   agent     agent_wait                        —           —             status check, line पर बने रहिए
8   agent     agent_answer_query                —           —             shipped है, शाम आठ बजे तक
9   customer  customer_ask_query                neutral     —             दोनों
10  agent     agent_clarify                     —           —             किसी और order, details बता दीजिए
11  customer  customer_ask_query                neutral     —             चंदा momma, show हुआ है
12  agent     agent_wait                        —           —             order list check, line पर बने रहिए
13  agent     agent_ask_to_repeat               —           —             still there
14  customer  customer_acknowledge              neutral     —             Hello
15  agent     agent_answer_query                —           —             दो Kurta Sets, दोनों orders से related
16  customer  customer_ask_question             neutral     —             आऐंगे ना
17  agent     agent_wait                        —           —             status check, line पर बने रहिए
18  agent     agent_answer_query                —           —             shipped हैं, शाम आठ बजे तक
19  customer  customer_ask_question             neutral     —             कब price किया था
20  agent     agent_answer_query                —           —             18 July, place किए गए
21  customer  customer_ask_question             neutral     —             price क्या है
22  agent     agent_answer_query                —           —             price की details नहीं हैं, My Orders section
```

## Call GEN-myntra-3b523c8e-1524-4598-a406-9c1da2a0b034 (completed) — 24 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order, क्या issue है
3   customer  customer_ask_query                neutral     —             order देखी
4   agent     agent_clarify                     —           —             problem delivery
5   customer  customer_other                    confused    —             —
6   agent     agent_clarify                     —           —             delivery से related, return से
7   customer  customer_unclear                  confused    —             क्या problem से
8   agent     agent_clarify                     —           —             delivery से related, return
9   customer  customer_ask_query                frustrated  —             अभी तक order नहीं हुई
10  agent     agent_wait                        —           —             order list check
11  customer  customer_other                    confused    —             —
12  agent     agent_answer_query                —           —             shipped है, कल तक deliver, complaint already register
13  customer  customer_express_frustration      frustrated  —             मैं क्या करूं, कितने सारे कल आ चुके थे
14  agent     agent_de_escalate                 —           —             फिक्र न करें, तुरंत resolve करेंगे
15  customer  customer_other                    confused    —             —
16  agent     agent_acknowledge                 —           —             —
17  customer  customer_acknowledge              neutral     —             ठीक थी
18  agent     agent_end_call                    —           —             एसएमएस पर
19  customer  customer_unclear                  confused    —             ठीक नहीं था
20  agent     agent_clarify                     —           —             कुछ और पूछना है, कोई और problem
21  customer  customer_acknowledge              neutral     —             इतना ही problem था
22  agent     agent_end_call                    —           —             feedback form, धन्यवाद
23  agent     agent_end_call                    —           —             Thank you for calling, great day
```

## Call GEN-myntra-455278e1-77db-4b28-a25e-0599ed37402b (completed) — 20 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             आप किस order के बारे में बात करना चाहते हैं, क्या issue है
3   customer  customer_greet                    neutral     —             Hello
4   agent     agent_clarify                     —           —             आप किस order के बारे में बात करना
5   customer  customer_ask_query                neutral     —             मैंने अभी just order किया है
6   agent     agent_ask_to_repeat               —           —             आप किस order के बारे में बात करना चाहते हैं
7   customer  customer_ask_query                neutral     —             मैंने just अभी जो order किया है, उसके बारे में बात करना चाहती हूं
8   agent     agent_clarify                     —           —             problem delivery से related है, या return से
9   customer  customer_ask_question             neutral     —             Delivery से related है, second August को मिल सकता है
10  agent     agent_wait                        —           —             status check कर रही हूँ, कृपया line पर बने रहिए
11  agent     agent_answer_query                —           —             processing में है, 3 August तक deliver होने की उम्मीद है, delivery date change नहीं कर सकते
12  customer  customer_disagree                 frustrated  —             second second August, को चाहिए
13  agent     agent_acknowledge                 —           —             मै समझ सकती हूँ
14  customer  customer_disagree                 frustrated  —             मुझे second August को चाहिए, यह delivery
15  agent     agent_answer_query                —           —             2 August तक चाहिए, processing में है, 3 August तक deliver होने की उम्मीद है, Delivery date change करना हमारे हाथ में नहीं
16  agent     agent_clarify                     —           —             किसी और चीज़ में मदद कर सकती हूँ
17  customer  customer_acknowledge              neutral     —             No thanks
18  agent     agent_end_call                    —           —             feedback form, अच्छी रेटिंग, call के लिए धन्यवाद
19  agent     agent_end_call                    —           —             Thank you for calling मिंत्रा, Have a great day
```

## Call GEN-myntra-5295bb0c-0620-4011-a0c6-7a6c8b58360f (transferred) — 28 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             order के बारे में पूछना था
2   customer  customer_ask_query                neutral     —             दो बार, customer care service, call किया
3   customer  customer_ask_query                frustrated  —             your order is in your prior, अभी तक वह order पहुंचा नहीं है
4   customer  customer_express_frustration      frustrated  —             logistic department से कोई coordination नहीं है
5   agent     agent_de_escalate                 —           —             माफी चाहती हूँ, delivery नहीं हो पाई है, latest status
6   customer  customer_express_frustration      frustrated  —             आप इतना frustrate क्यों कर रहे हो
7   agent     agent_de_escalate                 —           —             मै समझ सकती हूँ, यह delay
8   customer  customer_express_frustration      frustrated  —             getting so irritating
9   agent     agent_de_escalate                 —           —             यह delay परेशान करने वाला है
10  customer  customer_express_frustration      frustrated  —             तीन पांच दिन चार दिन हो गए हैं
11  agent     agent_answer_query                —           —             Nike T-Shirt, shipped है, 29 July तक deliver, case priority पर है
12  customer  customer_express_frustration      frustrated  —             आज ही deliver करवाओ
13  customer  customer_express_frustration      frustrated  —             refund आऐंगे कि नहीं, logistics department, पच्चीस को क्यों नहीं हुआ
14  agent     agent_de_escalate                 —           —             परेशान करने वाला है, माफी चाहती हूँ, cancellation और refund
15  customer  customer_express_frustration      frustrated  —             कोई conclusion तो निकल ही नहीं रहा, priority list में है, दिलासा दे रहे हो
16  agent     agent_de_escalate                 —           —             बार-बार एक ही बात सुनना निराशाजनक है, 29 July तक deliver
17  customer  customer_ask_question             frustrated  —             कब होगा resolve
18  customer  customer_ask_question             frustrated  —             what's the date to date, दो दिन अभी और लगेंगे
19  agent     agent_de_escalate                 —           —             और इंतज़ार करना पड़ रहा है, यह वाकई मुश्किल है
20  agent     agent_ask_to_repeat               —           —             माफ़ कीजिये, दोबारा कह सकते हैं
21  customer  customer_express_frustration      frustrated  —             coordination करने के लिए, logistic department
22  agent     agent_de_escalate                 —           —             काफी समय लग रहा है
23  customer  customer_express_frustration      frustrated  —             दो दिन का time, logistic से
24  agent     agent_de_escalate                 —           —             priority पर रख रहे हैं, 29 July तक deliver हो जाएगा, कोई और मदद कर सकती हूँ
25  customer  customer_ask_question             neutral     —             cancellation का जानना है, refund मिलेगा
26  agent     agent_clarify                     —           —             expert agent से बात करना चाहेंगे, बेहतर मदद कर पाएंगे
27  customer  customer_agree                    neutral     —             हां, हां जी, भेज दीजिए
```

## Call GEN-myntra-5f08af09-7b76-4a0a-9952-cfdb4f1ce714 (completed) — 18 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             parcel आने वाला था, कितने बजे तक आएगा
2   agent     agent_acknowledge                 —           —             order का इंतज़ार कर रहे हैं
3   customer  customer_request_wait             neutral     —             एक minute
4   agent     agent_wait                        —           —             कोई बात नहीं, समय ले लीजिए, line पर हूँ
5   customer  customer_ask_query                neutral     —             exact timing, घर पर नहीं हूं, cash on delivery
6   agent     agent_answer_query                —           —             packed है, आज deliver होने की उम्मीद है, out for delivery नहीं हुआ है
7   customer  customer_ask_question             neutral     —             request किया, इस time पर भेजे
8   agent     agent_answer_query                —           —             exact time slot select करने का option, पहुँचने से पहले आपको call ज़रूर करेंगे
9   customer  customer_ask_question             neutral     —             call नहीं आए थे, कब तक आ गया
10  agent     agent_answer_query                —           —             माफी चाहती हूँ, request डाल देती हूँ, call ज़रूर करे
11  customer  customer_acknowledge              neutral     —             अच्छा
12  agent     agent_acknowledge                 —           —             बिल्कुल, निश्चिंत रहें
13  customer  customer_ask_question             neutral     —             call करने बोलो, पहुंचने के पहले
14  agent     agent_acknowledge                 —           —             request note कर लेती हूँ, आज deliver होने की उम्मीद है
15  customer  customer_end                      happy       —             बस इतना ही पूछना था, thank you
16  agent     agent_end_call                    —           —             feedback form, अच्छी रेटिंग, धन्यवाद
17  agent     agent_end_call                    —           —             Thank you for calling मिंत्रा, Have a great day
```

## Call GEN-myntra-634ba1db-10f3-4df6-b847-ea23a9eb3a0f (transferred) — 18 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             आप किस order के बारे में बात करना चाहते हैं, क्या issue है
3   customer  customer_ask_query                frustrated  —             order deliver नहीं हुआ है, delivery date twenty first of July
4   agent     agent_acknowledge                 —           —             order अभी तक नहीं आया है, मै status
5   customer  customer_acknowledge              neutral     —             ठीक है
6   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
7   agent     agent_answer_query                —           —             Trolley Bag अभी shipped है, delivery काफी delay हो गई है, complaint register हो चुकी है
8   customer  customer_request_wait             neutral     —             एक second
9   agent     agent_wait                        —           —             समय ले लीजिए, line पर
10  customer  customer_ask_query                neutral     —             मेरा order जो है, complaint
11  agent     agent_answer_query                —           —             आपकी complaint register
12  customer  customer_ask_query                neutral     —             twenty second को complaint raise किया
13  agent     agent_answer_query                —           —             complaint register हो चुकी है, priority पर resolve, Trolley Bag अभी shipped है
14  customer  customer_express_frustration      frustrated  —             forty eight hours, अभी तक मुझे कोई resolution नहीं है
15  agent     agent_de_escalate                 —           —             बहुत frustrating है, माफी चाहती हूँ, expert agent से बात करना चाहेंगे
16  agent     agent_wait                        —           —             expert agent से connect कर रही हूँ, line पर बने रहिए
17  agent     agent_wait                        —           —             specialized team, Transferring your call now
```

## Call GEN-myntra-6b038a5c-c5ba-477b-99d8-a659bc1c0334 (completed) — 18 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             order आज का date दिखा रहा है, कब तक पहुंचे
2   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
3   agent     agent_answer_query                —           —             Roadster Shirt अभी shipped है, आज शाम आठ बजे तक
4   customer  customer_ask_question             skeptical   —             शाम में आठ बजे
5   agent     agent_answer_query                —           —             आज शाम आठ बजे तक deliver हो जाएगा
6   customer  customer_ask_question             skeptical   —             उससे पहले नहीं होगा
7   agent     agent_answer_query                —           —             fastest route पर है, जल्द से जल्द मिल जाए
8   customer  customer_ask_question             neutral     —             किसी और number पर call किया था, order के regarding में
9   agent     agent_answer_query                —           —             किसी और number पर call नहीं किया गया है
10  customer  customer_express_distrust         distrustful —             दूसरे number पर, call back, बात हुआ है
11  agent     agent_reassure_trust              —           —             digital assistant हूँ, calls नहीं करती हूँ
12  customer  customer_acknowledge              neutral     —             धन्यवाद
13  agent     agent_clarify                     —           —             किसी और चीज़ में मदद कर सकती हूँ
14  customer  customer_express_distrust         distrustful —             दूसरे number पर, बात की है क्या
15  agent     agent_reassure_trust              —           —             digital assistant हूँ, कोई बात नहीं हुई है
16  customer  customer_acknowledge              neutral     —             ठीक, Thanks
17  agent     agent_end_call                    —           —             आपका स्वागत है
```

## Call GEN-myntra-6b9f462f-aaaf-490c-8d45-1129ef3b58d8 (incomplete) — 16 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_query                frustrated  —             सुबह नौ बजे तक deliver होने वाला था, अभी तक आया नहीं है
2   customer  customer_express_frustration      frustrated  —             thirty minutes, one hour में वह deliver, पूरे date में दिखा रहा है
3   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
4   agent     agent_answer_query                —           —             YK T-shirt and Shorts set, shipped है, आज शाम आठ बजे तक deliver
5   customer  customer_unclear                  confused    —             can you repeat, कब तक order आएगा
6   agent     agent_answer_query                —           —             आज शाम आठ बजे तक deliver हो जाएगा
7   customer  customer_express_frustration      frustrated  —             gift देना है, बाहर कब जाऊंगी, आठ बजे तक deliver करोगे
8   agent     agent_de_escalate                 —           —             परेशानी समझ सकती हूँ, gift के लिए जल्दी चाहिए था, priority पर है
9   customer  customer_ask_query                frustrated  —             मुझे चार बजे
10  agent     agent_de_escalate                 —           —             मैं समझती हूँ
11  customer  customer_express_frustration      frustrated  —             चार बजे मुझे बाहर जा है, आठ बजे देकर, time पर deliver नहीं कर सकते
12  customer  customer_express_frustration      frustrated  —             repeat sentences मत बताइए, आज नहीं आ सकता, सोच समझकर ही order किया है
13  agent     agent_de_escalate                 —           —             काफी परेशान हैं, fastest route पर है, transit में है
14  customer  customer_request_wait             neutral     —             एक minute
15  agent     agent_confirm                     —           —             बताइए
```

## Call GEN-myntra-6f29b3fc-c8ae-4740-ac7f-da97c158b30c (transferred) — 16 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             Which order would you like to talk about, what is the issue
3   customer  customer_ask_question             neutral     —             Is it the AI agent
4   agent     agent_answer_query                —           —             I am an AI assistant, orders and returns
5   customer  customer_ask_question             neutral     —             orders that are supposed to come today, another two hours
6   agent     agent_wait                        —           —             Let me pull up your order list, Please stay on the line
7   agent     agent_answer_query                —           —             CRUSSET Girls Textured Belt, U.S. Polo Assn. Polo T-shirt, order list
8   customer  customer_ask_question             neutral     —             all these products, another two hours, is it possible
9   agent     agent_wait                        —           —             Please stay on the line, check the current status
10  agent     agent_answer_query                —           —             shipped and have reached the Kottayam hub, expected to be delivered by 8 PM, cannot guarantee a delivery within two hours
11  customer  customer_ask_question             neutral     —             customer care executive
12  agent     agent_clarify                     —           —             expert agent, better assistance
13  customer  customer_agree                    neutral     —             Yes please
14  agent     agent_wait                        —           —             expert agent से connect कर रही हूँ, line पर बने रहिए
15  agent     agent_wait                        —           —             specialized team, Transferring your call now
```

## Call GEN-myntra-75397766-14cb-411a-bdff-e370eb537ddf (incomplete) — 23 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             Sorry, could you say that again
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             आप किस order के बारे में बात करना चाहते हैं
3   customer  customer_ask_question             neutral     —             कहां पर है, अभी तक मिला receive नहीं हुआ है
4   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
5   agent     agent_answer_query                —           —             Kurti अभी packed है, delivery में delay हुआ है, कल तक deliver हो जाएगा
6   customer  customer_ask_question             frustrated  —             क्यों हुआ, यह तो Sunday
7   agent     agent_answer_query                —           —             shipping delays
8   customer  customer_ask_question             frustrated  —             मुझे भी जानना, जब Sunday का था
9   agent     agent_de_escalate                 —           —             Sunday तक order न मिलना परेशान
10  customer  customer_ask_query                frustrated  —             Sunday को booking का time था
11  agent     agent_answer_query                —           —             delivery में delay हुआ है, shipping delays या high order volumes, priority पर है
12  customer  customer_ask_question             frustrated  —             कब तक wait करना है, connect step क्या लेना है
13  agent     agent_answer_query                —           —             कल तक wait करना होगा, दोबारा
14  agent     agent_ask_to_repeat               —           —             माफ़ कीजिये, फिर से बता सकते हैं
15  customer  customer_express_frustration      frustrated  —             चौथी या पांचवी call है, पांच बार का complaint raise करी
16  agent     agent_de_escalate                 —           —             माफी चाहती हूँ, priority पर है
17  customer  customer_express_frustration      frustrated  —             problem resolveी हुई ना, exchange अभी तक मेरा नहीं मिला
18  customer  customer_express_frustration      frustrated  —             बार बार बोल रहे हो, आज wait करिए, परसों करिए
19  customer  customer_express_frustration      frustrated  —             order cancel करके, refund कर दीजिए
20  agent     agent_de_escalate                 —           —             यह delay वाकई बहुत परेशान करने वाला है, माफी चाहती हूँ, priority पर है
21  customer  customer_agree                    neutral     —             कल आपको wait करूंगी
22  agent     agent_confirm                     —           —             ठीक है
```

## Call GEN-myntra-7d23dc06-6b4d-458f-b806-cab2f985ddb9 (transferred) — 14 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             deliver होगा, urgent चाहिए
2   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
3   agent     agent_answer_query                —           —             shipped हैं, आज शाम आठ बजे तक deliver, GURUGRAM hub
4   customer  customer_express_frustration      frustrated  —             अभी भेजो, अभी भेज दो
5   agent     agent_de_escalate                 —           —             fastest route पर है, पूरी कोशिश कर रहे हैं
6   customer  customer_express_frustration      frustrated  —             दिक्कत हो गया
7   agent     agent_de_escalate                 —           —             यह जल्दी चाहिए, priority पर है
8   customer  customer_ask_question             neutral     —             f w d क्या होता है
9   agent     agent_clarify                     —           —             जानकारी नहीं है, expert agent से बात करना चाहेंगे
10  customer  customer_ask_question             neutral     —             तो आप बोलो
11  agent     agent_clarify                     —           —             जानकारी नहीं है, expert agent से बात करना चाहेंगे
12  agent     agent_wait                        —           —             expert agent से connect कर रही हूँ, line पर बने रहिए
13  agent     agent_wait                        —           —             connect you with our specialized team, Transferring your call now
```

## Call GEN-myntra-7dd623f2-054f-4ce9-b502-355df8252796 (completed) — 15 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             frustrated  —             delivered हो ही नहीं रहा
2   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
3   agent     agent_answer_query                —           —             shipped है, out for delivery, 24 hours में
4   customer  customer_express_frustration      frustrated  —             पंद्रह दिन हो गया
5   agent     agent_de_escalate                 —           —             15 days का wait, out for delivery
6   customer  customer_express_frustration      frustrated  —             क्या ही help चाहिए
7   agent     agent_de_escalate                 —           —             परेशान हैं, wait कर लीजिए
8   customer  customer_express_frustration      frustrated  —             चौबीस hour के अंदर
9   agent     agent_acknowledge                 —           —             मैं आपकी बात
10  customer  customer_other                    neutral     —             —
11  agent     agent_de_escalate                 —           —             बाहर जा रहे हैं, out for delivery
12  customer  customer_acknowledge              neutral     —             हो गया
13  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
14  agent     agent_end_call                    —           —             Thank you for calling, Have a great day
```

## Call GEN-myntra-92a64f7c-3f9e-41bc-9a18-57f9a80cf656 (transferred) — 26 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_express_frustration      frustrated  —             within twenty four hour, Even day को होगा
2   customer  customer_express_frustration      frustrated  —             Solution तो कुछ मिला नहीं, twenty four hour में हो जाएगा
3   agent     agent_de_escalate                 —           —             माफी चाहती हूँ, status check कर रही हूँ, line पर बने रहिए
4   customer  customer_express_frustration      frustrated  —             Wednesday को होगा, तीन चार दिन delay
5   agent     agent_de_escalate                 —           —             Rajkot hub, 29 July तक deliver, priority पर है
6   customer  customer_express_frustration      frustrated  —             आज हो जाना चाहिए, इतना problem हो रहा है
7   customer  customer_express_frustration      frustrated  —             twenty four hour में हो जाएगा, यह कोई बात हुई क्या
8   agent     agent_de_escalate                 —           —             नाराजगी बिलकुल सही
9   agent     agent_ask_to_repeat               —           —             माफ़ कीजिये, फिर कह सकते हैं
10  customer  customer_express_frustration      frustrated  —             deliverable नहीं है, मना कर दो
11  customer  customer_express_frustration      frustrated  —             twenty four hour में हो जाएगा, उनतीस तक हो जाएगा
12  agent     agent_de_escalate                 —           —             समझ सकती हूँ
13  customer  customer_express_frustration      frustrated  —             customer service ले है
14  customer  customer_express_frustration      frustrated  —             आज delivery चाहिए, solution इसका निकालो
15  agent     agent_de_escalate                 —           —             परेशानी बिलकुल जायज, माफी चाहती हूँ
16  customer  customer_express_frustration      frustrated  —             आज की date में deliver, तीन दिन तो और delay
17  agent     agent_de_escalate                 —           —             माफी चाहती हूँ, आज ही चाहिए था
18  customer  customer_express_frustration      frustrated  —             छब्बीस तारीख, इक्कीस को order किया
19  customer  customer_express_frustration      frustrated  —             इतना late होने वाला है, emergency वाला है
20  agent     agent_de_escalate                 —           —             26 July तक delivery, निराशाजनक है, दिल से माफी
21  customer  customer_express_frustration      frustrated  —             आज कर दीजिए, resolve करके
22  agent     agent_de_escalate                 —           —             urgency समझ रही हूँ, आज ही deliver हो जाए
23  customer  customer_agree                    frustrated  —             हां, करवा दीजिए
24  agent     agent_wait                        —           —             expert agent से connect, line पर बने रहिए
25  agent     agent_wait                        —           —             specialized team, Transferring your call now
```

## Call GEN-myntra-96535ab9-428d-439d-a023-128d8011062d (transferred) — 12 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             seal का number, match नहीं हो रहा
2   customer  customer_ask_question             neutral     —             won't give the product
3   agent     agent_answer_query                —           —             out for delivery, My Orders page
4   customer  customer_express_frustration      frustrated  —             how how
5   agent     agent_acknowledge                 —           —             आपकी बात सुन रही हूँ
6   customer  customer_express_frustration      frustrated  —             sun लो आप ढंग से
7   customer  customer_express_frustration      frustrated  —             सुनो पहले ढंग से, Seal number नहीं हो रहा match
8   agent     agent_answer_query                —           —             My Orders page, expert agent से बात करना चाहेंगे
9   customer  customer_express_frustration      frustrated  —             expert agent को ही forward कीजिए, समझ में नहीं आ रही
10  agent     agent_wait                        —           —             expert agent से connect, line पर बने रहिए
11  agent     agent_wait                        —           —             specialized team, Transferring your call now
```

## Call GEN-myntra-9d5249e0-9947-4f6f-88b1-ec6cd8b61437 (completed) — 16 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             कितनी quantities, कितने pieces
2   agent     agent_wait                        —           —             order details check, line पर बने रहिए
3   agent     agent_clarify                     —           —             MIRAGGIO Laptop Bag, related है
4   agent     agent_wait                        —           —             status check, line पर बने रहिए
5   agent     agent_answer_query                —           —             packed है, आज deliver होने की उम्मीद
6   customer  customer_ask_question             neutral     —             कितने pieces, deliver होने वाले हैं आज
7   agent     agent_answer_query                —           —             एक piece है, आज deliver होने वाला
8   customer  customer_ask_question             skeptical   —             तेरह piece की quantity
9   agent     agent_wait                        —           —             details check कर लेती हूँ, line पर बने रहिए
10  agent     agent_answer_query                —           —             कुल 13 pieces, scheduled हैं
11  customer  customer_acknowledge              neutral     —             तेरा pieces, आज ही deliver होंगे
12  agent     agent_answer_query                —           —             सभी 13 pieces, आज deliver होने की उम्मीद
13  customer  customer_end                      happy       —             thank you
14  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
15  agent     agent_end_call                    —           —             Thank you for calling, Have a great day
```

## Call GEN-myntra-a24c6f8b-94b6-49da-b492-23464aea7b6b (completed) — 14 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   agent     agent_ask_to_repeat               —           —             Sorry, could you say that
2   customer  customer_ask_question             neutral     —             check करके बताइए
3   agent     agent_wait                        —           —             status check, line पर बने रहिए
4   agent     agent_answer_query                —           —             shipped है, Ahmedabad hub, 1 August तक
5   customer  customer_ask_question             neutral     —             मेरे को पता ही है
6   agent     agent_ask_to_repeat               —           —             क्या बताना चाह रहे हैं
7   customer  customer_ask_question             neutral     —             एक तारीख को आने वाला
8   customer  customer_ask_question             neutral     —             आज कहां पर है, update नहीं आ रहा
9   customer  customer_ask_question             neutral     —             तेईस तारीख को, अहमदाबाद वाले center
10  agent     agent_answer_query                —           —             exact update जानना चाहते, 1 August तक
11  customer  customer_acknowledge              neutral     —             नहीं
12  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
13  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
```

## Call GEN-myntra-a3b10246-7b04-4685-9119-370d58691460 (completed) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_other                    confused    —             —
2   agent     agent_clarify                     —           —             किस order के बारे में, क्या issue
3   customer  customer_ask_query                neutral     —             मैं आपको बताती हूं
4   agent     agent_answer_query                —           —             Roadster T-shirt, shipped है
5   customer  customer_request_wait             neutral     —             एक minute
6   agent     agent_wait                        —           —             आराम से बात कर लीजिए, line पर ही हूँ
7   customer  customer_other                    confused    —             —
8   agent     agent_answer_query                —           —             Roadster T-shirt, complaint register, कल तक deliver
9   customer  customer_end                      happy       —             thank you madam
10  customer  customer_ask_question             neutral     —             कल तक आ जाना चाहिए, निकल रही हूं
11  agent     agent_answer_query                —           —             दिए हुए address पर, कल तक आप तक पहुँच
12  customer  customer_end                      happy       —             thank you madam
13  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
14  customer  customer_end                      happy       —             धन्यवाद, Thank you
15  agent     agent_end_call                    —           —             feedback form, अच्छी रेटिंग
16  customer  customer_acknowledge              happy       —             भर देंगे
17  agent     agent_end_call                    —           —             बहुत धन्यवाद, call के लिए धन्यवाद
18  agent     agent_end_call                    —           —             Thank you for
```

## Call GEN-myntra-a8100583-8ac8-460e-9d8a-644b6e195b19 (completed) — 20 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order के बारे में, क्या issue है
3   customer  customer_ask_query                neutral     —             Safari, Forty five liter
4   agent     agent_answer_query                —           —             processing में है, 29 July तक deliver
5   customer  customer_ask_question             neutral     —             पहले मतलब मेरे को चाहिए था
6   agent     agent_answer_query                —           —             fastest route पर है, 29 July तक पहुँच जाएगा
7   customer  customer_ask_question             neutral     —             कल तक ही मेरे को चाहिए, fast job करके
8   agent     agent_answer_query                —           —             urgency समझ रही हूँ, priority पर है
9   customer  customer_ask_question             neutral     —             twenty eight तक नहीं आ पाएगा
10  agent     agent_wait                        —           —             फिर से check कर रही हूँ, line पर बने रहिए
11  agent     agent_answer_query                —           —             processing में है, 29 July तक ही deliver
12  customer  customer_ask_question             neutral     —             confirmation दे दीजिए, twenty eight July
13  customer  customer_ask_question             neutral     —             ship करवाने का try करिए, Twenty eight को
14  agent     agent_answer_query                —           —             परेशानी बिलकुल सही, 29 July की ही date
15  customer  customer_ask_question             neutral     —             chances हैं, कल भी यह मिल सकता है
16  agent     agent_answer_query                —           —             29 July की ही date confirm, status check करते रहिएगा
17  customer  customer_acknowledge              neutral     —             नहीं
18  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
19  agent     agent_end_call                    —           —             Thank you for calling, Have a great day
```

## Call GEN-myntra-acca438a-ad3c-4f67-b82f-10bf4d3dd176 (completed) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order के बारे में, क्या issue है
3   customer  customer_ask_query                neutral     —             Red tape shoes
4   agent     agent_clarify                     —           —             Red Tape shoes, क्या issue आ रहा है
5   customer  customer_ask_question             confused    —             exact location नहीं पता चल रही, Exact location चाहिए
6   agent     agent_wait                        —           —             status check कर रही हूँ
7   customer  customer_other                    confused    —             —
8   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
9   agent     agent_answer_query                —           —             —
10  agent     agent_answer_query                —           —             shipped हैं, 7 August तक मिल जाएगा
11  customer  customer_ask_question             confused    —             exact location कहां है
12  agent     agent_answer_query                —           —             exact शहर की details अभी available नहीं, 7 August तक आपके पास पहुँच जाएगा
13  customer  customer_express_frustration      frustrated  —             Flipkart देखा था, address proper दिखा
14  customer  customer_express_frustration      frustrated  —             official website से लिया है
15  agent     agent_answer_query                —           —             —
16  customer  customer_acknowledge              neutral     —             —
17  agent     agent_answer_query                —           —             tracking details अपडेट
18  customer  customer_ask_question             confused    —             item at in dispatch
19  agent     agent_answer_query                —           —             item in dispatch, warehouse से निकल चुका है
20  customer  customer_other                    neutral     —             —
21  customer  customer_express_frustration      frustrated  —             Item ship to nearest delivery center, Exact location तो बताना चाहिए
22  agent     agent_de_escalate                 —           —             परेशानी बिलकुल सही है
23  customer  customer_ask_question             confused    —             —
24  agent     agent_de_escalate                 —           —             —
25  customer  customer_acknowledge              neutral     —             —
26  agent     agent_answer_query                —           —             hub की तरफ जा रहा होता है, 7 August तक पहुँच जाएगा
27  customer  customer_end                      neutral     —             Thank you
28  agent     agent_end_call                    —           —             feedback form मिलेगा, call के लिए धन्यवाद
29  customer  customer_ask_question             neutral     —             आपका नाम क्या है
30  agent     agent_answer_query                —           —             मेरा नाम मीरा है
31  customer  customer_unclear                  confused    —             —
32  agent     agent_answer_query                —           —             मेरा नाम मीरा है
33  customer  customer_ask_question             skeptical   —             AI तो है
34  agent     agent_answer_query                —           —             AI assistant हूँ
35  customer  customer_other                    neutral     —             —
36  agent     agent_ask_to_repeat               —           —             समझ नहीं आई, दोबारा बता सकते हैं
37  customer  customer_end                      neutral     —             thank you
38  agent     agent_end_call                    —           —             feedback form मिलेगा
39  customer  customer_acknowledge              neutral     —             —
40  agent     agent_end_call                    —           —             शुक्रिया
41  agent     agent_end_call                    —           —             Thank you for calling, Have a great day
```

## Call GEN-myntra-ae82a833-a758-415f-b32c-e682edfaed12 (completed) — 31 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             Which order, what is the issue
3   customer  customer_greet                    neutral     —             Hello
4   agent     agent_clarify                     —           —             which order you are calling about
5   customer  customer_ask_query                neutral     —             delayed on second August
6   agent     agent_wait                        —           —             check the status, stay on the line
7   agent     agent_answer_query                —           —             has been shipped, delivered by tomorrow
8   customer  customer_acknowledge              neutral     —             —
9   agent     agent_answer_query                —           —             on its way, reach you by tomorrow
10  customer  customer_other                    confused    —             —
11  agent     agent_ask_to_repeat               —           —             didn't quite catch that, please repeat
12  customer  customer_ask_question             neutral     —             Both of them will come tomorrow
13  agent     agent_wait                        —           —             stay on the line
14  agent     agent_answer_query                —           —             both your Vastraaya Kurtis are shipped, delivered by tomorrow
15  customer  customer_express_distrust         skeptical   —             Are you sure, delivery delayed on the app
16  agent     agent_reassure_trust              —           —             re-checked the latest system status, I can confirm
17  customer  customer_ask_question             neutral     —             not delayed anymore
18  agent     agent_answer_query                —           —             on track, delivered by tomorrow
19  customer  customer_ask_question             frustrated  —             change the status on the app
20  agent     agent_answer_query                —           —             updates automatically
21  customer  customer_ask_question             frustrated  —             traveling in two days, won't be able to give you OTPs
22  agent     agent_answer_query                —           —             coordinate with the delivery agent
23  customer  customer_ask_question             neutral     —             tomorrow itself right
24  agent     agent_answer_query                —           —             on track, delivered by tomorrow
25  customer  customer_ask_question             neutral     —             status changes on the app
26  agent     agent_answer_query                —           —             updates automatically
27  customer  customer_end                      neutral     —             No thank you
28  agent     agent_end_call                    —           —             feedback form via SMS
29  agent     agent_end_call                    —           —             feedback form via SMS, Thank you for calling
30  agent     agent_end_call                    —           —             feedback form via SMS, Thank you for calling
```

## Call GEN-myntra-aee1b45e-bb00-4d19-a142-976566267b0f (completed) — 11 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order के बारे में, क्या issue है
3   customer  customer_ask_question             frustrated  —             exchange किया था, कब मिलेगा यह action
4   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
5   agent     agent_answer_query                —           —             out for delivery है, 24 hours में मिल जाएगा
6   customer  customer_ask_question             neutral     —             आज
7   agent     agent_answer_query                —           —             out for delivery है, 24 hours में मिल जाएगा
8   customer  customer_end                      neutral     —             Thank you
9   agent     agent_end_call                    —           —             feedback form मिलेगा, call के लिए धन्यवाद
10  agent     agent_end_call                    —           —             Thank you for calling, Have a great day
```

## Call GEN-myntra-aef10062-0439-440c-b40d-c6a0850878d3 (transferred) — 33 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_query                neutral     —             order किया था shoes
2   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
3   agent     agent_answer_query                —           —             shipped हैं, आठ बजे तक deliver
4   customer  customer_other                    neutral     —             —
5   agent     agent_acknowledge                 —           —             मैं यहीं हूँ
6   customer  customer_ask_question             frustrated  —             एक या दो बजे तक, deliver करवा दो
7   agent     agent_answer_query                —           —             fastest route पर है, आठ बजे तक पहुँच जाएगा
8   customer  customer_ask_question             frustrated  —             एक दो बजे तक ज़रूर
9   agent     agent_answer_query                —           —             urgency समझ रही हूँ
10  customer  customer_ask_question             frustrated  —             एक दो बजे तक
11  agent     agent_answer_query                —           —             priority पर है, आठ बजे तक deliver हो जाएगा
12  customer  customer_express_frustration      frustrated  —             एक दो बजे तक, shoes चाहिए
13  agent     agent_de_escalate                 —           —             priority पर है, आठ बजे तक deliver
14  customer  customer_other                    neutral     —             —
15  agent     agent_clarify                     —           —             —
16  customer  customer_ask_question             frustrated  —             दो बजे तक पहुंच जाना
17  agent     agent_acknowledge                 —           —             request नोट कर ली है
18  customer  customer_ask_question             frustrated  —             —
19  customer  customer_express_distrust         skeptical   —             Real इंसान हो
20  agent     agent_reassure_trust              —           —             virtual assistant हूँ
21  customer  customer_express_frustration      frustrated  —             human
22  agent     agent_de_escalate                 —           —             —
23  customer  customer_express_distrust         skeptical   —             human हो या AI हो
24  agent     agent_reassure_trust              —           —             virtual assistant हूँ
25  customer  customer_express_frustration      frustrated  —             बकवास है
26  agent     agent_de_escalate                 —           —             माफी चाहती हूँ
27  customer  customer_agree                    frustrated  —             दो बजे तक
28  agent     agent_clarify                     —           —             expert agent से बात करना
29  customer  customer_agree                    frustrated  —             हां हां करवाऊंगी
30  agent     agent_confirm                     —           —             —
31  customer  customer_other                    neutral     —             —
32  agent     agent_end_call                    —           —             Transferring your call now, specialized team
```

## Call GEN-myntra-af3ab03a-9be5-4f6f-8429-675f3aa6ad35 (completed) — 15 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             Delivery
2   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
3   agent     agent_answer_query                —           —             shipped हैं, 30 July तक deliver
4   customer  customer_ask_question             neutral     —             one day पहले, Twenty nine
5   agent     agent_answer_query                —           —             fastest route पर है, 30 July show हो रही है
6   customer  customer_ask_question             neutral     —             request है मेरा
7   agent     agent_answer_query                —           —             priority पर है, system के हिसाब से ही update होती है
8   customer  customer_ask_question             neutral     —             पहले ही आ सकता है
9   agent     agent_answer_query                —           —             —
10  customer  customer_ask_question             neutral     —             उम्मीद कर सकते हैं
11  agent     agent_answer_query                —           —             उम्मीद कर सकते हैं, priority पर है
12  customer  customer_end                      neutral     —             thank you
13  agent     agent_end_call                    —           —             feedback form मिलेगा, call के लिए धन्यवाद
14  agent     agent_end_call                    —           —             Thank you for calling, Have a great day
```

## Call GEN-myntra-b1b8e93d-e177-4214-9926-85a34cc3a238 (completed) — 32 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order के बारे में, क्या issue है
3   customer  customer_ask_query                confused    —             delivery दिखा है, fake दिखा रहा है
4   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
5   agent     agent_answer_query                —           —             out for delivery है, delivery attempt fail हुआ था
6   customer  customer_other                    confused    —             —
7   agent     agent_ask_to_repeat               —           —             समझ नहीं पाई, फिर से बता सकते हैं
8   customer  customer_ask_query                frustrated  —             message आया था, parcel नहीं आया
9   agent     agent_answer_query                —           —             delivery attempt fail हुआ था, माफी चाहती हूँ
10  customer  customer_ask_question             frustrated  —             कैसे हुआ
11  agent     agent_answer_query                —           —             —
12  customer  customer_express_frustration      frustrated  —             attempt नहीं किया था
13  agent     agent_de_escalate                 —           —             —
14  customer  customer_ask_question             frustrated  —             —
15  agent     agent_answer_query                —           —             —
16  customer  customer_express_frustration      frustrated  —             attempt नहीं किया
17  customer  customer_express_frustration      frustrated  —             attempt fail हुआ, call तो आया नहीं
18  agent     agent_de_escalate                 —           —             परेशान करने वाला है
19  customer  customer_express_frustration      frustrated  —             technical error आना चाहिए, attempt नहीं किया
20  agent     agent_acknowledge                 —           —             बिलकुल सही है
21  customer  customer_ask_question             frustrated  —             —
22  agent     agent_answer_query                —           —             —
23  customer  customer_express_frustration      frustrated  —             attempt नहीं किया
24  customer  customer_express_frustration      frustrated  —             attempt नहीं किया, call आया
25  agent     agent_de_escalate                 —           —             attempt fail mark कर दिया जाता है, माफी चाहती हूँ
26  customer  customer_express_frustration      frustrated  —             —
27  agent     agent_answer_query                —           —             जल्द से जल्द deliver
28  customer  customer_ask_question             frustrated  —             पांच बजे तक
29  agent     agent_answer_query                —           —             exact time slot promise नहीं कर सकती
30  customer  customer_end                      neutral     —             Thank you
31  agent     agent_end_call                    —           —             —
```

## Call GEN-myntra-b407331b-ef3e-4634-aa37-8a22f479883b (transferred) — 23 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             neutral     —             connect मलयालम
2   agent     agent_acknowledge_decline         —           —             Hindi or English only
3   customer  customer_ask_query                frustrated  —             package delayed, didn't get my package
4   agent     agent_wait                        —           —             check the status, stay on the line
5   agent     agent_answer_query                —           —             shipped and currently in transit, delivered by tomorrow
6   customer  customer_ask_question             neutral     —             —
7   agent     agent_answer_query                —           —             कल तक deliver हो जाएगा
8   customer  customer_unclear                  confused    —             I didn't understand, हिंदी
9   agent     agent_answer_query                —           —             delivered by tomorrow
10  customer  customer_ask_question             neutral     —             —
11  customer  customer_ask_question             neutral     —             deliver today
12  agent     agent_answer_query                —           —             —
13  customer  customer_report_unavailable       neutral     —             not free
14  agent     agent_answer_query                —           —             not available tomorrow
15  customer  customer_report_unavailable       neutral     —             nobody is there
16  customer  customer_ask_question             neutral     —             —
17  agent     agent_answer_query                —           —             coordinate with the delivery agent
18  customer  customer_ask_question             neutral     —             —
19  agent     agent_ask_to_repeat               —           —             —
20  customer  customer_ask_question             neutral     —             delivery agent name, pick up my order
21  customer  customer_other                    neutral     —             —
22  agent     agent_acknowledge_decline         —           —             self pickup, not supported
```

## Call GEN-myntra-b56dbe05-1c53-4042-9fcf-c620775551f1 (incomplete) — 12 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा
1   customer  customer_ask_question             frustrated  —             order delay हो गया है, कब तक आएगा
2   agent     agent_wait                        —           —             status check कर रही हूँ, line पर बने रहिए
3   agent     agent_answer_query                —           —             processing में है, माफी चाहती हूँ
4   customer  customer_express_frustration      frustrated  —             twenty five July, thirty बोल रहे हैं
5   agent     agent_de_escalate                 —           —             date change होने से आप परेशान हैं, 30 July तक deliver होगा
6   customer  customer_ask_question             frustrated  —             delay होने का reason
7   agent     agent_answer_query                —           —             high order volumes, shipping delays
8   customer  customer_ask_question             skeptical   —             —
9   agent     agent_clarify                     —           —             app में आपको क्या show हो रहा है
10  customer  customer_express_distrust         skeptical   —             confirmed in next twelve hours, दो दिन जैसा दिखा रहा है
11  agent     agent_reassure_trust              —           —             माफी चाहती हूँ, system के हिसाब से
```

## Call GEN-myntra-b60504f5-17ec-4054-bd72-333e15d648d6 (incomplete) — 17 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_ask_query                neutral     —             order
2   agent     agent_clarify                     —           —             क्या आप मुझे बता सकते हैं
3   customer  customer_ask_query                neutral     —             मेरा order अभी तक आया नहीं है
4   agent     agent_wait                        —           —             status check कर रही हूँ, कृपया line पर बने रहिए
5   agent     agent_answer_query                —           —             shipped है, कल तक deliver हो जाएगा, complaint पहले से registered है
6   customer  customer_ask_question             neutral     —             एक दूसरा order भी है
7   agent     agent_clarify                     —           —             क्या issue है, बता सकते हैं
8   customer  customer_ask_query                neutral     —             delay हो चुका है
9   agent     agent_wait                        —           —             order list check कर रही हूँ, line पर बने रहिए
10  agent     agent_clarify                     —           —             ग्लिचेज Grey T-shirt, क्या आपकी problem इसी order से related है
11  agent     agent_answer_query                —           —             shipped है, कल तक deliver हो जाएगा, complaint registered है
12  customer  customer_acknowledge              neutral     —             Thank you
13  agent     agent_end_call                    —           —             धन्यवाद, feedback form, call के लिए धन्यवाद
14  agent     agent_end_call                    —           —             Thank you for calling मिंत्रा
15  customer  customer_other                    confused    —             —
16  agent     agent_ask_to_repeat               —           —             मैं आपकी बात समझ नहीं पाई, क्या आप अपने orders के बारे में कुछ और पूछना चाहते हैं
```

## Call GEN-myntra-cb053454-0910-4130-8b7f-8c0db10920e3 (transferred) — 21 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_ask_question             neutral     —             मीरा बात कर रही हैं
2   agent     agent_answer_query                —           —             मै मीरा बात कर रही हूँ, मै आपकी कैसे मदद कर सकती हूँ
3   customer  customer_acknowledge              neutral     —             Hello, Ok ok
4   agent     agent_clarify                     —           —             किस order के बारे में
5   customer  customer_unclear                  confused    —             मतलब यह है कि Myntra है
6   agent     agent_answer_query                —           —             यह मिंत्रा ही है
7   customer  customer_ask_question             frustrated  —             orders, cancel क्यों हो जाते हैं
8   agent     agent_clarify                     —           —             orders cancel हो रहे हैं, किस product, expert agent से बात करना चाहेंगे
9   customer  customer_express_frustration      frustrated  —             cancel हो रही है, मेरे address पर क्यों नहीं आ रहे, cancel कर देंगे
10  agent     agent_wait                        —           —             check करती हूँ, line पर बने रहिए
11  customer  customer_acknowledge              neutral     —             हां आते हैं
12  agent     agent_answer_query                —           —             shipped है, आज शाम आठ बजे तक deliver, cancel नहीं होगा
13  customer  customer_ask_question             skeptical   —             cancel तो नहीं होगा
14  agent     agent_answer_query                —           —             बिल्कुल नहीं, cancel नहीं होगा, आज शाम आठ बजे तक
15  customer  customer_ask_question             frustrated  —             cancel हुए, पैसे भी cut, छत्तीस रुपए
16  agent     agent_answer_query                —           —             खेद है, expert agent से connect करना होगा
17  customer  customer_ask_question             frustrated  —             order cancel हुए हैं, बता दीजिए
18  agent     agent_answer_query                —           —             specialized experts, expert agent से बात करना चाहेंगे
19  customer  customer_agree                    neutral     —             हां जी, ठीक है
20  agent     agent_other                       —           —             Transferring your call now
```

## Call GEN-myntra-cf054916-3e70-4421-8c7d-9ed13d0fbd59 (transferred) — 30 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_ask_query                neutral     —             headphones, delay, twenty nine May
2   agent     agent_answer_query                —           —             out for delivery, आज शाम आठ बजे तक
3   customer  customer_ask_query                frustrated  —             पहले भी, deliver नहीं हो, cancel करके
4   customer  customer_ask_query                neutral     —             delivered on twenty nine
5   customer  customer_ask_question             frustrated  —             no update, contact details of agent, share some details
6   agent     agent_answer_query                —           —             out for delivery है, My Orders page, delivery agent की details
7   customer  customer_other                    confused    —             —
8   customer  customer_ask_question             frustrated  —             नहीं दिखा रहा, check करके बोलो
9   agent     agent_de_escalate                 —           —             मै समझ सकती
10  customer  customer_express_frustration      frustrated  —             Daily message, फिर भी नहीं आ रहा, ten days
11  agent     agent_de_escalate                 —           —             मै समझ सकती हूँ, दस दिनों से
12  customer  customer_ask_question             skeptical   —             issue with my account
13  agent     agent_answer_query                —           —             account की problem नहीं है
14  customer  customer_other                    confused    —             —
15  agent     agent_answer_query                —           —             account की problem
16  customer  customer_express_frustration      frustrated  —             payment करने के बाद भी
17  agent     agent_answer_query                —           —             account या payment की कोई problem नहीं, out for delivery है, आज शाम आठ बजे तक
18  customer  customer_ask_question             frustrated  —             delivery नहीं हुए तो
19  agent     agent_answer_query                —           —             अगर आज delivery नहीं
20  customer  customer_ask_question             frustrated  —             What should I do
21  agent     agent_answer_query                —           —             फिक्र न करें, order priority
22  customer  customer_express_frustration      frustrated  —             Previously
23  agent     agent_de_escalate                 —           —             माफी चाहती हूँ, priority पर है, शाम आठ बजे तक
24  customer  customer_other                    frustrated  —             —
25  agent     agent_de_escalate                 —           —             काफी परेशान हैं, priority पर है
26  customer  customer_ask_question             frustrated  —             platform fees, credit नहीं हो रहे, charge कराओ
27  agent     agent_answer_query                —           —             क्षमा चाहती हूँ, expert agent से connect करना होगा
28  agent     agent_wait                        —           —             expert agent से connect कर रही हूँ, line पर बने रहिए
29  agent     agent_other                       —           —             Transferring your call now
```

## Call GEN-myntra-d139fc8d-b84b-4550-98e1-b286157935b4 (completed) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_ask_question             neutral     —             order कब तक आया थी
2   agent     agent_wait                        —           —             status check कर रही हूँ, कृपया line पर बने रहिए
3   agent     agent_answer_query                —           —             zayla Jeans shipped है
4   agent     agent_answer_query                —           —             shipped है, 29 July तक deliver, मदद कर सकती हूँ
5   customer  customer_ask_question             skeptical   —             Twenty nine को ही होगा, आगे नहीं मिल सकता
6   agent     agent_answer_query                —           —             fastest route, 29 July तक पहुँच जाएगा
7   customer  customer_acknowledge              neutral     —             जितना जल्दी हो सके
8   agent     agent_answer_query                —           —             जल्दी चाहिए, priority पर है, fastest route
9   customer  customer_ask_question             neutral     —             आज तक मिल सकता है
10  agent     agent_answer_query                —           —             out for delivery नहीं हुआ है, आज मिलना मुश्किल है
11  customer  customer_express_frustration      frustrated  —             ऐसा हाल, आज ही मेरे को नहीं
12  agent     agent_de_escalate                 —           —             समझ सकती हूँ, आज ही इसकी ज़रूरत
13  customer  customer_acknowledge              neutral     —             कोई नहीं, call request करूंगी
14  agent     agent_end_call                    —           —             feedback form, धन्यवाद
15  agent     agent_end_call                    —           —             Thank you for
16  customer  customer_acknowledge              neutral     —             Ok, Sure
17  agent     agent_end_call                    —           —             धन्यवाद, feedback form
18  agent     agent_end_call                    —           —             Thank you for calling मिंत्रा, Have a great day
```

## Call GEN-myntra-d67b4b34-d834-417b-8fdd-38bb2dfd7e77 (transferred) — 61 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order, क्या issue है
3   customer  customer_greet                    neutral     —             hello
4   agent     agent_clarify                     —           —             किस order के बारे में, क्या issue
5   customer  customer_ask_query                neutral     —             अशोक fan, नाम से order
6   agent     agent_clarify                     —           —             किस order के बारे में बात
7   customer  customer_other                    confused    —             —
8   agent     agent_clarify                     —           —             —
9   customer  customer_other                    confused    —             —
10  agent     agent_clarify                     —           —             delivery से related है या return से
11  customer  customer_express_frustration      frustrated  —             लेकर भाग गया, एक minute भी नहीं रुका, सीधा निकल गया
12  agent     agent_wait                        —           —             परेशान करने वाला है, status check कर रही हूँ, line पर बने रहिए
13  agent     agent_answer_query                —           —             Roadster Jeans
14  customer  customer_request_callback         frustrated  —             call call me
15  agent     agent_answer_query                —           —             Roadster Jeans का status
16  customer  customer_request_callback         frustrated  —             call करने का बोल, मेरा number दो
17  agent     agent_answer_query                —           —             out for delivery नहीं है, delivery agent की details उपलब्ध नहीं
18  customer  customer_request_callback         frustrated  —             call कर
19  customer  customer_request_callback         frustrated  —             call करवाए जाए, निकल गया सीधा
20  agent     agent_de_escalate                 —           —             परेशान हैं
21  customer  customer_request_callback         frustrated  —             number पर call करवाए
22  agent     agent_answer_query                —           —             out for delivery नहीं है, delivery agent से contact करना possible नहीं, complaint register है
23  customer  customer_express_frustration      frustrated  —             time नहीं है, आज ही time है, on duty रहूंगा
24  agent     agent_de_escalate                 —           —             परेशानी समझ सकती हूँ, आज ही order चाहिए
25  customer  customer_express_frustration      frustrated  —             मेरी location में ही है, आगे निकला है सीधा
26  agent     agent_de_escalate                 —           —             परेशान हैं
27  customer  customer_request_callback         frustrated  —             Call किए गए, call location
28  agent     agent_answer_query                —           —             delivery agent से contact नहीं करवा सकती, complaint register है
29  customer  customer_express_frustration      frustrated  —             आज ही होना चाहिए, आज ही मिलना चाहिए
30  agent     agent_de_escalate                 —           —             urgency समझ सकती हूँ
31  customer  customer_express_frustration      frustrated  —             आज ही order मिलना चाहिए
32  agent     agent_de_escalate                 —           —             urgency समझ सकती हूँ, रास्ते में है, कल तक deliver
33  customer  customer_ask_question             frustrated  —             कल तक नहीं deliver
34  agent     agent_answer_query                —           —             latest status कल तक, शिकायत register है, priority पर देख रही है
35  customer  customer_express_frustration      frustrated  —             charge दे धोना चाहिए, बिना रुके, call करके बोला जाए
36  agent     agent_de_escalate                 —           —             नाराजगी समझ सकती हूँ
37  customer  customer_express_frustration      frustrated  —             लगनी चाहिए
38  agent     agent_de_escalate                 —           —             नाराजगी बिल्कुल सही है, रुकना चाहिए था
39  customer  customer_express_frustration      frustrated  —             lock बता रहा है, Out of delivery कैसे हो गया
40  agent     agent_de_escalate                 —           —             निराशाजनक है
41  customer  customer_ask_question             frustrated  —             कोई reason है
42  agent     agent_answer_query                —           —             high order volume, shipping में कुछ दिक्कतें, माफी चाहती हूँ
43  customer  customer_acknowledge              neutral     —             बिल्कुल
44  customer  customer_request_callback         frustrated  —             call किया जाए, contact करके
45  agent     agent_answer_query                —           —             बात समझ रही हूँ
46  customer  customer_express_frustration      frustrated  —             Call नहीं किया है
47  agent     agent_de_escalate                 —           —             बिना call आए
48  customer  customer_request_callback         frustrated  —             location को पता करके, numbers है
49  agent     agent_reassure_trust              —           —             परेशानी समझ सकती हूँ, security
50  customer  customer_request_callback         frustrated  —             location बता करके
51  agent     agent_reassure_trust              —           —             security reasons, number share नहीं कर सकती
52  customer  customer_ask_question             skeptical   —             क्यों
53  agent     agent_reassure_trust              —           —             security reasons, personal details share नहीं कर सकते, My Orders page
54  customer  customer_express_distrust         distrustful —             संतुष्ट नहीं, report गलत हो रही है, pending बता रहा है
55  agent     agent_de_escalate                 —           —             परेशान करने वाला है, बिल्कुल सही कह रहे हैं, priority पर है
56  customer  customer_express_frustration      frustrated  —             आज ही होना चाहिए, redliver में डालो, priority किस चीज़ की
57  agent     agent_answer_query                —           —             मेरे control में नहीं है, expert agent से बात करना चाहेंगे
58  customer  customer_agree                    neutral     —             बात कराइए
59  agent     agent_wait                        —           —             expert agent से connect कर रही हूँ, line पर बने रहिए
60  agent     agent_other                       —           —             Transferring your call now
```

## Call GEN-myntra-d801b036-bc8f-45da-a31a-1468ff53712a (transferred) — 16 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_ask_question             neutral     —             delivery agent का contact detail, product delivery होगा आज
2   agent     agent_wait                        —           —             status check कर रही हूँ, कृपया line पर बने रहिए
3   agent     agent_answer_query                —           —             shipped है, आज शाम आठ बजे तक deliver, agent की details available नहीं
4   customer  customer_ask_question             neutral     —             update कब हो जाएगा, At what time
5   agent     agent_answer_query                —           —             exact time बताना मुश्किल है, app में update आ जाता है
6   customer  customer_ask_question             neutral     —             Puma slide, update बता सकते हैं क्या
7   agent     agent_wait                        —           —             details check कर रही हूँ, line पर बने रहिए
8   agent     agent_answer_query                —           —             काफी delay हो गया है, माफी चाहती हूँ, complaint register हो चुकी है
9   customer  customer_express_frustration      frustrated  —             twenty four hours, दो दिन से, update नहीं मिल रहा
10  agent     agent_de_escalate                 —           —             काफी समय से wait, case priority पर है
11  customer  customer_disagree                 frustrated  —             कल contact करूंगी, पांच छह item बाहर purchase करूंगी
12  agent     agent_de_escalate                 —           —             नाराजगी समझ सकती हूँ, जल्द से जल्द आप तक पहुँचे
13  customer  customer_end                      neutral     —             ठीक है, Thank you
14  agent     agent_end_call                    —           —             धन्यवाद, feedback form
15  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
```

## Call GEN-myntra-d9497653-524e-48c2-b129-35c93a72d15f (incomplete) — 36 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   agent     agent_other                       —           —             are you still there
2   customer  customer_ask_question             neutral     —             आवाज़ आ रही है मेरी
3   agent     agent_answer_query                —           —             कैसे मदद कर सकती हूँ
4   customer  customer_greet                    neutral     —             Hello
5   agent     agent_clarify                     —           —             बताइए
6   customer  customer_ask_query                neutral     —             एक बहुत order
7   agent     agent_clarify                     —           —             आपने क्या order
8   customer  customer_ask_query                neutral     —             tomorrow delivery
9   agent     agent_de_escalate                 —           —             समझ सकती हूँ
10  customer  customer_ask_question             frustrated  —             अभी तक क्यों नहीं आया है
11  agent     agent_de_escalate                 —           —             order का wait कर रहे हैं
12  customer  customer_other                    confused    —             —
13  agent     agent_de_escalate                 —           —             समझ सकती हूँ
14  customer  customer_other                    confused    —             —
15  agent     agent_de_escalate                 —           —             समझ सकती हूँ
16  customer  customer_other                    confused    —             —
17  agent     agent_answer_query                —           —             JOKER & WITCH Watch Gift Set, shipped है, 29 July तक deliver
18  customer  customer_unclear                  confused    —             thirtieth July
19  agent     agent_answer_query                —           —             29 July तक deliver हो जाएगा
20  customer  customer_unclear                  confused    —             July क्यों हुआ
21  agent     agent_de_escalate                 —           —             date change होने से, परेशान हैं
22  customer  customer_other                    confused    —             —
23  agent     agent_acknowledge                 —           —             —
24  customer  customer_other                    confused    —             —
25  agent     agent_de_escalate                 —           —             —
26  customer  customer_other                    confused    —             —
27  agent     agent_de_escalate                 —           —             —
28  customer  customer_other                    confused    —             —
29  agent     agent_ask_to_repeat               —           —             ठीक से समझ नहीं आई, फिर से बता सकते हैं
30  customer  customer_express_frustration      frustrated  —             उनतीस से तीस, तीस से एक
31  customer  customer_express_frustration      frustrated  —             यही problem है, इससे पहले भी
32  customer  customer_express_frustration      frustrated  —             बहुत order किया था, खुद ही cancel किया गया
33  agent     agent_de_escalate                 —           —             —
34  customer  customer_express_frustration      frustrated  —             order तो stop
35  agent     agent_de_escalate                 —           —             बार-बार date बदलने, काफी परेशान हैं, priority पर है
```

## Call GEN-myntra-e04e66b2-5de4-4cf7-a472-8d11c5a39f83 (completed) — 18 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_ask_question             neutral     —             कब तक
2   agent     agent_wait                        —           —             माफी चाहती हू, status check कर रही हू, line पर बने रहिए
3   agent     agent_answer_query                —           —             Mark View Jeans, shipped है, कल तक deliver
4   agent     agent_other                       —           —             क्या आप अभी भी वहां हैं
5   customer  customer_acknowledge              neutral     —             हां हां
6   agent     agent_clarify                     —           —             कुछ और पूछना चाहते हैं
7   customer  customer_ask_question             neutral     —             कल तक आ जाएगा ना
8   agent     agent_answer_query                —           —             कल तक deliver हो जाएगा, resolve करने की पूरी कोशिश
9   customer  customer_other                    confused    —             —
10  agent     agent_ask_to_repeat               —           —             समझ नहीं पाई
11  customer  customer_acknowledge              neutral     —             ठीक है, thank you
12  agent     agent_answer_query                —           —             कल तक deliver हो जाएगा, priority पर रख रहे हैं
13  customer  customer_acknowledge              neutral     —             गुस्सा नहीं नहीं
14  agent     agent_clarify                     —           —             कोई बात नहीं, कुछ और पूछना चाहते हैं
15  customer  customer_acknowledge              neutral     —             नहीं नहीं
16  agent     agent_end_call                    —           —             feedback form, call के लिए धन्यवाद
17  agent     agent_end_call                    —           —             Thank you for calling मिंत्रा, Have a great day
```

## Call GEN-myntra-e069ca08-7602-4558-9096-387753f33493 (completed) — 18 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_greet                    neutral     —             Hello, am I audible
2   agent     agent_answer_query                —           —             Yes, you are audible, How can I help you today
3   customer  customer_ask_query                neutral     —             ordered a pair of shoes, मिंत्रा for last week
4   agent     agent_wait                        —           —             let me check the status, Please stay on the line
5   customer  customer_other                    neutral     —             —
6   agent     agent_answer_query                —           —             shipped, Sholinganallur hub in Chennai, delivered by 29 July
7   customer  customer_ask_query                frustrated  —             delayed little bit faster, postponed to thirty one July, Before Friday
8   agent     agent_acknowledge                 —           —             I understand that you
9   customer  customer_ask_query                neutral     —             I want to use
10  agent     agent_answer_query                —           —             need your order urgently, fastest available route, cannot change the date
11  customer  customer_ask_question             neutral     —             probability of getting my order, before thirty first July
12  agent     agent_answer_query                —           —             on track to be delivered by 29 July, very high probability, by the 29th
13  customer  customer_end                      neutral     —             Ok, thank you, call you back
14  agent     agent_end_call                    —           —             most welcome, feedback form, Thank you for calling
15  agent     agent_end_call                    —           —             Thank you for calling मिंत्रा
16  customer  customer_end                      neutral     —             Ok, thank you
17  agent     agent_end_call                    —           —             —
```

## Call GEN-myntra-ef8bbf95-26bb-49b9-a01f-13607bf985fd (completed) — 24 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_greet                    neutral     —             Hello
2   agent     agent_clarify                     —           —             किस order, क्या issue है
3   customer  customer_ask_query                neutral     —             animal print crop top
4   agent     agent_clarify                     —           —             LULU & SKY Animal Print Crop Top, related है
5   agent     agent_wait                        —           —             status check, line पर बने रहिए
6   agent     agent_answer_query                —           —             shipped है, 12 August तक deliver
7   customer  customer_ask_query                neutral     —             twelve August, out of station
8   agent     agent_answer_query                —           —             12 August तक पहुँच जाएगा
9   customer  customer_ask_query                neutral     —             two weeks
10  agent     agent_answer_query                —           —             out of station, family या society security, 12 August तक deliver
11  customer  customer_disagree                 frustrated  —             है ही नहीं
12  agent     agent_ask_to_repeat               —           —             समझ नहीं पाई
13  customer  customer_disagree                 frustrated  —             नहीं नहीं, किसी और को भी नहीं, ten to twelve August
14  agent     agent_answer_query                —           —             चिंता न करें, 12 August तक deliver, पूरी कोशिश
15  customer  customer_ask_query                frustrated  —             पहले नहीं चाहिए
16  agent     agent_answer_query                —           —             समझ गई, 12 August तक deliver, delivery agent
17  customer  customer_ask_query                frustrated  —             बारह August तक, receive कर पाऊं
18  agent     agent_answer_query                —           —             बिलकुल clear, 12 August तक deliver, delivery agent
19  customer  customer_ask_query                frustrated  —             बारह August, अपना product चाहिए था
20  agent     agent_answer_query                —           —             12 August
21  customer  customer_ask_query                frustrated  —             दस August से पहले नहीं
22  agent     agent_end_call                    —           —             feedback form, धन्यवाद
23  agent     agent_end_call                    —           —             Thank you for calling मिंत्रा, Have a great day
```

## Call GEN-myntra-f4a6b55f-cb72-4193-8cd0-4aeaa6a6cb34 (completed) — 23 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_greet                    neutral     —             Hello ma'am
2   agent     agent_clarify                     —           —             किस order, क्या issue है
3   customer  customer_ask_query                neutral     —             watch order
4   customer  customer_ask_question             neutral     —             अभी तक आया नहीं, exact date, कब तक आ जाएगा
5   agent     agent_wait                        —           —             status check, line पर बने रहिए
6   agent     agent_answer_query                —           —             shipped है, delay हुआ है, कल तक deliver
7   agent     agent_clarify                     —           —             कुछ और पूछना चाहते
8   customer  customer_ask_question             neutral     —             can you give me
9   agent     agent_ask_to_repeat               —           —             —
10  customer  customer_ask_question             neutral     —             number मिल सकता है, order लेकर आऐंगे
11  agent     agent_answer_query                —           —             out for delivery नहीं है, My Orders page
12  agent     agent_clarify                     —           —             कुछ और पूछना चाहते हैं
13  customer  customer_ask_question             skeptical   —             sure है ना, order मिल जाएगा ना
14  agent     agent_answer_query                —           —             कल तक deliver, निश्चिंत रहें
15  customer  customer_ask_query                frustrated  —             assure कर दीजिए, कल मिल जाना चाहिए
16  agent     agent_acknowledge                 —           —             समझ रही हूँ
17  customer  customer_ask_query                frustrated  —             कोशिश कीजिए
18  agent     agent_answer_query                —           —             fastest route, पूरी कोशिश
19  customer  customer_ask_query                frustrated  —             जल्दी से जल्दी मिल जाए
20  agent     agent_answer_query                —           —             —
21  customer  customer_end                      happy       —             ठीक है, thank you
22  agent     agent_end_call                    —           —             feedback form, धन्यवाद
```

## Call GEN-myntra-ff2fc8dc-de97-4e8d-bd94-90bf775061d8 (transferred) — 27 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, Welcome to मिंत्रा, How may I help you
1   customer  customer_ask_query                frustrated  —             delivery birth date, reschedule, इकत्तीस तारीख
2   agent     agent_wait                        —           —             delivery date change, status check, line पर बने रहिए
3   agent     agent_answer_query                —           —             shipped है, 29 July तक deliver, Nadia hub
4   customer  customer_ask_question             confused    —             उनतीस तारीख तक मिल जाएगा ना, reschedule, इक्कीस तारीख
5   agent     agent_answer_query                —           —             29 July तक आपको मिल जाएगा
6   customer  customer_ask_query                skeptical   —             नहीं नहीं
7   customer  customer_ask_query                skeptical   —             इक्कीस तारीख को deliver होगा, message भी दिया है
8   agent     agent_wait                        —           —             अलग date दिखने से confusion, फिर से check कर रही हूँ
9   customer  customer_ask_query                frustrated  —             नहीं नहीं नहीं
10  customer  customer_express_frustration      frustrated  —             update ही नहीं है
11  agent     agent_de_escalate                 —           —             परेशानी समझ सकती हूँ, 29 July की ही date
12  customer  customer_disagree                 frustrated  —             अलग नहीं
13  agent     agent_clarify                     —           —             अपनी बात कहिए, क्या बताना चाह रहे हैं
14  customer  customer_express_frustration      frustrated  —             इक्कीस तारीख को दिखा रहा है, update ही नहीं है उसका
15  agent     agent_answer_query                —           —             31 July दिख रहा है
16  customer  customer_ask_question             confused    —             कब मिलेगा
17  agent     agent_answer_query                —           —             29 July तक deliver, order priority पर है
18  customer  customer_other                    neutral     —             —
19  agent     agent_clarify                     —           —             बताइए, क्या कहना चाहते
20  customer  customer_other                    frustrated  —             complaint लिख लीजिए
21  agent     agent_wait                        —           —             complaint register कर देती हूँ, line पर बने रहिए
22  customer  customer_express_frustration      frustrated  —             order cancel कर दूंगा, platform fee, refund में
23  agent     agent_answer_query                —           —             expert agent से connect, platform fee, order cancellation
24  customer  customer_agree                    neutral     —             हां हां, लिखिए
25  agent     agent_wait                        —           —             expert agent से connect, line पर बने रहिए
26  agent     agent_wait                        —           —             specialized team, Transferring your call now
```
