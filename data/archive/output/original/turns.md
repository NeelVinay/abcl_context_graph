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
4   agent     agent_greet                       —           —             —
5   customer  customer_agree                    —           —             —
6   customer  customer_request_wait             —           —             —
7   agent     agent_wait                        —           —             —
8   agent     agent_ask_to_repeat               —           —             फिर से कह
9   customer  customer_agree                    —           —             —
10  agent     agent_confirm                     —           —             —
11  agent     agent_end_call                    —           —             —
12  customer  customer_acknowledge              —           —             —
13  agent     agent_send_sms_link               —           send_sms      sms, लिंक भेज
14  customer  customer_agree                    —           —             —
15  agent     agent_send_sms_link               —           send_sms      sms
16  customer  customer_report_sms_received      —           —             —
17  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
18  customer  customer_report_sms_received      —           —             —
19  agent     agent_reassure_trust              —           —             —
20  agent     agent_send_sms_link               —           send_sms      sms
21  agent     agent_send_sms_link               —           send_sms      sms
22  customer  customer_report_sms_received      —           —             —
23  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
24  customer  customer_request_wait             —           —             —
25  agent     agent_wait                        —           —             —
26  customer  customer_react_to_final_offer     —           —             —
27  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 01cef530 (transferred) — 60 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_present_offer               —           —             pre-approved, loan offer
4   agent     agent_ask_to_repeat               —           —             फिर से कह
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms
7   customer  customer_ask_question             —           —             —
8   agent     agent_answer_query                —           —             —
9   customer  customer_agree                    —           —             —
10  agent     agent_present_offer               —           —             pre-approved, loan offer
11  customer  customer_agree                    —           —             —
12  agent     agent_send_sms_link               —           send_sms      sms
13  customer  customer_express_distrust         —           —             —
14  agent     agent_present_final_offer         —           —             final offer
15  customer  customer_react_to_final_offer     —           —             —
16  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
17  customer  customer_other                    —           —             —
18  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
19  customer  customer_acknowledge              —           —             —
20  agent     agent_other                       —           —             —
21  customer  customer_other                    —           —             —
22  agent     agent_acknowledge                 —           —             —
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_confirm                     —           —             —
25  customer  customer_acknowledge              —           —             —
26  customer  customer_acknowledge              —           —             —
27  agent     agent_inform_manual_review        —           push_to_crm   —
28  customer  customer_ask_question             —           —             —
29  agent     agent_acknowledge                 —           —             —
30  customer  customer_express_distrust         —           —             —
31  agent     agent_answer_query                —           —             —
32  customer  customer_ask_question             —           —             —
33  agent     agent_answer_query                —           —             —
34  customer  customer_ask_question             —           —             —
35  agent     agent_answer_query                —           —             —
36  customer  customer_ask_question             —           —             —
37  agent     agent_answer_query                —           —             —
38  customer  customer_ask_question             —           —             —
39  agent     agent_answer_query                —           —             —
40  customer  customer_ask_question             frustrated  —             कब तक
41  agent     agent_answer_query                —           —             —
42  customer  customer_unclear                  —           —             —
43  customer  customer_other                    —           —             —
44  agent     agent_inform_manual_review        —           push_to_crm   —
45  customer  customer_ask_question             —           —             —
46  agent     agent_answer_query                —           —             —
47  customer  customer_acknowledge              —           —             —
48  agent     agent_answer_query                —           —             —
49  customer  customer_ask_question             —           —             —
50  agent     agent_answer_query                —           —             —
51  customer  customer_express_distrust         —           —             —
52  agent     agent_transfer_to_rm              —           transfer_to_rm—
53  customer  customer_ask_question             —           —             —
54  agent     agent_answer_query                —           —             —
55  customer  customer_express_distrust         —           —             —
56  agent     agent_transfer_to_rm              —           transfer_to_rm—
57  customer  customer_acknowledge              —           —             —
58  agent     agent_acknowledge                 —           —             —
59  customer  customer_acknowledge              —           —             —
```

## Call 072e5c6d (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_report_link_opened       —           —             —
7   agent     agent_guide_apply                 —           —             apply now
8   customer  customer_report_done              —           —             —
9   agent     agent_request_otp                 —           send_otp      otp
10  customer  customer_report_done              —           —             —
11  agent     agent_request_otp                 —           send_otp      otp
12  agent     agent_request_otp                 —           —             otp
13  customer  customer_report_done              —           —             कर दिया
14  agent     agent_request_pan                 —           —             पैन
15  agent     agent_ask_to_repeat               —           —             फिर से बता
16  customer  customer_report_done              —           —             हो गया
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_email               —           —             email
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_address             —           —             address, pincode, locality, building, house number
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_terms_accept        —           —             terms and condition, terms
24  agent     agent_ask_employment_type         —           —             salaried, self-employ
25  customer  customer_state_employment_type    —           —             self employ
26  agent     agent_request_income              —           —             income
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_org_name            —           —             —
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_business_details    —           —             business
31  customer  customer_report_done              —           —             —
32  agent     agent_request_udyam               —           —             udyam
33  customer  customer_skip_udyam               —           —             —
34  agent     agent_offer_skip_udyam            —           —             skip
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_otp                 —           send_otp      otp
37  customer  customer_report_done              —           —             हो गया
38  agent     agent_present_final_offer         —           —             final offer
39  customer  customer_react_to_final_offer     —           —             —
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
41  customer  customer_other                    —           —             —
```

## Call 07ea36d9 (transferred) — 71 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_ask_question             —           —             —
3   agent     agent_greet                       —           —             —
4   customer  customer_other                    —           —             —
5   agent     agent_acknowledge                 —           —             —
6   customer  customer_request_wait             —           —             एक second
7   agent     agent_wait                        —           —             —
8   customer  customer_agree                    —           —             —
9   agent     agent_greet                       —           —             —
10  customer  customer_agree                    —           —             —
11  customer  customer_query_fee                —           —             interest rate
12  agent     agent_answer_query                —           —             —
13  customer  customer_agree                    —           —             आगे बढ़
14  customer  customer_express_distrust         —           —             —
15  agent     agent_reassure_trust              —           —             —
16  agent     agent_ask_to_repeat               —           —             —
17  agent     agent_send_sms_link               —           send_sms      sms
18  agent     agent_send_sms_link               —           send_sms      sms
19  agent     agent_guide_open_link             —           —             खुल गया
20  customer  customer_report_link_opened       —           —             खुल गया
21  agent     agent_guide_apply                 —           —             apply now
22  customer  customer_report_applied           —           —             —
23  agent     agent_request_otp                 —           —             —
24  customer  customer_acknowledge              —           —             —
25  agent     agent_request_otp                 —           send_otp      otp
26  customer  customer_do_otp                   —           —             otp
27  agent     agent_clarify                     —           —             —
28  customer  customer_report_link_opened       —           —             खुल गया
29  agent     agent_request_pan                 —           —             पैन
30  customer  customer_provide_pan              —           —             pan
31  agent     agent_wait                        —           —             —
32  agent     agent_ask_to_repeat               —           —             फिर से कह
33  customer  customer_report_done              —           —             —
34  agent     agent_request_personal_details    —           —             gender, date of birth, marital
35  agent     agent_ask_to_repeat               —           —             —
36  customer  customer_report_done              —           —             —
37  agent     agent_request_email               —           —             email
38  agent     agent_ask_to_repeat               —           —             —
39  customer  customer_request_wait             —           —             —
40  agent     agent_request_email               —           —             email
41  agent     agent_request_address             —           —             address, locality, building, house number, flat
42  customer  customer_report_done              —           —             हो गया
43  agent     agent_wait                        —           —             —
44  customer  customer_provide_personal_details —           —             —
45  agent     agent_answer_query                —           —             —
46  customer  customer_ask_question             —           —             मतलब
47  agent     agent_request_udyam               —           —             udyam
48  customer  customer_state_employment_type    —           —             self employ
49  agent     agent_offer_skip_udyam            —           —             skip
50  customer  customer_acknowledge              —           —             —
51  agent     agent_wait                        —           —             —
52  agent     agent_request_udyam               —           —             udyam
53  agent     agent_request_udyam               —           —             udyam
54  customer  customer_request_wait             —           —             —
55  agent     agent_wait                        —           —             —
56  agent     agent_wait                        —           —             —
57  agent     agent_ask_to_repeat               —           —             —
58  customer  customer_other                    —           —             —
59  agent     agent_wait                        —           —             —
60  customer  customer_acknowledge              —           —             —
61  agent     agent_request_org_name            —           —             —
62  customer  customer_ask_question             —           —             —
63  agent     agent_answer_query                —           —             —
64  customer  customer_react_to_offer           —           —             —
65  customer  customer_react_to_offer           —           —             —
66  agent     agent_present_offer               —           —             —
67  customer  customer_react_to_offer           —           —             —
68  agent     agent_present_final_offer         —           —             —
69  agent     agent_present_final_offer         —           —             —
70  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 08145c39 (transferred) — 56 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   agent     agent_present_offer               —           —             —
6   customer  customer_agree                    —           —             —
7   customer  customer_ask_question             —           —             —
8   agent     agent_answer_query                —           —             —
9   agent     agent_ask_to_repeat               —           —             फिर से कह
10  customer  customer_agree                    —           —             —
11  agent     agent_present_offer               —           —             —
12  customer  customer_agree                    —           —             —
13  customer  customer_agree                    —           —             —
14  agent     agent_send_sms_link               —           send_sms      sms
15  agent     agent_guide_open_link             —           —             —
16  customer  customer_request_wait             —           —             wait
17  agent     agent_guide_apply                 —           —             apply now
18  customer  customer_request_wait             —           —             wait
19  agent     agent_wait                        —           —             —
20  customer  customer_greet                    —           —             hello
21  agent     agent_request_otp                 —           send_otp      otp
22  customer  customer_ask_question             —           —             —
23  agent     agent_answer_query                —           —             —
24  customer  customer_report_applied           —           —             —
25  agent     agent_request_otp                 —           send_otp      otp
26  customer  customer_ask_question             —           —             —
27  agent     agent_request_otp                 —           —             —
28  customer  customer_agree                    —           —             —
29  customer  customer_ask_question             —           —             —
30  agent     agent_guide_open_link             —           —             —
31  customer  customer_unclear                  —           —             —
32  agent     agent_guide_open_link             —           —             —
33  customer  customer_request_wait             —           —             —
34  agent     agent_guide_apply                 —           —             apply now
35  agent     agent_request_otp                 —           send_otp      otp
36  customer  customer_request_wait             —           —             एक second, रुकिए
37  agent     agent_wait                        —           —             —
38  customer  customer_ask_question             —           —             कौन सा
39  agent     agent_answer_query                —           —             —
40  customer  customer_ask_question             —           —             —
41  agent     agent_request_otp                 —           —             —
42  customer  customer_greet                    —           —             hello
43  agent     agent_request_otp                 —           send_otp      otp
44  customer  customer_do_otp                   —           —             otp
45  agent     agent_request_otp                 —           send_otp      otp
46  customer  customer_do_otp                   —           —             otp
47  agent     agent_wait                        —           —             wait
48  customer  customer_ask_question             —           —             —
49  agent     agent_wait                        —           —             wait
50  customer  customer_do_otp                   —           —             otp
51  agent     agent_request_otp                 —           —             otp
52  customer  customer_report_done              —           —             हो गया
53  agent     agent_present_final_offer         —           —             final offer
54  customer  customer_react_to_final_offer     —           —             —
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 0aed797d (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_present_offer               —           —             —
4   customer  customer_agree                    —           —             —
5   customer  customer_ask_question             —           —             मतलब
6   agent     agent_send_sms_link               —           send_sms      sms
7   customer  customer_agree                    —           —             —
8   agent     agent_guide_open_link             —           —             —
9   agent     agent_ask_to_repeat               —           —             —
10  customer  customer_acknowledge              —           —             —
11  agent     agent_guide_apply                 —           —             apply now
12  customer  customer_report_link_opened       —           —             —
13  agent     agent_guide_open_link             —           —             —
14  customer  customer_request_wait             —           —             —
15  agent     agent_wait                        —           —             —
16  customer  customer_request_wait             —           —             —
17  agent     agent_wait                        —           —             —
18  customer  customer_other                    —           —             —
19  agent     agent_reassure_trust              —           —             —
20  customer  customer_report_sms_received      —           —             —
21  agent     agent_send_sms_link               —           send_sms      sms
22  agent     agent_guide_open_link             —           —             —
23  customer  customer_report_sms_received      —           —             —
24  agent     agent_guide_open_link             —           —             —
25  customer  customer_other                    —           —             —
26  agent     agent_other                       —           —             —
27  customer  customer_unclear                  —           —             —
28  agent     agent_greet                       —           —             नमस्ते
29  customer  customer_unclear                  —           —             —
30  agent     agent_greet                       —           —             नमस्ते
31  customer  customer_greet                    —           —             hello
32  agent     agent_ask_to_repeat               —           —             —
33  customer  customer_unclear                  —           —             —
34  agent     agent_ask_to_repeat               —           —             —
35  customer  customer_report_link_opened       —           —             —
36  agent     agent_request_otp                 —           —             —
37  customer  customer_do_otp                   —           —             otp
38  agent     agent_request_otp                 —           —             —
39  customer  customer_do_otp                   —           —             —
40  agent     agent_acknowledge                 —           —             —
41  customer  customer_react_to_final_offer     —           —             —
42  customer  customer_query_fee                —           —             —
43  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
44  customer  customer_acknowledge              —           —             —
```

## Call 0d1b55e2 (transferred) — 51 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             —
1   customer  customer_greet                    —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
3   customer  customer_agree                    —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_guide_open_link             —           —             —
7   customer  customer_report_link_opened       —           —             —
8   agent     agent_guide_apply                 —           —             apply now
9   customer  customer_request_wait             —           —             —
10  agent     agent_wait                        —           —             —
11  customer  customer_agree                    —           —             —
12  agent     agent_request_otp                 —           send_otp      otp
13  customer  customer_ask_question             —           —             —
14  agent     agent_answer_query                —           —             —
15  customer  customer_ask_question             —           —             —
16  agent     agent_answer_query                —           —             —
17  customer  customer_ask_question             —           —             —
18  agent     agent_answer_query                —           —             —
19  customer  customer_ask_question             —           —             —
20  agent     agent_request_otp                 —           send_otp      otp
21  customer  customer_do_otp                   —           —             —
22  agent     agent_request_pan                 —           —             पैन
23  customer  customer_report_done              —           —             हो गया, कर दिया
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_request_email               —           —             email
27  customer  customer_report_done              —           —             कर दिया
28  agent     agent_request_address             —           —             address, pincode, locality, building, house number
29  customer  customer_report_done              —           —             कर दिया
30  agent     agent_request_terms_accept        —           —             terms and condition, terms
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_ask_employment_type         —           —             salaried, self-employ
33  agent     agent_ask_to_repeat               —           —             साफ़ बोल
34  customer  customer_state_employment_type    —           —             salaried
35  agent     agent_ask_employment_type         —           —             salaried, self-employ
36  customer  customer_state_employment_type    —           —             salaried
37  agent     agent_request_income              —           —             income
38  customer  customer_acknowledge              —           —             —
39  agent     agent_request_org_name            —           —             organization
40  customer  customer_ask_question             —           —             —
41  agent     agent_request_email               —           —             email
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_request_business_details    —           —             —
44  customer  customer_report_done              —           —             कर दिया
45  agent     agent_request_terms_accept        —           —             —
46  agent     agent_request_otp                 —           send_otp      otp
47  customer  customer_report_done              —           —             कर दिया
48  agent     agent_present_final_offer         —           —             final offer
49  customer  customer_react_to_final_offer     —           —             —
50  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 12913998 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_guide_open_link             —           —             —
7   customer  customer_report_done              —           —             कर दिया
8   agent     agent_guide_apply                 —           —             apply now
9   customer  customer_report_done              —           —             हो गया
10  agent     agent_request_otp                 —           send_otp      otp
11  customer  customer_report_done              —           —             हो गया
12  agent     agent_request_personal_details    —           —             —
13  agent     agent_request_pan                 —           —             पैन
14  customer  customer_report_done              —           —             हो गया
15  agent     agent_request_personal_details    —           —             gender, date of birth, marital
16  agent     agent_ask_to_repeat               —           —             फिर से कह
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_email               —           —             email
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_address             —           —             address, pincode, locality, building, house number
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_terms_accept        —           —             terms and condition, terms
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_ask_employment_type         —           —             salaried, self-employ
26  agent     agent_ask_employment_type         —           —             salaried, self-employ
27  customer  customer_state_employment_type    —           —             self employ
28  agent     agent_request_income              —           —             income
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_business_details    —           —             business
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_business_details    —           —             business
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_udyam               —           —             udyam
35  customer  customer_skip_udyam               —           —             —
36  agent     agent_offer_skip_udyam            —           —             skip
37  agent     agent_ask_to_repeat               —           —             —
38  customer  customer_request_wait             —           —             wait
39  agent     agent_acknowledge                 —           —             —
40  agent     agent_request_otp                 —           send_otp      otp
41  customer  customer_react_to_final_offer     —           —             —
42  agent     agent_present_final_offer         —           —             final offer
43  customer  customer_react_to_final_offer     —           —             —
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 133230ad (transferred) — 24 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_send_sms_link               —           send_sms      sms
4   agent     agent_guide_open_link             —           —             —
5   agent     agent_guide_apply                 —           —             apply now
6   customer  customer_other                    —           —             —
7   agent     agent_other                       —           —             —
8   customer  customer_acknowledge              —           —             —
9   agent     agent_guide_open_link             —           —             खुल गया
10  agent     agent_ask_to_repeat               —           —             फिर से कह
11  customer  customer_other                    —           —             —
12  agent     agent_guide_open_link             —           —             —
13  customer  customer_do_otp                   —           —             otp
14  agent     agent_wait                        —           —             wait
15  agent     agent_request_otp                 —           —             otp
16  customer  customer_do_otp                   —           —             otp
17  agent     agent_wait                        —           —             wait
18  agent     agent_wait                        —           —             wait
19  agent     agent_ask_to_repeat               —           —             —
20  customer  customer_acknowledge              —           —             —
21  agent     agent_present_final_offer         —           —             final offer
22  customer  customer_react_to_final_offer     —           —             —
23  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 16a9075f (transferred) — 22 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_other                    —           —             —
4   agent     agent_ask_to_repeat               —           —             फिर से कह
5   customer  customer_agree                    —           —             शुरू कर
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_guide_open_link             —           —             —
8   agent     agent_ask_to_repeat               —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_report_done              —           —             कर दिया
11  agent     agent_request_otp                 —           send_otp      otp
12  customer  customer_do_otp                   —           —             —
13  agent     agent_request_otp                 —           send_otp      otp
14  agent     agent_ask_to_repeat               —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  agent     agent_ask_to_repeat               —           —             —
17  agent     agent_request_otp                 —           send_otp      otp
18  customer  customer_do_otp                   —           —             —
19  customer  customer_provide_personal_details —           —             —
20  agent     agent_present_final_offer         —           —             final offer
21  customer  customer_ask_question             —           —             —
```

## Call 190be58f (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms
7   customer  customer_react_to_offer           —           —             —
8   customer  customer_greet                    —           —             hello
9   agent     agent_present_offer               —           —             —
10  customer  customer_acknowledge              —           —             —
11  agent     agent_guide_open_link             —           —             —
12  customer  customer_acknowledge              —           —             —
13  agent     agent_guide_open_link             —           —             खुल गया
14  agent     agent_guide_open_link             —           —             —
15  customer  customer_acknowledge              —           —             —
16  agent     agent_guide_apply                 —           —             apply now
17  customer  customer_other                    —           —             —
18  agent     agent_answer_query                —           —             —
19  customer  customer_other                    —           —             —
20  agent     agent_send_sms_link               —           send_sms      sms
21  customer  customer_report_sms_received      —           —             —
22  agent     agent_guide_open_link             —           —             —
23  customer  customer_report_link_opened       frustrated  —             नहीं हो
24  agent     agent_guide_open_link             —           —             —
25  customer  customer_other                    —           —             —
26  agent     agent_other                       —           —             —
27  customer  customer_ask_question             —           —             —
28  agent     agent_wait                        —           —             —
29  agent     agent_ask_to_repeat               —           —             फिर से कह
30  customer  customer_request_wait             —           —             wait
31  agent     agent_wait                        —           —             wait
32  customer  customer_ask_question             —           —             —
33  agent     agent_wait                        —           —             —
34  customer  customer_report_link_opened       —           —             —
35  agent     agent_guide_apply                 —           —             apply now
36  customer  customer_react_to_offer           —           —             loan offer
37  agent     agent_present_offer               —           —             loan offer
38  customer  customer_report_applied           —           —             apply now
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
40  customer  customer_ask_question             —           —             —
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 1d8b48d4 (transferred) — 48 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_agree                    —           —             —
7   agent     agent_guide_open_link             —           —             —
8   agent     agent_guide_apply                 —           —             apply now
9   customer  customer_report_sms_received      —           —             —
10  agent     agent_other                       —           —             —
11  customer  customer_acknowledge              —           —             —
12  agent     agent_guide_open_link             —           —             —
13  customer  customer_other                    —           —             —
14  agent     agent_greet                       —           —             —
15  customer  customer_request_wait             —           —             —
16  agent     agent_wait                        —           —             —
17  customer  customer_acknowledge              —           —             —
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_acknowledge              —           —             —
20  agent     agent_request_otp                 —           send_otp      otp
21  customer  customer_request_wait             —           —             —
22  agent     agent_wait                        —           —             —
23  customer  customer_do_otp                   —           —             otp
24  agent     agent_wait                        —           —             wait
25  customer  customer_request_wait             —           —             wait
26  agent     agent_request_otp                 —           —             otp
27  customer  customer_do_otp                   —           —             —
28  agent     agent_wait                        —           —             wait
29  customer  customer_acknowledge              —           —             —
30  agent     agent_request_otp                 —           —             otp
31  customer  customer_do_otp                   —           —             —
32  agent     agent_wait                        —           —             wait
33  customer  customer_report_link_opened       —           —             खुल गया
34  agent     agent_guide_apply                 —           —             apply now
35  agent     agent_request_address             —           —             —
36  customer  customer_other                    —           —             —
37  agent     agent_wait                        —           —             —
38  customer  customer_acknowledge              —           —             —
39  agent     agent_guide_open_link             —           —             —
40  customer  customer_report_done              —           —             कर दिया
41  agent     agent_present_final_offer         —           —             final offer
42  customer  customer_agree                    —           —             —
43  agent     agent_present_final_offer         —           —             final offer
44  agent     agent_present_final_offer         —           —             final offer
45  agent     agent_present_final_offer         —           —             final offer
46  customer  customer_report_done              —           —             हो गया
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 1dfb93a4 (transferred) — 49 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             —
1   customer  customer_greet                    —           —             hello
2   agent     agent_greet                       —           —             —
3   customer  customer_agree                    —           —             —
4   customer  customer_other                    —           —             —
5   agent     agent_present_offer               —           —             loan offer, personal loan, ₹200000, 200000
6   customer  customer_agree                    —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   agent     agent_send_sms_link               —           send_sms      sms
9   customer  customer_report_sms_received      —           —             —
10  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
11  agent     agent_ask_to_repeat               —           —             फिर से कह
12  customer  customer_report_link_opened       —           —             खुल गया
13  agent     agent_guide_apply                 —           —             apply now
14  customer  customer_do_otp                   —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_other                    —           —             —
17  agent     agent_request_pan                 —           —             पैन
18  agent     agent_end_call                    —           —             —
19  customer  customer_greet                    —           —             hello
20  agent     agent_request_pan                 —           —             पैन
21  customer  customer_provide_pan              —           —             pan
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital
23  customer  customer_report_done              —           —             भर दिया
24  agent     agent_request_email               —           —             email
25  customer  customer_acknowledge              —           —             —
26  agent     agent_request_address             —           —             address
27  agent     agent_request_address             —           —             address
28  customer  customer_report_done              —           —             —
29  agent     agent_request_terms_accept        —           —             terms and condition, terms
30  agent     agent_ask_to_repeat               —           —             फिर से कह
31  customer  customer_ask_question             —           —             —
32  agent     agent_ask_employment_type         —           —             salaried, self-employ
33  customer  customer_state_employment_type    —           —             self employ, self employee
34  agent     agent_request_income              —           —             income
35  customer  customer_report_done              —           —             —
36  agent     agent_request_org_name            —           —             —
37  customer  customer_report_done              —           —             —
38  agent     agent_request_business_details    —           —             business
39  customer  customer_report_done              —           —             —
40  agent     agent_request_business_details    —           —             business
41  customer  customer_report_done              —           —             हो गया, कर दिया
42  agent     agent_acknowledge                 —           —             —
43  customer  customer_request_wait             —           —             wait
44  agent     agent_wait                        —           —             —
45  customer  customer_acknowledge              —           —             —
46  agent     agent_present_final_offer         —           —             —
47  customer  customer_react_to_final_offer     —           —             —
48  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 1ea57f23 (transferred) — 71 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_greet                    —           —             बात कर रही, से बात
5   agent     agent_greet                       —           —             बात कर रही, से बात
6   agent     agent_greet                       —           —             —
7   customer  customer_agree                    —           —             —
8   agent     agent_greet                       —           —             —
9   agent     agent_disclose_recording          —           —             record, training, quality
10  customer  customer_ask_question             —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms
12  agent     agent_ask_to_repeat               —           —             फिर से कह
13  customer  customer_report_sms_received      —           —             sms
14  agent     agent_send_sms_link               —           send_sms      sms
15  agent     agent_send_sms_link               —           —             —
16  customer  customer_report_sms_received      —           —             sms
17  agent     agent_guide_open_link             —           —             —
18  customer  customer_report_sms_received      —           —             sms
19  agent     agent_guide_open_link             —           —             खुल गया
20  customer  customer_report_link_opened       —           —             खुल गया
21  agent     agent_guide_apply                 —           —             apply now
22  agent     agent_guide_apply                 —           —             apply now
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_request_otp                 —           send_otp      otp
25  customer  customer_provide_pan              —           —             pan
26  agent     agent_request_otp                 —           —             otp
27  customer  customer_report_done              —           —             —
28  agent     agent_request_pan                 —           —             पैन
29  customer  customer_acknowledge              —           —             —
30  agent     agent_request_pan                 —           —             पैन
31  agent     agent_ask_to_repeat               —           —             फिर से कह
32  customer  customer_provide_personal_details —           —             —
33  agent     agent_request_pan                 —           —             पैन
34  agent     agent_confirm                     —           —             आगे बढ़
35  customer  customer_other                    —           —             —
36  agent     agent_other                       —           —             —
37  customer  customer_greet                    —           —             hello
38  agent     agent_wait                        —           —             —
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_pan                 —           —             पैन
41  customer  customer_state_employment_type    —           —             —
42  agent     agent_ask_employment_type         —           —             salaried, self-employ
43  customer  customer_state_employment_type    —           —             self employ
44  agent     agent_request_income              —           —             income
45  agent     agent_request_org_name            —           —             —
46  agent     agent_wait                        —           —             —
47  customer  customer_agree                    —           —             —
48  agent     agent_confirm                     —           —             —
49  customer  customer_acknowledge              —           —             —
50  agent     agent_acknowledge                 —           —             —
51  customer  customer_respond_udyam            —           —             उद्यम
52  agent     agent_request_udyam               —           —             उद्यम
53  customer  customer_respond_udyam            —           —             उद्यम
54  agent     agent_offer_skip_udyam            —           —             skip
55  customer  customer_respond_udyam            —           —             —
56  agent     agent_request_udyam               —           —             उद्यम
57  customer  customer_acknowledge              —           —             —
58  agent     agent_request_udyam               —           —             उद्यम
59  agent     agent_request_otp                 —           send_otp      otp
60  customer  customer_acknowledge              —           —             —
61  agent     agent_wait                        —           —             —
62  customer  customer_ask_question             —           —             —
63  agent     agent_request_udyam               —           —             उद्यम
64  customer  customer_acknowledge              —           —             —
65  agent     agent_request_udyam               —           —             —
66  agent     agent_request_otp                 —           send_otp      otp
67  agent     agent_wait                        —           —             —
68  agent     agent_wait                        —           —             —
69  agent     agent_present_final_offer         —           —             —
70  agent     agent_present_final_offer         —           —             —
```

## Call 1fb2c1fa (transferred) — 68 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             —
6   customer  customer_agree                    —           —             —
7   customer  customer_query_fee                —           —             —
8   agent     agent_answer_query                —           —             —
9   agent     agent_send_sms_link               —           —             sms
10  customer  customer_greet                    —           —             hello
11  agent     agent_send_sms_link               —           —             sms
12  customer  customer_report_applied           —           —             apply now
13  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गया, लिंक पर क्लिक
14  customer  customer_report_link_opened       —           —             खुल गया
15  agent     agent_guide_apply                 —           —             —
16  customer  customer_greet                    —           —             hello
17  agent     agent_guide_apply                 —           —             apply now
18  customer  customer_do_otp                   —           —             —
19  agent     agent_request_otp                 —           send_otp      otp
20  customer  customer_do_otp                   —           —             —
21  agent     agent_request_pan                 —           —             पैन
22  customer  customer_acknowledge              —           —             —
23  agent     agent_request_personal_details    —           —             —
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_request_email               —           —             email
26  customer  customer_report_done              —           —             हो गया
27  agent     agent_request_address             —           —             —
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_terms_accept        —           —             terms and condition, terms
30  customer  customer_ask_question             —           —             मतलब
31  agent     agent_request_terms_accept        —           —             terms and condition, terms
32  customer  customer_other                    —           —             —
33  agent     agent_confirm                     —           —             —
34  customer  customer_provide_income           —           —             income
35  agent     agent_confirm                     —           —             —
36  customer  customer_ask_question             —           —             —
37  agent     agent_request_income              —           —             income
38  customer  customer_request_wait             —           —             wait
39  agent     agent_wait                        —           —             —
40  customer  customer_ask_question             —           —             मतलब
41  agent     agent_request_org_name            —           —             organization
42  customer  customer_request_wait             —           —             wait
43  agent     agent_wait                        —           —             —
44  customer  customer_request_wait             —           —             wait
45  agent     agent_wait                        —           —             —
46  customer  customer_acknowledge              —           —             —
47  agent     agent_request_income              —           —             income
48  customer  customer_request_wait             —           —             wait
49  agent     agent_wait                        —           —             —
50  agent     agent_ask_to_repeat               —           —             फिर से कह
51  customer  customer_request_wait             —           —             wait
52  agent     agent_wait                        —           —             —
53  customer  customer_request_wait             —           —             wait
54  agent     agent_wait                        —           —             —
55  customer  customer_request_wait             —           —             wait
56  agent     agent_wait                        —           —             —
57  customer  customer_request_wait             —           —             wait
58  agent     agent_wait                        —           —             —
59  customer  customer_acknowledge              —           —             —
60  agent     agent_request_income              —           —             income
61  customer  customer_report_done              —           —             हो गया
62  agent     agent_acknowledge                 —           —             —
63  customer  customer_request_wait             —           —             wait
64  agent     agent_acknowledge                 —           —             —
65  customer  customer_request_wait             —           —             wait
66  agent     agent_wait                        —           —             —
67  customer  customer_react_to_final_offer     —           —             —
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
5   agent     agent_greet                       —           —             —
6   customer  customer_other                    —           —             —
7   agent     agent_greet                       —           —             —
8   customer  customer_other                    —           —             —
9   agent     agent_greet                       —           —             —
10  customer  customer_agree                    —           —             —
11  agent     agent_ask_to_repeat               —           —             —
12  customer  customer_agree                    —           —             शुरू कर
13  agent     agent_send_sms_link               —           send_sms      sms
14  agent     agent_send_sms_link               —           —             —
15  customer  customer_acknowledge              —           —             —
16  agent     agent_send_sms_link               —           —             sms
17  customer  customer_report_sms_received      —           —             sms
18  customer  customer_report_sms_received      —           —             —
19  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
20  customer  customer_express_distrust         —           —             —
21  agent     agent_reassure_trust              —           —             —
22  customer  customer_report_link_opened       —           —             —
23  agent     agent_guide_apply                 —           —             apply now
24  customer  customer_do_otp                   —           —             —
25  agent     agent_request_otp                 —           send_otp      otp
26  customer  customer_request_wait             —           —             रुकिए
27  agent     agent_wait                        —           —             —
28  customer  customer_express_distrust         —           —             —
29  agent     agent_reassure_trust              —           —             —
30  customer  customer_express_distrust         —           —             —
31  agent     agent_reassure_trust              —           —             —
32  customer  customer_express_distrust         —           —             —
33  agent     agent_reassure_trust              —           —             —
34  customer  customer_do_otp                   —           —             otp
35  agent     agent_request_otp                 —           —             otp
36  customer  customer_do_otp                   —           —             otp
37  agent     agent_ask_employment_type         —           —             salaried, self-employ
38  customer  customer_state_employment_type    —           —             self employ
39  agent     agent_request_business_details    —           —             business
40  customer  customer_ask_question             —           —             —
41  agent     agent_answer_query                —           —             —
42  customer  customer_ask_question             —           —             —
43  agent     agent_wait                        —           —             —
44  customer  customer_agree                    —           —             —
45  agent     agent_wait                        —           —             —
46  customer  customer_acknowledge              —           —             —
47  agent     agent_clarify                     —           —             —
48  customer  customer_state_employment_type    —           —             —
49  customer  customer_provide_income           —           —             income
50  agent     agent_request_business_details    —           —             business
51  agent     agent_ask_to_repeat               —           —             —
52  customer  customer_report_done              —           —             भर दिया
53  customer  customer_respond_udyam            —           —             उद्यम
54  agent     agent_request_udyam               —           —             उद्यम
55  customer  customer_respond_udyam            —           —             —
56  agent     agent_offer_skip_udyam            —           —             skip
57  customer  customer_respond_udyam            —           —             —
58  agent     agent_wait                        —           —             —
59  customer  customer_other                    —           —             —
60  agent     agent_acknowledge                 —           —             —
61  customer  customer_respond_udyam            —           —             —
62  agent     agent_request_udyam               —           —             उद्यम
63  customer  customer_respond_udyam            —           —             —
64  agent     agent_request_otp                 —           —             otp
65  agent     agent_ask_to_repeat               —           —             —
66  customer  customer_request_wait             —           —             wait
67  agent     agent_wait                        —           —             —
68  customer  customer_other                    —           —             —
69  agent     agent_answer_query                —           —             —
70  customer  customer_report_done              —           —             —
71  agent     agent_request_otp                 —           —             otp
72  customer  customer_do_otp                   —           —             —
73  agent     agent_request_otp                 —           —             —
74  customer  customer_acknowledge              —           —             —
75  agent     agent_wait                        —           —             —
76  customer  customer_react_to_final_offer     —           —             —
77  agent     agent_acknowledge                 —           —             —
78  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 24d836c4 (transferred) — 53 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_express_distrust         distrustful —             fraud
7   agent     agent_reassure_trust              —           —             —
8   agent     agent_guide_apply                 —           —             apply now
9   agent     agent_request_otp                 —           send_otp      otp
10  agent     agent_ask_to_repeat               —           —             फिर से कह
11  agent     agent_ask_to_repeat               —           —             एक बार फिर
12  agent     agent_ask_to_repeat               —           —             एक बार फिर
13  customer  customer_provide_personal_details —           —             —
14  agent     agent_request_personal_details    —           —             gender, date of birth, marital
15  customer  customer_ask_question             —           —             —
16  agent     agent_request_personal_details    —           —             —
17  customer  customer_request_wait             —           —             —
18  agent     agent_wait                        —           —             —
19  customer  customer_request_wait             —           —             रुकिए
20  agent     agent_wait                        —           —             —
21  customer  customer_agree                    —           —             —
22  agent     agent_request_email               —           —             email
23  customer  customer_ask_question             —           —             —
24  agent     agent_request_email               —           —             email
25  customer  customer_acknowledge              —           —             —
26  agent     agent_request_address             —           —             address, pincode, locality, building, house number
27  customer  customer_ask_question             —           —             —
28  agent     agent_request_address             —           —             address, pincode, locality, building, flat
29  customer  customer_report_address_error     —           —             —
30  agent     agent_request_address             —           —             building, house number, flat
31  customer  customer_provide_business_details —           —             —
32  agent     agent_request_address             —           —             flat
33  customer  customer_ask_question             —           —             —
34  agent     agent_request_address             —           —             address, pincode, locality, building, house number
35  customer  customer_do_otp                   —           —             otp
36  agent     agent_request_address             —           —             address, pincode, locality, building, house number
37  customer  customer_do_otp                   —           —             otp
38  agent     agent_wait                        —           —             wait
39  customer  customer_other                    —           —             —
40  agent     agent_wait                        —           —             —
41  customer  customer_do_otp                   —           —             —
42  agent     agent_request_otp                 —           —             otp
43  agent     agent_ask_to_repeat               —           —             —
44  customer  customer_do_otp                   —           —             otp
45  agent     agent_request_otp                 —           —             otp
46  customer  customer_request_wait             —           —             —
47  agent     agent_wait                        —           —             —
48  customer  customer_react_to_final_offer     —           —             —
49  agent     agent_present_final_offer         —           —             final offer
50  customer  customer_report_applied           —           —             —
51  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
52  customer  customer_greet                    —           —             hello
```

## Call 26822e92 (transferred) — 60 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   customer  customer_acknowledge              —           —             —
6   agent     agent_send_sms_link               —           —             sms
7   customer  customer_express_distrust         —           —             —
8   agent     agent_reassure_trust              —           —             —
9   customer  customer_acknowledge              —           —             —
10  agent     agent_guide_open_link             —           —             लिंक पर क्लिक
11  agent     agent_guide_open_link             —           —             —
12  customer  customer_request_wait             —           —             —
13  agent     agent_wait                        —           —             —
14  agent     agent_ask_to_repeat               —           —             फिर से कह
15  agent     agent_guide_open_link             —           —             खुल गया
16  agent     agent_guide_open_link             —           —             —
17  agent     agent_guide_apply                 —           —             apply now
18  customer  customer_report_done              —           —             कर दिया
19  agent     agent_request_otp                 —           —             —
20  customer  customer_report_done              —           —             —
21  agent     agent_request_otp                 —           —             —
22  customer  customer_report_done              —           —             —
23  agent     agent_request_otp                 —           send_otp      otp
24  customer  customer_report_done              —           —             कर दिया
25  agent     agent_request_otp                 —           —             otp
26  agent     agent_request_personal_details    —           —             —
27  customer  customer_greet                    —           —             hello
28  agent     agent_request_pan                 —           —             पैन
29  agent     agent_ask_to_repeat               —           —             —
30  agent     agent_request_personal_details    —           —             gender, date of birth, marital
31  agent     agent_request_email               —           —             email
32  customer  customer_acknowledge              —           —             —
33  agent     agent_request_email               —           —             email
34  agent     agent_request_address             —           —             address, locality, building, house number, flat
35  agent     agent_ask_to_repeat               —           —             फिर से कह
36  customer  customer_report_done              —           —             भर दिया
37  agent     agent_request_terms_accept        —           —             terms and condition, terms
38  customer  customer_acknowledge              —           —             —
39  agent     agent_request_terms_accept        —           —             terms and condition, terms
40  customer  customer_other                    —           —             —
41  agent     agent_other                       —           —             —
42  customer  customer_other                    —           —             —
43  agent     agent_other                       —           —             —
44  customer  customer_react_to_offer           —           —             —
45  agent     agent_guide_apply                 —           —             apply now
46  agent     agent_guide_apply                 —           —             apply now
47  customer  customer_provide_email            —           —             email
48  agent     agent_request_email               —           —             email
49  customer  customer_provide_personal_details —           —             gender
50  agent     agent_ask_employment_type         —           —             self-employ
51  customer  customer_report_address_error     —           —             —
52  agent     agent_request_address             —           —             —
53  customer  customer_report_address_error     —           —             —
54  agent     agent_ask_to_repeat               —           —             फिर से बता
55  customer  customer_provide_address          —           —             house number
56  agent     agent_request_address             —           —             address, house number, flat
57  customer  customer_react_to_final_offer     —           —             —
58  agent     agent_present_final_offer         —           —             —
59  customer  customer_other                    —           —             —
```

## Call 286e2a38 (transferred) — 32 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             —
6   customer  customer_agree                    —           —             —
7   customer  customer_ask_query                —           —             —
8   agent     agent_present_offer               —           —             pre approved
9   agent     agent_send_sms_link               —           send_sms      sms
10  agent     agent_send_sms_link               —           —             sms
11  customer  customer_other                    —           —             —
12  agent     agent_reassure_trust              —           —             —
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
14  customer  customer_report_link_opened       —           —             खुल गया
15  agent     agent_guide_apply                 —           —             apply now
16  customer  customer_report_applied           —           —             —
17  agent     agent_request_otp                 —           —             —
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_do_otp                   —           —             otp
20  agent     agent_request_otp                 —           —             otp
21  customer  customer_do_otp                   —           —             otp
22  agent     agent_request_otp                 —           —             —
23  customer  customer_other                    —           —             —
24  agent     agent_wait                        —           —             —
25  customer  customer_other                    —           —             —
26  agent     agent_wait                        —           —             —
27  customer  customer_report_done              —           —             —
28  agent     agent_present_final_offer         —           —             final offer
29  customer  customer_react_to_final_offer     —           —             —
30  agent     agent_present_final_offer         —           —             —
31  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 28eeeb54 (transferred) — 50 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_acknowledge                 —           —             —
6   customer  customer_acknowledge              —           —             —
7   customer  customer_ask_question             —           —             —
8   customer  customer_query_fee                —           —             —
9   agent     agent_send_sms_link               —           send_sms      लिंक भेज
10  customer  customer_acknowledge              —           —             —
11  customer  customer_query_fee                —           —             processing fee
12  customer  customer_query_fee                —           —             —
13  agent     agent_explain_fee                 —           —             processing fee
14  customer  customer_acknowledge              —           —             —
15  agent     agent_acknowledge                 —           —             —
16  customer  customer_query_fee                —           —             interest rate
17  customer  customer_query_fee                —           —             processing fee, interest rate
18  agent     agent_explain_fee                 —           —             processing fee, interest rate
19  agent     agent_send_sms_link               —           send_sms      sms
20  customer  customer_acknowledge              —           —             —
21  agent     agent_guide_open_link             —           —             —
22  customer  customer_greet                    —           —             hello
23  agent     agent_guide_open_link             —           —             वेबसाइट, लिंक पर क्लिक
24  agent     agent_ask_to_repeat               —           —             —
25  customer  customer_acknowledge              —           —             —
26  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई, लिंक पर क्लिक
27  customer  customer_report_link_opened       —           —             खुल गई
28  agent     agent_guide_apply                 —           —             —
29  customer  customer_report_applied           —           —             apply now
30  agent     agent_guide_apply                 —           —             apply now
31  customer  customer_do_otp                   —           —             —
32  agent     agent_acknowledge                 —           —             —
33  customer  customer_acknowledge              —           —             —
34  agent     agent_request_otp                 —           —             —
35  agent     agent_ask_to_repeat               —           —             —
36  customer  customer_acknowledge              —           —             —
37  customer  customer_report_sms_received      —           —             link भेज
38  agent     agent_send_sms_link               —           send_sms      sms
39  customer  customer_express_distrust         —           —             —
40  customer  customer_skip_udyam               frustrated  —             नहीं हो
41  agent     agent_reassure_trust              —           —             —
42  customer  customer_express_distrust         —           —             —
43  agent     agent_reassure_trust              —           —             —
44  customer  customer_do_otp                   —           —             otp
45  agent     agent_request_otp                 —           —             otp
46  customer  customer_react_to_final_offer     —           —             —
47  agent     agent_present_final_offer         —           —             —
48  customer  customer_react_to_final_offer     —           —             —
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 292a5872 (transferred) — 40 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
1   agent     agent_greet                       —           —             —
2   agent     agent_ask_to_repeat               —           —             फिर से कह
3   customer  customer_agree                    —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_send_sms_link               —           send_sms      sms
7   customer  customer_report_sms_received      —           —             —
8   agent     agent_guide_open_link             —           —             खुल गया
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_acknowledge              —           —             —
11  agent     agent_request_otp                 —           send_otp      otp
12  customer  customer_report_done              —           —             हो गया
13  agent     agent_ask_employment_type         —           —             salaried, self-employ
14  customer  customer_state_employment_type    —           —             self employ
15  agent     agent_request_income              —           —             income
16  customer  customer_other                    —           —             —
17  agent     agent_request_org_name            —           —             —
18  customer  customer_acknowledge              —           —             —
19  agent     agent_request_business_details    —           —             business
20  customer  customer_provide_personal_details —           —             date of birth
21  agent     agent_request_personal_details    —           —             —
22  customer  customer_provide_personal_details —           —             —
23  agent     agent_request_personal_details    —           —             marital
24  customer  customer_state_employment_type    —           —             self employ
25  agent     agent_request_income              —           —             income
26  customer  customer_report_done              —           —             —
27  agent     agent_request_business_details    —           —             business
28  customer  customer_respond_udyam            —           —             उद्यम
29  agent     agent_request_udyam               —           —             udyam
30  agent     agent_ask_to_repeat               —           —             —
31  customer  customer_acknowledge              —           —             —
32  agent     agent_request_udyam               —           —             udyam
33  agent     agent_ask_to_repeat               —           —             —
34  customer  customer_acknowledge              —           —             —
35  agent     agent_wait                        —           —             —
36  customer  customer_ask_question             —           —             —
37  agent     agent_present_final_offer         —           —             —
38  customer  customer_acknowledge              —           —             —
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 294cf852 (transferred) — 39 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_report_link_opened       —           —             —
7   customer  customer_greet                    —           —             hello
8   agent     agent_guide_apply                 —           —             apply now
9   customer  customer_report_applied           —           —             —
10  agent     agent_request_otp                 —           send_otp      otp
11  customer  customer_do_otp                   —           —             otp
12  agent     agent_request_otp                 —           send_otp      otp
13  customer  customer_do_otp                   —           —             —
14  agent     agent_request_pan                 —           —             पैन
15  customer  customer_provide_pan              —           —             pan
16  agent     agent_request_personal_details    —           —             gender, date of birth, marital
17  customer  customer_report_done              —           —             भर दिया
18  agent     agent_request_email               —           —             email
19  customer  customer_report_done              —           —             भर दिया
20  agent     agent_request_address             —           —             address, pincode, locality, building, house number
21  customer  customer_report_done              —           —             कर दिया
22  agent     agent_request_terms_accept        —           —             terms and condition, terms
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_ask_employment_type         —           —             salaried, self-employ
25  customer  customer_state_employment_type    —           —             salaried
26  agent     agent_request_income              —           —             income
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_org_name            —           —             organization
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_email               —           —             email
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_business_details    —           —             —
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_otp                 —           send_otp      otp
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_present_final_offer         —           —             final offer
37  customer  customer_react_to_final_offer     —           —             —
38  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 298f09f6 (transferred) — 124 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   customer  customer_greet                    —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
3   customer  customer_greet                    —           —             hello
4   agent     agent_greet                       —           —             —
5   customer  customer_express_distrust         —           —             —
6   customer  customer_query_fee                —           —             —
7   customer  customer_agree                    —           —             —
8   agent     agent_send_sms_link               —           send_sms      sms
9   agent     agent_guide_open_link             —           —             —
10  customer  customer_report_sms_received      —           —             sms
11  agent     agent_send_sms_link               —           —             sms
12  customer  customer_report_sms_received      —           —             —
13  agent     agent_guide_apply                 —           —             apply now
14  agent     agent_ask_to_repeat               —           —             फिर से कह
15  customer  customer_report_applied           —           —             apply now
16  agent     agent_guide_apply                 —           —             apply now
17  customer  customer_report_done              —           —             कर दिया
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_ask_question             —           —             —
20  agent     agent_request_otp                 —           —             —
21  customer  customer_report_done              —           —             कर दिया
22  agent     agent_request_otp                 —           send_otp      otp
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_request_pan                 —           —             पैन
25  customer  customer_provide_pan              —           —             —
26  agent     agent_request_pan                 —           —             पैन
27  customer  customer_react_to_final_offer     —           —             —
28  agent     agent_request_pan                 —           —             पैन
29  agent     agent_ask_to_repeat               —           —             फिर से कह, एक बार फिर
30  customer  customer_ask_question             —           —             —
31  agent     agent_request_personal_details    —           —             gender, date of birth, marital
32  customer  customer_acknowledge              —           —             —
33  agent     agent_request_personal_details    —           —             gender, date of birth, marital
34  agent     agent_ask_to_repeat               —           —             साफ़ बोल
35  customer  customer_request_wait             —           —             —
36  customer  customer_greet                    —           —             hello
37  agent     agent_wait                        —           —             —
38  customer  customer_greet                    —           —             hello
39  agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
40  agent     agent_greet                       —           —             नमस्ते
41  agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
42  customer  customer_provide_personal_details —           —             date of birth
43  agent     agent_request_email               —           —             email
44  customer  customer_report_done              —           —             —
45  agent     agent_request_address             —           —             address, pincode, locality, building, house number
46  customer  customer_acknowledge              —           —             —
47  agent     agent_request_address             —           —             address, pincode, locality, building, house number
48  customer  customer_report_done              —           —             हो गया
49  agent     agent_request_terms_accept        —           —             terms and condition, terms
50  customer  customer_report_address_error     —           —             —
51  agent     agent_other                       —           —             —
52  customer  customer_report_address_error     —           —             —
53  agent     agent_help_address_error          —           —             —
54  customer  customer_ask_question             —           —             —
55  agent     agent_request_address             —           —             address, building
56  customer  customer_ask_question             —           —             —
57  agent     agent_request_address             —           —             address
58  customer  customer_acknowledge              —           —             —
59  agent     agent_request_address             —           —             address
60  customer  customer_report_done              —           —             कर दिया
61  agent     agent_request_otp                 —           send_otp      otp
62  customer  customer_ask_question             —           —             —
63  agent     agent_request_otp                 —           send_otp      otp
64  customer  customer_ask_question             —           —             —
65  agent     agent_request_otp                 —           —             otp
66  customer  customer_provide_email            —           —             email
67  agent     agent_request_otp                 —           —             otp
68  customer  customer_acknowledge              —           —             —
69  agent     agent_request_otp                 —           —             otp
70  agent     agent_request_otp                 —           —             otp
71  customer  customer_do_otp                   —           —             —
72  agent     agent_wait                        —           —             wait
73  customer  customer_provide_income           —           —             income
74  agent     agent_request_income              —           —             income
75  customer  customer_acknowledge              —           —             —
76  agent     agent_request_income              —           —             income
77  customer  customer_other                    frustrated  —             नहीं हो रहा, नहीं हो
78  agent     agent_ask_to_repeat               —           —             —
79  customer  customer_express_distrust         distrustful —             fraud
80  agent     agent_reassure_trust              —           —             —
81  customer  customer_provide_personal_details —           —             —
82  agent     agent_request_personal_details    —           —             —
83  customer  customer_provide_org_name         frustrated  —             नहीं हो रहा, नहीं हो
84  agent     agent_request_org_name            —           —             —
85  customer  customer_ask_question             —           —             —
86  agent     agent_request_org_name            —           —             organization
87  customer  customer_acknowledge              —           —             —
88  agent     agent_request_org_name            —           —             organization
89  customer  customer_provide_org_name         —           —             —
90  agent     agent_request_org_name            —           —             organization
91  customer  customer_provide_org_name         —           —             —
92  agent     agent_request_org_name            —           —             organization
93  customer  customer_ask_question             —           —             —
94  customer  customer_provide_email            —           —             email
95  agent     agent_request_email               —           —             email
96  customer  customer_provide_email            —           —             email
97  agent     agent_request_email               —           —             email
98  customer  customer_report_done              —           —             —
99  agent     agent_request_business_details    —           —             —
100 customer  customer_report_done              —           —             हो गया
101 agent     agent_request_terms_accept        —           —             —
102 customer  customer_request_wait             —           —             wait
103 agent     agent_wait                        —           —             —
104 customer  customer_react_to_final_offer     —           —             —
105 agent     agent_present_final_offer         —           —             —
106 customer  customer_query_fee                —           —             —
107 agent     agent_explain_fee                 —           —             interest rate
108 customer  customer_query_fee                —           —             —
109 agent     agent_explain_fee                 —           —             interest rate
110 customer  customer_query_fee                —           —             processing fee
111 agent     agent_explain_fee                 —           —             processing fee
112 customer  customer_other                    —           —             —
113 agent     agent_end_call                    —           —             —
114 customer  customer_query_fee                —           —             charges
115 agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
116 customer  customer_agree                    skeptical   —             doubt
117 agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
118 customer  customer_agree                    —           —             —
119 agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
120 customer  customer_acknowledge              —           —             —
121 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
122 agent     agent_end_call                    —           —             goodbye, duration has been exceeded
123 customer  customer_other                    —           —             —
```

## Call 2af0490b (transferred) — 35 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_query_fee                confused    —             interest rate, कैसे
4   agent     agent_explain_fee                 —           —             interest rate
5   customer  customer_query_fee                —           —             —
6   agent     agent_explain_fee                 —           —             interest rate
7   customer  customer_query_fee                —           —             —
8   agent     agent_explain_fee                 —           —             interest rate
9   customer  customer_other                    —           —             —
10  customer  customer_query_fee                —           —             —
11  agent     agent_explain_fee                 —           —             interest rate
12  customer  customer_agree                    —           —             —
13  agent     agent_send_sms_link               —           send_sms      sms
14  agent     agent_ask_to_repeat               —           —             फिर से कह
15  customer  customer_provide_email            —           —             email
16  agent     agent_request_email               —           —             email
17  customer  customer_report_link_opened       —           —             —
18  customer  customer_report_link_opened       —           —             —
19  agent     agent_guide_open_link             —           —             —
20  customer  customer_report_applied           —           —             —
21  agent     agent_guide_apply                 —           —             apply now
22  customer  customer_do_otp                   —           —             —
23  agent     agent_request_otp                 —           send_otp      otp
24  customer  customer_provide_email            —           —             email
25  agent     agent_request_email               —           —             email
26  customer  customer_do_otp                   —           —             otp
27  agent     agent_request_otp                 —           send_otp      otp
28  customer  customer_do_otp                   —           —             —
29  agent     agent_request_otp                 —           send_otp      otp
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_present_final_offer         —           —             final offer
32  customer  customer_query_fee                frustrated  —             interest rate, नहीं हो रहा, नहीं हो
33  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
34  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 30f7f2d2 (transferred) — 47 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   customer  customer_ask_question             —           —             —
6   agent     agent_present_offer               —           —             pre-approved
7   customer  customer_ask_question             —           —             —
8   agent     agent_explain_fee                 —           —             interest rate
9   customer  customer_agree                    —           —             —
10  agent     agent_send_sms_link               —           send_sms      sms
11  customer  customer_ask_question             —           —             —
12  agent     agent_guide_open_link             —           —             —
13  customer  customer_ask_question             —           —             —
14  agent     agent_guide_open_link             —           —             —
15  customer  customer_ask_question             —           —             —
16  agent     agent_guide_apply                 —           —             apply now
17  customer  customer_report_done              —           —             —
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_ask_question             —           —             —
20  agent     agent_request_otp                 —           send_otp      otp
21  customer  customer_provide_personal_details —           —             —
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital
23  customer  customer_ask_question             —           —             —
24  agent     agent_request_email               —           —             email
25  customer  customer_ask_question             —           —             —
26  agent     agent_request_address             —           —             address, pincode, locality, building, house number
27  customer  customer_ask_question             —           —             —
28  agent     agent_request_terms_accept        —           —             terms and condition, terms
29  agent     agent_ask_employment_type         —           —             salaried, self-employ
30  customer  customer_state_employment_type    —           —             salaried
31  agent     agent_request_income              —           —             income
32  customer  customer_acknowledge              —           —             —
33  agent     agent_request_org_name            —           —             organization
34  agent     agent_request_email               —           —             email
35  agent     agent_request_business_details    —           —             —
36  customer  customer_acknowledge              —           —             —
37  agent     agent_guide_apply                 —           —             —
38  agent     agent_request_otp                 —           send_otp      otp
39  agent     agent_ask_to_repeat               —           —             फिर से कह
40  customer  customer_report_done              —           —             —
41  agent     agent_request_otp                 —           —             otp
42  agent     agent_present_final_offer         —           —             —
43  customer  customer_do_otp                   —           —             otp
44  agent     agent_present_final_offer         —           —             final offer
45  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
46  agent     agent_transfer_to_rm              —           transfer_to_rm140000
```

## Call 3263832d (transferred) — 89 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
1   customer  customer_agree                    —           —             —
2   agent     agent_send_sms_link               —           send_sms      sms
3   agent     agent_guide_open_link             —           —             —
4   customer  customer_ask_question             —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_ask_to_repeat               —           —             फिर से कह
7   customer  customer_report_link_opened       —           —             —
8   agent     agent_guide_apply                 —           —             apply now
9   customer  customer_report_link_opened       —           —             —
10  agent     agent_guide_open_link             —           —             —
11  customer  customer_other                    —           —             —
12  agent     agent_guide_open_link             —           —             —
13  customer  customer_request_wait             —           —             —
14  agent     agent_wait                        —           —             —
15  customer  customer_request_wait             —           —             —
16  agent     agent_wait                        —           —             —
17  customer  customer_report_link_opened       —           —             —
18  agent     agent_send_sms_link               —           send_sms      sms
19  customer  customer_report_link_opened       —           —             —
20  agent     agent_answer_query                —           —             —
21  customer  customer_ask_question             —           —             —
22  agent     agent_answer_query                —           —             —
23  customer  customer_ask_question             —           —             —
24  agent     agent_answer_query                —           —             —
25  agent     agent_ask_to_repeat               —           —             फिर से बता
26  customer  customer_request_wait             —           —             —
27  customer  customer_other                    —           —             —
28  agent     agent_wait                        —           —             —
29  customer  customer_greet                    —           —             hello
30  agent     agent_confirm                     —           —             आगे बढ़
31  customer  customer_report_link_opened       —           —             —
32  agent     agent_present_offer               —           —             pre-approved, loan offer
33  agent     agent_ask_to_repeat               —           —             फिर से कह
34  customer  customer_acknowledge              —           —             —
35  agent     agent_acknowledge                 —           —             —
36  customer  customer_report_done              —           —             —
37  agent     agent_guide_open_link             —           —             —
38  customer  customer_do_otp                   —           —             —
39  agent     agent_request_otp                 —           send_otp      otp
40  customer  customer_ask_question             —           —             —
41  agent     agent_request_otp                 —           send_otp      otp
42  customer  customer_request_wait             —           —             wait
43  agent     agent_wait                        —           —             —
44  customer  customer_report_done              —           —             —
45  agent     agent_wait                        —           —             —
46  customer  customer_agree                    —           —             —
47  agent     agent_wait                        —           —             —
48  customer  customer_ask_question             —           —             —
49  agent     agent_greet                       —           —             —
50  customer  customer_provide_org_name         —           —             —
51  agent     agent_request_org_name            —           —             organization
52  customer  customer_request_wait             —           —             —
53  agent     agent_wait                        —           —             —
54  customer  customer_provide_org_name         —           —             —
55  agent     agent_request_org_name            —           —             —
56  customer  customer_acknowledge              —           —             —
57  agent     agent_request_email               —           —             email
58  agent     agent_ask_to_repeat               —           —             फिर से कह
59  customer  customer_other                    —           —             —
60  agent     agent_request_email               —           —             email
61  customer  customer_ask_question             —           —             मतलब
62  agent     agent_answer_query                —           —             —
63  agent     agent_request_org_name            —           —             organization
64  customer  customer_request_wait             —           —             —
65  agent     agent_wait                        —           —             —
66  customer  customer_ask_question             —           —             —
67  agent     agent_answer_query                —           —             —
68  customer  customer_report_done              —           —             —
69  agent     agent_wait                        —           —             —
70  customer  customer_react_to_final_offer     —           —             —
71  agent     agent_present_final_offer         —           —             final offer
72  customer  customer_react_to_final_offer     —           —             —
73  agent     agent_present_final_offer         —           —             final offer
74  customer  customer_react_to_final_offer     —           —             —
75  agent     agent_present_final_offer         —           —             —
76  customer  customer_query_fee                —           —             —
77  agent     agent_explain_fee                 —           —             interest rate
78  customer  customer_react_to_final_offer     —           —             —
79  agent     agent_explain_fee                 —           —             interest rate
80  customer  customer_react_to_final_offer     —           —             —
81  agent     agent_explain_fee                 —           —             interest rate
82  customer  customer_react_to_final_offer     —           —             —
83  agent     agent_present_final_offer         —           —             —
84  customer  customer_react_to_final_offer     —           —             —
85  agent     agent_present_final_offer         —           —             final offer
86  customer  customer_react_to_final_offer     —           —             —
87  agent     agent_present_final_offer         —           —             final offer
88  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 354b7cd9 (transferred) — 60 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_acknowledge              —           —             —
3   agent     agent_greet                       —           —             —
4   customer  customer_greet                    —           —             —
5   agent     agent_present_offer               —           —             pre-approved, loan offer
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_guide_open_link             —           —             —
8   agent     agent_ask_to_repeat               —           —             —
9   customer  customer_request_wait             —           —             —
10  agent     agent_wait                        —           —             —
11  customer  customer_report_link_opened       —           —             —
12  agent     agent_guide_apply                 —           —             apply now
13  agent     agent_request_otp                 —           send_otp      otp
14  agent     agent_ask_to_repeat               —           —             —
15  customer  customer_request_wait             —           —             —
16  agent     agent_wait                        —           —             —
17  agent     agent_request_otp                 —           —             otp
18  customer  customer_report_done              —           —             —
19  agent     agent_request_pan                 —           —             pan
20  customer  customer_report_done              —           —             —
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital
22  agent     agent_ask_to_repeat               —           —             —
23  customer  customer_provide_address          —           —             address
24  agent     agent_request_email               —           —             email
25  agent     agent_ask_to_repeat               —           —             —
26  customer  customer_report_done              —           —             —
27  agent     agent_request_address             —           —             address, pincode, locality, building, house number
28  agent     agent_request_terms_accept        —           —             terms and condition, terms
29  customer  customer_acknowledge              —           —             —
30  agent     agent_ask_employment_type         —           —             salaried, self-employ
31  agent     agent_ask_employment_type         —           —             salaried, self-employ
32  agent     agent_ask_to_repeat               —           —             —
33  customer  customer_report_done              —           —             —
34  agent     agent_request_income              —           —             —
35  agent     agent_ask_to_repeat               —           —             —
36  customer  customer_request_wait             —           —             —
37  agent     agent_request_income              —           —             —
38  customer  customer_express_distrust         —           —             —
39  agent     agent_reassure_trust              —           —             —
40  agent     agent_ask_to_repeat               —           —             —
41  customer  customer_request_wait             —           —             wait
42  agent     agent_wait                        —           —             —
43  agent     agent_ask_to_repeat               —           —             —
44  customer  customer_do_otp                   —           —             —
45  agent     agent_request_org_name            —           —             organization
46  agent     agent_ask_to_repeat               —           —             —
47  agent     agent_request_email               —           —             email
48  customer  customer_report_done              —           —             —
49  agent     agent_request_address             —           —             address, pincode
50  agent     agent_request_address             —           —             address, pincode
51  customer  customer_report_done              —           —             —
52  agent     agent_request_terms_accept        —           —             —
53  agent     agent_ask_to_repeat               —           —             —
54  agent     agent_confirm_step                —           —             —
55  agent     agent_request_otp                 —           —             otp
56  agent     agent_request_otp                 —           —             otp
57  customer  customer_report_done              —           —             —
58  agent     agent_present_final_offer         —           —             final offer, loan amount and
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 3b10addb (transferred) — 37 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_ask_question             —           —             —
5   agent     agent_present_offer               —           —             pre-approved
6   customer  customer_query_fee                —           —             —
7   agent     agent_present_offer               —           —             pre-approved
8   customer  customer_ask_question             —           —             —
9   agent     agent_present_offer               —           —             pre-approved
10  customer  customer_query_fee                —           —             —
11  agent     agent_explain_fee                 —           —             interest rate
12  customer  customer_greet                    —           —             hello
13  agent     agent_guide_open_link             —           —             —
14  agent     agent_ask_to_repeat               —           —             फिर से कह
15  customer  customer_agree                    —           —             शुरू कर
16  agent     agent_send_sms_link               —           send_sms      sms
17  agent     agent_send_sms_link               —           send_sms      sms
18  agent     agent_guide_open_link             —           —             —
19  agent     agent_ask_to_repeat               —           —             फिर से कह
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_guide_apply                 —           —             apply now
22  customer  customer_report_applied           —           —             —
23  agent     agent_guide_apply                 —           —             apply now
24  customer  customer_report_done              —           —             कर दिया
25  agent     agent_request_otp                 —           send_otp      otp
26  agent     agent_ask_to_repeat               —           —             —
27  customer  customer_other                    —           —             —
28  agent     agent_request_otp                 —           send_otp      otp
29  customer  customer_report_done              —           —             कर दिया
30  agent     agent_request_otp                 —           send_otp      otp
31  customer  customer_react_to_final_offer     —           —             —
32  agent     agent_request_otp                 —           —             otp
33  customer  customer_report_done              —           —             कर दिया
34  agent     agent_present_final_offer         —           —             final offer
35  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
36  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 3bda83f6 (transferred) — 44 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   customer  customer_greet                    —           —             hello
4   agent     agent_send_sms_link               —           send_sms      sms
5   customer  customer_acknowledge              —           —             —
6   agent     agent_guide_open_link             —           —             —
7   customer  customer_acknowledge              —           —             —
8   agent     agent_guide_apply                 —           —             —
9   customer  customer_report_done              —           —             कर दिया
10  agent     agent_guide_apply                 —           —             apply now
11  customer  customer_report_done              —           —             कर दिया
12  agent     agent_request_otp                 —           send_otp      otp
13  customer  customer_report_done              —           —             कर दिया
14  agent     agent_request_otp                 —           send_otp      otp
15  customer  customer_do_otp                   —           —             —
16  agent     agent_request_pan                 —           —             पैन
17  customer  customer_report_done              —           —             कर दिया
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital
19  customer  customer_report_done              —           —             हो गया
20  agent     agent_request_email               —           —             email
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_address             —           —             address, pincode, locality, building, house number
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_terms_accept        —           —             terms and condition, terms
25  customer  customer_accept_terms             —           —             —
26  agent     agent_ask_employment_type         —           —             salaried, self-employ
27  customer  customer_state_employment_type    —           —             salaried
28  agent     agent_request_income              —           —             income
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_org_name            —           —             organization
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_email               —           —             email
33  customer  customer_acknowledge              —           —             —
34  agent     agent_acknowledge                 —           —             —
35  customer  customer_report_done              —           —             कर दिया
36  agent     agent_request_business_details    —           —             —
37  customer  customer_report_done              —           —             कर दिया
38  agent     agent_guide_apply                 —           —             —
39  customer  customer_report_done              —           —             कर दिया
40  agent     agent_request_otp                 —           send_otp      otp
41  customer  customer_do_otp                   —           —             —
42  agent     agent_present_final_offer         —           —             final offer
43  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 3f381582 (transferred) — 53 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   customer  customer_query_fee                —           —             —
4   agent     agent_explain_fee                 —           —             interest rate
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_guide_open_link             —           —             —
7   agent     agent_guide_apply                 —           —             apply now
8   agent     agent_ask_to_repeat               —           —             —
9   customer  customer_do_otp                   —           —             —
10  agent     agent_request_otp                 —           —             —
11  customer  customer_do_otp                   —           —             —
12  agent     agent_request_otp                 —           send_otp      otp
13  agent     agent_request_otp                 —           send_otp      otp
14  customer  customer_provide_pan              —           —             pan
15  agent     agent_request_pan                 —           —             पैन
16  agent     agent_request_pan                 —           —             पैन
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital
18  agent     agent_request_email               —           —             email
19  agent     agent_request_address             —           —             address, pincode, locality, building, house number
20  agent     agent_request_terms_accept        —           —             terms and condition, terms
21  customer  customer_request_wait             —           —             wait
22  agent     agent_wait                        —           —             —
23  agent     agent_ask_employment_type         —           —             salaried, self-employ
24  agent     agent_ask_employment_type         —           —             salaried, self-employ
25  agent     agent_request_income              —           —             —
26  customer  customer_state_employment_type    —           —             self employ
27  agent     agent_request_income              —           —             income
28  agent     agent_request_income              —           —             income
29  customer  customer_report_done              —           —             —
30  agent     agent_request_business_details    —           —             business
31  agent     agent_request_business_details    —           —             business
32  customer  customer_report_done              —           —             —
33  agent     agent_request_udyam               —           —             udyam
34  customer  customer_acknowledge              —           —             —
35  agent     agent_request_otp                 —           send_otp      otp
36  customer  customer_skip_udyam               —           —             skip
37  agent     agent_offer_skip_udyam            —           —             skip
38  customer  customer_skip_udyam               —           —             skip
39  agent     agent_wait                        —           —             —
40  customer  customer_react_to_final_offer     —           —             loan amount and
41  agent     agent_present_final_offer         —           —             final offer, loan amount and, cannot be changed
42  agent     agent_ask_to_repeat               —           —             फिर से कह
43  customer  customer_request_wait             —           —             —
44  agent     agent_wait                        —           —             —
45  customer  customer_other                    —           —             —
46  agent     agent_answer_query                —           —             —
47  customer  customer_ask_question             —           —             —
48  agent     agent_answer_query                —           —             —
49  customer  customer_ask_query                —           —             —
50  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
51  customer  customer_agree                    —           —             —
52  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 42e13796 (transferred) — 78 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_ask_question             —           —             —
7   agent     agent_greet                       —           —             —
8   customer  customer_agree                    —           —             —
9   agent     agent_guide_open_link             —           —             —
10  customer  customer_report_link_opened       —           —             —
11  agent     agent_guide_apply                 —           —             apply now
12  customer  customer_report_done              —           —             कर दिया
13  agent     agent_request_otp                 —           —             —
14  customer  customer_do_otp                   —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_do_otp                   —           —             otp
17  agent     agent_request_otp                 —           send_otp      otp
18  agent     agent_ask_to_repeat               —           —             फिर से कह
19  customer  customer_report_done              —           —             कर दिया
20  customer  customer_react_to_offer           —           —             —
21  agent     agent_request_pan                 —           —             पैन
22  customer  customer_query_fee                —           —             —
23  agent     agent_answer_query                —           —             —
24  agent     agent_request_pan                 —           —             पैन
25  agent     agent_request_pan                 —           —             पैन
26  customer  customer_report_done              —           —             कर दिया
27  agent     agent_request_personal_details    —           —             gender, date of birth, marital
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_email               —           —             email
30  agent     agent_ask_to_repeat               —           —             —
31  customer  customer_provide_email            —           —             email
32  agent     agent_request_address             —           —             address, pincode, locality, building, house number
33  customer  customer_provide_address          —           —             building
34  agent     agent_answer_query                —           —             —
35  customer  customer_acknowledge              —           —             —
36  agent     agent_request_address             —           —             address, pincode, locality, building, house number
37  agent     agent_request_terms_accept        —           —             terms and condition, terms
38  customer  customer_acknowledge              —           —             —
39  agent     agent_request_terms_accept        —           —             terms and condition, terms
40  customer  customer_provide_address          —           —             —
41  agent     agent_answer_query                —           —             —
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_ask_employment_type         —           —             salaried, self-employ
44  agent     agent_ask_to_repeat               —           —             —
45  customer  customer_provide_business_details —           —             business
46  agent     agent_request_business_details    —           —             business
47  agent     agent_ask_to_repeat               —           —             —
48  customer  customer_provide_business_details —           —             business
49  agent     agent_request_business_details    —           —             business
50  customer  customer_provide_business_details —           —             business
51  agent     agent_request_address             —           —             address
52  customer  customer_provide_business_details —           —             business
53  agent     agent_request_address             —           —             —
54  customer  customer_acknowledge              —           —             —
55  agent     agent_guide_apply                 —           —             —
56  customer  customer_acknowledge              —           —             —
57  agent     agent_guide_apply                 —           —             —
58  agent     agent_ask_to_repeat               —           —             —
59  customer  customer_skip_udyam               —           —             skip
60  customer  customer_skip_udyam               —           —             skip
61  agent     agent_offer_skip_udyam            —           —             skip
62  customer  customer_acknowledge              —           —             —
63  agent     agent_offer_skip_udyam            —           —             skip
64  customer  customer_ask_question             —           —             —
65  agent     agent_inform_manual_review        —           push_to_crm   manual review
66  customer  customer_agree                    —           —             —
67  agent     agent_request_otp                 —           send_otp      otp
68  customer  customer_other                    —           —             —
69  agent     agent_end_call                    —           —             —
70  agent     agent_present_final_offer         —           —             —
71  customer  customer_acknowledge              —           —             —
72  agent     agent_present_final_offer         —           —             final offer
73  agent     agent_ask_to_repeat               —           —             —
74  agent     agent_present_final_offer         —           —             final offer
75  customer  customer_react_to_final_offer     —           —             —
76  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
77  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 465ce42d (transferred) — 58 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   customer  customer_greet                    —           —             hello
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_report_sms_received      —           —             —
9   agent     agent_wait                        —           —             —
10  agent     agent_guide_open_link             —           —             —
11  customer  customer_report_link_opened       —           —             —
12  agent     agent_guide_apply                 —           —             apply now
13  customer  customer_report_applied           —           —             —
14  agent     agent_request_otp                 —           send_otp      otp
15  customer  customer_query_fee                —           —             —
16  agent     agent_answer_query                —           —             —
17  customer  customer_agree                    —           —             —
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_react_to_offer           —           —             —
20  agent     agent_request_pan                 —           —             पैन
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital
22  agent     agent_request_email               —           —             email
23  customer  customer_acknowledge              —           —             —
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  customer  customer_acknowledge              —           —             —
26  agent     agent_request_terms_accept        —           —             terms and condition, terms
27  customer  customer_provide_address          —           —             address
28  agent     agent_ask_employment_type         —           —             salaried, self-employ
29  customer  customer_request_wait             —           —             —
30  agent     agent_wait                        —           —             —
31  customer  customer_acknowledge              —           —             —
32  agent     agent_ask_employment_type         —           —             salaried, self-employ
33  customer  customer_other                    frustrated  —             नहीं हो रहा, नहीं हो
34  agent     agent_request_income              —           —             income
35  customer  customer_other                    —           —             —
36  agent     agent_request_org_name            —           —             organization
37  customer  customer_other                    frustrated  —             नहीं हो रहा, नहीं हो
38  agent     agent_answer_query                —           —             —
39  customer  customer_acknowledge              —           —             —
40  agent     agent_answer_query                —           —             —
41  customer  customer_acknowledge              —           —             —
42  agent     agent_answer_query                —           —             —
43  customer  customer_report_link_opened       —           —             —
44  agent     agent_request_address             —           —             address, pincode
45  agent     agent_ask_to_repeat               —           —             —
46  customer  customer_report_done              —           —             —
47  agent     agent_request_terms_accept        —           —             terms and condition, terms
48  customer  customer_acknowledge              —           —             —
49  agent     agent_request_otp                 —           send_otp      otp
50  customer  customer_acknowledge              —           —             —
51  agent     agent_request_otp                 —           —             otp
52  customer  customer_acknowledge              —           —             —
53  agent     agent_request_otp                 —           —             otp
54  customer  customer_acknowledge              —           —             —
55  agent     agent_present_final_offer         —           —             final offer
56  customer  customer_react_to_final_offer     —           —             —
57  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 4ee4e8eb (transferred) — 86 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_present_offer               —           —             —
4   customer  customer_greet                    —           —             hello
5   customer  customer_greet                    —           —             hello
6   agent     agent_present_offer               —           —             —
7   customer  customer_agree                    —           —             —
8   customer  customer_agree                    confused    —             कैसे
9   agent     agent_send_sms_link               —           send_sms      sms
10  agent     agent_guide_open_link             —           —             —
11  customer  customer_query_fee                —           —             —
12  agent     agent_explain_fee                 —           —             interest rate
13  customer  customer_request_wait             —           —             —
14  agent     agent_wait                        —           —             —
15  agent     agent_guide_apply                 —           —             —
16  customer  customer_report_done              —           —             —
17  agent     agent_guide_apply                 —           —             apply now
18  customer  customer_agree                    —           —             —
19  agent     agent_request_otp                 —           send_otp      otp
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_otp                 —           send_otp      otp
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_pan                 —           —             पैन
24  customer  customer_request_wait             frustrated  —             नहीं हो रहा, नहीं हो
25  agent     agent_wait                        —           —             wait
26  customer  customer_do_otp                   —           —             otp
27  agent     agent_request_personal_details    —           —             gender, date of birth, marital
28  agent     agent_request_personal_details    —           —             gender, date of birth, marital
29  customer  customer_state_employment_type    —           —             —
30  agent     agent_ask_employment_type         —           —             salaried, self-employ
31  customer  customer_ask_question             —           —             —
32  agent     agent_answer_query                —           —             —
33  customer  customer_acknowledge              —           —             —
34  agent     agent_ask_employment_type         —           —             salaried, self-employ
35  customer  customer_state_employment_type    —           —             self employ, self employee
36  agent     agent_request_income              —           —             income
37  customer  customer_request_wait             —           —             —
38  agent     agent_wait                        —           —             —
39  customer  customer_provide_email            —           —             email
40  agent     agent_request_email               —           —             email
41  agent     agent_ask_to_repeat               —           —             —
42  customer  customer_provide_address          —           —             building, flat
43  agent     agent_request_address             —           —             address, pincode, locality, building, house number
44  customer  customer_acknowledge              —           —             —
45  agent     agent_request_terms_accept        —           —             terms and condition, terms
46  agent     agent_request_terms_accept        —           —             terms and condition, terms
47  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो
48  customer  customer_report_address_error     —           —             —
49  agent     agent_help_address_error          —           —             —
50  customer  customer_acknowledge              —           —             —
51  agent     agent_help_address_error          —           —             —
52  customer  customer_report_done              —           —             हो गया
53  agent     agent_request_terms_accept        —           —             —
54  customer  customer_ask_question             —           —             —
55  agent     agent_request_org_name            —           —             organization
56  agent     agent_request_org_name            —           —             organization
57  customer  customer_ask_question             —           —             —
58  agent     agent_request_org_name            —           —             organization
59  customer  customer_ask_question             —           —             —
60  agent     agent_request_income              —           —             income
61  customer  customer_ask_question             —           —             —
62  agent     agent_answer_query                —           —             —
63  customer  customer_ask_question             frustrated  —             नहीं हो
64  agent     agent_answer_query                —           —             —
65  customer  customer_report_done              —           —             हो गया
66  agent     agent_request_email               —           —             email
67  customer  customer_respond_udyam            —           —             उद्यम
68  agent     agent_request_udyam               —           —             udyam
69  customer  customer_skip_udyam               —           —             —
70  agent     agent_request_udyam               —           —             udyam
71  customer  customer_skip_udyam               —           —             —
72  agent     agent_offer_skip_udyam            —           —             skip
73  customer  customer_report_done              —           —             —
74  agent     agent_request_otp                 —           —             otp
75  customer  customer_request_wait             —           —             wait
76  agent     agent_wait                        —           —             —
77  customer  customer_react_to_final_offer     —           —             —
78  agent     agent_present_final_offer         —           —             final offer
79  customer  customer_react_to_final_offer     —           —             —
80  agent     agent_present_final_offer         —           —             —
81  customer  customer_react_to_final_offer     —           —             —
82  agent     agent_present_final_offer         —           —             final offer
83  customer  customer_report_done              —           —             —
84  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
85  customer  customer_request_wait             —           —             —
```

## Call 52b52766 (transferred) — 57 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_query_fee                —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_report_sms_received      —           —             —
7   agent     agent_wait                        —           —             wait
8   customer  customer_report_sms_received      —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_express_distrust         —           —             —
11  agent     agent_reassure_trust              —           —             —
12  customer  customer_express_distrust         distrustful —             fraud
13  agent     agent_reassure_trust              —           —             —
14  customer  customer_react_to_offer           —           —             —
15  agent     agent_present_offer               —           —             loan offer
16  customer  customer_agree                    —           —             —
17  agent     agent_request_otp                 —           send_otp      otp
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_otp                 —           send_otp      otp
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_personal_details    —           —             —
22  agent     agent_request_pan                 —           —             पैन
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_request_email               —           —             email
27  agent     agent_request_address             —           —             address, pincode, locality, building, house number
28  agent     agent_request_terms_accept        —           —             terms and condition, terms
29  customer  customer_accept_terms             —           —             —
30  agent     agent_request_terms_accept        —           —             terms and condition, terms
31  agent     agent_ask_employment_type         —           —             salaried, self-employ
32  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो
33  agent     agent_ask_employment_type         —           —             salaried, self-employ
34  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो
35  agent     agent_help_address_error          —           —             error
36  agent     agent_request_otp                 —           send_otp      otp
37  customer  customer_provide_address          —           —             house number, flat
38  agent     agent_request_otp                 —           —             otp
39  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो
40  agent     agent_help_address_error          —           —             —
41  customer  customer_state_employment_type    —           —             self employ, self employee
42  agent     agent_request_income              —           —             income
43  agent     agent_request_business_details    —           —             business
44  customer  customer_report_done              —           —             हो गया
45  agent     agent_request_business_details    —           —             business
46  customer  customer_respond_udyam            —           —             —
47  agent     agent_request_udyam               —           —             udyam
48  customer  customer_skip_udyam               —           —             —
49  agent     agent_offer_skip_udyam            —           —             skip
50  agent     agent_request_otp                 —           send_otp      otp
51  customer  customer_request_wait             —           —             —
52  agent     agent_wait                        —           —             —
53  customer  customer_acknowledge              —           —             —
54  agent     agent_present_final_offer         —           —             final offer
55  customer  customer_query_fee                —           —             —
56  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 52bf189e (transferred) — 69 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_provide_personal_details —           —             —
4   agent     agent_answer_query                —           —             —
5   customer  customer_acknowledge              —           —             record
6   agent     agent_send_sms_link               —           send_sms      sms
7   customer  customer_greet                    —           —             hello
8   agent     agent_send_sms_link               —           send_sms      sms
9   customer  customer_ask_question             —           —             —
10  agent     agent_guide_open_link             —           —             —
11  customer  customer_report_sms_received      —           —             —
12  agent     agent_guide_apply                 —           —             apply now
13  customer  customer_acknowledge              —           —             —
14  agent     agent_request_otp                 —           —             —
15  customer  customer_ask_question             —           —             —
16  agent     agent_request_otp                 —           —             —
17  customer  customer_ask_question             —           —             —
18  agent     agent_request_otp                 —           —             —
19  customer  customer_report_done              —           —             —
20  agent     agent_request_otp                 —           send_otp      otp
21  customer  customer_report_done              —           —             कर दिया
22  agent     agent_request_pan                 —           —             पैन
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_request_email               —           —             email
27  customer  customer_report_done              —           —             कर दिया
28  agent     agent_request_address             —           —             address
29  customer  customer_ask_question             —           —             —
30  agent     agent_request_address             —           —             address, pincode, locality, building, house number
31  customer  customer_ask_question             —           —             —
32  agent     agent_request_address             —           —             address
33  customer  customer_acknowledge              —           —             —
34  agent     agent_request_terms_accept        —           —             terms and condition, terms
35  customer  customer_acknowledge              —           —             —
36  agent     agent_request_terms_accept        —           —             terms and condition, terms
37  customer  customer_accept_terms             —           —             —
38  agent     agent_ask_employment_type         —           —             salaried, self-employ
39  customer  customer_state_employment_type    —           —             —
40  agent     agent_ask_employment_type         —           —             salaried, self-employ
41  customer  customer_report_done              —           —             कर दिया
42  agent     agent_request_income              —           —             income
43  customer  customer_report_done              —           —             कर दिया
44  agent     agent_request_org_name            —           —             organization
45  customer  customer_report_done              —           —             कर दिया
46  agent     agent_request_email               —           —             email
47  customer  customer_report_done              —           —             कर दिया
48  agent     agent_request_business_details    —           —             —
49  customer  customer_report_done              —           —             कर दिया
50  agent     agent_acknowledge                 —           —             —
51  customer  customer_do_otp                   —           —             —
52  agent     agent_request_terms_accept        —           —             —
53  customer  customer_report_done              —           —             कर दिया
54  agent     agent_request_otp                 —           send_otp      otp
55  customer  customer_report_done              —           —             कर दिया
56  agent     agent_wait                        —           —             wait
57  customer  customer_acknowledge              —           —             —
58  agent     agent_wait                        —           —             —
59  customer  customer_agree                    —           —             —
60  agent     agent_present_final_offer         —           —             final offer
61  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
62  customer  customer_agree                    —           —             —
63  customer  customer_acknowledge              —           —             —
64  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
65  customer  customer_agree                    —           —             —
66  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
67  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
68  agent     agent_end_call                    —           —             —
```

## Call 53797d20 (transferred) — 41 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_acknowledge              —           —             —
7   agent     agent_guide_apply                 —           —             apply now
8   customer  customer_report_done              —           —             हो गया
9   agent     agent_request_otp                 —           —             —
10  customer  customer_report_done              —           —             हो गया
11  agent     agent_request_otp                 —           send_otp      otp
12  customer  customer_do_otp                   —           —             otp
13  agent     agent_wait                        —           —             wait
14  customer  customer_do_otp                   —           —             otp
15  agent     agent_wait                        —           —             wait
16  agent     agent_request_otp                 —           send_otp      otp
17  customer  customer_ask_question             —           —             —
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_ask_question             —           —             —
20  agent     agent_request_otp                 —           send_otp      otp
21  customer  customer_ask_question             —           —             —
22  agent     agent_answer_query                —           —             —
23  agent     agent_end_call                    —           —             —
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_guide_apply                 —           —             —
26  customer  customer_acknowledge              —           —             —
27  agent     agent_request_terms_accept        —           —             —
28  customer  customer_request_wait             —           —             —
29  agent     agent_wait                        —           —             —
30  agent     agent_present_final_offer         —           —             final offer
31  agent     agent_end_call                    —           —             —
32  customer  customer_acknowledge              —           —             —
33  agent     agent_present_final_offer         —           —             final offer
34  customer  customer_skip_udyam               —           —             —
35  agent     agent_offer_skip_udyam            —           —             skip
36  customer  customer_request_wait             —           —             wait
37  agent     agent_wait                        —           —             —
38  customer  customer_react_to_final_offer     —           —             —
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
40  customer  customer_other                    —           —             —
```

## Call 5b805354 (transferred) — 56 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             —
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_request_wait             —           —             —
3   agent     agent_wait                        —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             —
6   customer  customer_agree                    —           —             —
7   customer  customer_react_to_offer           —           —             —
8   agent     agent_present_offer               —           —             pre approved
9   customer  customer_query_fee                —           —             —
10  agent     agent_answer_query                —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms
12  customer  customer_report_sms_received      —           —             —
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
14  customer  customer_report_applied           —           —             apply now
15  agent     agent_guide_apply                 —           —             apply now
16  customer  customer_do_otp                   —           —             —
17  agent     agent_request_otp                 —           send_otp      otp
18  customer  customer_provide_personal_details —           —             gender
19  agent     agent_request_personal_details    —           —             gender, date of birth, marital
20  agent     agent_request_email               —           —             email
21  agent     agent_request_address             —           —             address, locality, building, house number, flat
22  agent     agent_request_terms_accept        —           —             terms and condition, terms
23  customer  customer_greet                    —           —             hello
24  agent     agent_request_terms_accept        —           —             terms and condition, terms
25  customer  customer_provide_address          —           —             address
26  agent     agent_request_address             —           —             address, locality, building, house number, flat
27  customer  customer_request_wait             —           —             —
28  agent     agent_acknowledge                 —           —             —
29  agent     agent_request_terms_accept        —           —             terms and condition, terms
30  customer  customer_request_wait             —           —             —
31  agent     agent_wait                        —           —             —
32  agent     agent_request_terms_accept        —           —             —
33  customer  customer_provide_income           —           —             income
34  agent     agent_ask_employment_type         —           —             —
35  customer  customer_state_employment_type    —           —             —
36  agent     agent_ask_employment_type         —           —             salaried, self-employ
37  customer  customer_state_employment_type    —           —             salaried
38  agent     agent_request_income              —           —             income
39  agent     agent_request_business_details    —           —             —
40  agent     agent_request_otp                 —           —             otp
41  customer  customer_ask_question             —           —             —
42  agent     agent_answer_query                —           —             —
43  customer  customer_acknowledge              —           —             —
44  agent     agent_request_email               —           —             email
45  agent     agent_request_business_details    —           —             —
46  customer  customer_report_address_error     —           —             —
47  customer  customer_report_address_error     —           —             —
48  agent     agent_help_address_error          —           —             —
49  customer  customer_report_done              —           —             हो गया
50  agent     agent_request_terms_accept        —           —             —
51  agent     agent_wait                        —           —             —
52  agent     agent_present_final_offer         —           —             —
53  customer  customer_react_to_final_offer     —           —             —
54  agent     agent_present_final_offer         —           —             —
55  customer  customer_react_to_final_offer     —           —             —
```

## Call 5d2f1ea1 (transferred) — 38 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   agent     agent_guide_apply                 —           —             apply now
7   agent     agent_request_otp                 —           send_otp      otp
8   agent     agent_request_otp                 —           send_otp      otp
9   agent     agent_request_personal_details    —           —             —
10  agent     agent_request_pan                 —           —             पैन
11  customer  customer_report_done              —           —             हो गया
12  agent     agent_request_personal_details    —           —             gender, date of birth, marital
13  customer  customer_report_done              —           —             हो गया
14  agent     agent_request_email               —           —             email
15  customer  customer_report_done              —           —             हो गया
16  agent     agent_request_address             —           —             address, pincode, locality, building, house number
17  customer  customer_ask_question             —           —             —
18  agent     agent_request_terms_accept        —           —             terms and condition, terms
19  customer  customer_report_done              —           —             हो गया
20  agent     agent_ask_employment_type         —           —             salaried, self-employ
21  customer  customer_state_employment_type    —           —             —
22  agent     agent_ask_employment_type         —           —             salaried, self-employ
23  customer  customer_state_employment_type    —           —             —
24  agent     agent_request_income              —           —             income
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_request_org_name            —           —             organization
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_email               —           —             email
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_business_details    —           —             —
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_terms_accept        —           —             —
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_otp                 —           send_otp      otp
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_present_final_offer         —           —             final offer
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 5e6f5156 (transferred) — 92 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             record
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_send_sms_link               —           send_sms      sms
8   customer  customer_ask_question             —           —             —
9   agent     agent_send_sms_link               —           —             sms
10  agent     agent_ask_to_repeat               —           —             फिर से कह
11  customer  customer_react_to_offer           —           —             personal loan
12  agent     agent_guide_apply                 —           —             apply now
13  customer  customer_do_otp                   —           —             —
14  agent     agent_request_otp                 —           —             —
15  customer  customer_acknowledge              —           —             —
16  agent     agent_request_otp                 —           —             —
17  customer  customer_do_otp                   —           —             —
18  agent     agent_answer_query                —           —             —
19  customer  customer_report_done              —           —             —
20  agent     agent_request_terms_accept        —           —             terms and condition, terms
21  customer  customer_do_otp                   —           —             otp
22  agent     agent_request_otp                 —           —             otp
23  customer  customer_do_otp                   —           —             otp
24  agent     agent_request_otp                 —           —             otp
25  customer  customer_provide_pan              —           —             pan
26  agent     agent_request_personal_details    —           —             gender, date of birth, marital
27  customer  customer_ask_question             —           —             —
28  agent     agent_answer_query                —           —             —
29  customer  customer_provide_pan              —           —             —
30  agent     agent_request_pan                 —           —             पैन
31  customer  customer_report_address_error     —           —             error
32  agent     agent_help_address_error          —           —             error
33  customer  customer_report_address_error     —           —             —
34  agent     agent_request_terms_accept        —           —             terms
35  customer  customer_acknowledge              —           —             —
36  agent     agent_request_terms_accept        —           —             terms and condition, terms
37  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो
38  agent     agent_help_address_error          —           —             error, नहीं हो रहा
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_terms_accept        —           —             —
41  customer  customer_provide_income           —           —             income
42  agent     agent_request_income              —           —             income
43  customer  customer_provide_personal_details —           —             —
44  agent     agent_request_personal_details    —           —             —
45  agent     agent_request_income              —           —             income
46  customer  customer_report_done              —           —             —
47  agent     agent_request_personal_details    —           —             —
48  customer  customer_report_done              —           —             हो गया
49  agent     agent_ask_employment_type         —           —             salaried, self-employ
50  customer  customer_ask_question             —           —             —
51  agent     agent_ask_employment_type         —           —             —
52  customer  customer_state_employment_type    —           —             —
53  agent     agent_ask_employment_type         —           —             salaried
54  customer  customer_report_done              —           —             हो गया
55  agent     agent_request_income              —           —             income
56  customer  customer_provide_business_details —           —             —
57  agent     agent_request_business_details    —           —             —
58  customer  customer_report_done              —           —             हो गया
59  agent     agent_request_terms_accept        —           —             —
60  agent     agent_ask_to_repeat               —           —             एक बार फिर
61  customer  customer_other                    —           —             —
62  agent     agent_wait                        —           —             —
63  customer  customer_report_done              —           —             —
64  agent     agent_present_final_offer         —           —             final offer
65  customer  customer_do_otp                   —           —             otp
66  agent     agent_request_otp                 —           —             otp
67  customer  customer_report_applied           —           —             apply now
68  agent     agent_guide_apply                 —           —             apply now
69  customer  customer_report_applied           —           —             —
70  agent     agent_guide_apply                 —           —             —
71  customer  customer_provide_pan              —           —             pan
72  agent     agent_request_pan                 —           —             पैन
73  customer  customer_acknowledge              —           —             —
74  agent     agent_request_pan                 —           —             पैन
75  agent     agent_end_call                    —           —             —
76  customer  customer_report_done              —           —             हो गया
77  agent     agent_acknowledge                 —           —             —
78  customer  customer_ask_question             —           —             —
79  agent     agent_request_terms_accept        —           —             —
80  customer  customer_report_done              —           —             —
81  agent     agent_confirm                     —           —             —
82  customer  customer_acknowledge              —           —             —
83  agent     agent_request_personal_details    —           —             —
84  customer  customer_react_to_final_offer     —           —             —
85  agent     agent_present_final_offer         —           —             final offer
86  customer  customer_react_to_final_offer     —           —             —
87  agent     agent_present_final_offer         —           —             final offer
88  customer  customer_react_to_final_offer     —           —             —
89  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
90  customer  customer_agree                    —           —             —
91  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 606af2e2 (transferred) — 67 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             —
2   customer  customer_other                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_other                    —           —             —
5   agent     agent_present_offer               —           —             —
6   customer  customer_other                    —           —             —
7   agent     agent_present_offer               —           —             pre-approved
8   customer  customer_other                    —           —             —
9   agent     agent_confirm                     —           —             —
10  customer  customer_other                    —           —             —
11  agent     agent_greet                       —           —             —
12  customer  customer_other                    —           —             —
13  agent     agent_confirm                     —           —             —
14  customer  customer_other                    —           —             —
15  agent     agent_acknowledge                 —           —             —
16  customer  customer_other                    —           —             —
17  agent     agent_acknowledge                 —           —             —
18  customer  customer_other                    —           —             —
19  agent     agent_acknowledge                 —           —             —
20  customer  customer_greet                    —           —             hello
21  agent     agent_present_offer               —           —             —
22  customer  customer_agree                    confused    —             कैसे
23  agent     agent_send_sms_link               —           send_sms      sms
24  agent     agent_send_sms_link               —           send_sms      sms
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_guide_apply                 —           —             apply now
27  customer  customer_report_done              —           —             —
28  agent     agent_guide_apply                 —           —             apply now
29  customer  customer_report_done              —           —             कर दिया
30  agent     agent_request_otp                 —           send_otp      otp
31  customer  customer_report_done              —           —             कर दिया
32  agent     agent_request_otp                 —           send_otp      otp
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_personal_details    —           —             —
35  customer  customer_agree                    —           —             —
36  agent     agent_request_pan                 —           —             पैन
37  customer  customer_report_done              —           —             भर दिया, कर दिया
38  agent     agent_request_personal_details    —           —             gender, date of birth, marital
39  customer  customer_report_done              —           —             हो गया, कर दिया
40  agent     agent_request_email               —           —             email
41  customer  customer_report_done              —           —             हो गया, कर दिया
42  agent     agent_request_address             —           —             address, pincode, locality, building, house number
43  customer  customer_report_done              —           —             कर दिया
44  agent     agent_request_terms_accept        —           —             terms and condition, terms
45  customer  customer_accept_terms             —           —             —
46  agent     agent_ask_employment_type         —           —             —
47  customer  customer_report_done              —           —             भर दिया
48  agent     agent_ask_employment_type         —           —             salaried, self-employ
49  customer  customer_state_employment_type    —           —             self employ
50  agent     agent_request_income              —           —             income
51  customer  customer_report_done              —           —             कर दिया
52  agent     agent_request_org_name            —           —             —
53  customer  customer_report_done              —           —             कर दिया
54  agent     agent_request_business_details    —           —             business
55  customer  customer_report_done              —           —             कर दिया
56  agent     agent_request_udyam               —           —             udyam
57  customer  customer_acknowledge              —           —             —
58  agent     agent_request_otp                 —           send_otp      otp
59  customer  customer_report_done              —           —             हो गया, भर दिया
60  agent     agent_confirm                     —           —             आगे बढ़
61  customer  customer_acknowledge_transfer     —           —             —
62  agent     agent_present_final_offer         —           —             final offer
63  customer  customer_react_to_final_offer     —           —             —
64  agent     agent_present_final_offer         —           —             final offer
65  customer  customer_acknowledge_transfer     —           —             —
66  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 6187fa3c (transferred) — 56 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   customer  customer_request_wait             —           —             —
6   agent     agent_wait                        —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   agent     agent_guide_open_link             —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_request_wait             —           —             wait
11  agent     agent_wait                        —           —             —
12  customer  customer_ask_question             —           —             —
13  agent     agent_guide_apply                 —           —             apply now
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_request_otp                 —           send_otp      otp
16  agent     agent_request_otp                 —           send_otp      otp
17  agent     agent_request_otp                 —           —             otp
18  agent     agent_request_pan                 —           —             पैन
19  customer  customer_request_wait             —           —             wait
20  agent     agent_wait                        —           —             —
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital
22  customer  customer_acknowledge              —           —             —
23  agent     agent_request_email               —           —             email
24  customer  customer_acknowledge              —           —             —
25  agent     agent_request_address             —           —             address, pincode, locality, building, house number
26  customer  customer_request_wait             —           —             wait
27  agent     agent_wait                        —           —             —
28  customer  customer_report_done              —           —             कर दिया
29  agent     agent_request_terms_accept        —           —             terms and condition, terms
30  customer  customer_report_address_error     —           —             —
31  agent     agent_help_address_error          —           —             red, error
32  agent     agent_ask_employment_type         —           —             salaried, self-employ
33  agent     agent_ask_employment_type         —           —             salaried, self-employ
34  customer  customer_request_wait             —           —             wait
35  agent     agent_wait                        —           —             —
36  agent     agent_request_income              —           —             income
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_org_name            —           —             organization
39  agent     agent_request_email               —           —             email
40  agent     agent_request_business_details    —           —             —
41  customer  customer_request_wait             —           —             wait
42  agent     agent_wait                        —           —             —
43  agent     agent_ask_to_repeat               —           —             फिर से कह
44  customer  customer_request_wait             —           —             wait
45  agent     agent_wait                        —           —             —
46  agent     agent_request_terms_accept        —           —             —
47  customer  customer_request_wait             —           —             wait
48  agent     agent_request_otp                 —           send_otp      otp
49  customer  customer_request_wait             —           —             wait
50  agent     agent_wait                        —           —             wait
51  agent     agent_request_otp                 —           send_otp      otp
52  customer  customer_report_done              —           —             —
53  agent     agent_present_final_offer         —           —             final offer
54  customer  customer_react_to_final_offer     —           —             —
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 65d3a240 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_ask_question             —           —             —
4   agent     agent_answer_query                —           —             —
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_report_link_opened       —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_acknowledge              —           —             —
11  agent     agent_request_otp                 —           send_otp      otp
12  agent     agent_request_otp                 —           send_otp      otp
13  agent     agent_request_otp                 —           —             otp
14  customer  customer_do_otp                   —           —             —
15  agent     agent_request_pan                 —           —             पैन
16  customer  customer_report_done              —           —             हो गया
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_email               —           —             email
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_address             —           —             address, pincode, locality, building, house number
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_terms_accept        —           —             terms and condition, terms
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_ask_employment_type         —           —             salaried, self-employ
26  customer  customer_report_done              —           —             हो गया
27  agent     agent_ask_employment_type         —           —             salaried, self-employ
28  customer  customer_state_employment_type    —           —             —
29  agent     agent_request_income              —           —             income
30  customer  customer_report_done              —           —             —
31  agent     agent_request_org_name            —           —             organization
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_email               —           —             email
34  customer  customer_report_done              —           —             —
35  agent     agent_request_business_details    —           —             —
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_guide_apply                 —           —             —
38  agent     agent_ask_to_repeat               —           —             फिर से कह
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_otp                 —           send_otp      otp
41  customer  customer_report_done              —           —             हो गया
42  agent     agent_present_final_offer         —           —             final offer
43  customer  customer_react_to_final_offer     —           —             —
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 696e940c (transferred) — 49 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते
2   customer  customer_provide_personal_details —           —             —
3   agent     agent_request_personal_details    —           —             —
4   customer  customer_provide_personal_details —           —             —
5   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
6   customer  customer_agree                    —           —             —
7   customer  customer_ask_question             confused    —             कैसे
8   customer  customer_greet                    —           —             hello
9   agent     agent_explain_fee                 —           —             interest rate
10  agent     agent_ask_to_repeat               —           —             —
11  customer  customer_acknowledge              —           —             —
12  agent     agent_guide_open_link             —           —             —
13  customer  customer_report_link_opened       —           —             —
14  agent     agent_guide_open_link             —           —             —
15  customer  customer_unclear                  —           —             —
16  agent     agent_guide_open_link             —           —             —
17  agent     agent_guide_open_link             —           —             —
18  customer  customer_report_sms_received      —           —             sms
19  agent     agent_send_sms_link               —           send_sms      sms
20  customer  customer_report_sms_received      —           —             —
21  agent     agent_send_sms_link               —           send_sms      sms
22  customer  customer_report_sms_received      —           —             —
23  agent     agent_guide_apply                 —           —             apply now
24  customer  customer_report_done              —           —             —
25  agent     agent_request_otp                 —           send_otp      otp
26  customer  customer_report_applied           —           —             —
27  agent     agent_request_otp                 —           send_otp      otp
28  agent     agent_ask_to_repeat               —           —             फिर से कह
29  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो
30  agent     agent_request_otp                 —           send_otp      otp
31  customer  customer_do_otp                   —           —             —
32  agent     agent_request_otp                 —           send_otp      otp
33  customer  customer_do_otp                   —           —             otp
34  agent     agent_request_otp                 —           —             otp
35  agent     agent_ask_to_repeat               —           —             —
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_present_final_offer         —           —             final offer
38  customer  customer_react_to_final_offer     —           —             —
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
42  customer  customer_ask_question             —           —             —
43  agent     agent_greet                       —           —             —
44  customer  customer_acknowledge              —           —             —
45  agent     agent_guide_open_link             —           —             —
46  customer  customer_report_done              —           —             कर दिया
47  agent     agent_send_sms_link               —           send_sms      sms
48  agent     agent_end_call                    —           —             —
```

## Call 69b2ff40 (transferred) — 27 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_present_offer               —           —             —
3   customer  customer_agree                    —           —             —
4   customer  customer_react_to_offer           —           —             —
5   customer  customer_ask_question             —           —             —
6   agent     agent_explain_fee                 —           —             interest rate
7   customer  customer_ask_question             —           —             —
8   agent     agent_send_sms_link               —           send_sms      sms
9   customer  customer_agree                    —           —             —
10  agent     agent_send_sms_link               —           send_sms      sms
11  customer  customer_report_sms_received      —           —             —
12  agent     agent_send_sms_link               —           send_sms      sms
13  customer  customer_request_wait             —           —             —
14  agent     agent_wait                        —           —             —
15  customer  customer_request_wait             —           —             —
16  agent     agent_wait                        —           —             —
17  customer  customer_request_wait             —           —             —
18  agent     agent_wait                        —           —             —
19  customer  customer_express_distrust         —           —             —
20  agent     agent_reassure_trust              —           —             —
21  customer  customer_acknowledge              —           —             —
22  agent     agent_guide_open_link             —           —             लिंक पर क्लिक
23  customer  customer_react_to_offer           —           —             —
24  agent     agent_present_offer               —           —             pre approved, loan offer, personal loan
25  customer  customer_agree                    —           —             —
26  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 6cd62134 (transferred) — 44 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_send_sms_link               —           send_sms      sms
3   agent     agent_guide_open_link             —           —             —
4   agent     agent_guide_apply                 —           —             apply now
5   agent     agent_request_otp                 —           send_otp      otp
6   agent     agent_request_otp                 —           send_otp      otp
7   agent     agent_request_otp                 —           —             otp
8   agent     agent_request_pan                 —           —             पैन
9   customer  customer_ask_question             —           —             —
10  agent     agent_request_pan                 —           —             पैन
11  agent     agent_request_personal_details    —           —             gender, date of birth, marital
12  customer  customer_report_done              —           —             हो गया
13  agent     agent_request_email               —           —             email
14  agent     agent_clarify                     —           —             —
15  agent     agent_request_email               —           —             email
16  customer  customer_report_done              —           —             कर दिया
17  agent     agent_request_address             —           —             address, pincode, locality, building, house number
18  agent     agent_clarify                     —           —             —
19  customer  customer_report_done              —           —             कर दिया
20  agent     agent_request_terms_accept        —           —             terms and condition, terms
21  customer  customer_report_done              —           —             —
22  agent     agent_ask_employment_type         —           —             salaried, self-employ
23  agent     agent_ask_to_repeat               —           —             फिर से कह
24  customer  customer_state_employment_type    —           —             —
25  agent     agent_ask_employment_type         —           —             salaried, self-employ
26  customer  customer_state_employment_type    —           —             —
27  agent     agent_request_income              —           —             income
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_org_name            —           —             organization
30  agent     agent_ask_to_repeat               —           —             —
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_email               —           —             —
33  agent     agent_request_email               —           —             email
34  agent     agent_clarify                     —           —             —
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_business_details    —           —             —
37  customer  customer_report_done              —           —             कर दिया
38  agent     agent_guide_apply                 —           —             —
39  customer  customer_report_done              —           —             कर दिया
40  agent     agent_request_otp                 —           send_otp      otp
41  customer  customer_report_done              —           —             हो गया
42  agent     agent_present_final_offer         —           —             final offer
43  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 6d27dee2 (transferred) — 61 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_express_distrust         —           —             —
3   agent     agent_reassure_trust              —           —             —
4   customer  customer_agree                    confused    —             कैसे
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_guide_open_link             —           —             —
7   customer  customer_request_wait             —           —             —
8   agent     agent_wait                        —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_acknowledge              —           —             —
11  agent     agent_greet                       —           —             —
12  customer  customer_agree                    —           —             —
13  agent     agent_request_personal_details    —           —             —
14  customer  customer_acknowledge              —           —             —
15  agent     agent_request_pan                 —           —             पैन
16  customer  customer_ask_question             —           —             —
17  agent     agent_request_pan                 —           —             पैन
18  agent     agent_request_pan                 —           —             पैन
19  agent     agent_end_call                    —           —             —
20  agent     agent_ask_to_repeat               —           —             —
21  customer  customer_greet                    —           —             hello
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_email               —           —             email
25  customer  customer_report_done              —           —             —
26  agent     agent_request_address             —           —             address, pincode, locality, building, house number
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_terms_accept        —           —             terms and condition, terms
29  customer  customer_accept_terms             —           —             —
30  agent     agent_request_terms_accept        —           —             terms and condition, terms
31  customer  customer_report_done              —           —             —
32  agent     agent_ask_employment_type         —           —             salaried, self-employ
33  agent     agent_ask_to_repeat               —           —             फिर से कह
34  customer  customer_state_employment_type    —           —             self employ
35  agent     agent_request_income              —           —             income
36  agent     agent_request_org_name            —           —             —
37  agent     agent_request_business_details    —           —             business
38  customer  customer_report_done              —           —             हो गया
39  agent     agent_request_udyam               —           —             udyam
40  customer  customer_respond_udyam            —           —             —
41  agent     agent_offer_skip_udyam            —           —             skip
42  agent     agent_request_otp                 —           send_otp      otp
43  agent     agent_wait                        —           —             wait
44  agent     agent_wait                        —           —             —
45  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
48  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
49  agent     agent_ask_to_repeat               —           —             —
50  agent     agent_acknowledge                 —           —             —
51  customer  customer_acknowledge              —           —             —
52  agent     agent_present_final_offer         —           —             final offer
53  customer  customer_react_to_final_offer     —           —             —
54  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
56  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
57  agent     agent_ask_to_repeat               —           —             —
58  customer  customer_request_wait             —           —             —
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
60  agent     agent_transfer_to_rm              —           transfer_to_rm—
```

## Call 709d4cce (transferred) — 58 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             record
1   agent     agent_other                       —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             hello
4   agent     agent_present_offer               —           —             pre-approved, loan offer
5   customer  customer_react_to_offer           —           —             —
6   agent     agent_present_offer               —           —             —
7   customer  customer_provide_address          —           —             address, आधार
8   customer  customer_provide_address          —           —             address, आधार
9   agent     agent_request_address             —           —             address, आधार
10  customer  customer_ask_question             —           —             —
11  customer  customer_report_sms_received      —           —             link भेज
12  agent     agent_send_sms_link               —           send_sms      sms
13  agent     agent_guide_open_link             —           —             —
14  customer  customer_acknowledge              —           —             —
15  agent     agent_guide_apply                 —           —             apply now
16  customer  customer_report_applied           —           —             apply now
17  agent     agent_request_otp                 —           send_otp      otp
18  customer  customer_react_to_offer           —           —             —
19  agent     agent_request_otp                 —           send_otp      otp
20  customer  customer_provide_pan              —           —             —
21  agent     agent_request_pan                 —           —             पैन
22  customer  customer_ask_question             —           —             —
23  agent     agent_answer_query                —           —             —
24  customer  customer_ask_question             —           —             —
25  agent     agent_request_personal_details    —           —             gender, date of birth
26  customer  customer_provide_address          —           —             building, house number, flat
27  agent     agent_request_address             —           —             address, pincode, locality, building, house number
28  customer  customer_provide_address          —           —             house number
29  agent     agent_request_address             —           —             —
30  customer  customer_report_address_error     —           —             —
31  customer  customer_provide_address          —           —             locality, building, flat
32  customer  customer_provide_address          —           —             —
33  customer  customer_report_address_error     —           —             —
34  customer  customer_provide_address          —           —             —
35  customer  customer_accept_terms             —           —             —
36  agent     agent_request_terms_accept        —           —             terms and condition, terms
37  customer  customer_state_employment_type    —           —             —
38  agent     agent_ask_employment_type         —           —             —
39  customer  customer_provide_income           —           —             income
40  customer  customer_provide_org_name         —           —             organization
41  agent     agent_request_org_name            —           —             organization
42  customer  customer_provide_org_name         —           —             —
43  customer  customer_provide_org_name         —           —             —
44  customer  customer_provide_email            —           —             —
45  agent     agent_request_email               —           —             email
46  customer  customer_provide_business_details —           —             —
47  agent     agent_request_business_details    —           —             —
48  customer  customer_report_done              —           —             —
49  agent     agent_request_terms_accept        —           —             —
50  customer  customer_request_wait             —           —             —
51  agent     agent_wait                        —           —             wait
52  customer  customer_react_to_final_offer     —           —             —
53  agent     agent_present_final_offer         —           —             final offer
54  customer  customer_query_fee                —           —             processing fee
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
56  customer  customer_acknowledge              —           —             —
57  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 715e7ec7 (transferred) — 68 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_agree                    —           —             —
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   customer  customer_react_to_offer           —           —             —
4   agent     agent_explain_fee                 —           —             interest rate
5   customer  customer_other                    —           —             —
6   customer  customer_other                    —           —             —
7   agent     agent_acknowledge                 —           —             —
8   customer  customer_ask_question             —           —             —
9   customer  customer_other                    —           —             —
10  agent     agent_send_sms_link               —           send_sms      sms
11  customer  customer_other                    —           —             —
12  agent     agent_send_sms_link               —           send_sms      sms
13  customer  customer_acknowledge              —           —             —
14  agent     agent_send_sms_link               —           —             sms
15  customer  customer_report_sms_received      —           —             —
16  agent     agent_guide_open_link             —           —             —
17  customer  customer_report_link_opened       —           —             —
18  agent     agent_guide_apply                 —           —             apply now
19  customer  customer_other                    —           —             —
20  agent     agent_guide_apply                 —           —             apply now
21  agent     agent_request_otp                 —           send_otp      otp
22  customer  customer_acknowledge              —           —             —
23  agent     agent_request_otp                 —           send_otp      otp
24  agent     agent_ask_to_repeat               —           —             —
25  customer  customer_other                    —           —             —
26  agent     agent_ask_to_repeat               —           —             फिर से कह
27  agent     agent_request_pan                 —           —             पैन
28  customer  customer_acknowledge              —           —             —
29  agent     agent_request_personal_details    —           —             gender, date of birth, marital
30  agent     agent_request_email               —           —             email
31  customer  customer_other                    —           —             —
32  customer  customer_other                    —           —             —
33  customer  customer_ask_question             —           —             —
34  agent     agent_guide_open_link             —           —             —
35  customer  customer_acknowledge              —           —             —
36  agent     agent_greet                       —           —             —
37  customer  customer_ask_question             —           —             —
38  agent     agent_greet                       —           —             —
39  customer  customer_ask_question             —           —             —
40  agent     agent_greet                       —           —             —
41  customer  customer_other                    —           —             —
42  agent     agent_guide_open_link             —           —             —
43  customer  customer_agree                    —           —             —
44  customer  customer_other                    —           —             —
45  agent     agent_confirm                     —           —             आगे बढ़
46  customer  customer_agree                    —           —             —
47  agent     agent_send_sms_link               —           send_sms      sms
48  customer  customer_agree                    —           —             —
49  agent     agent_send_sms_link               —           send_sms      sms
50  customer  customer_acknowledge              —           —             —
51  agent     agent_guide_open_link             —           —             —
52  agent     agent_guide_apply                 —           —             apply now
53  agent     agent_guide_apply                 —           —             apply now
54  customer  customer_acknowledge              —           —             —
55  agent     agent_request_otp                 —           send_otp      otp
56  customer  customer_acknowledge              —           —             —
57  agent     agent_request_otp                 —           send_otp      otp
58  customer  customer_acknowledge              —           —             —
59  agent     agent_request_otp                 —           —             otp
60  customer  customer_do_otp                   —           —             otp
61  agent     agent_request_otp                 —           —             otp
62  customer  customer_acknowledge              —           —             —
63  agent     agent_present_final_offer         —           —             —
64  customer  customer_acknowledge              —           —             —
65  agent     agent_present_final_offer         —           —             final offer
66  agent     agent_transfer_to_rm              —           transfer_to_rm—
67  customer  customer_request_wait             —           —             —
```

## Call 77bb4be2 (transferred) — 22 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello, से बात
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms
7   customer  customer_report_sms_received      —           —             —
8   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
9   agent     agent_guide_open_link             —           —             —
10  customer  customer_report_done              —           —             कर लिया
11  agent     agent_request_otp                 —           —             —
12  customer  customer_ask_query                —           —             —
13  agent     agent_answer_query                —           —             —
14  customer  customer_ask_question             —           —             —
15  agent     agent_answer_query                —           —             —
16  customer  customer_ask_query                —           —             —
17  customer  customer_ask_question             frustrated  —             कब तक
18  agent     agent_answer_query                —           —             —
19  customer  customer_react_to_final_offer     —           —             —
20  agent     agent_present_final_offer         —           —             final offer
21  customer  customer_react_to_final_offer     —           —             —
```

## Call 78dbd7a8 (transferred) — 100 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_query_fee                —           —             emi
5   agent     agent_explain_fee                 —           —             interest rate
6   customer  customer_agree                    —           —             —
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_report_sms_received      —           —             sms
9   agent     agent_wait                        —           —             —
10  customer  customer_request_wait             —           —             —
11  agent     agent_wait                        —           —             —
12  customer  customer_report_link_opened       —           —             —
13  agent     agent_guide_apply                 —           —             apply now
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_do_otp                   —           —             —
17  agent     agent_ask_to_repeat               —           —             फिर से कह
18  customer  customer_respond_udyam            —           —             उद्यम
19  agent     agent_request_udyam               —           —             उद्यम
20  customer  customer_acknowledge              —           —             —
21  agent     agent_request_otp                 —           send_otp      otp
22  agent     agent_wait                        —           —             wait
23  agent     agent_wait                        —           —             —
24  agent     agent_present_final_offer         —           —             final offer
25  customer  customer_query_fee                —           —             —
26  agent     agent_explain_fee                 —           —             interest rate
27  customer  customer_query_fee                —           —             —
28  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
29  customer  customer_agree                    —           —             —
30  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
31  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
32  agent     agent_ask_to_repeat               —           —             फिर से कह, एक बार फिर
33  customer  customer_acknowledge_transfer     —           —             —
34  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
35  customer  customer_query_fee                —           —             —
36  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
37  customer  customer_query_fee                —           —             —
38  customer  customer_query_fee                —           —             —
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
40  customer  customer_ask_question             —           —             —
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
42  customer  customer_ask_question             —           —             —
43  agent     agent_transfer_to_rm              —           transfer_to_rm—
44  customer  customer_agree                    —           —             —
45  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
46  customer  customer_query_fee                —           —             —
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
48  customer  customer_query_fee                —           —             —
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
50  customer  customer_query_fee                —           —             —
51  customer  customer_acknowledge              —           —             —
52  customer  customer_query_fee                —           —             —
53  agent     agent_acknowledge                 —           —             —
54  customer  customer_ask_question             —           —             —
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
56  customer  customer_query_fee                —           —             —
57  customer  customer_query_fee                —           —             —
58  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
59  customer  customer_agree                    —           —             —
60  customer  customer_ask_question             frustrated  —             कब तक
61  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
62  customer  customer_acknowledge              —           —             —
63  customer  customer_acknowledge              frustrated  —             दोबारा
64  customer  customer_other                    frustrated  —             दोबारा
65  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
66  customer  customer_acknowledge              —           —             —
67  agent     agent_transfer_to_rm              —           transfer_to_rm—
68  customer  customer_ask_question             —           —             —
69  customer  customer_query_fee                —           —             —
70  customer  customer_acknowledge              —           —             —
71  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
72  customer  customer_ask_question             —           —             —
73  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
74  customer  customer_ask_question             —           —             —
75  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
76  customer  customer_acknowledge_transfer     —           —             —
77  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
78  customer  customer_acknowledge              —           —             —
79  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
80  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
81  customer  customer_ask_question             —           —             —
82  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
83  customer  customer_ask_question             —           —             —
84  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
85  customer  customer_query_fee                —           —             —
86  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
87  customer  customer_report_done              —           —             कर दिया
88  customer  customer_provide_pan              —           —             pan
89  customer  customer_acknowledge              —           —             —
90  customer  customer_ask_question             —           —             —
91  customer  customer_acknowledge              —           —             —
92  customer  customer_acknowledge              —           —             —
93  customer  customer_greet                    —           —             hello
94  agent     agent_transfer_to_rm              —           transfer_to_rm—
95  customer  customer_acknowledge              —           —             —
96  agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
97  customer  customer_agree                    —           —             —
98  customer  customer_greet                    —           —             hello
99  agent     agent_explain_fee                 —           —             interest rate
```

## Call 7986eb00 (transferred) — 41 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_greet                    —           —             —
5   agent     agent_present_offer               —           —             pre-approved, loan offer
6   customer  customer_agree                    —           —             —
7   agent     agent_present_offer               —           —             —
8   customer  customer_ask_question             —           —             —
9   customer  customer_query_fee                —           —             —
10  customer  customer_ask_query                —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms
12  customer  customer_agree                    —           —             —
13  agent     agent_send_sms_link               —           send_sms      sms
14  agent     agent_guide_open_link             —           —             —
15  agent     agent_ask_to_repeat               —           —             —
16  customer  customer_report_link_opened       —           —             —
17  agent     agent_guide_apply                 —           —             apply now
18  customer  customer_report_link_opened       —           —             —
19  agent     agent_answer_query                —           —             —
20  customer  customer_report_done              —           —             —
21  agent     agent_request_otp                 —           send_otp      otp
22  customer  customer_acknowledge              —           —             —
23  agent     agent_request_otp                 —           send_otp      otp
24  agent     agent_request_otp                 —           send_otp      otp
25  agent     agent_request_pan                 —           —             पैन
26  customer  customer_acknowledge              —           —             —
27  agent     agent_request_personal_details    —           —             —
28  customer  customer_greet                    —           —             hello
29  agent     agent_request_personal_details    —           —             gender, date of birth, marital
30  agent     agent_ask_to_repeat               —           —             फिर से कह, एक बार फिर
31  customer  customer_request_wait             —           —             रुकिए
32  agent     agent_wait                        —           —             —
33  customer  customer_ask_question             —           —             —
34  agent     agent_ask_to_repeat               —           —             फिर से बता
35  customer  customer_react_to_final_offer     —           —             —
36  customer  customer_react_to_final_offer     —           —             —
37  agent     agent_present_final_offer         —           —             final offer
38  customer  customer_react_to_final_offer     —           —             —
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
40  customer  customer_acknowledge              —           —             —
```

## Call 799e5a0e (transferred) — 35 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_acknowledge              —           —             —
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_acknowledge              —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_acknowledge              —           —             —
11  agent     agent_guide_apply                 —           —             apply now
12  customer  customer_report_link_opened       —           —             —
13  agent     agent_guide_open_link             —           —             —
14  customer  customer_ask_question             —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_do_otp                   —           —             otp
17  agent     agent_request_otp                 —           —             otp
18  agent     agent_ask_to_repeat               —           —             फिर से कह
19  customer  customer_react_to_offer           —           —             —
20  agent     agent_request_otp                 —           —             otp
21  customer  customer_do_otp                   —           —             otp
22  agent     agent_request_pan                 —           —             पैन
23  customer  customer_react_to_final_offer     —           —             —
24  agent     agent_present_final_offer         —           —             final offer
25  customer  customer_react_to_final_offer     —           —             —
26  agent     agent_explain_fee                 —           —             interest rate
27  customer  customer_react_to_final_offer     —           —             —
28  agent     agent_present_final_offer         —           —             final offer
29  customer  customer_agree                    —           —             —
30  agent     agent_present_final_offer         —           —             final offer
31  customer  customer_provide_address          —           —             —
32  agent     agent_present_final_offer         —           —             final offer
33  customer  customer_acknowledge              —           —             —
34  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 7e3575b7 (transferred) — 50 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_report_sms_received      —           —             —
9   agent     agent_send_sms_link               —           —             sms
10  customer  customer_acknowledge              —           —             —
11  agent     agent_send_sms_link               —           —             sms
12  customer  customer_report_sms_received      —           —             —
13  agent     agent_wait                        —           —             wait
14  agent     agent_ask_to_repeat               —           —             फिर से कह
15  customer  customer_agree                    —           —             —
16  agent     agent_send_sms_link               —           —             sms
17  customer  customer_report_sms_received      —           —             —
18  agent     agent_wait                        —           —             —
19  agent     agent_ask_to_repeat               —           —             —
20  customer  customer_other                    —           —             —
21  agent     agent_send_sms_link               —           send_sms      sms
22  customer  customer_other                    —           —             —
23  agent     agent_send_sms_link               —           send_sms      sms
24  agent     agent_guide_open_link             —           —             —
25  customer  customer_report_link_opened       —           —             —
26  agent     agent_guide_apply                 —           —             apply now
27  customer  customer_do_otp                   —           —             —
28  agent     agent_request_otp                 —           send_otp      otp
29  customer  customer_ask_question             —           —             —
30  agent     agent_request_otp                 —           send_otp      otp
31  agent     agent_request_otp                 —           send_otp      otp
32  customer  customer_provide_email            —           —             —
33  agent     agent_request_email               —           —             email
34  customer  customer_ask_question             —           —             —
35  agent     agent_request_email               —           —             email
36  customer  customer_report_done              —           —             कर दिया
37  agent     agent_request_address             —           —             address, pincode, locality, building, house number
38  customer  customer_report_done              —           —             —
39  agent     agent_request_address             —           —             address, pincode, locality, building, house number
40  agent     agent_request_terms_accept        —           —             terms and condition, terms
41  agent     agent_ask_employment_type         —           —             salaried, self-employ
42  customer  customer_respond_udyam            —           —             —
43  agent     agent_request_otp                 —           —             —
44  agent     agent_request_otp                 —           send_otp      otp
45  agent     agent_request_otp                 —           send_otp      otp
46  agent     agent_request_otp                 —           —             otp
47  agent     agent_present_final_offer         —           —             final offer
48  customer  customer_acknowledge              —           —             —
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 7fd658f2 (transferred) — 73 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             —
3   agent     agent_ask_to_repeat               —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           —             —
6   customer  customer_acknowledge              —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   agent     agent_send_sms_link               —           send_sms      sms
9   customer  customer_acknowledge              —           —             —
10  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
11  customer  customer_report_link_opened       —           —             खुल गया
12  agent     agent_guide_apply                 —           —             apply now
13  customer  customer_report_applied           —           —             apply now
14  agent     agent_request_otp                 —           send_otp      otp
15  customer  customer_do_otp                   —           —             —
16  agent     agent_clarify                     —           —             —
17  customer  customer_provide_pan              —           —             pan
18  agent     agent_request_pan                 —           —             पैन
19  customer  customer_provide_pan              —           —             —
20  agent     agent_request_personal_details    —           —             —
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_email               —           —             email
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_address             —           —             —
25  agent     agent_end_call                    —           —             —
26  customer  customer_report_done              —           —             हो गया
27  agent     agent_request_terms_accept        —           —             terms and condition, terms
28  customer  customer_other                    —           —             —
29  agent     agent_ask_employment_type         —           —             salaried, self-employ
30  agent     agent_ask_employment_type         —           —             salaried, self-employ
31  customer  customer_state_employment_type    —           —             salaried
32  agent     agent_request_income              —           —             income
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_org_name            —           —             organization
35  customer  customer_ask_question             —           —             मतलब
36  agent     agent_request_org_name            —           —             organization
37  agent     agent_ask_to_repeat               —           —             फिर से बता
38  customer  customer_provide_org_name         —           —             —
39  agent     agent_request_email               —           —             email
40  customer  customer_acknowledge              —           —             —
41  agent     agent_acknowledge                 —           —             —
42  customer  customer_ask_question             —           —             —
43  agent     agent_answer_query                —           —             —
44  customer  customer_provide_email            —           —             email
45  agent     agent_request_address             —           —             address
46  customer  customer_provide_org_name         frustrated  —             company name, नहीं हो रहा, नहीं हो
47  agent     agent_answer_query                —           —             —
48  customer  customer_report_done              —           —             —
49  agent     agent_request_address             —           —             —
50  customer  customer_report_done              —           —             हो गया
51  agent     agent_request_otp                 —           —             otp
52  agent     agent_request_otp                 —           —             otp
53  customer  customer_do_otp                   —           —             otp
54  agent     agent_wait                        —           —             —
55  agent     agent_wait                        —           —             —
56  customer  customer_acknowledge              —           —             —
57  agent     agent_acknowledge                 —           —             —
58  customer  customer_react_to_final_offer     —           —             —
59  agent     agent_clarify                     —           —             —
60  customer  customer_react_to_final_offer     —           —             —
61  agent     agent_present_final_offer         —           —             —
62  customer  customer_report_done              —           —             —
63  agent     agent_clarify                     —           —             —
64  customer  customer_request_wait             —           —             —
65  agent     agent_wait                        —           —             —
66  customer  customer_react_to_final_offer     —           —             —
67  agent     agent_present_final_offer         —           —             —
68  customer  customer_ask_question             —           —             —
69  agent     agent_present_final_offer         —           —             ₹378000, 378000
70  customer  customer_react_to_final_offer     —           —             —
71  agent     agent_present_final_offer         —           —             ₹378000, 378000
72  customer  customer_report_done              —           —             —
```

## Call 814513e5 (transferred) — 33 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   agent     agent_ask_to_repeat               —           —             फिर से कह
5   customer  customer_greet                    —           —             नमस्ते
6   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
7   customer  customer_agree                    —           —             —
8   agent     agent_greet                       —           —             —
9   customer  customer_agree                    —           —             —
10  customer  customer_report_done              —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms, link भेज
12  customer  customer_report_done              —           —             —
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
14  customer  customer_ask_question             —           —             —
15  agent     agent_guide_open_link             —           —             —
16  customer  customer_report_link_opened       —           —             खुल गया
17  agent     agent_guide_apply                 —           —             apply now
18  customer  customer_report_done              —           —             कर दिया
19  agent     agent_request_otp                 —           —             —
20  customer  customer_do_otp                   —           —             —
21  agent     agent_request_otp                 —           send_otp      otp
22  customer  customer_react_to_final_offer     —           —             —
23  agent     agent_other                       —           —             —
24  customer  customer_ask_question             —           —             —
25  agent     agent_acknowledge                 —           —             —
26  customer  customer_report_done              —           —             —
27  agent     agent_ask_employment_type         —           —             salaried, self-employ
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_present_final_offer         —           —             final offer
30  customer  customer_react_to_final_offer     —           —             —
31  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
32  customer  customer_acknowledge              —           —             —
```

## Call 88699263 (transferred) — 40 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             —
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_ask_to_repeat               —           —             फिर से कह
3   agent     agent_send_sms_link               —           send_sms      sms
4   agent     agent_guide_open_link             —           —             —
5   agent     agent_guide_apply                 —           —             apply now
6   customer  customer_acknowledge              —           —             —
7   agent     agent_request_otp                 —           send_otp      otp
8   customer  customer_acknowledge              —           —             —
9   agent     agent_request_otp                 —           send_otp      otp
10  agent     agent_request_otp                 —           —             otp
11  agent     agent_request_pan                 —           —             पैन
12  agent     agent_ask_to_repeat               —           —             फिर से कह
13  agent     agent_request_personal_details    —           —             gender, date of birth, marital
14  agent     agent_ask_to_repeat               —           —             —
15  agent     agent_ask_to_repeat               —           —             फिर से कह
16  agent     agent_ask_to_repeat               —           —             —
17  agent     agent_request_email               —           —             email
18  agent     agent_request_address             —           —             address, pincode, locality, building, house number
19  customer  customer_report_done              —           —             हो गया
20  agent     agent_request_terms_accept        —           —             terms and condition, terms
21  agent     agent_ask_employment_type         —           —             salaried, self-employ
22  agent     agent_ask_to_repeat               —           —             —
23  customer  customer_report_done              —           —             —
24  agent     agent_ask_employment_type         —           —             salaried, self-employ
25  agent     agent_ask_to_repeat               —           —             साफ़ बोल
26  agent     agent_request_income              —           —             income
27  agent     agent_ask_to_repeat               —           —             —
28  agent     agent_ask_to_repeat               —           —             —
29  agent     agent_request_org_name            —           —             organization
30  agent     agent_request_email               —           —             email
31  agent     agent_ask_to_repeat               —           —             —
32  agent     agent_request_address             —           —             address, pincode
33  agent     agent_ask_to_repeat               —           —             —
34  agent     agent_request_otp                 —           send_otp      otp
35  agent     agent_request_otp                 —           —             otp
36  agent     agent_ask_to_repeat               —           —             —
37  agent     agent_ask_to_repeat               —           —             —
38  agent     agent_present_final_offer         —           —             final offer
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 8e975c75 (transferred) — 28 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   agent     agent_ask_to_repeat               —           —             —
7   customer  customer_acknowledge              —           —             —
8   agent     agent_greet                       —           —             —
9   agent     agent_ask_to_repeat               —           —             —
10  customer  customer_greet                    —           —             hello
11  customer  customer_greet                    —           —             hello
12  agent     agent_send_sms_link               —           send_sms      sms
13  agent     agent_guide_open_link             —           —             —
14  agent     agent_guide_open_link             —           —             —
15  customer  customer_acknowledge              —           —             —
16  agent     agent_guide_apply                 —           —             apply now
17  customer  customer_do_otp                   —           —             otp
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_do_otp                   —           —             otp
20  agent     agent_wait                        —           —             wait
21  customer  customer_do_otp                   —           —             otp
22  agent     agent_request_otp                 —           —             otp
23  customer  customer_do_otp                   —           —             —
24  agent     agent_request_otp                 —           —             otp
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_present_final_offer         —           —             final offer
27  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 8ed64c9d (transferred) — 43 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते
4   customer  customer_greet                    —           —             hello
5   agent     agent_greet                       —           —             —
6   customer  customer_agree                    —           —             —
7   agent     agent_greet                       —           —             —
8   customer  customer_agree                    —           —             —
9   agent     agent_greet                       —           —             —
10  customer  customer_agree                    —           —             —
11  customer  customer_agree                    —           —             —
12  agent     agent_send_sms_link               —           send_sms      sms, लिंक भेज
13  customer  customer_report_sms_received      —           —             —
14  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
15  customer  customer_report_link_opened       —           —             खुल गया
16  agent     agent_guide_apply                 —           —             apply now
17  customer  customer_report_done              —           —             हो गया
18  agent     agent_request_otp                 —           —             —
19  customer  customer_report_done              —           —             —
20  agent     agent_request_otp                 —           send_otp      otp
21  customer  customer_greet                    —           —             hello
22  agent     agent_request_otp                 —           —             otp
23  agent     agent_ask_to_repeat               —           —             फिर से कह
24  customer  customer_request_wait             —           —             —
25  agent     agent_wait                        —           —             —
26  agent     agent_request_otp                 —           —             otp
27  customer  customer_do_otp                   —           —             —
28  agent     agent_ask_employment_type         —           —             salaried, self-employ
29  customer  customer_state_employment_type    —           —             self employ
30  agent     agent_request_income              —           —             —
31  agent     agent_ask_to_repeat               —           —             फिर से कह
32  agent     agent_request_income              —           —             income
33  customer  customer_acknowledge              —           —             —
34  agent     agent_request_org_name            —           —             —
35  customer  customer_acknowledge              —           —             —
36  agent     agent_request_org_name            —           —             —
37  customer  customer_report_done              —           —             कर दिया
38  agent     agent_request_business_details    —           —             —
39  customer  customer_report_done              —           —             कर दिया
40  agent     agent_guide_apply                 —           —             —
41  customer  customer_report_done              —           —             —
42  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 908e0eac (transferred) — 51 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   customer  customer_ask_query                —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_request_wait             —           —             —
9   agent     agent_wait                        —           —             —
10  customer  customer_report_link_opened       —           —             —
11  agent     agent_guide_apply                 —           —             apply now
12  customer  customer_report_done              —           —             कर दिया
13  agent     agent_request_otp                 —           send_otp      otp
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_do_otp                   —           —             —
17  agent     agent_request_pan                 —           —             पैन
18  agent     agent_wait                        —           —             —
19  customer  customer_provide_personal_details —           —             —
20  agent     agent_request_personal_details    —           —             gender, date of birth, marital
21  customer  customer_acknowledge              —           —             —
22  agent     agent_request_email               —           —             email
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_request_terms_accept        —           —             terms and condition, terms
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_ask_employment_type         —           —             salaried, self-employ
29  customer  customer_state_employment_type    —           —             salaried
30  agent     agent_request_income              —           —             income
31  agent     agent_ask_to_repeat               —           —             फिर से कह
32  customer  customer_request_wait             —           —             रुकिए
33  agent     agent_wait                        —           —             —
34  agent     agent_request_income              —           —             income
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_org_name            —           —             organization
37  customer  customer_report_done              —           —             हो गया
38  agent     agent_request_email               —           —             email
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_business_details    —           —             —
41  customer  customer_report_done              —           —             हो गया
42  agent     agent_guide_apply                 —           —             —
43  customer  customer_ask_query                —           —             —
44  agent     agent_answer_query                —           —             —
45  customer  customer_agree                    —           —             —
46  agent     agent_request_otp                 —           send_otp      otp
47  customer  customer_report_done              —           —             हो गया
48  agent     agent_present_final_offer         —           —             final offer
49  customer  customer_react_to_final_offer     —           —             final offer
50  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 92641b40 (transferred) — 81 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_present_offer               —           —             —
4   customer  customer_greet                    —           —             से बात
5   customer  customer_query_fee                —           —             interest rate
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_acknowledge              —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  agent     agent_ask_to_repeat               —           —             —
11  customer  customer_agree                    —           —             —
12  agent     agent_request_otp                 —           send_otp      otp
13  customer  customer_do_otp                   —           —             otp
14  agent     agent_request_otp                 —           send_otp      otp
15  customer  customer_do_otp                   —           —             otp
16  agent     agent_request_otp                 —           send_otp      otp
17  customer  customer_do_otp                   —           —             —
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_other                    —           —             —
20  agent     agent_answer_query                —           —             —
21  agent     agent_wait                        —           —             —
22  agent     agent_request_pan                 —           —             पैन
23  customer  customer_do_otp                   —           —             otp
24  agent     agent_request_otp                 —           —             otp
25  customer  customer_do_otp                   —           —             otp
26  agent     agent_wait                        —           —             wait
27  customer  customer_acknowledge              —           —             —
28  agent     agent_request_otp                 —           —             otp
29  customer  customer_ask_question             —           —             —
30  agent     agent_answer_query                —           —             —
31  customer  customer_acknowledge              —           —             —
32  agent     agent_request_pan                 —           —             पैन
33  customer  customer_acknowledge              —           —             —
34  agent     agent_request_pan                 —           —             पैन
35  customer  customer_provide_pan              —           —             —
36  agent     agent_request_pan                 —           —             पैन
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_pan                 —           —             पैन
39  customer  customer_acknowledge              —           —             —
40  agent     agent_request_personal_details    —           —             gender, date of birth, marital
41  customer  customer_report_done              —           —             —
42  agent     agent_request_pan                 —           —             पैन
43  agent     agent_request_personal_details    —           —             gender, date of birth, marital
44  customer  customer_ask_question             —           —             कौन सा
45  agent     agent_request_address             —           —             —
46  customer  customer_provide_address          —           —             आधार
47  agent     agent_request_address             —           —             address, आधार
48  customer  customer_acknowledge              —           —             —
49  agent     agent_request_address             —           —             address
50  agent     agent_request_address             —           —             address, pincode, locality, building, house number
51  agent     agent_ask_to_repeat               —           —             फिर से कह
52  customer  customer_provide_address          —           —             —
53  agent     agent_request_terms_accept        —           —             terms and condition, terms
54  customer  customer_ask_question             —           —             —
55  agent     agent_greet                       —           —             —
56  agent     agent_request_terms_accept        —           —             terms and condition, terms
57  customer  customer_provide_address          —           —             address
58  agent     agent_wait                        —           —             —
59  agent     agent_ask_employment_type         —           —             salaried, self-employ
60  agent     agent_ask_employment_type         —           —             salaried, self-employ
61  customer  customer_report_done              —           —             —
62  agent     agent_request_income              —           —             income
63  agent     agent_request_org_name            —           —             organization
64  agent     agent_request_email               —           —             email
65  customer  customer_acknowledge              —           —             —
66  agent     agent_request_business_details    —           —             —
67  customer  customer_provide_address          —           —             address
68  agent     agent_wait                        —           —             —
69  agent     agent_guide_apply                 —           —             —
70  customer  customer_report_done              —           —             हो गया
71  agent     agent_request_otp                 —           send_otp      otp
72  customer  customer_react_to_final_offer     —           —             —
73  agent     agent_present_final_offer         —           —             final offer
74  customer  customer_query_fee                —           —             processing fee
75  agent     agent_present_final_offer         —           —             final offer
76  agent     agent_present_final_offer         —           —             final offer
77  customer  customer_ask_question             —           —             —
78  agent     agent_present_final_offer         —           —             final offer
79  customer  customer_acknowledge              —           —             —
80  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 92ef6aa2 (transferred) — 72 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_query_fee                —           —             —
4   customer  customer_ask_question             confused    —             कैसे
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_guide_open_link             —           —             —
7   customer  customer_query_fee                —           —             —
8   agent     agent_explain_fee                 —           —             interest rate
9   customer  customer_ask_query                —           —             —
10  customer  customer_express_distrust         —           —             —
11  agent     agent_explain_fee                 —           —             interest rate
12  agent     agent_guide_open_link             —           —             —
13  customer  customer_report_link_opened       —           —             —
14  agent     agent_guide_open_link             —           —             —
15  customer  customer_report_link_opened       —           —             —
16  agent     agent_guide_apply                 —           —             apply now
17  customer  customer_ask_question             —           —             —
18  agent     agent_answer_query                —           —             —
19  customer  customer_query_fee                —           —             —
20  agent     agent_explain_fee                 —           —             interest rate
21  customer  customer_query_fee                —           —             —
22  agent     agent_explain_fee                 —           —             interest rate
23  customer  customer_ask_question             confused    —             कैसे
24  agent     agent_answer_query                —           —             —
25  customer  customer_agree                    —           —             —
26  agent     agent_confirm                     —           —             —
27  agent     agent_ask_to_repeat               —           —             फिर से कह
28  customer  customer_request_wait             —           —             —
29  agent     agent_wait                        —           —             —
30  customer  customer_express_distrust         —           —             —
31  agent     agent_reassure_trust              —           —             —
32  customer  customer_acknowledge              —           —             —
33  agent     agent_guide_apply                 —           —             —
34  customer  customer_other                    —           —             —
35  agent     agent_confirm                     —           —             —
36  customer  customer_ask_question             —           —             —
37  agent     agent_confirm                     —           —             —
38  agent     agent_end_call                    —           —             —
39  customer  customer_greet                    —           —             hello
40  agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
41  customer  customer_provide_email            —           —             email
42  agent     agent_request_email               —           —             email
43  customer  customer_ask_question             —           —             कौन सा
44  agent     agent_request_email               —           —             email
45  customer  customer_state_employment_type    —           —             self employ, self employee
46  agent     agent_ask_employment_type         —           —             salaried, self-employ
47  customer  customer_state_employment_type    —           —             —
48  agent     agent_request_income              —           —             income
49  customer  customer_provide_org_name         —           —             —
50  agent     agent_request_org_name            —           —             —
51  customer  customer_provide_org_name         —           —             —
52  agent     agent_request_org_name            —           —             —
53  customer  customer_acknowledge              —           —             —
54  agent     agent_request_business_details    —           —             business
55  customer  customer_acknowledge              —           —             —
56  agent     agent_request_business_details    —           —             business
57  customer  customer_acknowledge              —           —             —
58  agent     agent_request_udyam               —           —             udyam
59  agent     agent_offer_skip_udyam            —           —             —
60  customer  customer_respond_udyam            —           —             उद्यम
61  agent     agent_request_udyam               —           —             udyam, उद्यम
62  customer  customer_respond_udyam            —           —             —
63  agent     agent_offer_skip_udyam            —           —             skip
64  customer  customer_report_done              —           —             —
65  agent     agent_request_otp                 —           send_otp      otp
66  customer  customer_react_to_final_offer     —           —             —
67  customer  customer_react_to_final_offer     —           —             —
68  agent     agent_present_final_offer         —           —             final offer
69  customer  customer_ask_question             confused    —             कैसे
70  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
71  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 93a25fd6 (transferred) — 31 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_present_offer               —           —             pre-approved
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   customer  customer_report_link_opened       —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   agent     agent_guide_open_link             —           —             —
9   customer  customer_report_link_opened       —           —             —
10  agent     agent_guide_apply                 —           —             apply now
11  customer  customer_ask_question             —           —             —
12  agent     agent_guide_apply                 —           —             apply now
13  agent     agent_guide_apply                 —           —             apply now
14  customer  customer_acknowledge              —           —             —
15  agent     agent_request_otp                 —           —             —
16  customer  customer_do_otp                   —           —             —
17  agent     agent_request_otp                 —           send_otp      otp
18  agent     agent_request_otp                 —           send_otp      otp
19  agent     agent_request_personal_details    —           —             —
20  customer  customer_do_otp                   —           —             otp
21  agent     agent_wait                        —           —             wait
22  agent     agent_request_otp                 —           —             otp
23  customer  customer_do_otp                   —           —             —
24  agent     agent_wait                        —           —             —
25  agent     agent_wait                        —           —             —
26  customer  customer_do_otp                   —           —             otp
27  agent     agent_present_final_offer         —           —             final offer
28  customer  customer_react_to_final_offer     —           —             —
29  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
30  customer  customer_acknowledge              —           —             —
```

## Call 995adf61 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_send_sms_link               —           send_sms      sms
4   agent     agent_guide_open_link             —           —             —
5   customer  customer_report_sms_received      —           —             —
6   agent     agent_guide_apply                 —           —             apply now
7   customer  customer_report_done              —           —             हो गया
8   agent     agent_request_otp                 —           send_otp      otp
9   customer  customer_report_done              —           —             कर दिया
10  agent     agent_request_otp                 —           send_otp      otp
11  customer  customer_acknowledge              —           —             —
12  agent     agent_request_otp                 —           —             otp
13  customer  customer_report_done              —           —             —
14  agent     agent_request_personal_details    —           —             —
15  agent     agent_request_pan                 —           —             पैन
16  customer  customer_report_done              —           —             हो गया
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital
18  customer  customer_report_done              —           —             —
19  agent     agent_request_email               —           —             email
20  customer  customer_acknowledge              —           —             —
21  agent     agent_request_address             —           —             address, pincode, locality, building, house number
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_terms_accept        —           —             terms and condition, terms
24  agent     agent_ask_employment_type         —           —             salaried, self-employ
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_ask_employment_type         —           —             salaried, self-employ
27  customer  customer_state_employment_type    —           —             self employ
28  agent     agent_request_income              —           —             income
29  customer  customer_report_done              —           —             —
30  agent     agent_request_org_name            —           —             —
31  agent     agent_ask_to_repeat               —           —             फिर से कह
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_business_details    —           —             business
34  customer  customer_report_done              —           —             हो गया
35  agent     agent_request_udyam               —           —             udyam
36  customer  customer_respond_udyam            —           —             उद्यम
37  agent     agent_offer_skip_udyam            —           —             skip
38  agent     agent_request_otp                 —           send_otp      otp
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_otp                 —           —             otp
41  agent     agent_wait                        —           —             —
42  customer  customer_react_to_final_offer     —           —             —
43  agent     agent_present_final_offer         —           —             final offer
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call 9e9d4e8e (transferred) — 56 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   customer  customer_express_distrust         —           —             —
6   agent     agent_explain_fee                 —           —             interest rate
7   customer  customer_agree                    —           —             —
8   agent     agent_send_sms_link               —           send_sms      sms
9   agent     agent_guide_open_link             —           —             —
10  customer  customer_ask_question             —           —             —
11  agent     agent_guide_open_link             —           —             —
12  agent     agent_guide_apply                 —           —             apply now
13  agent     agent_ask_to_repeat               —           —             फिर से बता
14  customer  customer_report_done              —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_do_otp                   —           —             —
17  agent     agent_request_otp                 —           send_otp      otp
18  customer  customer_other                    —           —             —
19  agent     agent_request_pan                 —           —             पैन
20  customer  customer_do_otp                   —           —             otp
21  agent     agent_request_otp                 —           send_otp      otp
22  agent     agent_request_otp                 —           —             otp
23  agent     agent_ask_to_repeat               —           —             —
24  customer  customer_ask_question             —           —             —
25  agent     agent_request_otp                 —           send_otp      otp
26  customer  customer_other                    —           —             —
27  agent     agent_answer_query                —           —             —
28  customer  customer_request_wait             —           —             —
29  agent     agent_wait                        —           —             —
30  customer  customer_do_otp                   —           —             otp
31  agent     agent_wait                        —           —             —
32  customer  customer_do_otp                   —           —             —
33  agent     agent_request_otp                 —           —             otp
34  customer  customer_provide_pan              —           —             pan
35  agent     agent_present_final_offer         —           —             final offer
36  customer  customer_react_to_final_offer     —           —             —
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
38  customer  customer_acknowledge              —           —             —
39  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
41  customer  customer_acknowledge              —           —             —
42  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
43  customer  customer_agree                    —           —             —
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
45  customer  customer_acknowledge              —           —             —
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
47  customer  customer_acknowledge              —           —             —
48  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
49  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
50  customer  customer_acknowledge              —           —             —
51  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
52  customer  customer_acknowledge              —           —             —
53  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
54  customer  customer_other                    —           —             —
55  agent     agent_reassure_trust              —           —             —
```

## Call 9fe046b5 (transferred) — 50 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_other                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   customer  customer_query_fee                —           —             —
6   agent     agent_explain_fee                 —           —             interest rate
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_report_done              —           —             —
9   agent     agent_guide_open_link             —           —             —
10  agent     agent_request_otp                 —           send_otp      otp
11  customer  customer_ask_question             —           —             —
12  agent     agent_present_offer               —           —             pre-approved
13  customer  customer_provide_pan              —           —             —
14  agent     agent_request_pan                 —           —             पैन
15  customer  customer_request_wait             —           —             wait
16  agent     agent_wait                        —           —             —
17  agent     agent_ask_to_repeat               —           —             फिर से कह
18  customer  customer_report_done              —           —             हो गया, भर दिया
19  customer  customer_request_wait             —           —             रुकिए, wait
20  agent     agent_wait                        —           —             —
21  customer  customer_agree                    —           —             —
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_email               —           —             email
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_request_address             —           —             address, pincode, locality, building, house number
27  agent     agent_request_terms_accept        —           —             terms and condition, terms
28  customer  customer_request_wait             —           —             —
29  agent     agent_wait                        —           —             —
30  customer  customer_ask_question             —           —             —
31  agent     agent_request_address             —           —             address, pincode, locality, building, house number
32  customer  customer_acknowledge              —           —             —
33  agent     agent_ask_employment_type         —           —             salaried, self-employ
34  customer  customer_report_done              —           —             —
35  agent     agent_ask_employment_type         —           —             salaried, self-employ
36  customer  customer_ask_question             —           —             —
37  agent     agent_answer_query                —           —             —
38  agent     agent_request_org_name            —           —             organization
39  customer  customer_report_done              —           —             हो गया
40  agent     agent_request_email               —           —             email
41  customer  customer_report_done              —           —             हो गया
42  agent     agent_request_business_details    —           —             —
43  customer  customer_report_done              —           —             हो गया
44  agent     agent_request_otp                 —           send_otp      otp
45  customer  customer_other                    —           —             —
46  agent     agent_wait                        —           —             wait
47  agent     agent_request_otp                 —           send_otp      otp
48  customer  customer_query_fee                —           —             emi
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call a051b745 (transferred) — 79 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             शुरू कर
5   agent     agent_send_sms_link               —           —             sms
6   customer  customer_acknowledge              —           —             —
7   customer  customer_greet                    —           —             hello
8   agent     agent_guide_open_link             —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  agent     agent_guide_apply                 —           —             apply now
11  agent     agent_ask_to_repeat               —           —             फिर से कह
12  agent     agent_guide_open_link             —           —             —
13  customer  customer_report_done              —           —             हो गया
14  agent     agent_guide_apply                 —           —             apply now
15  customer  customer_report_done              —           —             कर दिया
16  agent     agent_request_otp                 —           send_otp      otp
17  agent     agent_request_otp                 —           send_otp      otp
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_otp                 —           send_otp      otp
20  agent     agent_request_otp                 —           —             otp
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_pan                 —           —             पैन
23  customer  customer_ask_question             —           —             —
24  agent     agent_request_pan                 —           —             पैन
25  customer  customer_provide_pan              —           —             —
26  agent     agent_request_pan                 —           —             पैन
27  customer  customer_ask_question             —           —             —
28  agent     agent_answer_query                —           —             —
29  customer  customer_agree                    —           —             —
30  agent     agent_request_personal_details    —           —             gender, date of birth, marital
31  agent     agent_request_personal_details    —           —             gender, date of birth, marital
32  customer  customer_acknowledge              —           —             —
33  agent     agent_request_email               —           —             email
34  customer  customer_acknowledge              —           —             —
35  agent     agent_request_email               —           —             email
36  agent     agent_request_address             —           —             address, pincode, locality, building, house number
37  customer  customer_request_wait             —           —             —
38  agent     agent_wait                        —           —             —
39  agent     agent_request_address             —           —             address, pincode, locality, building, house number
40  customer  customer_request_wait             —           —             —
41  agent     agent_wait                        —           —             —
42  customer  customer_acknowledge              —           —             —
43  agent     agent_request_address             —           —             address, pincode, locality, building, house number
44  customer  customer_acknowledge              —           —             —
45  agent     agent_request_terms_accept        —           —             terms and condition, terms
46  customer  customer_accept_terms             —           —             —
47  agent     agent_request_terms_accept        —           —             terms and condition, terms
48  customer  customer_ask_question             —           —             —
49  agent     agent_answer_query                —           —             —
50  customer  customer_report_done              —           —             हो गया
51  agent     agent_request_org_name            —           —             organization
52  customer  customer_acknowledge              —           —             —
53  agent     agent_request_org_name            —           —             organization
54  customer  customer_acknowledge              —           —             —
55  agent     agent_inform_manual_review        —           push_to_crm   —
56  customer  customer_react_to_final_offer     —           —             —
57  customer  customer_react_to_final_offer     —           —             —
58  agent     agent_present_final_offer         —           —             —
59  agent     agent_present_final_offer         —           —             —
60  customer  customer_ask_question             —           —             —
61  agent     agent_answer_query                —           —             —
62  customer  customer_ask_question             —           —             —
63  agent     agent_answer_query                —           —             —
64  agent     agent_answer_query                —           —             —
65  customer  customer_acknowledge              —           —             —
66  agent     agent_end_call                    —           —             —
67  customer  customer_acknowledge              —           —             —
68  agent     agent_present_final_offer         —           —             final offer
69  customer  customer_report_done              —           —             —
70  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
71  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
72  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
73  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
74  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
75  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
76  customer  customer_acknowledge              —           —             —
77  agent     agent_end_call                    —           —             goodbye
78  customer  customer_other                    confused    —             कैसे
```

## Call a1b72c5c (transferred) — 48 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             —
1   customer  customer_greet                    —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
3   customer  customer_agree                    —           —             —
4   agent     agent_greet                       —           —             —
5   customer  customer_agree                    —           —             —
6   customer  customer_agree                    —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   agent     agent_send_sms_link               —           —             sms
9   agent     agent_guide_open_link             —           —             —
10  customer  customer_report_link_opened       —           —             —
11  agent     agent_guide_open_link             —           —             —
12  customer  customer_report_done              —           —             —
13  agent     agent_guide_apply                 —           —             apply now
14  agent     agent_ask_to_repeat               —           —             —
15  customer  customer_report_done              —           —             कर दिया
16  agent     agent_request_otp                 —           send_otp      otp
17  agent     agent_ask_to_repeat               —           —             फिर से कह
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_pan                 —           —             पैन
20  customer  customer_provide_pan              —           —             —
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_email               —           —             email
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_request_address             —           —             address, pincode, locality, building, house number
26  agent     agent_request_terms_accept        —           —             terms and condition, terms
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_ask_employment_type         —           —             salaried, self-employ
29  customer  customer_state_employment_type    —           —             —
30  agent     agent_ask_employment_type         —           —             salaried, self-employ
31  customer  customer_state_employment_type    —           —             self employ
32  agent     agent_request_income              —           —             income
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_business_details    —           —             business
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_business_details    —           —             business
37  agent     agent_ask_to_repeat               —           —             —
38  customer  customer_report_done              —           —             हो गया
39  agent     agent_request_udyam               —           —             udyam
40  customer  customer_skip_udyam               —           —             skip
41  agent     agent_offer_skip_udyam            —           —             skip
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_request_otp                 —           send_otp      otp
44  customer  customer_report_done              —           —             हो गया
45  agent     agent_wait                        —           —             —
46  customer  customer_react_to_final_offer     —           —             —
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call a2ff0814 (transferred) — 51 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_send_sms_link               —           send_sms      sms
7   customer  customer_acknowledge              —           —             —
8   agent     agent_send_sms_link               —           —             sms
9   customer  customer_acknowledge              —           —             —
10  agent     agent_guide_open_link             —           —             लिंक पर क्लिक
11  customer  customer_report_applied           —           —             —
12  agent     agent_guide_open_link             —           —             लिंक पर क्लिक
13  customer  customer_agree                    —           —             —
14  agent     agent_guide_apply                 —           —             apply now
15  customer  customer_report_done              —           —             —
16  agent     agent_guide_apply                 —           —             apply now
17  customer  customer_agree                    —           —             —
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_do_otp                   frustrated  —             otp, बार बार
20  agent     agent_acknowledge                 —           —             —
21  customer  customer_do_otp                   —           —             otp
22  agent     agent_acknowledge                 —           —             —
23  customer  customer_ask_question             —           —             —
24  agent     agent_wait                        —           —             —
25  customer  customer_other                    —           —             —
26  agent     agent_greet                       —           —             —
27  customer  customer_ask_question             —           —             —
28  agent     agent_answer_query                —           —             —
29  customer  customer_ask_question             —           —             —
30  agent     agent_clarify                     —           —             —
31  customer  customer_ask_question             —           —             —
32  agent     agent_answer_query                —           —             —
33  customer  customer_agree                    —           —             —
34  agent     agent_request_personal_details    —           —             —
35  customer  customer_react_to_final_offer     —           —             —
36  agent     agent_present_final_offer         —           —             —
37  customer  customer_query_fee                —           —             emi
38  agent     agent_answer_query                —           —             —
39  customer  customer_query_fee                —           —             —
40  agent     agent_answer_query                —           —             —
41  customer  customer_acknowledge              —           —             —
42  agent     agent_confirm                     —           —             आगे बढ़
43  customer  customer_react_to_final_offer     —           —             —
44  customer  customer_query_fee                —           —             —
45  customer  customer_query_fee                —           —             —
46  agent     agent_answer_query                —           —             —
47  customer  customer_ask_question             —           —             —
48  agent     agent_answer_query                —           —             —
49  customer  customer_agree                    —           —             —
50  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call a638362d (transferred) — 57 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             —
3   customer  customer_query_fee                —           —             —
4   agent     agent_answer_query                —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_send_sms_link               —           —             sms
7   customer  customer_report_sms_received      —           —             —
8   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
9   customer  customer_report_link_opened       —           —             —
10  agent     agent_guide_apply                 —           —             apply now
11  customer  customer_do_otp                   —           —             —
12  agent     agent_request_otp                 —           —             —
13  agent     agent_request_otp                 —           send_otp      otp
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_clarify                     —           —             —
16  customer  customer_provide_pan              —           —             pan
17  agent     agent_request_pan                 —           —             पैन
18  agent     agent_request_pan                 —           —             पैन
19  customer  customer_ask_question             —           —             —
20  agent     agent_request_personal_details    —           —             gender, date of birth, marital
21  customer  customer_report_address_error     —           —             —
22  agent     agent_help_address_error          —           —             —
23  customer  customer_report_address_error     —           —             —
24  agent     agent_help_address_error          —           —             —
25  customer  customer_report_address_error     —           —             —
26  agent     agent_help_address_error          —           —             —
27  customer  customer_acknowledge              —           —             —
28  agent     agent_request_terms_accept        —           —             terms and condition, terms
29  customer  customer_state_employment_type    —           —             —
30  agent     agent_ask_employment_type         —           —             —
31  customer  customer_state_employment_type    —           —             —
32  agent     agent_acknowledge                 —           —             —
33  agent     agent_request_income              —           —             income
34  agent     agent_request_income              —           —             income
35  customer  customer_provide_business_details —           —             —
36  agent     agent_request_business_details    —           —             business
37  customer  customer_provide_business_details —           —             —
38  agent     agent_request_business_details    —           —             business
39  customer  customer_report_done              —           —             —
40  agent     agent_request_business_details    —           —             —
41  customer  customer_agree                    —           —             —
42  agent     agent_acknowledge                 —           —             —
43  customer  customer_respond_udyam            —           —             उद्यम
44  agent     agent_request_udyam               —           —             उद्यम
45  agent     agent_offer_skip_udyam            —           —             skip
46  customer  customer_report_done              —           —             —
47  agent     agent_clarify                     —           —             कौन सा
48  customer  customer_skip_udyam               —           —             skip
49  agent     agent_offer_skip_udyam            —           —             skip
50  customer  customer_report_done              —           —             कर दिया
51  agent     agent_request_terms_accept        —           —             —
52  customer  customer_react_to_final_offer     —           —             —
53  agent     agent_present_final_offer         —           —             final offer
54  customer  customer_react_to_final_offer     —           —             —
55  agent     agent_transfer_to_rm              —           transfer_to_rm—
56  customer  customer_other                    —           —             —
```

## Call a78e74de (transferred) — 47 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             —
6   customer  customer_agree                    —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   agent     agent_send_sms_link               —           send_sms      sms
9   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
10  customer  customer_report_link_opened       —           —             खुल गया
11  agent     agent_guide_apply                 —           —             apply now
12  customer  customer_report_done              —           —             कर दिया
13  agent     agent_request_otp                 —           —             —
14  customer  customer_report_done              —           —             कर दिया
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_do_otp                   —           —             —
17  agent     agent_request_personal_details    —           —             —
18  customer  customer_provide_pan              —           —             pan
19  agent     agent_request_pan                 —           —             पैन
20  customer  customer_provide_pan              —           —             —
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital
23  customer  customer_provide_address          —           —             address
24  agent     agent_request_address             —           —             address, locality
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_request_terms_accept        —           —             terms and condition, terms
27  customer  customer_report_done              —           —             कर दिया
28  agent     agent_ask_employment_type         —           —             salaried, self-employ
29  customer  customer_state_employment_type    —           —             self employ
30  agent     agent_request_income              —           —             income
31  customer  customer_report_done              —           —             कर दिया
32  agent     agent_request_udyam               —           —             udyam
33  customer  customer_respond_udyam            —           —             उद्यम
34  agent     agent_request_udyam               —           —             udyam
35  customer  customer_respond_udyam            —           —             —
36  agent     agent_request_udyam               —           —             udyam
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_otp                 —           —             otp
39  customer  customer_do_otp                   —           —             —
40  agent     agent_wait                        —           —             —
41  customer  customer_acknowledge              —           —             —
42  agent     agent_wait                        —           —             —
43  customer  customer_other                    —           —             —
44  agent     agent_wait                        —           —             —
45  customer  customer_react_to_final_offer     —           —             —
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call a880a397 (transferred) — 48 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             —
1   customer  customer_report_link_opened       —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_guide_apply                 —           —             apply now
4   customer  customer_provide_address          —           —             —
5   agent     agent_request_otp                 —           send_otp      otp
6   customer  customer_report_done              —           —             कर दिया
7   agent     agent_request_otp                 —           send_otp      otp
8   customer  customer_report_done              —           —             —
9   agent     agent_request_otp                 —           —             otp
10  agent     agent_request_pan                 —           —             पैन
11  customer  customer_provide_pan              —           —             —
12  agent     agent_request_personal_details    —           —             gender, date of birth, marital
13  customer  customer_report_done              —           —             —
14  agent     agent_request_personal_details    —           —             —
15  customer  customer_report_done              —           —             —
16  agent     agent_request_email               —           —             email
17  customer  customer_report_done              —           —             हो गया
18  agent     agent_request_address             —           —             address, pincode, locality, building, house number
19  agent     agent_request_address             —           —             address
20  agent     agent_request_terms_accept        —           —             terms and condition, terms
21  customer  customer_ask_question             —           —             —
22  agent     agent_request_terms_accept        —           —             terms and condition, terms
23  customer  customer_report_done              —           —             कर दिया
24  agent     agent_ask_employment_type         —           —             salaried, self-employ
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_ask_employment_type         —           —             salaried, self-employ
27  agent     agent_ask_to_repeat               —           —             फिर से कह
28  customer  customer_state_employment_type    —           —             —
29  agent     agent_request_income              —           —             income
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_request_org_name            —           —             organization
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_email               —           —             email
34  customer  customer_ask_question             —           —             —
35  agent     agent_answer_query                —           —             —
36  customer  customer_report_done              —           —             कर दिया
37  agent     agent_request_business_details    —           —             —
38  customer  customer_report_done              —           —             —
39  agent     agent_request_business_details    —           —             —
40  customer  customer_report_done              —           —             —
41  agent     agent_guide_apply                 —           —             —
42  agent     agent_request_otp                 —           send_otp      otp
43  customer  customer_report_done              —           —             कर दिया
44  agent     agent_present_final_offer         —           —             final offer
45  customer  customer_react_to_final_offer     —           —             —
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call b07fcd2f (transferred) — 80 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_send_sms_link               —           send_sms      sms
4   agent     agent_guide_open_link             —           —             —
5   agent     agent_guide_apply                 —           —             apply now
6   customer  customer_do_otp                   —           —             —
7   agent     agent_request_otp                 —           send_otp      otp
8   agent     agent_end_call                    —           —             —
9   customer  customer_other                    —           —             —
10  agent     agent_request_otp                 —           send_otp      otp
11  agent     agent_request_otp                 —           send_otp      otp
12  agent     agent_request_otp                 —           —             otp
13  customer  customer_report_done              —           —             —
14  agent     agent_request_pan                 —           —             पैन
15  customer  customer_request_wait             —           —             wait
16  agent     agent_wait                        —           —             —
17  customer  customer_provide_pan              —           —             pan
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital
19  customer  customer_ask_question             —           —             —
20  agent     agent_request_personal_details    —           —             —
21  customer  customer_acknowledge              —           —             —
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital
23  customer  customer_do_otp                   —           —             otp
24  agent     agent_request_otp                 —           send_otp      otp
25  customer  customer_request_wait             —           —             wait
26  agent     agent_request_otp                 —           —             otp
27  customer  customer_do_otp                   —           —             otp
28  agent     agent_wait                        —           —             —
29  agent     agent_request_email               —           —             email
30  customer  customer_provide_pan              —           —             pan
31  agent     agent_request_email               —           —             email
32  customer  customer_provide_pan              —           —             pan
33  agent     agent_request_pan                 —           —             पैन
34  customer  customer_report_done              —           —             हो गया
35  agent     agent_request_personal_details    —           —             gender, date of birth, marital
36  agent     agent_request_email               —           —             email
37  customer  customer_provide_personal_details —           —             marital
38  customer  customer_provide_email            —           —             email
39  agent     agent_request_email               —           —             email
40  customer  customer_report_done              —           —             —
41  agent     agent_request_address             —           —             address, pincode, locality, building, house number
42  customer  customer_request_wait             —           —             —
43  agent     agent_request_email               —           —             email
44  customer  customer_provide_address          —           —             address
45  agent     agent_request_address             —           —             address, pincode, locality, building, house number
46  agent     agent_request_terms_accept        —           —             terms and condition, terms
47  customer  customer_report_done              —           —             कर दिया
48  agent     agent_ask_employment_type         —           —             salaried, self-employ
49  customer  customer_report_done              —           —             —
50  agent     agent_ask_employment_type         —           —             salaried, self-employ
51  customer  customer_acknowledge              —           —             —
52  customer  customer_ask_question             —           —             —
53  agent     agent_ask_employment_type         —           —             salaried, self-employ
54  customer  customer_ask_question             —           —             —
55  customer  customer_report_address_error     —           —             —
56  agent     agent_help_address_error          —           —             red, error
57  customer  customer_report_done              —           —             कर दिया
58  agent     agent_request_org_name            —           —             organization
59  agent     agent_request_org_name            —           —             organization
60  customer  customer_ask_question             —           —             —
61  agent     agent_answer_query                —           —             —
62  customer  customer_ask_question             —           —             मतलब
63  agent     agent_answer_query                —           —             —
64  customer  customer_provide_org_name         —           —             organization
65  agent     agent_answer_query                —           —             —
66  customer  customer_request_wait             —           —             रुकिए
67  agent     agent_wait                        —           —             —
68  agent     agent_request_email               —           —             email
69  agent     agent_request_email               —           —             email
70  agent     agent_request_email               —           —             email
71  agent     agent_request_business_details    —           —             —
72  customer  customer_ask_question             —           —             —
73  agent     agent_answer_query                —           —             —
74  customer  customer_skip_udyam               —           —             —
75  agent     agent_offer_skip_udyam            —           —             skip
76  agent     agent_request_otp                 —           send_otp      otp
77  agent     agent_request_otp                 —           —             otp
78  customer  customer_react_to_final_offer     —           —             —
79  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call b10463b7 (transferred) — 54 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             —
1   customer  customer_acknowledge              —           —             —
2   agent     agent_ask_to_repeat               —           —             —
3   customer  customer_greet                    —           —             hello
4   agent     agent_greet                       —           —             hello
5   customer  customer_greet                    —           —             —
6   agent     agent_greet                       —           —             —
7   customer  customer_ask_question             —           —             —
8   agent     agent_present_offer               —           —             pre-approved, loan offer
9   customer  customer_ask_question             —           —             —
10  agent     agent_disclose_recording          —           —             record, training, quality
11  customer  customer_agree                    —           —             —
12  agent     agent_present_offer               —           —             pre-approved, loan offer
13  customer  customer_agree                    —           —             —
14  agent     agent_send_sms_link               —           send_sms      sms
15  customer  customer_express_distrust         distrustful —             fraud, fake
16  agent     agent_reassure_trust              —           —             —
17  customer  customer_report_link_opened       —           —             —
18  agent     agent_guide_apply                 —           —             apply now
19  agent     agent_request_otp                 —           send_otp      otp
20  customer  customer_report_done              —           —             कर दिया
21  agent     agent_request_otp                 —           send_otp      otp
22  agent     agent_request_otp                 —           —             otp
23  customer  customer_do_otp                   —           —             —
24  agent     agent_request_pan                 —           —             पैन
25  customer  customer_report_done              —           —             —
26  agent     agent_request_personal_details    —           —             gender, date of birth, marital
27  customer  customer_report_done              —           —             —
28  agent     agent_request_email               —           —             email
29  customer  customer_report_done              —           —             —
30  agent     agent_request_address             —           —             address, pincode, locality, building, house number
31  customer  customer_report_done              —           —             कर दिया
32  agent     agent_request_terms_accept        —           —             terms and condition, terms
33  customer  customer_report_done              —           —             कर लिया
34  agent     agent_ask_employment_type         —           —             salaried, self-employ
35  customer  customer_report_done              —           —             कर दिया
36  agent     agent_ask_employment_type         —           —             salaried, self-employ
37  agent     agent_ask_employment_type         —           —             salaried, self-employ
38  customer  customer_state_employment_type    —           —             salaried
39  agent     agent_request_income              —           —             income
40  customer  customer_report_done              —           —             कर दिया
41  agent     agent_request_org_name            —           —             organization
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_request_email               —           —             email
44  customer  customer_report_done              —           —             हो गया, कर दिया
45  agent     agent_request_business_details    —           —             —
46  customer  customer_report_done              —           —             कर दिया
47  agent     agent_guide_apply                 —           —             —
48  customer  customer_report_done              —           —             कर दिया
49  agent     agent_request_otp                 —           send_otp      otp
50  customer  customer_report_done              —           —             —
51  agent     agent_present_final_offer         —           —             final offer
52  customer  customer_react_to_final_offer     —           —             —
53  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
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
5   agent     agent_greet                       —           —             —
6   customer  customer_ask_question             —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   customer  customer_acknowledge              —           —             —
9   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
10  customer  customer_express_distrust         —           —             —
11  agent     agent_reassure_trust              —           —             —
12  agent     agent_guide_apply                 —           —             apply now
13  customer  customer_do_otp                   —           —             —
14  agent     agent_request_otp                 —           send_otp      otp
15  customer  customer_report_done              —           —             —
16  agent     agent_request_pan                 —           —             पैन
17  customer  customer_query_fee                —           —             processing fee
18  agent     agent_explain_fee                 —           —             processing fee, interest rate
19  agent     agent_request_pan                 —           —             पैन
20  agent     agent_end_call                    —           —             —
21  agent     agent_request_pan                 —           —             पैन
22  customer  customer_request_wait             —           —             —
23  agent     agent_wait                        —           —             —
24  agent     agent_request_pan                 —           —             पैन
25  agent     agent_request_pan                 —           —             पैन
26  customer  customer_report_address_error     —           —             —
27  agent     agent_help_address_error          —           —             —
28  customer  customer_report_address_error     —           —             —
29  agent     agent_acknowledge                 —           —             —
30  customer  customer_request_wait             —           —             —
31  agent     agent_wait                        —           —             —
32  agent     agent_help_address_error          —           —             —
33  customer  customer_report_address_error     —           —             —
34  agent     agent_help_address_error          —           —             —
35  customer  customer_ask_question             —           —             —
36  agent     agent_answer_query                —           —             —
37  customer  customer_acknowledge              —           —             —
38  agent     agent_help_address_error          —           —             —
39  customer  customer_provide_address          —           —             —
40  agent     agent_acknowledge                 —           —             —
41  customer  customer_report_done              —           —             —
42  customer  customer_provide_email            —           —             email
43  agent     agent_request_email               —           —             email
44  agent     agent_request_address             —           —             address, pincode
45  customer  customer_acknowledge              —           —             —
46  agent     agent_request_address             —           —             address, pincode
47  customer  customer_ask_question             —           —             —
48  agent     agent_answer_query                —           —             —
49  customer  customer_ask_question             —           —             —
50  agent     agent_answer_query                —           —             —
51  customer  customer_query_fee                —           —             charges
52  agent     agent_explain_fee                 —           —             charges
53  customer  customer_request_wait             —           —             wait
54  agent     agent_wait                        —           —             —
55  customer  customer_acknowledge              —           —             —
56  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call bb88ae27 (transferred) — 53 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_present_offer               —           —             pre-approved, loan offer
4   customer  customer_greet                    —           —             hello
5   agent     agent_present_offer               —           —             —
6   customer  customer_agree                    —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   agent     agent_guide_open_link             —           —             —
9   customer  customer_query_fee                —           —             —
10  agent     agent_explain_fee                 —           —             interest rate
11  customer  customer_agree                    —           —             —
12  agent     agent_guide_apply                 —           —             apply now
13  customer  customer_report_done              —           —             कर दिया
14  agent     agent_request_otp                 —           send_otp      otp
15  customer  customer_acknowledge              —           —             —
16  agent     agent_request_otp                 —           send_otp      otp
17  customer  customer_react_to_offer           —           —             —
18  agent     agent_request_personal_details    —           —             —
19  agent     agent_request_pan                 —           —             पैन
20  agent     agent_request_personal_details    —           —             gender, date of birth, marital
21  customer  customer_report_done              —           —             —
22  agent     agent_request_email               —           —             email
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  customer  customer_report_done              —           —             हो गया
26  agent     agent_request_terms_accept        —           —             terms and condition, terms
27  customer  customer_report_done              —           —             —
28  agent     agent_ask_employment_type         —           —             salaried, self-employ
29  customer  customer_report_done              —           —             —
30  agent     agent_ask_employment_type         —           —             salaried, self-employ
31  customer  customer_report_done              —           —             —
32  agent     agent_ask_employment_type         —           —             salaried, self-employ
33  agent     agent_ask_to_repeat               —           —             फिर से कह
34  customer  customer_state_employment_type    —           —             —
35  agent     agent_request_income              —           —             income
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_request_org_name            —           —             organization
38  customer  customer_report_done              —           —             हो गया
39  agent     agent_request_email               —           —             email
40  customer  customer_report_done              —           —             हो गया
41  agent     agent_request_address             —           —             address, pincode
42  customer  customer_report_done              —           —             हो गया
43  agent     agent_guide_apply                 —           —             —
44  agent     agent_ask_to_repeat               —           —             —
45  customer  customer_report_done              —           —             हो गया
46  agent     agent_request_otp                 —           send_otp      otp
47  customer  customer_ask_question             —           —             —
48  agent     agent_request_otp                 —           —             otp
49  customer  customer_report_done              —           —             हो गया
50  agent     agent_present_final_offer         —           —             final offer
51  customer  customer_react_to_final_offer     —           —             —
52  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call c3a47f19 (transferred) — 44 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_ask_query                —           —             —
5   agent     agent_acknowledge                 —           —             —
6   customer  customer_ask_query                —           —             —
7   customer  customer_ask_query                —           —             —
8   agent     agent_send_sms_link               —           send_sms      sms
9   agent     agent_send_sms_link               —           send_sms      sms
10  agent     agent_guide_open_link             —           —             —
11  agent     agent_guide_apply                 —           —             apply now
12  agent     agent_request_otp                 —           send_otp      otp
13  agent     agent_request_otp                 —           send_otp      otp
14  agent     agent_request_personal_details    —           —             —
15  agent     agent_request_pan                 —           —             पैन
16  agent     agent_ask_to_repeat               —           —             —
17  agent     agent_request_personal_details    —           —             gender, date of birth, marital
18  agent     agent_ask_to_repeat               —           —             —
19  agent     agent_request_email               —           —             email
20  agent     agent_request_address             —           —             address, pincode, locality, building, house number
21  agent     agent_ask_to_repeat               —           —             —
22  agent     agent_request_terms_accept        —           —             terms and condition, terms
23  agent     agent_ask_to_repeat               —           —             —
24  agent     agent_ask_employment_type         —           —             salaried, self-employ
25  agent     agent_ask_to_repeat               —           —             —
26  agent     agent_ask_employment_type         —           —             salaried, self-employ
27  agent     agent_ask_to_repeat               —           —             —
28  agent     agent_request_income              —           —             income
29  agent     agent_ask_to_repeat               —           —             —
30  agent     agent_request_org_name            —           —             organization
31  agent     agent_request_email               —           —             email
32  agent     agent_ask_to_repeat               —           —             —
33  agent     agent_request_address             —           —             address, pincode
34  agent     agent_ask_to_repeat               —           —             —
35  agent     agent_guide_apply                 —           —             —
36  agent     agent_request_otp                 —           send_otp      otp
37  agent     agent_request_otp                 —           send_otp      otp
38  agent     agent_present_final_offer         —           —             final offer
39  agent     agent_ask_to_repeat               —           —             —
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
41  agent     agent_ask_to_repeat               —           —             —
42  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
43  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call c44d3103 (transferred) — 20 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             —
3   agent     agent_send_sms_link               —           send_sms      sms
4   agent     agent_send_sms_link               —           —             sms
5   customer  customer_report_sms_received      —           —             —
6   agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
7   agent     agent_guide_open_link             —           —             खुल गया
8   agent     agent_ask_to_repeat               —           —             फिर से कह
9   customer  customer_report_link_opened       —           —             खुल गया
10  agent     agent_guide_apply                 —           —             apply now
11  customer  customer_report_applied           —           —             —
12  agent     agent_request_otp                 —           —             —
13  agent     agent_request_otp                 —           send_otp      otp
14  customer  customer_do_otp                   —           —             otp
15  agent     agent_clarify                     —           —             —
16  customer  customer_other                    —           —             —
17  agent     agent_wait                        —           —             —
18  customer  customer_react_to_final_offer     —           —             —
19  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call c4d807c2 (transferred) — 62 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   customer  customer_agree                    —           —             —
4   customer  customer_query_fee                —           —             —
5   agent     agent_explain_fee                 —           —             interest rate
6   agent     agent_ask_to_repeat               —           —             —
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_report_sms_received      —           —             sms
9   agent     agent_send_sms_link               —           send_sms      sms
10  customer  customer_report_sms_received      —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms
12  customer  customer_query_fee                —           —             processing fee, interest rate
13  agent     agent_explain_fee                 —           —             processing fee, interest rate
14  agent     agent_ask_to_repeat               —           —             —
15  agent     agent_guide_open_link             —           —             —
16  agent     agent_ask_to_repeat               —           —             —
17  customer  customer_report_link_opened       —           —             —
18  agent     agent_guide_apply                 —           —             apply now
19  customer  customer_request_wait             —           —             —
20  agent     agent_wait                        —           —             —
21  customer  customer_report_applied           —           —             —
22  agent     agent_guide_apply                 —           —             —
23  customer  customer_report_applied           —           —             apply now
24  agent     agent_guide_apply                 —           —             apply now
25  customer  customer_do_otp                   —           —             —
26  agent     agent_request_otp                 —           send_otp      otp
27  customer  customer_request_wait             —           —             —
28  agent     agent_request_otp                 —           send_otp      otp
29  customer  customer_do_otp                   —           —             otp
30  agent     agent_request_otp                 —           —             otp
31  agent     agent_ask_to_repeat               —           —             —
32  customer  customer_do_otp                   —           —             otp
33  agent     agent_request_otp                 —           —             otp
34  customer  customer_request_wait             —           —             —
35  agent     agent_wait                        —           —             —
36  customer  customer_request_wait             —           —             —
37  agent     agent_wait                        —           —             —
38  customer  customer_do_otp                   —           —             otp
39  agent     agent_request_otp                 —           —             otp
40  customer  customer_do_otp                   —           —             otp
41  agent     agent_wait                        —           —             wait
42  customer  customer_acknowledge              —           —             —
43  agent     agent_request_otp                 —           —             otp
44  customer  customer_request_wait             —           —             —
45  agent     agent_request_otp                 —           —             otp
46  customer  customer_request_wait             —           —             —
47  agent     agent_request_otp                 —           —             otp
48  customer  customer_do_otp                   —           —             —
49  agent     agent_request_otp                 —           —             otp
50  agent     agent_ask_to_repeat               —           —             —
51  customer  customer_report_done              —           —             हो गया
52  agent     agent_present_final_offer         —           —             final offer
53  customer  customer_provide_pan              —           —             pan
54  agent     agent_present_final_offer         —           —             final offer
55  customer  customer_provide_pan              —           —             pan
56  agent     agent_present_final_offer         —           —             final offer
57  customer  customer_react_to_final_offer     —           —             —
58  agent     agent_present_final_offer         —           —             final offer
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
60  customer  customer_query_fee                —           —             —
61  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call c6a8b74f (transferred) — 35 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_greet                    —           —             hello
5   agent     agent_greet                       —           —             —
6   customer  customer_ask_question             —           —             —
7   agent     agent_answer_query                —           —             —
8   customer  customer_acknowledge              —           —             —
9   agent     agent_greet                       —           —             —
10  customer  customer_agree                    —           —             —
11  agent     agent_greet                       —           —             —
12  customer  customer_agree                    —           —             —
13  customer  customer_ask_question             —           —             —
14  agent     agent_reassure_trust              —           —             —
15  customer  customer_query_fee                —           —             —
16  agent     agent_explain_fee                 —           —             interest rate
17  agent     agent_send_sms_link               —           send_sms      sms
18  agent     agent_end_call                    —           —             —
19  customer  customer_acknowledge              —           —             —
20  agent     agent_guide_open_link             —           —             —
21  customer  customer_agree                    —           —             —
22  agent     agent_guide_open_link             —           —             लिंक पर क्लिक
23  customer  customer_report_link_opened       —           —             —
24  agent     agent_guide_apply                 —           —             apply now
25  customer  customer_acknowledge              —           —             —
26  agent     agent_request_otp                 —           send_otp      otp
27  customer  customer_do_otp                   —           —             otp
28  agent     agent_request_otp                 —           —             otp
29  customer  customer_acknowledge              —           —             —
30  agent     agent_request_otp                 —           —             otp
31  customer  customer_do_otp                   —           —             otp
32  customer  customer_react_to_offer           —           —             —
33  agent     agent_present_final_offer         —           —             —
34  customer  customer_react_to_final_offer     —           —             —
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
5   agent     agent_greet                       —           —             —
6   customer  customer_ask_question             —           —             —
7   agent     agent_greet                       —           —             —
8   customer  customer_ask_question             —           —             —
9   agent     agent_greet                       —           —             —
10  customer  customer_agree                    —           —             —
11  customer  customer_ask_question             —           —             —
12  agent     agent_answer_query                —           —             —
13  customer  customer_query_fee                —           —             interest rate
14  agent     agent_explain_fee                 —           —             interest rate
15  customer  customer_query_fee                —           —             interest rate
16  agent     agent_explain_fee                 —           —             interest rate
17  customer  customer_agree                    —           —             —
18  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
19  customer  customer_ask_question             —           —             —
20  agent     agent_confirm                     —           —             —
21  customer  customer_ask_question             —           —             —
22  agent     agent_confirm                     —           —             —
23  customer  customer_ask_question             —           —             —
24  agent     agent_answer_query                —           —             —
25  customer  customer_do_otp                   —           —             otp
26  agent     agent_request_otp                 —           —             otp
27  customer  customer_other                    —           —             —
28  agent     agent_clarify                     —           —             —
29  customer  customer_provide_personal_details —           —             —
30  agent     agent_request_pan                 —           —             पैन
31  customer  customer_acknowledge              —           —             —
32  agent     agent_wait                        —           —             —
33  customer  customer_request_wait             —           —             —
34  agent     agent_wait                        —           —             —
35  agent     agent_request_personal_details    —           —             gender, date of birth, marital
36  customer  customer_state_employment_type    —           —             self employ
37  agent     agent_request_business_details    —           —             business
38  customer  customer_provide_org_name         —           —             —
39  agent     agent_request_org_name            —           —             —
40  customer  customer_respond_udyam            —           —             उद्यम
41  agent     agent_request_udyam               —           —             udyam, उद्यम
42  customer  customer_respond_udyam            —           —             —
43  agent     agent_clarify                     —           —             —
44  customer  customer_other                    —           —             —
45  customer  customer_react_to_final_offer     —           —             —
46  customer  customer_react_to_final_offer     —           —             —
47  agent     agent_present_final_offer         —           —             final offer
48  customer  customer_react_to_final_offer     —           —             —
49  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call c947d052 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
1   agent     agent_ask_to_repeat               —           —             फिर से कह
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
6   customer  customer_agree                    —           —             —
7   customer  customer_agree                    —           —             —
8   agent     agent_send_sms_link               —           send_sms      sms
9   agent     agent_guide_open_link             —           —             —
10  customer  customer_report_done              —           —             —
11  agent     agent_guide_apply                 —           —             apply now
12  customer  customer_report_done              —           —             —
13  agent     agent_request_otp                 —           send_otp      otp
14  customer  customer_report_done              —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_do_otp                   —           —             —
17  agent     agent_request_pan                 —           —             पैन
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_personal_details    —           —             gender, date of birth, marital
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_email               —           —             email
22  customer  customer_report_done              —           —             हो गया
23  agent     agent_request_address             —           —             address, pincode, locality, building, house number
24  agent     agent_request_terms_accept        —           —             terms and condition, terms
25  agent     agent_request_terms_accept        —           —             terms and condition, terms
26  agent     agent_ask_employment_type         —           —             salaried, self-employ
27  agent     agent_ask_employment_type         —           —             salaried, self-employ
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_income              —           —             income
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_request_org_name            —           —             organization
32  customer  customer_acknowledge              —           —             —
33  agent     agent_request_email               —           —             email
34  customer  customer_acknowledge              —           —             —
35  agent     agent_request_address             —           —             address, pincode
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_guide_apply                 —           —             —
38  customer  customer_acknowledge              —           —             —
39  agent     agent_request_otp                 —           send_otp      otp
40  customer  customer_acknowledge              —           —             —
41  agent     agent_request_otp                 —           —             otp
42  customer  customer_report_done              —           —             कर लिया
43  agent     agent_present_final_offer         —           —             final offer
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call cad04765 (transferred) — 95 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   customer  customer_ask_question             —           —             —
6   agent     agent_answer_query                —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   customer  customer_acknowledge              —           —             —
9   agent     agent_send_sms_link               —           —             sms
10  customer  customer_report_sms_received      —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms
12  agent     agent_send_sms_link               —           send_sms      sms
13  customer  customer_request_wait             —           —             —
14  agent     agent_wait                        —           —             —
15  customer  customer_report_sms_received      —           —             —
16  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई, लिंक पर क्लिक
17  customer  customer_report_link_opened       —           —             —
18  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई
19  customer  customer_request_wait             —           —             —
20  agent     agent_wait                        —           —             —
21  customer  customer_request_wait             —           —             —
22  agent     agent_wait                        —           —             —
23  customer  customer_report_link_opened       —           —             website
24  agent     agent_guide_apply                 —           —             apply now
25  customer  customer_do_otp                   —           —             —
26  agent     agent_request_otp                 —           send_otp      otp
27  customer  customer_do_otp                   —           —             —
28  agent     agent_guide_apply                 —           —             —
29  agent     agent_request_personal_details    —           —             —
30  agent     agent_request_pan                 —           —             पैन
31  customer  customer_provide_pan              —           —             —
32  agent     agent_request_personal_details    —           —             gender, date of birth, marital
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_email               —           —             email
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_address             —           —             locality, building, house number, flat
37  customer  customer_request_wait             —           —             —
38  agent     agent_wait                        —           —             —
39  customer  customer_request_wait             —           —             —
40  agent     agent_wait                        —           —             —
41  agent     agent_end_call                    —           —             —
42  customer  customer_request_wait             —           —             —
43  agent     agent_wait                        —           —             —
44  agent     agent_end_call                    —           —             —
45  customer  customer_greet                    —           —             hello
46  agent     agent_request_address             —           —             —
47  customer  customer_request_wait             —           —             —
48  agent     agent_wait                        —           —             —
49  customer  customer_request_wait             —           —             —
50  agent     agent_wait                        —           —             —
51  customer  customer_request_wait             —           —             रुकिए
52  agent     agent_request_terms_accept        —           —             terms and condition, terms
53  customer  customer_request_wait             —           —             —
54  agent     agent_wait                        —           —             —
55  customer  customer_request_wait             —           —             —
56  agent     agent_wait                        —           —             —
57  agent     agent_ask_employment_type         —           —             salaried, self-employ
58  customer  customer_request_wait             —           —             —
59  agent     agent_wait                        —           —             —
60  customer  customer_provide_personal_details —           —             —
61  agent     agent_ask_employment_type         —           —             salaried, self-employ
62  customer  customer_state_employment_type    —           —             salaried
63  agent     agent_request_income              —           —             income
64  customer  customer_provide_org_name         —           —             —
65  agent     agent_answer_query                —           —             —
66  customer  customer_provide_org_name         —           —             —
67  agent     agent_answer_query                —           —             —
68  customer  customer_provide_org_name         frustrated  —             नहीं हो रहा, नहीं हो
69  agent     agent_answer_query                —           —             —
70  customer  customer_provide_org_name         —           —             —
71  agent     agent_request_org_name            —           —             —
72  agent     agent_request_address             —           —             address
73  customer  customer_provide_email            —           —             —
74  agent     agent_request_email               —           —             email
75  agent     agent_request_address             —           —             address
76  customer  customer_request_wait             —           —             —
77  agent     agent_wait                        —           —             —
78  customer  customer_report_address_error     —           —             —
79  agent     agent_help_address_error          —           —             नहीं हो रहा
80  customer  customer_report_address_error     —           —             —
81  agent     agent_help_address_error          —           —             —
82  customer  customer_report_address_error     frustrated  —             नहीं हो
83  agent     agent_help_address_error          —           —             —
84  customer  customer_report_address_error     —           —             —
85  agent     agent_help_address_error          —           —             —
86  customer  customer_report_address_error     —           —             —
87  agent     agent_help_address_error          —           —             —
88  customer  customer_report_done              —           —             —
89  agent     agent_guide_apply                 —           —             —
90  customer  customer_acknowledge              —           —             —
91  agent     agent_wait                        —           —             —
92  customer  customer_acknowledge              —           —             —
93  agent     agent_present_final_offer         —           —             —
94  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call cb6c7a0a (transferred) — 27 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   agent     agent_greet                       —           —             —
5   customer  customer_request_wait             —           —             —
6   customer  customer_request_wait             —           —             —
7   agent     agent_wait                        —           —             —
8   customer  customer_agree                    —           —             —
9   customer  customer_agree                    —           —             —
10  agent     agent_send_sms_link               —           send_sms      sms
11  agent     agent_send_sms_link               —           —             sms
12  customer  customer_report_sms_received      —           —             —
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
14  customer  customer_acknowledge              —           —             —
15  agent     agent_guide_open_link             —           —             खुल गया
16  customer  customer_do_otp                   —           —             —
17  agent     agent_request_otp                 —           —             —
18  customer  customer_do_otp                   —           —             —
19  agent     agent_request_otp                 —           —             —
20  agent     agent_ask_to_repeat               —           —             फिर से कह
21  customer  customer_do_otp                   —           —             otp
22  agent     agent_request_otp                 —           —             otp
23  agent     agent_request_otp                 —           —             otp
24  customer  customer_acknowledge              —           —             —
25  agent     agent_wait                        —           —             —
26  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call cd8f7d74 (transferred) — 45 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_agree                    —           —             शुरू कर
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_acknowledge              —           —             —
7   customer  customer_report_sms_received      —           —             —
8   agent     agent_guide_apply                 —           —             apply now
9   customer  customer_report_done              —           —             हो गया
10  agent     agent_request_otp                 —           send_otp      otp
11  agent     agent_ask_to_repeat               —           —             फिर से कह
12  customer  customer_report_done              —           —             कर दिया
13  agent     agent_wait                        —           —             wait
14  customer  customer_do_otp                   —           —             —
15  agent     agent_request_pan                 —           —             पैन
16  agent     agent_ask_to_repeat               —           —             फिर से बता
17  customer  customer_provide_pan              —           —             —
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital
19  agent     agent_ask_to_repeat               —           —             —
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_email               —           —             email
22  agent     agent_ask_to_repeat               —           —             एक बार फिर
23  customer  customer_agree                    —           —             —
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  customer  customer_report_done              —           —             —
26  agent     agent_request_terms_accept        —           —             terms and condition, terms
27  customer  customer_report_done              —           —             कर दिया
28  agent     agent_ask_employment_type         —           —             salaried, self-employ
29  customer  customer_state_employment_type    —           —             salaried
30  agent     agent_request_income              —           —             income
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_org_name            —           —             organization
33  customer  customer_report_done              —           —             हो गया
34  agent     agent_request_email               —           —             email
35  customer  customer_report_done              —           —             हो गया
36  agent     agent_request_address             —           —             address, pincode
37  customer  customer_report_done              —           —             हो गया
38  agent     agent_guide_apply                 —           —             —
39  customer  customer_report_done              —           —             कर दिया
40  agent     agent_request_otp                 —           send_otp      otp
41  customer  customer_report_done              —           —             कर दिया
42  agent     agent_present_final_offer         —           —             final offer
43  customer  customer_react_to_final_offer     —           —             —
44  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call d1dea46c (transferred) — 63 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_greet                    —           —             hello
5   agent     agent_present_offer               —           —             pre-approved, loan offer
6   customer  customer_agree                    —           —             —
7   agent     agent_send_sms_link               —           send_sms      sms
8   agent     agent_guide_open_link             —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  agent     agent_request_otp                 —           send_otp      otp
11  agent     agent_request_otp                 —           send_otp      otp
12  agent     agent_request_otp                 —           send_otp      otp
13  agent     agent_request_otp                 —           —             otp
14  customer  customer_report_done              —           —             कर लिया
15  agent     agent_request_personal_details    —           —             —
16  customer  customer_acknowledge              —           —             —
17  agent     agent_request_pan                 —           —             पैन
18  customer  customer_acknowledge              —           —             —
19  agent     agent_request_pan                 —           —             pan
20  customer  customer_acknowledge              —           —             —
21  agent     agent_request_pan                 —           —             pan
22  customer  customer_provide_pan              —           —             —
23  agent     agent_request_personal_details    —           —             gender, date of birth, marital
24  customer  customer_request_wait             —           —             —
25  agent     agent_request_personal_details    —           —             gender, date of birth, marital
26  customer  customer_request_wait             —           —             —
27  agent     agent_request_personal_details    —           —             gender, date of birth, marital
28  agent     agent_request_personal_details    —           —             gender, date of birth, marital
29  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो
30  agent     agent_help_address_error          —           —             —
31  agent     agent_request_address             —           —             address, pincode, locality, building, house number
32  customer  customer_provide_address          —           —             —
33  agent     agent_request_address             —           —             address, pincode, locality, building, house number
34  customer  customer_report_done              —           —             कर दिया
35  agent     agent_request_terms_accept        —           —             terms and condition, terms
36  agent     agent_request_terms_accept        —           —             terms and condition, terms
37  agent     agent_ask_to_repeat               —           —             साफ़ बोल
38  agent     agent_request_terms_accept        —           —             terms and condition, terms
39  customer  customer_report_done              —           —             कर दिया
40  agent     agent_ask_employment_type         —           —             —
41  customer  customer_acknowledge              —           —             —
42  agent     agent_ask_employment_type         —           —             salaried, self-employ
43  agent     agent_ask_to_repeat               —           —             फिर से कह
44  agent     agent_ask_to_repeat               —           —             —
45  agent     agent_ask_employment_type         —           —             salaried, self-employ
46  customer  customer_respond_udyam            —           —             उद्यम
47  agent     agent_offer_skip_udyam            —           —             skip
48  customer  customer_skip_udyam               —           —             —
49  agent     agent_wait                        —           —             —
50  agent     agent_present_final_offer         —           —             final offer
51  customer  customer_other                    —           —             —
52  agent     agent_present_final_offer         —           —             final offer
53  customer  customer_other                    —           —             —
54  agent     agent_present_final_offer         —           —             final offer
55  customer  customer_request_wait             —           —             —
56  agent     agent_present_final_offer         —           —             final offer
57  customer  customer_other                    —           —             —
58  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
59  customer  customer_request_wait             —           —             रुकिए
60  agent     agent_wait                        —           —             —
61  customer  customer_react_to_final_offer     —           —             —
62  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call d3ca27af (transferred) — 83 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   customer  customer_ask_question             —           —             —
7   agent     agent_answer_query                —           —             —
8   customer  customer_request_wait             —           —             —
9   agent     agent_wait                        —           —             —
10  customer  customer_agree                    —           —             —
11  agent     agent_guide_apply                 —           —             apply now
12  customer  customer_report_done              —           —             —
13  agent     agent_request_otp                 —           send_otp      otp
14  customer  customer_acknowledge              —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_report_done              —           —             —
17  agent     agent_request_personal_details    —           —             —
18  customer  customer_acknowledge              —           —             —
19  customer  customer_react_to_final_offer     —           —             —
20  agent     agent_request_pan                 —           —             पैन
21  customer  customer_ask_question             —           —             —
22  agent     agent_request_personal_details    —           —             —
23  customer  customer_provide_pan              —           —             pan
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital
25  customer  customer_other                    frustrated  —             बार बार
26  agent     agent_wait                        —           —             —
27  customer  customer_acknowledge              —           —             —
28  agent     agent_request_personal_details    —           —             gender, date of birth, marital
29  customer  customer_report_done              —           —             —
30  agent     agent_request_email               —           —             email
31  customer  customer_report_done              —           —             —
32  agent     agent_request_address             —           —             address, pincode, locality, building, house number
33  customer  customer_report_done              —           —             —
34  agent     agent_request_address             —           —             address, pincode, locality, building, house number
35  customer  customer_acknowledge              —           —             —
36  agent     agent_request_terms_accept        —           —             terms and condition, terms
37  customer  customer_acknowledge              —           —             —
38  agent     agent_ask_employment_type         —           —             salaried, self-employ
39  customer  customer_provide_org_name         —           —             —
40  agent     agent_ask_employment_type         —           —             salaried, self-employ
41  customer  customer_report_done              —           —             —
42  agent     agent_request_income              —           —             income
43  customer  customer_report_done              —           —             —
44  agent     agent_request_org_name            —           —             organization
45  customer  customer_report_done              —           —             —
46  agent     agent_request_email               —           —             email
47  customer  customer_report_done              —           —             —
48  customer  customer_acknowledge              —           —             —
49  agent     agent_request_address             —           —             address, pincode
50  agent     agent_request_address             —           —             address
51  agent     agent_ask_employment_type         —           —             salaried, self-employ
52  customer  customer_state_employment_type    —           —             —
53  agent     agent_request_income              —           —             income
54  customer  customer_unclear                  —           —             —
55  agent     agent_acknowledge                 —           —             —
56  customer  customer_ask_query                —           —             —
57  customer  customer_react_to_final_offer     —           —             —
58  agent     agent_answer_query                —           —             —
59  customer  customer_ask_query                —           —             —
60  agent     agent_answer_query                —           —             —
61  customer  customer_ask_question             confused    —             कैसे
62  agent     agent_answer_query                —           —             —
63  customer  customer_react_to_final_offer     —           —             —
64  agent     agent_present_offer               —           —             —
65  customer  customer_query_fee                —           —             —
66  agent     agent_confirm                     —           —             शुरू कर
67  customer  customer_react_to_final_offer     —           —             —
68  agent     agent_present_final_offer         —           —             —
69  customer  customer_ask_question             —           —             —
70  agent     agent_wait                        —           —             —
71  customer  customer_other                    frustrated  —             बार बार
72  agent     agent_acknowledge                 —           —             —
73  customer  customer_acknowledge              —           —             —
74  agent     agent_present_final_offer         —           —             final offer
75  customer  customer_acknowledge              —           —             —
76  agent     agent_present_final_offer         —           —             final offer
77  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
78  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
79  customer  customer_acknowledge              —           —             —
80  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
81  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
82  agent     agent_end_call                    —           —             —
```

## Call d4dd5882 (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             —
3   customer  customer_agree                    —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_send_sms_link               —           —             sms
7   customer  customer_report_sms_received      —           —             —
8   agent     agent_present_offer               —           —             —
9   customer  customer_agree                    —           —             —
10  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
11  agent     agent_ask_to_repeat               —           —             —
12  customer  customer_report_link_opened       —           —             —
13  agent     agent_guide_apply                 —           —             apply now
14  customer  customer_provide_pan              —           —             pan
15  agent     agent_request_pan                 —           —             पैन
16  customer  customer_ask_question             —           —             —
17  agent     agent_request_pan                 —           —             पैन
18  customer  customer_provide_org_name         —           —             —
19  agent     agent_request_personal_details    —           —             gender, date of birth, marital
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_email               —           —             email
22  customer  customer_report_done              —           —             —
23  agent     agent_request_address             —           —             address
24  customer  customer_ask_question             —           —             —
25  agent     agent_request_address             —           —             address
26  customer  customer_ask_question             —           —             —
27  agent     agent_answer_query                —           —             —
28  customer  customer_do_otp                   —           —             otp
29  agent     agent_request_otp                 —           —             otp
30  customer  customer_do_otp                   —           —             —
31  agent     agent_wait                        —           —             —
32  customer  customer_provide_personal_details —           —             —
33  agent     agent_wait                        —           —             —
34  agent     agent_present_final_offer         —           —             —
35  customer  customer_react_to_final_offer     —           —             —
36  agent     agent_wait                        —           —             —
37  agent     agent_present_final_offer         —           —             —
38  customer  customer_request_wait             —           —             wait
39  agent     agent_wait                        —           —             —
40  customer  customer_react_to_final_offer     —           —             —
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call d4e27a05 (transferred) — 107 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   agent     agent_guide_apply                 —           —             —
7   customer  customer_acknowledge              —           —             —
8   agent     agent_guide_apply                 —           —             apply now
9   customer  customer_other                    —           —             —
10  agent     agent_request_otp                 —           send_otp      otp
11  customer  customer_report_applied           —           —             apply now
12  agent     agent_request_otp                 —           send_otp      otp
13  customer  customer_acknowledge              —           —             —
14  agent     agent_request_otp                 —           send_otp      otp
15  agent     agent_request_otp                 —           send_otp      otp
16  agent     agent_ask_to_repeat               —           —             फिर से कह
17  customer  customer_request_wait             —           —             —
18  agent     agent_wait                        —           —             —
19  customer  customer_react_to_offer           —           —             —
20  agent     agent_present_offer               —           —             —
21  customer  customer_agree                    —           —             —
22  agent     agent_guide_apply                 —           —             apply now
23  customer  customer_report_done              —           —             कर लिया
24  customer  customer_ask_question             —           —             —
25  agent     agent_request_pan                 —           —             पैन
26  agent     agent_request_pan                 —           —             —
27  customer  customer_agree                    —           —             —
28  agent     agent_request_pan                 —           —             पैन
29  customer  customer_ask_question             —           —             —
30  agent     agent_request_pan                 —           —             पैन
31  customer  customer_acknowledge              —           —             —
32  agent     agent_request_personal_details    —           —             gender, date of birth, marital
33  agent     agent_ask_to_repeat               —           —             फिर से बता
34  customer  customer_provide_pan              —           —             pan
35  agent     agent_request_personal_details    —           —             —
36  customer  customer_request_wait             —           —             —
37  agent     agent_wait                        —           —             —
38  customer  customer_acknowledge              —           —             —
39  agent     agent_request_email               —           —             email
40  customer  customer_report_done              —           —             —
41  customer  customer_provide_address          —           —             address, flat
42  agent     agent_request_address             —           —             address, pincode, locality, building, house number
43  customer  customer_request_wait             —           —             wait
44  agent     agent_wait                        —           —             —
45  customer  customer_acknowledge              —           —             —
46  agent     agent_request_address             —           —             address, pincode, locality, building, house number
47  customer  customer_request_wait             —           —             wait
48  customer  customer_ask_question             —           —             कौन सा
49  agent     agent_request_terms_accept        —           —             terms and condition, terms
50  customer  customer_acknowledge              —           —             —
51  agent     agent_request_terms_accept        —           —             terms and condition, terms
52  customer  customer_acknowledge              —           —             —
53  agent     agent_ask_employment_type         —           —             salaried, self-employ
54  customer  customer_provide_income           —           —             income
55  agent     agent_request_income              —           —             income
56  customer  customer_provide_income           —           —             income
57  agent     agent_request_income              —           —             —
58  customer  customer_acknowledge              —           —             —
59  agent     agent_request_org_name            —           —             organization
60  customer  customer_acknowledge              —           —             —
61  agent     agent_request_org_name            —           —             organization
62  customer  customer_report_done              —           —             —
63  agent     agent_request_email               —           —             email
64  customer  customer_request_wait             —           —             —
65  agent     agent_request_email               —           —             email
66  customer  customer_report_address_error     —           —             —
67  agent     agent_request_address             —           —             address, pincode
68  customer  customer_respond_udyam            —           —             —
69  agent     agent_request_address             —           —             address, pincode
70  customer  customer_acknowledge              —           —             —
71  agent     agent_request_udyam               —           —             udyam
72  customer  customer_other                    —           —             —
73  agent     agent_other                       —           —             —
74  agent     agent_other                       —           —             —
75  agent     agent_request_otp                 —           send_otp      otp
76  customer  customer_ask_question             —           —             —
77  agent     agent_request_otp                 —           —             otp
78  agent     agent_request_otp                 —           —             otp
79  agent     agent_wait                        —           —             —
80  agent     agent_present_final_offer         —           —             final offer
81  customer  customer_react_to_final_offer     —           —             —
82  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
83  customer  customer_acknowledge              —           —             —
84  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
85  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
86  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
87  customer  customer_acknowledge              —           —             —
88  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
89  customer  customer_acknowledge              —           —             —
90  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
91  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
92  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
93  customer  customer_acknowledge              —           —             —
94  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
95  customer  customer_acknowledge              —           —             —
96  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
97  customer  customer_acknowledge              —           —             —
98  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
99  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
100 customer  customer_acknowledge              —           —             —
101 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
102 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
103 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
104 customer  customer_acknowledge              —           —             —
105 agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
106 agent     agent_end_call                    —           —             goodbye, duration has been exceeded
```

## Call d5e52e7a (transferred) — 33 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_guide_open_link             —           —             —
7   customer  customer_express_distrust         distrustful —             fraud
8   agent     agent_reassure_trust              —           —             —
9   customer  customer_ask_question             —           —             —
10  agent     agent_answer_query                —           —             —
11  customer  customer_agree                    —           —             —
12  agent     agent_guide_open_link             —           —             —
13  agent     agent_guide_apply                 —           —             apply now
14  agent     agent_ask_to_repeat               —           —             फिर से बता
15  agent     agent_guide_apply                 —           —             apply now
16  agent     agent_request_otp                 —           send_otp      otp
17  customer  customer_do_otp                   —           —             otp
18  agent     agent_request_otp                 —           send_otp      otp
19  agent     agent_request_otp                 —           —             otp
20  customer  customer_do_otp                   frustrated  —             नहीं हो
21  agent     agent_wait                        —           —             wait
22  customer  customer_ask_question             —           —             —
23  agent     agent_guide_open_link             —           —             —
24  agent     agent_end_call                    —           —             —
25  customer  customer_agree                    —           —             —
26  agent     agent_request_otp                 —           —             otp
27  customer  customer_do_otp                   —           —             —
28  agent     agent_request_otp                 —           —             otp
29  customer  customer_report_done              —           —             कर लिया
30  agent     agent_present_final_offer         —           —             final offer
31  customer  customer_react_to_final_offer     —           —             —
32  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call d6f6cda6 (transferred) — 33 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_ask_question             —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_guide_open_link             —           —             —
7   agent     agent_guide_apply                 —           —             apply now
8   agent     agent_request_otp                 —           send_otp      otp
9   customer  customer_do_otp                   —           —             otp
10  agent     agent_request_otp                 —           send_otp      otp
11  agent     agent_request_pan                 —           —             पैन
12  customer  customer_acknowledge              —           —             —
13  agent     agent_request_personal_details    —           —             gender, date of birth, marital
14  agent     agent_request_email               —           —             email
15  customer  customer_report_done              —           —             —
16  agent     agent_request_address             —           —             address, pincode, locality, building, house number
17  agent     agent_request_terms_accept        —           —             terms and condition, terms
18  agent     agent_request_terms_accept        —           —             terms and condition, terms
19  agent     agent_ask_employment_type         —           —             salaried, self-employ
20  agent     agent_ask_employment_type         —           —             salaried, self-employ
21  customer  customer_state_employment_type    —           —             self employ
22  agent     agent_request_income              —           —             income
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_org_name            —           —             —
25  customer  customer_respond_udyam            —           —             उद्यम
26  agent     agent_request_udyam               —           —             udyam
27  customer  customer_respond_udyam            —           —             उद्यम
28  agent     agent_offer_skip_udyam            —           —             skip
29  agent     agent_request_otp                 —           send_otp      otp
30  customer  customer_react_to_final_offer     —           —             —
31  agent     agent_present_final_offer         —           —             final offer
32  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call d99d6949 (transferred) — 52 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
3   agent     agent_greet                       —           —             —
4   agent     agent_disclose_recording          —           —             record, training, quality
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_send_sms_link               —           —             sms
7   customer  customer_acknowledge              —           —             —
8   agent     agent_send_sms_link               —           —             sms
9   customer  customer_report_sms_received      —           —             sms
10  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई, लिंक पर क्लिक
11  customer  customer_report_link_opened       —           —             खुल गई
12  agent     agent_guide_apply                 —           —             apply now
13  customer  customer_report_done              —           —             —
14  agent     agent_request_otp                 —           send_otp      otp
15  customer  customer_unclear                  —           —             —
16  agent     agent_request_otp                 —           —             —
17  customer  customer_report_done              —           —             कर दिया
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_provide_income           —           —             income
20  agent     agent_request_income              —           —             income
21  customer  customer_provide_business_details —           —             business
22  agent     agent_request_org_name            —           —             —
23  agent     agent_ask_to_repeat               —           —             —
24  customer  customer_report_done              —           —             कर दिया
25  agent     agent_request_address             —           —             address
26  agent     agent_ask_to_repeat               —           —             —
27  customer  customer_acknowledge              —           —             —
28  agent     agent_request_business_details    —           —             —
29  customer  customer_ask_question             —           —             —
30  agent     agent_answer_query                —           —             —
31  agent     agent_present_final_offer         —           —             final offer
32  customer  customer_greet                    —           —             hello
33  agent     agent_present_final_offer         —           —             —
34  customer  customer_provide_address          —           —             —
35  agent     agent_help_address_error          —           —             —
36  customer  customer_report_done              frustrated  —             भर दिया, नहीं हो रहा, नहीं हो
37  agent     agent_acknowledge                 —           —             —
38  customer  customer_provide_business_details —           —             business
39  agent     agent_request_business_details    —           —             —
40  customer  customer_respond_udyam            —           —             उद्यम
41  agent     agent_request_udyam               —           —             udyam, उद्यम
42  agent     agent_ask_to_repeat               —           —             फिर से कह
43  customer  customer_skip_udyam               —           —             skip
44  agent     agent_offer_skip_udyam            —           —             skip
45  customer  customer_unclear                  —           —             —
46  agent     agent_offer_skip_udyam            —           —             skip
47  customer  customer_ask_question             —           —             —
48  agent     agent_answer_query                —           —             —
49  customer  customer_react_to_final_offer     —           —             —
50  agent     agent_present_final_offer         —           —             final offer
51  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call d9aaa177 (transferred) — 27 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   agent     agent_greet                       —           —             —
5   customer  customer_agree                    —           —             —
6   customer  customer_ask_question             —           —             —
7   agent     agent_present_offer               —           —             pre approved, personal loan
8   agent     agent_send_sms_link               —           send_sms      sms
9   agent     agent_send_sms_link               —           —             sms
10  customer  customer_report_sms_received      —           —             —
11  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
12  customer  customer_report_link_opened       —           —             —
13  customer  customer_express_distrust         —           —             —
14  agent     agent_acknowledge                 —           —             —
15  customer  customer_acknowledge              —           —             —
16  agent     agent_guide_open_link             —           —             लिंक पर क्लिक
17  customer  customer_express_distrust         —           —             —
18  agent     agent_reassure_trust              —           —             —
19  customer  customer_greet                    —           —             hello
20  agent     agent_guide_open_link             —           —             —
21  customer  customer_acknowledge              —           —             —
22  agent     agent_present_final_offer         —           —             —
23  customer  customer_ask_question             —           —             —
24  agent     agent_present_final_offer         —           —             —
25  customer  customer_react_to_final_offer     —           —             —
26  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call db6ab517 (transferred) — 35 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             बात कर रही, से बात
4   customer  customer_agree                    —           —             शुरू कर
5   agent     agent_send_sms_link               —           send_sms      sms
6   customer  customer_acknowledge              —           —             —
7   agent     agent_guide_open_link             —           —             —
8   agent     agent_ask_to_repeat               —           —             फिर से कह
9   customer  customer_report_link_opened       —           —             —
10  agent     agent_guide_apply                 —           —             apply now
11  customer  customer_report_sms_received      —           —             —
12  agent     agent_other                       —           —             —
13  customer  customer_ask_question             —           —             —
14  agent     agent_answer_query                —           —             —
15  customer  customer_request_wait             —           —             —
16  agent     agent_wait                        —           —             —
17  customer  customer_acknowledge              —           —             —
18  agent     agent_guide_apply                 —           —             apply now
19  customer  customer_report_applied           —           —             —
20  agent     agent_request_otp                 —           send_otp      otp
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_otp                 —           send_otp      otp
23  agent     agent_ask_to_repeat               —           —             —
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_guide_apply                 —           —             —
26  agent     agent_ask_to_repeat               —           —             —
27  customer  customer_do_otp                   —           —             —
28  agent     agent_request_email               —           —             email
29  customer  customer_ask_question             —           —             —
30  agent     agent_wait                        —           —             wait
31  agent     agent_present_final_offer         —           —             final offer
32  agent     agent_present_final_offer         —           —             final offer
33  customer  customer_react_to_final_offer     —           —             —
34  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call dc0ddbd3 (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_greet                    —           —             hello
3   customer  customer_report_link_opened       —           —             —
4   agent     agent_guide_open_link             —           —             —
5   customer  customer_express_distrust         —           —             —
6   agent     agent_acknowledge                 —           —             —
7   customer  customer_report_link_opened       —           —             —
8   agent     agent_guide_open_link             —           —             —
9   customer  customer_ask_question             —           —             —
10  customer  customer_other                    —           —             —
11  agent     agent_wait                        —           —             —
12  agent     agent_ask_to_repeat               —           —             —
13  agent     agent_guide_open_link             —           —             —
14  customer  customer_report_sms_received      —           —             sms, link भेज
15  agent     agent_send_sms_link               —           send_sms      sms
16  customer  customer_report_sms_received      —           —             link भेज
17  agent     agent_send_sms_link               —           send_sms      sms
18  customer  customer_ask_question             —           —             —
19  agent     agent_guide_apply                 —           —             apply now
20  customer  customer_report_applied           —           —             —
21  agent     agent_request_otp                 —           send_otp      otp
22  customer  customer_unclear                  —           —             —
23  agent     agent_request_otp                 —           send_otp      otp
24  customer  customer_do_otp                   —           —             otp
25  agent     agent_guide_apply                 —           —             —
26  customer  customer_ask_question             —           —             —
27  agent     agent_acknowledge                 —           —             —
28  customer  customer_agree                    —           —             —
29  agent     agent_wait                        —           —             —
30  customer  customer_acknowledge              —           —             —
31  customer  customer_request_wait             —           —             —
32  agent     agent_wait                        —           —             —
33  customer  customer_ask_question             —           —             —
34  agent     agent_acknowledge                 —           —             —
35  customer  customer_ask_question             —           —             —
36  agent     agent_wait                        —           —             —
37  customer  customer_acknowledge              —           —             —
38  agent     agent_wait                        —           —             —
39  customer  customer_acknowledge              —           —             —
40  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
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
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             —
6   customer  customer_agree                    —           —             —
7   customer  customer_query_fee                —           —             emi
8   agent     agent_answer_query                —           —             —
9   customer  customer_agree                    —           —             —
10  agent     agent_send_sms_link               —           send_sms      sms
11  agent     agent_send_sms_link               —           —             sms
12  customer  customer_request_wait             —           —             —
13  agent     agent_wait                        —           —             —
14  customer  customer_report_done              —           —             —
15  agent     agent_guide_open_link             —           —             खुल गया
16  customer  customer_report_link_opened       —           —             खुल गया
17  agent     agent_guide_apply                 —           —             apply now
18  customer  customer_report_applied           —           —             apply now
19  customer  customer_do_otp                   —           —             —
20  agent     agent_request_otp                 —           send_otp      otp
21  customer  customer_report_done              —           —             हो गया
22  agent     agent_request_terms_accept        —           —             —
23  customer  customer_provide_personal_details —           —             —
24  agent     agent_request_pan                 —           —             पैन
25  customer  customer_provide_address          —           —             address
26  agent     agent_request_personal_details    —           —             gender, date of birth, marital
27  customer  customer_report_done              —           —             हो गया
28  agent     agent_request_email               —           —             email
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_address             —           —             address, locality, building, house number, flat
31  customer  customer_report_done              —           —             हो गया
32  agent     agent_request_terms_accept        —           —             terms and condition, terms
33  customer  customer_report_address_error     —           —             —
34  agent     agent_help_address_error          —           —             error
35  customer  customer_report_address_error     —           —             —
36  agent     agent_help_address_error          —           —             error
37  customer  customer_report_done              —           —             हो गया
38  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक
39  customer  customer_state_employment_type    —           —             —
40  agent     agent_ask_employment_type         —           —             salaried, self-employ
41  customer  customer_state_employment_type    —           —             self employ
42  agent     agent_request_income              —           —             income
43  agent     agent_request_org_name            —           —             —
44  customer  customer_report_done              —           —             हो गया
45  agent     agent_request_business_details    —           —             business
46  customer  customer_report_done              —           —             हो गया
47  agent     agent_request_business_details    —           —             business
48  customer  customer_report_done              —           —             हो गया
49  agent     agent_request_udyam               —           —             udyam
50  customer  customer_respond_udyam            —           —             उद्यम
51  agent     agent_request_udyam               —           —             udyam
52  customer  customer_skip_udyam               —           —             skip
53  agent     agent_offer_skip_udyam            —           —             skip
54  customer  customer_request_wait             —           —             wait
55  agent     agent_wait                        —           —             —
56  customer  customer_react_to_final_offer     —           —             —
57  agent     agent_request_otp                 —           —             otp
58  customer  customer_ask_question             —           —             —
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call e0df1c39 (transferred) — 87 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             —
6   customer  customer_agree                    —           —             —
7   agent     agent_present_offer               —           —             pre approved, loan offer, personal loan, ₹150000, 150000
8   customer  customer_greet                    —           —             hello
9   agent     agent_send_sms_link               —           send_sms      sms
10  customer  customer_greet                    —           —             hello
11  agent     agent_send_sms_link               —           send_sms      sms
12  customer  customer_greet                    —           —             hello
13  agent     agent_send_sms_link               —           —             sms
14  customer  customer_report_sms_received      —           —             —
15  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
16  agent     agent_ask_to_repeat               —           —             फिर से बता
17  customer  customer_request_wait             —           —             —
18  agent     agent_wait                        —           —             —
19  customer  customer_report_link_opened       —           —             खुल गया
20  agent     agent_guide_apply                 —           —             apply now
21  customer  customer_do_otp                   —           —             —
22  agent     agent_request_otp                 —           send_otp      otp
23  agent     agent_request_otp                 —           —             otp
24  customer  customer_do_otp                   —           —             —
25  agent     agent_wait                        —           —             —
26  agent     agent_wait                        —           —             —
27  customer  customer_do_otp                   frustrated  —             otp, नहीं हो रहा, नहीं हो
28  agent     agent_answer_query                —           —             —
29  agent     agent_ask_to_repeat               —           —             —
30  customer  customer_unclear                  —           —             —
31  agent     agent_greet                       —           —             —
32  customer  customer_unclear                  —           —             —
33  agent     agent_greet                       —           —             बात कर रही, से बात
34  customer  customer_agree                    —           —             —
35  agent     agent_greet                       —           —             —
36  customer  customer_agree                    —           —             —
37  customer  customer_agree                    —           —             —
38  customer  customer_agree                    —           —             —
39  agent     agent_send_sms_link               —           send_sms      sms
40  customer  customer_report_sms_received      —           —             sms
41  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
42  customer  customer_report_link_opened       —           —             खुल गया
43  agent     agent_guide_apply                 —           —             apply now
44  customer  customer_acknowledge              —           —             —
45  agent     agent_request_otp                 —           send_otp      otp
46  agent     agent_ask_to_repeat               —           —             —
47  customer  customer_do_otp                   —           —             —
48  agent     agent_request_otp                 —           send_otp      otp
49  agent     agent_ask_to_repeat               —           —             —
50  customer  customer_greet                    —           —             hello
51  agent     agent_greet                       —           —             बात कर रही, से बात
52  customer  customer_agree                    —           —             —
53  agent     agent_greet                       —           —             —
54  customer  customer_provide_pan              —           —             pan
55  agent     agent_request_pan                 —           —             पैन
56  customer  customer_agree                    —           —             —
57  agent     agent_acknowledge                 —           —             —
58  customer  customer_agree                    —           —             —
59  agent     agent_guide_open_link             —           —             लिंक पर क्लिक
60  agent     agent_guide_open_link             —           —             लिंक पर क्लिक
61  customer  customer_request_wait             —           —             —
62  agent     agent_wait                        —           —             —
63  agent     agent_ask_to_repeat               —           —             फिर से कह
64  customer  customer_provide_pan              —           —             pan
65  agent     agent_request_pan                 —           —             पैन
66  customer  customer_acknowledge              —           —             —
67  agent     agent_request_personal_details    —           —             gender, date of birth, marital
68  customer  customer_acknowledge              —           —             —
69  agent     agent_request_email               —           —             email
70  customer  customer_provide_pan              —           —             pan
71  agent     agent_wait                        —           —             —
72  customer  customer_ask_question             —           —             —
73  agent     agent_reassure_trust              —           —             —
74  customer  customer_request_wait             —           —             —
75  agent     agent_wait                        —           —             —
76  agent     agent_ask_to_repeat               —           —             —
77  customer  customer_request_wait             —           —             —
78  agent     agent_wait                        —           —             —
79  agent     agent_ask_to_repeat               —           —             —
80  agent     agent_end_call                    —           —             —
81  agent     agent_clarify                     —           —             —
82  customer  customer_react_to_final_offer     —           —             —
83  agent     agent_present_final_offer         —           —             final offer
84  customer  customer_react_to_final_offer     —           —             —
85  agent     agent_present_final_offer         —           —             final offer
86  customer  customer_ask_question             —           —             —
```

## Call e4d8f629 (transferred) — 38 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   agent     agent_ask_to_repeat               —           —             —
1   customer  customer_greet                    —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
3   customer  customer_agree                    —           —             —
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   customer  customer_acknowledge              —           —             —
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_report_link_opened       —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_report_applied           —           —             —
11  agent     agent_request_otp                 —           send_otp      otp
12  customer  customer_report_done              —           —             —
13  agent     agent_request_pan                 —           —             पैन
14  customer  customer_report_done              —           —             हो गया
15  agent     agent_request_personal_details    —           —             gender, date of birth, marital
16  customer  customer_report_done              —           —             कर दिया
17  agent     agent_request_email               —           —             email
18  customer  customer_report_done              —           —             —
19  agent     agent_request_address             —           —             address, pincode, locality, building, house number
20  customer  customer_report_done              —           —             भर दिया
21  agent     agent_request_terms_accept        —           —             terms and condition, terms
22  customer  customer_report_done              —           —             कर दिया
23  agent     agent_ask_employment_type         —           —             salaried, self-employ
24  customer  customer_state_employment_type    —           —             salaried
25  agent     agent_request_income              —           —             income
26  customer  customer_report_done              —           —             भर दिया
27  agent     agent_request_org_name            —           —             organization
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_email               —           —             email
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_request_business_details    —           —             —
32  customer  customer_report_done              —           —             —
33  agent     agent_request_otp                 —           send_otp      otp
34  customer  customer_report_done              —           —             हो गया
35  agent     agent_present_final_offer         —           —             final offer
36  customer  customer_react_to_final_offer     —           —             —
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call e867e396 (transferred) — 66 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_send_sms_link               —           send_sms      sms
3   agent     agent_guide_open_link             —           —             —
4   customer  customer_report_link_opened       —           —             —
5   agent     agent_guide_apply                 —           —             apply now
6   agent     agent_guide_apply                 —           —             apply now
7   customer  customer_do_otp                   —           —             —
8   agent     agent_request_otp                 —           send_otp      otp
9   customer  customer_report_done              —           —             कर दिया
10  agent     agent_request_otp                 —           send_otp      otp
11  customer  customer_report_done              —           —             कर दिया
12  agent     agent_request_otp                 —           —             —
13  customer  customer_acknowledge              —           —             —
14  agent     agent_request_pan                 —           —             पैन
15  customer  customer_acknowledge              —           —             —
16  agent     agent_request_pan                 —           —             पैन
17  customer  customer_provide_pan              —           —             pan
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital
19  customer  customer_report_done              —           —             कर दिया
20  agent     agent_request_email               —           —             email
21  customer  customer_report_done              —           —             कर दिया
22  agent     agent_request_email               —           —             email
23  customer  customer_report_done              —           —             हो गया
24  agent     agent_request_address             —           —             address, pincode, locality, building, house number
25  agent     agent_request_address             —           —             address
26  customer  customer_report_done              —           —             हो गया
27  agent     agent_request_terms_accept        —           —             terms and condition, terms
28  agent     agent_request_terms_accept        —           —             terms and condition, terms
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_ask_employment_type         —           —             salaried, self-employ
31  customer  customer_acknowledge              —           —             —
32  agent     agent_ask_employment_type         —           —             salaried, self-employ
33  customer  customer_report_done              —           —             कर दिया
34  agent     agent_ask_employment_type         —           —             salaried, self-employ
35  agent     agent_request_income              —           —             income
36  customer  customer_report_done              —           —             कर दिया
37  agent     agent_request_org_name            —           —             organization
38  customer  customer_provide_email            —           —             email
39  agent     agent_answer_query                —           —             —
40  customer  customer_report_done              —           —             कर दिया
41  agent     agent_request_business_details    —           —             —
42  agent     agent_end_call                    —           —             —
43  customer  customer_acknowledge              —           —             —
44  agent     agent_greet                       —           —             —
45  customer  customer_acknowledge              —           —             —
46  agent     agent_request_pan                 —           —             पैन
47  agent     agent_ask_to_repeat               —           —             फिर से कह
48  customer  customer_other                    —           —             —
49  agent     agent_wait                        —           —             —
50  agent     agent_present_final_offer         —           —             final offer
51  customer  customer_other                    —           —             —
52  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
53  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
54  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
55  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
56  agent     agent_present_final_offer         —           —             final offer
57  customer  customer_react_to_final_offer     —           —             —
58  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
59  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
60  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
61  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
62  customer  customer_acknowledge              —           —             —
63  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
64  customer  customer_other                    —           —             —
65  customer  customer_ask_question             —           —             —
```

## Call eac9ea27 (transferred) — 80 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_agree                    —           —             —
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   customer  customer_express_distrust         —           —             —
6   agent     agent_reassure_trust              —           —             —
7   customer  customer_agree                    —           —             शुरू कर
8   agent     agent_send_sms_link               —           send_sms      sms
9   agent     agent_send_sms_link               —           —             sms
10  customer  customer_request_wait             —           —             एक second
11  agent     agent_wait                        —           —             —
12  customer  customer_report_sms_received      —           —             sms
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
14  customer  customer_request_wait             —           —             —
15  agent     agent_wait                        —           —             —
16  customer  customer_report_link_opened       —           —             —
17  agent     agent_guide_apply                 —           —             apply now
18  customer  customer_acknowledge              —           —             —
19  agent     agent_guide_apply                 —           —             apply now
20  customer  customer_do_otp                   —           —             otp
21  agent     agent_request_otp                 —           —             otp
22  customer  customer_provide_personal_details —           —             —
23  agent     agent_request_personal_details    —           —             —
24  customer  customer_provide_personal_details —           —             date of birth
25  agent     agent_request_personal_details    —           —             date of birth, marital
26  customer  customer_provide_email            —           —             email
27  agent     agent_request_address             —           —             address, locality, building, house number, flat
28  customer  customer_provide_address          —           —             address
29  agent     agent_request_address             —           —             address
30  customer  customer_provide_address          —           —             address
31  agent     agent_request_address             —           —             address
32  customer  customer_provide_address          —           —             address
33  agent     agent_request_terms_accept        —           —             terms and condition, terms
34  customer  customer_request_wait             —           —             एक second
35  agent     agent_wait                        —           —             —
36  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_terms_accept        —           —             —
39  customer  customer_report_done              —           —             —
40  agent     agent_ask_employment_type         —           —             salaried, self-employ
41  agent     agent_ask_to_repeat               —           —             फिर से कह
42  agent     agent_ask_to_repeat               —           —             —
43  customer  customer_state_employment_type    —           —             salaried
44  agent     agent_request_income              —           —             income
45  agent     agent_request_org_name            —           —             organization
46  customer  customer_provide_email            —           —             email
47  agent     agent_answer_query                —           —             —
48  customer  customer_provide_business_details —           —             —
49  agent     agent_request_business_details    —           —             —
50  agent     agent_request_business_details    —           —             —
51  customer  customer_acknowledge              —           —             —
52  agent     agent_request_otp                 —           —             otp
53  customer  customer_provide_email            —           —             email
54  agent     agent_request_email               —           —             email
55  customer  customer_report_address_error     —           —             —
56  agent     agent_answer_query                —           —             —
57  customer  customer_ask_query                —           —             —
58  agent     agent_answer_query                —           —             —
59  customer  customer_ask_query                —           —             —
60  agent     agent_answer_query                —           —             —
61  customer  customer_provide_email            —           —             email
62  agent     agent_request_email               —           —             email
63  customer  customer_report_done              —           —             —
64  agent     agent_ask_employment_type         —           —             salaried, self-employ
65  customer  customer_report_done              —           —             कर दिया
66  agent     agent_ask_employment_type         —           —             —
67  customer  customer_other                    —           —             —
68  agent     agent_answer_query                —           —             —
69  customer  customer_report_done              —           —             —
70  agent     agent_wait                        —           —             —
71  customer  customer_provide_pan              —           —             pan
72  agent     agent_request_pan                 —           —             पैन
73  agent     agent_request_pan                 —           —             पैन
74  customer  customer_acknowledge              —           —             —
75  agent     agent_inform_manual_review        —           push_to_crm   —
76  customer  customer_react_to_final_offer     —           —             —
77  agent     agent_present_final_offer         —           —             final offer
78  customer  customer_ask_question             —           —             —
79  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call eafb82a7 (transferred) — 43 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_ask_question             —           —             —
3   agent     agent_greet                       —           —             बात कर रही, से बात
4   customer  customer_greet                    —           —             hello
5   customer  customer_agree                    —           —             शुरू कर
6   agent     agent_send_sms_link               —           send_sms      sms
7   customer  customer_agree                    —           —             —
8   agent     agent_guide_open_link             —           —             —
9   agent     agent_ask_to_repeat               —           —             फिर से कह
10  customer  customer_other                    —           —             —
11  agent     agent_guide_open_link             —           —             —
12  customer  customer_request_wait             —           —             —
13  agent     agent_wait                        —           —             —
14  customer  customer_report_sms_received      —           —             —
15  agent     agent_guide_apply                 —           —             apply now
16  customer  customer_report_done              —           —             —
17  agent     agent_request_otp                 —           —             —
18  customer  customer_report_applied           —           —             apply now
19  agent     agent_request_otp                 —           send_otp      otp
20  customer  customer_report_done              —           —             —
21  agent     agent_request_otp                 —           send_otp      otp
22  agent     agent_ask_to_repeat               —           —             एक बार फिर
23  customer  customer_other                    —           —             —
24  customer  customer_greet                    —           —             hello
25  agent     agent_send_sms_link               —           send_sms      sms
26  agent     agent_guide_open_link             —           —             —
27  customer  customer_ask_question             —           —             —
28  agent     agent_guide_open_link             —           —             —
29  customer  customer_request_wait             —           —             —
30  agent     agent_wait                        —           —             —
31  agent     agent_ask_to_repeat               —           —             —
32  customer  customer_request_wait             —           —             —
33  agent     agent_guide_apply                 —           —             apply now
34  customer  customer_react_to_final_offer     —           —             —
35  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
36  customer  customer_acknowledge              —           —             —
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
38  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
39  customer  customer_ask_question             —           —             —
40  agent     agent_explain_fee                 —           —             interest rate
41  agent     agent_end_call                    —           —             —
42  customer  customer_greet                    —           —             hello
```

## Call eeebd91b (transferred) — 41 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_send_sms_link               —           —             sms
6   customer  customer_react_to_offer           —           —             —
7   agent     agent_present_offer               —           —             pre approved
8   customer  customer_report_link_opened       —           —             खुल गया
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_report_done              —           —             —
11  agent     agent_acknowledge                 —           —             —
12  agent     agent_request_otp                 —           send_otp      otp
13  customer  customer_provide_pan              —           —             —
14  agent     agent_request_otp                 —           send_otp      otp
15  customer  customer_ask_question             —           —             —
16  agent     agent_confirm                     —           —             —
17  customer  customer_other                    —           —             —
18  agent     agent_answer_query                —           —             —
19  customer  customer_other                    —           —             —
20  agent     agent_answer_query                —           —             —
21  agent     agent_request_otp                 —           send_otp      otp
22  agent     agent_request_pan                 —           —             पैन
23  customer  customer_do_otp                   —           —             otp
24  agent     agent_wait                        —           —             —
25  customer  customer_ask_question             —           —             —
26  agent     agent_answer_query                —           —             —
27  customer  customer_other                    —           —             —
28  agent     agent_answer_query                —           —             —
29  customer  customer_request_wait             —           —             —
30  agent     agent_wait                        —           —             —
31  customer  customer_provide_pan              —           —             pan
32  agent     agent_request_pan                 —           —             पैन
33  customer  customer_request_wait             —           —             —
34  agent     agent_wait                        —           —             —
35  customer  customer_acknowledge              —           —             —
36  agent     agent_wait                        —           —             —
37  customer  customer_react_to_final_offer     —           —             —
38  agent     agent_present_final_offer         —           —             —
39  customer  customer_agree                    —           —             —
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call ef64397b (transferred) — 69 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   agent     agent_greet                       —           —             hello
6   agent     agent_present_offer               —           —             pre-approved, loan offer
7   customer  customer_agree                    —           —             —
8   agent     agent_confirm                     —           —             —
9   agent     agent_send_sms_link               —           send_sms      sms
10  customer  customer_agree                    —           —             —
11  agent     agent_send_sms_link               —           send_sms      sms
12  customer  customer_report_sms_received      —           —             sms
13  agent     agent_guide_apply                 —           —             apply now
14  customer  customer_do_otp                   —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  agent     agent_ask_to_repeat               —           —             —
17  customer  customer_do_otp                   —           —             —
18  agent     agent_request_pan                 —           —             pan
19  customer  customer_provide_pan              —           —             pan
20  agent     agent_request_pan                 —           —             pan
21  agent     agent_request_personal_details    —           —             gender, date of birth, marital
22  customer  customer_request_wait             —           —             —
23  agent     agent_wait                        —           —             —
24  agent     agent_ask_to_repeat               —           —             —
25  customer  customer_provide_personal_details —           —             —
26  agent     agent_request_email               —           —             email
27  customer  customer_provide_address          —           —             address
28  agent     agent_request_address             —           —             address, pincode, locality, building, house number
29  agent     agent_request_terms_accept        —           —             terms and condition, terms
30  customer  customer_accept_terms             —           —             —
31  agent     agent_ask_employment_type         —           —             salaried, self-employ
32  customer  customer_request_wait             —           —             wait
33  agent     agent_wait                        —           —             wait
34  agent     agent_ask_to_repeat               —           —             —
35  customer  customer_provide_address          —           —             —
36  agent     agent_ask_employment_type         —           —             salaried, self-employ
37  customer  customer_ask_question             —           —             —
38  agent     agent_ask_employment_type         —           —             salaried
39  customer  customer_state_employment_type    —           —             —
40  agent     agent_ask_employment_type         —           —             salaried, self-employ
41  agent     agent_request_income              —           —             income
42  customer  customer_agree                    —           —             —
43  agent     agent_request_org_name            —           —             organization
44  customer  customer_agree                    —           —             —
45  agent     agent_request_org_name            —           —             organization
46  customer  customer_ask_question             —           —             —
47  agent     agent_ask_to_repeat               —           —             —
48  customer  customer_request_wait             —           —             —
49  agent     agent_wait                        —           —             —
50  customer  customer_agree                    —           —             —
51  agent     agent_request_email               —           —             email
52  customer  customer_acknowledge              —           —             —
53  agent     agent_request_email               —           —             email
54  customer  customer_acknowledge              —           —             —
55  agent     agent_request_business_details    —           —             —
56  customer  customer_ask_question             —           —             —
57  agent     agent_request_business_details    —           —             —
58  customer  customer_agree                    —           —             —
59  agent     agent_request_business_details    —           —             —
60  customer  customer_report_done              —           —             —
61  agent     agent_request_terms_accept        —           —             —
62  customer  customer_other                    —           —             —
63  agent     agent_request_terms_accept        —           —             —
64  customer  customer_agree                    —           —             —
65  agent     agent_present_final_offer         —           —             final offer, loan amount and
66  customer  customer_ask_question             —           —             —
67  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
68  customer  customer_greet                    —           —             hello
```

## Call f08ea751 (transferred) — 41 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             —
3   agent     agent_disclose_recording          —           —             —
4   agent     agent_send_sms_link               —           send_sms      sms
5   customer  customer_other                    —           —             —
6   agent     agent_answer_query                —           —             —
7   customer  customer_report_sms_received      —           —             —
8   agent     agent_send_sms_link               —           send_sms      sms
9   customer  customer_report_sms_received      —           —             —
10  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
11  agent     agent_guide_open_link             —           —             —
12  customer  customer_acknowledge              —           —             —
13  agent     agent_guide_open_link             —           —             खुल गया, लिंक पर क्लिक
14  customer  customer_report_link_opened       —           —             —
15  agent     agent_guide_apply                 —           —             apply now
16  customer  customer_other                    —           —             —
17  agent     agent_answer_query                —           —             —
18  customer  customer_acknowledge              —           —             —
19  agent     agent_guide_open_link             —           —             —
20  customer  customer_other                    —           —             —
21  agent     agent_answer_query                —           —             —
22  customer  customer_report_link_opened       —           —             खुल गया
23  agent     agent_guide_apply                 —           —             apply now
24  agent     agent_acknowledge                 —           —             —
25  customer  customer_report_link_opened       —           —             खुल गया
26  agent     agent_guide_apply                 —           —             apply now
27  customer  customer_do_otp                   —           —             —
28  agent     agent_request_otp                 —           send_otp      otp
29  customer  customer_report_done              —           —             —
30  agent     agent_request_otp                 —           send_otp      otp
31  customer  customer_do_otp                   —           —             otp
32  agent     agent_acknowledge                 —           —             —
33  customer  customer_other                    —           —             —
34  agent     agent_request_otp                 —           —             otp
35  customer  customer_do_otp                   —           —             —
36  agent     agent_request_otp                 —           —             otp
37  customer  customer_do_otp                   —           —             otp
38  agent     agent_wait                        —           —             —
39  customer  customer_react_to_final_offer     —           —             —
40  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call f13dd20b (transferred) — 50 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_acknowledge              —           —             record
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_present_offer               —           —             pre-approved, loan offer
4   customer  customer_agree                    —           —             —
5   agent     agent_send_sms_link               —           send_sms      sms
6   customer  customer_acknowledge              —           —             —
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_report_link_opened       —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  agent     agent_request_otp                 —           send_otp      otp
11  agent     agent_request_otp                 —           —             otp
12  agent     agent_request_pan                 —           —             pan
13  customer  customer_provide_pan              —           —             pan
14  agent     agent_request_pan                 —           —             pan
15  customer  customer_provide_pan              —           —             pan
16  agent     agent_request_personal_details    —           —             gender, date of birth, marital
17  customer  customer_report_done              —           —             —
18  agent     agent_request_email               —           —             email
19  customer  customer_report_done              —           —             —
20  agent     agent_request_address             —           —             address, pincode, locality, building, house number
21  customer  customer_report_done              —           —             —
22  customer  customer_greet                    —           —             hello
23  agent     agent_request_address             —           —             address
24  customer  customer_agree                    —           —             —
25  agent     agent_request_terms_accept        —           —             terms and condition, terms
26  agent     agent_ask_to_repeat               —           —             —
27  customer  customer_report_done              —           —             —
28  agent     agent_ask_employment_type         —           —             salaried, self-employ
29  customer  customer_state_employment_type    —           —             —
30  agent     agent_request_income              —           —             income
31  customer  customer_report_done              —           —             —
32  agent     agent_request_org_name            —           —             organization
33  customer  customer_ask_question             —           —             —
34  agent     agent_request_org_name            —           —             organization
35  customer  customer_report_done              —           —             —
36  agent     agent_request_email               —           —             email
37  customer  customer_acknowledge              —           —             —
38  agent     agent_request_email               —           —             email
39  customer  customer_report_done              —           —             —
40  agent     agent_request_business_details    —           —             —
41  customer  customer_report_done              —           —             —
42  agent     agent_request_terms_accept        —           —             —
43  customer  customer_report_done              —           —             —
44  agent     agent_request_otp                 —           —             otp
45  customer  customer_report_done              —           —             —
46  agent     agent_present_final_offer         —           —             final offer, loan amount and
47  customer  customer_react_to_final_offer     —           —             —
48  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
49  customer  customer_query_fee                —           —             processing fee
```

## Call f2c92714 (transferred) — 38 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   customer  customer_ask_question             —           —             —
6   customer  customer_agree                    —           —             शुरू कर
7   agent     agent_send_sms_link               —           send_sms      sms
8   agent     agent_guide_open_link             —           —             —
9   agent     agent_ask_to_repeat               —           —             फिर से कह
10  customer  customer_report_done              —           —             —
11  agent     agent_guide_open_link             —           —             —
12  customer  customer_report_link_opened       —           —             —
13  agent     agent_guide_apply                 —           —             apply now
14  customer  customer_report_done              —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_report_done              —           —             —
17  agent     agent_request_otp                 —           send_otp      otp
18  customer  customer_acknowledge              —           —             —
19  agent     agent_ask_to_repeat               —           —             —
20  customer  customer_do_otp                   —           —             otp
21  agent     agent_guide_apply                 —           —             —
22  customer  customer_ask_question             —           —             —
23  agent     agent_request_otp                 —           send_otp      otp
24  agent     agent_request_otp                 —           —             otp
25  customer  customer_ask_question             —           —             —
26  customer  customer_respond_udyam            —           —             —
27  agent     agent_request_otp                 —           —             otp
28  customer  customer_request_wait             —           —             —
29  agent     agent_wait                        —           —             —
30  customer  customer_do_otp                   —           —             otp
31  agent     agent_request_otp                 —           —             otp
32  customer  customer_react_to_offer           —           —             —
33  agent     agent_present_offer               —           —             loan offer
34  customer  customer_agree                    —           —             आगे बढ़
35  agent     agent_present_final_offer         —           —             final offer
36  customer  customer_react_to_final_offer     —           —             —
37  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call f39df9d9 (transferred) — 46 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             —
3   customer  customer_agree                    —           —             —
4   customer  customer_ask_question             —           —             —
5   agent     agent_present_offer               —           —             pre approved, personal loan
6   customer  customer_query_fee                —           —             —
7   agent     agent_explain_fee                 —           —             interest rate
8   agent     agent_send_sms_link               —           —             sms
9   agent     agent_guide_open_link             —           —             लिंक पर क्लिक
10  agent     agent_ask_to_repeat               —           —             —
11  customer  customer_acknowledge              —           —             —
12  agent     agent_guide_open_link             —           —             खुल गया
13  agent     agent_ask_to_repeat               —           —             —
14  customer  customer_report_link_opened       —           —             —
15  agent     agent_guide_apply                 —           —             apply now
16  customer  customer_report_done              —           —             कर लिया
17  agent     agent_request_otp                 —           send_otp      otp
18  customer  customer_report_done              —           —             हो गया
19  agent     agent_request_personal_details    —           —             —
20  agent     agent_request_pan                 —           —             पैन
21  customer  customer_report_done              —           —             कर दिया
22  agent     agent_request_personal_details    —           —             gender, date of birth, marital
23  customer  customer_report_done              —           —             —
24  agent     agent_request_email               —           —             email
25  customer  customer_report_done              —           —             —
26  agent     agent_request_address             —           —             address, locality, building, house number, flat
27  agent     agent_clarify                     —           —             —
28  customer  customer_report_done              —           —             हो गया, कर दिया
29  agent     agent_request_terms_accept        —           —             terms and condition, terms
30  agent     agent_ask_employment_type         —           —             salaried, self-employ
31  customer  customer_state_employment_type    —           —             salaried
32  agent     agent_request_income              —           —             income
33  customer  customer_report_done              —           —             भर दिया
34  agent     agent_request_org_name            —           —             organization
35  customer  customer_report_done              —           —             —
36  agent     agent_request_email               —           —             email
37  customer  customer_report_done              —           —             हो गया
38  agent     agent_request_address             —           —             address
39  customer  customer_report_done              —           —             —
40  agent     agent_request_address             —           —             —
41  customer  customer_report_done              —           —             कर दिया
42  agent     agent_guide_apply                 —           —             —
43  customer  customer_report_done              —           —             कर दिया
44  agent     agent_present_final_offer         —           —             —
45  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call f430cd70 (transferred) — 42 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_wait                        —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_guide_open_link             —           —             —
8   customer  customer_report_done              —           —             —
9   agent     agent_guide_apply                 —           —             apply now
10  customer  customer_do_otp                   —           —             otp
11  agent     agent_request_pan                 —           —             पैन
12  customer  customer_provide_pan              —           —             pan
13  agent     agent_request_pan                 —           —             पैन
14  customer  customer_report_done              —           —             हो गया
15  agent     agent_request_personal_details    —           —             gender, date of birth, marital
16  customer  customer_report_done              —           —             हो गया
17  agent     agent_request_email               —           —             email
18  customer  customer_report_done              —           —             कर दिया
19  agent     agent_request_address             —           —             address, pincode, locality, building, house number
20  customer  customer_report_done              —           —             हो गया
21  agent     agent_request_terms_accept        —           —             terms and condition, terms
22  customer  customer_accept_terms             —           —             —
23  agent     agent_request_terms_accept        —           —             terms and condition, terms
24  customer  customer_report_done              —           —             हो गया
25  agent     agent_ask_employment_type         —           —             salaried, self-employ
26  customer  customer_state_employment_type    —           —             self employ
27  agent     agent_request_income              —           —             income
28  customer  customer_report_done              —           —             हो गया
29  agent     agent_request_business_details    —           —             business
30  customer  customer_report_done              —           —             हो गया
31  agent     agent_request_business_details    —           —             business
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_udyam               —           —             udyam
34  customer  customer_report_done              —           —             कर दिया
35  agent     agent_request_otp                 —           —             otp
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_wait                        —           —             —
38  customer  customer_do_otp                   confused    —             otp, कैसे
39  agent     agent_present_final_offer         —           —             final offer
40  customer  customer_react_to_final_offer     —           —             —
41  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call f4c4eb40 (transferred) — 48 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   customer  customer_unclear                  —           —             —
3   agent     agent_greet                       —           —             —
4   customer  customer_agree                    —           —             —
5   customer  customer_agree                    —           —             —
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_send_sms_link               —           —             sms
8   customer  customer_report_sms_received      —           —             —
9   agent     agent_guide_open_link             —           —             —
10  customer  customer_report_done              —           —             कर दिया
11  agent     agent_guide_apply                 —           —             apply now
12  customer  customer_report_done              —           —             हो गया
13  agent     agent_request_otp                 —           send_otp      otp
14  customer  customer_ask_question             —           —             मतलब
15  agent     agent_answer_query                —           —             —
16  customer  customer_acknowledge              —           —             —
17  customer  customer_request_wait             —           —             —
18  agent     agent_wait                        —           —             —
19  customer  customer_acknowledge              —           —             —
20  agent     agent_request_otp                 —           send_otp      otp
21  customer  customer_accept_terms             —           —             —
22  agent     agent_request_terms_accept        —           —             terms and condition, terms
23  customer  customer_accept_terms             —           —             —
24  agent     agent_request_terms_accept        —           —             —
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_ask_employment_type         —           —             salaried, self-employ
27  customer  customer_state_employment_type    —           —             salaried
28  agent     agent_request_income              —           —             income
29  customer  customer_report_done              —           —             हो गया
30  agent     agent_request_org_name            —           —             organization
31  agent     agent_request_org_name            —           —             organization
32  customer  customer_report_done              —           —             हो गया
33  agent     agent_request_email               —           —             email
34  customer  customer_report_done              —           —             हो गया
35  agent     agent_request_email               —           —             email
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_request_business_details    —           —             —
38  customer  customer_report_done              —           —             —
39  agent     agent_guide_apply                 —           —             —
40  customer  customer_report_done              —           —             हो गया
41  agent     agent_request_otp                 —           send_otp      otp
42  customer  customer_report_done              —           —             हो गया
43  agent     agent_present_final_offer         —           —             final offer
44  customer  customer_react_to_final_offer     —           —             —
45  agent     agent_present_final_offer         —           —             final offer
46  customer  customer_react_to_final_offer     —           —             —
47  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call f5019156 (transferred) — 80 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
3   customer  customer_agree                    —           —             —
4   agent     agent_greet                       —           —             —
5   customer  customer_agree                    —           —             —
6   agent     agent_disclose_recording          —           —             —
7   customer  customer_acknowledge              —           —             —
8   customer  customer_agree                    —           —             शुरू कर
9   agent     agent_send_sms_link               —           send_sms      sms
10  agent     agent_send_sms_link               —           —             sms
11  customer  customer_report_sms_received      —           —             —
12  agent     agent_guide_open_link             —           —             वेबसाइट, खुल गई, लिंक पर क्लिक
13  agent     agent_guide_open_link             —           —             खुल गया
14  customer  customer_report_link_opened       —           —             site खुल, खुल गई, खुल गया
15  agent     agent_guide_apply                 —           —             apply now
16  customer  customer_do_otp                   —           —             —
17  agent     agent_request_otp                 —           send_otp      otp
18  agent     agent_request_otp                 —           send_otp      otp
19  customer  customer_provide_pan              —           —             pan
20  agent     agent_request_pan                 —           —             पैन
21  customer  customer_request_wait             —           —             wait
22  agent     agent_wait                        —           —             —
23  agent     agent_request_personal_details    —           —             gender, date of birth, marital
24  agent     agent_wait                        —           —             —
25  customer  customer_ask_question             —           —             —
26  agent     agent_request_address             —           —             address, आधार
27  agent     agent_request_email               —           —             email
28  agent     agent_request_address             —           —             address, locality
29  customer  customer_provide_address          —           —             address
30  agent     agent_request_address             —           —             address
31  agent     agent_request_terms_accept        —           —             terms and condition, terms
32  customer  customer_report_address_error     —           —             —
33  agent     agent_help_address_error          —           —             —
34  customer  customer_report_address_error     —           —             leading slash
35  agent     agent_help_address_error          —           —             error
36  customer  customer_request_wait             —           —             एक second
37  agent     agent_wait                        —           —             —
38  agent     agent_request_address             —           —             address
39  customer  customer_acknowledge              —           —             —
40  customer  customer_report_address_error     —           —             red
41  agent     agent_help_address_error          —           —             —
42  agent     agent_ask_to_repeat               —           —             —
43  customer  customer_report_done              —           —             —
44  agent     agent_wait                        —           —             —
45  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक
46  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक
47  customer  customer_report_address_error     frustrated  —             नहीं हो रहा, नहीं हो
48  agent     agent_help_address_error          —           —             —
49  customer  customer_provide_address          —           —             locality, building, house number, flat
50  agent     agent_request_address             —           —             address, locality, building
51  customer  customer_ask_question             —           —             —
52  agent     agent_acknowledge                 —           —             —
53  customer  customer_report_done              —           —             हो गया
54  agent     agent_request_terms_accept        —           —             terms and condition, terms, बॉक्स चेक
55  customer  customer_state_employment_type    —           —             salaried, self employ, self employee
56  agent     agent_ask_employment_type         —           —             —
57  customer  customer_state_employment_type    —           —             self employ, self employee
58  agent     agent_request_income              —           —             income
59  agent     agent_request_business_details    —           —             business
60  agent     agent_request_business_details    —           —             business, shop
61  customer  customer_report_done              —           —             —
62  agent     agent_request_business_details    —           —             business
63  agent     agent_wait                        —           —             —
64  agent     agent_request_address             —           —             —
65  agent     agent_request_otp                 —           send_otp      otp
66  customer  customer_respond_udyam            confused    —             क्या भरूं
67  agent     agent_request_udyam               —           —             udyam
68  agent     agent_acknowledge                 —           —             —
69  customer  customer_respond_udyam            —           —             उद्यम
70  customer  customer_respond_udyam            —           —             उद्यम
71  agent     agent_offer_skip_udyam            —           —             skip
72  customer  customer_skip_udyam               —           —             skip
73  agent     agent_inform_manual_review        —           push_to_crm   manual review
74  customer  customer_agree                    —           —             —
75  agent     agent_wait                        —           —             —
76  customer  customer_react_to_final_offer     —           —             loan amount and, final and
77  customer  customer_react_to_final_offer     —           —             —
78  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
79  customer  customer_acknowledge              —           —             —
```

## Call f510bd17 (transferred) — 54 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
2   agent     agent_greet                       —           —             —
3   customer  customer_agree                    —           —             —
4   agent     agent_disclose_recording          —           —             record, training, quality
5   agent     agent_send_sms_link               —           send_sms      sms
6   agent     agent_send_sms_link               —           send_sms      sms
7   agent     agent_ask_to_repeat               —           —             फिर से कह
8   customer  customer_agree                    —           —             —
9   agent     agent_guide_open_link             —           —             खुल गया
10  customer  customer_report_link_opened       —           —             खुल गया
11  agent     agent_guide_apply                 —           —             apply now
12  agent     agent_request_otp                 —           send_otp      otp
13  agent     agent_ask_to_repeat               —           —             फिर से कह
14  customer  customer_other                    —           —             —
15  agent     agent_request_otp                 —           send_otp      otp
16  customer  customer_provide_pan              —           —             pan
17  agent     agent_request_pan                 —           —             पैन
18  agent     agent_request_personal_details    —           —             gender, date of birth, marital
19  agent     agent_request_email               —           —             email
20  agent     agent_request_address             —           —             address, locality, building, house number, flat
21  agent     agent_ask_to_repeat               —           —             —
22  customer  customer_request_wait             —           —             —
23  agent     agent_wait                        —           —             —
24  agent     agent_other                       —           —             —
25  customer  customer_provide_address          —           —             —
26  agent     agent_request_address             —           —             address
27  customer  customer_acknowledge              —           —             —
28  agent     agent_request_address             —           —             address
29  customer  customer_acknowledge              —           —             —
30  agent     agent_request_terms_accept        —           —             terms and condition, terms
31  customer  customer_acknowledge              —           —             —
32  agent     agent_request_terms_accept        —           —             terms and condition, terms
33  customer  customer_acknowledge              —           —             —
34  agent     agent_request_terms_accept        —           —             terms and condition, terms
35  agent     agent_acknowledge                 —           —             —
36  customer  customer_report_done              —           —             हो गया
37  agent     agent_ask_employment_type         —           —             salaried, self-employ
38  customer  customer_state_employment_type    —           —             self employ, self employee
39  agent     agent_request_income              —           —             income
40  customer  customer_provide_org_name         —           —             —
41  agent     agent_acknowledge                 —           —             —
42  agent     agent_request_org_name            —           —             —
43  agent     agent_request_business_details    —           —             business
44  agent     agent_request_address             —           —             —
45  customer  customer_acknowledge              —           —             —
46  agent     agent_request_address             —           —             —
47  agent     agent_request_udyam               —           —             udyam
48  customer  customer_report_done              —           —             हो गया
49  agent     agent_request_otp                 —           —             otp
50  customer  customer_report_done              —           —             हो गया
51  agent     agent_wait                        —           —             —
52  customer  customer_react_to_final_offer     —           —             —
53  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call f887a187 (transferred) — 47 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             hello
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_greet                    —           —             hello
5   agent     agent_greet                       —           —             —
6   agent     agent_ask_to_repeat               —           —             —
7   customer  customer_agree                    —           —             —
8   customer  customer_react_to_offer           —           —             —
9   agent     agent_present_offer               —           —             ₹593000, 593000
10  customer  customer_ask_query                —           —             —
11  agent     agent_answer_query                —           —             —
12  customer  customer_agree                    —           —             —
13  agent     agent_send_sms_link               —           send_sms      sms
14  agent     agent_send_sms_link               —           —             sms
15  customer  customer_report_sms_received      —           —             —
16  agent     agent_guide_open_link             —           —             खुल गया
17  customer  customer_report_link_opened       —           —             खुल गया
18  agent     agent_guide_apply                 —           —             apply now
19  agent     agent_guide_apply                 —           —             apply now
20  customer  customer_report_done              —           —             कर दिया
21  agent     agent_request_otp                 —           —             —
22  agent     agent_ask_to_repeat               —           —             —
23  customer  customer_do_otp                   —           —             otp
24  agent     agent_request_otp                 —           —             otp
25  customer  customer_report_done              —           —             कर दिया
26  agent     agent_ask_employment_type         —           —             —
27  customer  customer_request_wait             —           —             एक second
28  agent     agent_wait                        —           —             —
29  customer  customer_request_wait             —           —             एक second
30  agent     agent_wait                        —           —             —
31  customer  customer_agree                    —           —             —
32  agent     agent_ask_employment_type         —           —             salaried, self-employ
33  customer  customer_state_employment_type    —           —             —
34  agent     agent_ask_to_repeat               —           —             —
35  customer  customer_state_employment_type    —           —             —
36  agent     agent_ask_employment_type         —           —             salaried, self-employ
37  customer  customer_state_employment_type    —           —             —
38  agent     agent_request_income              —           —             income
39  agent     agent_request_org_name            —           —             —
40  agent     agent_request_org_name            —           —             organization
41  agent     agent_request_email               —           —             email
42  customer  customer_report_done              —           —             कर दिया
43  agent     agent_request_address             —           —             address, building
44  customer  customer_report_done              —           —             कर दिया
45  agent     agent_present_final_offer         —           —             final offer
46  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```

## Call f8d9819a (transferred) — 84 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_other                       —           —             —
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   customer  customer_agree                    —           —             —
5   customer  customer_query_fee                —           —             emi
6   agent     agent_explain_fee                 —           —             interest rate
7   customer  customer_query_fee                —           —             —
8   agent     agent_answer_query                —           —             —
9   customer  customer_report_sms_received      —           —             sms
10  agent     agent_send_sms_link               —           send_sms      sms
11  agent     agent_guide_open_link             —           —             —
12  customer  customer_report_link_opened       —           —             —
13  agent     agent_wait                        —           —             —
14  agent     agent_guide_apply                 —           —             apply now
15  customer  customer_report_applied           —           —             —
16  agent     agent_request_otp                 —           send_otp      otp
17  agent     agent_request_otp                 —           send_otp      otp
18  customer  customer_request_wait             —           —             रुकिए
19  agent     agent_wait                        —           —             —
20  customer  customer_report_link_opened       —           —             खुल गया
21  agent     agent_request_pan                 —           —             पैन
22  customer  customer_query_fee                confused    —             emi, कैसे
23  agent     agent_explain_fee                 —           —             interest rate
24  customer  customer_query_fee                —           —             —
25  agent     agent_request_personal_details    —           —             —
26  customer  customer_ask_question             —           —             —
27  customer  customer_ask_question             —           —             —
28  agent     agent_answer_query                —           —             —
29  agent     agent_answer_query                —           —             —
30  agent     agent_request_pan                 —           —             पैन
31  customer  customer_state_employment_type    —           —             —
32  agent     agent_request_org_name            —           —             organization
33  agent     agent_request_org_name            —           —             organization
34  agent     agent_wait                        —           —             —
35  agent     agent_request_email               —           —             email
36  agent     agent_ask_to_repeat               —           —             फिर से बता
37  customer  customer_request_wait             —           —             —
38  agent     agent_wait                        —           —             —
39  agent     agent_wait                        —           —             —
40  agent     agent_request_address             —           —             address
41  agent     agent_request_address             —           —             —
42  customer  customer_report_done              —           —             हो गया
43  customer  customer_query_fee                —           —             processing fee, emi
44  customer  customer_query_fee                —           —             —
45  agent     agent_explain_fee                 —           —             processing fee, emi, ₹2,950, ₹5,150, ₹1,40,000
46  customer  customer_query_fee                —           —             processing fee
47  agent     agent_explain_fee                 —           —             processing fee, emi, ₹2,950,, ₹1,40,000,
48  customer  customer_query_fee                —           —             emi
49  agent     agent_explain_fee                 —           —             emi, ₹5,150, ₹1,40,000
50  customer  customer_react_to_final_offer     —           —             —
51  agent     agent_present_final_offer         —           —             —
52  customer  customer_query_fee                —           —             —
53  agent     agent_explain_fee                 —           —             emi, interest rate
54  customer  customer_react_to_final_offer     —           —             final offer
55  agent     agent_present_final_offer         —           —             final offer
56  agent     agent_guide_apply                 —           —             apply now
57  customer  customer_do_otp                   —           —             —
58  agent     agent_request_otp                 —           send_otp      otp
59  agent     agent_request_otp                 —           send_otp      otp
60  agent     agent_end_call                    —           —             —
61  agent     agent_guide_apply                 —           —             apply now
62  customer  customer_ask_question             frustrated  —             कब तक
63  agent     agent_answer_query                —           —             —
64  customer  customer_query_fee                —           —             processing fee
65  customer  customer_query_fee                —           —             processing fee
66  customer  customer_query_fee                —           —             —
67  agent     agent_explain_fee                 —           —             processing fee, ₹4,248, ₹1,15,752, ₹1,20,000
68  customer  customer_query_fee                —           —             emi
69  agent     agent_explain_fee                 —           —             emi, ₹4,440
70  customer  customer_ask_question             —           —             —
71  agent     agent_answer_query                —           —             —
72  agent     agent_answer_query                —           —             —
73  customer  customer_report_applied           —           —             —
74  agent     agent_answer_query                —           —             —
75  customer  customer_request_wait             —           —             रुकिए
76  agent     agent_wait                        —           —             —
77  customer  customer_request_wait             —           —             —
78  agent     agent_wait                        —           —             —
79  agent     agent_answer_query                —           —             —
80  customer  customer_ask_question             —           —             मतलब
81  agent     agent_answer_query                —           —             —
82  customer  customer_agree                    —           —             —
83  agent     agent_transfer_to_rm              —           transfer_to_rmspecialist से connect
```

## Call f93c02d0 (transferred) — 58 turns

```
#   SPEAKER   INTENT                            SENTIMENT   TOOL          KEYWORDS
----------------------------------------------------------------------------------
0   customer  customer_greet                    —           —             hello
1   agent     agent_greet                       —           —             नमस्ते, से बात
2   customer  customer_greet                    —           —             hello
3   agent     agent_greet                       —           —             नमस्ते, बात कर रही, से बात
4   agent     agent_send_sms_link               —           send_sms      sms
5   agent     agent_guide_open_link             —           —             —
6   agent     agent_guide_apply                 —           —             apply now
7   agent     agent_request_otp                 —           send_otp      otp
8   agent     agent_ask_to_repeat               —           —             —
9   agent     agent_request_otp                 —           send_otp      otp
10  agent     agent_request_otp                 —           —             otp
11  agent     agent_request_otp                 —           —             otp
12  agent     agent_request_otp                 —           —             otp
13  customer  customer_report_done              —           —             —
14  agent     agent_request_pan                 —           —             pan
15  customer  customer_provide_pan              —           —             pan
16  agent     agent_request_pan                 —           —             pan
17  agent     agent_wait                        —           —             —
18  customer  customer_acknowledge              —           —             —
19  agent     agent_request_pan                 —           —             pan
20  agent     agent_request_personal_details    —           —             gender, date of birth, marital
21  customer  customer_request_wait             —           —             —
22  agent     agent_wait                        —           —             —
23  agent     agent_ask_to_repeat               —           —             —
24  agent     agent_request_personal_details    —           —             gender, date of birth, marital
25  agent     agent_ask_to_repeat               —           —             —
26  agent     agent_request_email               —           —             email
27  agent     agent_ask_to_repeat               —           —             —
28  customer  customer_agree                    —           —             —
29  agent     agent_request_email               —           —             email
30  customer  customer_report_done              —           —             —
31  agent     agent_request_address             —           —             address, pincode, locality, building, house number
32  customer  customer_report_done              —           —             —
33  agent     agent_request_terms_accept        —           —             terms and condition, terms
34  customer  customer_report_done              —           —             —
35  agent     agent_ask_employment_type         —           —             salaried, self-employ
36  customer  customer_state_employment_type    —           —             —
37  agent     agent_ask_employment_type         —           —             salaried, self-employ
38  agent     agent_ask_to_repeat               —           —             —
39  agent     agent_ask_employment_type         —           —             salaried, self-employ
40  customer  customer_report_done              —           —             —
41  agent     agent_request_income              —           —             —
42  customer  customer_report_done              —           —             —
43  agent     agent_request_org_name            —           —             organization
44  customer  customer_report_done              —           —             —
45  agent     agent_request_email               —           —             email
46  customer  customer_report_done              —           —             —
47  agent     agent_request_address             —           —             address, pincode
48  agent     agent_ask_to_repeat               —           —             —
49  agent     agent_guide_apply                 —           —             —
50  agent     agent_request_otp                 —           —             otp
51  agent     agent_wait                        —           —             —
52  agent     agent_request_otp                 —           —             otp
53  agent     agent_ask_to_repeat               —           —             —
54  agent     agent_request_otp                 —           —             otp
55  customer  customer_report_done              —           —             —
56  agent     agent_present_final_offer         —           —             final offer, loan amount and
57  agent     agent_transfer_to_rm              —           transfer_to_rmrelationship manager
```
