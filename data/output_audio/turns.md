# Per-turn intent capture

Every turn of every call — who spoke, the intent, sentiment, tool/API call, and the signal keywords.

## Call LCS-03F4 (incomplete) — 12 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_ask_question             —           —             कॉल, चेक, लीड, लाइन, इश्यू
1   agent     agent_greet                       —           —             hello, बात कर रही, से बात
2   customer  customer_provide_personal_details —           —             हमको
3   agent     agent_request_personal_details    —           —             जान, जिसके
4   customer  customer_ask_question             —           —             लीड, ऐसे, ताकि, गलत, चेंजेस
5   agent     agent_request_personal_details    —           —             लीड
6   customer  customer_ask_question             —           —             लीड, गलत
7   agent     agent_wait                        —           —             एक मिनट, मिनट
8   customer  customer_other                    —           —             चेक, लीड, लास्ट, गलत, हमको
9   agent     agent_wait                        —           —             एक मिनट, चेक, मिनट
10  agent     agent_wait                        —           —             देखिए, लगा
11  customer  customer_ask_question             —           —             customer, concern, support, option, application
```

## Call LCS-0ING (incomplete) — 2 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             किरा
1   customer  customer_ask_question             —           —             चेक, call, सब्सक्राइब, नंबर, देख
```

## Call LCS-0X5J (raised_request) — 23 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             आपसे
1   customer  customer_other                    confused    —             कैसे, सब्सक्राइब, काम, उनको, मैडम
2   agent     agent_answer_query                —           —             कहने, नीड
3   customer  customer_other                    —           —             राइट, रॉंग, रेजिस्टर, नीड, ट्रॉपर
4   agent     agent_request_pan                 —           —             चेक, नंबर
5   customer  customer_other                    —           —             देखो, इसी, नाइन, डबल
6   agent     agent_wait                        —           —             नाइन, डबल, फोर
7   customer  customer_query_fee                —           —             नाइन, डबल, सेवन, फोर
8   agent     agent_answer_query                —           —             जान, नाइन, सद्गुरू
9   customer  customer_ask_question             —           —             —
10  agent     agent_answer_query                —           —             लीड, देखिए, लास्ट, जान, देखो
11  customer  customer_report_done              —           —             लीड, तरीक
12  agent     agent_acknowledge                 —           —             बोलो, रॉंग, पढ़ता, पढ़
13  customer  customer_ask_query                —           —             —
14  agent     agent_acknowledge                 —           —             लीड, काम, request, check, issue
15  customer  customer_ask_question             —           —             मतलब, काम, देख, टाइम, बड़ा
16  agent     agent_answer_query                —           —             लीड, काम, प्रॉब्लम, ऐसे, लेके
17  customer  customer_query_fee                —           —             काम, देखो, पैसा, कितना, रुकिये
18  agent     agent_acknowledge                 —           —             ऐसा
19  customer  customer_express_distrust         frustrated  —             नहीं हो, उसको, बंद, डाला, उदर
20  agent     agent_reassure_trust              —           —             लीड, करूँगी, चेंजेस, दीजे, आइन
21  customer  customer_acknowledge              —           —             —
22  agent     agent_acknowledge                 —           —             —
```

## Call LCS-115Q (incomplete) — 15 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             हेलो, बोलो, हाँ।, हेलो।
1   customer  customer_query_fee                —           —             ऊपर, वाशी
2   agent     agent_answer_query                —           —             —
3   customer  customer_ask_question             —           —             ऊपर
4   agent     agent_request_business_details    —           —             अंदर, ऊपर
5   customer  customer_request_wait             —           —             अंदर
6   agent     agent_answer_query                —           —             —
7   customer  customer_report_done              —           —             दियो
8   agent     agent_answer_query                —           —             —
9   customer  customer_agree                    —           —             —
10  agent     agent_reassure_trust              —           —             उन्होंने
11  customer  customer_agree                    —           —             उन्होंने, दियो
12  agent     agent_acknowledge                 —           —             —
13  customer  customer_acknowledge              —           —             —
14  agent     agent_ask_to_repeat               —           —             देख
```

## Call LCS-18CV (raised_request) — 2 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             वेलकम
1   agent     agent_greet                       —           —             बात कर रही, कॉल, call, नंबर, काम
```

## Call LCS-1FT7 (incomplete) — 4 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             कॉल, call, person, wait, व्यक्ति
1   customer  customer_ask_question             —           —             speaking
2   agent     agent_wait                        —           —             कॉल, call, उसने, रखा, person
3   customer  customer_acknowledge              —           —             कॉल, उनको, थैंक, right, वाल
```

## Call LCS-1FT7 (transferred) — 7 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             कॉल, अल्लो, इन्दा, जेस्टर
1   agent     agent_answer_query                —           —             प्रॉब्लम, कस्टमर, उन्होंने, सपोर्ट, सर्विस
2   customer  customer_other                    —           —             रिगार्डिंग, हफ्ता, नीम
3   agent     agent_answer_query                —           —             लास्ट, डिपार्टमेंट, kyc, डॉक्यूमेंट, कोड़ा
4   customer  customer_acknowledge_transfer     —           —             kyc, पेंडिंग, नोड़ता, चक्मार
5   agent     agent_acknowledge                 —           —             —
6   customer  customer_acknowledge              —           —             अलवा
```

## Call LCS-1KJ9 (incomplete) — 11 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             request, issue, business, problem, जिसके
1   customer  customer_express_distrust         —           —             प्रॉब्लम, inquiry, लाइक, बाहर, दिखा
2   agent     agent_other                       —           —             मालो
3   customer  customer_other                    —           —             —
4   agent     agent_answer_query                —           —             चेक, लीड, देख, उन्होंने, आउट
5   customer  customer_other                    —           —             लीड, सब्सक्राइब, उसको, बोलते, सर्च
6   agent     agent_answer_query                —           —             लीड, उसको, search, जाए, जिसके
7   customer  customer_report_address_error     frustrated  —             नहीं हो, देने, होगे
8   agent     agent_answer_query                —           —             चेक, बिजनेस, रेटिंग, देखे, ऑप्शन
9   customer  customer_report_done              —           —             वीडियो
10  agent     agent_answer_query                —           —             कॉल, शेयर, रेटिंग, प्लीज, वेलकम
```

## Call LCS-1O0N (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             चेक, सब्सक्राइब, शेयर, लाइन, टाइम
```

## Call LCS-1QJ9 (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             कॉल, call, customer, thank, लिंक
```

## Call LCS-1V8M (incomplete) — 29 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_request_address             —           —             लेंगे, com, जस्टाइल
1   customer  customer_provide_business_details —           —             लेंगे, com, जस्टाइल
2   agent     agent_request_address             —           —             com, जस्टाइल
3   customer  customer_ask_query                —           —             लेंगे, याद, पेर
4   agent     agent_ask_to_repeat               —           —             पेर
5   customer  customer_other                    —           —             उन्होंने, कुमार
6   agent     agent_answer_query                —           —             कॉल, टीम, उन्होंने, अच्छी, सेंटर
7   customer  customer_ask_query                —           —             कॉल, मना, सेंटर, अटेंड, टेस्ट
8   agent     agent_answer_query                —           —             टाइम, उन्होंने, पाते
9   customer  customer_other                    —           —             वेरी, अटेंड, इपना
10  agent     agent_answer_query                —           —             टाइम, उन्होंने, आगे, लेंगे, वीडियो
11  customer  customer_other                    —           —             —
12  agent     agent_request_terms_accept        —           —             —
13  customer  customer_other                    —           —             वाट्सएप
14  agent     agent_reassure_trust              —           —             लीड, इनके, कंसन, पाने, डाउनलोड
15  customer  customer_other                    —           —             बैक, एंड, नांग
16  agent     agent_answer_query                —           —             सब्सक्राइब, हूँ।, करें।, नहीं।, इंट्रेस्ट
17  customer  customer_report_address_error     —           —             कोड़े
18  agent     agent_answer_query                —           —             —
19  customer  customer_skip_udyam               frustrated  —             नहीं हो, बेस्ट, प्र
20  agent     agent_other                       —           —             —
21  customer  customer_other                    —           —             —
22  agent     agent_acknowledge                 —           —             —
23  customer  customer_acknowledge              —           —             —
24  agent     agent_acknowledge                 —           —             लेंगे, बेस्ट
25  customer  customer_acknowledge              —           —             इदे, इप्पो
26  agent     agent_acknowledge                 —           —             इदे
27  customer  customer_acknowledge              —           —             इदे
28  agent     agent_acknowledge                 —           —             थैंक, फॉर, इन्होंने
```

## Call LCS-2374 (incomplete) — 17 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_explain_fee                 —           —             सब्सक्राइब
1   customer  customer_other                    —           —             लीड, रिगारिंग
2   agent     agent_help_address_error          —           —             लीड, रिगारिंग
3   customer  customer_acknowledge              —           —             आगे
4   agent     agent_answer_query                —           —             कस्टमर, बोलते, मिला
5   customer  customer_query_fee                —           —             ऐसा, पता, कितना
6   agent     agent_answer_query                —           —             call, काम, lead, टीम, inquiry
7   customer  customer_ask_question             —           —             अंदर, बताईए
8   agent     agent_wait                        —           —             काम, सपोर्ट, टिकेट, हेल्प, डाल
9   customer  customer_report_done              —           —             —
10  agent     agent_acknowledge                 —           —             चलेगा, किधर
11  customer  customer_other                    —           —             चलेगा, मंबई
12  agent     agent_acknowledge                 —           —             —
13  customer  customer_ask_question             —           —             चलेगा
14  agent     agent_answer_query                —           —             customer, लगा, support, ticket, हेल्प
15  customer  customer_acknowledge              —           —             रवी
16  agent     agent_acknowledge                 —           —             देखिए, चीज़ा
```

## Call LCS-2LVC (completed) — 27 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             जजजा
1   customer  customer_agree                    —           —             लेकर
2   agent     agent_answer_query                —           —             सब्सक्राइब, लास्ट, हलो, करें।, लेकर
3   customer  customer_other                    —           —             लास्ट, लॉगिन, जनवर
4   agent     agent_acknowledge                 —           —             —
5   customer  customer_other                    —           —             कॉल, में।, एक्सटर, मैंना।
6   agent     agent_answer_query                —           —             मिनट, अपडेट, देखते
7   customer  customer_report_done              —           —             अपडेट, देखते, ओके।, जेडी
8   agent     agent_acknowledge                 —           —             लाइन, लेंगे
9   customer  customer_acknowledge              —           —             लाइन, लेंगे
10  agent     agent_answer_query                —           —             इल्ला, रेस्पॉंस, मेंशन, जेसे
11  customer  customer_acknowledge              —           —             —
12  agent     agent_reassure_trust              —           —             कॉल, लीज़, इल्ला, फिल्टर, अन्ते
13  customer  customer_other                    —           —             मना, इल्ला, वालों, आइट
14  agent     agent_answer_query                —           —             लोगों, टाइमिंग, मैंना, वेस्ट
15  customer  customer_other                    —           —             टाइमिंग, मैंना
16  agent     agent_answer_query                —           —             टाइमिंग, नगर, बोर्ड, गंटा, एंटी
17  customer  customer_request_wait             —           —             प्रूफ, डॉक्यूमेंट, यदि
18  agent     agent_answer_query                —           —             सब्सक्राइब, बिजनेस, इतना, देते, करें।
19  customer  customer_respond_udyam            —           —             उद्यम, certificate
20  agent     agent_request_business_details    —           —             कंपनी, लगता, जस्ट, डीटेल्स, डाइल
21  customer  customer_do_otp                   —           —             नंबर, फोन
22  agent     agent_answer_query                —           —             इतना, लाइक, लीज, अपडेट, sms
23  customer  customer_other                    —           —             मैसेज
24  agent     agent_answer_query                —           —             लीड, सब्सक्राइब, कस्टमर, बिजनेस, हूँ।
25  customer  customer_other                    —           —             अल्लाँ
26  agent     agent_end_call                    —           —             कॉल, बिजनेस, सर्विस, टिकेट, कंपनी
```

## Call LCS-2PN8 (incomplete) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, चेक, लीड, अंदर, com
1   customer  customer_other                    —           —             —
2   agent     agent_answer_query                —           —             टाइम, थैंक, ग्रेट
```

## Call LCS-2SJT (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             सब्सक्राइब
```

## Call LCS-3C5E (raised_request) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             चेक, लीड, देख, शेयर, देखिए
1   customer  customer_report_sms_received      —           —             नंबर
2   agent     agent_answer_query                —           —             चेक, लीड, सब्सक्राइब, शेयर, फोन
```

## Call LCS-3ENT (transferred) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             से बात, 420709, 420701, 420702, कॉल
1   customer  customer_other                    —           —             thank
2   agent     agent_transfer_to_rm              —           transfer_to_rmcom, day, calling, nice, dot
```

## Call LCS-3IW7 (incomplete) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             कॉल, शेयर, ओपन, प्रोफाइल, अपडेट
1   customer  customer_express_distrust         —           —             अगले
2   agent     agent_other                       —           —             शेयर, अंदर, टिकेट, लेने, out
```

## Call LCS-3OK6 (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             बात कर रही, से बात, कॉल, call, शेयर
```

## Call LCS-3W62 (incomplete) — 9 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_guide_open_link             —           —             ओपन, वाटसप, देखा
1   customer  customer_ask_question             —           —             चाहते, देखना
2   agent     agent_answer_query                —           —             चेक, उसमें, देखते, whatsapp, resolution
3   customer  customer_other                    —           —             चेक, whatsapp
4   agent     agent_request_otp                 —           —             चेक
5   customer  customer_ask_question             —           —             चेक, प्रॉब्लम, उसमें, मोबाइल, सॉल्व
6   agent     agent_answer_query                —           —             ओपन, भेज, देखोगे
7   customer  customer_ask_question             —           —             पड़ेगा, मालूम
8   agent     agent_acknowledge                 —           —             —
```

## Call LCS-437E (transferred) — 16 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_ask_question             —           —             कंप्लेंट, अगले, लीट
1   agent     agent_answer_query                —           —             चाहते, अगले, लीट
2   customer  customer_agree                    —           —             —
3   agent     agent_answer_query                —           —             चाहते, अगले, लीट
4   customer  customer_express_distrust         —           —             सब्सक्राइब
5   agent     agent_present_offer               —           —             —
6   customer  customer_other                    —           —             आगे, नमक
7   agent     agent_wait                        —           —             सब्सक्राइब, लाइन, इतना, निंगे, चक्पण
8   customer  customer_request_wait             —           —             इतना, भाई, अगे, अदो
9   agent     agent_acknowledge                 —           —             नमके
10  customer  customer_other                    —           —             कस्टमर, अटेंड
11  agent     agent_answer_query                —           —             लीज़, याद, कमी
12  customer  customer_other                    —           —             एल्ला
13  agent     agent_ask_to_repeat               —           —             लीज़, मत्ते, रॉम, कंप्यून
14  customer  customer_acknowledge              —           —             मैडम, इश्यू, इला
15  agent     agent_transfer_to_rm              —           transfer_to_rmकॉल, सर्विस, रेटिंग, लेंगे, लाइक
```

## Call LCS-49S5 (incomplete) — 20 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             कॉम, जजजा, साम, कॉलेज, लॉट
1   agent     agent_answer_query                —           —             अंदर, लाइक, leads, back, लीड्स
2   customer  customer_other                    —           —             लेट, आउट, लेस्ट
3   agent     agent_answer_query                —           —             जस्ट, दूसरी, बड़ी, डाइल, अलड़ी
4   customer  customer_report_sms_received      —           —             पाई
5   agent     agent_present_offer               —           —             यूज़
6   customer  customer_acknowledge              —           —             —
7   agent     agent_answer_query                —           —             सब्सक्राइब, कंपनी, जस्टाइल, शुरू, पेर
8   customer  customer_report_done              —           —             —
9   agent     agent_answer_query                —           —             जिससे, सेकंड, कंसर्न, स्टेट, दोस्तो
10  customer  customer_other                    —           —             माता, शोर
11  agent     agent_answer_query                —           —             मैडम, अगे, डाउन, नीड, वर्ग
12  customer  customer_ask_question             —           —             मना, पता
13  agent     agent_answer_query                —           —             मैंना
14  customer  customer_other                    —           —             जस्ट, कलेक्ट
15  agent     agent_answer_query                —           —             —
16  customer  customer_agree                    —           —             चलता
17  agent     agent_acknowledge                 —           —             —
18  customer  customer_acknowledge              —           —             कारण, प्रोसेस
19  agent     agent_acknowledge                 —           —             कारण, प्रोसेस
```

## Call LCS-4E0N (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             बात कर रही, लीड, प्रॉब्लम, हूँ।, जान
```

## Call LCS-4GM3 (incomplete) — 0 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
```

## Call LCS-4P6Q (transferred) — 7 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             बात कर रही, टीम, सपोर्ट, com, हेलो
1   customer  customer_other                    —           —             कॉल, इश्यू, बोलते, लीज़, कहते
2   agent     agent_reassure_trust              —           —             कॉल, चेक, लीड, सब्सक्राइब, बिजनेस
3   customer  customer_acknowledge              —           —             थैंक, मिलेगा
4   agent     agent_answer_query                —           —             चेक, टीम, लीज, सेट, सर्च
5   customer  customer_other                    —           —             —
6   agent     agent_transfer_to_rm              —           transfer_to_rmकॉल, टाइम, सपोर्ट, ऑप्शन, रिक्वेस्ट
```

## Call LCS-55MJ (transferred) — 26 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             ऐसे, कॉम, कस्टुमर, लोट
1   customer  customer_acknowledge              —           —             —
2   agent     agent_acknowledge                 —           —             सब्सक्राइब
3   customer  customer_ask_question             —           —             लाइन, वीडियो, धन्यवाद, देखने
4   agent     agent_clarify                     —           —             चेक, नंबर, अंदर, सुन, सेकंड
5   customer  customer_other                    —           —             offline
6   agent     agent_answer_query                —           —             मिल, लेते, पूरा, leads, searches
7   customer  customer_other                    —           —             ऐसा, continue, offline
8   agent     agent_answer_query                —           —             जरूर, रिगार्डिंग, टोटल, बिजनस
9   customer  customer_other                    —           —             आगे, लीज, साल, भूल
10  agent     agent_answer_query                —           —             जरूर, मेल, कोंट्रैक्ट, बड़, रिक्वायमेंट
11  customer  customer_other                    —           —             next, ecs
12  agent     agent_answer_query                —           —             टिकेट
13  customer  customer_ask_question             —           —             —
14  agent     agent_answer_query                —           —             call, customer, support, ticket, मार्केटिंग
15  customer  customer_ask_query                —           —             उसको, आगे, raise, ticket, पता
16  agent     agent_answer_query                —           —             raise, ticket, किस, department, करी
17  customer  customer_react_to_offer           —           —             सब्सक्राइब, raise, ticket, उससे, करी
18  agent     agent_request_pan                 —           —             सब्सक्राइब, लाइन, ऑप्शन, किस, करी
19  customer  customer_other                    —           —             टिकेट, करूँगी, कॉंट्रेक्ट, पेमेंट, ecs
20  agent     agent_wait                        —           —             कॉल, टिकेट, रेट, अरेंज, करूँगी
21  customer  customer_acknowledge              —           —             —
22  agent     agent_acknowledge                 —           —             —
23  customer  customer_ask_question             —           —             —
24  agent     agent_transfer_to_rm              —           transfer_to_rmfeedback, service, link, आपसे, किये
25  customer  customer_acknowledge              —           —             —
```

## Call LCS-5DGE (raised_request) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, चेक, लीड, call, काम
1   customer  customer_acknowledge              —           —             प्रॉपर, देखिये
2   agent     agent_request_terms_accept        —           —             रेटिंग, मिलेगा, प्लीज, मिलता, यदि
```

## Call LCS-5JXW (incomplete) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             से बात, उसने, व्यक्ति
1   agent     agent_wait                        —           —             कॉल, call, रखा, person, hold
2   customer  customer_other                    —           —             कस्टमर, सपोर्ट, कॉम, वेलकम, डॉट
```

## Call LCS-5OKL (transferred) — 15 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             बोलिये, आलो
1   customer  customer_agree                    —           —             बोलिये
2   agent     agent_clarify                     —           —             कॉल, लीड, प्रॉब्लम, टीम, कॉम
3   customer  customer_ask_question             —           —             मतलब, लीड, इंक्वारी, दिक्कत
4   agent     agent_answer_query                —           —             बिजनेस, उसमें
5   customer  customer_ask_question             —           —             उसमें, बना
6   agent     agent_clarify                     —           —             —
7   customer  customer_other                    —           —             रखा
8   agent     agent_wait                        —           —             लेके, चलिए, तारिक
9   customer  customer_do_otp                   —           —             लीड
10  agent     agent_acknowledge                 —           —             तारिक
11  customer  customer_acknowledge              —           —             —
12  agent     agent_answer_query                —           —             फिल्टर, लेड, मार्च
13  customer  customer_acknowledge              —           —             चेक
14  agent     agent_ask_employment_type         —           —             चेक, काम, लगा, रखा, हेल्प
```

## Call LCS-5XWH (transferred) — 4 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_present_offer               —           —             नंबर, काम, देखिए, बिजनेस, फोन
1   customer  customer_express_distrust         —           —             call, customer, thank, feedback, service
2   agent     agent_transfer_to_rm              —           transfer_to_rmcall, काम, customer, thank, उनको
3   customer  customer_agree                    —           —             यूज़
```

## Call LCS-5Y7D (incomplete) — 6 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_other                    —           —             —
1   agent     agent_answer_query                —           —             कॉल, कस्टमर, कॉंट्रैक्ट, जजजा, सॉर्विस
2   customer  customer_agree                    —           —             दिखा
3   agent     agent_reassure_trust              —           —             बोल, ऐसा, दिखा, इंक्वाइरी
4   customer  customer_other                    —           —             काम, बोल, ऐसा, दोनों
5   agent     agent_wait                        —           —             एक मिनट, लाइन, देखे, मिनट, प्रॉपर
```

## Call LCS-6LB4 (incomplete) — 5 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_present_offer               —           —             लीड, नंबर, काम, प्रॉब्लम, ऐसा
1   customer  customer_ask_question             —           —             कॉल, लाइन, व्यक्ति, बोले, बुला
2   agent     agent_ask_to_repeat               —           —             लाइन, उनको, आलो
3   customer  customer_ask_question             —           —             कॉल, call, लाइन, उसने, रखा
4   agent     agent_answer_query                —           —             call, बोल, देखिए, टाइम, lead
```

## Call LCS-6R5O (transferred) — 8 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             लीड, काम, बिजनेस, आउट, एरिया
1   customer  customer_express_distrust         —           —             —
2   agent     agent_request_terms_accept        —           —             डबल, पिन, कोड
3   customer  customer_ask_question             —           —             —
4   agent     agent_request_address             —           —             कही, नगर
5   customer  customer_acknowledge              —           —             —
6   agent     agent_ask_to_repeat               —           —             सब्सक्राइब, चाहते, एरिया, दूँगा, गुड़
7   agent     agent_transfer_to_rm              —           transfer_to_rmसब्सक्राइब, नंबर, शेयर, लगा, रिसीव
```

## Call LCS-6W7C (transferred) — 7 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             नंबर, बोल, कीजिए, राइट, विशेष
1   customer  customer_react_to_offer           —           —             thank
2   agent     agent_transfer_to_rm              —           transfer_to_rmcall, customer, thank, feedback, service
3   customer  customer_other                    —           —             काम, इंक्वाइरी, मुझसे, नेज
4   agent     agent_reassure_trust              —           —             काम, आपसे, actually, लड़का
5   customer  customer_ask_question             —           —             बोलता, hours
6   agent     agent_answer_query                —           —             देखिए, inquiry, सर्विस, लिंक, रेटिंग
```

## Call LCS-70HM (incomplete) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             कॉल, देख, लाइन, कस्टमर, बिजनेस
1   customer  customer_ask_question             —           —             कॉल, thank, किये, धन्यवाद, बीच
2   agent     agent_wait                        —           —             एक मिनट, wait, कॉल, चेक, सब्सक्राइब
```

## Call LCS-76E1 (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, सब्सक्राइब, लाइन, सर्विस, लिंक
```

## Call LCS-79OA (incomplete) — 14 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             सपोर्ट, अंत, कॉन्ट्राक्ट, इन्दा
1   customer  customer_other                    —           —             —
2   agent     agent_present_offer               —           —             इश्यू, इदर
3   customer  customer_ask_question             —           —             number, self, rental, car
4   agent     agent_answer_query                —           —             car
5   customer  customer_ask_query                —           —             car
6   agent     agent_answer_query                —           —             car
7   customer  customer_ask_query                —           —             car
8   agent     agent_answer_query                —           —             इतना, लीज, car
9   customer  customer_ask_query                —           —             बढ़ता, स्टेट, दिए
10  agent     agent_answer_query                —           —             बढ़ता, दिए
11  customer  customer_ask_question             —           —             बढ़ता, दिए
12  agent     agent_acknowledge                 —           —             दिए, खड़मे
13  customer  customer_acknowledge              —           —             सब्सक्राइब
```

## Call LCS-7AAC (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             टिकेट, लाइक, करें।, कॉंट्रैक्ट, आवाज
```

## Call LCS-7HAV (incomplete) — 5 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             आगे, पता, इंक्वारी, पहली, जी।
1   customer  customer_other                    —           —             उन्होंने, इतना, उसको, समझ, आगे
2   agent     agent_request_business_details    —           —             business, लीड, शेयर, lead, contract
3   customer  customer_ask_query                —           —             देख, google
4   agent     agent_request_org_name            —           —             कॉल, शेयर, लिंक, रेटिंग, मिल
```

## Call LCS-7IM9 (transferred) — 10 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             आपसे, जिसके, तरफ, कमेंट, हलो।
1   agent     agent_acknowledge                 —           —             कॉम, डॉट, जस्ट, हलो।
2   customer  customer_other                    —           —             टीम, सपोर्ट, कस्टुमर, से।
3   agent     agent_answer_query                —           —             चेक, बिजनेस, अंदर, मिनट, प्रोफाइल
4   customer  customer_request_wait             —           —             मिनट, रिलेटेड
5   agent     agent_answer_query                —           —             —
6   customer  customer_report_done              —           —             —
7   agent     agent_request_pan                 —           —             चेक, रखा, पेमेंट, तारीख, लिस्टिंग
8   customer  customer_provide_address          —           —             आधार, कार्ड
9   agent     agent_transfer_to_rm              —           transfer_to_rmशेयर, request, देखे, रिक्वेस्ट, share
```

## Call LCS-7SJY (incomplete) — 6 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_other                    —           —             contact, चाहते, बंद
1   agent     agent_answer_query                —           —             कॉल, call, बोल, ऐसा, inquiry
2   customer  customer_express_distrust         —           —             लगाया, वालों, बैंक
3   agent     agent_request_personal_details    —           —             बिल्कुल, पूछ
4   customer  customer_provide_org_name         —           —             कॉल, टीम, आगे, जिसके, राइट
5   agent     agent_acknowledge                 —           —             प्लीज
```

## Call LCS-8844 (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             194949, कॉल, चेक, लीड, नंबर
```

## Call LCS-88GC (raised_request) — 34 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             उससे, इल्ला
1   customer  customer_express_distrust         —           —             बिजनेस, नाक
2   agent     agent_answer_query                —           —             नानी, गुड़ा
3   customer  customer_acknowledge              —           —             नाक
4   agent     agent_greet                       —           —             लेनी
5   customer  customer_query_fee                —           —             लीज़, दोस्तों
6   agent     agent_explain_fee                 —           —             लीज़
7   customer  customer_query_fee                —           —             लीज़, दोस्तों
8   agent     agent_ask_to_repeat               —           —             लीज़, दोस्तों
9   customer  customer_query_fee                —           —             लीज़, दोस्तों
10  agent     agent_acknowledge                 —           —             —
11  customer  customer_other                    —           —             —
12  agent     agent_answer_query                —           —             —
13  customer  customer_other                    —           —             —
14  agent     agent_ask_to_repeat               —           —             —
15  customer  customer_other                    —           —             —
16  agent     agent_wait                        —           —             अज़े
17  customer  customer_other                    —           —             देख
18  agent     agent_acknowledge                 —           —             देख
19  customer  customer_agree                    —           —             —
20  agent     agent_request_udyam               —           —             बिजनेस, सर्विस, इपने
21  customer  customer_ask_question             —           —             बिजनेस, लगे, काउंट, येश
22  agent     agent_answer_query                —           —             लेंगे
23  customer  customer_request_wait             —           —             लेंगे
24  agent     agent_answer_query                —           —             कहते, अल्लाँ, जर्च
25  customer  customer_ask_question             —           —             —
26  agent     agent_greet                       —           —             लाइक, कहते, अंतर, तारी, काल
27  customer  customer_acknowledge              —           —             —
28  agent     agent_acknowledge                 —           —             आगर
29  agent     agent_answer_query                —           —             सर्वेस, अधि, वालो
30  customer  customer_acknowledge              —           —             अधि
31  agent     agent_answer_query                —           —             लेंगे, इसको, लेके, सर्च, कहते
32  customer  customer_acknowledge              —           —             टीम
33  agent     agent_answer_query                —           —             डिपार्टमेंट, अलग, मार्ट, अले
```

## Call LCS-89OM (raised_request) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             कॉल, चेक, लीड, देख, शेयर
1   customer  customer_express_distrust         —           —             समझ, पूर्ण
2   agent     agent_reassure_trust              —           —             कॉल, चेक, लीड, टाइम, टीम
```

## Call LCS-89RR (transferred) — 22 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             concern, उससे
1   customer  customer_other                    —           —             inquiry, उनको, फोन, issue, लगा
2   agent     agent_answer_query                —           —             customer, lead, inquiry, support, भेजते
3   customer  customer_acknowledge              frustrated  —             नहीं हो, काम
4   agent     agent_acknowledge                 —           —             चेक, हूँ।, लेते, पैसे
5   customer  customer_express_distrust         —           —             चेक, लेते, इंक्वारी, सही, पैसे
6   agent     agent_acknowledge                 —           —             चेक, बोल, इंक्वारी, सही
7   customer  customer_ask_question             —           —             किस, इंक्वारी, बताई, एश्यू
8   agent     agent_answer_query                —           —             जगा
9   customer  customer_ask_query                —           —             उसको, बोलते, दिखा, बेचने, खाने
10  agent     agent_answer_query                —           —             inquiry, ऐसी, भाई, दीजे
11  customer  customer_acknowledge              —           —             नंबर, लास्ट
12  agent     agent_answer_query                —           —             देखिए, lead, concern, team, regarding
13  customer  customer_ask_query                —           —             call, back, arrange
14  agent     agent_ask_to_repeat               —           —             lead, inquiry, concern, सही, बोर
15  customer  customer_other                    —           —             team, अलग, department
16  agent     agent_answer_query                —           —             बोल, अरेंज, टीम्स, गॉल
17  customer  customer_ask_question             —           —             पूरा, कंसन, देगी
18  agent     agent_acknowledge                 —           —             कॉल, कीजिए, रेट
19  customer  customer_acknowledge              —           —             काम, देखे, खत्म
20  agent     agent_request_org_name            —           —             customer, lead, concern, contract, support
21  agent     agent_answer_query                —           —             कॉल, टीम, समझ, बेज, कीज
```

## Call LCS-8AF3 (incomplete) — 4 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             रिगार्डिंग, कॉंट्राक्ट, सेंड
1   customer  customer_other                    —           —             इश्यू, फेस, कॉंट्राक्ट
2   agent     agent_wait                        —           —             चेक, इश्यू, लेट, लाइव, विजिबिलिटी
3   customer  customer_acknowledge              —           —             —
```

## Call LCS-8EMS (transferred) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, सर्विस, सेट, डॉट
1   customer  customer_acknowledge              —           —             कॉल, देखते, पड़े
2   agent     agent_answer_query                —           —             —
3   customer  customer_query_fee                —           —             टाइमिंग, सेर
4   agent     agent_answer_query                —           —             लाइन, कॉम, डॉट, डाइल, दान
5   customer  customer_ask_query                —           —             अन्ते, दूर
6   agent     agent_confirm                     —           —             लेते, अन्ते
7   customer  customer_other                    —           —             —
8   agent     agent_acknowledge                 —           —             —
9   customer  customer_other                    —           —             लीड़, पार्ट, पिक
10  agent     agent_answer_query                —           —             सेट, लीड़, मैंना, सेर, अज़े
11  customer  customer_express_distrust         —           —             चेक, डिटेल्स, लीड़, एक्जांपल, अज़े
12  agent     agent_send_sms_link               —           —             —
13  customer  customer_other                    —           —             लीड़
14  agent     agent_answer_query                —           —             वेट, लोगों, फिल्टर, इंक्वायरी, सिस्टम
15  customer  customer_acknowledge              —           —             फॉरवर्ड
16  agent     agent_request_org_name            —           —             कॉल, call, नंबर, शेयर, customer
17  customer  customer_acknowledge              —           —             thank
18  agent     agent_transfer_to_rm              —           transfer_to_rmcom, day, calling, great, using
```

## Call LCS-93AB (transferred) — 29 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             customer, service, com, good, help
1   agent     agent_answer_query                —           —             leads, marketing, irrelevant, job
2   customer  customer_ask_question             —           —             बोल
3   agent     agent_answer_query                —           —             leads, irrelevant
4   customer  customer_report_address_error     —           —             leads, proper
5   agent     agent_send_sms_link               —           —             —
6   customer  customer_express_distrust         —           —             lead, issue
7   agent     agent_answer_query                —           —             call, marketing, mobile, job
8   customer  customer_ask_question             —           —             प्रॉब्लम, number, अच्छी, जान, business
9   agent     agent_answer_query                —           —             लीड़
10  customer  customer_other                    —           —             अलग, purpose
11  agent     agent_answer_query                —           —             ऐसा, ऐसे, अलग, देखोगे, जिनको
12  customer  customer_other                    —           —             लीड, काम, आउट, इसको, बाहर
13  agent     agent_answer_query                —           —             उनको, लाइट
14  customer  customer_express_distrust         frustrated  —             नहीं हो, उनको, बाहर, सीखा
15  agent     agent_answer_query                —           —             category, ऑप्शन, review, तुझे, लगे
16  customer  customer_ask_question             —           —             लास्ट, check, issue, hold, धीर
17  agent     agent_answer_query                —           —             request, ऐसे, कीजिए, message
18  customer  customer_respond_udyam            —           —             contract, response, problem, पूरा, complaint
19  agent     agent_answer_query                —           —             जिसका, जगह, account
20  customer  customer_other                    —           —             second, दिख, list, फिलाल
21  agent     agent_answer_query                —           —             —
22  customer  customer_report_done              —           —             उन्होंने, आये
23  agent     agent_transfer_to_rm              —           transfer_to_rmकॉल, टाइम, टीम, बुला, काफी
24  customer  customer_ask_question             —           —             मतलब, वाटसप, कहीं, मेल
25  agent     agent_answer_query                —           —             उन्होंने, बोला, लोगों, आये, ऑफिस
26  customer  customer_request_wait             —           —             टाइम, कीजिए
27  agent     agent_answer_query                —           —             फोन, उठा
28  customer  customer_skip_udyam               happy       —             thank you so much, चेक, call, customer, thank
```

## Call LCS-9EV3 (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             सब्सक्राइब, सर्विस, ऐसे, हलो, आवाज
```

## Call LCS-9MBJ (raised_request) — 17 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_explain_fee                 —           —             कॉल, शेयर, सर्वेस, कस्मो
1   customer  customer_agree                    —           —             बोली
2   agent     agent_disclose_recording          —           —             कॉल, thank, कॉंट्रैक्ट, होल्ड, कंसन
3   customer  customer_other                    —           —             बढ़ते
4   agent     agent_answer_query                —           —             चेक, लास्ट, डिटेल्स, टोटल, रेस्ट
5   customer  customer_acknowledge              —           —             —
6   agent     agent_answer_query                —           —             चेक, नंबर
7   customer  customer_request_wait             —           —             नंबर, मिनट, देखिये, लाइट, बोरो
8   agent     agent_answer_query                —           —             सर्विस, मैडम, रिसीव, दोनों, services
9   customer  customer_other                    —           —             services
10  agent     agent_answer_query                —           —             कॉल, लीड, नंबर, बोल, टाइम
11  customer  customer_acknowledge              —           —             नंबर, शेयर, बोल, मैडम
12  agent     agent_request_udyam               —           —             नंबर, मैडम
13  customer  customer_report_address_error     —           —             सॉरी
14  agent     agent_clarify                     —           —             कौन सा, चेक, नंबर, टाइम, inquiry
15  customer  customer_report_done              —           —             पूरे
16  agent     agent_request_org_name            —           —             कॉल, चेक, thank, feedback, concern
```

## Call LCS-9PBQ (raised_request) — 23 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_guide_open_link             —           —             लीड, आईएगी
1   customer  customer_provide_address          —           —             नंबर, बोर्ड
2   agent     agent_answer_query                —           —             लीड, उसने, पता
3   customer  customer_ask_question             —           —             इसमे
4   agent     agent_answer_query                —           —             category, number, service, mobile, repair
5   customer  customer_ask_question             —           —             number, mobile
6   agent     agent_ask_to_repeat               —           —             —
7   customer  customer_acknowledge              —           —             —
8   agent     agent_answer_query                —           —             बोली
9   customer  customer_agree                    —           —             दीजिये
10  agent     agent_request_pan                 —           —             नंबर
11  customer  customer_other                    —           —             नंबर, दीजिये
12  agent     agent_request_pan                 —           —             दीजिये
13  customer  customer_acknowledge              —           —             दीजिये
14  agent     agent_acknowledge                 —           —             कॉल, ऐसा, लेट, बोलते
15  customer  customer_request_wait             —           —             कॉल, मिनट, समय, वेट, जितना
16  agent     agent_other                       —           —             कॉल, लीड, लास्ट, मिनट, टोटल
17  customer  customer_ask_question             —           —             काम, उसमें, उससे, बना, जाओ
18  agent     agent_request_org_name            —           —             लीड, call, उसको, category, request
19  customer  customer_ask_question             —           —             उसको, देखे, time, पूरा
20  agent     agent_answer_query                —           —             कॉल, लीड, काम, टाइम, दिखा
21  customer  customer_ask_question             —           —             शोर
22  agent     agent_answer_query                —           —             अंदर, देते, डाल, बताईए, hours
```

## Call LCS-9V23 (incomplete) — 11 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             से बात, लीड, ऐसा, अंदर, उसमें
1   customer  customer_express_distrust         —           —             फोन, डाल
2   agent     agent_send_sms_link               —           —             फोन
3   customer  customer_ask_question             —           —             —
4   agent     agent_answer_query                —           —             मार्केटिंग, kyc, प्रोसेस, डीटेल
5   customer  customer_ask_question             confused    —             मतलब, मतलब क्या, उनको, समय, मार्केटिंग
6   agent     agent_answer_query                —           —             उन्होंने, बोला, अरेंज, दूँगा, जानना
7   customer  customer_report_address_error     —           —             —
8   agent     agent_answer_query                —           —             अरेंज
9   customer  customer_other                    —           —             चलो
10  agent     agent_answer_query                —           —             कॉल, देख, बिजनेस, लिंक, रिक्वेस्ट
```

## Call LCS-9XSU (transferred) — 5 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             चेक, नंबर, लाइन, customer, feedback
1   customer  customer_ask_question             —           —             उन्होंने, दोनों
2   agent     agent_reassure_trust              —           —             call, काम, बोल, लाइन, ऐसा
3   customer  customer_acknowledge              —           —             —
4   agent     agent_present_final_offer         —           —             कॉल, लीड, call, काम, देख
```

## Call LCS-A3M2 (incomplete) — 14 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_report_done              —           —             हो गया
1   agent     agent_send_sms_link               —           —             —
2   customer  customer_report_done              —           —             —
3   agent     agent_request_udyam               —           —             शेयर, business, update, msme, address
4   customer  customer_provide_address          —           —             address
5   agent     agent_wait                        —           —             चेक, पड़ेगा, msme
6   customer  customer_ask_question             —           —             दिखा, सिटी
7   agent     agent_ask_to_repeat               —           —             दिखा, नगर
8   customer  customer_request_wait             —           —             चेक, कोंटेक्ट
9   agent     agent_answer_query                —           —             ऐसा, लीज, प्रूफ, बिजनस, बिल
10  customer  customer_ask_question             —           —             बिल
11  agent     agent_request_udyam               —           —             उद्यम, ऑप्शन, समझ, लीज, पॉइंट
12  customer  customer_other                    —           —             —
13  agent     agent_answer_query                —           —             जाए, ticket, whatsapp, provide, दीजेगा
```

## Call LCS-A569 (incomplete) — 5 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             लीड, टिकेट, रिसीव, कॉंट्रैक्ट, इशू
1   customer  customer_acknowledge              —           —             उसमें
2   agent     agent_answer_query                —           —             —
3   customer  customer_ask_question             —           —             सब्सक्राइब
4   agent     agent_answer_query                —           —             कॉल, सब्सक्राइब, पूछ, चाहेंगे, दोस्तों
```

## Call LCS-A5YM (incomplete) — 6 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             लीड, good, डिपार्टमेंट, afternoon, लड़का
1   customer  customer_acknowledge              —           —             —
2   agent     agent_answer_query                —           —             शेयर, मार्केटिंग, रिगार्डिंग, करनी, कोंटेक्ट
3   customer  customer_acknowledge              —           —             —
4   agent     agent_request_org_name            —           —             शेयर, उसको, category, अच्छी, समझ
5   customer  customer_acknowledge              —           —             —
```

## Call LCS-AGNV (incomplete) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_ask_question             —           —             चेक, call, नंबर, बोल, बिजनेस
1   agent     agent_request_org_name            —           —             वीडियो, किये, धन्यवाद, बीच, उपयोग
2   customer  customer_other                    frustrated  —             नहीं हो रहा, नहीं हो, कॉल, चेक, प्रॉब्लम
```

## Call LCS-AR0V (raised_request) — 10 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_present_offer               —           —             सर्विस, इशू, कॉंट्रेक्ट, जर्जाल
1   customer  customer_express_distrust         —           —             इशू, कॉंट्रेक्ट, जर्जाल, बोले, रिलेटिट
2   agent     agent_send_sms_link               —           —             —
3   customer  customer_report_address_error     —           —             कॉल, पैसा, लिखे
4   customer  customer_report_address_error     —           —             प्रॉब्लम, अकम
5   agent     agent_other                       —           —             मैम, wrong, location, नीड
6   customer  customer_express_distrust         —           —             call, customer, phone, गलती, बोलेंगे
7   agent     agent_answer_query                —           —             काम, मैडम, लीज, problem, raise
8   customer  customer_skip_udyam               —           —             जरूर, चार
9   agent     agent_other                       —           —             सब्सक्राइब, रेस्ट, इश्योर
```

## Call LCS-ATFU (completed) — 15 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             से बात, लीड, ऐसी
1   customer  customer_express_distrust         —           —             प्रॉब्लम
2   agent     agent_answer_query                —           —             —
3   customer  customer_express_distrust         —           —             लीड, चलू
4   agent     agent_end_call                    —           —             लीड, जाओ, सलून
5   customer  customer_other                    —           —             लीड, मैडम, बोलो, डाला, बाकी
6   agent     agent_ask_to_repeat               —           —             category, area, wrong, किसने, sorry
7   customer  customer_ask_query                —           —             category, दिखा, दोनों, उन्हीं, एकी
8   agent     agent_answer_query                —           —             कॉल, देख, ऐसा, lead, लिंक
9   customer  customer_express_distrust         —           —             अंदर
10  agent     agent_answer_query                —           —             लिंक, दोनों, डाला, अप्रूफ, पढ़ा
11  customer  customer_express_distrust         —           —             —
12  agent     agent_acknowledge                 —           —             चेक, करनी, जाओ
13  customer  customer_other                    —           —             ओपन, पड़ेगा, करनी
14  agent     agent_answer_query                —           —             प्रॉब्लम, फोन, लें
```

## Call LCS-ATFU (completed) — 22 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             समय, लिंग
1   customer  customer_ask_question             —           —             बोल, समझ, कैसा, प्रूफ, लिंग
2   agent     agent_guide_open_link             —           —             बोल, लिंक, ओपन, देखो, क्लिक
3   customer  customer_express_distrust         —           —             उसको, ओपन, दिखा, जाओ
4   agent     agent_guide_open_link             —           —             उसको, ओपन
5   customer  customer_agree                    —           —             लिखे
6   agent     agent_guide_open_link             —           —             लिंक, देखिये
7   customer  customer_report_link_opened       —           —             मिनट, खुल
8   agent     agent_answer_query                —           —             option, changes, approve, लिखा, लिख
9   customer  customer_ask_question             —           —             अंदर, मिनट, return, email
10  agent     agent_answer_query                —           —             ओपन, चेंजेस, क्लिक, लिखा, अप्रूफ
11  customer  customer_report_done              —           —             अंदर, चेंजेस, लिखा
12  agent     agent_acknowledge                 —           —             how
13  customer  customer_ask_question             —           —             help, सेट, today
14  agent     agent_other                       —           —             बोल, देखो, कॉंट्रेक्ट, वाटसप, माई
15  customer  customer_unclear                  —           —             मैडम
16  agent     agent_wait                        —           —             देख, देखे, मैडम, देखो, यार
17  customer  customer_report_sms_received      —           —             लिंक भेज, लिंक, मिनट, मैडम, ओपन
18  agent     agent_answer_query                —           —             मैसेज, टेक्स, भेज
19  customer  customer_ask_question             —           —             मिल, मैसेज, टेक्स
20  agent     agent_end_call                    —           —             मिल
21  customer  customer_acknowledge              —           —             कॉल, नंबर, देख
```

## Call LCS-AZWX (incomplete) — 2 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             चेक, call, नंबर, देख, प्रॉब्लम
1   customer  customer_acknowledge              —           —             हलो
```

## Call LCS-AZWX (transferred) — 13 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             से बात, कस्टमर, रिक्वेस्ट, मार्केटिंग, बोलिए
1   customer  customer_ask_question             —           —             पता, हमको
2   agent     agent_answer_query                —           —             call, request, available, मार
3   customer  customer_react_to_offer           —           —             लीड, just, शायद
4   agent     agent_send_sms_link               —           —             लीड, मिल, रिक्वेस्ट, रिपोर्ट
5   customer  customer_ask_question             —           —             कॉल
6   agent     agent_answer_query                —           —             लीड
7   customer  customer_acknowledge              —           —             —
8   agent     agent_transfer_to_rm              —           transfer_to_rmलीड, रिपोर्ट
9   customer  customer_do_otp                   frustrated  —             नहीं हो, नंबर, एक्सटर
10  agent     agent_end_call                    —           —             कॉल
11  customer  customer_ask_question             —           —             मैनेजर
12  agent     agent_answer_query                —           —             जानना, जानते
```

## Call LCS-AZWX (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             से बात, call, lead, उनको, feedback
```

## Call LCS-B0WF (incomplete) — 10 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_wait                        —           —             जिसके, डॉट, डिपार्टमेंट, हेल्प, kyc
1   customer  customer_do_otp                   —           —             अप्शन
2   agent     agent_guide_open_link             —           —             चेक, देख, शेयर, देखिए, लाइन
3   customer  customer_acknowledge              —           —             —
4   customer  customer_report_done              —           —             —
5   agent     agent_clarify                     —           —             कॉल, चेक, call, देखिए, लाइन
6   customer  customer_ask_question             —           —             —
7   agent     agent_wait                        —           —             मेल, लीचे
8   customer  customer_other                    —           —             डॉट, जस्ट, डाइल
9   agent     agent_answer_query                —           —             कॉल, चेक, सब्सक्राइब, लेंगे, कॉम
```

## Call LCS-B7AU (transferred) — 9 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             रिक्वेस्ट, issue, business, रिसीव, जिसके
1   customer  customer_express_distrust         —           —             समय, kyc, related
2   agent     agent_transfer_to_rm              —           transfer_to_rmissue, kyc
3   customer  customer_other                    —           —             बोल, टाइम, उन्होंने, बोला, बताई
4   agent     agent_reassure_trust              —           —             चेक, contract, details, मैम, जिसके
5   customer  customer_respond_udyam            —           —             कंप्लीट, नीम
6   agent     agent_request_udyam               —           —             उद्यम, चेक, call, नंबर, देखिए
7   customer  customer_ask_question             —           —             —
8   agent     agent_clarify                     —           —             चेक, शेयर, ऑप्शन, raise, प्लीज
```

## Call LCS-BEVS (incomplete) — 2 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             कॉल, सब्सक्राइब, अरेंज, मार्केटिंग, बैक
1   customer  customer_report_done              —           —             सब्सक्राइब
```

## Call LCS-BEVS (incomplete) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             लीड, इश्यू, रिगार्डिंग, फेस, कीवर्ड्स
1   customer  customer_report_done              —           —             कीवर्ड्स
2   agent     agent_clarify                     —           —             कराने
```

## Call LCS-BFC9 (transferred) — 15 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             सर्विस, समय, फॉर्म
1   customer  customer_report_sms_received      frustrated  —             नहीं हो रहा, नहीं हो, मेसेज, लेड, रवी
2   agent     agent_acknowledge                 —           —             call, service, issue, problem, day
3   customer  customer_other                    —           —             कॉल
4   agent     agent_answer_query                —           —             लीड, लास्ट, रॉंग, आईए
5   customer  customer_express_distrust         —           —             कॉल, उनको, फोन, उठा, चेंज
6   agent     agent_send_sms_link               —           —             जाल
7   customer  customer_acknowledge              —           —             चेंज
8   agent     agent_answer_query                —           —             मिलता, करा, चेंज
9   customer  customer_ask_question             frustrated  —             मतलब, नहीं हो, call, इतना, बाहर
10  agent     agent_answer_query                —           —             चेक
11  customer  customer_react_to_final_offer     —           —             देख, उसमें, कितना, मिला
12  agent     agent_answer_query                —           —             मिला, चीन
13  customer  customer_express_distrust         —           —             मिला, चीन
14  agent     agent_reassure_trust              —           —             लीड, उसमें, जितना, चीन
```

## Call LCS-BG9F (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_request_pan                 —           —             चेक, देख, सपोर्ट, रिक्वेस्ट, समझ
```

## Call LCS-BNCL (incomplete) — 13 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             —
1   customer  customer_other                    —           —             —
2   agent     agent_answer_query                —           —             सब्सक्राइब, बिजनेस, ऑप्शन, लाइक, क्लिक
3   customer  customer_provide_business_details —           —             बिजनेस
4   agent     agent_ask_to_repeat               —           —             हेलो, audible, मेको, लोकल
5   customer  customer_acknowledge              —           —             मेको
6   agent     agent_acknowledge                 —           —             मेको
7   customer  customer_skip_udyam               —           —             —
8   agent     agent_offer_skip_udyam            —           —             —
9   customer  customer_skip_udyam               —           —             —
10  agent     agent_answer_query                —           —             सब्सक्राइब, उपयोग, विशेष
11  customer  customer_report_done              —           —             सब्सक्राइब, करें।
12  agent     agent_ask_to_repeat               —           —             category, वीडियो, अप्रूव, सॉरी, सार
```

## Call LCS-BPXM (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, सब्सक्राइब, देख, लाइन, सर्विस
```

## Call LCS-BSSY (completed) — 10 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             सब्सक्राइब, सबसे, वजह, notification, phone
1   agent     agent_answer_query                —           —             ऐसा, lead, request, ओपन, पूरा
2   customer  customer_other                    —           —             दिखा, report, नेटवर्क
3   agent     agent_answer_query                —           —             feedback, ताकि, लगता, पूरे, sms
4   customer  customer_other                    —           —             प्रॉब्लम
5   agent     agent_answer_query                —           —             काम, notification, लीट
6   customer  customer_ask_question             —           —             मतलब, check, option, महीने, notification
7   agent     agent_other                       —           —             बोल, सबसे, whatsapp, नोटिफिकेशन
8   customer  customer_respond_udyam            —           —             नंबर, हूँ।, मेल, चलो
9   agent     agent_end_call                    —           —             lead, बोला, करवा, sms, notification
```

## Call LCS-BYAQ (transferred) — 7 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             हूँ।
1   customer  customer_greet                    —           —             साइड, सर।, अलो।
2   agent     agent_transfer_to_rm              —           transfer_to_rmशेयर, बोल, बिजनेस, हूँ।, kyc
3   customer  customer_acknowledge              —           —             शेयर, असर
4   agent     agent_request_address             —           —             address, चेक, issue, business, kyc
5   customer  customer_ask_question             —           —             share, पूरा
6   agent     agent_acknowledge                 —           —             call
```

## Call LCS-C6FG (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, चेक, लीड, call, शेयर
```

## Call LCS-C6UL (incomplete) — 20 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_agree                    —           —             रिक्वेस्ट, तरफ
1   agent     agent_send_sms_link               —           —             जिसके, इशू, मिली, आपे
2   customer  customer_ask_question             —           —             inquiry, whatsapp, पेस्ट
3   agent     agent_ask_to_repeat               —           —             notification
4   customer  customer_other                    —           —             call, option, कुछी
5   agent     agent_reassure_trust              —           —             दिख
6   customer  customer_acknowledge              —           —             वाटसेप
7   agent     agent_reassure_trust              —           —             शेयर, देखिए, मिल, concern, समझ
8   customer  customer_ask_question             —           —             call, देते, option
9   agent     agent_ask_to_repeat               —           —             देख, lead, inquiry, मिल, number
10  customer  customer_acknowledge              —           —             दूँ
11  agent     agent_request_pan                 —           —             call, देते, option, पढ़
12  customer  customer_ask_query                —           —             साल
13  agent     agent_answer_query                —           —             वहीं
14  customer  customer_ask_question             —           —             मार्च
15  agent     agent_clarify                     —           —             whatsapp, sms, provide, नोटिफिकेशन, माध्यम
16  customer  customer_other                    —           —             whatsapp, notification, मान, चलिए
17  agent     agent_reassure_trust              —           —             आपसे, whatsapp, नॉटिफिकेशन, सेटिंग
18  customer  customer_acknowledge              —           —             चाह
19  agent     agent_clarify                     —           —             लिंक, रेटिंग, मिल, मिलेगा, जाए
```

## Call LCS-CIX6 (incomplete) — 7 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             इल्ला, लगता, इन्हां, अल्लो, बढ़ता
1   customer  customer_query_fee                —           —             अपडेट, माड़ी
2   agent     agent_answer_query                —           —             category, लीज, बढ़ता, चक्मा, मड़म
3   customer  customer_acknowledge              —           —             हूँ।, ओके।
4   agent     agent_answer_query                —           —             लाइक, रिपोर्ट, फीडबैक, कैटेगरी, लगते
5   customer  customer_acknowledge              —           —             चेक, नोट, जागा, माड़
6   agent     agent_acknowledge                 —           —             —
```

## Call LCS-CLJ2 (incomplete) — 24 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             कॉल, लगा, हलो, टेक्स
1   agent     agent_acknowledge                 —           —             लगा, हलो
2   customer  customer_express_distrust         —           —             कस्टमर, बोलते, कॉम, डॉट, जर्जाल
3   agent     agent_answer_query                —           —             चाली
4   customer  customer_acknowledge              —           —             ओके।, हलो।
5   agent     agent_explain_fee                 —           —             लीड, शेयर, ओके।, अलड़ी, चाली
6   customer  customer_acknowledge              —           —             चेक
7   agent     agent_answer_query                —           —             इतना, जिसमें, रखो, भूल, वापर
8   customer  customer_other                    —           —             मिनट, चाहते, इंक्वारी, गलत, बोलना
9   agent     agent_answer_query                —           —             इंक्वारी, दोनों, गलत
10  customer  customer_request_wait             —           —             चेक, मिनट, लेते
11  agent     agent_ask_to_repeat               —           —             बोल, प्रॉब्लम, लाइन, अच्छी, समझ
12  customer  customer_other                    —           —             सबसे, पहली, कंट्राक्ट
13  agent     agent_acknowledge                 —           —             —
14  customer  customer_express_distrust         —           —             ऐसे, प्रॉपर, मना, इंक्वाइरी, कंट्राक्ट
15  agent     agent_answer_query                —           —             काम, शेयर, प्रॉब्लम, complaint, दूसरी
16  customer  customer_ask_question             —           —             समझ, जरूरत
17  agent     agent_answer_query                —           —             इसको
18  customer  customer_ask_question             —           —             —
19  agent     agent_acknowledge                 —           —             काम, बोल, प्रॉब्लम, inquiry, आगे
20  customer  customer_other                    —           —             प्लीज
21  agent     agent_answer_query                —           —             देख, प्रॉपर
22  customer  customer_skip_udyam               —           —             —
23  agent     agent_acknowledge                 —           —             पूरा, पड़ेगा, वाल
```

## Call LCS-CRB6 (transferred) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             customer, service, good, afternoon, jaisal
1   customer  customer_respond_udyam            —           —             business, help, how, wrong, lease
2   agent     agent_answer_query                —           —             lease, now, getting
3   customer  customer_express_distrust         —           —             काम, ऐसे, आगे, इश्यू, आपसे
4   agent     agent_answer_query                —           —             बड़ा
5   customer  customer_react_to_offer           —           —             रॉंग
6   agent     agent_explain_fee                 —           —             दोनों
7   customer  customer_report_address_error     —           —             प्रॉब्लम
8   agent     agent_request_address             —           —             नंबर, रजिस्टर, मोबाल
9   customer  customer_report_address_error     —           —             नंबर, रजिस्टर
10  agent     agent_request_address             —           —             नंबर, भाई, ऑफिस, रजिस्टर, मोबाल
11  customer  customer_express_distrust         —           —             उसको, लोगों, बोलता, तुम्हारे, रुपया
12  agent     agent_acknowledge                 —           —             —
13  customer  customer_ask_question             —           —             यार
14  agent     agent_answer_query                —           —             पैसा, बेच
15  customer  customer_react_to_final_offer     —           —             पैकेज, हमको, तुमने
16  agent     agent_reassure_trust              —           —             पैसे
17  customer  customer_acknowledge              —           —             इंपोर्टेंट
18  agent     agent_present_final_offer         —           —             देख, प्रॉब्लम, मैडम, पैसा, बिजनस
```

## Call LCS-D3HH (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             call, सब्सक्राइब, नंबर, टाइम, customer
```

## Call LCS-D4BD (incomplete) — 14 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             अल्लो
1   agent     agent_answer_query                —           —             कॉल, इन्हां
2   customer  customer_express_distrust         —           —             देखेंगे, इन्हों
3   agent     agent_acknowledge                 —           —             देखेंगे, नोड़ता, चक्मा, इले
4   customer  customer_other                    —           —             —
5   customer  customer_express_distrust         —           —             नेंगे
6   agent     agent_answer_query                —           —             —
7   customer  customer_express_distrust         —           —             इसको, नोड़ता
8   agent     agent_ask_to_repeat               —           —             मड़म
9   customer  customer_other                    —           —             मड़म
10  agent     agent_acknowledge                 —           —             अरेंच
11  customer  customer_other                    —           —             अपलोड
12  agent     agent_ask_to_repeat               —           —             —
13  customer  customer_skip_udyam               —           —             शुरू, अपलोड
```

## Call LCS-DF7C (incomplete) — 7 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_acknowledge                 —           —             —
1   customer  customer_express_distrust         —           —             लीड्स, तुम्हारे
2   agent     agent_reassure_trust              —           —             लीड्स, तुम्हारे
3   customer  customer_acknowledge              —           —             —
4   agent     agent_acknowledge                 —           —             —
5   customer  customer_agree                    —           —             सब्सक्राइब
6   agent     agent_acknowledge                 —           —             सब्सक्राइब
```

## Call LCS-DMBH (transferred) — 25 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_query_fee                —           —             लीड
1   agent     agent_answer_query                —           —             लीड, बड़ा
2   customer  customer_agree                    —           —             लीड
3   agent     agent_answer_query                —           —             आगे, नोटिफिकेशन, रुके, सेंड
4   customer  customer_report_sms_received      —           —             —
5   agent     agent_wait                        —           —             टाइम, आये, नोटिफिकेशन, मिनट्स, नमके
6   customer  customer_other                    —           —             लेट, इले
7   agent     agent_wait                        —           —             देख, लेट
8   customer  customer_acknowledge              —           —             देख
9   agent     agent_answer_query                —           —             नंबर, लेंगे, कंप्लेंट, जस्टाइल, मेल
10  customer  customer_other                    —           —             टीम, फोन, ओपन, मना, बैक
11  agent     agent_answer_query                —           —             लीड, टाइम, सेट, आवरेज, रेस्पॉन्स
12  customer  customer_ask_query                —           —             नंबर, अंत
13  agent     agent_answer_query                —           —             नंबर
14  customer  customer_report_address_error     —           —             नंबर
15  agent     agent_answer_query                —           —             इतना, उसको
16  customer  customer_acknowledge              —           —             —
17  agent     agent_answer_query                —           —             नंबर, उन्होंने, अच्छी, इश्यू, अपडेट
18  customer  customer_do_otp                   —           —             इश्यू, इप्पो
19  agent     agent_wait                        —           —             सेंड
20  customer  customer_acknowledge              —           —             पाते, अलो।
21  agent     agent_transfer_to_rm              —           transfer_to_rm—
22  customer  customer_other                    —           —             इन्हों
23  agent     agent_wait                        —           —             —
24  customer  customer_acknowledge              —           —             सब्सक्राइब
```

## Call LCS-E4SV (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, लीड, टिकेट, इश्यू, कॉम
```

## Call LCS-E5K5 (incomplete) — 33 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             सब्सक्राइब, शेयर, टाइम, lead, उन्होंने
1   customer  customer_express_distrust         —           —             लेंगे, message, company, नेंगे, received
2   agent     agent_answer_query                —           —             —
3   customer  customer_ask_question             —           —             —
4   agent     agent_answer_query                —           —             देखते, complaint
5   customer  customer_express_distrust         —           —             देखते, complaint, अगले, कम्प्लेंट, वाइट
6   agent     agent_wait                        —           —             —
7   customer  customer_other                    —           —             —
8   agent     agent_acknowledge                 —           —             —
9   customer  customer_other                    —           —             लोगी
10  agent     agent_wait                        —           —             नीचे, रुके, दोस्त
11  customer  customer_other                    —           —             कॉल, लेंगे, कंपनी, सेंटर, रुके
12  agent     agent_answer_query                —           —             —
13  customer  customer_ask_question             frustrated  —             नहीं हो
14  agent     agent_other                       —           —             —
15  customer  customer_query_fee                —           —             सब्सक्राइब, लीट्स, नालगी
16  agent     agent_answer_query                —           —             उनको, यूजर
17  customer  customer_acknowledge              —           —             —
18  agent     agent_answer_query                —           —             यूजर, उगल
19  customer  customer_acknowledge              —           —             वरू
20  agent     agent_answer_query                —           —             यूजर, वरू
21  customer  customer_express_distrust         —           —             लीड, यूजर, वरू
22  agent     agent_acknowledge                 —           —             यूजर
23  customer  customer_respond_udyam            —           —             यूजर
24  agent     agent_request_udyam               —           —             मार्केटिंग, सोली
25  customer  customer_agree                    —           —             सब्सक्राइब, करें।
26  agent     agent_request_business_details    —           —             कस्टमर, उनको, आगे, इसको, कंप्लेंट
27  customer  customer_report_address_error     frustrated  —             नहीं हो, लीड
28  agent     agent_answer_query                —           —             उम्मी
29  customer  customer_acknowledge              —           —             उम्मी
30  agent     agent_acknowledge                 —           —             नांग
31  customer  customer_acknowledge              —           —             कंप्लेंट
32  agent     agent_wait                        —           —             वेट, अगले, यूजर, जाना।, लीट्स
```

## Call LCS-ECE2 (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             —
```

## Call LCS-EE1V (incomplete) — 7 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             कस्टमर्स, जजजाई
1   customer  customer_query_fee                —           —             लीड, इतना, लेकर, दूसरा, कस्टमर्स
2   agent     agent_answer_query                —           —             चेक, काम, देख, मिल, कीजिए
3   customer  customer_other                    —           —             —
4   agent     agent_other                       —           —             —
5   customer  customer_acknowledge              —           —             —
6   agent     agent_help_address_error          —           —             प्रॉब्लम, सपोर्ट, ऑप्शन, मिलता, जाकर
```

## Call LCS-EOD9 (incomplete) — 5 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नानी, इन्होंना
1   customer  customer_express_distrust         —           —             कॉल, रखा, व्यक्ति, होल्ड, बने
2   agent     agent_answer_query                —           —             सब्सक्राइब, प्रॉब्लम, टाइम, सपोर्ट, इतना
3   customer  customer_ask_question             —           —             लाओ
4   agent     agent_ask_to_repeat               —           —             धन्यवाद, हेलो, माता
```

## Call LCS-ERUS (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             कॉल, चेक, काम, देखिए, बिजनेस
```

## Call LCS-F1GL (incomplete) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             से बात, call, बोल, customer, बिजनेस
1   customer  customer_express_distrust         —           —             call, customer, thank, feedback, service
2   agent     agent_wait                        —           —             थैंक, जाए, भाई, hold, चीज़ा
```

## Call LCS-FE74 (incomplete) — 13 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             हेलो, इश्यों
1   customer  customer_ask_question             —           —             सर्विस, एरिया, लाइट, अधि, पिन
2   agent     agent_answer_query                —           —             अन्ते
3   customer  customer_ask_question             —           —             —
4   agent     agent_request_pan                 —           —             टेन
5   customer  customer_agree                    —           —             हाँ।, मेको
6   agent     agent_acknowledge                 —           —             अन्ते, मेंचे
7   customer  customer_query_fee                —           —             अन्ते, अगे, मेंचे, मेको
8   agent     agent_wait                        —           —             लाइक, अन्ते, ज़रूर, अन्ने
9   customer  customer_request_wait             —           —             अन्ने
10  agent     agent_acknowledge                 —           —             ज़रूर, अन्ने
11  customer  customer_report_address_error     —           —             देखने, उत्तर
12  agent     agent_ask_to_repeat               —           —             चेक, इतना, बड़ा, इनके, ओके।
```

## Call LCS-FEM8 (raised_request) — 24 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_guide_open_link             —           —             वेलकम, डॉटकॉम
1   customer  customer_ask_query                —           —             टीम, सपोर्ट, कस्टम, हाई, टुड़े
2   agent     agent_answer_query                —           —             —
3   customer  customer_ask_question             —           —             लीड, नंबर, बोल, जान, एरिया
4   agent     agent_ask_to_repeat               —           —             लीड्स
5   customer  customer_express_distrust         frustrated  —             बार बार, फोन, देखिये, बोलता, किसने
6   agent     agent_answer_query                —           —             lead, गलत, recent, बताइ
7   customer  customer_ask_question             —           —             ऐसा, महीने, चार, पांच, office
8   agent     agent_acknowledge                 —           —             —
9   customer  customer_ask_question             —           —             काम, महीने
10  agent     agent_answer_query                —           —             कॉल, काम, उसमें, डिटेल्स
11  customer  customer_acknowledge              —           —             इंटर
12  agent     agent_clarify                     —           —             उनको, उसको, उसमें, देखिये, पूछते
13  customer  customer_other                    —           —             —
14  agent     agent_wait                        —           —             देख
15  customer  customer_ask_question             —           —             उसमें, ऐसे, बोलिये, प्रेस, बढ़िया
16  agent     agent_acknowledge                 —           —             बड़ा, आवाज, बड़
17  customer  customer_acknowledge              —           —             देखिए, आवाज, सुन
18  agent     agent_other                       —           —             देखिए, प्रॉपर, रिस्पॉंस
19  customer  customer_ask_question             —           —             प्रोफाइल
20  agent     agent_answer_query                —           —             नंबर, करूँगी, बेट, करिए
21  customer  customer_respond_udyam            —           —             देखे, प्रोफाइल, मिलेगा, चेंजी, इसने
22  agent     agent_acknowledge                 —           —             कॉल, कस्टमर, सपोर्ट, thank, concern
23  customer  customer_other                    —           —             com
```

## Call LCS-FICV (incomplete) — 5 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_answer_query                —           —             customer, service, good, how, afternoon
2   customer  customer_do_otp                   —           —             लीड, नंबर, हलो, इसको, help
3   agent     agent_answer_query                —           —             हलो, जैसा, आवाज, सेकंड
4   customer  customer_other                    —           —             बोरो
```

## Call LCS-FPJ7 (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             चाहता, पंपी
```

## Call LCS-FPJ7 (incomplete) — 18 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             person, speaking, called
1   agent     agent_answer_query                —           —             चेक, बड़ा, हलो, wait, साइड
2   customer  customer_acknowledge              —           —             इश्यों
3   agent     agent_other                       —           —             लीड, लास्ट, रोज, इकड़ा
4   customer  customer_agree                    —           —             —
5   agent     agent_ask_to_repeat               —           —             अन्ने, लगते
6   customer  customer_request_wait             —           —             —
7   agent     agent_answer_query                —           —             अन्ते, दान, वालो
8   customer  customer_express_distrust         frustrated  —             नहीं हो, वालो
9   agent     agent_answer_query                —           —             नहीं।
10  customer  customer_express_distrust         —           —             बड़ी
11  agent     agent_answer_query                —           —             लेंगे, सबस्क्राइब, जनवर
12  customer  customer_ask_query                —           —             अंदर, लास्ट, लेट, करें।, पूर्ट
13  agent     agent_answer_query                —           —             लगा, अपडेट, सर्चेस, यूजर, अरे
14  customer  customer_skip_udyam               —           —             —
15  agent     agent_acknowledge                 —           —             —
16  customer  customer_skip_udyam               —           —             इसको, पैकेज
17  agent     agent_help_address_error          —           —             951523, कॉल, call, लिंक, अच्छी
```

## Call LCS-FPO5 (incomplete) — 3 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, शेयर, लाइन, कस्टमर, लेते
1   customer  customer_report_done              —           —             —
2   agent     agent_answer_query                —           —             कॉल, चेक, लीड, नंबर, उन्होंने
```

## Call LCS-FWYG (transferred) — 9 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, टाइम, लेंगे, जस्टाइल, कनेक्ट
1   customer  customer_query_fee                —           —             टाइम, कनेक्ट
2   agent     agent_answer_query                —           —             चेक, लिंक, टिकेट, लेंगे, team
3   customer  customer_request_wait             —           —             आदि
4   agent     agent_request_pan                 —           —             नंबर
5   customer  customer_ask_query                —           —             टाइम, नोटिफिकेशन
6   agent     agent_answer_query                —           —             नंबर, उनको, आउट, बेस्ट, कंसर्न
7   customer  customer_report_done              —           —             —
8   agent     agent_transfer_to_rm              —           transfer_to_rm—
```

## Call LCS-G4GA (incomplete) — 15 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_request_business_details    —           —             सब्सक्राइब, काम, कंपनी, लीड्स, उन्हीं
1   customer  customer_query_fee                —           —             लीड
2   agent     agent_clarify                     —           —             मतलब, चेक, लीड, category, उसमें
3   customer  customer_ask_query                —           —             —
4   agent     agent_acknowledge                 —           —             सब्सक्राइब, जरूर
5   customer  customer_acknowledge              —           —             सब्सक्राइब, मिल, जरूर, देखने
6   agent     agent_answer_query                —           —             बिजनेस, गलत, एंड, डाउन
7   customer  customer_report_done              —           —             टोटल
8   agent     agent_answer_query                —           —             कॉल, अंदर, अच्छी, समझ, उससे
9   customer  customer_ask_question             —           —             टाइम
10  agent     agent_answer_query                —           —             ऐसा, पूरे
11  customer  customer_acknowledge              —           —             application, ज़रूरत
12  agent     agent_answer_query                —           —             शेयर, lead, लिंक, लास्ट, response
13  customer  customer_report_done              —           —             देखिए, अंदर
14  agent     agent_wait                        —           —             एक मिनट, लीड, ऐसा, उसको, मिल
```

## Call LCS-G7KI (transferred) — 38 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_react_to_offer           —           —             वेलकम
1   agent     agent_answer_query                —           —             उन्होंने, फोन, बाहर, ऐसी, सबसे
2   customer  customer_agree                    —           —             लेते
3   agent     agent_greet                       —           —             बताईए
4   customer  customer_ask_question             —           —             चेक, call, lead, concern, लाइक
5   agent     agent_reassure_trust              —           —             लीड, lead, उनको, फोन, share
6   customer  customer_other                    —           —             फोन, उठा
7   agent     agent_answer_query                —           —             बिजनेस, उन्होंने, ऐसी, जस्ट, गूगल
8   customer  customer_agree                    —           —             उन्होंने
9   agent     agent_present_offer               —           —             बाकी
10  customer  customer_ask_question             —           —             गूगल, लिस्टिंग, प्लान
11  agent     agent_answer_query                —           —             कॉल, लीड, काम, बोल, टाइम
12  customer  customer_ask_question             —           —             देखे, concern, time, searches, profile
13  agent     agent_answer_query                —           —             उनको, देखे, लेकर, आये, upload
14  customer  customer_ask_question             —           —             लीड, सब्सक्राइब, बोल, देखिए, बोला
15  agent     agent_send_sms_link               —           —             call, देखिए, lead, अंदर, मिल
16  customer  customer_express_distrust         —           —             ऐसा, मिल, check, response, बोला
17  agent     agent_answer_query                —           —             लीड, देखिए, उन्होंने, फोन, उसने
18  customer  customer_acknowledge              —           —             —
19  agent     agent_answer_query                —           —             टाइम, मिल, पैसा, पता, कहते
20  customer  customer_other                    —           —             बिल्कुल
21  agent     agent_acknowledge                 —           —             बोल, पता, सही
22  customer  customer_express_distrust         —           —             किस, कनेक्ट, कुमार, बोर
23  agent     agent_transfer_to_rm              —           transfer_to_rmआये, कुमार
24  customer  customer_acknowledge              —           —             जिससे, जेडी
25  agent     agent_answer_query                —           —             नंबर, फोन, उठा
26  customer  customer_skip_udyam               —           —             चेक, नंबर, कीजिए, issue, resolution
27  agent     agent_answer_query                —           —             मिल, अच्छी, problem, refund
28  customer  customer_express_distrust         —           —             concern, मिलेगा, complaint, raise, help
29  agent     agent_reassure_trust              —           —             लीड, देखिए, ऐसा, उनको, ऐसे
30  customer  customer_express_distrust         frustrated  —             नहीं हो, चेक, लीड, काम, शेयर
31  agent     agent_answer_query                —           —             बाकि, ecs
32  customer  customer_ask_question             —           —             —
33  agent     agent_acknowledge                 —           —             —
34  customer  customer_ask_question             —           —             —
35  agent     agent_answer_query                —           —             महीने, month
36  customer  customer_acknowledge              —           —             call, thank, number, concern, issue
37  agent     agent_acknowledge                 —           —             end
```

## Call LCS-GBI7 (transferred) — 17 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_answer_query                —           —             सब्सक्राइब, लीज
1   customer  customer_express_distrust         —           —             लीज
2   agent     agent_acknowledge                 —           —             लीज
3   customer  customer_acknowledge              —           —             लीज
4   agent     agent_acknowledge                 —           —             चेक
5   customer  customer_other                    —           —             लाइन, मिनिट
6   agent     agent_answer_query                —           —             लाइन, inquiry, लास्ट, check, contract
7   customer  customer_ask_query                —           —             शेयर, अन्ता, लाइफ
8   agent     agent_answer_query                —           —             —
9   customer  customer_react_to_final_offer     —           —             देखिए
10  agent     agent_acknowledge                 —           —             देखिए
11  customer  customer_acknowledge              —           —             देखिए
12  agent     agent_answer_query                —           —             अपडेट, प्रॉपर, आउट, एवरी, लाग
13  customer  customer_respond_udyam            —           —             बढ़ता
14  agent     agent_answer_query                —           —             —
15  customer  customer_acknowledge              —           —             बढ़ता
16  agent     agent_clarify                     —           —             जाए, लाइव, तीके, अक्टिव, इश्य
```

## Call LCS-GOQS (raised_request) — 7 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, इश्यू, अरेंज
1   customer  customer_other                    —           —             लेट
2   agent     agent_acknowledge                 —           —             लेट
3   customer  customer_acknowledge              —           —             लेट
4   agent     agent_reassure_trust              —           —             चेक, सब्सक्राइब, इतना, service, ऐसे
5   customer  customer_ask_question             —           —             काम, टाइम, फ्लो, चलता
6   agent     agent_reassure_trust              —           —             कॉल, लीड, call, सब्सक्राइब, काम
```

## Call LCS-HJV5 (transferred) — 21 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             —
1   customer  customer_acknowledge              —           —             आउट
2   agent     agent_other                       —           —             आउट, कंप्लेंट, कंसन
3   customer  customer_agree                    —           —             —
4   agent     agent_answer_query                —           —             आउट, कंप्लेंट, कंसन, कंट्रेक्ट, एंटी
5   customer  customer_other                    —           —             लीड्स, अन्य
6   agent     agent_ask_to_repeat               —           —             चेक, लीड, सब्सक्राइब, हेलो, डिटेल्स
7   customer  customer_report_done              —           —             सब्सक्राइब, लीड्स
8   agent     agent_clarify                     —           —             लीड्स, डीटेल्स, फेस, अल्ली
9   customer  customer_greet                    —           —             रीसेंट, एक्जांपल
10  agent     agent_answer_query                —           —             लीड्स, कारण, फेस, अल्ली, लाइंग
11  customer  customer_report_link_opened       —           —             ओपन
12  agent     agent_answer_query                —           —             फिल्टर
13  customer  customer_express_distrust         —           —             मना, फिल्टर
14  agent     agent_answer_query                —           —             फिल्टर, अधि, अनेदी, सोर्स
15  customer  customer_acknowledge              —           —             ओपन, देते, जरूर, सोर्स
16  agent     agent_answer_query                —           —             बिजनेस, यूज़, फोटोस, मात्रे, कार्ज
17  customer  customer_skip_udyam               —           —             अधिक
18  agent     agent_answer_query                —           —             कॉल, सेंटर, सेर
19  customer  customer_other                    —           —             वेरे, अदि
20  agent     agent_transfer_to_rm              —           transfer_to_rmकॉल, सब्सक्राइब, सर्विस, रेटिंग, feedback
```

## Call LCS-IM39 (incomplete) — 2 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_query_fee                —           —             दिये, रखते
1   agent     agent_answer_query                —           —             call, inquiry, मिल, request, number
```

## Call LCS-IPR5 (transferred) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_wait                        —           —             लाइन, जस्टाइल, पाने, डॉटकाम
1   customer  customer_ask_question             —           —             यार, पाने, वाल
2   agent     agent_answer_query                —           —             वीडियो
3   customer  customer_express_distrust         —           —             लेट
4   agent     agent_acknowledge                 —           —             पेंडिंग, इन्हों, सिस्टम
5   customer  customer_ask_question             —           —             सिस्टम
6   agent     agent_other                       —           —             पेंडिंग
7   customer  customer_ask_question             —           —             पेंडिंग
8   agent     agent_wait                        —           —             पेंडिंग
9   customer  customer_acknowledge              —           —             पढ़ता, पूर्ण
10  agent     agent_other                       —           —             —
11  customer  customer_other                    —           —             कंपनी, पूर्ट
12  agent     agent_wait                        —           —             कॉल, टाइम, टीम, ऑप्शन, अपडेट
13  customer  customer_other                    —           —             लगता, एक्शन, लाओ, पूछे
14  agent     agent_other                       —           —             टीम, kyc, प्रूफ, लाँ
15  customer  customer_other                    —           —             टीम, kyc, पूछे
16  agent     agent_transfer_to_rm              —           transfer_to_rmनंबर, उन्होंने, नानी, इन्होंना
17  customer  customer_agree                    —           —             उन्होंने
18  agent     agent_transfer_to_rm              —           transfer_to_rmउन्होंने, नानी
```

## Call LCS-NO12 (raised_request) — 13 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, इश्यू, रेट, अरेंज, कंट्राक्ट
1   customer  customer_other                    —           —             रेट
2   agent     agent_acknowledge                 —           —             लाइन
3   customer  customer_acknowledge              —           —             चेक
4   agent     agent_present_offer               —           —             check, contract, issue, lease, less
5   customer  customer_acknowledge              —           —             —
6   agent     agent_explain_fee                 —           —             lead, category, feedback, concern, check
7   customer  customer_other                    —           —             issue, changes
8   agent     agent_acknowledge                 —           —             —
9   customer  customer_request_wait             —           —             —
10  agent     agent_acknowledge                 —           —             प्रॉपर, मिलेगा, रिस्पॉंस, अलावा, अभी।
11  customer  customer_acknowledge              —           —             अलावा
12  agent     agent_other                       —           —             call, कस्टमर, टीम, सपोर्ट, thank
```

## Call LCS-O0TD (incomplete) — 1 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_disclose_recording          —           —             कॉल, काम, customer, कस्टमर, बोलते
```

## Call LCS-RDCG (raised_request) — 2 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_report_address_error     —           —             error
1   agent     agent_wait                        —           —             कॉल, चेक, लाइन, thank, category
```

## Call LCS-XPYP (raised_request) — 25 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_ask_question             —           —             —
1   agent     agent_other                       —           —             पूरा, महीने, साल, बाती
2   customer  customer_agree                    —           —             —
3   agent     agent_send_sms_link               —           —             रिक्वेस्ट
4   customer  customer_acknowledge              —           —             —
5   agent     agent_ask_to_repeat               —           —             —
6   customer  customer_acknowledge              —           —             मैडम
7   agent     agent_other                       —           —             अच्छी, महीने, महीना
8   customer  customer_other                    —           —             उसने, असर
9   agent     agent_answer_query                —           —             इंकॉरी
10  customer  customer_acknowledge              —           —             लीड, काम, हूँ।, ओके।, इन्हां
11  agent     agent_answer_query                —           —             इंक्वारी, महीने
12  customer  customer_other                    —           —             काम, प्रॉब्लम, करवाती
13  agent     agent_answer_query                —           —             पैसा, इंक्वारी, सिस्टम, रुपया, बनता
14  customer  customer_express_distrust         —           —             —
15  agent     agent_answer_query                —           —             टाइम, पैसा, जैस, जवाब, बैंक
16  customer  customer_provide_org_name         —           —             —
17  agent     agent_answer_query                —           —             काम, सर्विस, बंद, देने, बिल्कुल
18  customer  customer_acknowledge              —           —             काम
19  agent     agent_answer_query                —           —             पूरा, साल
20  customer  customer_other                    —           —             —
21  agent     agent_other                       —           —             —
22  customer  customer_other                    —           —             चीज़े
23  agent     agent_answer_query                —           —             टाइम, फोन, देखा, रोज, रखो
24  customer  customer_request_wait             —           —             चीज़े
```

## Call LCS-Y48Z (completed) — 19 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             hello, customer, service, good, help
1   customer  customer_ask_question             —           —             help, how, tell
2   agent     agent_answer_query                —           —             लीज, mobile, register
3   customer  customer_ask_question             —           —             —
4   agent     agent_send_sms_link               —           —             —
5   customer  customer_query_fee                —           —             number
6   agent     agent_ask_to_repeat               —           —             call, second
7   customer  customer_query_fee                —           —             —
8   agent     agent_explain_fee                 —           —             808080
9   customer  customer_respond_udyam            —           —             बिजनेस
10  agent     agent_other                       —           —             लीड, लेके
11  customer  customer_ask_question             —           —             लीड
12  agent     agent_wait                        —           —             लीड, लास्ट, लीज, पॉइंट, मिली
13  customer  customer_acknowledge              —           —             —
14  agent     agent_answer_query                —           —             चेक, देख, किसने
15  customer  customer_acknowledge              —           —             कॉल
16  agent     agent_end_call                    —           —             रॉम
17  customer  customer_acknowledge              —           —             —
18  agent     agent_acknowledge                 —           —             कॉल, प्रॉब्लम, रेटिंग, मिल, थैंक
```
