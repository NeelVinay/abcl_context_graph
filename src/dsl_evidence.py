"""Assemble the factual evidence pack about a client's real calls.

Purely mechanical — no interpretation, no LLM. This is what gets handed to the
model in the autonomous run so its analysis is grounded in real numbers and real
quotes rather than plausible-sounding invention.

Two principles that shaped this:

  * **Every number carries its n and its significance.** During planning, three
    findings looked like signal and were not: `network` (4/72 vs 2/157, Fisher
    p=0.08), the rate/fee objection (customers who raise it complete BETTER than
    baseline — 22.7% vs 31.4% incomplete), and a substring scan suggesting 19
    "car" mentions that word-boundary matching showed to be 0. If the pack states
    bare counts, a reader (human or model) will over-read them. So prevalence
    numbers ship with p-values and the traps are named explicitly.

  * **Unflattering evidence is included.** Of the 33 calls that die before the
    SMS, several are voicemail / driving / a Tamil-only speaker / audio failure —
    not persuasion problems at all. Filtering to the addressable subset would
    bias the analysis toward "this is all fixable with better copy". Sorting real
    opportunities from noise is exactly the judgment being asked for.
"""
from __future__ import annotations

import json
import re
from collections import Counter

STAGE_ORDER = ["pre_sms", "sms_sent", "link_opened", "otp_stage", "form_deep"]


def call_stage(call: dict) -> str:
    """How far into the journey did this call actually get? Derived from the
    tool calls and intent labels already on the turns (validated by hand against
    the real corpus during planning)."""
    tools = [t.get("tool") for t in call["turns"] if t.get("tool")]
    intents = [t.get("intent", "") or "" for t in call["turns"]]
    if any("udyam" in i or "employment" in i or "profession" in i for i in intents):
        return "form_deep"
    if any("otp" in i for i in intents):
        return "otp_stage"
    if any("report_link" in i or "link_opened" in i for i in intents):
        return "link_opened"
    if any("sms" in str(x).lower() for x in tools):
        return "sms_sent"
    return "pre_sms"


def _fisher(a: int, n_a: int, b: int, n_b: int):
    """p-value for 'is rate a/n_a different from b/n_b', or None if scipy absent."""
    try:
        from scipy.stats import fisher_exact
        _, p = fisher_exact([[a, n_a - a], [b, n_b - b]])
        return p
    except Exception:  # noqa: BLE001
        return None


def stage_breakdown(calls: list) -> list:
    rows = []
    for stage in STAGE_ORDER:
        sub = [c for c in calls if call_stage(c) == stage]
        if not sub:
            continue
        inc = sum(1 for c in sub if c["outcome"] == "incomplete")
        rows.append({
            "stage": stage, "calls": len(sub), "incomplete": inc,
            "incomplete_rate": round(inc / len(sub), 3),
        })
    return rows


def dropoff_quotes(calls: list, stage: str, limit: int = 15) -> list:
    """The last thing the customer actually said before an incomplete call at this
    stage. Verbatim — this is the raw material for understanding *why*."""
    out = []
    for c in calls:
        if c["outcome"] != "incomplete" or call_stage(c) != stage:
            continue
        cust = [t for t in c["turns"] if t.get("speaker") == "customer"]
        if cust:
            out.append({"call_id": c["call_id"], "text": cust[-1]["text"][:200],
                        "intent": cust[-1].get("intent", "")})
        if len(out) >= limit:
            break
    return out


def theme_prevalence(calls: list, themes: dict) -> list:
    """For each theme regex: how many calls mention it, their incomplete rate vs
    baseline, and the Fisher p-value. p is what separates signal from the traps."""
    n_all = len(calls)
    base_inc = sum(1 for c in calls if c["outcome"] == "incomplete")
    rows = []
    for name, pattern in themes.items():
        p = re.compile(pattern, re.IGNORECASE)
        sub = [c for c in calls
               if any(t.get("speaker") == "customer" and p.search(t.get("text", ""))
                      for t in c["turns"])]
        if not sub:
            continue
        inc = sum(1 for c in sub if c["outcome"] == "incomplete")
        pv = _fisher(inc, len(sub), base_inc - inc, n_all - len(sub))
        rows.append({
            "theme": name, "calls": len(sub), "incomplete": inc,
            "incomplete_rate": round(inc / len(sub), 3),
            "baseline_rate": round(base_inc / n_all, 3),
            "p_value": round(pv, 4) if pv is not None else None,
            "significant": (pv is not None and pv < 0.05),
        })
    rows.sort(key=lambda r: -r["calls"])
    return rows


DEFAULT_THEMES = {
    "not_interested": r"नहीं चाहिए|interested नहीं|नहीं लेना|मत करो|मना कर|नहीं करना",
    "already_has_loan": r"पहले से loan|already.*loan|loan चल रहा|EMI चल",
    "busy_or_later": r"busy|अभी नहीं|बाद में|later|time नहीं|drive कर",
    "tech_issue": r"network|problem|नहीं खुल|open नहीं|link नहीं|error",
    "trust_doubt": r"fraud|scam|फ्रॉड|genuine|असली|कैसे भरोसा|bot|automatic",
    "rate_objection": r"ब्याज.*ज़्यादा|interest.*ज़्यादा|बहुत ज़्यादा|महंगा|rate.*high",
    "wants_reason": r"क्यों|reason|details चाहिए|जानकारी चाहिए|कैसे|बताइए",
    "eligibility_doubt": r"cibil|civil score|eligib|score कम|credit",
    "language_mismatch": r"तमिल|tamil|telugu|कन्नड़|marathi|बंगाली|हिंदी नहीं",
    "unreachable": r"voicemail|not available|switched off|call.*forwarded",
}


# Customer turns that are QUESTIONS or OBJECTIONS — the raw material for writing
# responses. Deliberately NOT significance-gated: "do customers say this?" is a
# descriptive fact needing only a count, while "does saying this predict a lost
# call?" is a causal claim needing a p-value. An earlier version gated both the
# same way, and since nothing in a 229-call corpus reaches p<0.05, that silently
# forbade the model from using customer speech at all — it fell back to writing
# generic funnel copy. Answering a common objection well is worth doing whether
# or not raising it correlates with dropping off.
_VOICE_INTENTS = {
    "customer_ask_question", "customer_query_fee", "customer_express_distrust",
    "customer_ask_query", "customer_react_to_offer", "customer_react_to_final_offer",
}

VOICE_THEMES = {
    "cost_and_terms": r"interest|ब्याज|rate|EMI|processing fee|कितना|charge|percent|महंगा",
    "why_calling": r"क्यों|reason|किस लिए|कैसे मिला|कहाँ से|number कहां|कहां से मिला",
    "eligibility_doubt": r"cibil|civil score|eligib|score|credit|मिलेगा क्या|approve होगा",
    "trust_or_fraud": r"fraud|scam|फ्रॉड|fake|विश्वास|भरोसा|genuine|असली|सही है ना",
    "is_it_a_bot": r"\bAI\b|computer|इंसान|robot|automatic|मशीन",
    "already_engaged": r"पहले से|already|चल रहा|कर लिया|apply कर दिया|हो गया है",
    "amount_expectation": r"ज़्यादा चाहिए|और मिलेगा|कम है|इतना ही|बढ़ा|top up",
    "wants_time": r"बाद में|later|busy|अभी नहीं|कल|शाम को|time नहीं",
    "process_mechanics": r"कैसे करना|क्या करना|कहाँ click|समझ नहीं आया|कौन सा|कहां डालना",
}


def customer_voice(calls: list, min_calls: int = 3, per_theme: int = 8) -> list:
    """What customers actually SAY, grouped by theme, with verbatim quotes.

    Counted over distinct calls (not turns) so one talkative caller can't invent
    a theme — the same >=min_calls recurrence guard used everywhere else in this
    pipeline, which doubles as a PII guard."""
    out = []
    for theme, pattern in VOICE_THEMES.items():
        rx = re.compile(pattern, re.IGNORECASE)
        quotes, call_ids = [], set()
        for c in calls:
            hit = None
            for t in c["turns"]:
                if t.get("speaker") != "customer":
                    continue
                text = t.get("text", "")
                # a question/objection turn, or any turn matching the theme
                if not rx.search(text):
                    continue
                if t.get("intent") in _VOICE_INTENTS or "?" in text:
                    hit = text
                    break
            if hit:
                call_ids.add(c["call_id"])
                if len(quotes) < per_theme:
                    quotes.append({"call_id": c["call_id"], "text": hit[:180]})
        if len(call_ids) >= min_calls:
            out.append({
                "theme": theme, "calls": len(call_ids),
                "share_of_corpus": round(len(call_ids) / max(len(calls), 1), 3),
                "quotes": quotes,
            })
    out.sort(key=lambda r: -r["calls"])
    return out


def graph_facts(calls: list, top: int = 10) -> dict:
    """Read the actual context graph (src/merge.build_master) rather than
    recomputing a weaker parallel analysis.

    The graph is the artifact this whole project produces: nodes are intents
    carrying real counts, keywords and sentiment; edges are observed transitions
    carrying counts and transition_prob. It knows things a stage-bucket heuristic
    cannot — e.g. which intent most often immediately precedes the call ENDING,
    and what the agent's own turn was right before that."""
    try:
        from src import analyze, merge
        import config as _cfg
    except Exception:  # noqa: BLE001
        return {}
    g = merge.build_master(calls)

    drop = analyze.drop_off_nodes(g, top)
    # for each drop-off node, what typically LED here — the turn before the call died
    inbound = {}
    for node, _cnt in drop:
        preds = sorted(
            ((a, d["count"]) for a, _b, d in g.in_edges(node, data=True)
             if a != _cfg.START),
            key=lambda e: -e[1])[:3]
        inbound[node] = preds

    sentiment = {}
    for n, data in g.nodes(data=True):
        s = {k: v for k, v in dict(data.get("sentiments", {})).items() if v}
        if s:
            sentiment[n] = {"count": data.get("count", 0), "sentiments": s,
                            "keywords": (data.get("keywords") or [])[:6]}

    return {
        "nodes": g.number_of_nodes(), "edges": g.number_of_edges(),
        "drop_off": [{"intent": n, "calls_ended_here": c,
                      "usually_preceded_by": inbound.get(n, [])} for n, c in drop],
        "top_transitions": [{"from": a, "to": b, "count": c}
                            for a, b, c in analyze.top_transitions(g, top)],
        "negative_sentiment_nodes": dict(
            sorted(sentiment.items(),
                   key=lambda kv: -sum(v for k, v in kv[1]["sentiments"].items()
                                       if k in ("frustrated", "confused", "skeptical")))[:8]),
    }


def build_pack(calls: list, dsl, client_key: str) -> dict:
    """The full factual picture handed to the model."""
    n = len(calls)
    outcomes = Counter(c["outcome"] for c in calls)
    stages = stage_breakdown(calls)
    worst = sorted(stages, key=lambda r: -r["incomplete_rate"])[:3]

    med_inc = sorted(len(c["turns"]) for c in calls if c["outcome"] == "incomplete")
    med_ok = sorted(len(c["turns"]) for c in calls if c["outcome"] != "incomplete")

    return {
        "corpus": {
            "total_calls": n,
            "outcomes": dict(outcomes),
            "median_turns_incomplete": med_inc[len(med_inc) // 2] if med_inc else None,
            "median_turns_successful": med_ok[len(med_ok) // 2] if med_ok else None,
        },
        "stage_breakdown": stages,
        "quotes_by_stage": {
            r["stage"]: dropoff_quotes(calls, r["stage"]) for r in worst
        },
        "theme_prevalence": theme_prevalence(calls, DEFAULT_THEMES),
        "customer_voice": customer_voice(calls),
        "graph": graph_facts(calls),
        "known_traps": [
            "The rate/fee objection LOOKS like a loss driver but is not: customers "
            "who raise it complete BETTER than baseline (22.7% incomplete vs 31.4%). "
            "This limits what you may CLAIM about cause — it does NOT mean you should "
            "leave the question poorly answered. It is the single most common thing "
            "customers ask about; answer it well, just don't justify the change by "
            "saying it causes drop-off.",
            "'network' correlates with drop-off but NOT significantly (4/72 vs "
            "2/157, Fisher p=0.08). Don't claim it as a cause.",
            "A substring scan suggested 19 mentions of 'car' as a purchase motive; "
            "word-boundary matching found 0. There are NO genuine life-event or "
            "purchase-motive mentions anywhere in this corpus.",
        ],
        "data_limitations": [
            "No timestamps exist on any call — only call_id, language, outcome, "
            "turns. Any trigger based on date, season, festival, time-of-day, or "
            "salary cycle is IMPOSSIBLE to detect or gate on. Do not propose one.",
            "session{} variables are injected by the caller at call time. You may "
            "only gate on variables that ALREADY exist in the session{} block.",
        ],
        "existing_intents": sorted(dsl.intents.keys()),
        "session_vars": _session_vars(dsl),
    }


def _session_vars(dsl) -> list:
    m = re.search(r"session\s*\{(.*?)\n\s*\}", dsl.text, re.S)
    if not m:
        return []
    return re.findall(r"^\s*(\w+)\s*:", m.group(1), re.M)


def render_pack(pack: dict) -> str:
    """Compact text form for the prompt — JSON is token-hungry for nested quotes."""
    L = []
    c = pack["corpus"]
    L.append(f"CORPUS: {c['total_calls']} calls, outcomes={c['outcomes']}")
    L.append(f"Median turns: incomplete={c['median_turns_incomplete']}, "
             f"successful={c['median_turns_successful']}")
    L.append("")
    L.append("STAGE BREAKDOWN (where calls die):")
    for r in pack["stage_breakdown"]:
        L.append(f"  {r['stage']:12s} {r['incomplete']:3d}/{r['calls']:3d} incomplete "
                 f"= {r['incomplete_rate']:.1%}")
    gf = pack.get("graph") or {}
    if gf:
        L.append("")
        L.append("=" * 70)
        L.append(f"CONTEXT GRAPH — {gf['nodes']} intent nodes, {gf['edges']} observed")
        L.append("transitions, built from every call. This is the real conversation")
        L.append("structure, not a summary.")
        L.append("=" * 70)
        L.append("\nWHERE CALLS ACTUALLY END (intent immediately before the call stops,")
        L.append("with what usually led into it):")
        for r in gf["drop_off"]:
            pre = ", ".join(f"{a} ({c})" for a, c in r["usually_preceded_by"]) or "—"
            L.append(f"  {r['calls_ended_here']:4d} calls end at [{r['intent']}]")
            L.append(f"        reached from: {pre}")
        L.append("\nMOST COMMON TRANSITIONS (how conversations actually move):")
        for t in gf["top_transitions"]:
            L.append(f"  {t['count']:4d}  {t['from']} -> {t['to']}")
        L.append("\nINTENTS CARRYING NEGATIVE SENTIMENT (frustrated/confused/skeptical),")
        L.append("with the keywords the graph associates with them:")
        for n, v in gf["negative_sentiment_nodes"].items():
            L.append(f"  [{n}] n={v['count']} {v['sentiments']} kw={v['keywords']}")

    L.append("")
    L.append("=" * 70)
    L.append("WHAT CUSTOMERS ACTUALLY SAY — grouped by theme, verbatim, counted by")
    L.append("distinct calls. THIS IS YOUR PRIMARY MATERIAL for writing responses.")
    L.append("These counts are descriptive facts, not causal claims — they do not")
    L.append("need a p-value. If customers keep asking something, the agent should")
    L.append("have a good answer for it.")
    L.append("=" * 70)
    for r in pack.get("customer_voice", []):
        L.append(f"\n[{r['theme']}] — {r['calls']} calls ({r['share_of_corpus']:.0%} of corpus)")
        for q in r["quotes"]:
            L.append(f"   \"{q['text']}\"")
    L.append("")
    L.append("THEME PREVALENCE — does raising a theme PREDICT a lost call? This is a")
    L.append("separate, causal question and it IS significance-gated. Use it only to")
    L.append("decide what NOT to claim about cause; do NOT use it to decide whether")
    L.append("to answer a customer question. A theme can be worth answering well")
    L.append("even when raising it does not predict dropping off.")
    for r in pack["theme_prevalence"]:
        sig = "SIGNIFICANT" if r["significant"] else "not significant"
        L.append(f"  {r['theme']:18s} n={r['calls']:3d}  {r['incomplete_rate']:.1%} "
                 f"vs {r['baseline_rate']:.1%} baseline  p={r['p_value']}  [{sig}]")
    L.append("")
    for stage, quotes in pack["quotes_by_stage"].items():
        L.append(f"VERBATIM last customer turns before dropping at [{stage}]:")
        for q in quotes:
            L.append(f"  - ({q['intent']}) {q['text']}")
        L.append("")
    L.append("KNOWN TRAPS — correlations that look real but are not:")
    for t in pack["known_traps"]:
        L.append(f"  ! {t}")
    L.append("")
    L.append("HARD DATA LIMITATIONS:")
    for t in pack["data_limitations"]:
        L.append(f"  ! {t}")
    L.append("")
    L.append(f"EXISTING INTENTS: {', '.join(pack['existing_intents'])}")
    L.append(f"EXISTING session{{}} VARIABLES (the only gateable ones): "
             f"{', '.join(pack['session_vars'])}")
    return "\n".join(L)
