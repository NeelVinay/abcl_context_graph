# ABCL Call Context-Graph Report

Calls analyzed: **115** · intents: **15** · transitions: **101**
_(counts are per-turn occurrences across all calls, not number of calls)_

## 1. Keywords by intent (the signal words)

- **agent_investigate_explain** (255x): justdial, customer, com, support, good, call
- **customer_acknowledge** (149x): justdial, दिये, थी।, करा, साथ।, see
- **customer_complaint** (143x): customer, support, ticket, area, location, call
- **customer_other** (123x): talking, machine, out, पाएं।, justdial, lead
- **agent_other** (93x): justdial, lead, number, one, second, problem
- **agent_greet** (82x): customer, good, service, department, day, name
- **agent_acknowledge** (51x): दिये, साथ।, बड़, justdial, customer, call
- **customer_greet** (48x): justdial, customer, com, support, good, service
- **agent_acknowledge_complaint** (44x): forward, ऊपर, leave, area, definitely, बाहर
- **customer_ask_question** (44x): लीड, चेक, ना।, इसको, ऐसा, number
- **agent_raise_request** (43x): justdial, call, business, feedback, rating, lead
- **agent_ask** (36x): बोला, just, tell, talking, ticket, department
- **customer_respond** (31x): contract, request, share, चेक, search, customer

## 2. Customer sentiment by intent

- **customer_acknowledge**: happy:2 · frustrated:1
- **customer_complaint**: frustrated:8 · distrustful:3 · confused:1
- **customer_other**: frustrated:2
- **customer_ask_question**: confused:1
- **customer_respond**: frustrated:2 · confused:1

## 3. Tool / API calls detected

_Inferred from the agent's words (a proxy, not real tool logs). Count = turns where the tool actually fired._

_(no tool calls detected)_
