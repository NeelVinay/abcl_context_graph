# Per-turn intent capture

Every turn of every call — who spoke, the intent, sentiment, tool/API call, and the signal keywords.

## Call 0139490a (transferred) — 28 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
5   customer  customer_agree                    —           —             बोलिए
6   customer  customer_request_wait             —           —             काम, इधर, work
7   agent     agent_wait                        —           —             मदद, आगे, समझ, दिक्कत, लिए।
8   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
9   customer  customer_agree                    —           —             —
10  agent     agent_confirm                     —           —             apply, हूँ।, आगे, तैयार, guide
11  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
12  customer  customer_acknowledge              —           —             बोलने, पढ़ते
13  agent     agent_send_sms_link               —           send_sms      sms, लिंक भेज, हूँ।, मदद, application
14  customer  customer_agree                    —           —             देखते, रहो
15  agent     agent_send_sms_link               —           send_sms      sms, apply, करें।, कृपया, रखें
16  customer  customer_report_sms_received      —           —             —
17  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
18  customer  customer_report_sms_received      —           —             message, whatsapp, दूसरा
19  agent     agent_reassure_trust              —           —             sms, कृपया, तरफ, आगे, capital
20  agent     agent_send_sms_link               —           send_sms      sms, हूँ।, कृपया, रखें, भेज
21  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, रखें, भेज
22  customer  customer_report_sms_received      —           —             message
23  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
24  customer  customer_request_wait             —           —             minute, open
25  agent     agent_wait                        —           —             मदद, लिंक, दिक्कत, लिए।, आराम
26  customer  customer_react_to_final_offer     —           —             loan, दिखा, उसमें, pay
27  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, offer, amount, हूँ।
```

## Call 01cef530 (transferred) — 60 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, approved
4   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms, भेज
7   customer  customer_ask_question             —           —             बोलिए
8   agent     agent_answer_query                —           —             बोल, हूँ।, तरफ, आदित्य, बिरला
9   customer  customer_agree                    —           —             बोलिए
10  agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, approved
11  customer  customer_agree                    —           —             बोलिए
12  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
13  customer  customer_express_distrust         —           —             process, complete, phone
14  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
15  customer  customer_react_to_final_offer     —           —             lakh, दिखा, two
16  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
17  customer  customer_other                    —           —             kyc, चुका
18  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, relationship, manager, connect
19  customer  customer_acknowledge              —           —             loan, application, check, देर, दिखा
20  agent     agent_other                       —           —             call, relationship, manager, दूँ, नहीं।
21  customer  customer_other                    —           —             करिए
22  agent     agent_acknowledge                 —           —             करें।, process, complete, चाहें
23  customer  customer_report_done              —           —             कर दिया, complete
24  agent     agent_confirm                     —           —             मदद, application, आगे, चाहेंगे, पूछना
25  customer  customer_acknowledge              —           —             process, kyc, complete, पूरा, review
26  customer  customer_acknowledge              —           —             loan, application, check, लाख, देर
27  agent     agent_inform_manual_review        —           push_to_crm   application, process, check, सही, देर
28  customer  customer_ask_question             —           —             —
29  agent     agent_acknowledge                 —           —             मदद, बताइए।
30  customer  customer_express_distrust         —           —             person, real
31  agent     agent_answer_query                —           —             बोल, हूँ।, तरफ, capital, aditya
32  customer  customer_ask_question             —           —             air
33  agent     agent_answer_query                —           —             बोल, हूँ।, तरफ, capital, aditya
34  customer  customer_ask_question             —           —             person, real
35  agent     agent_answer_query                —           —             बोल, हूँ।, तरफ, capital, aditya
36  customer  customer_ask_question             —           —             bot
37  agent     agent_answer_query                —           —             बोल, हूँ।, तरफ, capital, aditya
38  customer  customer_ask_question             —           —             —
39  agent     agent_answer_query                —           —             —
40  customer  customer_ask_question             frustrated  —             कब तक, application, review, under
41  agent     agent_answer_query                —           —             application, process, complete, मिल, review
42  customer  customer_unclear                  —           —             —
43  customer  customer_other                    —           —             normal
44  agent     agent_inform_manual_review        —           push_to_crm   application, process, complete, इंतज़ार, जाएगा।
45  customer  customer_ask_question             —           —             मिल, minute, पाएंगे, पांच, अंदर
46  agent     agent_answer_query                —           —             call, हूँ।, application, process, समय
47  customer  customer_acknowledge              —           —             loan, application, process, पूरा, पता
48  agent     agent_answer_query                —           —             loan, कृपया, process, समझ, ज़रूरी
49  customer  customer_ask_question             —           —             —
50  agent     agent_answer_query                —           —             बोल, हूँ।, तरफ, capital, aditya
51  customer  customer_express_distrust         —           —             बोल, पता, computer, झूठ
52  agent     agent_transfer_to_rm              —           transfer_to_rmहूँ।, connect, समझ, बिल्कुल, chd
53  customer  customer_ask_question             —           —             —
54  agent     agent_answer_query                —           —             बोल, हूँ।, तरफ, capital, aditya
55  customer  customer_express_distrust         —           —             पता, चुका, computer
56  agent     agent_transfer_to_rm              —           transfer_to_rmहूँ।, समझ, बिल्कुल, खेद, inconvenience
57  customer  customer_acknowledge              —           —             —
58  agent     agent_acknowledge                 —           —             —
59  customer  customer_acknowledge              —           —             —
```

## Call 072e5c6d (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलो
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, करें।, link, click
6   customer  customer_report_link_opened       —           —             click
7   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
8   customer  customer_report_done              —           —             click
9   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
10  customer  customer_report_done              —           —             लिख
11  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
12  agent     agent_request_otp                 —           —             otp, verify
13  customer  customer_report_done              —           —             कर दिया
14  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
15  agent     agent_ask_to_repeat               —           —             फिर से बता, कीजिए, माफ़
16  customer  customer_report_done              —           —             हो गया
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_address             —           —             address, pincode, locality, building, house number
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
24  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
25  customer  customer_state_employment_type    —           —             self employ, self, employed
26  agent     agent_request_income              —           —             income, fill, monthly, self, net
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_org_name            —           —             बताएं।, जाए, enter, registered, business
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, address
31  customer  customer_report_done              —           —             right
32  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
33  customer  customer_skip_udyam               —           —             number, एकदम
34  agent     agent_offer_skip_udyam            —           —             skip, number, बताएं।, जाए, click
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
37  customer  customer_report_done              —           —             हो गया
38  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, करें।
39  customer  customer_react_to_final_offer     —           —             see
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, now, process, relationship, manager
41  customer  customer_other                    —           —             —
```

## Call 07ea36d9 (transferred) — 71 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_ask_question             —           —             —
3   agent     agent_greet                       —           —             बोल, aditya, birla
4   customer  customer_other                    —           —             one, six, zero
5   agent     agent_acknowledge                 —           —             सवाल
6   customer  customer_request_wait             —           —             एक second, second
7   agent     agent_wait                        —           —             कृपया, इंतज़ार, बताएं, तैयार, हों।
8   customer  customer_agree                    —           —             बोलिए
9   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
10  customer  customer_agree                    —           —             बोलिए
11  customer  customer_query_fee                —           —             interest rate, interest, rate, कितना
12  agent     agent_answer_query                —           —             loan, offer, approved, amount, final
13  customer  customer_agree                    —           —             आगे बढ़, आगे, पूरा, लेंगे, procedure
14  customer  customer_express_distrust         —           —             loan, पड़ेगा, तरफ़
15  agent     agent_reassure_trust              —           —             sms, हूँ।, मदद, application, शुरू
16  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
17  agent     agent_send_sms_link               —           send_sms      sms, कृपया, application, रखें, जिसमें
18  agent     agent_send_sms_link               —           send_sms      sms, कृपया, भेज, फोन
19  agent     agent_guide_open_link             —           —             खुल गया, sms, कृपया, link, बताएं
20  customer  customer_report_link_opened       —           —             खुल गया, खुल
21  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
22  customer  customer_report_applied           —           —             click, login
23  agent     agent_request_otp                 —           —             कृपया, number, mobile, बताएं, सही
24  customer  customer_acknowledge              —           —             उसी
25  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
26  customer  customer_do_otp                   —           —             otp, verification
27  agent     agent_clarify                     —           —             कृपया, आगे, बताएं, होगा।, खुल
28  customer  customer_report_link_opened       —           —             खुल गया, खुल
29  agent     agent_request_pan                 —           —             पैन, कृपया, देख, personal, details
30  customer  customer_provide_pan              —           —             pan, number, second
31  agent     agent_wait                        —           —             कृपया, इंतज़ार, आगे, बताएं, तैयार
32  agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, कहेंगे
33  customer  customer_report_done              —           —             details, fill
34  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, कृपया
35  agent     agent_ask_to_repeat               —           —             कृपया, कहेंगे, स्पष्ट
36  customer  customer_report_done              —           —             details, clear
37  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
38  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
39  customer  customer_request_wait             —           —             second, just
40  agent     agent_request_email               —           —             email, कृपया, address, बताएं, पूरा
41  agent     agent_request_address             —           —             address, locality, building, house number, flat
42  customer  customer_report_done              —           —             हो गया, आगे, procedure
43  agent     agent_wait                        —           —             इंतज़ार, आगे, address, समझ, ताकि
44  customer  customer_provide_personal_details —           —             details, professional
45  agent     agent_answer_query                —           —             loan, offer, कृपया, page, बताएं।
46  customer  customer_ask_question             —           —             मतलब, details, उसमें, भरना, आधार
47  agent     agent_request_udyam               —           —             udyam, details, self, employment, salaried
48  customer  customer_state_employment_type    —           —             self employ, self, employed
49  agent     agent_offer_skip_udyam            —           —             skip, application, details, आगे, समझ
50  customer  customer_acknowledge              —           —             check, card, let, bank, याद
51  agent     agent_wait                        —           —             मदद, देख, आगे, बताएं, ताकि
52  agent     agent_request_udyam               —           —             udyam, करें।, कृपया, बताएं।, registered
53  agent     agent_request_udyam               —           —             udyam, करें।, कृपया, आगे, बताएं
54  customer  customer_request_wait             —           —             minute
55  agent     agent_wait                        —           —             कृपया, इंतज़ार, आगे, बताएं, पूरा
56  agent     agent_wait                        —           —             कृपया, इंतज़ार, बताएं, तैयार, हों।
57  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
58  customer  customer_other                    —           —             details, time, start, some, all
59  agent     agent_wait                        —           —             मदद, कृपया, समय, आगे, ताकि
60  customer  customer_acknowledge              —           —             —
61  agent     agent_request_org_name            —           —             कृपया, details, आगे, बताएं, पूरा
62  customer  customer_ask_question             —           —             wait, option
63  agent     agent_answer_query                —           —             हूँ।, मदद, शुरू, समय, कॉल
64  customer  customer_react_to_offer           —           —             —
65  customer  customer_react_to_offer           —           —             lakh, one, thousand
66  agent     agent_present_offer               —           —             amount, समझ, गई।
67  customer  customer_react_to_offer           —           —             loan, amount, मिल
68  agent     agent_present_final_offer         —           —             loan, offer, लाख, रुपये, आगे
69  agent     agent_present_final_offer         —           —             loan, offer, amount, देख, पेज
70  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 08145c39 (transferred) — 56 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             बोलिए
5   agent     agent_present_offer               —           —             —
6   customer  customer_agree                    —           —             बोलिए
7   customer  customer_ask_question             —           —             detail, बोलते
8   agent     agent_answer_query                —           —             loan, amount, हूँ।, application, शुरू
9   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
10  customer  customer_agree                    —           —             पूरा, बोलिए
11  agent     agent_present_offer               —           —             loan, amount, हूँ।, application, शुरू
12  customer  customer_agree                    —           —             बराबर
13  customer  customer_agree                    —           —             correct
14  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
15  agent     agent_guide_open_link             —           —             sms, करें।, link, click
16  customer  customer_request_wait             —           —             wait
17  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
18  customer  customer_request_wait             —           —             wait, open
19  agent     agent_wait                        —           —             इंतज़ार
20  customer  customer_greet                    —           —             hello, बोलिए
21  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
22  customer  customer_ask_question             —           —             बोलिए, दिखा, इधर
23  agent     agent_answer_query                —           —             number, terms, mobile, check, conditions
24  customer  customer_report_applied           —           —             apply
25  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
26  customer  customer_ask_question             —           —             सिर्फ़
27  agent     agent_request_otp                 —           —             number, terms, mobile, conditions, enter
28  customer  customer_agree                    —           —             बोलिए
29  customer  customer_ask_question             —           —             mobile, option, किधर, डालूं
30  agent     agent_guide_open_link             —           —             sms, application, page, number, link
31  customer  customer_unclear                  —           —             —
32  agent     agent_guide_open_link             —           —             sms, करें।, नमस्ते, link, click
33  customer  customer_request_wait             —           —             minute, open
34  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, नीचे
35  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
36  customer  customer_request_wait             —           —             एक second, रुकिए, minute, second
37  agent     agent_wait                        —           —             इंतज़ार
38  customer  customer_ask_question             —           —             कौन सा, call, number, second
39  agent     agent_answer_query                —           —             बोल, हूँ।, तरफ, आदित्य, बिरला
40  customer  customer_ask_question             —           —             number, mobile, enter, option
41  agent     agent_request_otp                 —           —             number, mobile
42  customer  customer_greet                    —           —             hello
43  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
44  customer  customer_do_otp                   —           —             otp, number, डाल, भेजा, भेजो
45  agent     agent_request_otp                 —           send_otp      otp, कृपया, verify, भेज, बताएं।
46  customer  customer_do_otp                   —           —             otp, call, message
47  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, बताएं।
48  customer  customer_ask_question             —           —             call, कितनी
49  agent     agent_wait                        —           —             wait, हूँ।, otp, कृपया, समय
50  customer  customer_do_otp                   —           —             otp, होकर
51  agent     agent_request_otp                 —           —             otp, verify
52  customer  customer_report_done              —           —             हो गया
53  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
54  customer  customer_react_to_final_offer     —           —             देखेंगे
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 0aed797d (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   agent     agent_present_offer               —           —             तरफ, आदित्य, बिरला, कैपिटल
4   customer  customer_agree                    —           —             बोलिए
5   customer  customer_ask_question             —           —             मतलब, credit, पैसा
6   agent     agent_send_sms_link               —           send_sms      sms, offer, करें।, final, कृपया
7   customer  customer_agree                    —           —             भेज
8   agent     agent_guide_open_link             —           —             sms, करें।, link, click
9   agent     agent_ask_to_repeat               —           —             कृपया, कॉल
10  customer  customer_acknowledge              —           —             —
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
12  customer  customer_report_link_opened       —           —             link
13  agent     agent_guide_open_link             —           —             करें।, कृपया, link, check, बताएं
14  customer  customer_request_wait             —           —             minute
15  agent     agent_wait                        —           —             इंतज़ार
16  customer  customer_request_wait             —           —             minute
17  agent     agent_wait                        —           —             इंतज़ार
18  customer  customer_other                    —           —             connect
19  agent     agent_reassure_trust              —           —             हूँ।, process, समझ, continue, step
20  customer  customer_report_sms_received      —           —             भेज, connect, बोलिए, minute, one
21  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, application, process
22  agent     agent_guide_open_link             —           —             sms, link
23  customer  customer_report_sms_received      —           —             भेज
24  agent     agent_guide_open_link             —           —             sms, करें।, link, click
25  customer  customer_other                    —           —             बजे, दबा
26  agent     agent_other                       —           —             call, करें।, हूँ।, कृपया, देर
27  customer  customer_unclear                  —           —             —
28  agent     agent_greet                       —           —             नमस्ते, बोल
29  customer  customer_unclear                  —           —             —
30  agent     agent_greet                       —           —             नमस्ते
31  customer  customer_greet                    —           —             hello, आवाज़
32  agent     agent_ask_to_repeat               —           —             बोल, आदित्य, बिरला, कैपिटल, से।
33  customer  customer_unclear                  —           —             बोल
34  agent     agent_ask_to_repeat               —           —             हूँ।, मदद, कृपया, सुन
35  customer  customer_report_link_opened       —           —             loan, number, link, mobile, personal
36  agent     agent_request_otp                 —           —             करें।, number, mobile, आगे, enter
37  customer  customer_do_otp                   —           —             otp, entry
38  agent     agent_request_otp                 —           —             verify, बढ़िया
39  customer  customer_do_otp                   —           —             verify
40  agent     agent_acknowledge                 —           —             अच्छा।
41  customer  customer_react_to_final_offer     —           —             lakh, one, thousand, five, पंद्रह
42  customer  customer_query_fee                —           —             interest, rate, point, दिखा, two
43  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, offer, करें।, final, कृपया
44  customer  customer_acknowledge              —           —             —
```

## Call 0d1b55e2 (transferred) — 51 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             sorry, again, say
1   customer  customer_greet                    —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
3   customer  customer_agree                    —           —             बोलिए
4   customer  customer_agree                    —           —             बोलिए
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
6   agent     agent_guide_open_link             —           —             sms, करें।, link, click
7   customer  customer_report_link_opened       —           —             —
8   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
9   customer  customer_request_wait             —           —             minute
10  agent     agent_wait                        —           —             इंतज़ार
11  customer  customer_agree                    —           —             —
12  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
13  customer  customer_ask_question             —           —             loan, amount, मिल, कितना
14  agent     agent_answer_query                —           —             loan, offer, approved, pre, amount
15  customer  customer_ask_question             —           —             loan, मिल, मिलेगा, उससे
16  agent     agent_answer_query                —           —             loan, amount, करें।, हूँ।, कृपया
17  customer  customer_ask_question             —           —             loan, offer, limit, maximum
18  agent     agent_answer_query                —           —             loan, offer, approved, pre, करें।
19  customer  customer_ask_question             —           —             —
20  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
21  customer  customer_do_otp                   —           —             —
22  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
23  customer  customer_report_done              —           —             हो गया, कर दिया, page, details, आगे
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
27  customer  customer_report_done              —           —             कर दिया
28  agent     agent_request_address             —           —             address, pincode, locality, building, house number
29  customer  customer_report_done              —           —             कर दिया
30  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
33  agent     agent_ask_to_repeat               —           —             साफ़ बोल, कीजिए, माफ़, साफ़, बोलिएगा
34  customer  customer_state_employment_type    —           —             salaried
35  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
36  customer  customer_state_employment_type    —           —             salaried, भाई
37  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
38  customer  customer_acknowledge              —           —             —
39  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
40  customer  customer_ask_question             —           —             —
41  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_request_business_details    —           —             address, fill, organization, fields, दिखाया
44  customer  customer_report_done              —           —             कर दिया, भाई
45  agent     agent_request_terms_accept        —           —             करें।, details, button, proceed, click
46  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
47  customer  customer_report_done              —           —             कर दिया
48  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
49  customer  customer_react_to_final_offer     —           —             देख
50  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 12913998 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
6   agent     agent_guide_open_link             —           —             sms, करें।, link, click
7   customer  customer_report_done              —           —             कर दिया
8   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, otp
9   customer  customer_report_done              —           —             हो गया
10  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
11  customer  customer_report_done              —           —             हो गया
12  agent     agent_request_personal_details    —           —             कृपया, personal, details, fill, बताएं
13  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
14  customer  customer_report_done              —           —             हो गया
15  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
16  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_address             —           —             address, pincode, locality, building, house number
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
26  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
27  customer  customer_state_employment_type    —           —             self employ, self, employed
28  agent     agent_request_income              —           —             income, बताएं।, जाए, fill, monthly
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, registered
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_business_details    —           —             business, जाए, enter, address, fill
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
35  customer  customer_skip_udyam               —           —             —
36  agent     agent_offer_skip_udyam            —           —             skip, करें।, कृपया, application, number
37  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, कहेंगे, दोबारा
38  customer  customer_request_wait             —           —             wait, waiting
39  agent     agent_acknowledge                 —           —             हूँ।, तरीके, simple, ज़रूर
40  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
41  customer  customer_react_to_final_offer     —           —             loan, option
42  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
43  customer  customer_react_to_final_offer     —           —             देख, दिख, emi
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 133230ad (transferred) — 24 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
4   agent     agent_guide_open_link             —           —             sms, करें।, link, click
5   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
6   customer  customer_other                    —           —             बोलते
7   agent     agent_other                       —           —             करें।, link, check, try, internet
8   customer  customer_acknowledge              —           —             call
9   agent     agent_guide_open_link             —           —             खुल गया, link, खुल, try
10  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
11  customer  customer_other                    —           —             —
12  agent     agent_guide_open_link             —           —             sms, करें।, हूँ।, link, click
13  customer  customer_do_otp                   —           —             otp
14  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
15  agent     agent_request_otp                 —           —             otp, loan, offer, कृपया, verify
16  customer  customer_do_otp                   —           —             otp
17  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, जाएगा।
18  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, बताएं।
19  agent     agent_ask_to_repeat               —           —             कृपया, कहेंगे, थोड़ा, दोबारा
20  customer  customer_acknowledge              —           —             line
21  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
22  customer  customer_react_to_final_offer     —           —             देखा
23  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 16a9075f (transferred) — 22 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोल
3   customer  customer_other                    —           —             apply, आगे, चुका, resume, journey
4   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
5   customer  customer_agree                    —           —             शुरू कर, शुरू, करिए
6   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  customer  customer_report_done              —           —             कर दिया, click
11  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
12  customer  customer_do_otp                   —           —             number, mobile
13  agent     agent_request_otp                 —           send_otp      otp, करें।, get, terms, check
14  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
15  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
16  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
17  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, भेज, बताएं।
18  customer  customer_do_otp                   —           —             verify
19  customer  customer_provide_personal_details —           —             number, mobile, enter, name, full
20  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
21  customer  customer_ask_question             —           —             —
```

## Call 190be58f (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, आपसे
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             बोलिए
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
7   customer  customer_react_to_offer           —           —             offer, कितने, preapproved
8   customer  customer_greet                    —           —             hello
9   agent     agent_present_offer               —           —             loan, offer, sms, amount, करें।
10  customer  customer_acknowledge              —           —             —
11  agent     agent_guide_open_link             —           —             loan, offer, sms, देख, link
12  customer  customer_acknowledge              —           —             check
13  agent     agent_guide_open_link             —           —             खुल गया, sms, कृपया, page, link
14  agent     agent_guide_open_link             —           —             sms, link, खोल, पाए
15  customer  customer_acknowledge              —           —             देख
16  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
17  customer  customer_other                    —           —             loan, link
18  agent     agent_answer_query                —           —             —
19  customer  customer_other                    —           —             बोलो, भाई, सबको
20  agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, कृपया, भेज
21  customer  customer_report_sms_received      —           —             मिला
22  agent     agent_guide_open_link             —           —             sms, करें।, link, click
23  customer  customer_report_link_opened       frustrated  —             नहीं हो, link, wait, open, second
24  agent     agent_guide_open_link             —           —             apply, करें।, now, कृपया, देख
25  customer  customer_other                    —           —             issue, महीने, network
26  agent     agent_other                       —           —             sms, link, जाए, आगे, समझ
27  customer  customer_ask_question             —           —             wait, पता, चलेगा, कैसा
28  agent     agent_wait                        —           —             इंतज़ार
29  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
30  customer  customer_request_wait             —           —             wait, something, patience
31  agent     agent_wait                        —           —             wait, sure, waiting
32  customer  customer_ask_question             —           —             पढ़ते
33  agent     agent_wait                        —           —             तैयार, हों, आराम, बताइए।, रहिए।
34  customer  customer_report_link_opened       —           —             link, open
35  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
36  customer  customer_react_to_offer           —           —             loan offer, loan, offer, लाख, मिल
37  agent     agent_present_offer               —           —             loan offer, loan, offer, amount, कृपया
38  customer  customer_report_applied           —           —             apply now, apply, now, click
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
40  customer  customer_ask_question             —           —             what
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 1d8b48d4 (transferred) — 48 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलो
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, link
6   customer  customer_agree                    —           —             भेजो
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
9   customer  customer_report_sms_received      —           —             message, कहीं
10  agent     agent_other                       —           —             करें।, link, check, try, internet
11  customer  customer_acknowledge              —           —             —
12  agent     agent_guide_open_link             —           —             कृपया, link, आगे, open, बढ़ें।
13  customer  customer_other                    —           —             call, phone, simple, अरे
14  agent     agent_greet                       —           —             बोल, हूँ।, तरफ, capital, aditya
15  customer  customer_request_wait             —           —             minute, बोलो, खोल, रुको
16  agent     agent_wait                        —           —             इंतज़ार
17  customer  customer_acknowledge              —           —             —
18  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
19  customer  customer_acknowledge              —           —             —
20  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
21  customer  customer_request_wait             —           —             minute, रुको
22  agent     agent_wait                        —           —             इंतज़ार
23  customer  customer_do_otp                   —           —             otp, phone
24  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, बताएं।
25  customer  customer_request_wait             —           —             wait
26  agent     agent_request_otp                 —           —             otp, मिल
27  customer  customer_do_otp                   —           —             मिला
28  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
29  customer  customer_acknowledge              —           —             —
30  agent     agent_request_otp                 —           —             otp, मिल
31  customer  customer_do_otp                   —           —             मिला, exactly
32  agent     agent_wait                        —           —             wait, हूँ।, otp, कृपया, जाएगा।
33  customer  customer_report_link_opened       —           —             खुल गया, खुल
34  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
35  agent     agent_request_address             —           —             मदद, fill, form, चाहिए।, रहें।
36  customer  customer_other                    —           —             —
37  agent     agent_wait                        —           —             कृपया, बताएं।, complete, जाए, fill
38  customer  customer_acknowledge              —           —             खोलता
39  agent     agent_guide_open_link             —           —             sms, करें।, link, click
40  customer  customer_report_done              —           —             कर दिया
41  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
42  customer  customer_agree                    —           —             —
43  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
44  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
45  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
46  customer  customer_report_done              —           —             हो गया
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 1dfb93a4 (transferred) — 49 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             sorry, again, say
1   customer  customer_greet                    —           —             hello, बोलो
2   agent     agent_greet                       —           —             बोल, capital, aditya, birla, समझ
3   customer  customer_agree                    —           —             बोलो
4   customer  customer_other                    —           —             detail
5   agent     agent_present_offer               —           —             loan offer, personal loan, ₹200000, 200000, loan
6   customer  customer_agree                    —           —             भेजो
7   agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, जिसमें, भेज
8   agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, भेज, मिल
9   customer  customer_report_sms_received      —           —             —
10  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
11  agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, कीजिए, माफ़, कहेंगे
12  customer  customer_report_link_opened       —           —             खुल गया, link, खुल
13  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, मदद
14  customer  customer_do_otp                   —           —             number, mobile, डालो
15  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, नीचे, बताएं।
16  customer  customer_other                    —           —             आगे, मांग, line, detail, total
17  agent     agent_request_pan                 —           —             पैन, कृपया, बताएं, समझ, पूरा
18  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
19  customer  customer_greet                    —           —             hello, detail
20  agent     agent_request_pan                 —           —             पैन, बताएं, नंबर, भरने, अगला
21  customer  customer_provide_pan              —           —             pan, number, डाल
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, कृपया
23  customer  customer_report_done              —           —             भर दिया
24  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
25  customer  customer_acknowledge              —           —             डाला
26  agent     agent_request_address             —           —             address, कृपया, बताएं।, सही, पूरा
27  agent     agent_request_address             —           —             address, शुक्रिया
28  customer  customer_report_done              —           —             डाल
29  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, conditions, proceed
30  agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, माफ़, कहेंगे
31  customer  customer_ask_question             —           —             process, आगे
32  agent     agent_ask_employment_type         —           —             salaried, self-employ, details, self, employment
33  customer  customer_state_employment_type    —           —             self employ, self employee, self, employee
34  agent     agent_request_income              —           —             income, amount, कृपया, बताएं।, monthly
35  customer  customer_report_done              —           —             डाल, what
36  agent     agent_request_org_name            —           —             कृपया, बताएं।, पूरा, business, टाइप
37  customer  customer_report_done              —           —             detail, डालता
38  agent     agent_request_business_details    —           —             business, कृपया, बताएं।, इंतज़ार, address
39  customer  customer_report_done              —           —             डाल
40  agent     agent_request_business_details    —           —             business, कृपया, सही, दिख, बढ़िया
41  customer  customer_report_done              —           —             हो गया, कर दिया
42  agent     agent_acknowledge                 —           —             कृपया
43  customer  customer_request_wait             —           —             wait
44  agent     agent_wait                        —           —             loan, offer, मदद, कृपया, process
45  customer  customer_acknowledge              —           —             चालू
46  agent     agent_present_final_offer         —           —             loan, offer, amount, final, देख
47  customer  customer_react_to_final_offer     —           —             देख
48  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, कृपया, process, relationship
```

## Call 1ea57f23 (transferred) — 71 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             बोलिए
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_greet                    —           —             बात कर रही, से बात, बोलो
5   agent     agent_greet                       —           —             बात कर रही, से बात, हूँ।, चाहती, माफ़ी
6   agent     agent_greet                       —           —             बोल, बिल्कुल
7   customer  customer_agree                    —           —             बोलिए
8   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
9   agent     agent_disclose_recording          —           —             record, training, quality, call, तरफ
10  customer  customer_ask_question             —           —             पड़ेगा
11  agent     agent_send_sms_link               —           send_sms      sms, application, process, जिसमें, भेज
12  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
13  customer  customer_report_sms_received      —           —             sms, भेज
14  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, रखें, जिसमें
15  agent     agent_send_sms_link               —           —             कृपया, फोन
16  customer  customer_report_sms_received      —           —             sms, मिल
17  agent     agent_guide_open_link             —           —             कृपया, बढ़िया, जी।
18  customer  customer_report_sms_received      —           —             sms, मिल
19  agent     agent_guide_open_link             —           —             खुल गया, sms, कृपया, link, बताएं
20  customer  customer_report_link_opened       —           —             खुल गया, link, खुल
21  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
22  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, screen
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
25  customer  customer_provide_pan              —           —             pan, डाल, card, दूं, return
26  agent     agent_request_otp                 —           —             otp, कृपया, verify, screen, आगे
27  customer  customer_report_done              —           —             आगे
28  agent     agent_request_pan                 —           —             पैन, complete, personal, details, सबसे
29  customer  customer_acknowledge              —           —             —
30  agent     agent_request_pan                 —           —             पैन, complete, बताएं, नंबर, जाए।
31  agent     agent_ask_to_repeat               —           —             फिर से कह, माफ़, कहेंगे
32  customer  customer_provide_personal_details —           —             detail
33  agent     agent_request_pan                 —           —             पैन, आगे, बताएं, ताकि, सकें।
34  agent     agent_confirm                     —           —             आगे बढ़, हूँ।, complete, details, आगे
35  customer  customer_other                    —           —             ten, free
36  agent     agent_other                       —           —             call, perfect, सुबह, बजे, schedule
37  customer  customer_greet                    —           —             hello
38  agent     agent_wait                        —           —             इंतज़ार
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_pan                 —           —             पैन, कृपया, personal, details, नंबर
41  customer  customer_state_employment_type    —           —             professional, चुका
42  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, page, details
43  customer  customer_state_employment_type    —           —             self employ, self, employed
44  agent     agent_request_income              —           —             income, कृपया, complete, monthly, net
45  agent     agent_request_org_name            —           —             कृपया, बताएं, पूरा, बढ़िया, जाए।
46  agent     agent_wait                        —           —             loan, offer, मदद, कृपया, fetch
47  customer  customer_agree                    —           —             proceed, दूं
48  agent     agent_confirm                     —           —             proceed, पूरा, बिल्कुल, जी।, दें।
49  customer  customer_acknowledge              —           —             —
50  agent     agent_acknowledge                 —           —             जी।
51  customer  customer_respond_udyam            —           —             उद्यम
52  agent     agent_request_udyam               —           —             उद्यम, page, नीचे, registered, होगा।
53  customer  customer_respond_udyam            —           —             उद्यम
54  agent     agent_offer_skip_udyam            —           —             skip, नंबर, क्लिक, पेज, उद्यम
55  customer  customer_respond_udyam            —           —             —
56  agent     agent_request_udyam               —           —             उद्यम, करें।, कृपया, बताएं।, registered
57  customer  customer_acknowledge              —           —             —
58  agent     agent_request_udyam               —           —             उद्यम, मदद, कृपया, आगे, बताएं
59  agent     agent_request_otp                 —           send_otp      otp, कृपया, verify, registered, बताएं
60  customer  customer_acknowledge              —           —             —
61  agent     agent_wait                        —           —             इंतज़ार
62  customer  customer_ask_question             —           —             number, डाल, उद्यम, पड़ेगा, दूं
63  agent     agent_request_udyam               —           —             उद्यम, कृपया, page, बताएं, नंबर
64  customer  customer_acknowledge              —           —             —
65  agent     agent_request_udyam               —           —             कृपया, आगे, बताएं, ताकि, नंबर
66  agent     agent_request_otp                 —           send_otp      otp, कृपया, verify, complete, registered
67  agent     agent_wait                        —           —             loan, offer, मदद, कृपया, समय
68  agent     agent_wait                        —           —             loan, offer, कृपया, समय, fetch
69  agent     agent_present_final_offer         —           —             loan, offer, देख, धन्यवाद, पेज
70  agent     agent_present_final_offer         —           —             loan, amount, final, देख, page
```

## Call 1fb2c1fa (transferred) — 68 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             बोलिए
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             बोल
5   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
6   customer  customer_agree                    —           —             —
7   customer  customer_query_fee                —           —             interest, कितना, महीना
8   agent     agent_answer_query                —           —             loan, offer, sms, approved, amount
9   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
10  customer  customer_greet                    —           —             hello
11  agent     agent_send_sms_link               —           —             sms, हूँ।, मदद, कृपया, आगे
12  customer  customer_report_applied           —           —             apply now, apply, now
13  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गया, लिंक पर क्लिक, apply, sms
14  customer  customer_report_link_opened       —           —             खुल गया, खुल, open
15  agent     agent_guide_apply                 —           —             नीचे, बढ़िया
16  customer  customer_greet                    —           —             hello, बोलिए
17  agent     agent_guide_apply                 —           —             apply now, apply, now, लिंक, पेज
18  customer  customer_do_otp                   —           —             two, three, six, zero
19  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, नीचे, get
20  customer  customer_do_otp                   —           —             verify, lakh, two, congratulations
21  agent     agent_request_pan                 —           —             पैन, personal, details, सबसे, बताएं
22  customer  customer_acknowledge              —           —             —
23  agent     agent_request_personal_details    —           —             कृपया, बताएं।, पैन, पूरा, अनुसार
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
26  customer  customer_report_done              —           —             हो गया
27  agent     agent_request_address             —           —             कृपया, सही, पूरा, नंबर, भरने
28  customer  customer_report_done              —           —             हो गया, sun
29  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, देख, conditions
30  customer  customer_ask_question             —           —             मतलब, company
31  agent     agent_request_terms_accept        —           —             terms and condition, terms, conditions, आगे, सही
32  customer  customer_other                    —           —             बोल
33  agent     agent_confirm                     —           —             proceed, क्लिक, बढ़िया
34  customer  customer_provide_income           —           —             income, monthly
35  agent     agent_confirm                     —           —             proceed, बिल्कुल
36  customer  customer_ask_question             —           —             monthly, income, किधर
37  agent     agent_request_income              —           —             income, details, आगे, monthly, employment
38  customer  customer_request_wait             —           —             wait, लूंगा
39  agent     agent_wait                        —           —             इंतज़ार, आगे, बताएं, ताकि, बिल्कुल
40  customer  customer_ask_question             —           —             मतलब, organization
41  agent     agent_request_org_name            —           —             organization, हूँ।, मदद, business, टाइप
42  customer  customer_request_wait             —           —             wait
43  agent     agent_wait                        —           —             बताएं।, इंतज़ार, तैयार, हों
44  customer  customer_request_wait             —           —             wait, रुको
45  agent     agent_wait                        —           —             इंतज़ार, आगे, बताएं, ताकि, बढ़
46  customer  customer_acknowledge              —           —             साल
47  agent     agent_request_income              —           —             income, कृपया, monthly, तैयार, हों
48  customer  customer_request_wait             —           —             wait
49  agent     agent_wait                        —           —             मदद, इंतज़ार, बताएं, ताकि, तैयार
50  agent     agent_ask_to_repeat               —           —             फिर से कह, माफ़
51  customer  customer_request_wait             —           —             wait
52  agent     agent_wait                        —           —             बताएं।, इंतज़ार, तैयार, हों
53  customer  customer_request_wait             —           —             wait, साल
54  agent     agent_wait                        —           —             इंतज़ार, आगे, बताएं, ताकि, बढ़
55  customer  customer_request_wait             —           —             wait
56  agent     agent_wait                        —           —             इंतज़ार
57  customer  customer_request_wait             —           —             wait, call
58  agent     agent_wait                        —           —             बताएं।, इंतज़ार, तैयार, हों
59  customer  customer_acknowledge              —           —             —
60  agent     agent_request_income              —           —             income, कृपया, जाए, आगे, monthly
61  customer  customer_report_done              —           —             हो गया
62  agent     agent_acknowledge                 —           —             —
63  customer  customer_request_wait             —           —             wait, facing
64  agent     agent_acknowledge                 —           —             समझती
65  customer  customer_request_wait             —           —             wait, offer, button, app, close
66  agent     agent_wait                        —           —             offer, मदद, कृपया, रखें, सही
67  customer  customer_react_to_final_offer     —           —             loan, amount, lakh, दिखा, two
```

## Call 2352c059 (transferred) — 79 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_greet                    —           —             से बात
5   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
6   customer  customer_other                    —           —             उसको
7   agent     agent_greet                       —           —             बोल, capital, aditya, birla, समझ
8   customer  customer_other                    —           —             —
9   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
10  customer  customer_agree                    —           —             देर, जानकारी, शुक्रिया, लेने, मुझसे
11  agent     agent_ask_to_repeat               —           —             माफ़
12  customer  customer_agree                    —           —             शुरू कर, शुरू, चलिए
13  agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, कृपया, application
14  agent     agent_send_sms_link               —           —             नंबर
15  customer  customer_acknowledge              —           —             —
16  agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
17  customer  customer_report_sms_received      —           —             sms, देख, मिल
18  customer  customer_report_sms_received      —           —             देख, message
19  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, खुल
20  customer  customer_express_distrust         —           —             link, कहीं, scan
21  agent     agent_reassure_trust              —           —             sms, कृपया, capital, बताएं, aditya
22  customer  customer_report_link_opened       —           —             खोल
23  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, नीचे
24  customer  customer_do_otp                   —           —             number, mobile, मांग, मुझसे
25  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
26  customer  customer_request_wait             —           —             रुकिए, check
27  agent     agent_wait                        —           —             इंतज़ार, आगे, बताएं, ताकि, बढ़
28  customer  customer_express_distrust         —           —             इंतज़ार
29  agent     agent_reassure_trust              —           —             हूँ।, मदद, otp, कृपया, आगे
30  customer  customer_express_distrust         —           —             —
31  agent     agent_reassure_trust              —           —             हूँ।, मदद, otp, कृपया, आगे
32  customer  customer_express_distrust         —           —             —
33  agent     agent_reassure_trust              —           —             हूँ।, मदद, otp, कृपया, आगे
34  customer  customer_do_otp                   —           —             otp, मिल
35  agent     agent_request_otp                 —           —             otp, कृपया, verify, जाए, आगे
36  customer  customer_do_otp                   —           —             otp, verified
37  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, self, employment
38  customer  customer_state_employment_type    —           —             self employ, self, employed
39  agent     agent_request_business_details    —           —             business, कृपया, details, proceed, address
40  customer  customer_ask_question             —           —             personal, professional, select, option
41  agent     agent_answer_query                —           —             कृपया, personal, details, आगे, professional
42  customer  customer_ask_question             —           —             इंतज़ार, submit, form
43  agent     agent_wait                        —           —             हूँ।, कृपया, इंतज़ार, आगे, बताएं
44  customer  customer_agree                    —           —             ज़रूर
45  agent     agent_wait                        —           —             मदद, आगे, बताएं, ताकि, सकें।
46  customer  customer_acknowledge              —           —             —
47  agent     agent_clarify                     —           —             submit, form
48  customer  customer_state_employment_type    —           —             personal, income, professional, चुका
49  customer  customer_provide_income           —           —             income, लाख, self, type, net
50  agent     agent_request_business_details    —           —             business, कृपया, बताएं।, proceed, address
51  agent     agent_ask_to_repeat               —           —             कॉल
52  customer  customer_report_done              —           —             भर दिया
53  customer  customer_respond_udyam            —           —             उद्यम, number, registered, card, उससे
54  agent     agent_request_udyam               —           —             उद्यम, number, नीचे, registered, समझ
55  customer  customer_respond_udyam            —           —             —
56  agent     agent_offer_skip_udyam            —           —             skip, करें।, कृपया, आगे, समझ
57  customer  customer_respond_udyam            —           —             इंतज़ार, देर, करिए
58  agent     agent_wait                        —           —             इंतज़ार, आगे, बताएं, ताकि, बढ़
59  customer  customer_other                    —           —             शुक्रिया
60  agent     agent_acknowledge                 —           —             मदद, कृपया, आगे, बताएं, ताकि
61  customer  customer_respond_udyam            —           —             number, समय, registered, याद
62  agent     agent_request_udyam               —           —             उद्यम, मदद, सबसे, सही, नंबर
63  customer  customer_respond_udyam            —           —             otp, इंतज़ार, कीजिए, registration, एकदम
64  agent     agent_request_otp                 —           —             otp, मदद, कृपया, verify, जाए
65  agent     agent_ask_to_repeat               —           —             कॉल
66  customer  customer_request_wait             —           —             wait, call, कीजिए
67  agent     agent_wait                        —           —             इंतज़ार, आगे, बताएं, ताकि, बढ़
68  customer  customer_other                    —           —             sms
69  agent     agent_answer_query                —           —             sms, हूँ।, मदद, कृपया, बताएं
70  customer  customer_report_done              —           —             —
71  agent     agent_request_otp                 —           —             otp, कृपया, verify, जाए, आगे
72  customer  customer_do_otp                   —           —             verification
73  agent     agent_request_otp                 —           —             कृपया, आगे, बताएं, पूरा, ताकि
74  customer  customer_acknowledge              —           —             offer, details, button, app, close
75  agent     agent_wait                        —           —             loan, offer, कृपया, शुरू, जाए
76  customer  customer_react_to_final_offer     —           —             loan, page, personal, lakh, चुका
77  agent     agent_acknowledge                 —           —             बढ़िया
78  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, call, amount, हूँ।
```

## Call 24d836c4 (transferred) — 53 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   customer  customer_agree                    —           —             चलेगा
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, करें।, link, click
6   customer  customer_express_distrust         distrustful —             fraud, उसमें
7   agent     agent_reassure_trust              —           —             sms, करें।, verify, page, capital
8   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
9   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
10  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
11  agent     agent_ask_to_repeat               —           —             एक बार फिर, कृपया, दोहरा
12  agent     agent_ask_to_repeat               —           —             एक बार फिर, कृपया, बताएं।, माफ़
13  customer  customer_provide_personal_details —           —             number, mobile, enter, name, full
14  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
15  customer  customer_ask_question             —           —             name, full, डालने
16  agent     agent_request_personal_details    —           —             enter, पैन, name, full, जैसा
17  customer  customer_request_wait             —           —             minute
18  agent     agent_wait                        —           —             इंतज़ार
19  customer  customer_request_wait             —           —             रुकिए, minute, line, confirm, pen
20  agent     agent_wait                        —           —             इंतज़ार
21  customer  customer_agree                    —           —             चलेगा
22  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
23  customer  customer_ask_question             —           —             capital, डालना, पड़ेगा
24  agent     agent_request_email               —           —             email, enter, address, सही, जैसा
25  customer  customer_acknowledge              —           —             —
26  agent     agent_request_address             —           —             address, pincode, locality, building, house number
27  customer  customer_ask_question             —           —             number, डालना, पड़ेगा
28  agent     agent_request_address             —           —             address, pincode, locality, building, flat
29  customer  customer_report_address_error     —           —             number, building
30  agent     agent_request_address             —           —             building, house number, flat, number, fill
31  customer  customer_provide_business_details —           —             —
32  agent     agent_request_address             —           —             flat, करें।, number, enter
33  customer  customer_ask_question             —           —             —
34  agent     agent_request_address             —           —             address, pincode, locality, building, house number
35  customer  customer_do_otp                   —           —             otp
36  agent     agent_request_address             —           —             address, pincode, locality, building, house number
37  customer  customer_do_otp                   —           —             otp, number, भेज, mobile, डाला
38  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, बताएं।
39  customer  customer_other                    —           —             मांग, service
40  agent     agent_wait                        —           —             करें।, otp, कृपया, बताएं।, इंतज़ार
41  customer  customer_do_otp                   —           —             —
42  agent     agent_request_otp                 —           —             otp, verify
43  agent     agent_ask_to_repeat               —           —             कृपया, माफ़, आखिरी, साफ़, दोहरा
44  customer  customer_do_otp                   —           —             otp
45  agent     agent_request_otp                 —           —             otp, हूँ।, verify, आगे, guide
46  customer  customer_request_wait             —           —             minute
47  agent     agent_wait                        —           —             इंतज़ार
48  customer  customer_react_to_final_offer     —           —             offer, लाख, हज़ार
49  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
50  customer  customer_report_applied           —           —             apply, देख
51  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
52  customer  customer_greet                    —           —             hello
```

## Call 26822e92 (transferred) — 60 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             करिए
5   customer  customer_acknowledge              —           —             खाली, गाड़ी
6   agent     agent_send_sms_link               —           —             sms, loan, कृपया, application, speaker
7   customer  customer_express_distrust         —           —             लेने, पैसे
8   agent     agent_reassure_trust              —           —             sms, कृपया, application, तरफ, capital
9   customer  customer_acknowledge              —           —             number
10  agent     agent_guide_open_link             —           —             लिंक पर क्लिक, sms, कृपया, बताएं, खुल
11  agent     agent_guide_open_link             —           —             sms, लिंक, शुक्रिया, खोल
12  customer  customer_request_wait             —           —             hold
13  agent     agent_wait                        —           —             इंतज़ार
14  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
15  agent     agent_guide_open_link             —           —             खुल गया, sms, कृपया, बताएं, बिल्कुल
16  agent     agent_guide_open_link             —           —             sms, लिंक, शुक्रिया, खोल
17  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, नीचे
18  customer  customer_report_done              —           —             कर दिया
19  agent     agent_request_otp                 —           —             कृपया, नंबर, टाइप, मोबाइल, पेज
20  customer  customer_report_done              —           —             —
21  agent     agent_request_otp                 —           —             कृपया, नंबर, मोबाइल
22  customer  customer_report_done              —           —             डाल
23  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
24  customer  customer_report_done              —           —             कर दिया
25  agent     agent_request_otp                 —           —             otp, हूँ।, मदद, verify, आगे
26  agent     agent_request_personal_details    —           —             कृपया, application, personal, details, सबसे
27  customer  customer_greet                    —           —             hello
28  agent     agent_request_pan                 —           —             पैन, कृपया, बताएं, नंबर, सुन
29  agent     agent_ask_to_repeat               —           —             कृपया, कीजिए, माफ़, दोबारा
30  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, बताएं।
31  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
32  customer  customer_acknowledge              —           —             —
33  agent     agent_request_email               —           —             email, कृपया, application, process, address
34  agent     agent_request_address             —           —             address, locality, building, house number, flat
35  agent     agent_ask_to_repeat               —           —             फिर से कह, माफ़, कहेंगे
36  customer  customer_report_done              —           —             भर दिया
37  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, नीचे, proceed
38  customer  customer_acknowledge              —           —             —
39  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, बताएं।, आगे
40  customer  customer_other                    —           —             आगे, उसमें
41  agent     agent_other                       —           —             कृपया, आगे, बताएं, समझती, पेज
42  customer  customer_other                    —           —             मांग, वापस
43  agent     agent_other                       —           —             sms, करें।, कृपया, शुरू, बताएं
44  customer  customer_react_to_offer           —           —             apply, offer, now, वापस, preapproved
45  agent     agent_guide_apply                 —           —             apply now, apply, now, मदद, कृपया
46  agent     agent_guide_apply                 —           —             apply now, apply, now, हूँ।, मदद
47  customer  customer_provide_email            —           —             email, डाल, मांग, दूं, mail
48  agent     agent_request_email               —           —             email, कृपया, personal, address, डालें
49  customer  customer_provide_personal_details —           —             gender, self, employed
50  agent     agent_ask_employment_type         —           —             self-employ, कृपया, details, self, employment
51  customer  customer_report_address_error     —           —             code, pin
52  agent     agent_request_address             —           —             करें।, सही, ताकि, चेक, जाए।
53  customer  customer_report_address_error     —           —             number, out
54  agent     agent_ask_to_repeat               —           —             फिर से बता, कृपया, कीजिए, माफ़, समझ
55  customer  customer_provide_address          —           —             house number, number, house, मांग
56  agent     agent_request_address             —           —             address, house number, flat, करें।, कृपया
57  customer  customer_react_to_final_offer     —           —             loan, offer
58  agent     agent_present_final_offer         —           —             loan, offer, amount, final, देख
59  customer  customer_other                    —           —             हज़ार, पचहत्तर
```

## Call 286e2a38 (transferred) — 32 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             बोलिए
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             बोलिए
5   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
6   customer  customer_agree                    —           —             बोलिए
7   customer  customer_ask_query                —           —             लाख, बोलिए, मिलेगा, पंद्रह, लेकर
8   agent     agent_present_offer               —           —             pre approved, loan, apply, approved, pre
9   agent     agent_send_sms_link               —           send_sms      sms, हूँ।, कृपया, application, रखें
10  agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
11  customer  customer_other                    —           —             apply
12  agent     agent_reassure_trust              —           —             loan, sms, application, शुरू, आगे
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
14  customer  customer_report_link_opened       —           —             खुल गया, खुल
15  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, नीचे
16  customer  customer_report_applied           —           —             click, दिए
17  agent     agent_request_otp                 —           —             करें।, कृपया, process, बताएं।, जाए
18  agent     agent_request_otp                 —           send_otp      otp, करें।, हूँ।, मदद, कृपया
19  customer  customer_do_otp                   —           —             otp
20  agent     agent_request_otp                 —           —             otp, कृपया, verify, आगे, बताएं
21  customer  customer_do_otp                   —           —             otp, डाल, दिए
22  agent     agent_request_otp                 —           —             मदद, कृपया, आगे, बताएं, पूरा
23  customer  customer_other                    —           —             time, loading
24  agent     agent_wait                        —           —             loan, offer, हूँ।, मदद, कृपया
25  customer  customer_other                    —           —             loading
26  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, application
27  customer  customer_report_done              —           —             loading
28  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
29  customer  customer_react_to_final_offer     —           —             कितना, पड़ेगा, लगता, हमको
30  agent     agent_present_final_offer         —           —             loan, offer, approved, pre, amount
31  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, मदद, कृपया, process
```

## Call 28eeeb54 (transferred) — 50 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello, fine, शेख
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             —
5   agent     agent_acknowledge                 —           —             ध्यान, गाड़ी
6   customer  customer_acknowledge              —           —             ऐसा
7   customer  customer_ask_question             —           —             process, दिए, time, कितने, बोला
8   customer  customer_query_fee                —           —             apply, समझ, बोलो, दिए, कैसा
9   agent     agent_send_sms_link               —           send_sms      लिंक भेज, application, भेज, समझ, करनी
10  customer  customer_acknowledge              —           —             —
11  customer  customer_query_fee                —           —             processing fee, process, processing, fees
12  customer  customer_query_fee                —           —             apply, सोच, मालूम
13  agent     agent_explain_fee                 —           —             processing fee, process, details, professional, समझ
14  customer  customer_acknowledge              —           —             —
15  agent     agent_acknowledge                 —           —             —
16  customer  customer_query_fee                —           —             interest rate, loan, amount, देख, process
17  customer  customer_query_fee                —           —             processing fee, interest rate, पूरा, interest, rate
18  agent     agent_explain_fee                 —           —             processing fee, interest rate, offer, sms, final
19  agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, जिसमें, भेज
20  customer  customer_acknowledge              —           —             मिल
21  agent     agent_guide_open_link             —           —             sms, कृपया, बढ़िया
22  customer  customer_greet                    —           —             hello
23  agent     agent_guide_open_link             —           —             वेबसाइट, लिंक पर क्लिक, sms, कृपया, बताएं
24  agent     agent_ask_to_repeat               —           —             माफ़, दोहरा
25  customer  customer_acknowledge              —           —             call
26  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई, लिंक पर क्लिक, खुल, क्लिक
27  customer  customer_report_link_opened       —           —             खुल गई, loan, personal, खुल, lakh
28  agent     agent_guide_apply                 —           —             नीचे
29  customer  customer_report_applied           —           —             apply now, apply, now, बोलकर
30  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, button
31  customer  customer_do_otp                   —           —             number, mobile, enter
32  agent     agent_acknowledge                 —           —             कृपया, सही
33  customer  customer_acknowledge              —           —             —
34  agent     agent_request_otp                 —           —             कृपया, number, mobile, था।, टाइप
35  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
36  customer  customer_acknowledge              —           —             call
37  customer  customer_report_sms_received      —           —             link भेज, process, भेज, link, पूरा
38  agent     agent_send_sms_link               —           send_sms      sms, हूँ।, मदद, कृपया, application
39  customer  customer_express_distrust         —           —             apply, ऐसा
40  customer  customer_skip_udyam               frustrated  —             नहीं हो, उसमें, cancel, problem
41  agent     agent_reassure_trust              —           —             loan, देख, application, शुरू, process
42  customer  customer_express_distrust         —           —             number, mobile, डाल, ऐसा, देने
43  agent     agent_reassure_trust              —           —             application, number, mobile, details, capital
44  customer  customer_do_otp                   —           —             otp, call, डालने, पुछ
45  agent     agent_request_otp                 —           —             otp, sms, करें।, मदद, कृपया
46  customer  customer_react_to_final_offer     —           —             loan, otp, लाख, congratulation
47  agent     agent_present_final_offer         —           —             loan, offer, देख, लाख, रुपये
48  customer  customer_react_to_final_offer     —           —             देख
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, मदद, कृपया, process
```

## Call 292a5872 (transferred) — 40 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
1   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
2   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
3   customer  customer_agree                    —           —             —
4   customer  customer_agree                    —           —             ज़रूर
5   agent     agent_send_sms_link               —           send_sms      sms, loan, करें।, कृपया, application
6   agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, भेज, मिल
7   customer  customer_report_sms_received      —           —             मिल
8   agent     agent_guide_open_link             —           —             खुल गया, sms, कृपया, खुल, बढ़िया
9   agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, नीचे
10  customer  customer_acknowledge              —           —             —
11  agent     agent_request_otp                 —           send_otp      otp, apply, करें।, now, कृपया
12  customer  customer_report_done              —           —             हो गया
13  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, जाएगा।, self
14  customer  customer_state_employment_type    —           —             self employ, self, employed
15  agent     agent_request_income              —           —             income, कृपया, बताएं।, जाए, monthly
16  customer  customer_other                    —           —             number, personal, professional, पुछ
17  agent     agent_request_org_name            —           —             कृपया, बताएं, समझ, business, टाइप
18  customer  customer_acknowledge              —           —             —
19  agent     agent_request_business_details    —           —             business, address
20  customer  customer_provide_personal_details —           —             date of birth, birth, date, इधर
21  agent     agent_request_personal_details    —           —             कृपया, personal, details, समझ, फॉर्म
22  customer  customer_provide_personal_details —           —             status
23  agent     agent_request_personal_details    —           —             marital, personal, आगे, email, address
24  customer  customer_state_employment_type    —           —             self employ, proceed, self, employed, पता
25  agent     agent_request_income              —           —             income, कृपया, बताएं।, monthly, self
26  customer  customer_report_done              —           —             —
27  agent     agent_request_business_details    —           —             business, करें।, कृपया, बताएं।, proceed
28  customer  customer_respond_udyam            —           —             उद्यम, पुछ, किधर
29  agent     agent_request_udyam               —           —             udyam, करें।, कृपया, number, नीचे
30  agent     agent_ask_to_repeat               —           —             माफ़, दोबारा
31  customer  customer_acknowledge              —           —             much
32  agent     agent_request_udyam               —           —             udyam, loan, offer, करें।, otp
33  agent     agent_ask_to_repeat               —           —             कृपया, दोहरा
34  customer  customer_acknowledge              —           —             note
35  agent     agent_wait                        —           —             loan, offer, हूँ।, otp, मदद
36  customer  customer_ask_question             —           —             —
37  agent     agent_present_final_offer         —           —             loan, offer, approved, amount, otp
38  customer  customer_acknowledge              —           —             —
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, कृपया, process, relationship
```

## Call 294cf852 (transferred) — 39 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, link
6   customer  customer_report_link_opened       —           —             बोलिए, देखा
7   customer  customer_greet                    —           —             hello
8   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
9   customer  customer_report_applied           —           —             apply
10  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
11  customer  customer_do_otp                   —           —             otp
12  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
13  customer  customer_do_otp                   —           —             verify, click
14  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
15  customer  customer_provide_pan              —           —             pan, number, डाल
16  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
17  customer  customer_report_done              —           —             भर दिया
18  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
19  customer  customer_report_done              —           —             भर दिया
20  agent     agent_request_address             —           —             address, pincode, locality, building, house number
21  customer  customer_report_done              —           —             कर दिया, fill
22  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
25  customer  customer_state_employment_type    —           —             salaried
26  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
37  customer  customer_react_to_final_offer     —           —             loan, offer, amount, देख, लाख
38  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 298f09f6 (transferred) — 124 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   customer  customer_greet                    —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, इंतज़ार
3   customer  customer_greet                    —           —             hello
4   agent     agent_greet                       —           —             बोल, हूँ।, शुरू, तरफ, आदित्य
5   customer  customer_express_distrust         —           —             apply
6   customer  customer_query_fee                —           —             interest, लगेगा
7   customer  customer_agree                    —           —             बोलो
8   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
9   agent     agent_guide_open_link             —           —             sms, करें।, link, click
10  customer  customer_report_sms_received      —           —             sms
11  agent     agent_send_sms_link               —           —             sms, करें।, कृपया, बताएं।, जाए
12  customer  customer_report_sms_received      —           —             —
13  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
14  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
15  customer  customer_report_applied           —           —             apply now, apply, now, click, खुला
16  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, नीचे
17  customer  customer_report_done              —           —             कर दिया
18  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
19  customer  customer_ask_question             —           —             —
20  agent     agent_request_otp                 —           —             number, get, terms, mobile, check
21  customer  customer_report_done              —           —             कर दिया
22  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_request_pan                 —           —             पैन, page, number, details, सबसे
25  customer  customer_provide_pan              —           —             तिरपन
26  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
27  customer  customer_react_to_final_offer     —           —             लाख, हज़ार, तिरपन
28  agent     agent_request_pan                 —           —             पैन, कृपया, number, fill, बताएं
29  agent     agent_ask_to_repeat               —           —             फिर से कह, एक बार फिर, माफ़, कहेंगे
30  customer  customer_ask_question             —           —             —
31  agent     agent_request_personal_details    —           —             gender, date of birth, marital, number, बताएं।
32  customer  customer_acknowledge              —           —             —
33  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
34  agent     agent_ask_to_repeat               —           —             साफ़ बोल, कीजिए, माफ़, साफ़, बोलेंगे
35  customer  customer_request_wait             —           —             minute
36  customer  customer_greet                    —           —             hello
37  agent     agent_wait                        —           —             इंतज़ार, chd
38  customer  customer_greet                    —           —             hello
39  agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
40  agent     agent_greet                       —           —             नमस्ते, बोल
41  agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
42  customer  customer_provide_personal_details —           —             date of birth, बोल, आगे, birth, date
43  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
44  customer  customer_report_done              —           —             email, डाल
45  agent     agent_request_address             —           —             address, pincode, locality, building, house number
46  customer  customer_acknowledge              —           —             —
47  agent     agent_request_address             —           —             address, pincode, locality, building, house number
48  customer  customer_report_done              —           —             हो गया
49  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
50  customer  customer_report_address_error     —           —             proceed
51  agent     agent_other                       —           —             करें।, कृपया, terms, check, conditions
52  customer  customer_report_address_error     —           —             name, building
53  agent     agent_help_address_error          —           —             करें।, name, building, सही, चेक
54  customer  customer_ask_question             —           —             डालो
55  agent     agent_request_address             —           —             address, building, name, सही, डालें
56  customer  customer_ask_question             —           —             address
57  agent     agent_request_address             —           —             address, फ्लैट
58  customer  customer_acknowledge              —           —             —
59  agent     agent_request_address             —           —             address
60  customer  customer_report_done              —           —             कर दिया, proceed
61  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
62  customer  customer_ask_question             —           —             —
63  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
64  customer  customer_ask_question             —           —             डालना
65  agent     agent_request_otp                 —           —             otp, करें।, verify, button, click
66  customer  customer_provide_email            —           —             email, डालना, पड़ेगा
67  agent     agent_request_otp                 —           —             otp, करें।, verify, personal, enter
68  customer  customer_acknowledge              —           —             अरे
69  agent     agent_request_otp                 —           —             otp, करें।, verify, बताएं।, जाए
70  agent     agent_request_otp                 —           —             otp, करें।, कृपया, check, enter
71  customer  customer_do_otp                   —           —             —
72  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, बताएं।
73  customer  customer_provide_income           —           —             income, आगे, address, monthly, मांग
74  agent     agent_request_income              —           —             income, home, monthly, net, salary
75  customer  customer_acknowledge              —           —             —
76  agent     agent_request_income              —           —             income, home, monthly, net, salary
77  customer  customer_other                    frustrated  —             नहीं हो रहा, नहीं हो, show
78  agent     agent_ask_to_repeat               —           —             साफ़, show, part
79  customer  customer_express_distrust         distrustful —             fraud
80  agent     agent_reassure_trust              —           —             sms, करें।, verify, page, capital
81  customer  customer_provide_personal_details —           —             name, मांग, original
82  agent     agent_request_personal_details    —           —             enter, पैन, name, full, जैसा
83  customer  customer_provide_org_name         frustrated  —             नहीं हो रहा, नहीं हो, name, option, उसमें
84  agent     agent_request_org_name            —           —             enter, official, company, documents, डालें।
85  customer  customer_ask_question             —           —             किस
86  agent     agent_request_org_name            —           —             organization, enter, company, उसी, जगह
87  customer  customer_acknowledge              —           —             मांग
88  agent     agent_request_org_name            —           —             organization, करें।, enter, name, field
89  customer  customer_provide_org_name         —           —             line, दूं, india
90  agent     agent_request_org_name            —           —             organization, name, सही, official, डालें
91  customer  customer_provide_org_name         —           —             डाल, दूं, private, india
92  agent     agent_request_org_name            —           —             organization, enter, name, exactly
93  customer  customer_ask_question             —           —             —
94  customer  customer_provide_email            —           —             email, official, डालूं
95  agent     agent_request_email               —           —             email, official, डालें, काम, जिसका
96  customer  customer_provide_email            —           —             email
97  agent     agent_request_email               —           —             email, personal, दिक्कत, डालें, use
98  customer  customer_report_done              —           —             proceed, डाल
99  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
100 customer  customer_report_done              —           —             हो गया, नीचे, proceed, मांग
101 agent     agent_request_terms_accept        —           —             button, proceed, click, आगे, ताकि
102 customer  customer_request_wait             —           —             wait, button, app, close, back
103 agent     agent_wait                        —           —             chd, sure
104 customer  customer_react_to_final_offer     —           —             loan, लाख, हज़ार, तिरपन
105 agent     agent_present_final_offer         —           —             loan, offer, लाख, रुपये, आगे
106 customer  customer_query_fee                —           —             interest
107 agent     agent_explain_fee                 —           —             interest rate, offer, final, शुरू, interest
108 customer  customer_query_fee                —           —             पच्चीस, उन्नीस
109 agent     agent_explain_fee                 —           —             interest rate, offer, final, शुरू, interest
110 customer  customer_query_fee                —           —             processing fee, हज़ार, processing, रुपए, fees
111 agent     agent_explain_fee                 —           —             processing fee, loan, मदद, terms, आगे
112 customer  customer_other                    —           —             loan
113 agent     agent_end_call                    —           —             call, हूँ।, समय, समझ, चाहें
114 customer  customer_query_fee                —           —             charges
115 agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, connect, समझ, चाहें, continue
116 customer  customer_agree                    skeptical   —             doubt, clear, दिक़्क़त
117 agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, हूँ।, connect, समझ, दूँ
118 customer  customer_agree                    —           —             connect
119 agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, करें।, हूँ।, कृपया, समय
120 customer  customer_acknowledge              —           —             call, free
121 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
122 agent     agent_end_call                    —           —             goodbye, duration has been exceeded, call, now, end
123 customer  customer_other                    —           —             —
```

## Call 2af0490b (transferred) — 35 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             —
3   customer  customer_query_fee                confused    —             interest rate, कैसे, interest, rate, जानकारी
4   agent     agent_explain_fee                 —           —             interest rate, offer, हूँ।, final, शुरू
5   customer  customer_query_fee                —           —             कितने, last
6   agent     agent_explain_fee                 —           —             interest rate, offer, sms, final, application
7   customer  customer_query_fee                —           —             शुरू, point, ten, nine, last
8   agent     agent_explain_fee                 —           —             interest rate, sms, application, जिसमें, भेज
9   customer  customer_other                    —           —             —
10  customer  customer_query_fee                —           —             interest, point, lakh, ten, nine
11  agent     agent_explain_fee                 —           —             interest rate, sms, करें।, final, application
12  customer  customer_agree                    —           —             बताएं
13  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
14  agent     agent_ask_to_repeat               —           —             फिर से कह, माफ़, कहेंगे
15  customer  customer_provide_email            —           —             email, line
16  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
17  customer  customer_report_link_opened       —           —             link
18  customer  customer_report_link_opened       —           —             email, address, open, भाई, डालेंगे
19  agent     agent_guide_open_link             —           —             sms, link, personal, सबसे, enter
20  customer  customer_report_applied           —           —             apply, click
21  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, link
22  customer  customer_do_otp                   —           —             बोल, number, mobile, डालने
23  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
24  customer  customer_provide_email            —           —             email
25  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
26  customer  customer_do_otp                   —           —             otp, मांग
27  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
28  customer  customer_do_otp                   —           —             number, मांग, same
29  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, number
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, हूँ।
32  customer  customer_query_fee                frustrated  —             interest rate, नहीं हो रहा, नहीं हो, interest, rate
33  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, relationship, manager, connect, help
34  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, मदद, कृपया, relationship
```

## Call 30f7f2d2 (transferred) — 47 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             बोलिए
5   customer  customer_ask_question             —           —             number, जिससे, पाए, दूसरा
6   agent     agent_present_offer               —           —             pre-approved, offer, approved, pre, हूँ।
7   customer  customer_ask_question             —           —             शुरू, documents
8   agent     agent_explain_fee                 —           —             interest rate, offer, sms, final, application
9   customer  customer_agree                    —           —             process, ऐसे
10  agent     agent_send_sms_link               —           send_sms      sms, हूँ।, application, शुरू, process
11  customer  customer_ask_question             —           —             पड़ेगा
12  agent     agent_guide_open_link             —           —             sms, link, भेजने
13  customer  customer_ask_question             —           —             step, next
14  agent     agent_guide_open_link             —           —             sms, करें।, link, click
15  customer  customer_ask_question             —           —             —
16  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, नीचे
17  customer  customer_report_done              —           —             —
18  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
19  customer  customer_ask_question             —           —             otp
20  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, personal, details
21  customer  customer_provide_personal_details —           —             personal, detail
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital, personal, details
23  customer  customer_ask_question             —           —             next
24  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
25  customer  customer_ask_question             —           —             —
26  agent     agent_request_address             —           —             address, pincode, locality, building, house number
27  customer  customer_ask_question             —           —             —
28  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
29  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
30  customer  customer_state_employment_type    —           —             salaried
31  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
32  customer  customer_acknowledge              —           —             next
33  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
34  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
35  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
36  customer  customer_acknowledge              —           —             —
37  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
38  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
39  agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, कहेंगे, साफ़, आया।
40  customer  customer_report_done              —           —             app
41  agent     agent_request_otp                 —           —             otp, verify, आगे, नहीं।, बढ़ेंगे।
42  agent     agent_present_final_offer         —           —             final, page
43  customer  customer_do_otp                   —           —             otp
44  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
45  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
46  agent     agent_transfer_to_rm              —           transfer_to_rm140000, loan, call, amount, name
```

## Call 3263832d (transferred) — 89 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
1   customer  customer_agree                    —           —             —
2   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
3   agent     agent_guide_open_link             —           —             sms, करें।, link, click
4   customer  customer_ask_question             —           —             भेज, बोलो
5   agent     agent_send_sms_link               —           send_sms      sms, process, भेज, link, complete
6   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
7   customer  customer_report_link_opened       —           —             link, share
8   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
9   customer  customer_report_link_opened       —           —             link
10  agent     agent_guide_open_link             —           —             करें।, link, check, try, internet
11  customer  customer_other                    —           —             internet, connection
12  agent     agent_guide_open_link             —           —             link, try, once, again
13  customer  customer_request_wait             —           —             minute
14  agent     agent_wait                        —           —             chd
15  customer  customer_request_wait             —           —             minute
16  agent     agent_wait                        —           —             chd, sure
17  customer  customer_report_link_opened       —           —             link, share
18  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, भेज, link
19  customer  customer_report_link_opened       —           —             call, link, cut, share
20  agent     agent_answer_query                —           —             capital, aditya, birla
21  customer  customer_ask_question             —           —             link
22  agent     agent_answer_query                —           —             sms, capital, name, registered, aditya
23  customer  customer_ask_question             —           —             mail
24  agent     agent_answer_query                —           —             sms, capital, aditya, birla, नहीं।
25  agent     agent_ask_to_repeat               —           —             फिर से बता, कीजिए, माफ़
26  customer  customer_request_wait             —           —             minute
27  customer  customer_other                    —           —             house, भाई, कैसा
28  agent     agent_wait                        —           —             इंतज़ार
29  customer  customer_greet                    —           —             hello
30  agent     agent_confirm                     —           —             आगे बढ़, हूँ।, आगे, बढ़ें
31  customer  customer_report_link_opened       —           —             लाख, click, बढ़िया, उसको, भेजा
32  agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, sms
33  agent     agent_ask_to_repeat               —           —             फिर से कह, माफ़, कहेंगे
34  customer  customer_acknowledge              —           —             call
35  agent     agent_acknowledge                 —           —             call
36  customer  customer_report_done              —           —             process
37  agent     agent_guide_open_link             —           —             sms, करें।, कृपया, application, process
38  customer  customer_do_otp                   —           —             call, number, डाला
39  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
40  customer  customer_ask_question             —           —             बोल, आगे
41  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, number, get
42  customer  customer_request_wait             —           —             wait, otp, minute, डाल, दिखा
43  agent     agent_wait                        —           —             सबसे
44  customer  customer_report_done              —           —             page, खुला
45  agent     agent_wait                        —           —             loan, सबसे
46  customer  customer_agree                    —           —             पूरा, बोलो, detail
47  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, इंतज़ार
48  customer  customer_ask_question             —           —             name, company
49  agent     agent_greet                       —           —             बोल, हूँ।, तरफ, आदित्य, बिरला
50  customer  customer_provide_org_name         —           —             company, दर्ज
51  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
52  customer  customer_request_wait             —           —             minute
53  agent     agent_wait                        —           —             इंतज़ार
54  customer  customer_provide_org_name         —           —             call, company, दर्ज
55  agent     agent_request_org_name            —           —             कृपया, बताएं।, जाए, enter, company
56  customer  customer_acknowledge              —           —             —
57  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
58  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
59  customer  customer_other                    —           —             what
60  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
61  customer  customer_ask_question             —           —             मतलब, income, महीने
62  agent     agent_answer_query                —           —             income, net, salary, account, महीने
63  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
64  customer  customer_request_wait             —           —             minute
65  agent     agent_wait                        —           —             इंतज़ार
66  customer  customer_ask_question             —           —             कितना, interface
67  agent     agent_answer_query                —           —             हूँ।, मदद, details, आगे, fill
68  customer  customer_report_done              —           —             processing
69  agent     agent_wait                        —           —             मदद, कृपया, पूरा, बढ़िया, processing
70  customer  customer_react_to_final_offer     —           —             amount, page, पूरा, खुल, दिख
71  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
72  customer  customer_react_to_final_offer     —           —             देख
73  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
74  customer  customer_react_to_final_offer     —           —             लाख, minute, रुपए, महीने, चौबीस
75  agent     agent_present_final_offer         —           —             loan, offer, लाख, आगे, चाहेंगे
76  customer  customer_query_fee                —           —             interest, कितना, उसको, बारह
77  agent     agent_explain_fee                 —           —             interest rate, interest, rate, percent, point
78  customer  customer_react_to_final_offer     —           —             हज़ार, चार
79  agent     agent_explain_fee                 —           —             interest rate, interest, rate, point, ten
80  customer  customer_react_to_final_offer     —           —             हज़ार, सात, चार
81  agent     agent_explain_fee                 —           —             interest rate, offer, final, शुरू, interest
82  customer  customer_react_to_final_offer     —           —             हज़ार, सात, इधर, पांच, चार
83  agent     agent_present_final_offer         —           —             loan, amount
84  customer  customer_react_to_final_offer     —           —             loan, लाख
85  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
86  customer  customer_react_to_final_offer     —           —             देख, सामने, खुला
87  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
88  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 354b7cd9 (transferred) — 60 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_acknowledge              —           —             english
3   agent     agent_greet                       —           —             capital, aditya, birla, speak
4   customer  customer_greet                    —           —             speaking
5   agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, apply
6   agent     agent_send_sms_link               —           send_sms      sms, application, link, speaker, check
7   agent     agent_guide_open_link             —           —             sms, now, link, click
8   agent     agent_ask_to_repeat               —           —             call, sorry, there, still
9   customer  customer_request_wait             —           —             one, second
10  agent     agent_wait                        —           —             chd, sure
11  customer  customer_report_link_opened       —           —             link
12  agent     agent_guide_apply                 —           —             apply now, apply, now, screen, button
13  agent     agent_request_otp                 —           send_otp      otp, now, number, get, terms
14  agent     agent_ask_to_repeat               —           —             call, sorry, still
15  customer  customer_request_wait             —           —             one, second
16  agent     agent_wait                        —           —             chd, sure
17  agent     agent_request_otp                 —           —             otp, verify, screen, click, enter
18  customer  customer_report_done              —           —             done
19  agent     agent_request_pan                 —           —             pan, now, page, number, details
20  customer  customer_report_done              —           —             done
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital, now, enter
22  agent     agent_ask_to_repeat               —           —             call, sorry, still
23  customer  customer_provide_address          —           —             address, typing
24  agent     agent_request_email               —           —             email, now, personal, enter, address
25  agent     agent_ask_to_repeat               —           —             sorry, repeat, catch
26  customer  customer_report_done              —           —             done
27  agent     agent_request_address             —           —             address, pincode, locality, building, house number
28  agent     agent_request_terms_accept        —           —             terms and condition, terms, button, check, conditions
29  customer  customer_acknowledge              —           —             —
30  agent     agent_ask_employment_type         —           —             salaried, self-employ, page, details, self
31  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
32  agent     agent_ask_to_repeat               —           —             call, sorry, there, still
33  customer  customer_report_done              —           —             done
34  agent     agent_request_income              —           —             home, monthly, net, salary, take
35  agent     agent_ask_to_repeat               —           —             call, sorry, still
36  customer  customer_request_wait             —           —             one, loading, second
37  agent     agent_request_income              —           —             home, enter, monthly, net, salary
38  customer  customer_express_distrust         —           —             person, real
39  agent     agent_reassure_trust              —           —             loan, application, capital, aditya, birla
40  agent     agent_ask_to_repeat               —           —             call, sorry, still
41  customer  customer_request_wait             —           —             wait, call, still
42  agent     agent_wait                        —           —             chd, sure
43  agent     agent_ask_to_repeat               —           —             there, still
44  customer  customer_do_otp                   —           —             —
45  agent     agent_request_org_name            —           —             organization, now, enter, name, know
46  agent     agent_ask_to_repeat               —           —             call, sorry, there, still
47  agent     agent_request_email               —           —             email, now, enter, official, know
48  customer  customer_report_done              —           —             done
49  agent     agent_request_address             —           —             address, pincode, now, fill, organization
50  agent     agent_request_address             —           —             address, pincode, enter, fill, organization
51  customer  customer_report_done              —           —             done
52  agent     agent_request_terms_accept        —           —             now, details, button, proceed, click
53  agent     agent_ask_to_repeat               —           —             call, there, still
54  agent     agent_confirm_step                —           —             now, details, button, proceed, click
55  agent     agent_request_otp                 —           —             otp, verify, email, registered, know
56  agent     agent_request_otp                 —           —             otp, get, wait, seconds, know
57  customer  customer_report_done              —           —             done
58  agent     agent_present_final_offer         —           —             final offer, loan amount and, loan, offer, amount
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, now, process, relationship, manager
```

## Call 3b10addb (transferred) — 37 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_ask_question             —           —             कितने
5   agent     agent_present_offer               —           —             pre-approved, loan, approved, pre, amount
6   customer  customer_query_fee                —           —             कितना
7   agent     agent_present_offer               —           —             pre-approved, loan, approved, pre
8   customer  customer_ask_question             —           —             कितना
9   agent     agent_present_offer               —           —             pre-approved, loan, approved, pre, amount
10  customer  customer_query_fee                —           —             interest, percent, कितना
11  agent     agent_explain_fee                 —           —             interest rate, हूँ।, application, शुरू, interest
12  customer  customer_greet                    —           —             hello
13  agent     agent_guide_open_link             —           —             sms, करें।, link, click
14  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
15  customer  customer_agree                    —           —             शुरू कर, शुरू
16  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
17  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
18  agent     agent_guide_open_link             —           —             sms, करें।, link, click
19  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
22  customer  customer_report_applied           —           —             apply
23  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, नीचे
24  customer  customer_report_done              —           —             कर दिया
25  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
26  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
27  customer  customer_other                    —           —             zero, सत्तर
28  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
29  customer  customer_report_done              —           —             कर दिया
30  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
31  customer  customer_react_to_final_offer     —           —             हज़ार, one
32  agent     agent_request_otp                 —           —             otp, करें।, verify, बताएं।, जाए
33  customer  customer_report_done              —           —             कर दिया
34  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
35  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
36  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 3bda83f6 (transferred) — 44 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   customer  customer_greet                    —           —             hello, शुरू
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   customer  customer_acknowledge              —           —             —
6   agent     agent_guide_open_link             —           —             sms, करें।, link, click
7   customer  customer_acknowledge              —           —             —
8   agent     agent_guide_apply                 —           —             screen, home
9   customer  customer_report_done              —           —             कर दिया
10  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
11  customer  customer_report_done              —           —             कर दिया
12  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
13  customer  customer_report_done              —           —             कर दिया
14  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
15  customer  customer_do_otp                   —           —             verify
16  agent     agent_request_pan                 —           —             पैन, otp, verify, शुरू, page
17  customer  customer_report_done              —           —             कर दिया
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
19  customer  customer_report_done              —           —             हो गया
20  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_address             —           —             address, pincode, locality, building, house number
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
25  customer  customer_accept_terms             —           —             proceed
26  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
27  customer  customer_state_employment_type    —           —             salaried
28  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
33  customer  customer_acknowledge              —           —             —
34  agent     agent_acknowledge                 —           —             —
35  customer  customer_report_done              —           —             कर दिया
36  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
37  customer  customer_report_done              —           —             कर दिया
38  agent     agent_guide_apply                 —           —             करें।, button, proceed, click
39  customer  customer_report_done              —           —             कर दिया, proceed
40  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
41  customer  customer_do_otp                   —           —             verify
42  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
43  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 3f381582 (transferred) — 53 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   customer  customer_query_fee                —           —             —
4   agent     agent_explain_fee                 —           —             interest rate, offer, final, शुरू, interest
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
6   agent     agent_guide_open_link             —           —             sms, करें।, link, click
7   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
8   agent     agent_ask_to_repeat               —           —             चूंकि, उत्तर
9   customer  customer_do_otp                   —           —             number, mobile
10  agent     agent_request_otp                 —           —             number, mobile
11  customer  customer_do_otp                   —           —             number, mobile, डाल
12  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
13  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
14  customer  customer_provide_pan              —           —             pan, number, मांग
15  agent     agent_request_pan                 —           —             पैन, करें।, number, enter, capital
16  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
18  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
19  agent     agent_request_address             —           —             address, pincode, locality, building, house number
20  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
21  customer  customer_request_wait             —           —             wait
22  agent     agent_wait                        —           —             इंतज़ार
23  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
24  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
25  agent     agent_request_income              —           —             monthly, salaried
26  customer  customer_state_employment_type    —           —             self employ, self, employed, filling
27  agent     agent_request_income              —           —             income, fill, monthly, self, net
28  agent     agent_request_income              —           —             income, बताएं।, जाए, fill, monthly
29  customer  customer_report_done              —           —             —
30  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, registered
31  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, address
32  customer  customer_report_done              —           —             —
33  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
34  customer  customer_acknowledge              —           —             —
35  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
36  customer  customer_skip_udyam               —           —             skip, उद्यम
37  agent     agent_offer_skip_udyam            —           —             skip, number, click, option, udyam
38  customer  customer_skip_udyam               —           —             skip, उद्यम, hold
39  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, इंतज़ार
40  customer  customer_react_to_final_offer     —           —             loan amount and, loan, amount, final, sorry
41  agent     agent_present_final_offer         —           —             final offer, loan amount and, cannot be changed, loan, offer
42  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
43  customer  customer_request_wait             —           —             minute, calculate
44  agent     agent_wait                        —           —             इंतज़ार
45  customer  customer_other                    —           —             loan, tenure
46  agent     agent_answer_query                —           —             loan, offer, मदद, final, आगे
47  customer  customer_ask_question             —           —             उसको, tenure
48  agent     agent_answer_query                —           —             loan, मदद, final, process, आगे
49  customer  customer_ask_query                —           —             साल
50  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, final, relationship, manager
51  customer  customer_agree                    —           —             —
52  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, मदद, कृपया, relationship
```

## Call 42e13796 (transferred) — 78 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   customer  customer_agree                    —           —             करिए
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, करें।, link, click
6   customer  customer_ask_question             —           —             saying
7   agent     agent_greet                       —           —             बोल, हूँ।, तरफ, आदित्य, बिरला
8   customer  customer_agree                    —           —             बोलिए
9   agent     agent_guide_open_link             —           —             sms, करें।, link, click
10  customer  customer_report_link_opened       —           —             open
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
12  customer  customer_report_done              —           —             कर दिया
13  agent     agent_request_otp                 —           —             number, mobile, enter
14  customer  customer_do_otp                   —           —             number, mobile, डालने, बोला
15  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
16  customer  customer_do_otp                   —           —             otp
17  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
18  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
19  customer  customer_report_done              —           —             कर दिया
20  customer  customer_react_to_offer           —           —             हज़ार, lakh, one, लिखा, रुपए
21  agent     agent_request_pan                 —           —             पैन, offer, हूँ।, final, application
22  customer  customer_query_fee                —           —             कितना, कितने, साल, month, per
23  agent     agent_answer_query                —           —             loan, offer, amount, final, application
24  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, सबसे
25  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, सबसे
26  customer  customer_report_done              —           —             कर दिया
27  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
30  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
31  customer  customer_provide_email            —           —             email, डाल
32  agent     agent_request_address             —           —             address, pincode, locality, building, house number
33  customer  customer_provide_address          —           —             building, name, चालू, area
34  agent     agent_answer_query                —           —             बताएं।, जाए, address, name, building
35  customer  customer_acknowledge              —           —             call
36  agent     agent_request_address             —           —             address, pincode, locality, building, house number
37  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
38  customer  customer_acknowledge              —           —             —
39  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
40  customer  customer_provide_address          —           —             area
41  agent     agent_answer_query                —           —             करें।, proceed, fill, सही, दिख
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
44  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
45  customer  customer_provide_business_details —           —             business, name, company
46  agent     agent_request_business_details    —           —             business, enter, name, registered, full
47  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
48  customer  customer_provide_business_details —           —             business, team
49  agent     agent_request_business_details    —           —             business, enter, name, registered, full
50  customer  customer_provide_business_details —           —             business, number, बोलो, code, pin
51  agent     agent_request_address             —           —             address, number, enter, business, documents
52  customer  customer_provide_business_details —           —             business, नीचे, address, डाल, code
53  agent     agent_request_address             —           —             करें।, कृपया, details, enter, सही
54  customer  customer_acknowledge              —           —             —
55  agent     agent_guide_apply                 —           —             करें।, button, proceed, click
56  customer  customer_acknowledge              —           —             ऊपर
57  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
58  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
59  customer  customer_skip_udyam               —           —             skip, दूं, उसको
60  customer  customer_skip_udyam               —           —             skip, उद्यम, उसको
61  agent     agent_offer_skip_udyam            —           —             skip, number, आगे, होगा।, udyam
62  customer  customer_acknowledge              —           —             cancel
63  agent     agent_offer_skip_udyam            —           —             skip, आगे, होगा।, नंबर, स्क्रीन
64  customer  customer_ask_question             —           —             आगे, बढ़ेगा
65  agent     agent_inform_manual_review        —           push_to_crm   manual review, करें।, application, आगे, जाएगा।
66  customer  customer_agree                    —           —             बोलिए
67  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
68  customer  customer_other                    —           —             loan, application, process, sorry, वापस
69  agent     agent_end_call                    —           —             loan, application, process, connect, आपसे
70  agent     agent_present_final_offer         —           —             final, page
71  customer  customer_acknowledge              —           —             call
72  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
73  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
74  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
75  customer  customer_react_to_final_offer     —           —             लाख, हज़ार
76  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
77  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 465ce42d (transferred) — 58 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             बोल, बोलिए
5   customer  customer_greet                    —           —             hello, बोलिए
6   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   customer  customer_report_sms_received      —           —             message
9   agent     agent_wait                        —           —             sms, करें।, कृपया, link, इंतज़ार
10  agent     agent_guide_open_link             —           —             sms, link, click
11  customer  customer_report_link_opened       —           —             देख
12  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
13  customer  customer_report_applied           —           —             apply
14  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
15  customer  customer_query_fee                —           —             आगे, interest, जानकारी, कितना, लगेगा
16  agent     agent_answer_query                —           —             loan, amount, application, number, mobile
17  customer  customer_agree                    —           —             —
18  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
19  customer  customer_react_to_offer           —           —             लाख, हज़ार
20  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
22  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
23  customer  customer_acknowledge              —           —             —
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  customer  customer_acknowledge              —           —             call
26  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
27  customer  customer_provide_address          —           —             address, save
28  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
29  customer  customer_request_wait             —           —             minute
30  agent     agent_wait                        —           —             इंतज़ार
31  customer  customer_acknowledge              —           —             —
32  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
33  customer  customer_other                    frustrated  —             नहीं हो रहा, नहीं हो, process, आगे, डाल
34  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
35  customer  customer_other                    —           —             page, open, first
36  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
37  customer  customer_other                    frustrated  —             नहीं हो रहा, नहीं हो, page, आगे, open
38  agent     agent_answer_query                —           —             sms, करें।, link, पूरी, open
39  customer  customer_acknowledge              —           —             call
40  agent     agent_answer_query                —           —             sms, link, पूरी, मिला, issue
41  customer  customer_acknowledge              —           —             call
42  agent     agent_answer_query                —           —             sms, link, पूरी, मिला, issue
43  customer  customer_report_link_opened       —           —             खोल
44  agent     agent_request_address             —           —             address, pincode, करें।, बताएं।, जाए
45  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, दोबारा
46  customer  customer_report_done              —           —             page, fill, दुबारा, first
47  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
48  customer  customer_acknowledge              —           —             —
49  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
50  customer  customer_acknowledge              —           —             बताएं
51  agent     agent_request_otp                 —           —             otp, करें।, कृपया, verify, बताएं।
52  customer  customer_acknowledge              —           —             —
53  agent     agent_request_otp                 —           —             otp, verify
54  customer  customer_acknowledge              —           —             call
55  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
56  customer  customer_react_to_final_offer     —           —             देख
57  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 4ee4e8eb (transferred) — 86 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello, बोलिए
3   agent     agent_present_offer               —           —             आदित्य, बिरला, कैपिटल
4   customer  customer_greet                    —           —             hello, बोलिए
5   customer  customer_greet                    —           —             hello
6   agent     agent_present_offer               —           —             तरफ, आदित्य, बिरला, कैपिटल
7   customer  customer_agree                    —           —             बोलिए
8   customer  customer_agree                    confused    —             कैसे
9   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
10  agent     agent_guide_open_link             —           —             sms, करें।, link, click
11  customer  customer_query_fee                —           —             rate, कितना
12  agent     agent_explain_fee                 —           —             interest rate, offer, sms, करें।, final
13  customer  customer_request_wait             —           —             minute
14  agent     agent_wait                        —           —             इंतज़ार
15  agent     agent_guide_apply                 —           —             screen, home
16  customer  customer_report_done              —           —             —
17  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
18  customer  customer_agree                    —           —             —
19  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
24  customer  customer_request_wait             frustrated  —             नहीं हो रहा, नहीं हो, verify, minute
25  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, बताएं।
26  customer  customer_do_otp                   —           —             otp
27  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
28  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
29  customer  customer_state_employment_type    —           —             personal, professional
30  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
31  customer  customer_ask_question             —           —             loan, direct
32  agent     agent_answer_query                —           —             loan, offer, details, best, हिसाब
33  customer  customer_acknowledge              —           —             —
34  agent     agent_ask_employment_type         —           —             salaried, self-employ, self, employment, type
35  customer  customer_state_employment_type    —           —             self employ, self employee, self, employee
36  agent     agent_request_income              —           —             income, बताएं।, जाए, fill, monthly
37  customer  customer_request_wait             —           —             minute, डाल, detail
38  agent     agent_wait                        —           —             इंतज़ार
39  customer  customer_provide_email            —           —             email, personal, address
40  agent     agent_request_email               —           —             email, personal, enter, address, know
41  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
42  customer  customer_provide_address          —           —             building, flat, number, name, मांग
43  agent     agent_request_address             —           —             address, pincode, locality, building, house number
44  customer  customer_acknowledge              —           —             —
45  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
46  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
47  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो
48  customer  customer_report_address_error     —           —             building
49  agent     agent_help_address_error          —           —             building, सही, चेक, दिक्कत, डालें
50  customer  customer_acknowledge              —           —             —
51  agent     agent_help_address_error          —           —             building, दिक्कत
52  customer  customer_report_done              —           —             हो गया, process
53  agent     agent_request_terms_accept        —           —             करें।, button, proceed, click
54  customer  customer_ask_question             —           —             —
55  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
56  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
57  customer  customer_ask_question             —           —             organization, डालना
58  agent     agent_request_org_name            —           —             organization, offer, पूरा, salary, डालें
59  customer  customer_ask_question             —           —             monthly, income
60  agent     agent_request_income              —           —             income, home, monthly, net, salary
61  customer  customer_ask_question             —           —             number, आगे, लगेगा
62  agent     agent_answer_query                —           —             करें।, number, address, fill, official
63  customer  customer_ask_question             frustrated  —             नहीं हो
64  agent     agent_answer_query                —           —             process, number, details, आगे, fill
65  customer  customer_report_done              —           —             हो गया, process
66  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
67  customer  customer_respond_udyam            —           —             उद्यम, number, मांग
68  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
69  customer  customer_skip_udyam               —           —             —
70  agent     agent_request_udyam               —           —             udyam, number
71  customer  customer_skip_udyam               —           —             —
72  agent     agent_offer_skip_udyam            —           —             skip, number, click, आगे, option
73  customer  customer_report_done              —           —             आगे, बढ़
74  agent     agent_request_otp                 —           —             otp, verify
75  customer  customer_request_wait             —           —             wait
76  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, इंतज़ार
77  customer  customer_react_to_final_offer     —           —             लाख, हज़ार, रुपए, पांच
78  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
79  customer  customer_react_to_final_offer     —           —             loan, लाख, हज़ार, रुपए, पांच
80  agent     agent_present_final_offer         —           —             final, page
81  customer  customer_react_to_final_offer     —           —             loan, offer, final, page
82  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
83  customer  customer_report_done              —           —             —
84  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
85  customer  customer_request_wait             —           —             minute
```

## Call 52b52766 (transferred) — 57 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बताएं
3   customer  customer_query_fee                —           —             बताएं, interest, rate
4   agent     agent_send_sms_link               —           send_sms      sms, offer, करें।, final, application
5   agent     agent_guide_open_link             —           —             sms, करें।, link, click
6   customer  customer_report_sms_received      —           —             message
7   agent     agent_wait                        —           —             wait, sms, करें।, कृपया, बताएं।
8   customer  customer_report_sms_received      —           —             message
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  customer  customer_express_distrust         —           —             जाए, छोड़
11  agent     agent_reassure_trust              —           —             हूँ।, process, समझ, continue, step
12  customer  customer_express_distrust         distrustful —             fraud
13  agent     agent_reassure_trust              —           —             sms, करें।, verify, page, capital
14  customer  customer_react_to_offer           —           —             लाख, congratulation, पांच
15  agent     agent_present_offer               —           —             loan offer, loan, offer, amount, process
16  customer  customer_agree                    —           —             correct
17  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
18  customer  customer_report_done              —           —             हो गया, complete
19  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_personal_details    —           —             page, details, type, basic, होंगी।
22  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, सबसे
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
27  agent     agent_request_address             —           —             address, pincode, locality, building, house number
28  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
29  customer  customer_accept_terms             —           —             दोनों
30  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
31  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
32  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो, आगे, continue
33  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
34  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो, proceed
35  agent     agent_help_address_error          —           —             error, करें।, कृपया, proceed, monthly
36  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
37  customer  customer_provide_address          —           —             house number, flat, number, house
38  agent     agent_request_otp                 —           —             otp, करें।, verify, number, बताएं।
39  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो, button, proceed, name
40  agent     agent_help_address_error          —           —             करें।, कृपया, button, check, proceed
41  customer  customer_state_employment_type    —           —             self employ, self employee, self, employee
42  agent     agent_request_income              —           —             income, बताएं।, जाए, fill, monthly
43  agent     agent_request_business_details    —           —             business, company
44  customer  customer_report_done              —           —             हो गया
45  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, address
46  customer  customer_respond_udyam            —           —             —
47  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
48  customer  customer_skip_udyam               —           —             number, उद्यम
49  agent     agent_offer_skip_udyam            —           —             skip, number, click, option, udyam
50  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
51  customer  customer_request_wait             —           —             call, कृपया, line, hold, speaking
52  agent     agent_wait                        —           —             इंतज़ार
53  customer  customer_acknowledge              —           —             —
54  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
55  customer  customer_query_fee                —           —             point, two, five, उन्नीस
56  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, relationship, manager, सही
```

## Call 52bf189e (transferred) — 69 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             बात कर रही, से बात, बोल, आदित्य, बिरला
2   customer  customer_agree                    —           —             बोलिए
3   customer  customer_provide_personal_details —           —             —
4   agent     agent_answer_query                —           —             loan, बोल, हूँ।, application, शुरू
5   customer  customer_acknowledge              —           —             record, call, now, बोलिए, recorded
6   agent     agent_send_sms_link               —           send_sms      sms, loan, application, process, link
7   customer  customer_greet                    —           —             hello, आदित्य, capital, बोलिए
8   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
9   customer  customer_ask_question             —           —             कीजिए, speaker, हमसे
10  agent     agent_guide_open_link             —           —             loan, sms, हूँ।, देख, application
11  customer  customer_report_sms_received      —           —             देख
12  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
13  customer  customer_acknowledge              —           —             देख
14  agent     agent_request_otp                 —           —             करें।, number, mobile, enter
15  customer  customer_ask_question             —           —             click, दूं
16  agent     agent_request_otp                 —           —             number, mobile, enter
17  customer  customer_ask_question             —           —             click, दूं
18  agent     agent_request_otp                 —           —             number, mobile, आगे, enter, बढ़ें।
19  customer  customer_report_done              —           —             click, आगे, बढ़
20  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
21  customer  customer_report_done              —           —             कर दिया
22  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
25  customer  customer_report_done              —           —             कर दिया, minute, रुकिए
26  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
27  customer  customer_report_done              —           —             कर दिया
28  agent     agent_request_address             —           —             address, fill
29  customer  customer_ask_question             —           —             registered
30  agent     agent_request_address             —           —             address, pincode, locality, building, house number
31  customer  customer_ask_question             —           —             आदित्य, registered
32  agent     agent_request_address             —           —             address, करें।, कृपया, fill, current
33  customer  customer_acknowledge              —           —             —
34  agent     agent_request_terms_accept        —           —             terms and condition, terms, conditions, checkboxes
35  customer  customer_acknowledge              —           —             —
36  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
37  customer  customer_accept_terms             —           —             proceed, बोलिए
38  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
39  customer  customer_state_employment_type    —           —             salary
40  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
41  customer  customer_report_done              —           —             कर दिया
42  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
43  customer  customer_report_done              —           —             कर दिया
44  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
45  customer  customer_report_done              —           —             कर दिया, उसको
46  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
47  customer  customer_report_done              —           —             कर दिया
48  agent     agent_request_business_details    —           —             address, fill, pincode, organization, office
49  customer  customer_report_done              —           —             कर दिया
50  agent     agent_acknowledge                 —           —             —
51  customer  customer_do_otp                   —           —             दिए, six, digit
52  agent     agent_request_terms_accept        —           —             करें।, button, proceed, click
53  customer  customer_report_done              —           —             कर दिया, खुल, सामने
54  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
55  customer  customer_report_done              —           —             कर दिया, एकदम
56  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
57  customer  customer_acknowledge              —           —             —
58  agent     agent_wait                        —           —             loan, offer, करें।, मदद, कृपया
59  customer  customer_agree                    —           —             —
60  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
61  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, relationship, manager, connect
62  customer  customer_agree                    —           —             कीजिए, एकदम
63  customer  customer_acknowledge              —           —             call
64  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
65  customer  customer_agree                    —           —             कीजिए
66  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
67  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
68  agent     agent_end_call                    —           —             जवाब
```

## Call 53797d20 (transferred) — 41 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   customer  customer_agree                    —           —             करिए
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, करें।, link, click
6   customer  customer_acknowledge              —           —             —
7   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
8   customer  customer_report_done              —           —             हो गया
9   agent     agent_request_otp                 —           —             करें।, number, terms, mobile, conditions
10  customer  customer_report_done              —           —             हो गया
11  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
12  customer  customer_do_otp                   —           —             otp
13  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, जाएगा।
14  customer  customer_do_otp                   —           —             otp
15  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
16  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
17  customer  customer_ask_question             —           —             otp, time, इतना, किधर, लगता
18  agent     agent_request_otp                 —           send_otp      otp, offer, final, verify, शुरू
19  customer  customer_ask_question             —           —             email
20  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
21  customer  customer_ask_question             —           —             number, email, full, box, ऊपर
22  agent     agent_answer_query                —           —             otp, कृपया, verify, बताएं।, email
23  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, समाप्त, जवाब
24  customer  customer_report_done              —           —             हो गया, अरे
25  agent     agent_guide_apply                 —           —             करें।, कृपया, button, proceed, click
26  customer  customer_acknowledge              —           —             —
27  agent     agent_request_terms_accept        —           —             करें।, details, button, proceed, click
28  customer  customer_request_wait             —           —             minute, line
29  agent     agent_wait                        —           —             इंतज़ार
30  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
31  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, समाप्त, जवाब
32  customer  customer_acknowledge              —           —             online
33  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
34  customer  customer_skip_udyam               —           —             details, fill, मांग, आधार, उद्यम
35  agent     agent_offer_skip_udyam            —           —             skip, कृपया, application, number, click
36  customer  customer_request_wait             —           —             wait, दिखा
37  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, इंतज़ार
38  customer  customer_react_to_final_offer     —           —             loan, amount, lakh, दिखा, one
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
40  customer  customer_other                    —           —             —
```

## Call 5b805354 (transferred) — 56 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             sorry, again, say
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_request_wait             —           —             minute
3   agent     agent_wait                        —           —             इंतज़ार
4   customer  customer_agree                    —           —             बोलिए
5   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
6   customer  customer_agree                    —           —             tell
7   customer  customer_react_to_offer           —           —             lakh, कितना, seven
8   agent     agent_present_offer               —           —             pre approved, apply, approved, pre, amount
9   customer  customer_query_fee                —           —             interest, what
10  agent     agent_answer_query                —           —             loan, sms, approved, amount, हूँ।
11  agent     agent_send_sms_link               —           send_sms      sms, कृपया, application, process, रखें
12  customer  customer_report_sms_received      —           —             message, got
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, करें।, कृपया, खुल
14  customer  customer_report_applied           —           —             apply now, apply, now
15  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, मदद
16  customer  customer_do_otp                   —           —             number, mobile, five, eight
17  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, process
18  customer  customer_provide_personal_details —           —             gender, number, personal, details, आगे
19  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, page
20  agent     agent_request_email               —           —             email, कृपया, complete, personal, details
21  agent     agent_request_address             —           —             address, locality, building, house number, flat
22  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, complete, proceed
23  customer  customer_greet                    —           —             hello
24  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, proceed, आगे
25  customer  customer_provide_address          —           —             address
26  agent     agent_request_address             —           —             address, locality, building, house number, flat
27  customer  customer_request_wait             —           —             just
28  agent     agent_acknowledge                 —           —             हूँ।, सुन
29  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, conditions, proceed
30  customer  customer_request_wait             —           —             minute, just
31  agent     agent_wait                        —           —             इंतज़ार
32  agent     agent_request_terms_accept        —           —             कृपया, proceed, आगे, बताएं, ताकि
33  customer  customer_provide_income           —           —             income, personal, monthly, salary
34  agent     agent_ask_employment_type         —           —             मदद, कृपया, page, details, employment
35  customer  customer_state_employment_type    —           —             details, employment, पुछ
36  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, page, details
37  customer  customer_state_employment_type    —           —             salaried
38  agent     agent_request_income              —           —             income, करें।, कृपया, details, आगे
39  agent     agent_request_business_details    —           —             करें।, शुरू, नीचे, terms, जाए
40  agent     agent_request_otp                 —           —             otp, कृपया, verify, बताएं।, check
41  customer  customer_ask_question             —           —             email, official, organization, company, डालना
42  agent     agent_answer_query                —           —             मदद, email, बताएं, ताकि, official
43  customer  customer_acknowledge              —           —             —
44  agent     agent_request_email               —           —             email, कृपया, बताएं।, आगे, official
45  agent     agent_request_business_details    —           —             करें।, आगे, address, बताएं, सही
46  customer  customer_report_address_error     —           —             enter, code, pin, valid
47  customer  customer_report_address_error     —           —             enter, code, pin, बोलकर, service
48  agent     agent_help_address_error          —           —             कृपया, complete, जाए, आगे, बताएं
49  customer  customer_report_done              —           —             हो गया, complete
50  agent     agent_request_terms_accept        —           —             कृपया, proceed, आगे, बताएं, ताकि
51  agent     agent_wait                        —           —             loan, offer, कृपया, बताएं।, इंतज़ार
52  agent     agent_present_final_offer         —           —             loan, offer, approved, pre, amount
53  customer  customer_react_to_final_offer     —           —             loan, apply, personal, lakh, instant
54  agent     agent_present_final_offer         —           —             समझती, जरूरत
55  customer  customer_react_to_final_offer     —           —             amount, final
```

## Call 5d2f1ea1 (transferred) — 38 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, करें।, link, click
6   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
7   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
8   agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
9   agent     agent_request_personal_details    —           —             हूँ।, मदद, otp, verify, personal
10  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
11  customer  customer_report_done              —           —             हो गया
12  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
13  customer  customer_report_done              —           —             हो गया
14  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
15  customer  customer_report_done              —           —             हो गया
16  agent     agent_request_address             —           —             address, pincode, locality, building, house number
17  customer  customer_ask_question             —           —             —
18  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
19  customer  customer_report_done              —           —             हो गया
20  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
21  customer  customer_state_employment_type    —           —             salary
22  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
23  customer  customer_state_employment_type    —           —             employee
24  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_terms_accept        —           —             करें।, details, button, proceed, click
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 5e6f5156 (transferred) — 92 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             record, call, now, recorded
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             बोलिए
5   customer  customer_agree                    —           —             बोलिए
6   agent     agent_send_sms_link               —           send_sms      sms, हूँ।, कृपया, application, जिसमें
7   agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, भेज, मिल
8   customer  customer_ask_question             —           —             —
9   agent     agent_send_sms_link               —           —             sms, हूँ।, मदद, कृपया, आगे
10  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
11  customer  customer_react_to_offer           —           —             personal loan, loan, apply, now, personal
12  agent     agent_guide_apply                 —           —             apply now, apply, now, हूँ।, मदद
13  customer  customer_do_otp                   —           —             number, mobile
14  agent     agent_request_otp                 —           —             कृपया, process, बताएं।, आगे, ताकि
15  customer  customer_acknowledge              —           —             —
16  agent     agent_request_otp                 —           —             मदद, कृपया, बताएं।, सही, पूरा
17  customer  customer_do_otp                   —           —             number, पता, डाला
18  agent     agent_answer_query                —           —             loan, कृपया, बताएं।, नंबर, डाल
19  customer  customer_report_done              —           —             डाल
20  agent     agent_request_terms_accept        —           —             terms and condition, terms, otp, कृपया, नीचे
21  customer  customer_do_otp                   —           —             otp
22  agent     agent_request_otp                 —           —             otp, मदद, कृपया, verify, जाए
23  customer  customer_do_otp                   —           —             otp, पच्चीस, डालता
24  agent     agent_request_otp                 —           —             otp, verify, पूरी, लें, प्रक्रिया
25  customer  customer_provide_pan              —           —             pan, number, name, full, दिखा
26  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, आगे
27  customer  customer_ask_question             —           —             चलेगा, लिखना
28  agent     agent_answer_query                —           —             कृपया, बताएं।, पैन, समझ, सही
29  customer  customer_provide_pan              —           —             number
30  agent     agent_request_pan                 —           —             पैन, आगे, बताएं, ताकि, बढ़
31  customer  customer_report_address_error     —           —             error, name, building
32  agent     agent_help_address_error          —           —             error, मदद, कृपया, address, name
33  customer  customer_report_address_error     —           —             —
34  agent     agent_request_terms_accept        —           —             terms, करें।, कृपया, बढ़िया, अगला
35  customer  customer_acknowledge              —           —             —
36  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, proceed, आगे
37  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो, click
38  agent     agent_help_address_error          —           —             error, नहीं हो रहा, करें।, हूँ।, मदद
39  customer  customer_report_done              —           —             हो गया, name, बोलो, दिखा, original
40  agent     agent_request_terms_accept        —           —             मदद, जाए, proceed, आगे, बताएं
41  customer  customer_provide_income           —           —             income, monthly
42  agent     agent_request_income              —           —             income, करें।, कृपया, रखें, बताएं।
43  customer  customer_provide_personal_details —           —             name, पूरा, डालने, original
44  agent     agent_request_personal_details    —           —             कृपया, application, बताएं।, name, सही
45  agent     agent_request_income              —           —             income, कृपया, details, आगे, monthly
46  customer  customer_report_done              —           —             डाल, लिख
47  agent     agent_request_personal_details    —           —             मदद, आगे, बताएं, सही, जैसा
48  customer  customer_report_done              —           —             हो गया
49  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, self, employment
50  customer  customer_ask_question             —           —             minute
51  agent     agent_ask_employment_type         —           —             कृपया, आगे, employment, type, बताएं
52  customer  customer_state_employment_type    —           —             government, private
53  agent     agent_ask_employment_type         —           —             salaried, मदद, कृपया, आगे, बताएं
54  customer  customer_report_done              —           —             हो गया, process, नीचे, लिखा
55  agent     agent_request_income              —           —             income, कृपया, monthly, बढ़िया, टाइप
56  customer  customer_provide_business_details —           —             code, pin, डालिए
57  agent     agent_request_business_details    —           —             करें।, कृपया, आगे, बताएं, सही
58  customer  customer_report_done              —           —             हो गया, process, दूं
59  agent     agent_request_terms_accept        —           —             मदद, कृपया, proceed, बताएं, अगली
60  agent     agent_ask_to_repeat               —           —             एक बार फिर, कृपया, कीजिए, माफ़, कहेंगे
61  customer  customer_other                    —           —             five, second, four
62  agent     agent_wait                        —           —             loan, offer, कृपया, समय, बताएं।
63  customer  customer_report_done              —           —             खुल
64  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
65  customer  customer_do_otp                   —           —             otp, loan, apply, number, mobile
66  agent     agent_request_otp                 —           —             otp, कृपया, बताएं।, समझ, मिल
67  customer  customer_report_applied           —           —             apply now, apply, now, ऊपर
68  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, हूँ।
69  customer  customer_report_applied           —           —             खुल
70  agent     agent_guide_apply                 —           —             मदद, कृपया, आगे, बताएं, ताकि
71  customer  customer_provide_pan              —           —             pan, name, full, card, tick
72  agent     agent_request_pan                 —           —             पैन, कृपया, terms, conditions, आगे
73  customer  customer_acknowledge              —           —             कीजिए, note
74  agent     agent_request_pan                 —           —             पैन, हूँ।, मदद, कृपया, details
75  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
76  customer  customer_report_done              —           —             हो गया
77  agent     agent_acknowledge                 —           —             बढ़िया।
78  customer  customer_ask_question             —           —             continue
79  agent     agent_request_terms_accept        —           —             करें।, मदद, proceed, आगे, बताएं
80  customer  customer_report_done              —           —             continue
81  agent     agent_confirm                     —           —             मदद, कृपया, आगे, बताएं, ताकि
82  customer  customer_acknowledge              —           —             detail
83  agent     agent_request_personal_details    —           —             loan, कृपया, process, details, आगे
84  customer  customer_react_to_final_offer     —           —             amount, confirmation, lakh, one, लिखा
85  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
86  customer  customer_react_to_final_offer     —           —             loan, offer, personal, लाख
87  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
88  customer  customer_react_to_final_offer     —           —             loan, offer, नीचे, lakh, one
89  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, offer, amount, मदद
90  customer  customer_agree                    —           —             छोड़
91  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, कृपया, relationship, manager
```

## Call 606af2e2 (transferred) — 67 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             chd
2   customer  customer_other                    —           —             phone, बोलो, बोलता
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_other                    —           —             loan
5   agent     agent_present_offer               —           —             loan, amount, application, guide, documents
6   customer  customer_other                    —           —             loan
7   agent     agent_present_offer               —           —             pre-approved, offer, approved, pre, मदद
8   customer  customer_other                    —           —             loan, call, number, phone, इधर
9   agent     agent_confirm                     —           —             हूँ।, मदद, application, link, complete
10  customer  customer_other                    —           —             call, लगा, माधव
11  agent     agent_greet                       —           —             बोल, हूँ।, मदद, application, तरफ
12  customer  customer_other                    —           —             छोड़, लोगों, मान, दूंगा
13  agent     agent_confirm                     —           —             हूँ।, कृपया, application, आगे, पूरा
14  customer  customer_other                    —           —             समझती
15  agent     agent_acknowledge                 —           —             हूँ।, कृपया, समझती
16  customer  customer_other                    —           —             समझती
17  agent     agent_acknowledge                 —           —             loan, हूँ।, मदद, application, समझती
18  customer  customer_other                    —           —             समझती, अरे
19  agent     agent_acknowledge                 —           —             loan, हूँ।, मदद, समझती
20  customer  customer_greet                    —           —             hello, बोलिए, समझा
21  agent     agent_present_offer               —           —             loan, हूँ।, मदद, application, पूरा
22  customer  customer_agree                    confused    —             कैसे
23  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, शुरू, process
24  agent     agent_send_sms_link               —           send_sms      sms, application, process, जिसमें, भेज
25  customer  customer_report_done              —           —             कर दिया, इसी
26  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
27  customer  customer_report_done              —           —             देख
28  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
29  customer  customer_report_done              —           —             कर दिया, click, उसमें
30  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
31  customer  customer_report_done              —           —             कर दिया
32  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_personal_details    —           —             कृपया, personal, details, आगे, बताएं
35  customer  customer_agree                    —           —             तैयार, एकदम
36  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
37  customer  customer_report_done              —           —             भर दिया, कर दिया
38  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
39  customer  customer_report_done              —           —             हो गया, कर दिया
40  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
41  customer  customer_report_done              —           —             हो गया, कर दिया
42  agent     agent_request_address             —           —             address, pincode, locality, building, house number
43  customer  customer_report_done              —           —             कर दिया
44  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
45  customer  customer_accept_terms             —           —             check
46  agent     agent_ask_employment_type         —           —             loan, offer, page, details, employment
47  customer  customer_report_done              —           —             भर दिया, बोलिए
48  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, self, employment
49  customer  customer_state_employment_type    —           —             self employ, self, employed
50  agent     agent_request_income              —           —             income, बताएं।, जाए, fill, monthly
51  customer  customer_report_done              —           —             कर दिया
52  agent     agent_request_org_name            —           —             बताएं।, जाए, enter, registered, business
53  customer  customer_report_done              —           —             कर दिया, डाल
54  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, address
55  customer  customer_report_done              —           —             कर दिया
56  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
57  customer  customer_acknowledge              —           —             —
58  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
59  customer  customer_report_done              —           —             हो गया, भर दिया
60  agent     agent_confirm                     —           —             आगे बढ़, मदद, आगे, बढ़ना, चाहते
61  customer  customer_acknowledge_transfer     —           —             call, बोलो, senior
62  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, हूँ।
63  customer  customer_react_to_final_offer     —           —             दिख, एकदम
64  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
65  customer  customer_acknowledge_transfer     —           —             देख, पूछना, senior, कराओ
66  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 6187fa3c (transferred) — 56 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             बोलिए
5   customer  customer_request_wait             —           —             minute, just
6   agent     agent_wait                        —           —             इंतज़ार
7   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
8   agent     agent_guide_open_link             —           —             sms, करें।, link, click
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  customer  customer_request_wait             —           —             wait
11  agent     agent_wait                        —           —             इंतज़ार
12  customer  customer_ask_question             —           —             आगे
13  agent     agent_guide_apply                 —           —             apply now, apply, now, नीचे, button
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
16  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
17  agent     agent_request_otp                 —           —             otp, verify
18  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
19  customer  customer_request_wait             —           —             wait
20  agent     agent_wait                        —           —             इंतज़ार
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
22  customer  customer_acknowledge              —           —             —
23  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
24  customer  customer_acknowledge              —           —             —
25  agent     agent_request_address             —           —             address, pincode, locality, building, house number
26  customer  customer_request_wait             —           —             wait
27  agent     agent_wait                        —           —             इंतज़ार
28  customer  customer_report_done              —           —             कर दिया
29  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
30  customer  customer_report_address_error     —           —             proceed, option
31  agent     agent_help_address_error          —           —             red, error, करें।, कृपया, check
32  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
33  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
34  customer  customer_request_wait             —           —             wait
35  agent     agent_wait                        —           —             इंतज़ार
36  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
39  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
40  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
41  customer  customer_request_wait             —           —             wait
42  agent     agent_wait                        —           —             इंतज़ार
43  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
44  customer  customer_request_wait             —           —             wait
45  agent     agent_wait                        —           —             इंतज़ार
46  agent     agent_request_terms_accept        —           —             करें।, details, button, proceed, click
47  customer  customer_request_wait             —           —             wait
48  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
49  customer  customer_request_wait             —           —             wait
50  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
51  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
52  customer  customer_report_done              —           —             page, खुल, दुबारा
53  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
54  customer  customer_react_to_final_offer     —           —             page, खुल, बारह
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, कृपया, process
```

## Call 65d3a240 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलो
3   customer  customer_ask_question             —           —             digital
4   agent     agent_answer_query                —           —             apply, sms, process, भेज, link
5   customer  customer_agree                    —           —             भेज
6   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   customer  customer_report_link_opened       —           —             sms, link, open
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  customer  customer_acknowledge              —           —             —
11  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
12  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
13  agent     agent_request_otp                 —           —             otp, verify
14  customer  customer_do_otp                   —           —             verify
15  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
16  customer  customer_report_done              —           —             हो गया
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_address             —           —             address, pincode, locality, building, house number
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
26  customer  customer_report_done              —           —             हो गया
27  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
28  customer  customer_state_employment_type    —           —             select, salary
29  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
30  customer  customer_report_done              —           —             —
31  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
34  customer  customer_report_done              —           —             डाल
35  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
38  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
41  customer  customer_report_done              —           —             हो गया
42  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
43  customer  customer_react_to_final_offer     —           —             देख
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 696e940c (transferred) — 49 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बोल, आदित्य, बिरला, कैपिटल
2   customer  customer_provide_personal_details —           —             —
3   agent     agent_request_personal_details    —           —             कृपया, पैन, बताएं, पूरा, जैसा
4   customer  customer_provide_personal_details —           —             —
5   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
6   customer  customer_agree                    —           —             बोलो
7   customer  customer_ask_question             confused    —             कैसे, emi, वापस
8   customer  customer_greet                    —           —             hello
9   agent     agent_explain_fee                 —           —             interest rate, offer, sms, final, application
10  agent     agent_ask_to_repeat               —           —             माफ़
11  customer  customer_acknowledge              —           —             —
12  agent     agent_guide_open_link             —           —             sms, link
13  customer  customer_report_link_opened       —           —             करवा, उधर
14  agent     agent_guide_open_link             —           —             sms, application, link, complete, सही
15  customer  customer_unclear                  —           —             sorry
16  agent     agent_guide_open_link             —           —             sms, करें।, link, click
17  agent     agent_guide_open_link             —           —             sms, करें।, हूँ।, application, शुरू
18  customer  customer_report_sms_received      —           —             sms, link
19  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, process, link
20  customer  customer_report_sms_received      —           —             message
21  agent     agent_send_sms_link               —           send_sms      sms, हूँ।, कृपया, समय, भेज
22  customer  customer_report_sms_received      —           —             —
23  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
24  customer  customer_report_done              —           —             —
25  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
26  customer  customer_report_applied           —           —             apply
27  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
28  agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, कीजिए, माफ़, कहें
29  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो, भाई, भरे
30  agent     agent_request_otp                 —           send_otp      otp, करें।, हूँ।, मदद, number
31  customer  customer_do_otp                   —           —             number, mobile, डाल
32  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
33  customer  customer_do_otp                   —           —             otp, select, दोनों, box
34  agent     agent_request_otp                 —           —             otp, करें।, verify, बताएं।, जाए
35  agent     agent_ask_to_repeat               —           —             कृपया, कीजिए, माफ़, दोहरा
36  customer  customer_report_done              —           —             हो गया, भाई
37  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
38  customer  customer_react_to_final_offer     —           —             देख
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, कृपया, process
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
42  customer  customer_ask_question             —           —             —
43  agent     agent_greet                       —           —             बोल, हूँ।, तरफ, capital, aditya
44  customer  customer_acknowledge              —           —             call
45  agent     agent_guide_open_link             —           —             sms, करें।, हूँ।, application, शुरू
46  customer  customer_report_done              —           —             कर दिया
47  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, process, link
48  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
```

## Call 69b2ff40 (transferred) — 27 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_present_offer               —           —             बोल, capital, aditya, birla, देर
3   customer  customer_agree                    —           —             —
4   customer  customer_react_to_offer           —           —             —
5   customer  customer_ask_question             —           —             percent, कितने
6   agent     agent_explain_fee                 —           —             interest rate, loan, offer, sms, approved
7   customer  customer_ask_question             —           —             उसमें, दिखेगा
8   agent     agent_send_sms_link               —           send_sms      sms, loan, offer, amount, final
9   customer  customer_agree                    —           —             भेज
10  agent     agent_send_sms_link               —           send_sms      sms, कृपया, application, रखें, जिसमें
11  customer  customer_report_sms_received      —           —             देख, भेज, check, phone, लूंगा
12  agent     agent_send_sms_link               —           send_sms      sms, कृपया, भेज, बताएं, चेक
13  customer  customer_request_wait             —           —             minute
14  agent     agent_wait                        —           —             इंतज़ार
15  customer  customer_request_wait             —           —             minute
16  agent     agent_wait                        —           —             इंतज़ार
17  customer  customer_request_wait             —           —             hold
18  agent     agent_wait                        —           —             हूँ।, बताएं, तैयार, हों, यहीं
19  customer  customer_express_distrust         —           —             तरफ, link, second
20  agent     agent_reassure_trust              —           —             तरफ, capital, aditya, birla, लिंक
21  customer  customer_acknowledge              —           —             —
22  agent     agent_guide_open_link             —           —             लिंक पर क्लिक, sms, करें।, मदद, कृपया
23  customer  customer_react_to_offer           —           —             लाख, दिखा, सात
24  agent     agent_present_offer               —           —             pre approved, loan offer, personal loan, loan, offer
25  customer  customer_agree                    —           —             —
26  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, offer, हूँ।, मदद
```

## Call 6cd62134 (transferred) — 44 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
3   agent     agent_guide_open_link             —           —             sms, करें।, link, click
4   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
5   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
6   agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
7   agent     agent_request_otp                 —           —             otp, verify
8   agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
9   customer  customer_ask_question             —           —             उसमें, लगता
10  agent     agent_request_pan                 —           —             पैन, number, capital, type, card
11  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
12  customer  customer_report_done              —           —             हो गया
13  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
14  agent     agent_clarify                     —           —             कॉल
15  agent     agent_request_email               —           —             email, personal, enter, address, चुके
16  customer  customer_report_done              —           —             कर दिया
17  agent     agent_request_address             —           —             address, pincode, locality, building, house number
18  agent     agent_clarify                     —           —             कॉल
19  customer  customer_report_done              —           —             कर दिया
20  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
21  customer  customer_report_done              —           —             —
22  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
23  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
24  customer  customer_state_employment_type    —           —             salary
25  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
26  customer  customer_state_employment_type    —           —             job, private
27  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
30  agent     agent_ask_to_repeat               —           —             कॉल
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_email               —           —             official
33  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
34  agent     agent_clarify                     —           —             कॉल
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
37  customer  customer_report_done              —           —             कर दिया
38  agent     agent_guide_apply                 —           —             करें।, button, proceed, click
39  customer  customer_report_done              —           —             कर दिया
40  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
41  customer  customer_report_done              —           —             हो गया
42  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
43  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 6d27dee2 (transferred) — 61 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_express_distrust         —           —             —
3   agent     agent_reassure_trust              —           —             समय, लगेगा।, continue, चाहिए।
4   customer  customer_agree                    confused    —             कैसे
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
6   agent     agent_guide_open_link             —           —             sms, करें।, link, click
7   customer  customer_request_wait             —           —             minute
8   agent     agent_wait                        —           —             इंतज़ार
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  customer  customer_acknowledge              —           —             call
11  agent     agent_greet                       —           —             बोल, हूँ।, तरफ, capital, aditya
12  customer  customer_agree                    —           —             बोलिए
13  agent     agent_request_personal_details    —           —             page, details, type, basic, होंगी।
14  customer  customer_acknowledge              —           —             —
15  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, सबसे
16  customer  customer_ask_question             —           —             number, mobile, मांग
17  agent     agent_request_pan                 —           —             पैन, करें।, हूँ।, number, enter
18  agent     agent_request_pan                 —           —             पैन, कृपया, number, capital, type
19  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, समाप्त, जवाब
20  agent     agent_ask_to_repeat               —           —             सुन
21  customer  customer_greet                    —           —             hello
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
25  customer  customer_report_done              —           —             डाल, दिए
26  agent     agent_request_address             —           —             address, pincode, locality, building, house number
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
29  customer  customer_accept_terms             —           —             दिए
30  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
31  customer  customer_report_done              —           —             दिए
32  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
33  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
34  customer  customer_state_employment_type    —           —             self employ, self, employed
35  agent     agent_request_income              —           —             income, बताएं।, जाए, fill, monthly
36  agent     agent_request_org_name            —           —             बताएं।, जाए, enter, registered, business
37  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, address
38  customer  customer_report_done              —           —             हो गया
39  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
40  customer  customer_respond_udyam            —           —             number
41  agent     agent_offer_skip_udyam            —           —             skip, number, click, option, udyam
42  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
43  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
44  agent     agent_wait                        —           —             करें।, otp, कृपया, बताएं।, जाए
45  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
48  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
49  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, कहेंगे, दोबारा, कनेक्शन
50  agent     agent_acknowledge                 —           —             हूँ।, तरीके, simple, ज़रूर
51  customer  customer_acknowledge              —           —             —
52  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
53  customer  customer_react_to_final_offer     —           —             लाख, रुपया
54  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
56  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, कृपया, relationship
57  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, कनेक्शन, बोलेंगे
58  customer  customer_request_wait             —           —             line, बने
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, कृपया, relationship
60  agent     agent_transfer_to_rm              —           transfer_to_rmहूँ।, connect, समझ, बिल्कुल, करेंगे।
```

## Call 709d4cce (transferred) — 58 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             record, call, now, recorded
1   agent     agent_other                       —           —             chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             hello, capital, aditya, birla, कुमार
4   agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, apply
5   customer  customer_react_to_offer           —           —             eligibility, preapproved
6   agent     agent_present_offer               —           —             loan, amount, based
7   customer  customer_provide_address          —           —             address, आधार
8   customer  customer_provide_address          —           —             address, आधार
9   agent     agent_request_address             —           —             address, आधार, करें।, number, बताएं।
10  customer  customer_ask_question             —           —             number, address, आधार, दिखता, चालू
11  customer  customer_report_sms_received      —           —             link भेज, link, line, रहिए, देखते
12  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
13  agent     agent_guide_open_link             —           —             sms, link
14  customer  customer_acknowledge              —           —             देख
15  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
16  customer  customer_report_applied           —           —             apply now, apply, now, number, mobile
17  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
18  customer  customer_react_to_offer           —           —             लाख, congratulation, लिख
19  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
20  customer  customer_provide_pan              —           —             लाख, दिखा, मांग, pen
21  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
22  customer  customer_ask_question             —           —             देख, eligible, preapproved, लेते
23  agent     agent_answer_query                —           —             loan, offer, करें।, final, number
24  customer  customer_ask_question             —           —             भाई
25  agent     agent_request_personal_details    —           —             gender, date of birth, enter, पैन, name
26  customer  customer_provide_address          —           —             building, house number, flat, number, house
27  agent     agent_request_address             —           —             address, pincode, locality, building, house number
28  customer  customer_provide_address          —           —             house number, number, house, मिला, हाथ
29  agent     agent_request_address             —           —             sms, करें।, बताएं।, link, details
30  customer  customer_report_address_error     —           —             address, training, ऐसा, cannot, space
31  customer  customer_provide_address          —           —             locality, building, flat, street, दिए
32  customer  customer_provide_address          —           —             near
33  customer  customer_report_address_error     —           —             space, leading
34  customer  customer_provide_address          —           —             one, code, three, pin, eight
35  customer  customer_accept_terms             —           —             check, proceed, click, दिए, box
36  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
37  customer  customer_state_employment_type    —           —             monthly, employment, income, salary, दिए
38  agent     agent_ask_employment_type         —           —             employment, professional
39  customer  customer_provide_income           —           —             income, monthly
40  customer  customer_provide_org_name         —           —             organization, name, पुछ
41  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
42  customer  customer_provide_org_name         —           —             name
43  customer  customer_provide_org_name         —           —             government, india
44  customer  customer_provide_email            —           —             बोलिए, office, account, mail
45  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
46  customer  customer_provide_business_details —           —             address, बोलिए, official, organization, पुछ
47  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
48  customer  customer_report_done              —           —             offer, बिल्कुल, detail, checking
49  agent     agent_request_terms_accept        —           —             करें।, otp, verify, बताएं।, जाए
50  customer  customer_request_wait             —           —             application, button, done, hold, close
51  agent     agent_wait                        —           —             wait, application, button, done, close
52  customer  customer_react_to_final_offer     —           —             lakh, ten, congratulation
53  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
54  customer  customer_query_fee                —           —             processing fee, processing, fee
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, relationship, manager, सही
56  customer  customer_acknowledge              —           —             बोलिए
57  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, relationship, manager, सही
```

## Call 715e7ec7 (transferred) — 68 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_agree                    —           —             बोलो
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   customer  customer_react_to_offer           —           —             loan
4   agent     agent_explain_fee                 —           —             interest rate, interest, rate
5   customer  customer_other                    —           —             —
6   customer  customer_other                    —           —             देख, भैया
7   agent     agent_acknowledge                 —           —             समझ
8   customer  customer_ask_question             —           —             —
9   customer  customer_other                    —           —             loan
10  agent     agent_send_sms_link               —           send_sms      sms, हूँ।, जिसमें, भेज, link
11  customer  customer_other                    —           —             loan, भेज, ज़रूरी
12  agent     agent_send_sms_link               —           send_sms      sms, process, जिसमें, भेज, link
13  customer  customer_acknowledge              —           —             —
14  agent     agent_send_sms_link               —           —             sms, करें।, रखें, check
15  customer  customer_report_sms_received      —           —             भेज, check
16  agent     agent_guide_open_link             —           —             sms, करें।, link, click
17  customer  customer_report_link_opened       —           —             लिखा, देखा
18  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
19  customer  customer_other                    —           —             call, number, air
20  agent     agent_guide_apply                 —           —             apply now, apply, now, नीचे, button
21  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
22  customer  customer_acknowledge              —           —             —
23  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
24  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
25  customer  customer_other                    —           —             —
26  agent     agent_ask_to_repeat               —           —             फिर से कह, कहेंगे, क्षमा
27  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
28  customer  customer_acknowledge              —           —             —
29  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
30  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
31  customer  customer_other                    —           —             चार
32  customer  customer_other                    —           —             सात, पांच
33  customer  customer_ask_question             —           —             number, mobile, लाख, बाकी, करवा
34  agent     agent_guide_open_link             —           —             sms, करें।, process, link, complete
35  customer  customer_acknowledge              —           —             number, phone
36  agent     agent_greet                       —           —             बोल, हूँ।, तरफ, capital, aditya
37  customer  customer_ask_question             —           —             —
38  agent     agent_greet                       —           —             capital, aditya
39  customer  customer_ask_question             —           —             —
40  agent     agent_greet                       —           —             बोल, हूँ।, तरफ, capital, aditya
41  customer  customer_other                    —           —             —
42  agent     agent_guide_open_link             —           —             शुरू, process, link, click
43  customer  customer_agree                    —           —             शुरू, ज़रूरी, लोगों, बोलता, हमको
44  customer  customer_other                    —           —             loan, लेकर
45  agent     agent_confirm                     —           —             आगे बढ़, sms, जिसमें, भेज, आगे
46  customer  customer_agree                    —           —             loan, भेज, ज़रूरी, तैयार, अच्छी
47  agent     agent_send_sms_link               —           send_sms      sms, जिसमें, भेज
48  customer  customer_agree                    —           —             भेज
49  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, रखें, भेज
50  customer  customer_acknowledge              —           —             check
51  agent     agent_guide_open_link             —           —             sms, करें।, link, click
52  agent     agent_guide_apply                 —           —             apply now, apply, now, नीचे, screen
53  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, button
54  customer  customer_acknowledge              —           —             —
55  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
56  customer  customer_acknowledge              —           —             —
57  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
58  customer  customer_acknowledge              —           —             —
59  agent     agent_request_otp                 —           —             otp, कृपया, verify, बताएं।
60  customer  customer_do_otp                   —           —             otp
61  agent     agent_request_otp                 —           —             otp, verify
62  customer  customer_acknowledge              —           —             —
63  agent     agent_present_final_offer         —           —             loan, amount, final
64  customer  customer_acknowledge              —           —             —
65  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
66  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship
67  customer  customer_request_wait             —           —             minute
```

## Call 77bb4be2 (transferred) — 22 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello, से बात
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             —
5   customer  customer_agree                    —           —             बिल्कुल
6   agent     agent_send_sms_link               —           send_sms      sms, loan, कृपया, application, process
7   customer  customer_report_sms_received      —           —             मिल
8   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
9   agent     agent_guide_open_link             —           —             apply, sms, now, कृपया, देख
10  customer  customer_report_done              —           —             कर लिया, process
11  agent     agent_request_otp                 —           —             समझ, नंबर, मोबाइल, स्क्रीन, डालना
12  customer  customer_ask_query                —           —             दुबारा, ज़रूरत, द्वारा
13  agent     agent_answer_query                —           —             loan, offer, amount, final, देख
14  customer  customer_ask_question             —           —             आवाज़, sun
15  agent     agent_answer_query                —           —             हूँ।, मदद, कृपया, बताएं, किस
16  customer  customer_ask_query                —           —             दूं
17  customer  customer_ask_question             frustrated  —             कब तक, loan, approved, amount, application
18  agent     agent_answer_query                —           —             loan, amount, मदद, कृपया, process
19  customer  customer_react_to_final_offer     —           —             loan, application, complete, approval
20  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
21  customer  customer_react_to_final_offer     —           —             loan, amount, application, complete, हज़ार
```

## Call 78dbd7a8 (transferred) — 100 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_query_fee                —           —             emi, interest, कितना, कितने, महीने
5   agent     agent_explain_fee                 —           —             interest rate, offer, sms, final, शुरू
6   customer  customer_agree                    —           —             —
7   agent     agent_guide_open_link             —           —             करें।, link, click
8   customer  customer_report_sms_received      —           —             sms, minute, उसमें, ऐसे, देखना
9   agent     agent_wait                        —           —             इंतज़ार
10  customer  customer_request_wait             —           —             minute
11  agent     agent_wait                        —           —             इंतज़ार
12  customer  customer_report_link_opened       —           —             link, खोल
13  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
16  customer  customer_do_otp                   —           —             nine, one, six, eight, नब्बे
17  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
18  customer  customer_respond_udyam            —           —             उद्यम, बोलिए
19  agent     agent_request_udyam               —           —             उद्यम, number, नंबर, skip, registration
20  customer  customer_acknowledge              —           —             —
21  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
22  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
23  agent     agent_wait                        —           —             loan, offer, कृपया, इंतज़ार, सबसे
24  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
25  customer  customer_query_fee                —           —             ब्याज
26  agent     agent_explain_fee                 —           —             interest rate, interest, rate, point, ten
27  customer  customer_query_fee                —           —             हज़ार, fees
28  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, offer, हूँ।, final, शुरू
29  customer  customer_agree                    —           —             —
30  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
31  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
32  agent     agent_ask_to_repeat               —           —             फिर से कह, एक बार फिर, कीजिए, माफ़
33  customer  customer_acknowledge_transfer     —           —             कराइए, उनसे
34  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, करें।, हूँ।, कृपया, समय
35  customer  customer_query_fee                —           —             हज़ार, रुपए, इतना
36  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
37  customer  customer_query_fee                —           —             पसंद
38  customer  customer_query_fee                —           —             percent
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, relationship, manager, connect
40  customer  customer_ask_question             —           —             कितना, time
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
42  customer  customer_ask_question             —           —             धान
43  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship
44  customer  customer_agree                    —           —             —
45  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
46  customer  customer_query_fee                —           —             हज़ार, सत्तर, score, total, कितनी
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, offer, हूँ।, final, शुरू
48  customer  customer_query_fee                —           —             देख, चवालीस
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, relationship, manager, connect
50  customer  customer_query_fee                —           —             लाख, हज़ार, कितना, रुपए, पांच
51  customer  customer_acknowledge              —           —             —
52  customer  customer_query_fee                —           —             लाख, हज़ार, करवा, सोच, cut
53  agent     agent_acknowledge                 —           —             हूँ।, समझती
54  customer  customer_ask_question             —           —             हज़ार, कितना, time, रुपए, अरे
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
56  customer  customer_query_fee                —           —             इतना, साढ़े
57  customer  customer_query_fee                —           —             लाख, साढ़े
58  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
59  customer  customer_agree                    —           —             सही
60  customer  customer_ask_question             frustrated  —             कब तक, manager, line, पता, only
61  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
62  customer  customer_acknowledge              —           —             customer
63  customer  customer_acknowledge              frustrated  —             दोबारा, सही
64  customer  customer_other                    frustrated  —             दोबारा
65  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
66  customer  customer_acknowledge              —           —             दुबारा
67  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship
68  customer  customer_ask_question             —           —             loan, कितने, पैसे, सबको
69  customer  customer_query_fee                —           —             percent, confirm, ब्याज
70  customer  customer_acknowledge              —           —             दोनों, सही, पूरा, साल, उन्होंने
71  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, मदद, कृपया
72  customer  customer_ask_question             —           —             —
73  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
74  customer  customer_ask_question             —           —             connect, कितना, time, लगेगा, कराओ
75  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, मदद, कृपया, relationship
76  customer  customer_acknowledge_transfer     —           —             जल्दी, time, कराइए
77  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, मदद, कृपया, relationship
78  customer  customer_acknowledge              —           —             लगा, दूंगा
79  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, मदद, कृपया, relationship
80  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
81  customer  customer_ask_question             —           —             option
82  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, मदद, कृपया
83  customer  customer_ask_question             —           —             दिए, बोला, उससे
84  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, मदद, कृपया
85  customer  customer_query_fee                —           —             हज़ार, पूरी, कितना, रुपए, पांच
86  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
87  customer  customer_report_done              —           —             कर दिया
88  customer  customer_provide_pan              —           —             pan, number, connect, phone, account
89  customer  customer_acknowledge              —           —             —
90  customer  customer_ask_question             —           —             पता
91  customer  customer_acknowledge              —           —             —
92  customer  customer_acknowledge              —           —             phone, पांच, साल, लोगों
93  customer  customer_greet                    —           —             hello, line
94  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship
95  customer  customer_acknowledge              —           —             बोलो
96  agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
97  customer  customer_agree                    —           —             हमसे
98  customer  customer_greet                    —           —             hello
99  agent     agent_explain_fee                 —           —             interest rate, offer, sms, करें।, final
```

## Call 7986eb00 (transferred) — 41 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_greet                    —           —             —
5   agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, call
6   customer  customer_agree                    —           —             बोलिए
7   agent     agent_present_offer               —           —             loan, apply, हूँ।, मदद, शुरू
8   customer  customer_ask_question             —           —             आदित्य, उसको, correct
9   customer  customer_query_fee                —           —             monthly, कितना
10  customer  customer_ask_query                —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms, offer, final, application, शुरू
12  customer  customer_agree                    —           —             भेजिए
13  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
14  agent     agent_guide_open_link             —           —             sms, करें।, link, click
15  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
16  customer  customer_report_link_opened       —           —             open
17  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
18  customer  customer_report_link_opened       —           —             open
19  agent     agent_answer_query                —           —             करें।, link, check, try, internet
20  customer  customer_report_done              —           —             login, दिखा
21  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
22  customer  customer_acknowledge              —           —             —
23  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
24  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
25  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
26  customer  customer_acknowledge              —           —             दिखा
27  agent     agent_request_personal_details    —           —             name, full
28  customer  customer_greet                    —           —             hello
29  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
30  agent     agent_ask_to_repeat               —           —             फिर से कह, एक बार फिर, कीजिए, माफ़, कहेंगे
31  customer  customer_request_wait             —           —             रुकिए
32  agent     agent_wait                        —           —             इंतज़ार
33  customer  customer_ask_question             —           —             साल
34  agent     agent_ask_to_repeat               —           —             फिर से बता, कृपया, बताएं।, कीजिए, माफ़
35  customer  customer_react_to_final_offer     —           —             amount, otp, click, दिखा, इधर
36  customer  customer_react_to_final_offer     —           —             लाख, दिखा
37  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
38  customer  customer_react_to_final_offer     —           —             देख
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
40  customer  customer_acknowledge              —           —             —
```

## Call 799e5a0e (transferred) — 35 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   customer  customer_agree                    —           —             बोलो
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, link
6   customer  customer_acknowledge              —           —             —
7   agent     agent_guide_open_link             —           —             home
8   customer  customer_acknowledge              —           —             —
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  customer  customer_acknowledge              —           —             line
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
12  customer  customer_report_link_opened       —           —             link, अंदर
13  agent     agent_guide_open_link             —           —             apply, sms, करें।, now, नीचे
14  customer  customer_ask_question             —           —             number, डालना
15  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
16  customer  customer_do_otp                   —           —             otp
17  agent     agent_request_otp                 —           —             otp, verify, बताएं।, जाए, screen
18  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
19  customer  customer_react_to_offer           —           —             हज़ार, चार, साठ
20  agent     agent_request_otp                 —           —             otp, verify, screen, enter, अगली
21  customer  customer_do_otp                   —           —             otp, amount, enter
22  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, personal
23  customer  customer_react_to_final_offer     —           —             हज़ार, सात, चार, eligible
24  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
25  customer  customer_react_to_final_offer     —           —             loan, amount
26  agent     agent_explain_fee                 —           —             interest rate, loan, offer, amount, final
27  customer  customer_react_to_final_offer     —           —             loan, apply, amount, हज़ार, दिखेगा
28  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
29  customer  customer_agree                    —           —             —
30  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
31  customer  customer_provide_address          —           —             apply, number, डालता
32  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
33  customer  customer_acknowledge              —           —             —
34  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, कृपया, process
```

## Call 7e3575b7 (transferred) — 50 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए, आवाज़, cut
3   agent     agent_greet                       —           —             बोल, आदित्य, बिरला
4   customer  customer_agree                    —           —             बोलिए, बोलकर, sun
5   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
6   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   customer  customer_report_sms_received      —           —             call, message
9   agent     agent_send_sms_link               —           —             sms, कृपया, inbox
10  customer  customer_acknowledge              —           —             —
11  agent     agent_send_sms_link               —           —             sms, कृपया, inbox
12  customer  customer_report_sms_received      —           —             message
13  agent     agent_wait                        —           —             wait, sms, करें।, कृपया, जाएगा।
14  agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, कीजिए, माफ़, कहेंगे
15  customer  customer_agree                    —           —             बोलिए
16  agent     agent_send_sms_link               —           —             sms, समय, थोड़ा
17  customer  customer_report_sms_received      —           —             message
18  agent     agent_wait                        —           —             call, sms, कृपया, समय, link
19  agent     agent_ask_to_repeat               —           —             बोल, कीजिए, माफ़
20  customer  customer_other                    —           —             message
21  agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, कृपया, भेज
22  customer  customer_other                    —           —             sorry, message
23  agent     agent_send_sms_link               —           send_sms      sms, हूँ।, कृपया, भेज, देर
24  agent     agent_guide_open_link             —           —             apply, sms, करें।, now, link
25  customer  customer_report_link_opened       —           —             loan, link, दिख, उसमें, message
26  agent     agent_guide_apply                 —           —             apply now, loan, offer, apply, now
27  customer  customer_do_otp                   —           —             number, mobile, मांग
28  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
29  customer  customer_ask_question             —           —             —
30  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
31  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
32  customer  customer_provide_email            —           —             —
33  agent     agent_request_email               —           —             email, कृपया, personal, check, enter
34  customer  customer_ask_question             —           —             मालूम, पड़
35  agent     agent_request_email               —           —             email, कृपया, personal, check, enter
36  customer  customer_report_done              —           —             कर दिया
37  agent     agent_request_address             —           —             address, pincode, locality, building, house number
38  customer  customer_report_done              —           —             —
39  agent     agent_request_address             —           —             address, pincode, locality, building, house number
40  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
41  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
42  customer  customer_respond_udyam            —           —             number, mobile, मांग, registration
43  agent     agent_request_otp                 —           —             कृपया, number, mobile, enter, बताएं
44  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
45  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, click, enter
46  agent     agent_request_otp                 —           —             otp, करें।, verify, click, enter
47  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
48  customer  customer_acknowledge              —           —             —
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 7fd658f2 (transferred) — 73 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
3   agent     agent_ask_to_repeat               —           —             sorry, repeat
4   customer  customer_agree                    —           —             बोलिए
5   agent     agent_send_sms_link               —           —             नंबर, मोबाइल
6   customer  customer_acknowledge              —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, जिसमें, भेज
8   agent     agent_send_sms_link               —           send_sms      sms, कृपया, बताएं, मिल, लिंक
9   customer  customer_acknowledge              —           —             —
10  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, करें।, कृपया, खुल
11  customer  customer_report_link_opened       —           —             खुल गया, खुल
12  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
13  customer  customer_report_applied           —           —             apply now, apply, now
14  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, page
15  customer  customer_do_otp                   —           —             verify
16  agent     agent_clarify                     —           —             मदद, कृपया, बताएं, आपसे, होगा।
17  customer  customer_provide_pan              —           —             pan, name, full, card
18  agent     agent_request_pan                 —           —             पैन, कृपया, सबसे, बताएं, पूरा
19  customer  customer_provide_pan              —           —             number, पूरा, ten
20  agent     agent_request_personal_details    —           —             कृपया, बताएं।, पैन, पूरा, बढ़िया
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_address             —           —             कृपया, बताएं।, सही, पूरा, नंबर
25  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
26  customer  customer_report_done              —           —             हो गया
27  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, proceed, आगे
28  customer  customer_other                    —           —             आगे
29  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, details, self
30  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, self, बताएं
31  customer  customer_state_employment_type    —           —             salaried, salary
32  agent     agent_request_income              —           —             income, कृपया, home, monthly, net
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_org_name            —           —             organization, कृपया, बताएं, बढ़िया, टाइप
35  customer  customer_ask_question             —           —             मतलब, organization
36  agent     agent_request_org_name            —           —             organization, करें।, कृपया, टाइप, सवाल
37  agent     agent_ask_to_repeat               —           —             फिर से बता, कीजिए, माफ़
38  customer  customer_provide_org_name         —           —             —
39  agent     agent_request_email               —           —             email, कृपया, बताएं, पूरा, जाए।
40  customer  customer_acknowledge              —           —             उसमें
41  agent     agent_acknowledge                 —           —             समझती
42  customer  customer_ask_question             —           —             उसमें
43  agent     agent_answer_query                —           —             आगे, email, official, समझती, बढ़
44  customer  customer_provide_email            —           —             email, address, official
45  agent     agent_request_address             —           —             address, कृपया, बताएं, सही, पूरा
46  customer  customer_provide_org_name         frustrated  —             company name, नहीं हो रहा, नहीं हो, name, company
47  agent     agent_answer_query                —           —             कृपया, टाइप, सवाल, जहां, काम
48  customer  customer_report_done              —           —             दिए
49  agent     agent_request_address             —           —             कृपया, बताएं।, सही, बढ़िया, टाइप
50  customer  customer_report_done              —           —             हो गया
51  agent     agent_request_otp                 —           —             otp, करें।, कृपया, verify, नीचे
52  agent     agent_request_otp                 —           —             otp, कृपया, verify, आगे, बताएं
53  customer  customer_do_otp                   —           —             otp
54  agent     agent_wait                        —           —             मदद, otp, कृपया, समय, इंतज़ार
55  agent     agent_wait                        —           —             otp, कृपया, इंतज़ार, धन्यवाद।
56  customer  customer_acknowledge              —           —             आगे
57  agent     agent_acknowledge                 —           —             समझती
58  customer  customer_react_to_final_offer     —           —             lakh, one, two, thousand, three
59  agent     agent_clarify                     —           —             मदद, ताकि, पेज, ध्यान, सकूँ।
60  customer  customer_react_to_final_offer     —           —             loan, amount, select
61  agent     agent_present_final_offer         —           —             loan, amount, select, बिल्कुल, पेज
62  customer  customer_report_done              —           —             दिए, चुन
63  agent     agent_clarify                     —           —             बढ़िया, दिक्कत, अगले, पाए, स्टेप
64  customer  customer_request_wait             —           —             minute
65  agent     agent_wait                        —           —             इंतज़ार
66  customer  customer_react_to_final_offer     —           —             amount, select
67  agent     agent_present_final_offer         —           —             loan, amount, कृपया, आगे, select
68  customer  customer_ask_question             —           —             amount, select, minute, कितना
69  agent     agent_present_final_offer         —           —             ₹378000, 378000, loan, approved, pre
70  customer  customer_react_to_final_offer     —           —             one, two, three, eight, sixty
71  agent     agent_present_final_offer         —           —             ₹378000, 378000, loan, approved, pre
72  customer  customer_report_done              —           —             चुन
```

## Call 814513e5 (transferred) — 33 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, आपसे
4   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
5   customer  customer_greet                    —           —             नमस्ते
6   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, आपसे
7   customer  customer_agree                    —           —             आपसे
8   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
9   customer  customer_agree                    —           —             free
10  customer  customer_report_done              —           —             process, दिए, documents, approval, रखा
11  agent     agent_send_sms_link               —           send_sms      sms, link भेज, हूँ।, मदद, application
12  customer  customer_report_done              —           —             option, रखा, end
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, करें।, कृपया
14  customer  customer_ask_question             —           —             —
15  agent     agent_guide_open_link             —           —             हूँ।, कृपया, समय, बताएं, खुल
16  customer  customer_report_link_opened       —           —             खुल गया, link, खुल
17  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, तरफ
18  customer  customer_report_done              —           —             कर दिया
19  agent     agent_request_otp                 —           —             कृपया, number, mobile, screen, आगे
20  customer  customer_do_otp                   —           —             number, mobile, type
21  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
22  customer  customer_react_to_final_offer     —           —             apply, check, लाख, डाल, हज़ार
23  agent     agent_other                       —           —             continue, sorry, english, only, hindi
24  customer  customer_ask_question             —           —             process, receive, रखा, under
25  agent     agent_acknowledge                 —           —             मदद, application, शुरू, personal, details
26  customer  customer_report_done              —           —             detail, under, चुकी
27  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, details, आगे
28  customer  customer_report_done              —           —             हो गया, चुका
29  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
30  customer  customer_react_to_final_offer     —           —             दिख, तिरपन
31  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, मदद, process, relationship, manager
32  customer  customer_acknowledge              —           —             —
```

## Call 88699263 (transferred) — 40 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             —
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, कीजिए, कहेंगे, माफ
3   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
4   agent     agent_guide_open_link             —           —             sms, करें।, link, click
5   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, otp
6   customer  customer_acknowledge              —           —             just
7   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
8   customer  customer_acknowledge              —           —             —
9   agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
10  agent     agent_request_otp                 —           —             otp, verify
11  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
12  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
13  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
14  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
15  agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, माफ़, कहेंगे
16  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
17  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
18  agent     agent_request_address             —           —             address, pincode, locality, building, house number
19  customer  customer_report_done              —           —             हो गया
20  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
21  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
22  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
23  customer  customer_report_done              —           —             —
24  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, बताएं
25  agent     agent_ask_to_repeat               —           —             साफ़ बोल, माफ़, साफ़, बोलेंगे
26  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
27  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, कहेंगे, स्पष्ट
28  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
29  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
30  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
31  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
32  agent     agent_request_address             —           —             address, pincode, बताएं।, जाए, fill
33  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
34  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
35  agent     agent_request_otp                 —           —             otp, verify
36  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
37  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
38  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 8e975c75 (transferred) — 28 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, करें।, link, click
6   agent     agent_ask_to_repeat               —           —             सॉरी
7   customer  customer_acknowledge              —           —             —
8   agent     agent_greet                       —           —             बोल, हूँ।, तरफ, capital, aditya
9   agent     agent_ask_to_repeat               —           —             कृपया, कीजिए, माफ़
10  customer  customer_greet                    —           —             hello, बोलो
11  customer  customer_greet                    —           —             hello
12  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
13  agent     agent_guide_open_link             —           —             sms, करें।, link, click
14  agent     agent_guide_open_link             —           —             sms, क्लिक, लिंक, पाए
15  customer  customer_acknowledge              —           —             अरे
16  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
17  customer  customer_do_otp                   —           —             otp
18  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
19  customer  customer_do_otp                   —           —             otp
20  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
21  customer  customer_do_otp                   —           —             otp, send
22  agent     agent_request_otp                 —           —             otp, verify
23  customer  customer_do_otp                   —           —             five, three, six, eight, four
24  agent     agent_request_otp                 —           —             otp, मदद, कृपया, verify, आगे
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
27  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 8ed64c9d (transferred) — 43 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             बोला
3   agent     agent_greet                       —           —             नमस्ते
4   customer  customer_greet                    —           —             hello
5   agent     agent_greet                       —           —             बोल, बिल्कुल
6   customer  customer_agree                    —           —             —
7   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
8   customer  customer_agree                    —           —             —
9   agent     agent_greet                       —           —             सबसे, बिल्कुल
10  customer  customer_agree                    —           —             बोलिए
11  customer  customer_agree                    —           —             —
12  agent     agent_send_sms_link               —           send_sms      sms, लिंक भेज, कृपया, रखें, भेज
13  customer  customer_report_sms_received      —           —             मिल
14  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, करें।, कृपया
15  customer  customer_report_link_opened       —           —             खुल गया, खुल
16  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, मदद
17  customer  customer_report_done              —           —             हो गया
18  agent     agent_request_otp                 —           —             कृपया, बताएं।, आगे, ताकि, बढ़
19  customer  customer_report_done              —           —             डाल
20  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, नीचे, बताएं।
21  customer  customer_greet                    —           —             hello
22  agent     agent_request_otp                 —           —             otp, हूँ।, भरकर, पाए, सुन
23  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
24  customer  customer_request_wait             —           —             minute
25  agent     agent_wait                        —           —             इंतज़ार
26  agent     agent_request_otp                 —           —             otp, कृपया, verify, आगे, बताएं
27  customer  customer_do_otp                   —           —             verified
28  agent     agent_ask_employment_type         —           —             salaried, self-employ, self, employment, type
29  customer  customer_state_employment_type    —           —             self employ, self, employed
30  agent     agent_request_income              —           —             कृपया, बताएं।, समझ, पूरा, टाइप
31  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
32  agent     agent_request_income              —           —             income, now, enter, monthly, net
33  customer  customer_acknowledge              —           —             —
34  agent     agent_request_org_name            —           —             —
35  customer  customer_acknowledge              —           —             —
36  agent     agent_request_org_name            —           —             मदद, कृपया, आगे, बताएं, पूरा
37  customer  customer_report_done              —           —             कर दिया
38  agent     agent_request_business_details    —           —             कृपया, बताएं।, सही, पूरा, दिख
39  customer  customer_report_done              —           —             कर दिया
40  agent     agent_guide_apply                 —           —             loan, offer, करें।, कृपया, बताएं।
41  customer  customer_report_done              —           —             खुल
42  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, offer, amount, हूँ।
```

## Call 908e0eac (transferred) — 51 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             बोलिए
5   customer  customer_ask_query                —           —             account, कितने, बोले
6   agent     agent_send_sms_link               —           send_sms      sms, offer, करें।, final, application
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   customer  customer_request_wait             —           —             minute
9   agent     agent_wait                        —           —             इंतज़ार
10  customer  customer_report_link_opened       —           —             click
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
12  customer  customer_report_done              —           —             कर दिया
13  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
16  customer  customer_do_otp                   —           —             verify
17  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
18  agent     agent_wait                        —           —             इंतज़ार
19  customer  customer_provide_personal_details —           —             details, fill
20  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
21  customer  customer_acknowledge              —           —             —
22  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  customer  customer_report_done              —           —             हो गया, feel
26  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
29  customer  customer_state_employment_type    —           —             salaried
30  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
31  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
32  customer  customer_request_wait             —           —             रुकिए
33  agent     agent_wait                        —           —             इंतज़ार
34  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
37  customer  customer_report_done              —           —             हो गया
38  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
41  customer  customer_report_done              —           —             हो गया
42  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
43  customer  customer_ask_query                —           —             लाख
44  agent     agent_answer_query                —           —             loan, offer, amount, process, complete
45  customer  customer_agree                    —           —             proceed
46  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
47  customer  customer_report_done              —           —             हो गया
48  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
49  customer  customer_react_to_final_offer     —           —             final offer, offer, final, लाख
50  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 92641b40 (transferred) — 81 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             —
3   agent     agent_present_offer               —           —             तरफ, आदित्य, बिरला, कैपिटल
4   customer  customer_greet                    —           —             से बात
5   customer  customer_query_fee                —           —             interest rate, interest, rate
6   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   customer  customer_acknowledge              —           —             —
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, दोबारा
11  customer  customer_agree                    —           —             —
12  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
13  customer  customer_do_otp                   —           —             otp
14  agent     agent_request_otp                 —           send_otp      otp, कृपया, verify, number, बताएं।
15  customer  customer_do_otp                   —           —             otp, option, इधर
16  agent     agent_request_otp                 —           send_otp      otp, कृपया, page, number, terms
17  customer  customer_do_otp                   —           —             number, mobile, डाल, condition, term
18  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, get, terms
19  customer  customer_other                    —           —             option
20  agent     agent_answer_query                —           —             sms, करें।, कृपया, link, पूरी
21  agent     agent_wait                        —           —             इंतजार
22  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
23  customer  customer_do_otp                   —           —             otp
24  agent     agent_request_otp                 —           —             otp, verify
25  customer  customer_do_otp                   —           —             otp
26  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, बताएं।
27  customer  customer_acknowledge              —           —             phone
28  agent     agent_request_otp                 —           —             otp
29  customer  customer_ask_question             —           —             number, change
30  agent     agent_answer_query                —           —             otp, कृपया, verify, number, समय
31  customer  customer_acknowledge              —           —             seven
32  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
33  customer  customer_acknowledge              —           —             call
34  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
35  customer  customer_provide_pan              —           —             number
36  agent     agent_request_pan                 —           —             पैन, कृपया, number
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_pan                 —           —             पैन, कृपया, number, complete, fill
39  customer  customer_acknowledge              —           —             —
40  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
41  customer  customer_report_done              —           —             —
42  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
43  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
44  customer  customer_ask_question             —           —             कौन सा, address, चलेगा
45  agent     agent_request_address             —           —             current
46  customer  customer_provide_address          —           —             आधार, card
47  agent     agent_request_address             —           —             address, आधार, fill, सही, card
48  customer  customer_acknowledge              —           —             current
49  agent     agent_request_address             —           —             address, करें।, fill, current, residential
50  agent     agent_request_address             —           —             address, pincode, locality, building, house number
51  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
52  customer  customer_provide_address          —           —             —
53  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
54  customer  customer_ask_question             —           —             —
55  agent     agent_greet                       —           —             बोल, हूँ।, तरफ, terms, conditions
56  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
57  customer  customer_provide_address          —           —             address, डाल, रुको
58  agent     agent_wait                        —           —             इंतज़ार
59  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
60  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
61  customer  customer_report_done              —           —             जिसमें
62  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
63  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
64  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
65  customer  customer_acknowledge              —           —             —
66  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
67  customer  customer_provide_address          —           —             address, fill, hold, चुका
68  agent     agent_wait                        —           —             इंतज़ार
69  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
70  customer  customer_report_done              —           —             हो गया
71  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
72  customer  customer_react_to_final_offer     —           —             दिखा, emi
73  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
74  customer  customer_query_fee                —           —             processing fee, thousand, processing, four, fees
75  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
76  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
77  customer  customer_ask_question             —           —             —
78  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
79  customer  customer_acknowledge              —           —             —
80  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 92ef6aa2 (transferred) — 72 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   customer  customer_query_fee                —           —             interest
4   customer  customer_ask_question             confused    —             कैसे, शुरू, details
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
6   agent     agent_guide_open_link             —           —             sms, करें।, link, click
7   customer  customer_query_fee                —           —             interest
8   agent     agent_explain_fee                 —           —             interest rate, offer, sms, करें।, final
9   customer  customer_ask_query                —           —             loan, लाख, बोलिए, आपसे, चार
10  customer  customer_express_distrust         —           —             percent, कितना, six, पुछ, thirty
11  agent     agent_explain_fee                 —           —             interest rate, offer, sms, करें।, final
12  agent     agent_guide_open_link             —           —             हूँ।, मदद, link, click, आगे
13  customer  customer_report_link_opened       —           —             application, open, बोले
14  agent     agent_guide_open_link             —           —             sms, application, शुरू, link, click
15  customer  customer_report_link_opened       —           —             open
16  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
17  customer  customer_ask_question             —           —             details, भरना, पड़ेगा
18  agent     agent_answer_query                —           —             loan, offer, हूँ।, शुरू, details
19  customer  customer_query_fee                —           —             details, percent, कितना, देखा
20  agent     agent_explain_fee                 —           —             interest rate, शुरू, interest, rate, percent
21  customer  customer_query_fee                —           —             बोल, percent, point, बोलो, nine
22  agent     agent_explain_fee                 —           —             interest rate, offer, final, शुरू, interest
23  customer  customer_ask_question             confused    —             कैसे, पता, चलेगा
24  agent     agent_answer_query                —           —             loan, offer, sms, final, application
25  customer  customer_agree                    —           —             —
26  agent     agent_confirm                     —           —             हूँ।, मदद, बढ़िया, सवाल, बताइए।
27  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
28  customer  customer_request_wait             —           —             process, line, रहिए
29  agent     agent_wait                        —           —             इंतज़ार
30  customer  customer_express_distrust         —           —             personal, rate, बोला
31  agent     agent_reassure_trust              —           —             application, process, relationship, manager, complete
32  customer  customer_acknowledge              —           —             —
33  agent     agent_guide_apply                 —           —             मदद, application, process
34  customer  customer_other                    —           —             —
35  agent     agent_confirm                     —           —             कृपया, complete, बिल्कुल, जल्दी, दें।
36  customer  customer_ask_question             —           —             —
37  agent     agent_confirm                     —           —             कृपया, complete, बिल्कुल, जल्दी, दें।
38  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
39  customer  customer_greet                    —           —             hello
40  agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
41  customer  customer_provide_email            —           —             email, personal, डालना, बोला
42  agent     agent_request_email               —           —             email, application, personal, check, address
43  customer  customer_ask_question             —           —             कौन सा, personal, professional
44  agent     agent_request_email               —           —             email, personal, check, professional, डालना
45  customer  customer_state_employment_type    —           —             self employ, self employee, page, personal, कीजिए
46  agent     agent_ask_employment_type         —           —             salaried, self-employ, page, details, self
47  customer  customer_state_employment_type    —           —             business, चलती
48  agent     agent_request_income              —           —             income, बताएं।, जाए, fill, monthly
49  customer  customer_provide_org_name         —           —             business, लिखना
50  agent     agent_request_org_name            —           —             बताएं।, जाए, enter, registered, business
51  customer  customer_provide_org_name         —           —             डालना, सिर्फ़
52  agent     agent_request_org_name            —           —             registered, पूरा, business, डालना, records
53  customer  customer_acknowledge              —           —             —
54  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, address
55  customer  customer_acknowledge              —           —             —
56  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, address
57  customer  customer_acknowledge              —           —             —
58  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
59  agent     agent_offer_skip_udyam            —           —             चूंकि, जवाब
60  customer  customer_respond_udyam            —           —             उद्यम
61  agent     agent_request_udyam               —           —             udyam, उद्यम, करें।, page, number
62  customer  customer_respond_udyam            —           —             number, same
63  agent     agent_offer_skip_udyam            —           —             skip, application, page, number, mobile
64  customer  customer_report_done              —           —             दिखा
65  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
66  customer  customer_react_to_final_offer     —           —             लाख, पांच
67  customer  customer_react_to_final_offer     —           —             देखा
68  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
69  customer  customer_ask_question             confused    —             कैसे, amount, three, month, change
70  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, offer, amount, हूँ।
71  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, मदद, कृपया, relationship
```

## Call 93a25fd6 (transferred) — 31 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   agent     agent_present_offer               —           —             pre-approved, loan, approved, pre, मदद
4   customer  customer_agree                    —           —             करनी, app
5   agent     agent_send_sms_link               —           send_sms      sms, भेज
6   customer  customer_report_link_opened       —           —             app, लूं
7   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
8   agent     agent_guide_open_link             —           —             sms, करें।, link, click
9   customer  customer_report_link_opened       —           —             —
10  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
11  customer  customer_ask_question             —           —             link
12  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
13  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
14  customer  customer_acknowledge              —           —             —
15  agent     agent_request_otp                 —           —             करें।, number, mobile, enter
16  customer  customer_do_otp                   —           —             number, mobile
17  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
18  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
19  agent     agent_request_personal_details    —           —             details, basic
20  customer  customer_do_otp                   —           —             otp
21  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, जाएगा।
22  agent     agent_request_otp                 —           —             otp, करें।, कृपया, verify, इंतज़ार
23  customer  customer_do_otp                   —           —             update
24  agent     agent_wait                        —           —             otp, कृपया, बताएं।, इंतज़ार, जाए
25  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, fetch
26  customer  customer_do_otp                   —           —             otp
27  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
28  customer  customer_react_to_final_offer     —           —             हज़ार
29  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
30  customer  customer_acknowledge              —           —             —
```

## Call 995adf61 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             —
3   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
4   agent     agent_guide_open_link             —           —             sms, करें।, link, click
5   customer  customer_report_sms_received      —           —             —
6   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
7   customer  customer_report_done              —           —             हो गया
8   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
9   customer  customer_report_done              —           —             कर दिया
10  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
11  customer  customer_acknowledge              —           —             —
12  agent     agent_request_otp                 —           —             otp, कृपया, verify, बताएं।, enter
13  customer  customer_report_done              —           —             done
14  agent     agent_request_personal_details    —           —             complete, personal, details, आगे, login
15  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
16  customer  customer_report_done              —           —             हो गया
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
18  customer  customer_report_done              —           —             done
19  agent     agent_request_email               —           —             email, now, personal, enter, address
20  customer  customer_acknowledge              —           —             extra
21  agent     agent_request_address             —           —             address, pincode, locality, building, house number
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_terms_accept        —           —             terms and condition, terms, button, check, conditions
24  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, now
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
27  customer  customer_state_employment_type    —           —             self employ, employed
28  agent     agent_request_income              —           —             income, fill, monthly, net, business
29  customer  customer_report_done              —           —             done
30  agent     agent_request_org_name            —           —             now, enter, name, registered, business
31  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, address
34  customer  customer_report_done              —           —             हो गया
35  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
36  customer  customer_respond_udyam            —           —             उद्यम
37  agent     agent_offer_skip_udyam            —           —             skip, number, click, option, उद्यम
38  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_otp                 —           —             otp, कृपया, verify, number, बताएं।
41  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, application
42  customer  customer_react_to_final_offer     —           —             दिख, pen
43  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call 9e9d4e8e (transferred) — 56 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             बोल, भैया
5   customer  customer_express_distrust         —           —             पाएगा, झूठ
6   agent     agent_explain_fee                 —           —             interest rate, offer, final, शुरू, समझ
7   customer  customer_agree                    —           —             कीजिए
8   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
9   agent     agent_guide_open_link             —           —             sms, करें।, link, click
10  customer  customer_ask_question             —           —             message, whatsapp
11  agent     agent_guide_open_link             —           —             sms, कृपया, जिसमें, link, आगे
12  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
13  agent     agent_ask_to_repeat               —           —             फिर से बता, कृपया, कीजिए, माफ़, बताइए।
14  customer  customer_report_done              —           —             click
15  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
16  customer  customer_do_otp                   —           —             number
17  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
18  customer  customer_other                    —           —             —
19  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
20  customer  customer_do_otp                   —           —             otp
21  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
22  agent     agent_request_otp                 —           —             otp, कृपया, verify, बताएं।, जाए
23  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
24  customer  customer_ask_question             —           —             —
25  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, email
26  customer  customer_other                    —           —             —
27  agent     agent_answer_query                —           —             कृपया, समय, कॉल, कीजिए, बताएं
28  customer  customer_request_wait             —           —             minute, line, दुबारा
29  agent     agent_wait                        —           —             इंतज़ार, chd
30  customer  customer_do_otp                   —           —             otp
31  agent     agent_wait                        —           —             otp, कृपया, बताएं।, इंतज़ार, जाए
32  customer  customer_do_otp                   —           —             —
33  agent     agent_request_otp                 —           —             otp, कृपया, verify, बताएं।
34  customer  customer_provide_pan              —           —             pan, card, आधार, लिखा
35  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
36  customer  customer_react_to_final_offer     —           —             लाख, दिखा
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
38  customer  customer_acknowledge              —           —             —
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, कृपया, relationship
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, relationship, manager, connect
41  customer  customer_acknowledge              —           —             —
42  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
43  customer  customer_agree                    —           —             —
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, relationship, manager, connect, kyc
45  customer  customer_acknowledge              —           —             —
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
47  customer  customer_acknowledge              —           —             —
48  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, करें।, हूँ।, कृपया, समय
49  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, करें।, हूँ।, कृपया, समय
50  customer  customer_acknowledge              —           —             —
51  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, करें।, हूँ।, कृपया, समय
52  customer  customer_acknowledge              —           —             —
53  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, करें।, हूँ।, कृपया, समय
54  customer  customer_other                    —           —             माफ़
55  agent     agent_reassure_trust              —           —             हूँ।, connect, समझ, बिल्कुल, करेंगे।
```

## Call 9fe046b5 (transferred) — 50 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_other                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             बोल
5   customer  customer_query_fee                —           —             interest, rate
6   agent     agent_explain_fee                 —           —             interest rate, offer, sms, करें।, final
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   customer  customer_report_done              —           —             check
9   agent     agent_guide_open_link             —           —             link, click, चुके
10  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, number, get
11  customer  customer_ask_question             —           —             approved, pre, समय, मांग
12  agent     agent_present_offer               —           —             pre-approved, loan, approved, pre, otp
13  customer  customer_provide_pan              —           —             number, card, मांग, भरना, detail
14  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
15  customer  customer_request_wait             —           —             wait
16  agent     agent_wait                        —           —             इंतज़ार
17  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
18  customer  customer_report_done              —           —             हो गया, भर दिया
19  customer  customer_request_wait             —           —             रुकिए, wait, minute
20  agent     agent_wait                        —           —             इंतज़ार
21  customer  customer_agree                    —           —             —
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_request_address             —           —             address, pincode, locality, building, house number
27  agent     agent_request_terms_accept        —           —             terms and condition, terms, conditions
28  customer  customer_request_wait             —           —             minute
29  agent     agent_wait                        —           —             इंतज़ार
30  customer  customer_ask_question             —           —             address, space
31  agent     agent_request_address             —           —             address, pincode, locality, building, house number
32  customer  customer_acknowledge              —           —             —
33  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
34  customer  customer_report_done              —           —             डाल
35  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
36  customer  customer_ask_question             —           —             email, official, डालना
37  agent     agent_answer_query                —           —             otp, email, ज़रूरी, official, verification
38  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
39  customer  customer_report_done              —           —             हो गया, complete
40  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
41  customer  customer_report_done              —           —             हो गया
42  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
43  customer  customer_report_done              —           —             हो गया, complete
44  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
45  customer  customer_other                    —           —             —
46  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
47  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
48  customer  customer_query_fee                —           —             emi, interest, rate, point, दिखा
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, offer, करें।, हूँ।, final
```

## Call a051b745 (transferred) — 79 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             शुरू कर, शुरू, करिए
5   agent     agent_send_sms_link               —           —             sms
6   customer  customer_acknowledge              —           —             time
7   customer  customer_greet                    —           —             hello, call
8   agent     agent_guide_open_link             —           —             sms, करें।, link, click
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
11  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
12  agent     agent_guide_open_link             —           —             sms, करें।, link, click
13  customer  customer_report_done              —           —             हो गया
14  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
15  customer  customer_report_done              —           —             कर दिया
16  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
17  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
20  agent     agent_request_otp                 —           —             otp, करें।, verify, बताएं।, जाए
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
23  customer  customer_ask_question             —           —             select, मांग, first, document
24  agent     agent_request_pan                 —           —             पैन, बताएं।, fill, select, नंबर
25  customer  customer_provide_pan              —           —             number, डालना, pay
26  agent     agent_request_pan                 —           —             पैन, number, capital, type, card
27  customer  customer_ask_question             —           —             मांग, two, choose, last, year
28  agent     agent_answer_query                —           —             आगे, select, डालें।, two, form
29  customer  customer_agree                    —           —             —
30  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
31  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
32  customer  customer_acknowledge              —           —             call
33  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
34  customer  customer_acknowledge              —           —             call
35  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
36  agent     agent_request_address             —           —             address, pincode, locality, building, house number
37  customer  customer_request_wait             —           —             आगे, रुक, जाइए, बढ़े
38  agent     agent_wait                        —           —             हूँ।, तैयार, हों, बताइए।, रुक
39  agent     agent_request_address             —           —             address, pincode, locality, building, house number
40  customer  customer_request_wait             —           —             hold
41  agent     agent_wait                        —           —             इंतज़ार
42  customer  customer_acknowledge              —           —             बोल
43  agent     agent_request_address             —           —             address, pincode, locality, building, house number
44  customer  customer_acknowledge              —           —             call, करा
45  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
46  customer  customer_accept_terms             —           —             choose, सोच
47  agent     agent_request_terms_accept        —           —             terms and condition, terms, conditions, दोनों
48  customer  customer_ask_question             —           —             जहां, डालनी
49  agent     agent_answer_query                —           —             करें।, डालने, two, confusion, बताइए।
50  customer  customer_report_done              —           —             हो गया
51  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
52  customer  customer_acknowledge              —           —             call
53  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
54  customer  customer_acknowledge              —           —             offer, application, check, review, सात
55  agent     agent_inform_manual_review        —           push_to_crm   application, check, review, time, some
56  customer  customer_react_to_final_offer     —           —             loan, eligible
57  customer  customer_react_to_final_offer     —           —             lakh, one, thousand, five, rupees
58  agent     agent_present_final_offer         —           —             loan, lakh, one, thousand, five
59  agent     agent_present_final_offer         —           —             loan, application, proceed, lakh, one
60  customer  customer_ask_question             —           —             आगे, back, लूं
61  agent     agent_answer_query                —           —             loan, application, complete, आगे, ताकि
62  customer  customer_ask_question             —           —             offer, option, बढ़ने
63  agent     agent_answer_query                —           —             करें।, मदद, page, इंतज़ार, आगे
64  agent     agent_answer_query                —           —             करें।, कृपया, page, connect, आपसे
65  customer  customer_acknowledge              —           —             team, कराइए
66  agent     agent_end_call                    —           —             मदद, connect, आपसे, दिक्कत, जल्दी
67  customer  customer_acknowledge              —           —             sun
68  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
69  customer  customer_report_done              —           —             देख
70  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
71  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
72  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
73  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
74  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
75  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
76  customer  customer_acknowledge              —           —             thank, रहिए
77  agent     agent_end_call                    —           —             goodbye, धन्यवाद, जी।, time, eoc
78  customer  customer_other                    confused    —             कैसे
```

## Call a1b72c5c (transferred) — 48 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             sorry, again, say
1   customer  customer_greet                    —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, शिवा
3   customer  customer_agree                    —           —             —
4   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
5   customer  customer_agree                    —           —             —
6   customer  customer_agree                    —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
8   agent     agent_send_sms_link               —           —             sms, मिल
9   agent     agent_guide_open_link             —           —             sms, करें।, link, click
10  customer  customer_report_link_opened       —           —             click
11  agent     agent_guide_open_link             —           —             कृपया, link, screen, home, click
12  customer  customer_report_done              —           —             —
13  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
14  agent     agent_ask_to_repeat               —           —             call
15  customer  customer_report_done              —           —             कर दिया, click, know
16  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, number, बताएं।
17  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
20  customer  customer_provide_pan              —           —             डाल
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_request_address             —           —             address, pincode, locality, building, house number
26  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
29  customer  customer_state_employment_type    —           —             —
30  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
31  customer  customer_state_employment_type    —           —             self employ, self, select, employed
32  agent     agent_request_income              —           —             income, बताएं।, जाए, fill, monthly
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, registered
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_business_details    —           —             business, बताएं।, जाए, enter, address
37  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, दोहरा
38  customer  customer_report_done              —           —             हो गया, डाल, बोला
39  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
40  customer  customer_skip_udyam               —           —             skip
41  agent     agent_offer_skip_udyam            —           —             skip, करें।, बताएं।, जाए, click
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
44  customer  customer_report_done              —           —             हो गया
45  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, fetch
46  customer  customer_react_to_final_offer     —           —             लाख, दिखा
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call a2ff0814 (transferred) — 51 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             बोलो
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, कृपया, application
6   agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, भेज, मिल
7   customer  customer_acknowledge              —           —             —
8   agent     agent_send_sms_link               —           —             sms, करें।, कृपया, मिल, क्लिक
9   customer  customer_acknowledge              —           —             —
10  agent     agent_guide_open_link             —           —             लिंक पर क्लिक, क्लिक, लिंक
11  customer  customer_report_applied           —           —             apply, करूंगा
12  agent     agent_guide_open_link             —           —             लिंक पर क्लिक, हूँ।, मदद, कृपया, आगे
13  customer  customer_agree                    —           —             बोल, starting
14  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, आगे
15  customer  customer_report_done              —           —             लगा
16  agent     agent_guide_apply                 —           —             apply now, apply, now, हूँ।, मदद
17  customer  customer_agree                    —           —             आगे
18  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
19  customer  customer_do_otp                   frustrated  —             otp, बार बार, number, mobile, आगे
20  agent     agent_acknowledge                 —           —             समझती
21  customer  customer_do_otp                   —           —             otp, लगा
22  agent     agent_acknowledge                 —           —             समझ, गई।
23  customer  customer_ask_question             —           —             —
24  agent     agent_wait                        —           —             loan, offer, otp, fetch, इंतजार
25  customer  customer_other                    —           —             —
26  agent     agent_greet                       —           —             बताएं
27  customer  customer_ask_question             —           —             journey
28  agent     agent_answer_query                —           —             हूँ।, समझ, लेकर, journey
29  customer  customer_ask_question             —           —             रखा, journey
30  agent     agent_clarify                     —           —             मदद, कृपया, बताएं, समझ, ताकि
31  customer  customer_ask_question             —           —             लिखा, ऐसा, resume, journey
32  agent     agent_answer_query                —           —             कृपया, शुरू, बताएं।, आगे, ताकि
33  customer  customer_agree                    —           —             —
34  agent     agent_request_personal_details    —           —             personal, आगे, बढ़
35  customer  customer_react_to_final_offer     —           —             loan, amount, लाख, हज़ार, option
36  agent     agent_present_final_offer         —           —             loan, amount, मदद, देख, लाख
37  customer  customer_query_fee                —           —             emi, लाख, monthly, हज़ार, उसमें
38  agent     agent_answer_query                —           —             loan, हूँ।, मदद, लाख, रुपये
39  customer  customer_query_fee                —           —             नीचे, percent, उसी, ऐसा, पांच
40  agent     agent_answer_query                —           —             loan, हूँ।, interest, rate, चाहें
41  customer  customer_acknowledge              —           —             eight
42  agent     agent_confirm                     —           —             आगे बढ़, offer, मदद, आगे, सवाल
43  customer  customer_react_to_final_offer     —           —             loan, लाख, बाकी, पांच, दूसरा
44  customer  customer_query_fee                —           —             महीने, साल, छत्तीस
45  customer  customer_query_fee                —           —             उसमें, सात, चौबीस
46  agent     agent_answer_query                —           —             loan, हूँ।, मदद, लाख, समझ
47  customer  customer_ask_question             —           —             लाख
48  agent     agent_answer_query                —           —             loan, amount, हूँ।, मदद, process
49  customer  customer_agree                    —           —             —
50  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, मदद, कृपया, relationship
```

## Call a638362d (transferred) — 57 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
3   customer  customer_query_fee                —           —             interest, rate
4   agent     agent_answer_query                —           —             loan, offer, apply, approved, amount
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, कृपया, application
6   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, speaker, मिल
7   customer  customer_report_sms_received      —           —             मिल
8   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
9   customer  customer_report_link_opened       —           —             exactly
10  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, नीचे
11  customer  customer_do_otp                   —           —             now, number, mobile, मांग
12  agent     agent_request_otp                 —           —             कृपया, screen, आगे, ताकि, सकें।
13  agent     agent_request_otp                 —           send_otp      otp, कृपया, verify, नीचे, get
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_clarify                     —           —             मदद, कृपया, आगे, बताएं, अगली
16  customer  customer_provide_pan              —           —             pan, number, name, full, मांग
17  agent     agent_request_pan                 —           —             पैन, कृपया, personal, details, सबसे
18  agent     agent_request_pan                 —           —             पैन, कृपया, पूरा, नंबर, जाए।
19  customer  customer_ask_question             —           —             address, भरनी
20  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, number
21  customer  customer_report_address_error     —           —             number, डाल, दिखा, city, code
22  agent     agent_help_address_error          —           —             हूँ।, मदद, कृपया, fill, सही
23  customer  customer_report_address_error     —           —             सही, city
24  agent     agent_help_address_error          —           —             हूँ।, मदद, check, बताएं, सही
25  customer  customer_report_address_error     —           —             दिखा, city, समस्या, internet, गलत
26  agent     agent_help_address_error          —           —             करें।, मदद, details, proceed, आगे
27  customer  customer_acknowledge              —           —             —
28  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, मदद, कृपया
29  customer  customer_state_employment_type    —           —             professional
30  agent     agent_ask_employment_type         —           —             professional
31  customer  customer_state_employment_type    —           —             self, type, employee
32  agent     agent_acknowledge                 —           —             समझ
33  agent     agent_request_income              —           —             income, कृपया, monthly, net, बताएं
34  agent     agent_request_income              —           —             income, कृपया, monthly, net
35  customer  customer_provide_business_details —           —             दुकान
36  agent     agent_request_business_details    —           —             business, कृपया, self, बताएं, समझ
37  customer  customer_provide_business_details —           —             —
38  agent     agent_request_business_details    —           —             business, application, बताएं, सही, पूरा
39  customer  customer_report_done              —           —             इधर
40  agent     agent_request_business_details    —           —             हूँ।, मदद, कृपया, complete, details
41  customer  customer_agree                    —           —             —
42  agent     agent_acknowledge                 —           —             —
43  customer  customer_respond_udyam            —           —             उद्यम
44  agent     agent_request_udyam               —           —             उद्यम, करें।, कृपया, नीचे, नंबर
45  agent     agent_offer_skip_udyam            —           —             skip
46  customer  customer_report_done              —           —             —
47  agent     agent_clarify                     —           —             कौन सा, मदद, कृपया, बताएं, ताकि
48  customer  customer_skip_udyam               —           —             skip, cancel, anyway
49  agent     agent_offer_skip_udyam            —           —             skip, करें।, कृपया, आगे, बताएं
50  customer  customer_report_done              —           —             कर दिया
51  agent     agent_request_terms_accept        —           —             हूँ।, मदद, कृपया, समय, proceed
52  customer  customer_react_to_final_offer     —           —             loan, amount, लाख, हज़ार, रुपए
53  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
54  customer  customer_react_to_final_offer     —           —             loan, amount, देख
55  agent     agent_transfer_to_rm              —           transfer_to_rmबिल्कुल
56  customer  customer_other                    —           —             छत्तीस
```

## Call a78e74de (transferred) — 47 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
6   customer  customer_agree                    —           —             बोलो
7   agent     agent_send_sms_link               —           send_sms      sms, loan, करें।, कृपया, application
8   agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, भेज, speaker
9   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
10  customer  customer_report_link_opened       —           —             खुल गया, खुल
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
12  customer  customer_report_done              —           —             कर दिया
13  agent     agent_request_otp                 —           —             कृपया, screen, बताएं, होगा।, नंबर
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, process
16  customer  customer_do_otp                   —           —             verified
17  agent     agent_request_personal_details    —           —             कृपया, page, आगे, बताएं, बढ़
18  customer  customer_provide_pan              —           —             pan, number, मांग
19  agent     agent_request_pan                 —           —             पैन, page, personal, details, सबसे
20  customer  customer_provide_pan              —           —             —
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, बताएं।
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital, आगे, status
23  customer  customer_provide_address          —           —             address
24  agent     agent_request_address             —           —             address, locality, कृपया, जिसमें, बताएं।
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, बताएं।, proceed
27  customer  customer_report_done              —           —             कर दिया
28  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, details, self
29  customer  customer_state_employment_type    —           —             self employ, self, employed
30  agent     agent_request_income              —           —             income, करें।, हूँ।, कृपया, जिसमें
31  customer  customer_report_done              —           —             कर दिया
32  agent     agent_request_udyam               —           —             udyam, करें।, कृपया, number, mobile
33  customer  customer_respond_udyam            —           —             उद्यम
34  agent     agent_request_udyam               —           —             udyam, loan, offer, करें।, otp
35  customer  customer_respond_udyam            —           —             उसमें, लिखना
36  agent     agent_request_udyam               —           —             udyam, करें।, कृपया, बताएं।, registered
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_otp                 —           —             otp, करें।, कृपया, verify, समय
39  customer  customer_do_otp                   —           —             verify
40  agent     agent_wait                        —           —             कृपया, देख, बताएं, पूरा, सकें।
41  customer  customer_acknowledge              —           —             processing
42  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, समय
43  customer  customer_other                    —           —             call, means, fetching
44  agent     agent_wait                        —           —             loan, offer, हूँ।, final, कृपया
45  customer  customer_react_to_final_offer     —           —             lakh, two, rupees
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, approved, pre, amount, हूँ।
```

## Call a880a397 (transferred) — 48 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             sorry, again, say
1   customer  customer_report_link_opened       —           —             link, open, बोलो
2   customer  customer_greet                    —           —             hello
3   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
4   customer  customer_provide_address          —           —             भेज, personal, name, डाल, code
5   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
6   customer  customer_report_done              —           —             कर दिया
7   agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
8   customer  customer_report_done              —           —             डाल
9   agent     agent_request_otp                 —           —             otp, verify
10  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
11  customer  customer_provide_pan              —           —             डाल
12  agent     agent_request_personal_details    —           —             gender, date of birth, marital, enter, पैन
13  customer  customer_report_done              —           —             डाल
14  agent     agent_request_personal_details    —           —             करें।, बताएं।, जाए, status, select
15  customer  customer_report_done              —           —             डाल
16  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
17  customer  customer_report_done              —           —             हो गया
18  agent     agent_request_address             —           —             address, pincode, locality, building, house number
19  agent     agent_request_address             —           —             address, fill, पाए
20  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
21  customer  customer_ask_question             —           —             किधर
22  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, नीचे, button
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
27  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
28  customer  customer_state_employment_type    —           —             salary, choose
29  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_request_org_name            —           —             organization, करें।, बताएं।, जाए, enter
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_email               —           —             email, करें।, बताएं।, जाए, enter
34  customer  customer_ask_question             —           —             ज़रूरी
35  agent     agent_answer_query                —           —             करें।, मदद, otp, कृपया, verify
36  customer  customer_report_done              —           —             कर दिया
37  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
38  customer  customer_report_done              —           —             डाल
39  agent     agent_request_business_details    —           —             सही, दिख, ध्यान, पिनकोड, डालें
40  customer  customer_report_done              —           —             डाल
41  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
42  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
43  customer  customer_report_done              —           —             कर दिया
44  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
45  customer  customer_react_to_final_offer     —           —             दिख
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, कृपया, relationship
```

## Call b07fcd2f (transferred) — 80 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello, गाड़ी
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
4   agent     agent_guide_open_link             —           —             sms, करें।, link, click
5   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
6   customer  customer_do_otp                   —           —             number, mobile, डालना
7   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
8   agent     agent_end_call                    —           —             कॉल, चूंकि, समाप्त, उत्तर
9   customer  customer_other                    —           —             seven
10  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
11  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
12  agent     agent_request_otp                 —           —             otp, verify
13  customer  customer_report_done              —           —             करवा
14  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, personal
15  customer  customer_request_wait             —           —             wait, कीजिए
16  agent     agent_wait                        —           —             इंतज़ार
17  customer  customer_provide_pan              —           —             pan, number
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
19  customer  customer_ask_question             —           —             check, pan
20  agent     agent_request_personal_details    —           —             करें।, enter, पैन, जैसा, कार्ड
21  customer  customer_acknowledge              —           —             apply, बोल
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, हूँ।
23  customer  customer_do_otp                   —           —             otp, बोला
24  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
25  customer  customer_request_wait             —           —             wait
26  agent     agent_request_otp                 —           —             otp, करें।, कृपया, verify, बताएं।
27  customer  customer_do_otp                   —           —             otp, check, wait
28  agent     agent_wait                        —           —             इंतज़ार
29  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
30  customer  customer_provide_pan              —           —             pan, otp, डाल, card
31  agent     agent_request_email               —           —             email, personal
32  customer  customer_provide_pan              —           —             pan, card
33  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
34  customer  customer_report_done              —           —             हो गया
35  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
36  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
37  customer  customer_provide_personal_details —           —             marital, status
38  customer  customer_provide_email            —           —             email, full, मांग, डालना, दिखाई
39  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
40  customer  customer_report_done              —           —             email
41  agent     agent_request_address             —           —             address, pincode, locality, building, house number
42  customer  customer_request_wait             —           —             email, डालने, कुमार
43  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, address
44  customer  customer_provide_address          —           —             address, डाल, mail
45  agent     agent_request_address             —           —             address, pincode, locality, building, house number
46  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
47  customer  customer_report_done              —           —             कर दिया
48  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
49  customer  customer_report_done              —           —             proceed, option, दिखाई
50  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
51  customer  customer_acknowledge              —           —             पता
52  customer  customer_ask_question             —           —             personal, professional, लिखा, पता, ऊपर
53  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, बताएं।, जाए
54  customer  customer_ask_question             —           —             बोल, मिल, पड़ेगा
55  customer  customer_report_address_error     —           —             number, proceed, email, address, flat
56  agent     agent_help_address_error          —           —             red, error, कृपया, button, check
57  customer  customer_report_done              —           —             कर दिया, proceed, name, बाकी
58  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
59  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
60  customer  customer_ask_question             —           —             personal, fill, दोनों, organization, दूं
61  agent     agent_answer_query                —           —             offer, personal, enter, full, salary
62  customer  customer_ask_question             —           —             मतलब, organization
63  agent     agent_answer_query                —           —             enter, organization, नहीं।, जरूरी, दें
64  customer  customer_provide_org_name         —           —             organization, accept
65  agent     agent_answer_query                —           —             कृपया, enter, पूरा, salary, जैसा
66  customer  customer_request_wait             —           —             रुकिए
67  agent     agent_wait                        —           —             इंतज़ार
68  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
69  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
70  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
71  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
72  customer  customer_ask_question             —           —             दूं, register
73  agent     agent_answer_query                —           —             आगे, address, fill, organization, पता
74  customer  customer_skip_udyam               —           —             बोल, keep
75  agent     agent_offer_skip_udyam            —           —             skip, number, click, आगे, option
76  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
77  agent     agent_request_otp                 —           —             otp, कृपया, verify
78  customer  customer_react_to_final_offer     —           —             loan, amount, लाख, दिखा, रुपया
79  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, offer, हूँ।, final, शुरू
```

## Call b10463b7 (transferred) — 54 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             sorry, again, say
1   customer  customer_acknowledge              —           —             call
2   agent     agent_ask_to_repeat               —           —             sorry, repeat
3   customer  customer_greet                    —           —             hello
4   agent     agent_greet                       —           —             hello, hardika
5   customer  customer_greet                    —           —             who
6   agent     agent_greet                       —           —             capital, aditya, birla, minutes, speak
7   customer  customer_ask_question             —           —             —
8   agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, approved
9   customer  customer_ask_question             —           —             offer, what
10  agent     agent_disclose_recording          —           —             record, training, quality, loan, offer
11  customer  customer_agree                    —           —             बोलो
12  agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, apply
13  customer  customer_agree                    —           —             बोलो
14  agent     agent_send_sms_link               —           send_sms      sms, now, application, link, speaker
15  customer  customer_express_distrust         distrustful —             fraud, fake
16  agent     agent_reassure_trust              —           —             sms, करें।, कृपया, verify, page
17  customer  customer_report_link_opened       —           —             click
18  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, नीचे
19  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
20  customer  customer_report_done              —           —             कर दिया
21  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
22  agent     agent_request_otp                 —           —             otp, verify
23  customer  customer_do_otp                   —           —             —
24  agent     agent_request_pan                 —           —             पैन, कृपया, बताएं।, जाए, details
25  customer  customer_report_done              —           —             details, डाल
26  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
27  customer  customer_report_done              —           —             details, डाल, अरे, already
28  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
29  customer  customer_report_done              —           —             page, details, डाल, अरे
30  agent     agent_request_address             —           —             address, pincode, locality, building, house number
31  customer  customer_report_done              —           —             कर दिया
32  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
33  customer  customer_report_done              —           —             कर लिया
34  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, details
35  customer  customer_report_done              —           —             कर दिया
36  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, बताएं।, self
37  agent     agent_ask_employment_type         —           —             salaried, self-employ, self, employment, type
38  customer  customer_state_employment_type    —           —             salaried, आगे, बढ़ना, अरे, भाई
39  agent     agent_request_income              —           —             income, home, fill, monthly, salaried
40  customer  customer_report_done              —           —             कर दिया, आगे, बोलो, अरे
41  agent     agent_request_org_name            —           —             organization, करें।, बताएं।, जाए, enter
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_request_email               —           —             email, करें।, बताएं।, जाए, enter
44  customer  customer_report_done              —           —             हो गया, कर दिया
45  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
46  customer  customer_report_done              —           —             कर दिया
47  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
48  customer  customer_report_done              —           —             कर दिया
49  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
50  customer  customer_report_done              —           —             डाल
51  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
52  customer  customer_react_to_final_offer     —           —             देख
53  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call b147ce0b (transferred) — 57 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_greet                    —           —             hello
5   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
6   customer  customer_ask_question             —           —             call, purpose, what
7   agent     agent_send_sms_link               —           send_sms      sms, कृपया, application, रखें, जिसमें
8   customer  customer_acknowledge              —           —             —
9   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, जाए
10  customer  customer_express_distrust         —           —             call, recorded, auto
11  agent     agent_reassure_trust              —           —             sms, बोल, हूँ।, मदद, capital
12  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, नीचे
13  customer  customer_do_otp                   —           —             number, mobile
14  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
15  customer  customer_report_done              —           —             done
16  agent     agent_request_pan                 —           —             पैन, कृपया, personal, details, सबसे
17  customer  customer_query_fee                —           —             processing fee, terms, conditions, interest, rate
18  agent     agent_explain_fee                 —           —             processing fee, interest rate, loan, approved, amount
19  agent     agent_request_pan                 —           —             पैन, कृपया, आगे, बताएं, पूरा
20  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
21  agent     agent_request_pan                 —           —             पैन, मदद, कृपया, आगे, बताएं
22  customer  customer_request_wait             —           —             minute, some, give
23  agent     agent_wait                        —           —             हूँ।, समय, इंतज़ार, बिल्कुल, लें
24  agent     agent_request_pan                 —           —             पैन, आगे, बताएं, ताकि, बढ़
25  agent     agent_request_pan                 —           —             पैन, मदद, कृपया, जाए, बताएं
26  customer  customer_report_address_error     —           —             address, training, like, cannot, space
27  agent     agent_help_address_error          —           —             करें।, हूँ।, मदद, कृपया, समय
28  customer  customer_report_address_error     —           —             दिक़्क़त
29  agent     agent_acknowledge                 —           —             समझती, दिक्कत
30  customer  customer_request_wait             —           —             minute
31  agent     agent_wait                        —           —             कृपया, समय, इंतज़ार, लें।
32  agent     agent_help_address_error          —           —             हूँ।, मदद, बताएं, सही, बढ़िया
33  customer  customer_report_address_error     —           —             page, proceed, आगे
34  agent     agent_help_address_error          —           —             करें।, हूँ।, मदद, कृपया, बताएं
35  customer  customer_ask_question             —           —             details, fill, पूरा
36  agent     agent_answer_query                —           —             करें।, हूँ।, मदद, details, आगे
37  customer  customer_acknowledge              —           —             —
38  agent     agent_help_address_error          —           —             हूँ।, मदद, कृपया, आगे, बताएं
39  customer  customer_provide_address          —           —             details, fill
40  agent     agent_acknowledge                 —           —             हूँ।, मदद, कृपया, details, दिक्कत
41  customer  customer_report_done              —           —             page, proceed
42  customer  customer_provide_email            —           —             email, enter, salaried, official, customer
43  agent     agent_request_email               —           —             email, हूँ।, मदद, कृपया, बताएं।
44  agent     agent_request_address             —           —             address, pincode, कृपया, बताएं।, पूरा
45  customer  customer_acknowledge              —           —             —
46  agent     agent_request_address             —           —             address, pincode, कृपया, जाए, आगे
47  customer  customer_ask_question             —           —             loan, close
48  agent     agent_answer_query                —           —             loan, हूँ।, मदद, बताएं, अनुसार
49  customer  customer_ask_question             —           —             emi, first, close, after, month
50  agent     agent_answer_query                —           —             loan, हूँ।, मदद, कृपया, details
51  customer  customer_query_fee                —           —             charges, loan
52  agent     agent_explain_fee                 —           —             charges, loan, offer, final, देख
53  customer  customer_request_wait             —           —             wait, offer, details, button, app
54  agent     agent_wait                        —           —             हूँ।, मदद, कृपया, process, इंतज़ार
55  customer  customer_acknowledge              —           —             —
56  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, amount, करें।, final
```

## Call bb88ae27 (transferred) — 53 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, call
4   customer  customer_greet                    —           —             hello
5   agent     agent_present_offer               —           —             apply, हूँ।, मदद, शुरू
6   customer  customer_agree                    —           —             बोलिए, करिए
7   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
8   agent     agent_guide_open_link             —           —             sms, link
9   customer  customer_query_fee                —           —             rate, कितना
10  agent     agent_explain_fee                 —           —             interest rate, offer, sms, final, शुरू
11  customer  customer_agree                    —           —             बोलिए
12  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
13  customer  customer_report_done              —           —             कर दिया
14  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
15  customer  customer_acknowledge              —           —             बोलिए
16  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
17  customer  customer_react_to_offer           —           —             loan, interest, lakh, five, congratulation
18  agent     agent_request_personal_details    —           —             now, details, proceed, fill, basic
19  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
20  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
21  customer  customer_report_done              —           —             —
22  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
23  customer  customer_report_done              —           —             हो गया, बोलिए
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
27  customer  customer_report_done              —           —             —
28  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
29  customer  customer_report_done              —           —             —
30  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
31  customer  customer_report_done              —           —             बोलिए
32  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
33  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
34  customer  customer_state_employment_type    —           —             salary
35  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
38  customer  customer_report_done              —           —             हो गया, डाल
39  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
40  customer  customer_report_done              —           —             हो गया
41  agent     agent_request_address             —           —             address, pincode, बताएं।, जाए, fill
42  customer  customer_report_done              —           —             हो गया
43  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
44  agent     agent_ask_to_repeat               —           —             कृपया, कीजिए, माफ़, समझ, दोहराएँ।
45  customer  customer_report_done              —           —             हो गया
46  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
47  customer  customer_ask_question             —           —             —
48  agent     agent_request_otp                 —           —             otp, verify
49  customer  customer_report_done              —           —             हो गया
50  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
51  customer  customer_react_to_final_offer     —           —             लाख, दिख, रुपए, पांच
52  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call c3a47f19 (transferred) — 44 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_ask_query                —           —             cancel
5   agent     agent_acknowledge                 —           —             समझ
6   customer  customer_ask_query                —           —             —
7   customer  customer_ask_query                —           —             proceed, cancel
8   agent     agent_send_sms_link               —           send_sms      sms, application, process, जिसमें, भेज
9   agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, रखें, भेज
10  agent     agent_guide_open_link             —           —             sms, करें।, link, click
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
12  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
13  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
14  agent     agent_request_personal_details    —           —             otp, verify, personal, details, help
15  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
16  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
18  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
19  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
20  agent     agent_request_address             —           —             address, pincode, locality, building, house number
21  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
22  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
23  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
24  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
25  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
26  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
27  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
28  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
29  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
30  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
31  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
32  agent     agent_ask_to_repeat               —           —             कॉल, क्षमा
33  agent     agent_request_address             —           —             address, pincode, बताएं।, जाए, fill
34  agent     agent_ask_to_repeat               —           —             कृपया, कॉल, बताएं
35  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
36  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
37  agent     agent_request_otp                 —           send_otp      otp, कृपया, verify, बताएं।, जाए
38  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
39  agent     agent_ask_to_repeat               —           —             कृपया, कॉल, बताएं
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
41  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
42  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
43  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call c44d3103 (transferred) — 20 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
3   agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, application, process
4   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
5   customer  customer_report_sms_received      —           —             मिल
6   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
7   agent     agent_guide_open_link             —           —             खुल गया, खुल, लिंक, शुक्रिया
8   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
9   customer  customer_report_link_opened       —           —             खुल गया, खुल
10  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
11  customer  customer_report_applied           —           —             —
12  agent     agent_request_otp                 —           —             कृपया, बताएं।, आगे, ताकि, होगा।
13  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
14  customer  customer_do_otp                   —           —             otp
15  agent     agent_clarify                     —           —             मदद, कृपया, आगे, बताएं, दिख
16  customer  customer_other                    —           —             लिखा, खड़ा
17  agent     agent_wait                        —           —             loan, offer, कृपया, समय, सबसे
18  customer  customer_react_to_final_offer     —           —             offer, डालना
19  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, offer, approved, pre
```

## Call c4d807c2 (transferred) — 62 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   customer  customer_agree                    —           —             बोलिए
4   customer  customer_query_fee                —           —             interest, बोलिए, rate, मान
5   agent     agent_explain_fee                 —           —             interest rate, offer, sms, करें।, final
6   agent     agent_ask_to_repeat               —           —             कृपया, कॉल
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   customer  customer_report_sms_received      —           —             sms, link
9   agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, कृपया, भेज
10  customer  customer_report_sms_received      —           —             मिल, मिला
11  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, application, process
12  customer  customer_query_fee                —           —             processing fee, interest rate, आगे, interest, rate
13  agent     agent_explain_fee                 —           —             processing fee, interest rate, loan, offer, sms
14  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
15  agent     agent_guide_open_link             —           —             sms, करें।, link, click
16  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
17  customer  customer_report_link_opened       —           —             खोल
18  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
19  customer  customer_request_wait             —           —             minute, open
20  agent     agent_wait                        —           —             इंतज़ार
21  customer  customer_report_applied           —           —             apply
22  agent     agent_guide_apply                 —           —             screen, home
23  customer  customer_report_applied           —           —             apply now, apply, now, नीचे, लिख
24  agent     agent_guide_apply                 —           —             apply now, apply, now, screen, button
25  customer  customer_do_otp                   —           —             apply, now, number, mobile
26  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
27  customer  customer_request_wait             —           —             number, mobile, minute, डालने
28  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
29  customer  customer_do_otp                   —           —             otp, get
30  agent     agent_request_otp                 —           —             otp, verify, number, mobile, click
31  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
32  customer  customer_do_otp                   —           —             otp
33  agent     agent_request_otp                 —           —             otp, करें।, verify, बताएं।, जाए
34  customer  customer_request_wait             —           —             रुक, जाइए
35  agent     agent_wait                        —           —             इंतज़ार
36  customer  customer_request_wait             —           —             minute
37  agent     agent_wait                        —           —             इंतज़ार
38  customer  customer_do_otp                   —           —             otp
39  agent     agent_request_otp                 —           —             otp, verify, बताएं।, जाए
40  customer  customer_do_otp                   —           —             otp
41  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
42  customer  customer_acknowledge              —           —             —
43  agent     agent_request_otp                 —           —             otp
44  customer  customer_request_wait             —           —             save
45  agent     agent_request_otp                 —           —             otp, verify
46  customer  customer_request_wait             —           —             minute
47  agent     agent_request_otp                 —           —             otp, कृपया
48  customer  customer_do_otp                   —           —             —
49  agent     agent_request_otp                 —           —             otp, verify, बताएं।, जाए
50  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
51  customer  customer_report_done              —           —             हो गया, verify
52  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
53  customer  customer_provide_pan              —           —             pan, number, card, डालना, पड़ेगा
54  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
55  customer  customer_provide_pan              —           —             pan, number, डाल, card
56  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
57  customer  customer_react_to_final_offer     —           —             —
58  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
60  customer  customer_query_fee                —           —             offer, check, interest, rate, minute
61  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, कृपया, process
```

## Call c6a8b74f (transferred) — 35 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello, कहिए
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_greet                    —           —             hello
5   agent     agent_greet                       —           —             बोल, aditya
6   customer  customer_ask_question             —           —             —
7   agent     agent_answer_query                —           —             —
8   customer  customer_acknowledge              —           —             सही
9   agent     agent_greet                       —           —             बोल, aditya, birla
10  customer  customer_agree                    —           —             —
11  agent     agent_greet                       —           —             बोल, aditya, birla, बिल्कुल, जी।
12  customer  customer_agree                    —           —             सही
13  customer  customer_ask_question             —           —             —
14  agent     agent_reassure_trust              —           —             loan, offer, personal, capital, aditya
15  customer  customer_query_fee                —           —             interest, हज़ार, रुपए, पचास
16  agent     agent_explain_fee                 —           —             interest rate, loan, offer, sms, amount
17  agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, जिसमें, भेज
18  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
19  customer  customer_acknowledge              —           —             —
20  agent     agent_guide_open_link             —           —             loan, sms, देख, application, process
21  customer  customer_agree                    —           —             —
22  agent     agent_guide_open_link             —           —             लिंक पर क्लिक, apply, sms, now, कृपया
23  customer  customer_report_link_opened       —           —             खोल
24  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, मदद
25  customer  customer_acknowledge              —           —             —
26  agent     agent_request_otp                 —           send_otp      otp, apply, करें।, now, कृपया
27  customer  customer_do_otp                   —           —             otp
28  agent     agent_request_otp                 —           —             otp, करें।, मदद, कृपया, verify
29  customer  customer_acknowledge              —           —             —
30  agent     agent_request_otp                 —           —             otp, कृपया, verify, जाए, आगे
31  customer  customer_do_otp                   —           —             otp, डाल, congratulation, eligible
32  customer  customer_react_to_offer           —           —             loan, eligible
33  agent     agent_present_final_offer         —           —             loan, offer, amount, final, देख
34  customer  customer_react_to_final_offer     —           —             loan, offer, amount, thousand
```

## Call c834150c (transferred) — 50 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             बोल, समझती
6   customer  customer_ask_question             —           —             —
7   agent     agent_greet                       —           —             बोल, capital, aditya, birla, आपसे
8   customer  customer_ask_question             —           —             —
9   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
10  customer  customer_agree                    —           —             बोल, भैया
11  customer  customer_ask_question             —           —             ज़रूरत, required
12  agent     agent_answer_query                —           —             sms, application, details, पैन, self
13  customer  customer_query_fee                —           —             interest rate, interest, rate, like
14  agent     agent_explain_fee                 —           —             interest rate, loan, offer, sms, approved
15  customer  customer_query_fee                —           —             interest rate, interest, rate, बोलो, बोलते
16  agent     agent_explain_fee                 —           —             interest rate, loan, offer, sms, मदद
17  customer  customer_agree                    —           —             मिल, बिल्कुल, धन्यवाद, approval, बोलने
18  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, करें।, कृपया
19  customer  customer_ask_question             —           —             link, आपसे, सवाल, खोलने
20  agent     agent_confirm                     —           —             कृपया, बताएं
21  customer  customer_ask_question             —           —             आपसे, सवाल
22  agent     agent_confirm                     —           —             कृपया, बताएं।, बिल्कुल, सवाल, मुझसे
23  customer  customer_ask_question             —           —             loan, approval, mandatory
24  agent     agent_answer_query                —           —             loan, मदद, application, आगे, समझ
25  customer  customer_do_otp                   —           —             otp, page, number, phone, minute
26  agent     agent_request_otp                 —           —             otp, करें।, हूँ।, मदद, कृपया
27  customer  customer_other                    —           —             page, पूरा, like, बोलकर, ready
28  agent     agent_clarify                     —           —             मदद, सही, ताकि, पेज, सकूँ।
29  customer  customer_provide_personal_details —           —             page, details, basic
30  agent     agent_request_pan                 —           —             पैन, कृपया, page, details, सबसे
31  customer  customer_acknowledge              —           —             —
32  agent     agent_wait                        —           —             हूँ।, मदद, कृपया, शुरू, पैन
33  customer  customer_request_wait             —           —             minute, form, just, filling
34  agent     agent_wait                        —           —             इंतज़ार, आगे, पैन, बताएं, ताकि
35  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, कृपया
36  customer  customer_state_employment_type    —           —             self employ, self, employed, organization, like
37  agent     agent_request_business_details    —           —             business, करें।, कृपया, आगे, monthly
38  customer  customer_provide_org_name         —           —             name, business
39  agent     agent_request_org_name            —           —             कृपया, आगे, business, बढ़, सकें।
40  customer  customer_respond_udyam            —           —             उद्यम, number, self, employed, what
41  agent     agent_request_udyam               —           —             udyam, उद्यम, कृपया, application, number
42  customer  customer_respond_udyam            —           —             call, issue
43  agent     agent_clarify                     —           —             मदद, कृपया, बताएं, समझती, issue
44  customer  customer_other                    —           —             like
45  customer  customer_react_to_final_offer     —           —             loan, amount, now, lakh, one
46  customer  customer_react_to_final_offer     —           —             amount, let, cannot, note, change
47  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
48  customer  customer_react_to_final_offer     —           —             six, thirty
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, amount, हूँ।, final
```

## Call c947d052 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
1   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
2   customer  customer_agree                    —           —             बोल, बोलो
3   agent     agent_greet                       —           —             बात कर रही, से बात, हूँ।, खेद, उनसे
4   customer  customer_agree                    —           —             बोल, बोलो
5   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
6   customer  customer_agree                    —           —             बोल, बोलिए
7   customer  customer_agree                    —           —             कीजिए, पूरा
8   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
9   agent     agent_guide_open_link             —           —             sms, करें।, link, click
10  customer  customer_report_done              —           —             दिए
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
12  customer  customer_report_done              —           —             दिए
13  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
14  customer  customer_report_done              —           —             दिए
15  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
16  customer  customer_do_otp                   —           —             verify, कीजिए, click
17  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_address             —           —             address, pincode, locality, building, house number
24  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
25  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
26  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
27  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
32  customer  customer_acknowledge              —           —             —
33  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
34  customer  customer_acknowledge              —           —             —
35  agent     agent_request_address             —           —             address, pincode, बताएं।, जाए, fill
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
38  customer  customer_acknowledge              —           —             —
39  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
40  customer  customer_acknowledge              —           —             —
41  agent     agent_request_otp                 —           —             otp, verify
42  customer  customer_report_done              —           —             कर लिया
43  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, relationship, manager, connect, kyc
```

## Call cad04765 (transferred) — 95 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             बोलिए
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             बोलिए
5   customer  customer_ask_question             —           —             —
6   agent     agent_answer_query                —           —             apply, sms, process, जिसमें, link
7   agent     agent_send_sms_link               —           send_sms      sms, भेजती
8   customer  customer_acknowledge              —           —             —
9   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
10  customer  customer_report_sms_received      —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms, कृपया, समय, भेज, इंतज़ार
12  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, भेज, मिल
13  customer  customer_request_wait             —           —             minute
14  agent     agent_wait                        —           —             इंतज़ार
15  customer  customer_report_sms_received      —           —             मिला, just
16  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई, लिंक पर क्लिक, sms, कृपया
17  customer  customer_report_link_opened       —           —             browser, experience, using
18  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई, कृपया, बताएं, खुल
19  customer  customer_request_wait             —           —             minute
20  agent     agent_wait                        —           —             इंतज़ार
21  customer  customer_request_wait             —           —             minute
22  agent     agent_wait                        —           —             मदद, आगे, ताकि, बिल्कुल, तैयार
23  customer  customer_report_link_opened       —           —             website, apply, open
24  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, देख
25  customer  customer_do_otp                   —           —             बोल, number, mobile, डालने
26  agent     agent_request_otp                 —           send_otp      otp, करें।, मदद, कृपया, verify
27  customer  customer_do_otp                   —           —             verify
28  agent     agent_guide_apply                 —           —             कृपया, verify, बताएं, खुल, स्क्रीन
29  agent     agent_request_personal_details    —           —             हूँ।, कृपया, personal, details, आगे
30  agent     agent_request_pan                 —           —             पैन, कृपया, personal, details, सबसे
31  customer  customer_provide_pan              —           —             डाल
32  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, status
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_address             —           —             locality, building, house number, flat, कृपया
37  customer  customer_request_wait             —           —             minute
38  agent     agent_wait                        —           —             इंतज़ार
39  customer  customer_request_wait             —           —             minute
40  agent     agent_wait                        —           —             इंतज़ार
41  agent     agent_end_call                    —           —             चूंकि, उत्तर
42  customer  customer_request_wait             —           —             minute
43  agent     agent_wait                        —           —             मदद, आगे, ताकि, बिल्कुल, तैयार
44  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
45  customer  customer_greet                    —           —             hello
46  agent     agent_request_address             —           —             मदद, personal, details, भरने, चुके
47  customer  customer_request_wait             —           —             minute
48  agent     agent_wait                        —           —             इंतज़ार
49  customer  customer_request_wait             —           —             minute
50  agent     agent_wait                        —           —             मदद, आगे, बताएं, ताकि, बिल्कुल
51  customer  customer_request_wait             —           —             रुकिए, minute, almost, ख़त्म
52  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, देख, नीचे
53  customer  customer_request_wait             —           —             minute
54  agent     agent_wait                        —           —             इंतज़ार
55  customer  customer_request_wait             —           —             minute
56  agent     agent_wait                        —           —             इंतज़ार
57  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, details, self
58  customer  customer_request_wait             —           —             minute
59  agent     agent_wait                        —           —             मदद, इंतज़ार, आगे, बताएं, ताकि
60  customer  customer_provide_personal_details —           —             जिसमें, personal, details, professional, दिखा
61  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, details, self
62  customer  customer_state_employment_type    —           —             salaried
63  agent     agent_request_income              —           —             income, करें।, कृपया, रखें, home
64  customer  customer_provide_org_name         —           —             name, company
65  agent     agent_answer_query                —           —             करें।, कृपया, page, सही, समझती
66  customer  customer_provide_org_name         —           —             —
67  agent     agent_answer_query                —           —             करें।, हूँ।, मदद, बताएं, समझती
68  customer  customer_provide_org_name         frustrated  —             नहीं हो रहा, नहीं हो, company, actually, बाहर
69  agent     agent_answer_query                —           —             करें।, proceed, fill, बताएं, समझ
70  customer  customer_provide_org_name         —           —             other
71  agent     agent_request_org_name            —           —             कृपया, email, select, बताएं, पूरा
72  agent     agent_request_address             —           —             address, कृपया, complete, आगे, बताएं
73  customer  customer_provide_email            —           —             office, mail, मालूम
74  agent     agent_request_email               —           —             email, कृपया, personal, बताएं, पूरा
75  agent     agent_request_address             —           —             address, कृपया, आगे, बताएं, सही
76  customer  customer_request_wait             —           —             address, minute
77  agent     agent_wait                        —           —             इंतजार
78  customer  customer_report_address_error     —           —             code, pin
79  agent     agent_help_address_error          —           —             नहीं हो रहा, कृपया, रखें, सही, समझती
80  customer  customer_report_address_error     —           —             —
81  agent     agent_help_address_error          —           —             समझती, issue, network
82  customer  customer_report_address_error     frustrated  —             नहीं हो, office, five, code, pin
83  agent     agent_help_address_error          —           —             कृपया, सही, होगा।, समझती, office
84  customer  customer_report_address_error     —           —             six
85  agent     agent_help_address_error          —           —             समझती, पिनकोड, सिस्टम, स्वीकार, अंकों
86  customer  customer_report_address_error     —           —             code, pin
87  agent     agent_help_address_error          —           —             loan, कृपया, आगे, address, समझ
88  customer  customer_report_done              —           —             डाल
89  agent     agent_guide_apply                 —           —             करें।, कृपया, समय, बताएं।, proceed
90  customer  customer_acknowledge              —           —             load
91  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, इंतज़ार
92  customer  customer_acknowledge              —           —             —
93  agent     agent_present_final_offer         —           —             loan, offer, amount, देख, page
94  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, मदद, कृपया, relationship
```

## Call cb6c7a0a (transferred) — 27 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             बोलो
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   agent     agent_greet                       —           —             बोल, capital, aditya, birla, आपसे
5   customer  customer_request_wait             —           —             call, कृपया, line, hold, speaking
6   customer  customer_request_wait             —           —             call, कृपया, line, hold, speaking
7   agent     agent_wait                        —           —             कृपया, इंतज़ार, बताएं, तैयार, हों
8   customer  customer_agree                    —           —             बोलो
9   customer  customer_agree                    —           —             ज़रूर
10  agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, application, रखें
11  agent     agent_send_sms_link               —           —             sms, कृपया, रखें, speaker, मिल
12  customer  customer_report_sms_received      —           —             मिल
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, करें।, कृपया
14  customer  customer_acknowledge              —           —             बोल
15  agent     agent_guide_open_link             —           —             खुल गया, कृपया, बताएं, ताकि, खुल
16  customer  customer_do_otp                   —           —             number, डाल
17  agent     agent_request_otp                 —           —             कृपया, नंबर, टाइप, मोबाइल, जी।
18  customer  customer_do_otp                   —           —             मांग
19  agent     agent_request_otp                 —           —             करें।, हूँ।, मदद, कृपया, बताएं
20  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
21  customer  customer_do_otp                   —           —             otp, डाल
22  agent     agent_request_otp                 —           —             otp, कृपया, verify, complete, बताएं
23  agent     agent_request_otp                 —           —             otp, कृपया, verify, complete, जाए
24  customer  customer_acknowledge              —           —             call
25  agent     agent_wait                        —           —             loan, offer, मदद, otp, समय
26  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, offer, amount, मदद
```

## Call cd8f7d74 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   customer  customer_agree                    —           —             शुरू कर, शुरू
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, करें।, link, click
6   customer  customer_acknowledge              —           —             —
7   customer  customer_report_sms_received      —           —             link, लाख, मिल, बोलिए
8   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, otp
9   customer  customer_report_done              —           —             हो गया
10  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
11  agent     agent_ask_to_repeat               —           —             फिर से कह, माफ़
12  customer  customer_report_done              —           —             कर दिया
13  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, जाएगा।
14  customer  customer_do_otp                   —           —             बोल
15  agent     agent_request_pan                 —           —             पैन, otp, verify, page, number
16  agent     agent_ask_to_repeat               —           —             फिर से बता, माफ़
17  customer  customer_provide_pan              —           —             बोल, number
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
19  agent     agent_ask_to_repeat               —           —             call
20  customer  customer_report_done              —           —             हो गया, बोला
21  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
22  agent     agent_ask_to_repeat               —           —             एक बार फिर, कीजिए, माफ़, कहेंगे
23  customer  customer_agree                    —           —             बोलिए
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  customer  customer_report_done              —           —             बोला
26  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
27  customer  customer_report_done              —           —             कर दिया
28  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
29  customer  customer_state_employment_type    —           —             salaried
30  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_address             —           —             address, pincode, बताएं।, जाए, fill
37  customer  customer_report_done              —           —             हो गया, बोलिए
38  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
39  customer  customer_report_done              —           —             कर दिया
40  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
41  customer  customer_report_done              —           —             कर दिया, बोलिए
42  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
43  customer  customer_react_to_final_offer     —           —             offer, देख, लाख, दिखा
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call d1dea46c (transferred) — 63 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_greet                    —           —             hello, बोलिए
5   agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, approved
6   customer  customer_agree                    —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
8   agent     agent_guide_open_link             —           —             sms, करें।, link, click
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
11  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
12  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
13  agent     agent_request_otp                 —           —             otp, verify
14  customer  customer_report_done              —           —             कर लिया
15  agent     agent_request_personal_details    —           —             page, details, type, basic, होंगी।
16  customer  customer_acknowledge              —           —             ढूंढ
17  agent     agent_request_pan                 —           —             पैन, कृपया, number, बताएं।, जाए
18  customer  customer_acknowledge              —           —             —
19  agent     agent_request_pan                 —           —             pan, number, fill, know, done
20  customer  customer_acknowledge              —           —             —
21  agent     agent_request_pan                 —           —             pan, number, fill, know, done
22  customer  customer_provide_pan              —           —             fill, one, two, five, zero
23  agent     agent_request_personal_details    —           —             gender, date of birth, marital, now, enter
24  customer  customer_request_wait             —           —             one, second
25  agent     agent_request_personal_details    —           —             gender, date of birth, marital, now, enter
26  customer  customer_request_wait             —           —             one, second
27  agent     agent_request_personal_details    —           —             gender, date of birth, marital, now, enter
28  agent     agent_request_personal_details    —           —             gender, date of birth, marital, now, enter
29  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो, address, building, पूरा
30  agent     agent_help_address_error          —           —             enter, address, fill, building, सही
31  agent     agent_request_address             —           —             address, pincode, locality, building, house number
32  customer  customer_provide_address          —           —             —
33  agent     agent_request_address             —           —             address, pincode, locality, building, house number
34  customer  customer_report_done              —           —             कर दिया
35  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
36  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
37  agent     agent_ask_to_repeat               —           —             साफ़ बोल, कृपया, कीजिए, माफ़, थोड़ा
38  agent     agent_request_terms_accept        —           —             terms and condition, terms, check, conditions, दोनों
39  customer  customer_report_done              —           —             कर दिया, पूरा, submit
40  agent     agent_ask_employment_type         —           —             loan, offer, page, details, employment
41  customer  customer_acknowledge              —           —             —
42  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
43  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, थोड़ा
44  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, कहेंगे, धीरे
45  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
46  customer  customer_respond_udyam            —           —             उद्यम
47  agent     agent_offer_skip_udyam            —           —             skip, application, click, आगे, जाएगा।
48  customer  customer_skip_udyam               —           —             wait, only
49  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, इंतज़ार
50  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
51  customer  customer_other                    —           —             page, वापस
52  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
53  customer  customer_other                    —           —             loan, apply, personal, minute, lakh
54  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
55  customer  customer_request_wait             —           —             one, second
56  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
57  customer  customer_other                    —           —             otp, देख, दुबारा
58  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, relationship, manager, connect, हो।
59  customer  customer_request_wait             —           —             रुकिए, minute, दुबारा, entry
60  agent     agent_wait                        —           —             इंतज़ार
61  customer  customer_react_to_final_offer     —           —             लाख, हज़ार, रुपए
62  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call d3ca27af (transferred) — 83 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   customer  customer_agree                    —           —             चलेगा
4   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
5   agent     agent_guide_open_link             —           —             sms, link
6   customer  customer_ask_question             —           —             loan, मिल
7   agent     agent_answer_query                —           —             loan, offer, amount, process, complete
8   customer  customer_request_wait             —           —             minute
9   agent     agent_wait                        —           —             इंतज़ार
10  customer  customer_agree                    —           —             —
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
12  customer  customer_report_done              —           —             —
13  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
14  customer  customer_acknowledge              —           —             —
15  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
16  customer  customer_report_done              —           —             —
17  agent     agent_request_personal_details    —           —             details, basic
18  customer  customer_acknowledge              —           —             इधर
19  customer  customer_react_to_final_offer     —           —             दिख, lakh, one, thousand, five
20  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
21  customer  customer_ask_question             —           —             पूरा, भरना, पड़ेगा
22  agent     agent_request_personal_details    —           —             details, आगे, fill, पैन, पूरा
23  customer  customer_provide_pan              —           —             pan, number, personal, details, पूरा
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital, number, personal
25  customer  customer_other                    frustrated  —             बार बार, type, time, online, लगेगा
26  agent     agent_wait                        —           —             हूँ।, इंतज़ार, type, समझ, लें
27  customer  customer_acknowledge              —           —             —
28  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
29  customer  customer_report_done              —           —             —
30  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
31  customer  customer_report_done              —           —             proceed
32  agent     agent_request_address             —           —             address, pincode, locality, building, house number
33  customer  customer_report_done              —           —             —
34  agent     agent_request_address             —           —             address, pincode, locality, building, house number
35  customer  customer_acknowledge              —           —             —
36  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
37  customer  customer_acknowledge              —           —             —
38  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
39  customer  customer_provide_org_name         —           —             company
40  agent     agent_ask_employment_type         —           —             salaried, self-employ, करें।, monthly, self
41  customer  customer_report_done              —           —             —
42  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
43  customer  customer_report_done              —           —             process
44  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
45  customer  customer_report_done              —           —             process
46  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
47  customer  customer_report_done              —           —             process
48  customer  customer_acknowledge              —           —             दिखा, उतना, सिर्फ़
49  agent     agent_request_address             —           —             address, pincode, बताएं।, जाए, fill
50  agent     agent_request_address             —           —             address, fill, पूरा, organization, चुके
51  agent     agent_ask_employment_type         —           —             salaried, self-employ, हूँ।, कृपया, self
52  customer  customer_state_employment_type    —           —             salary
53  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
54  customer  customer_unclear                  —           —             बोल, आवाज़
55  agent     agent_acknowledge                 —           —             बताएं।, आगे, साफ़, आवाज़, सुनाई
56  customer  customer_ask_query                —           —             loan, लाख, आदित्य, capital, हज़ार
57  customer  customer_react_to_final_offer     —           —             amount, उसमें, thousand, seventy, eighty
58  agent     agent_answer_query                —           —             loan, आगे, profile, depend, चाहेंगे
59  customer  customer_ask_query                —           —             loan, पूछना
60  agent     agent_answer_query                —           —             loan, हूँ।, चाहते, सुन, जानना
61  customer  customer_ask_question             confused    —             कैसे, loan, पूरा
62  agent     agent_answer_query                —           —             loan, हूँ।, application, process, आगे
63  customer  customer_react_to_final_offer     —           —             हज़ार, पचास
64  agent     agent_present_offer               —           —             loan, application, शुरू, रुपये, आगे
65  customer  customer_query_fee                —           —             processing
66  agent     agent_confirm                     —           —             शुरू कर, हूँ।, मदद, शुरू, process
67  customer  customer_react_to_final_offer     —           —             process, thousand, sixty
68  agent     agent_present_final_offer         —           —             loan, मदद, कृपया, process, रुपये
69  customer  customer_ask_question             —           —             —
70  agent     agent_wait                        —           —             हूँ।, मदद, आगे, समझ, बढ़ें
71  customer  customer_other                    frustrated  —             बार बार, पुछ
72  agent     agent_acknowledge                 —           —             हूँ।, मदद, समझ, जानकारी, आराम
73  customer  customer_acknowledge              —           —             —
74  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
75  customer  customer_acknowledge              —           —             —
76  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
77  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
78  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
79  customer  customer_acknowledge              —           —             —
80  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
81  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
82  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
```

## Call d4dd5882 (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
3   customer  customer_agree                    —           —             बोलिए
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms, loan, करें।, कृपया, application
6   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
7   customer  customer_report_sms_received      —           —             बोलिए, message
8   agent     agent_present_offer               —           —             धन्यवाद, बताने
9   customer  customer_agree                    —           —             बोलिए
10  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
11  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, कहेंगे, दोबारा
12  customer  customer_report_link_opened       —           —             link, open, चुका
13  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, तरफ
14  customer  customer_provide_pan              —           —             pan, number, name, full, card
15  agent     agent_request_pan                 —           —             पैन, कृपया, personal, details, सबसे
16  customer  customer_ask_question             —           —             भरने
17  agent     agent_request_pan                 —           —             पैन, कृपया, personal, details, सबसे
18  customer  customer_provide_org_name         —           —             name
19  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, बताएं।
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
22  customer  customer_report_done              —           —             चुका
23  agent     agent_request_address             —           —             address, कृपया, जिसमें, भरें
24  customer  customer_ask_question             —           —             select, bank
25  agent     agent_request_address             —           —             address, कृपया, personal, details, select
26  customer  customer_ask_question             —           —             बोल, select, bank
27  agent     agent_answer_query                —           —             कृपया, बताएं।, select, धन्यवाद, लें
28  customer  customer_do_otp                   —           —             otp
29  agent     agent_request_otp                 —           —             otp, कृपया, verify, आगे, बताएं
30  customer  customer_do_otp                   —           —             verify
31  agent     agent_wait                        —           —             करें।, otp, कृपया, verify, बताएं।
32  customer  customer_provide_personal_details —           —             पूरा, detail, time, bank, accept
33  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, समय
34  agent     agent_present_final_offer         —           —             loan, offer, amount, final, देख
35  customer  customer_react_to_final_offer     —           —             scan
36  agent     agent_wait                        —           —             loan, offer, मदद, कृपया, जाए
37  agent     agent_present_final_offer         —           —             loan, offer, amount, final, देख
38  customer  customer_request_wait             —           —             wait, minute, one
39  agent     agent_wait                        —           —             बताएं।, इंतजार, तैयार, हों, बिलकुल
40  customer  customer_react_to_final_offer     —           —             loan, लाख, select, हज़ार
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, approved, pre, amount
```

## Call d4e27a05 (transferred) — 107 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_agree                    —           —             बोलिए
3   customer  customer_agree                    —           —             बोलिए
4   agent     agent_send_sms_link               —           send_sms      sms, application, process, रखें, जिसमें
5   agent     agent_guide_open_link             —           —             sms, करें।, link, check, click
6   agent     agent_guide_apply                 —           —             apply, नीचे, screen, home
7   customer  customer_acknowledge              —           —             —
8   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
9   customer  customer_other                    —           —             loan, personal, interest, thank, customer
10  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
11  customer  customer_report_applied           —           —             apply now, apply, now, उसमें, once
12  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
13  customer  customer_acknowledge              —           —             —
14  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
15  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
16  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, कहेंगे, माफ
17  customer  customer_request_wait             —           —             minute
18  agent     agent_wait                        —           —             इंतज़ार
19  customer  customer_react_to_offer           —           —             लाख, हज़ार, congratulation, लिखकर
20  agent     agent_present_offer               —           —             loan, apply, amount, करें।, now
21  customer  customer_agree                    —           —             —
22  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, नीचे
23  customer  customer_report_done              —           —             कर लिया
24  customer  customer_ask_question             —           —             personal, उसमें, पुछ, information
25  agent     agent_request_pan                 —           —             पैन, page, number, details, सबसे
26  agent     agent_request_pan                 —           —             बताएं।, जाए
27  customer  customer_agree                    —           —             —
28  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
29  customer  customer_ask_question             —           —             —
30  agent     agent_request_pan                 —           —             पैन, कृपया, number, enter, card
31  customer  customer_acknowledge              —           —             —
32  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
33  agent     agent_ask_to_repeat               —           —             फिर से बता, कीजिए, माफ़
34  customer  customer_provide_pan              —           —             pan, card, अरे, entry
35  agent     agent_request_personal_details    —           —             करें।, enter, पैन, name, full
36  customer  customer_request_wait             —           —             minute
37  agent     agent_wait                        —           —             इंतज़ार
38  customer  customer_acknowledge              —           —             कीजिए, clear
39  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
40  customer  customer_report_done              —           —             —
41  customer  customer_provide_address          —           —             address, flat, number, email, डालना
42  agent     agent_request_address             —           —             address, pincode, locality, building, house number
43  customer  customer_request_wait             —           —             wait, कीजिए, minute
44  agent     agent_wait                        —           —             इंतज़ार
45  customer  customer_acknowledge              —           —             call
46  agent     agent_request_address             —           —             address, pincode, locality, building, house number
47  customer  customer_request_wait             —           —             wait, कीजिए, बोलेंगे
48  customer  customer_ask_question             —           —             कौन सा
49  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
50  customer  customer_acknowledge              —           —             call
51  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
52  customer  customer_acknowledge              —           —             —
53  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
54  customer  customer_provide_income           —           —             income, monthly, net
55  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
56  customer  customer_provide_income           —           —             income, monthly, net
57  agent     agent_request_income              —           —             बताएं।, जाए
58  customer  customer_acknowledge              —           —             call
59  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
60  customer  customer_acknowledge              —           —             call
61  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
62  customer  customer_report_done              —           —             correct
63  agent     agent_request_email               —           —             email, now, enter, official, know
64  customer  customer_request_wait             —           —             minute
65  agent     agent_request_email               —           —             email, enter, official, know, done
66  customer  customer_report_address_error     —           —             number, mobile, इधर, एकदम, problem
67  agent     agent_request_address             —           —             address, pincode, बताएं।, जाए, fill
68  customer  customer_respond_udyam            —           —             एकदम
69  agent     agent_request_address             —           —             address, pincode, बताएं।, जाए, fill
70  customer  customer_acknowledge              —           —             call
71  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
72  customer  customer_other                    —           —             —
73  agent     agent_other                       —           —             connect, आपसे, जल्दी, issue, खेद
74  agent     agent_other                       —           —             आपसे, समस्या, जल्द, खेद, करेगी।
75  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
76  customer  customer_ask_question             —           —             call
77  agent     agent_request_otp                 —           —             otp, verify, number, बताएं।, mobile
78  agent     agent_request_otp                 —           —             otp, करें।, कृपया, verify, इंतज़ार
79  agent     agent_wait                        —           —             करें।, कृपया, इंतज़ार, screen, seconds
80  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
81  customer  customer_react_to_final_offer     —           —             देख
82  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
83  customer  customer_acknowledge              —           —             call
84  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
85  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
86  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
87  customer  customer_acknowledge              —           —             —
88  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
89  customer  customer_acknowledge              —           —             call
90  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
91  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
92  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
93  customer  customer_acknowledge              —           —             call
94  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
95  customer  customer_acknowledge              —           —             call
96  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
97  customer  customer_acknowledge              —           —             call
98  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
99  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
100 customer  customer_acknowledge              —           —             call
101 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
102 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
103 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
104 customer  customer_acknowledge              —           —             call
105 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
106 agent     agent_end_call                    —           —             goodbye, duration has been exceeded, call, now, end
```

## Call d5e52e7a (transferred) — 33 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             बात कर रही, से बात
4   customer  customer_agree                    —           —             बोलिए
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
6   agent     agent_guide_open_link             —           —             —
7   customer  customer_express_distrust         distrustful —             fraud
8   agent     agent_reassure_trust              —           —             sms, करें।, verify, page, capital
9   customer  customer_ask_question             —           —             कितना, emi, महीने
10  agent     agent_answer_query                —           —             loan, sms, amount, करें।, कृपया
11  customer  customer_agree                    —           —             बोलिए
12  agent     agent_guide_open_link             —           —             sms, करें।, link, click
13  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
14  agent     agent_ask_to_repeat               —           —             फिर से बता, कीजिए, माफ़
15  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
16  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
17  customer  customer_do_otp                   —           —             otp, दूं
18  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
19  agent     agent_request_otp                 —           —             otp, verify, receive
20  customer  customer_do_otp                   frustrated  —             नहीं हो, पाया
21  agent     agent_wait                        —           —             wait, करें।, otp, कृपया, बताएं।
22  customer  customer_ask_question             —           —             इसको
23  agent     agent_guide_open_link             —           —             sms, करें।, कृपया, link, click
24  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
25  customer  customer_agree                    —           —             —
26  agent     agent_request_otp                 —           —             otp, verify, receive
27  customer  customer_do_otp                   —           —             चौरानवे
28  agent     agent_request_otp                 —           —             otp, verify
29  customer  customer_report_done              —           —             कर लिया
30  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
31  customer  customer_react_to_final_offer     —           —             दिखा
32  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call d6f6cda6 (transferred) — 33 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_ask_question             —           —             documents
5   agent     agent_send_sms_link               —           send_sms      sms, offer, करें।, final, application
6   agent     agent_guide_open_link             —           —             sms, करें।, link, click
7   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
8   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
9   customer  customer_do_otp                   —           —             otp, proceed, डालकर
10  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
11  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
12  customer  customer_acknowledge              —           —             line
13  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
14  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
15  customer  customer_report_done              —           —             —
16  agent     agent_request_address             —           —             address, pincode, locality, building, house number
17  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
18  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
19  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
20  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
21  customer  customer_state_employment_type    —           —             self employ, self, employed
22  agent     agent_request_income              —           —             income, बताएं।, जाए, fill, monthly
23  customer  customer_report_done              —           —             हो गया, proceed
24  agent     agent_request_org_name            —           —             बताएं।, जाए, enter, registered, business
25  customer  customer_respond_udyam            —           —             उद्यम
26  agent     agent_request_udyam               —           —             udyam, करें।, page, number, mobile
27  customer  customer_respond_udyam            —           —             उद्यम, number, पड़ेगा, निकालना
28  agent     agent_offer_skip_udyam            —           —             skip, number, click, option, udyam
29  agent     agent_request_otp                 —           send_otp      otp, verify, number, बताएं।, mobile
30  customer  customer_react_to_final_offer     —           —             loan, amount, select
31  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
32  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call d99d6949 (transferred) — 52 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   agent     agent_disclose_recording          —           —             record, training, quality, call, सबसे
5   agent     agent_send_sms_link               —           send_sms      sms, loan, करें।, कृपया, application
6   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, speaker, बताएं
7   customer  customer_acknowledge              —           —             call, free
8   agent     agent_send_sms_link               —           —             sms, जिसमें, मिल, लिंक, धन्यवाद
9   customer  customer_report_sms_received      —           —             sms, मिल
10  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई, लिंक पर क्लिक, sms, कृपया
11  customer  customer_report_link_opened       —           —             खुल गई, खुल
12  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, नीचे
13  customer  customer_report_done              —           —             दबा
14  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
15  customer  customer_unclear                  —           —             बीस
16  agent     agent_request_otp                 —           —             कृपया, आगे, पूरा, ताकि, बढ़
17  customer  customer_report_done              —           —             कर दिया
18  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
19  customer  customer_provide_income           —           —             income, monthly, what, online
20  agent     agent_request_income              —           —             income, कृपया, home, आगे, monthly
21  customer  customer_provide_business_details —           —             business, company
22  agent     agent_request_org_name            —           —             करें।, कृपया, आगे, registered, बताएं
23  agent     agent_ask_to_repeat               —           —             कृपया, कीजिए, माफ़, कहेंगे, दोबारा
24  customer  customer_report_done              —           —             कर दिया, आराम, लिख
25  agent     agent_request_address             —           —             address, करें।, कृपया, बताएं।, proceed
26  agent     agent_ask_to_repeat               —           —             कृपया, माफ़, दोहरा
27  customer  customer_acknowledge              —           —             लगा
28  agent     agent_request_business_details    —           —             मदद, कृपया, details, proceed, आगे
29  customer  customer_ask_question             —           —             आगे, interest, record, जानकारी
30  agent     agent_answer_query                —           —             loan, offer, हूँ।, मदद, final
31  agent     agent_present_final_offer         —           —             final offer, offer, मदद, final, कृपया
32  customer  customer_greet                    —           —             hello
33  agent     agent_present_final_offer         —           —             loan, offer, बोल, final, कृपया
34  customer  customer_provide_address          —           —             apply, code, pin, लगा
35  agent     agent_help_address_error          —           —             हूँ।, मदद, कृपया, बताएं, समझ
36  customer  customer_report_done              frustrated  —             भर दिया, नहीं हो रहा, नहीं हो, आगे
37  agent     agent_acknowledge                 —           —             जी।
38  customer  customer_provide_business_details —           —             business
39  agent     agent_request_business_details    —           —             loan, offer, कृपया, जिसमें, समय
40  customer  customer_respond_udyam            —           —             उद्यम
41  agent     agent_request_udyam               —           —             udyam, उद्यम, कृपया, application, रखें
42  agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, कीजिए, माफ़, कहेंगे
43  customer  customer_skip_udyam               —           —             skip
44  agent     agent_offer_skip_udyam            —           —             skip, करें।, कृपया, बताएं, क्लिक
45  customer  customer_unclear                  —           —             सात
46  agent     agent_offer_skip_udyam            —           —             skip, कृपया, application, आगे, बताएं
47  customer  customer_ask_question             —           —             month, अठारह
48  agent     agent_answer_query                —           —             loan, offer, final, समझ, पूरा
49  customer  customer_react_to_final_offer     —           —             दिखा
50  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
51  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, मदद, कृपया, process
```

## Call d9aaa177 (transferred) — 27 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
5   customer  customer_agree                    —           —             —
6   customer  customer_ask_question             —           —             english, speak, much, how
7   agent     agent_present_offer               —           —             pre approved, personal loan, loan, apply, call
8   agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, जिसमें, बताएं
9   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
10  customer  customer_report_sms_received      —           —             got
11  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
12  customer  customer_report_link_opened       —           —             link, how
13  customer  customer_express_distrust         —           —             get, link, आदित्य, बिरला, some
14  agent     agent_acknowledge                 —           —             समझती, चाहती, माफ़ी
15  customer  customer_acknowledge              —           —             got
16  agent     agent_guide_open_link             —           —             लिंक पर क्लिक, करें।, हूँ।, मदद, कृपया
17  customer  customer_express_distrust         —           —             apply, call, now, get, आदित्य
18  agent     agent_reassure_trust              —           —             loan, apply, मदद, application, process
19  customer  customer_greet                    —           —             hello
20  agent     agent_guide_open_link             —           —             कृपया, बताएं, लिंक, खोल, सुन
21  customer  customer_acknowledge              —           —             approval, request
22  agent     agent_present_final_offer         —           —             loan, बिल्कुल, दिख, स्क्रीन, approval
23  customer  customer_ask_question             —           —             office, issue, धान
24  agent     agent_present_final_offer         —           —             loan, offer, amount, final, कृपया
25  customer  customer_react_to_final_offer     —           —             type, सही
26  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, मदद, कृपया, process
```

## Call db6ab517 (transferred) — 35 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             बात कर रही, से बात, कुमार
4   customer  customer_agree                    —           —             शुरू कर, शुरू
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
6   customer  customer_acknowledge              —           —             —
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
9   customer  customer_report_link_opened       —           —             —
10  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
11  customer  customer_report_sms_received      —           —             —
12  agent     agent_other                       —           —             करें।, link, check, try, internet
13  customer  customer_ask_question             —           —             भेज, whatsapp
14  agent     agent_answer_query                —           —             sms, करें।, हूँ।, कृपया, भेज
15  customer  customer_request_wait             —           —             minute
16  agent     agent_wait                        —           —             इंतज़ार
17  customer  customer_acknowledge              —           —             —
18  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
19  customer  customer_report_applied           —           —             number, click, मांग
20  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
23  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
26  agent     agent_ask_to_repeat               —           —             कृपया, कीजिए, माफ़
27  customer  customer_do_otp                   —           —             verify
28  agent     agent_request_email               —           —             email, otp, verify, बताएं।, जाए
29  customer  customer_ask_question             —           —             name, मांग
30  agent     agent_wait                        —           —             wait, otp, कृपया, बताएं।, जाए
31  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, करें।
32  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
33  customer  customer_react_to_final_offer     —           —             लाख, दिखा, कहीं, पंद्रह
34  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, relationship, manager, सही
```

## Call dc0ddbd3 (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_greet                    —           —             hello, speaking, समझना
3   customer  customer_report_link_opened       —           —             link, पूरा, open, बोलते, बोलता
4   agent     agent_guide_open_link             —           —             sms, करें।, कृपया, page, link
5   customer  customer_express_distrust         —           —             देख, पूरा, डालकर, bank, रखा
6   agent     agent_acknowledge                 —           —             internet
7   customer  customer_report_link_opened       —           —             open
8   agent     agent_guide_open_link             —           —             link, check, internet, connection
9   customer  customer_ask_question             —           —             link
10  customer  customer_other                    —           —             पूरा, minute, ऐसा, काम, भाई
11  agent     agent_wait                        —           —             इंतज़ार
12  agent     agent_ask_to_repeat               —           —             कॉल
13  agent     agent_guide_open_link             —           —             sms, करें।, process, बताएं।, link
14  customer  customer_report_sms_received      —           —             sms, link भेज, link, भेजो
15  agent     agent_send_sms_link               —           send_sms      sms, application, process, रखें, जिसमें
16  customer  customer_report_sms_received      —           —             link भेज, link, भेजा
17  agent     agent_send_sms_link               —           send_sms      sms, कृपया, भेज, link, click
18  customer  customer_ask_question             —           —             number, phone, पूरा, डालना, नया
19  agent     agent_guide_apply                 —           —             apply now, apply, sms, now, कृपया
20  customer  customer_report_applied           —           —             number, phone, open, बोलता, डालो
21  agent     agent_request_otp                 —           send_otp      otp, sms, करें।, verify, number
22  customer  customer_unclear                  —           —             two, seven
23  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
24  customer  customer_do_otp                   —           —             otp, check, पूरा, डाल, ऐसा
25  agent     agent_guide_apply                 —           —             करें।, कृपया, details, button, proceed
26  customer  customer_ask_question             —           —             phone
27  agent     agent_acknowledge                 —           —             कृपया, आपसे, थोड़ा, धैर्य, रखें।
28  customer  customer_agree                    —           —             बोलो, जल्दी
29  agent     agent_wait                        —           —             करें।, हूँ।, कृपया, connect, इंतज़ार
30  customer  customer_acknowledge              —           —             —
31  customer  customer_request_wait             —           —             call, कृपया, line, hold, रखा
32  agent     agent_wait                        —           —             इंतज़ार
33  customer  customer_ask_question             —           —             बोलो
34  agent     agent_acknowledge                 —           —             connect, आपसे, जल्दी, team
35  customer  customer_ask_question             —           —             amount, पूरा, बोला, बोले
36  agent     agent_wait                        —           —             loan, amount, कृपया, शुरू, connect
37  customer  customer_acknowledge              —           —             line, दूं, cut
38  agent     agent_wait                        —           —             कृपया, आपसे, जल्दी, लाइन, करेगी।
39  customer  customer_acknowledge              —           —             connect, line
40  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, करें।, हूँ।, कृपया, समय
41  customer  customer_agree                    —           —             —
```

## Call dcb47c49 (transferred) — 60 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             बोलो
5   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
6   customer  customer_agree                    —           —             बोलिए
7   customer  customer_query_fee                —           —             emi, monthly, कितना
8   agent     agent_answer_query                —           —             loan, offer, apply, approved, amount
9   customer  customer_agree                    —           —             देखेंगे
10  agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, कृपया, application
11  agent     agent_send_sms_link               —           —             sms, कृपया, रखें, speaker, बताएं
12  customer  customer_request_wait             —           —             minute
13  agent     agent_wait                        —           —             इंतज़ार
14  customer  customer_report_done              —           —             —
15  agent     agent_guide_open_link             —           —             खुल गया, sms, कृपया, link, बताएं
16  customer  customer_report_link_opened       —           —             खुल गया, खुल
17  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
18  customer  customer_report_applied           —           —             apply now, apply, now
19  customer  customer_do_otp                   —           —             number, mobile, registered, login
20  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, नीचे
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_terms_accept        —           —             मदद, कृपया, बताएं, खुल, बढ़िया
23  customer  customer_provide_personal_details —           —             personal, खुल
24  agent     agent_request_pan                 —           —             पैन, loan, कृपया, process, personal
25  customer  customer_provide_address          —           —             address, fill
26  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_address             —           —             address, locality, building, house number, flat
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, बताएं।, जाए
33  customer  customer_report_address_error     —           —             address, मिल, training, cannot, space
34  agent     agent_help_address_error          —           —             error, करें।, हूँ।, मदद, कृपया
35  customer  customer_report_address_error     —           —             address, one
36  agent     agent_help_address_error          —           —             error, हूँ।, मदद, कृपया, address
37  customer  customer_report_done              —           —             हो गया
38  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक, करें।, कृपया
39  customer  customer_state_employment_type    —           —             —
40  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, page, details
41  customer  customer_state_employment_type    —           —             self employ, self, employed
42  agent     agent_request_income              —           —             income, amount, कृपया, monthly, net
43  agent     agent_request_org_name            —           —             कृपया, आगे, registered, बताएं, ताकि
44  customer  customer_report_done              —           —             हो गया
45  agent     agent_request_business_details    —           —             business, कृपया, रखें, address, बताएं
46  customer  customer_report_done              —           —             हो गया
47  agent     agent_request_business_details    —           —             business, कृपया, बताएं।, सही, दिख
48  customer  customer_report_done              —           —             हो गया
49  agent     agent_request_udyam               —           —             udyam, करें।, हूँ।, मदद, कृपया
50  customer  customer_respond_udyam            —           —             उद्यम
51  agent     agent_request_udyam               —           —             udyam, करें।, कृपया, page, नीचे
52  customer  customer_skip_udyam               —           —             skip, उद्यम
53  agent     agent_offer_skip_udyam            —           —             skip, करें।, कृपया, application, जिसमें
54  customer  customer_request_wait             —           —             wait, hold
55  agent     agent_wait                        —           —             इंतज़ार
56  customer  customer_react_to_final_offer     —           —             lakh, ten, one, thousand
57  agent     agent_request_otp                 —           —             otp, करें।, कृपया, verify, जाए
58  customer  customer_ask_question             —           —             loan, six, tenure, month, thirty
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, मदद, कृपया, relationship
```

## Call e0df1c39 (transferred) — 87 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, सिंह
4   customer  customer_agree                    —           —             बोल, सिंह
5   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
6   customer  customer_agree                    —           —             बोलिए
7   agent     agent_present_offer               —           —             pre approved, loan offer, personal loan, ₹150000, 150000
8   customer  customer_greet                    —           —             hello
9   agent     agent_send_sms_link               —           send_sms      sms, loan, हूँ।, application, जिसमें
10  customer  customer_greet                    —           —             hello
11  agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, भेज, बताएं
12  customer  customer_greet                    —           —             hello
13  agent     agent_send_sms_link               —           —             sms, मिल
14  customer  customer_report_sms_received      —           —             मिल
15  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
16  agent     agent_ask_to_repeat               —           —             फिर से बता, माफ़
17  customer  customer_request_wait             —           —             minute
18  agent     agent_wait                        —           —             इंतज़ार
19  customer  customer_report_link_opened       —           —             खुल गया, खुल
20  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, नीचे
21  customer  customer_do_otp                   —           —             number, mobile, मांग
22  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, नीचे, get
23  agent     agent_request_otp                 —           —             otp, खुल, पेज, अगला, वेरीफाई
24  customer  customer_do_otp                   —           —             —
25  agent     agent_wait                        —           —             करें।, मदद, otp, कृपया, इंतज़ार
26  agent     agent_wait                        —           —             otp, कृपया, इंतज़ार, जाए, आगे
27  customer  customer_do_otp                   frustrated  —             otp, नहीं हो रहा, नहीं हो
28  agent     agent_answer_query                —           —             करें।, मदद, otp, कृपया, बताएं
29  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
30  customer  customer_unclear                  —           —             —
31  agent     agent_greet                       —           —             loan, हूँ।, मदद, otp, application
32  customer  customer_unclear                  —           —             कीजिए, बेटा
33  agent     agent_greet                       —           —             बात कर रही, से बात, सिंह
34  customer  customer_agree                    —           —             बोल, सिंह
35  agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
36  customer  customer_agree                    —           —             बोलिए
37  customer  customer_agree                    —           —             बोलिए
38  customer  customer_agree                    —           —             बोलिए
39  agent     agent_send_sms_link               —           send_sms      sms, loan, हूँ।, कृपया, application
40  customer  customer_report_sms_received      —           —             sms, miss
41  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, कृपया, बताएं
42  customer  customer_report_link_opened       —           —             खुल गया, खुल
43  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, नीचे
44  customer  customer_acknowledge              —           —             —
45  agent     agent_request_otp                 —           send_otp      otp, apply, करें।, now, कृपया
46  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़
47  customer  customer_do_otp                   —           —             number, mobile
48  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, नीचे, get
49  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
50  customer  customer_greet                    —           —             hello
51  agent     agent_greet                       —           —             बात कर रही, से बात, सिंह
52  customer  customer_agree                    —           —             —
53  agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
54  customer  customer_provide_pan              —           —             pan, name, full, card, मांग
55  agent     agent_request_pan                 —           —             पैन, हूँ।, मदद, कृपया, आगे
56  customer  customer_agree                    —           —             one, ज़रूर, computer
57  agent     agent_acknowledge                 —           —             मदद, कृपया, आगे, बताएं, पूरा
58  customer  customer_agree                    —           —             ज़रूर
59  agent     agent_guide_open_link             —           —             लिंक पर क्लिक, sms, करें।, हूँ।, मदद
60  agent     agent_guide_open_link             —           —             लिंक पर क्लिक, sms, application, शुरू, क्लिक
61  customer  customer_request_wait             —           —             —
62  agent     agent_wait                        —           —             मदद, कृपया, आगे, बताएं, बिल्कुल
63  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
64  customer  customer_provide_pan              —           —             pan, application, card
65  agent     agent_request_pan                 —           —             पैन, हूँ।, मदद, रखें, बताएं
66  customer  customer_acknowledge              —           —             —
67  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, आगे
68  customer  customer_acknowledge              —           —             ज़रूर
69  agent     agent_request_email               —           —             email, कृपया, जाए, personal, आगे
70  customer  customer_provide_pan              —           —             pan, card, load
71  agent     agent_wait                        —           —             करें।, हूँ।, मदद, कृपया, समय
72  customer  customer_ask_question             —           —             computer
73  agent     agent_reassure_trust              —           —             loan, हूँ।, मदद, कृपया, application
74  customer  customer_request_wait             —           —             hold
75  agent     agent_wait                        —           —             इंतज़ार
76  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
77  customer  customer_request_wait             —           —             minute, detail
78  agent     agent_wait                        —           —             इंतज़ार, आगे, बताएं, ताकि, बिल्कुल
79  agent     agent_ask_to_repeat               —           —             कॉल, कीजिए, माफ़
80  agent     agent_end_call                    —           —             चूंकि
81  agent     agent_clarify                     —           —             मदद, कृपया, बताएं, धन्यवाद, लिए।
82  customer  customer_react_to_final_offer     —           —             loan, लाख, रुपए
83  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
84  customer  customer_react_to_final_offer     —           —             monthly, दिख, हज़ार, lakh, nine
85  agent     agent_present_final_offer         —           —             final offer, offer, हूँ।, final, समझ
86  customer  customer_ask_question             —           —             —
```

## Call e4d8f629 (transferred) — 38 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             sorry, again, say
1   customer  customer_greet                    —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
3   customer  customer_agree                    —           —             —
4   customer  customer_agree                    —           —             बिल्कुल
5   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
6   customer  customer_acknowledge              —           —             —
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   customer  customer_report_link_opened       —           —             click
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  customer  customer_report_applied           —           —             click
11  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, number, get
12  customer  customer_report_done              —           —             —
13  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
14  customer  customer_report_done              —           —             हो गया
15  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
16  customer  customer_report_done              —           —             कर दिया
17  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
18  customer  customer_report_done              —           —             बढ़
19  agent     agent_request_address             —           —             address, pincode, locality, building, house number
20  customer  customer_report_done              —           —             भर दिया
21  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
22  customer  customer_report_done              —           —             कर दिया
23  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
24  customer  customer_state_employment_type    —           —             salaried, select
25  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
26  customer  customer_report_done              —           —             भर दिया
27  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
32  customer  customer_report_done              —           —             —
33  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, बताएं।, जाए
34  customer  customer_report_done              —           —             हो गया
35  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
36  customer  customer_react_to_final_offer     —           —             loan, offer, हज़ार, दिखाई, इधर
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call e867e396 (transferred) — 66 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
3   agent     agent_guide_open_link             —           —             sms, करें।, link, click
4   customer  customer_report_link_opened       —           —             apply, now, link, option
5   agent     agent_guide_apply                 —           —             apply now, apply, now, नीचे, screen
6   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
7   customer  customer_do_otp                   —           —             number, डाल, डालने
8   agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
9   customer  customer_report_done              —           —             कर दिया
10  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
11  customer  customer_report_done              —           —             कर दिया
12  agent     agent_request_otp                 —           —             हूँ।, मदद, verify, number, mobile
13  customer  customer_acknowledge              —           —             —
14  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
15  customer  customer_acknowledge              —           —             —
16  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
17  customer  customer_provide_pan              —           —             pan, number, birth, date
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
19  customer  customer_report_done              —           —             कर दिया
20  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
21  customer  customer_report_done              —           —             कर दिया
22  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  agent     agent_request_address             —           —             address, fill
26  customer  customer_report_done              —           —             हो गया
27  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
28  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
31  customer  customer_acknowledge              —           —             —
32  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
33  customer  customer_report_done              —           —             कर दिया
34  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
35  agent     agent_request_income              —           —             income, बताएं।, जाए, home, fill
36  customer  customer_report_done              —           —             कर दिया
37  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
38  customer  customer_provide_email            —           —             email
39  agent     agent_answer_query                —           —             हूँ।, otp, माफ़, आगे, email
40  customer  customer_report_done              —           —             कर दिया
41  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
42  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
43  customer  customer_acknowledge              —           —             —
44  agent     agent_greet                       —           —             बोल, हूँ।, तरफ, capital, aditya
45  customer  customer_acknowledge              —           —             —
46  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
47  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
48  customer  customer_other                    —           —             loading, load
49  agent     agent_wait                        —           —             loan, offer, करें।, कृपया, इंतज़ार
50  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
51  customer  customer_other                    —           —             number, दिखा, मांगा
52  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, मदद, कृपया, relationship
53  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, हूँ।, कृपया, process
54  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
56  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
57  customer  customer_react_to_final_offer     —           —             दिखा
58  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
60  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
61  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
62  customer  customer_acknowledge              —           —             समय, सही
63  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
64  customer  customer_other                    —           —             sorry
65  customer  customer_ask_question             —           —             कितने, उसको
```

## Call eac9ea27 (transferred) — 80 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, kumar
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             —
5   customer  customer_express_distrust         —           —             call, bot
6   agent     agent_reassure_trust              —           —             loan, apply, call, बोल, मदद
7   customer  customer_agree                    —           —             शुरू कर, शुरू
8   agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, कृपया, application
9   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
10  customer  customer_request_wait             —           —             एक second, check, second
11  agent     agent_wait                        —           —             sms, समय, इंतज़ार, मिल, बिल्कुल
12  customer  customer_report_sms_received      —           —             sms, link, मिला
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, कृपया, बताएं, खुल
14  customer  customer_request_wait             —           —             second
15  agent     agent_wait                        —           —             इंतज़ार, तैयार, हों, बताइए।
16  customer  customer_report_link_opened       —           —             link, open
17  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
18  customer  customer_acknowledge              —           —             —
19  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, आगे
20  customer  customer_do_otp                   —           —             otp, number, डाला
21  agent     agent_request_otp                 —           —             otp, करें।, हूँ।, मदद, कृपया
22  customer  customer_provide_personal_details —           —             name, डाल
23  agent     agent_request_personal_details    —           —             कृपया, आगे, पैन, बताएं, समझ
24  customer  customer_provide_personal_details —           —             date of birth, birth, date
25  agent     agent_request_personal_details    —           —             date of birth, marital, status, birth, date
26  customer  customer_provide_email            —           —             email, डाल
27  agent     agent_request_address             —           —             address, locality, building, house number, flat
28  customer  customer_provide_address          —           —             address, fill
29  agent     agent_request_address             —           —             address, मदद, कृपया, आगे, बताएं
30  customer  customer_provide_address          —           —             address, fill
31  agent     agent_request_address             —           —             address, कृपया, आगे, बताएं, पूरा
32  customer  customer_provide_address          —           —             address, fill
33  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, conditions, आगे
34  customer  customer_request_wait             —           —             एक second, second
35  agent     agent_wait                        —           —             समय, बिल्कुल, इंतजार
36  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक, करें।, मदद
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_terms_accept        —           —             proceed, बताएं, क्लिक, बढ़िया
39  customer  customer_report_done              —           —             proceed
40  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, details, self
41  agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़, कहेंगे
42  agent     agent_ask_to_repeat               —           —             कृपया, कीजिए, माफ़
43  customer  customer_state_employment_type    —           —             salaried, account
44  agent     agent_request_income              —           —             income, कृपया, देख, बताएं।, home
45  agent     agent_request_org_name            —           —             organization, करें।, हूँ।, मदद, कृपया
46  customer  customer_provide_email            —           —             email, official
47  agent     agent_answer_query                —           —             कृपया, बताएं।, proceed, आगे, email
48  customer  customer_provide_business_details —           —             address, डाल, line, second
49  agent     agent_request_business_details    —           —             मदद, कृपया, आगे, address, बताएं
50  agent     agent_request_business_details    —           —             कृपया, address, सही, दिख, चेक
51  customer  customer_acknowledge              —           —             —
52  agent     agent_request_otp                 —           —             otp, करें।, कृपया, verify, बताएं।
53  customer  customer_provide_email            —           —             email, बोल, proceed, official, डालने
54  agent     agent_request_email               —           —             email, करें।, हूँ।, मदद, कृपया
55  customer  customer_report_address_error     —           —             email, official, slash
56  agent     agent_answer_query                —           —             समझ, characters, वजह, special
57  customer  customer_ask_query                —           —             slash
58  agent     agent_answer_query                —           —             करें।, हूँ।, मदद, कृपया, email
59  customer  customer_ask_query                —           —             personal, email, use
60  agent     agent_answer_query                —           —             कृपया, जिसमें, personal, email, ताकि
61  customer  customer_provide_email            —           —             email, official, जगह, डाला
62  agent     agent_request_email               —           —             email, कृपया, personal, details, आगे
63  customer  customer_report_done              —           —             proceed
64  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, details, self
65  customer  customer_report_done              —           —             कर दिया, page, proceed, fill, employment
66  agent     agent_ask_employment_type         —           —             details, employment, समझ
67  customer  customer_other                    —           —             loan, application, process, further, unable
68  agent     agent_answer_query                —           —             हूँ।, मदद, कृपया, page, समझती
69  customer  customer_report_done              —           —             details, fill, दुबारा, second
70  agent     agent_wait                        —           —             समय, इंतज़ार, बिल्कुल, दिक्कत, लें।
71  customer  customer_provide_pan              —           —             pan, details, card, show
72  agent     agent_request_pan                 —           —             पैन, कृपया, जाए, details, आगे
73  agent     agent_request_pan                 —           —             पैन, कृपया, बताएं, पूरा, नंबर
74  customer  customer_acknowledge              —           —             details, proceed, wait, time, some
75  agent     agent_inform_manual_review        —           push_to_crm   कृपया, process, समय, इंतज़ार, details
76  customer  customer_react_to_final_offer     —           —             loan, personal, congratulation, instant
77  agent     agent_present_final_offer         —           —             final offer, loan, offer, approved, pre
78  customer  customer_ask_question             —           —             continue
79  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, amount, करें।, final
```

## Call eafb82a7 (transferred) — 43 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
2   customer  customer_ask_question             —           —             —
3   agent     agent_greet                       —           —             बात कर रही, से बात, बोल, आदित्य, बिरला
4   customer  customer_greet                    —           —             hello
5   customer  customer_agree                    —           —             शुरू कर, शुरू
6   agent     agent_send_sms_link               —           send_sms      sms, application, process, रखें, जिसमें
7   customer  customer_agree                    —           —             बोलिए
8   agent     agent_guide_open_link             —           —             sms, करें।, कृपया, link, click
9   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
10  customer  customer_other                    —           —             आदित्य
11  agent     agent_guide_open_link             —           —             sms, बोल, हूँ।, application, शुरू
12  customer  customer_request_wait             —           —             minute
13  agent     agent_wait                        —           —             इंतज़ार
14  customer  customer_report_sms_received      —           —             —
15  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
16  customer  customer_report_done              —           —             —
17  agent     agent_request_otp                 —           —             number, mobile, enter
18  customer  customer_report_applied           —           —             apply now, apply, now
19  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
20  customer  customer_report_done              —           —             —
21  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
22  agent     agent_ask_to_repeat               —           —             एक बार फिर, माफ़, कहेंगे
23  customer  customer_other                    —           —             lakh, one, thousand, forty
24  customer  customer_greet                    —           —             hello, शुरू, correct
25  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
26  agent     agent_guide_open_link             —           —             sms, करें।, link, click
27  customer  customer_ask_question             —           —             personal, form, profession
28  agent     agent_guide_open_link             —           —             sms, करें।, कृपया, application, शुरू
29  customer  customer_request_wait             —           —             minute
30  agent     agent_wait                        —           —             इंतज़ार
31  agent     agent_ask_to_repeat               —           —             कृपया, जवाब, सुनाई, दोहराएँ।
32  customer  customer_request_wait             —           —             minute
33  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
34  customer  customer_react_to_final_offer     —           —             lakh, one, thousand, forty, congratulations
35  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, approved, pre, amount
36  customer  customer_acknowledge              —           —             one
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
38  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
39  customer  customer_ask_question             —           —             कितने, महीने
40  agent     agent_explain_fee                 —           —             interest rate, offer, final, शुरू, interest
41  agent     agent_end_call                    —           —             हूँ।, कॉल, धन्यवाद, चूंकि, समाप्त
42  customer  customer_greet                    —           —             hello
```

## Call eeebd91b (transferred) — 41 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
3   customer  customer_agree                    —           —             बोलिए
4   agent     agent_send_sms_link               —           send_sms      sms, loan, हूँ।, कृपया, application
5   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
6   customer  customer_react_to_offer           —           —             offer
7   agent     agent_present_offer               —           —             pre approved, sms, approved, pre, amount
8   customer  customer_report_link_opened       —           —             खुल गया, खुल
9   agent     agent_guide_apply                 —           —             apply now, apply, sms, करें।, now
10  customer  customer_report_done              —           —             —
11  agent     agent_acknowledge                 —           —             —
12  agent     agent_request_otp                 —           send_otp      otp, apply, करें।, now, कृपया
13  customer  customer_provide_pan              —           —             number, डाल
14  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, get
15  customer  customer_ask_question             —           —             डाल, दूं
16  agent     agent_confirm                     —           —             हूँ।, मदद, verify, बताएं, बिल्कुल
17  customer  customer_other                    —           —             लिखा
18  agent     agent_answer_query                —           —             करें।, otp, कृपया, verify, बताएं।
19  customer  customer_other                    —           —             apply, दिखा, डालने, उसी, दुबारा
20  agent     agent_answer_query                —           —             screen, समझ, मोबाइल, login, ऐसा
21  agent     agent_request_otp                 —           send_otp      otp, करें।, हूँ।, मदद, कृपया
22  agent     agent_request_pan                 —           —             पैन, करें।, कृपया, नंबर, धन्यवाद
23  customer  customer_do_otp                   —           —             otp, डाल, दुबारा
24  agent     agent_wait                        —           —             loan, offer, हूँ।, मदद, otp
25  customer  customer_ask_question             —           —             —
26  agent     agent_answer_query                —           —             मदद, process, कॉल, पूरा, ताकि
27  customer  customer_other                    —           —             resume
28  agent     agent_answer_query                —           —             हूँ।, मदद, application, शुरू, जाए
29  customer  customer_request_wait             —           —             hold
30  agent     agent_wait                        —           —             शुरू, process, इंतज़ार, बताएं, ताकि
31  customer  customer_provide_pan              —           —             pan, number, card, मांग
32  agent     agent_request_pan                 —           —             पैन, हूँ।, मदद, कृपया, page
33  customer  customer_request_wait             —           —             hold
34  agent     agent_wait                        —           —             इंतज़ार, आगे, बताएं, ताकि, बढ़
35  customer  customer_acknowledge              —           —             details, check
36  agent     agent_wait                        —           —             मदद, कृपया, process, रखें, समय
37  customer  customer_react_to_final_offer     —           —             offer, लाख, दिखा, पांच
38  agent     agent_present_final_offer         —           —             loan, offer, देख, लाख, रुपये
39  customer  customer_agree                    —           —             आगे
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, कृपया, process, relationship
```

## Call ef64397b (transferred) — 69 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             english, speak
5   agent     agent_greet                       —           —             hello, capital, aditya, birla, speaking
6   agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, apply
7   customer  customer_agree                    —           —             —
8   agent     agent_confirm                     —           —             now, application, process, shall, begin
9   agent     agent_send_sms_link               —           send_sms      sms, link, send
10  customer  customer_agree                    —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms, application, process, link, complete
12  customer  customer_report_sms_received      —           —             sms, link, click, receive, also
13  agent     agent_guide_apply                 —           —             apply now, apply, now, screen, button
14  customer  customer_do_otp                   —           —             number, get, mobile, click
15  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
16  agent     agent_ask_to_repeat               —           —             call, sorry, there, still
17  customer  customer_do_otp                   —           —             call, get, personal, details, eligible
18  agent     agent_request_pan                 —           —             pan, page, number, details, enter
19  customer  customer_provide_pan              —           —             pan, number, enter, minute, wait
20  agent     agent_request_pan                 —           —             pan, number, enter, take, time
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital, now, enter
22  customer  customer_request_wait             —           —             details, minute, take, clear
23  agent     agent_wait                        —           —             details, enter, take, time, sure
24  agent     agent_ask_to_repeat               —           —             call, sorry, still
25  customer  customer_provide_personal_details —           —             call, enter, detail, still
26  agent     agent_request_email               —           —             email, now, personal, enter, address
27  customer  customer_provide_address          —           —             address, complete, enter, email, also
28  agent     agent_request_address             —           —             address, pincode, locality, building, house number
29  agent     agent_request_terms_accept        —           —             terms and condition, terms, button, check, conditions
30  customer  customer_accept_terms             —           —             button, click
31  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
32  customer  customer_request_wait             —           —             wait, minute
33  agent     agent_wait                        —           —             wait, take, time, sure, waiting
34  agent     agent_ask_to_repeat               —           —             sorry, repeat
35  customer  customer_provide_address          —           —             details, mail, also
36  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, select
37  customer  customer_ask_question             —           —             —
38  agent     agent_ask_employment_type         —           —             salaried, means
39  customer  customer_state_employment_type    —           —             person, only
40  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employed
41  agent     agent_request_income              —           —             income, home, monthly, net, salary
42  customer  customer_agree                    —           —             process, next
43  agent     agent_request_org_name            —           —             organization, now, enter, name, know
44  customer  customer_agree                    —           —             process, complete, all
45  agent     agent_request_org_name            —           —             organization, now, enter, name, official
46  customer  customer_ask_question             —           —             what
47  agent     agent_ask_to_repeat               —           —             call, sorry, there, still
48  customer  customer_request_wait             —           —             minute, just
49  agent     agent_wait                        —           —             chd, sure
50  customer  customer_agree                    —           —             —
51  agent     agent_request_email               —           —             email, now, enter, official, know
52  customer  customer_acknowledge              —           —             —
53  agent     agent_request_email               —           —             email, now, enter, official, know
54  customer  customer_acknowledge              —           —             next, update
55  agent     agent_request_business_details    —           —             now, address, fill, pincode, organization
56  customer  customer_ask_question             —           —             complete, point, what, next
57  agent     agent_request_business_details    —           —             now, address, fill, pincode, organization
58  customer  customer_agree                    —           —             complete
59  agent     agent_request_business_details    —           —             now, address, fill, pincode, organization
60  customer  customer_report_done              —           —             completed
61  agent     agent_request_terms_accept        —           —             now, button, proceed, click, continue
62  customer  customer_other                    —           —             complete, take, point, selfie
63  agent     agent_request_terms_accept        —           —             button, proceed, click, continue
64  customer  customer_agree                    —           —             continue
65  agent     agent_present_final_offer         —           —             final offer, loan amount and, loan, offer, amount
66  customer  customer_ask_question             —           —             process, next
67  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, process, relationship, manager, connect
68  customer  customer_greet                    —           —             hello
```

## Call f08ea751 (transferred) — 41 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, kumar
2   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
3   agent     agent_disclose_recording          —           —             सबसे, दूँ
4   agent     agent_send_sms_link               —           send_sms      sms, भेज
5   customer  customer_other                    —           —             आवाज़
6   agent     agent_answer_query                —           —             sms, करें।, कृपया, रखें, समझ
7   customer  customer_report_sms_received      —           —             —
8   agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, भेज, मिल
9   customer  customer_report_sms_received      —           —             मिला
10  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, करें।, कृपया
11  agent     agent_guide_open_link             —           —             sms, लिंक, खोल
12  customer  customer_acknowledge              —           —             sun
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक, sms, करें।, खुल
14  customer  customer_report_link_opened       —           —             खुल
15  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, मदद
16  customer  customer_other                    —           —             net, खुल, calling, खुलता
17  agent     agent_answer_query                —           —             मदद, कृपया, समय, बताएं, समझती
18  customer  customer_acknowledge              —           —             call
19  agent     agent_guide_open_link             —           —             करें।, हूँ।, कृपया, बताएं, खुल
20  customer  customer_other                    —           —             —
21  agent     agent_answer_query                —           —             apply, मदद, देर, ताकि, चाहें
22  customer  customer_report_link_opened       —           —             खुल गया, खुल
23  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, तरफ
24  agent     agent_acknowledge                 —           —             —
25  customer  customer_report_link_opened       —           —             खुल गया, खुल
26  agent     agent_guide_apply                 —           —             apply now, apply, now, बताएं, अगली
27  customer  customer_do_otp                   —           —             number, mobile, उसमें, लिखा, जगह
28  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, नीचे, get
29  customer  customer_report_done              —           —             —
30  agent     agent_request_otp                 —           send_otp      otp, कृपया, get, terms, conditions
31  customer  customer_do_otp                   —           —             otp, मांग
32  agent     agent_acknowledge                 —           —             सही
33  customer  customer_other                    —           —             forty
34  agent     agent_request_otp                 —           —             otp, sms, कृपया, रखें, कीजिए
35  customer  customer_do_otp                   —           —             —
36  agent     agent_request_otp                 —           —             otp, करें।, कृपया, verify, जाए
37  customer  customer_do_otp                   —           —             otp, डाल
38  agent     agent_wait                        —           —             loan, offer, हूँ।, मदद, कृपया
39  customer  customer_react_to_final_offer     —           —             लाख
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, offer, amount, करें।
```

## Call f13dd20b (transferred) — 50 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             record, call, recorded
1   agent     agent_greet                       —           —             hello, know, speaking, correct, person
2   customer  customer_greet                    —           —             hello, tell
3   agent     agent_present_offer               —           —             pre-approved, loan offer, loan, offer, approved
4   customer  customer_agree                    —           —             fine
5   agent     agent_send_sms_link               —           send_sms      sms, now, application, link, complete
6   customer  customer_acknowledge              —           —             fine
7   agent     agent_guide_open_link             —           —             sms, link, click, received
8   customer  customer_report_link_opened       —           —             —
9   agent     agent_guide_apply                 —           —             apply now, apply, now, screen, button
10  agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
11  agent     agent_request_otp                 —           —             otp, verify, screen, click, enter
12  agent     agent_request_pan                 —           —             pan, page, number, details, enter
13  customer  customer_provide_pan              —           —             pan, number
14  agent     agent_request_pan                 —           —             pan, call, number, type, step
15  customer  customer_provide_pan              —           —             pan, number, what, just, completed
16  agent     agent_request_personal_details    —           —             gender, date of birth, marital, now, enter
17  customer  customer_report_done              —           —             done
18  agent     agent_request_email               —           —             email, now, personal, enter, address
19  customer  customer_report_done              —           —             one, done
20  agent     agent_request_address             —           —             address, pincode, locality, building, house number
21  customer  customer_report_done              —           —             one, done, also
22  customer  customer_greet                    —           —             hello
23  agent     agent_request_address             —           —             address, details, continue, help, step
24  customer  customer_agree                    —           —             continue, next, year
25  agent     agent_request_terms_accept        —           —             terms and condition, terms, now, button, check
26  agent     agent_ask_to_repeat               —           —             sorry, repeat
27  customer  customer_report_done              —           —             data, just, all, filled, out
28  agent     agent_ask_employment_type         —           —             salaried, self-employ, now, page, details
29  customer  customer_state_employment_type    —           —             salary
30  agent     agent_request_income              —           —             income, enter, monthly, employment, salaried
31  customer  customer_report_done              —           —             done
32  agent     agent_request_org_name            —           —             organization, now, enter, name, know
33  customer  customer_ask_question             —           —             what, again
34  agent     agent_request_org_name            —           —             organization, enter, name, know, let
35  customer  customer_report_done              —           —             done
36  agent     agent_request_email               —           —             email, now, enter, official, know
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_email               —           —             email, enter, official, know, done
39  customer  customer_report_done              —           —             done, given
40  agent     agent_request_business_details    —           —             now, address, fill, pincode, organization
41  customer  customer_report_done              —           —             done, also
42  agent     agent_request_terms_accept        —           —             now, button, proceed, click, continue
43  customer  customer_report_done              —           —             done
44  agent     agent_request_otp                 —           —             otp, verify, email, registered, know
45  customer  customer_report_done              —           —             done, also
46  agent     agent_present_final_offer         —           —             final offer, loan amount and, loan, offer, amount
47  customer  customer_react_to_final_offer     —           —             loan, details, what, means, see
48  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, amount, now, relationship
49  customer  customer_query_fee                —           —             processing fee, processing, fee
```

## Call f2c92714 (transferred) — 38 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             —
5   customer  customer_ask_question             —           —             कितना, बढ़ेगा
6   customer  customer_agree                    —           —             शुरू कर, शुरू
7   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
8   agent     agent_guide_open_link             —           —             sms, करें।, link, click
9   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
10  customer  customer_report_done              —           —             —
11  agent     agent_guide_open_link             —           —             sms, करें।, link, click
12  customer  customer_report_link_opened       —           —             click
13  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
14  customer  customer_report_done              —           —             click
15  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
16  customer  customer_report_done              —           —             —
17  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
18  customer  customer_acknowledge              —           —             call
19  agent     agent_ask_to_repeat               —           —             otp, verify, कीजिए, माफ़, दोबारा
20  customer  customer_do_otp                   —           —             otp, link
21  agent     agent_guide_apply                 —           —             करें।, details, button, proceed, click
22  customer  customer_ask_question             —           —             button, proceed, ऊपर
23  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
24  agent     agent_request_otp                 —           —             otp, verify
25  customer  customer_ask_question             —           —             कैसा, मालूम
26  customer  customer_respond_udyam            —           —             otp, enter
27  agent     agent_request_otp                 —           —             otp, कृपया, verify, बताएं।, enter
28  customer  customer_request_wait             —           —             minute
29  agent     agent_wait                        —           —             इंतज़ार
30  customer  customer_do_otp                   —           —             otp, enter, four, zero
31  agent     agent_request_otp                 —           —             otp, verify
32  customer  customer_react_to_offer           —           —             two, congratulation, बोलकर, lakhs
33  agent     agent_present_offer               —           —             loan offer, loan, offer, application, लाख
34  customer  customer_agree                    —           —             आगे बढ़, आगे
35  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
36  customer  customer_react_to_final_offer     —           —             देख
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call f39df9d9 (transferred) — 46 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, kumar
2   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
3   customer  customer_agree                    —           —             बोलिए
4   customer  customer_ask_question             —           —             detail, इसको
5   agent     agent_present_offer               —           —             pre approved, personal loan, loan, sms, approved
6   customer  customer_query_fee                —           —             loan, sms, भेज, percent, कितने
7   agent     agent_explain_fee                 —           —             interest rate, offer, sms, करें।, हूँ।
8   agent     agent_send_sms_link               —           —             sms, कृपया, रखें, speaker, बताएं
9   agent     agent_guide_open_link             —           —             लिंक पर क्लिक, sms, कृपया, बताएं, खुल
10  agent     agent_ask_to_repeat               —           —             कॉल
11  customer  customer_acknowledge              —           —             —
12  agent     agent_guide_open_link             —           —             खुल गया, बिल्कुल, खुल, लिंक
13  agent     agent_ask_to_repeat               —           —             कीजिए, माफ़, बोलेंगे
14  customer  customer_report_link_opened       —           —             open
15  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
16  customer  customer_report_done              —           —             कर लिया, click
17  agent     agent_request_otp                 —           send_otp      otp, apply, करें।, कृपया, verify
18  customer  customer_report_done              —           —             हो गया, complete
19  agent     agent_request_personal_details    —           —             कृपया, application, personal, details, आगे
20  agent     agent_request_pan                 —           —             पैन, कृपया, page, personal, details
21  customer  customer_report_done              —           —             कर दिया
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, बताएं।
23  customer  customer_report_done              —           —             डाल
24  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
25  customer  customer_report_done              —           —             डाल
26  agent     agent_request_address             —           —             address, locality, building, house number, flat
27  agent     agent_clarify                     —           —             कॉल
28  customer  customer_report_done              —           —             हो गया, कर दिया, proceed
29  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, proceed, आगे
30  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, details, self
31  customer  customer_state_employment_type    —           —             salaried
32  agent     agent_request_income              —           —             income, हूँ।, कृपया, देख, बताएं।
33  customer  customer_report_done              —           —             भर दिया
34  agent     agent_request_org_name            —           —             organization, बताएं।, name, पूरा, टाइप
35  customer  customer_report_done              —           —             डाल
36  agent     agent_request_email               —           —             email, करें।, कृपया, बताएं।, पूरा
37  customer  customer_report_done              —           —             हो गया, पूरा
38  agent     agent_request_address             —           —             address, कृपया, बताएं।, पूरा, जैसा
39  customer  customer_report_done              —           —             डाल
40  agent     agent_request_address             —           —             करें।, कृपया, बताएं।, सही, पूरा
41  customer  customer_report_done              —           —             कर दिया
42  agent     agent_guide_apply                 —           —             loan, offer, करें।, कृपया, समय
43  customer  customer_report_done              —           —             कर दिया
44  agent     agent_present_final_offer         —           —             loan, offer, amount, final, देख
45  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, हूँ।, कृपया, process, relationship
```

## Call f430cd70 (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             इंतज़ार, chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             बोलो
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
7   agent     agent_guide_open_link             —           —             sms, करें।, link, click
8   customer  customer_report_done              —           —             —
9   agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
10  customer  customer_do_otp                   —           —             otp, डाल, बोलो, website
11  agent     agent_request_pan                 —           —             पैन, page, number, बताएं।, जाए
12  customer  customer_provide_pan              —           —             pan, number, fill
13  agent     agent_request_pan                 —           —             पैन, कृपया, number, बताएं।, fill
14  customer  customer_report_done              —           —             हो गया
15  agent     agent_request_personal_details    —           —             gender, date of birth, marital, करें।, बताएं।
16  customer  customer_report_done              —           —             हो गया
17  agent     agent_request_email               —           —             email, बताएं।, जाए, personal, enter
18  customer  customer_report_done              —           —             कर दिया, personal, details
19  agent     agent_request_address             —           —             address, pincode, locality, building, house number
20  customer  customer_report_done              —           —             हो गया, fill
21  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
22  customer  customer_accept_terms             —           —             button, proceed, click
23  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, कृपया, check
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
26  customer  customer_state_employment_type    —           —             self employ, self, employed
27  agent     agent_request_income              —           —             income, fill, monthly, net, business
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_business_details    —           —             business, now, enter, name, registered
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_request_business_details    —           —             business, now, enter, address, fill
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_udyam               —           —             udyam, page, number, mobile, proceed
34  customer  customer_report_done              —           —             कर दिया
35  agent     agent_request_otp                 —           —             otp, now, verify, number, mobile
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_wait                        —           —             loan, offer, otp, कृपया, verify
38  customer  customer_do_otp                   confused    —             otp, कैसे, offer, समझ, issue
39  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
40  customer  customer_react_to_final_offer     —           —             देख, लाख, दिख
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, कृपया, process, relationship
```

## Call f4c4eb40 (transferred) — 48 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, hardika
2   customer  customer_unclear                  —           —             बोलिए, दुबारा
3   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
4   customer  customer_agree                    —           —             बोलिए
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
7   agent     agent_send_sms_link               —           —             sms, मिल
8   customer  customer_report_sms_received      —           —             मिल
9   agent     agent_guide_open_link             —           —             sms, करें।, link, click
10  customer  customer_report_done              —           —             कर दिया
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
12  customer  customer_report_done              —           —             हो गया
13  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
14  customer  customer_ask_question             —           —             मतलब, number, register
15  agent     agent_answer_query                —           —             loan, application, number, mobile, capital
16  customer  customer_acknowledge              —           —             —
17  customer  customer_request_wait             —           —             minute, डाल, line, रुको
18  agent     agent_wait                        —           —             इंतज़ार
19  customer  customer_acknowledge              —           —             देख
20  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
21  customer  customer_accept_terms             —           —             box
22  agent     agent_request_terms_accept        —           —             terms and condition, terms, करें।, button, check
23  customer  customer_accept_terms             —           —             button, proceed, click
24  agent     agent_request_terms_accept        —           —             करें।, button, check, proceed, click
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
27  customer  customer_state_employment_type    —           —             salaried
28  agent     agent_request_income              —           —             income, कृपया, बताएं।, जाए, home
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_org_name            —           —             organization, करें।, बताएं।, जाए, enter
31  agent     agent_request_org_name            —           —             organization, करें।, बताएं।, जाए, enter
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_email               —           —             email, करें।, बताएं।, जाए, enter
34  customer  customer_report_done              —           —             हो गया, बोला
35  agent     agent_request_email               —           —             email, करें।, बताएं।, जाए, enter
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_request_business_details    —           —             बताएं।, जाए, address, fill, pincode
38  customer  customer_report_done              —           —             डाल
39  agent     agent_guide_apply                 —           —             करें।, button, proceed, click, आगे
40  customer  customer_report_done              —           —             हो गया
41  agent     agent_request_otp                 —           send_otp      otp, verify, बताएं।, जाए, email
42  customer  customer_report_done              —           —             हो गया
43  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
44  customer  customer_react_to_final_offer     —           —             देख
45  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
46  customer  customer_react_to_final_offer     —           —             देख
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, कृपया, process, relationship, manager
```

## Call f5019156 (transferred) — 80 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
3   customer  customer_agree                    —           —             बिल्कुल
4   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
5   customer  customer_agree                    —           —             —
6   agent     agent_disclose_recording          —           —             सबसे, बिल्कुल, दूँ
7   customer  customer_acknowledge              —           —             —
8   customer  customer_agree                    —           —             शुरू कर, शुरू
9   agent     agent_send_sms_link               —           send_sms      sms, करें।, कृपया, application, रखें
10  agent     agent_send_sms_link               —           —             sms, कृपया, रखें, मिल, फोन
11  customer  customer_report_sms_received      —           —             link, मिल
12  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई, लिंक पर क्लिक, कृपया, बताएं
13  agent     agent_guide_open_link             —           —             खुल गया, खुल, लिंक
14  customer  customer_report_link_opened       —           —             site खुल, खुल गई, खुल गया, खुल
15  agent     agent_guide_apply                 —           —             apply now, apply, now, कृपया, देख
16  customer  customer_do_otp                   —           —             apply, number, mobile, login, मांग
17  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, नीचे, get
18  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, बताएं।
19  customer  customer_provide_pan              —           —             pan, बोल, page, number, personal
20  agent     agent_request_pan                 —           —             पैन, कृपया, personal, details, बताएं
21  customer  customer_request_wait             —           —             wait
22  agent     agent_wait                        —           —             बताएं।, इंतज़ार, पैन, नंबर, लें
23  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, बताएं।
24  agent     agent_wait                        —           —             इंतज़ार, gender, पूरा
25  customer  customer_ask_question             —           —             address, card, भरना, आधार
26  agent     agent_request_address             —           —             address, आधार, कृपया, बताएं, सही
27  agent     agent_request_email               —           —             email, कृपया, address, बताएं, पूरा
28  agent     agent_request_address             —           —             address, locality, कृपया, बताएं।, सही
29  customer  customer_provide_address          —           —             address, बोल, house
30  agent     agent_request_address             —           —             address, कृपया, बताएं, पूरा, ध्यान
31  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, दोनों, चेक
32  customer  customer_report_address_error     —           —             address, डालना, slash
33  agent     agent_help_address_error          —           —             address, जैसा, official, डालें, भरें।
34  customer  customer_report_address_error     —           —             leading slash, address, training, लिखा, ऐसा
35  agent     agent_help_address_error          —           —             error, हूँ।, मदद, कृपया, address
36  customer  customer_request_wait             —           —             एक second, second
37  agent     agent_wait                        —           —             इंतज़ार
38  agent     agent_request_address             —           —             address, सही, बढ़िया
39  customer  customer_acknowledge              —           —             —
40  customer  customer_report_address_error     —           —             red, address, fill, name, building
41  agent     agent_help_address_error          —           —             करें।, हूँ।, मदद, कृपया, check
42  agent     agent_ask_to_repeat               —           —             सॉरी
43  customer  customer_report_done              —           —             दुबारा
44  agent     agent_wait                        —           —             हूँ।, कृपया, बताएं।, इंतज़ार, समझ
45  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक, proceed, आगे
46  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक, करें।, कृपया
47  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो, address
48  agent     agent_help_address_error          —           —             हूँ।, मदद, कृपया, रखें, समय
49  customer  customer_provide_address          —           —             locality, building, house number, flat, number
50  agent     agent_request_address             —           —             address, locality, building, मदद, कृपया
51  customer  customer_ask_question             —           —             —
52  agent     agent_acknowledge                 —           —             हूँ।, कृपया, बताएं, सुन
53  customer  customer_report_done              —           —             हो गया
54  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक, कृपया, proceed
55  customer  customer_state_employment_type    —           —             salaried, self employ, self employee, call, self
56  agent     agent_ask_employment_type         —           —             समझ, बिल्कुल
57  customer  customer_state_employment_type    —           —             self employ, self employee, monthly, self, income
58  agent     agent_request_income              —           —             income, कृपया, बताएं।, monthly, net
59  agent     agent_request_business_details    —           —             business, कृपया, बताएं।, registered, टाइप
60  agent     agent_request_business_details    —           —             business, shop, कृपया, बताएं।, address
61  customer  customer_report_done              —           —             खोलता
62  agent     agent_request_business_details    —           —             business, कृपया, बताएं।, address, बताएं
63  agent     agent_wait                        —           —             बताएं।, इंतज़ार, address, लें
64  agent     agent_request_address             —           —             कृपया, बताएं।, सही, business, चेक
65  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, बताएं।, proceed
66  customer  customer_respond_udyam            confused    —             क्या भरूं, number, mobile, registered, option
67  agent     agent_request_udyam               —           —             udyam, करें।, कृपया, page, number
68  agent     agent_acknowledge                 —           —             बताएं, सुन
69  customer  customer_respond_udyam            —           —             उद्यम, number, registered, ऐसा
70  customer  customer_respond_udyam            —           —             उद्यम, number, mobile, registration
71  agent     agent_offer_skip_udyam            —           —             skip, application, number, नीचे, mobile
72  customer  customer_skip_udyam               —           —             skip, anyway
73  agent     agent_inform_manual_review        —           push_to_crm   manual review, कृपया, application, इंतज़ार, बढ़िया
74  customer  customer_agree                    —           —             —
75  agent     agent_wait                        —           —             loan, offer, कृपया, समय, बताएं।
76  customer  customer_react_to_final_offer     —           —             loan amount and, final and, loan, amount, final
77  customer  customer_react_to_final_offer     —           —             lakh, one, thousand, five, six
78  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, offer, amount, करें।
79  customer  customer_acknowledge              —           —             इसको
```

## Call f510bd17 (transferred) — 54 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
3   customer  customer_agree                    —           —             बोलिए
4   agent     agent_disclose_recording          —           —             record, training, quality, loan, offer
5   agent     agent_send_sms_link               —           send_sms      sms, loan, करें।, हूँ।, कृपया
6   agent     agent_send_sms_link               —           send_sms      sms, कृपया, रखें, भेज, speaker
7   agent     agent_ask_to_repeat               —           —             फिर से कह, कीजिए, माफ़
8   customer  customer_agree                    —           —             मिल
9   agent     agent_guide_open_link             —           —             खुल गया, sms, कृपया, link, बताएं
10  customer  customer_report_link_opened       —           —             खुल गया, खुल
11  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
12  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, number
13  agent     agent_ask_to_repeat               —           —             फिर से कह, कृपया, कीजिए, माफ़, कहें
14  customer  customer_other                    —           —             चौरानवे
15  agent     agent_request_otp                 —           send_otp      otp, करें।, कृपया, verify, number
16  customer  customer_provide_pan              —           —             pan, number, निकालना
17  agent     agent_request_pan                 —           —             पैन, कृपया, बताएं, पूरा, होगा।
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital, कृपया, बताएं।
19  agent     agent_request_email               —           —             email, कृपया, personal, address, बताएं
20  agent     agent_request_address             —           —             address, locality, building, house number, flat
21  agent     agent_ask_to_repeat               —           —             माफ़, दुबारा
22  customer  customer_request_wait             —           —             minute
23  agent     agent_wait                        —           —             मदद, कृपया, बताएं।, जाए, पूरा
24  agent     agent_other                       —           —             चूंकि, प्रतिक्रिया
25  customer  customer_provide_address          —           —             number, डालना
26  agent     agent_request_address             —           —             address, कृपया, बताएं।, समझ, सही
27  customer  customer_acknowledge              —           —             feel, miss
28  agent     agent_request_address             —           —             address, कृपया, शुरू, आगे, बताएं
29  customer  customer_acknowledge              —           —             —
30  agent     agent_request_terms_accept        —           —             terms and condition, terms, कृपया, नीचे, address
31  customer  customer_acknowledge              —           —             भरा
32  agent     agent_request_terms_accept        —           —             terms and condition, terms, मदद, कृपया, proceed
33  customer  customer_acknowledge              —           —             call
34  agent     agent_request_terms_accept        —           —             terms and condition, terms, मदद, कृपया, proceed
35  agent     agent_acknowledge                 —           —             —
36  customer  customer_report_done              —           —             हो गया, proceed
37  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, page, details
38  customer  customer_state_employment_type    —           —             self employ, self employee, monthly, self, employee
39  agent     agent_request_income              —           —             income, कृपया, monthly, self, net
40  customer  customer_provide_org_name         —           —             —
41  agent     agent_acknowledge                 —           —             कृपया, समझ, गई।
42  agent     agent_request_org_name            —           —             कृपया, बताएं, पूरा, business, जाए।
43  agent     agent_request_business_details    —           —             business, करें।, कृपया, जिसमें, बताएं।
44  agent     agent_request_address             —           —             करें।, कृपया, बताएं, सही, पूरा
45  customer  customer_acknowledge              —           —             three
46  agent     agent_request_address             —           —             करें।, कृपया, आगे, बताएं, समझ
47  agent     agent_request_udyam               —           —             udyam, करें।, कृपया, number, mobile
48  customer  customer_report_done              —           —             हो गया
49  agent     agent_request_otp                 —           —             otp
50  customer  customer_report_done              —           —             हो गया
51  agent     agent_wait                        —           —             loan, offer, otp, कृपया, देख
52  customer  customer_react_to_final_offer     —           —             देख
53  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, loan, amount, हूँ।, final
```

## Call f887a187 (transferred) — 47 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, kumar
4   customer  customer_greet                    —           —             hello
5   agent     agent_greet                       —           —             बोल, capital, aditya, birla, देर
6   agent     agent_ask_to_repeat               —           —             sorry, repeat
7   customer  customer_agree                    —           —             बोलिए
8   customer  customer_react_to_offer           —           —             loan, लाख, पैसा
9   agent     agent_present_offer               —           —             ₹593000, 593000, loan, offer, लाख
10  customer  customer_ask_query                —           —             करनी, उतना, limit
11  agent     agent_answer_query                —           —             loan, amount, आगे, select, समझ
12  customer  customer_agree                    —           —             बोलिए
13  agent     agent_send_sms_link               —           send_sms      sms, करें।, हूँ।, कृपया, application
14  agent     agent_send_sms_link               —           —             sms, कृपया, रखें, speaker, बताएं
15  customer  customer_report_sms_received      —           —             मिल
16  agent     agent_guide_open_link             —           —             खुल गया, sms, कृपया, link, बताएं
17  customer  customer_report_link_opened       —           —             खुल गया, आगे, बोलिए, खुल
18  agent     agent_guide_apply                 —           —             apply now, apply, now, तरफ, नीचे
19  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, कृपया
20  customer  customer_report_done              —           —             कर दिया
21  agent     agent_request_otp                 —           —             कृपया, process, ताकि, नंबर, था।
22  agent     agent_ask_to_repeat               —           —             सॉरी
23  customer  customer_do_otp                   —           —             otp, verify, आकर
24  agent     agent_request_otp                 —           —             otp, हूँ।, मदद, verify, process
25  customer  customer_report_done              —           —             कर दिया, fill, पूरा, form
26  agent     agent_ask_employment_type         —           —             मदद, details, professional, तैयार, भरने
27  customer  customer_request_wait             —           —             एक second, second
28  agent     agent_wait                        —           —             इंतज़ार
29  customer  customer_request_wait             —           —             एक second, second
30  agent     agent_wait                        —           —             बताएं।, इंतज़ार, तैयार, हों
31  customer  customer_agree                    —           —             आगे, बोलिए
32  agent     agent_ask_employment_type         —           —             salaried, self-employ, कृपया, page, details
33  customer  customer_state_employment_type    —           —             employed
34  agent     agent_ask_to_repeat               —           —             कृपया, कीजिए, माफ़, बताएं, समझ
35  customer  customer_state_employment_type    —           —             employed
36  agent     agent_ask_employment_type         —           —             salaried, self-employ, self, employment, type
37  customer  customer_state_employment_type    —           —             employed
38  agent     agent_request_income              —           —             income, करें।, कृपया, home, monthly
39  agent     agent_request_org_name            —           —             कृपया, बताएं, पूरा, टाइप, company
40  agent     agent_request_org_name            —           —             organization, कृपया, बताएं, पूरा, बढ़िया
41  agent     agent_request_email               —           —             email, करें।, कृपया, बताएं।, official
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_request_address             —           —             address, building, कृपया, जिसमें, street
44  customer  customer_report_done              —           —             कर दिया, proceed, आगे
45  agent     agent_present_final_offer         —           —             final offer, loan, offer, amount, final
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, करें।, मदद, कृपया, process
```

## Call f8d9819a (transferred) — 84 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             chd
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   customer  customer_agree                    —           —             कहिए
5   customer  customer_query_fee                —           —             emi, कैसा, जानना
6   agent     agent_explain_fee                 —           —             interest rate, offer, final, शुरू, interest
7   customer  customer_query_fee                —           —             कीजिए, monthly, lakh, one, कितना
8   agent     agent_answer_query                —           —             loan, sms, amount, करें।, हूँ।
9   customer  customer_report_sms_received      —           —             sms
10  agent     agent_send_sms_link               —           send_sms      sms, करें।, application, process, रखें
11  agent     agent_guide_open_link             —           —             sms, करें।, link, click
12  customer  customer_report_link_opened       —           —             open, hold
13  agent     agent_wait                        —           —             इंतज़ार
14  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
15  customer  customer_report_applied           —           —             click
16  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
17  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
18  customer  customer_request_wait             —           —             रुकिए, minute, just
19  agent     agent_wait                        —           —             इंतज़ार
20  customer  customer_report_link_opened       —           —             खुल गया, application, खुल
21  agent     agent_request_pan                 —           —             पैन, number, बताएं।, जाए, fill
22  customer  customer_query_fee                confused    —             emi, कैसे, देखना
23  agent     agent_explain_fee                 —           —             interest rate, offer, final, शुरू, proceed
24  customer  customer_query_fee                —           —             check, fill
25  agent     agent_request_personal_details    —           —             page, details, basic
26  customer  customer_ask_question             —           —             verification
27  customer  customer_ask_question             —           —             home, मिल, verification, all
28  agent     agent_answer_query                —           —             loan, process, home, आगे, fill
29  agent     agent_answer_query                —           —             loan, process, home, आगे, fill
30  agent     agent_request_pan                 —           —             पैन, number, fill, चुके
31  customer  customer_state_employment_type    —           —             monthly, employment, type, income, salary
32  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
33  agent     agent_request_org_name            —           —             organization, बताएं।, जाए, enter
34  agent     agent_wait                        —           —             इंतज़ार
35  agent     agent_request_email               —           —             email, बताएं।, जाए, enter, official
36  agent     agent_ask_to_repeat               —           —             फिर से बता, कीजिए, माफ़
37  customer  customer_request_wait             —           —             minute, line, just
38  agent     agent_wait                        —           —             इंतज़ार
39  agent     agent_wait                        —           —             इंतज़ार
40  agent     agent_request_address             —           —             address, fill, organization
41  agent     agent_request_address             —           —             organization
42  customer  customer_report_done              —           —             हो गया
43  customer  customer_query_fee                —           —             processing fee, emi, amount, check, minute
44  customer  customer_query_fee                —           —             loan, apply, lakh, nine, one
45  agent     agent_explain_fee                 —           —             processing fee, emi, ₹2,950, ₹5,150, ₹1,40,000
46  customer  customer_query_fee                —           —             processing fee, apply, application, one, two
47  agent     agent_explain_fee                 —           —             processing fee, emi, ₹2,950,, ₹1,40,000,, loan
48  customer  customer_query_fee                —           —             emi, one, five, zero, right
49  agent     agent_explain_fee                 —           —             emi, ₹5,150, ₹1,40,000, loan, amount
50  customer  customer_react_to_final_offer     —           —             apply, amount, thousand, just, speaking
51  agent     agent_present_final_offer         —           —             loan, amount, eighty
52  customer  customer_query_fee                —           —             much, how
53  agent     agent_explain_fee                 —           —             emi, interest rate, loan, offer, amount
54  customer  customer_react_to_final_offer     —           —             final offer, apply, offer, final, lakh
55  agent     agent_present_final_offer         —           —             final offer, loan, offer, approved, pre
56  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
57  customer  customer_do_otp                   —           —             check
58  agent     agent_request_otp                 —           send_otp      otp, करें।, number, get, terms
59  agent     agent_request_otp                 —           send_otp      otp, करें।, verify, screen, click
60  agent     agent_end_call                    —           —             चूंकि, जवाब
61  agent     agent_guide_apply                 —           —             apply now, apply, करें।, now, देख
62  customer  customer_ask_question             frustrated  —             कब तक, apply, now, process
63  agent     agent_answer_query                —           —             process, relationship, manager, आगे, fill
64  customer  customer_query_fee                —           —             processing fee, loan, amount, now, lakh
65  customer  customer_query_fee                —           —             processing fee, two, thousand, processing, rupees
66  customer  customer_query_fee                —           —             lakh, one, thousand, means, only
67  agent     agent_explain_fee                 —           —             processing fee, ₹4,248, ₹1,15,752, ₹1,20,000, loan
68  customer  customer_query_fee                —           —             emi, now, final, one, thousand
69  agent     agent_explain_fee                 —           —             emi, ₹4,440, offer, final, application
70  customer  customer_ask_question             —           —             now, proceed, know, back, revert
71  agent     agent_answer_query                —           —             offer, now, final, relationship, manager
72  agent     agent_answer_query                —           —             offer, relationship, manager, proceed, आगे
73  customer  customer_report_applied           —           —             now, proceed, पड़ेगा, देखना, selfie
74  agent     agent_answer_query                —           —             मदद, application, verify, आगे, ताकि
75  customer  customer_request_wait             —           —             रुकिए
76  agent     agent_wait                        —           —             इंतज़ार
77  customer  customer_request_wait             —           —             minute, just
78  agent     agent_wait                        —           —             इंतज़ार
79  agent     agent_answer_query                —           —             verify, process, आगे, upload, बढ़ेगा।
80  customer  customer_ask_question             —           —             मतलब, loan, cancel, करूंगा
81  agent     agent_answer_query                —           —             loan, relationship, manager, connect, चाहें
82  customer  customer_agree                    —           —             correct
83  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect, करें।, हूँ।, कृपया, समय
```

## Call f93c02d0 (transferred) — 58 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, से बात, बोल, आदित्य, बिरला
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात, बोल, आदित्य
4   agent     agent_send_sms_link               —           send_sms      sms, application, link, complete, speaker
5   agent     agent_guide_open_link             —           —             sms, now, link, click, received
6   agent     agent_guide_apply                 —           —             apply now, apply, now, screen, button
7   agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
8   agent     agent_ask_to_repeat               —           —             call, sorry, there, still
9   agent     agent_request_otp                 —           send_otp      otp, number, get, terms, mobile
10  agent     agent_request_otp                 —           —             otp, verify, screen, click, enter
11  agent     agent_request_otp                 —           —             otp, now, verify, click, enter
12  agent     agent_request_otp                 —           —             otp, know, let, once, verified
13  customer  customer_report_done              —           —             —
14  agent     agent_request_pan                 —           —             pan, page, number, details, fill
15  customer  customer_provide_pan              —           —             pan, number
16  agent     agent_request_pan                 —           —             pan, number, capital, type, card
17  agent     agent_wait                        —           —             call, sorry, still
18  customer  customer_acknowledge              —           —             —
19  agent     agent_request_pan                 —           —             pan, number, enter, capital, card
20  agent     agent_request_personal_details    —           —             gender, date of birth, marital, now, enter
21  customer  customer_request_wait             —           —             minute, just
22  agent     agent_wait                        —           —             chd, sure
23  agent     agent_ask_to_repeat               —           —             there, still
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital, enter, name
25  agent     agent_ask_to_repeat               —           —             call, sorry, there, still
26  agent     agent_request_email               —           —             email, now, personal, enter, address
27  agent     agent_ask_to_repeat               —           —             call, sorry, still
28  customer  customer_agree                    —           —             —
29  agent     agent_request_email               —           —             email, personal, enter, address, know
30  customer  customer_report_done              —           —             done
31  agent     agent_request_address             —           —             address, pincode, locality, building, house number
32  customer  customer_report_done              —           —             done
33  agent     agent_request_terms_accept        —           —             terms and condition, terms, button, check, conditions
34  customer  customer_report_done              —           —             done
35  agent     agent_ask_employment_type         —           —             salaried, self-employ, loan, offer, page
36  customer  customer_state_employment_type    —           —             salary
37  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employment
38  agent     agent_ask_to_repeat               —           —             call, sorry, still
39  agent     agent_ask_employment_type         —           —             salaried, self-employ, monthly, self, employment
40  customer  customer_report_done              —           —             done
41  agent     agent_request_income              —           —             home, monthly, net, salary, take
42  customer  customer_report_done              —           —             done
43  agent     agent_request_org_name            —           —             organization, enter, name, know, done
44  customer  customer_report_done              —           —             done
45  agent     agent_request_email               —           —             email, enter, official, know, done
46  customer  customer_report_done              —           —             done
47  agent     agent_request_address             —           —             address, pincode, fill, organization, office
48  agent     agent_ask_to_repeat               —           —             call, sorry, there, still
49  agent     agent_guide_apply                 —           —             now, details, button, proceed, click
50  agent     agent_request_otp                 —           —             otp, verify, email, registered, know
51  agent     agent_wait                        —           —             call, sorry, there, still
52  agent     agent_request_otp                 —           —             otp, verify, email, registered, sent
53  agent     agent_ask_to_repeat               —           —             call, sorry, still
54  agent     agent_request_otp                 —           —             otp, now, verify, email, registered
55  customer  customer_report_done              —           —             done
56  agent     agent_present_final_offer         —           —             final offer, loan amount and, loan, offer, amount
57  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager, now, process, relationship, manager
```
