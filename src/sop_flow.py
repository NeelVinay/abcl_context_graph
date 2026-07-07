"""ABCL SOP call-flow diagram (reference-style): a FIXED procedure skeleton (decision
diamonds + labeled branches + colored terminals) with REAL call data overlaid as edge
counts. Structure = the canonical ABCL flow (from the agent DSL); numbers = the calls.

Unlike the frequency flow-tree, the shape is fixed and chronological, and paths reconverge
(a DAG, not a tree). Renders like HDFC_LOC_VoiceBot_Flow_Diagram.

  python make_sopflow.py --data mp3|txt|<dir>
"""
from __future__ import annotations

import math

# ---- node kinds -> graphviz style ----
_STYLE = {
    "start":     dict(shape="oval",    style="filled", fillcolor="#1f3b5c", fontcolor="white"),
    "success":   dict(shape="oval",    style="filled", fillcolor="#1f3b5c", fontcolor="white"),
    "close":     dict(shape="oval",    style="filled", fillcolor="#1f3b5c", fontcolor="white"),
    "escalate":  dict(shape="box",     style="rounded,filled", fillcolor="#f8d7da", color="#b02a37"),
    "step":      dict(shape="box",     style="rounded,filled", fillcolor="#dbe7f3", color="#33628f"),
    "decision":  dict(shape="hexagon", style="filled", fillcolor="#fdf0d0", color="#c99a2e"),
}

# ---- the ABCL SOP: every node (id -> (label, kind)) ----
NODES = {
    "start":       ("Call Starts", "start"),
    "greeting":    ("Greeting + Self-intro\\n(Priya, Aditya Birla Capital)", "step"),
    "d_language":  ("Can proceed in\\nHindi / English?", "decision"),
    "d_person":    ("Right person?", "decision"),
    "offer":       ("Share Pre-approved\\nLoan Offer + Consent", "step"),
    "d_interested": ("Interested?", "decision"),
    "d_query":     ("What does the\\ncustomer want to know?", "decision"),
    # specific query types (broken out from the old single "Answer Query")
    "ans_amount":  ("Answer: Loan amount", "step"),
    "ans_rate":    ("Answer: Interest rate\\n(from 10.99%)", "step"),
    "ans_higher":  ("Answer: Higher amount\\n(after process)", "step"),
    "ans_elig":    ("Answer: Eligibility / Documents", "step"),
    "ans_fee":     ("Answer: Processing fee / EMI", "step"),
    "ans_who":     ("Answer: Who's calling /\\nwhich company", "step"),
    "ans_why":     ("Answer: Why this call\\n(pre-approved offer)", "step"),
    "ans_general": ("Answer: General FAQ", "step"),
    "handle_objection": ("Handle Objection\\n(fraud / trust — reassure)", "step"),
    "d_ready":     ("Ready to apply?", "decision"),
    "sms":         ("Send SMS\\n(application link)", "step"),
    "open_link":   ("Open Link / Web Journey", "step"),
    "d_otp":       ("Link / OTP working?", "decision"),
    "login_otp":   ("Login — Mobile OTP", "step"),
    # personal details, field by field
    "pd_pan":      ("Enter PAN", "step"),
    "pd_name":     ("Name / Gender / DOB /\\nMarital status", "step"),
    "pd_email":    ("Personal Email", "step"),
    "pd_address":  ("Address + Pincode", "step"),
    "pd_terms":    ("Accept Terms & Conditions", "step"),
    "d_emptype":   ("Employment type?", "decision"),
    # salaried branch, step by step
    "sal_income":  ("Monthly Income\\n(salaried)", "step"),
    "sal_org":     ("Organization Name", "step"),
    "sal_email":   ("Official Email", "step"),
    "sal_address": ("Office Address + Pincode", "step"),
    "sal_otp":     ("Proceed — Email OTP", "step"),
    # self-employed branch, step by step
    "se_income":   ("Net Monthly Income\\n(self-employed)", "step"),
    "se_biz_name": ("Business Name", "step"),
    "se_biz_addr": ("Business Address + Pincode", "step"),
    "se_udyam":    ("Udyam Verification / Skip", "step"),
    "se_otp":      ("Proceed — Mobile OTP", "step"),
    "d_offer_vis": ("Offer visible?", "decision"),
    "final_offer": ("Final Offer\\n(amount, tenure, EMI)", "step"),
    # terminals
    "rm":          ("Transfer to\\nRelationship Manager", "success"),
    "callback":    ("Callback Scheduled", "close"),
    "closure":     ("Closure\\n(sign-off)", "close"),
    "escalate":    ("Escalate to Human\\n(full context passed)", "escalate"),
    "team_back":   ("Team will connect back", "escalate"),
}

# ---- every branch (src, dst, condition-label) ----
EDGES = [
    ("start", "greeting", ""),
    ("greeting", "d_language", ""),
    ("d_language", "closure", "other language"),
    ("d_language", "d_person", "hindi / english"),
    ("d_person", "closure", "wrong number / third party / deceased / unavailable"),
    ("d_person", "offer", "yes"),
    ("offer", "d_interested", ""),
    ("d_interested", "callback", "callback requested"),
    ("d_interested", "closure", "not interested"),
    ("d_interested", "handle_objection", "already has loan / other lender"),
    ("d_interested", "d_query", "yes / has questions"),
    # the query hub fans out to specific question types, then all feed back to "ready?"
    ("d_query", "ans_amount", "loan amount"),
    ("d_query", "ans_rate", "interest rate"),
    ("d_query", "ans_higher", "higher amount"),
    ("d_query", "ans_elig", "eligibility / docs"),
    ("d_query", "ans_fee", "fee / EMI"),
    ("d_query", "ans_who", "who's calling"),
    ("d_query", "ans_why", "why this call"),
    ("d_query", "ans_general", "general question"),
    ("d_query", "handle_objection", "fraud / trust concern"),
    ("d_query", "escalate", "talk to a person"),
    ("d_query", "d_ready", "no questions"),
    ("ans_amount", "d_ready", ""),
    ("ans_rate", "d_ready", ""),
    ("ans_higher", "d_ready", ""),
    ("ans_elig", "d_ready", ""),
    ("ans_fee", "d_ready", ""),
    ("ans_who", "d_ready", ""),
    ("ans_why", "d_ready", ""),
    ("ans_general", "d_ready", ""),
    ("handle_objection", "d_ready", "reassured"),
    ("handle_objection", "escalate", "insists on human"),
    ("d_ready", "closure", "no / not sure / will do it alone"),
    ("d_ready", "sms", "yes"),
    ("sms", "open_link", ""),
    ("open_link", "d_otp", ""),
    ("d_otp", "team_back", "tech issue (2x)"),
    ("d_otp", "login_otp", "working"),
    # personal details, in order
    ("login_otp", "pd_pan", ""),
    ("pd_pan", "pd_name", ""),
    ("pd_name", "pd_email", ""),
    ("pd_email", "pd_address", ""),
    ("pd_address", "pd_terms", ""),
    ("pd_terms", "d_emptype", ""),
    # salaried branch
    ("d_emptype", "sal_income", "salaried"),
    ("sal_income", "sal_org", ""),
    ("sal_org", "sal_email", ""),
    ("sal_email", "sal_address", ""),
    ("sal_address", "sal_otp", ""),
    ("sal_otp", "d_offer_vis", ""),
    # self-employed branch
    ("d_emptype", "se_income", "self-employed"),
    ("se_income", "se_biz_name", ""),
    ("se_biz_name", "se_biz_addr", ""),
    ("se_biz_addr", "se_udyam", ""),
    ("se_udyam", "se_otp", ""),
    ("se_otp", "d_offer_vis", ""),
    ("d_offer_vis", "escalate", "not visible / tech issue"),
    ("d_offer_vis", "final_offer", "visible"),
    ("final_offer", "rm", ""),
]


# ---- EXEC view: collapse the granular form fields into grouped boxes ----
COLLAPSE = {
    "pd_pan": "personal", "pd_name": "personal", "pd_email": "personal",
    "pd_address": "personal", "pd_terms": "personal",
    "sal_income": "sal_details", "sal_org": "sal_details", "sal_email": "sal_details",
    "sal_address": "sal_details", "sal_otp": "sal_details",
    "se_income": "se_details", "se_biz_name": "se_details", "se_biz_addr": "se_details",
    "se_udyam": "se_details", "se_otp": "se_details",
}
GROUP_NODES = {
    "personal":    ("Personal Details\\n(PAN · DOB · email · address · terms)", "step"),
    "sal_details": ("Salaried Details\\n(income · employer · OTP)", "step"),
    "se_details":  ("Self-employed Details\\n(income · business · Udyam · OTP)", "step"),
}


def _bases(call):
    return {t.get("base_intent") for t in call.get("turns", [])}


# specific query types detected from the CUSTOMER's question turns (priority order — first match wins)
QUERY_TYPES = [
    ("ans_why",    ["apply nahi", "अप्लाई नहीं", "apply nhi", "maine kab", "मैंने कब",
                    "did not apply", "why call", "क्यों call", "kaisa call"]),
    ("ans_who",    ["kaun bol", "कौन बोल", "who are you", "aap kaun", "आप कौन",
                    "konsi company", "कौन सी company", "kisne call", "which company"]),
    ("ans_higher", ["zyada loan", "ज़्यादा loan", "aur amount", "और amount", "badha",
                    "increase", "higher", "zyada mil"]),
    ("ans_rate",   ["rate", "byaj", "ब्याज", "interest", "प्रतिशत", "percent"]),
    ("ans_fee",    ["fee", "emi", "किश्त", "charges", "processing", "प्रोसेसिंग"]),
    ("ans_elig",   ["eligib", "document", "दस्तावेज़", "papers", "kya chahiye", "क्या चाहिए",
                    "kya dena", "kagaz"]),
    ("ans_amount", ["kitna loan", "कितना loan", "kitna amount", "कितना amount", "loan amount",
                    "amount kitna", "kitne ka loan"]),
]


def _query_node(call):
    """Which specific answer node this call's customer questions map to (or None)."""
    text = " ".join(t["text"] for t in call.get("turns", [])
                    if t.get("speaker") == "customer").lower()
    for node, kws in QUERY_TYPES:
        if any(k in text for k in kws):
            return node
    return None


def map_call_path(call) -> list[str]:
    """Walk a single call through the SOP, choosing branches from its disposition +
    which intents it actually reached + outcome. Returns the node-id sequence traversed."""
    disp = call.get("disposition", "none")
    b = _bases(call)
    outcome = call.get("outcome")
    p = ["start", "greeting", "d_language"]
    if disp == "language_barrier":
        return p + ["closure"]
    p += ["d_person"]
    if disp == "wrong_person":
        return p + ["closure"]
    p += ["offer", "d_interested"]
    if disp == "callback_requested":
        return p + ["callback"]
    if disp == "not_interested":
        return p + ["closure"]
    if disp == "already_has_loan":
        p += ["handle_objection"]
    p += ["d_query"]
    if disp == "security_concern" or "reassure_trust" in b:
        p += ["handle_objection"]
    else:
        q = _query_node(call)                       # specific query type, if any
        if q:
            p += [q]
        elif "answer_query" in b or "ask_question" in b:
            p += ["ans_general"]
    p += ["d_ready"]
    if "send_sms_link" not in b:            # never proceeded into the application
        return p + ["closure"]
    p += ["sms", "open_link", "d_otp"]
    if disp == "tech_or_otp_issue":
        return p + ["team_back"]
    p += ["login_otp"]
    reached_personal = "enter_pan" in b or "personal_details" in b
    if not reached_personal:
        # past OTP but no form data — either handed off or dropped
        return p + (["rm"] if (outcome == "transferred" or "transfer_to_rm" in b) else [])
    # walk the full personal-details field sequence (calls that reach the form go through it)
    p += ["pd_pan", "pd_name", "pd_email", "pd_address", "pd_terms", "d_emptype"]
    self_employed = "business_details" in b or "udyam_verification" in b
    reached_emp = self_employed or "employment_type" in b or "enter_income" in b
    if reached_emp:
        p += (["se_income", "se_biz_name", "se_biz_addr", "se_udyam", "se_otp"]
              if self_employed else
              ["sal_income", "sal_org", "sal_email", "sal_address", "sal_otp"])
        p += ["d_offer_vis"]
        if "final_offer" in b or outcome == "transferred":
            p += ["final_offer"]
    if outcome == "transferred" or "transfer_to_rm" in b:
        p += ["rm"]
    return p


def build_edge_counts(calls) -> dict:
    """How many calls traversed each SOP edge."""
    counts = {}
    for c in calls:
        path = map_call_path(c)
        for a, b in zip(path, path[1:]):
            counts[(a, b)] = counts.get((a, b), 0) + 1
    return counts


def _exec_edges(counts: dict) -> dict:
    """Collapse EDGES to exec level. Returns {(esrc,edst): [count, cond]}."""
    data: dict = {}
    for src, dst, cond in EDGES:
        esrc = COLLAPSE.get(src, src)
        edst = COLLAPSE.get(dst, dst)
        if esrc == edst:
            continue  # internal to a collapsed group — skip
        c = counts.get((src, dst), 0)
        key = (esrc, edst)
        if key not in data:
            data[key] = [0, cond]
        data[key][0] += c
    return data


def _greedy_path(active: dict) -> set:
    """Greedy walk from 'start': at each step follow the heaviest outgoing edge."""
    outgoing: dict = {}
    for (esrc, edst), (c, _) in active.items():
        outgoing.setdefault(esrc, []).append((edst, c))
    path_edges: set = set()
    cur, visited = "start", {"start"}
    while cur in outgoing:
        nexts = [(n, c) for n, c in outgoing[cur] if n not in visited]
        if not nexts:
            break
        best = max(nexts, key=lambda x: x[1])
        path_edges.add((cur, best[0]))
        cur = best[0]
        visited.add(cur)
    return path_edges


def render(calls, out_path_no_ext: str) -> str | None:
    """Draw the fixed SOP skeleton with real per-edge call counts overlaid."""
    try:
        from graphviz import Digraph
    except Exception as e:  # noqa: BLE001
        print(f"[sop] graphviz not available ({e})")
        return None
    counts = build_edge_counts(calls)
    total = len(calls)
    max_c = max(counts.values(), default=1)

    dot = Digraph("abcl_sop", format="png")
    dot.attr(rankdir="TB", splines="polyline", nodesep="0.5", ranksep="0.7")
    dot.attr("node", fontname="Helvetica", fontsize="10", margin="0.12,0.07")
    dot.attr("edge", fontname="Helvetica", fontsize="8", color="#5b6b7a")

    # only draw nodes reachable in the model (all of them) — fixed skeleton
    for nid, (label, kind) in NODES.items():
        dot.node(nid, label, **_STYLE[kind])

    for src, dst, cond in EDGES:
        c = counts.get((src, dst), 0)
        # label = branch condition + call count; thickness/colour scale with volume
        parts = [p for p in (cond, f"[{c}]" if total else "") if p]
        lbl = "  ".join(parts)
        pw = 1 + 3.0 * math.log1p(c) / math.log1p(max_c) if c else 0.8
        color = "#2e7d32" if c >= max_c * 0.5 and c > 0 else ("#5b6b7a" if c else "#c9ced3")
        dot.edge(src, dst, label=lbl, penwidth=f"{pw:.2f}", color=color,
                 fontcolor="#333333" if c else "#aaaaaa")
    try:
        dot.render(out_path_no_ext, cleanup=True)
        return f"{out_path_no_ext}.png"
    except Exception as e:  # noqa: BLE001
        print(f"[sop] render failed ({e})")
        return None


# Shortened branch conditions for exec view
_COND_SHORT = {
    "wrong number / third party / deceased / unavailable": "wrong person",
    "already has loan / other lender": "already has loan",
    "yes / has questions": "has questions",
    "no / not sure / will do it alone": "not proceeding",
    "fraud / trust concern": "fraud concern",
    "not visible / tech issue": "tech issue",
    "talk to a person": "to person",
    "tech issue (2x)": "tech issue",
    "hindi / english": "hindi / eng",
}

# Decision nodes — edges leaving these get a condition label; linear edges get count only
_DECISION_NODES = {
    "d_language", "d_person", "d_interested", "d_query",
    "d_ready", "d_otp", "d_emptype", "d_offer_vis", "handle_objection",
}

# Answer / fan-out nodes that should sit on the same horizontal rank
_ANSWER_NODES = {"ans_amount", "ans_rate", "ans_fee", "ans_elig",
                 "ans_who", "ans_why", "ans_general"}


def render_exec(calls, out_path_no_ext: str) -> str | None:
    """C-suite exec view: collapsed form steps, zero-count branches hidden, percentages."""
    import datetime
    try:
        from graphviz import Digraph
    except Exception as e:  # noqa: BLE001
        print(f"[sop] graphviz not available ({e})")
        return None

    counts = build_edge_counts(calls)
    total = len(calls)

    all_exec = _exec_edges(counts)
    active = {k: v for k, v in all_exec.items() if v[0] > 0}
    if not active:
        print("[sop] no active edges — nothing to render")
        return None

    main_edges = _greedy_path(active)

    active_nodes: set = set()
    for esrc, edst in active:
        active_nodes.update([esrc, edst])
    active_nodes.add("start")

    max_c = max(v[0] for v in active.values())
    month_year = datetime.date.today().strftime("%B %Y")

    dot = Digraph("abcl_sop_exec", format="png")
    dot.attr(
        rankdir="TB",
        splines="ortho",        # right-angle routing — no diagonals, no crossings
        nodesep="0.7",          # compact horizontal: prevents wide side-to-side spread
        ranksep="0.9",
        label=f"ABCL Loan Application — Call Flow\\n{total} calls  •  {month_year}",
        labelloc="t", fontsize="22", fontname="Helvetica-Bold",
        bgcolor="white",
        pad="0.6",
        dpi="150",
    )
    dot.attr("node", fontname="Helvetica", fontsize="13", margin="0.28,0.16",
             width="2.6", penwidth="1.5")
    dot.attr("edge", fontname="Helvetica", fontsize="9", arrowsize="0.9")

    # ── draw nodes ───────────────────────────────────────────────────────────
    node_lookup = {**NODES, **GROUP_NODES}
    for nid in sorted(active_nodes):
        if nid not in node_lookup:
            continue
        label, kind = node_lookup[nid]
        dot.node(nid, label, **_STYLE[kind])

    # ── rank=same: parallel fan-out answer nodes ─────────────────────────────
    answer_present = _ANSWER_NODES & active_nodes
    if len(answer_present) > 1:
        with dot.subgraph() as s:
            s.attr(rank="same")
            for n in sorted(answer_present):
                s.node(n)

    # ── rank=same: parallel employment-detail branches ───────────────────────
    if {"sal_details", "se_details"} <= active_nodes:
        with dot.subgraph() as s:
            s.attr(rank="same")
            s.node("sal_details")
            s.node("se_details")

    # ── draw edges ───────────────────────────────────────────────────────────
    for (esrc, edst), (c, cond) in active.items():
        pct = f"{100 * c / total:.0f}%" if total else ""
        count_lbl = f"{c} calls ({pct})"

        is_main = (esrc, edst) in main_edges
        is_decision = esrc in _DECISION_NODES

        # Single label at edge midpoint. Graphviz routes the arrow line AROUND
        # this bounding box automatically — it doesn't do that for head/tail labels,
        # which is why those cut through the arrow.
        lbl = f"{cond}\\n{count_lbl}" if (is_decision and cond) else count_lbl

        if is_main:
            dot.edge(esrc, edst, label=lbl,
                     penwidth="3.5", color="#1a6b2d", fontcolor="#1a6b2d")
        else:
            pw = 1.2 + 2.5 * math.log1p(c) / math.log1p(max_c)
            dot.edge(esrc, edst, label=lbl,
                     penwidth=f"{pw:.2f}", color="#4a6b8a", fontcolor="#555555")

    try:
        dot.render(out_path_no_ext, cleanup=True)
        return f"{out_path_no_ext}.png"
    except Exception as e:  # noqa: BLE001
        print(f"[sop] render_exec failed ({e})")
        return None
