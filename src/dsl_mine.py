"""Find real customer phrases the DSL prompt currently handles poorly, and rank
them for human review. This is the "identify commonly-said words and phrases"
half of the automated improvement loop — src/dsl_fix.py turns an ACCEPTED item
into an actual edit; nothing here writes to the prompt.

Two genuinely different mechanisms, kept separate because they were validated
separately and have different reliability:

  mine_anchor_gaps()        Corpus-frequency words missing from an EXISTING
                             intent's anchors. Reuses extract.build_keyword_vocab
                             (the same >=2-call document-frequency PII guard used
                             everywhere else in this pipeline) plus a cross-intent
                             lift filter so a domain-generic word ("number",
                             "loan") doesn't qualify just because it's frequent.
                             Only runs against dsl_audit.INTENT_ALIASES entries —
                             i.e. only intents already verified (by reading real
                             samples, not assumed) to correspond to one real
                             observed label. High confidence; auto-eligible.

  mine_uncovered_clusters()  Real customer turns that don't confidently match ANY
                             existing intent — margin-gated (best score AND the
                             gap to the runner-up), then clustered. This is what
                             a genuinely new intent looks like in the data.
                             Always propose-only: naming the intent and writing
                             its answer needs a person.

Both were measured, not assumed. See src/dsl_audit.py's module docstring and the
plan for the calibration evidence (argmax alone is 6/12 on real data; the margin
gate is what makes it usable at high precision / lower recall).
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

import config
from src import dsl_audit, dsl_parse

_WORD_RE = re.compile(r"[a-zA-Zऀ-ॣ]+")
MARGIN_DELTA = 0.10     # best-vs-runner-up gap required to trust an assignment
MATCH_FLOOR = 0.45      # below this, even an unopposed match isn't trusted

# A candidate word's rate INSIDE the target intent's calls vs. the overall corpus.
# Deliberately a light sanity floor (>=1.0, "at least as common in-bucket as
# everywhere else"), not a strict discriminativeness bar. Measured directly on
# real data: for a genuinely rare/specialized intent (query_fee), a 2.0x+ bar is
# right and achievable. For a DOMINANT, pervasive intent like `affirm` it is not —
# words like "बोलिए"/"बोलो" are affirm's natural vocabulary AND are also common
# throughout the whole corpus, because affirm-type language (yes/go ahead/ok) is
# woven through nearly every call regardless of topic. Tested directly: "बोलो"
# scored 0.83x (25/168 calls in-bucket vs 41/229 overall) — BELOW baseline, a
# real reason to distrust it as an affirm-specific signal despite being frequent
# in absolute terms. A 2.0x requirement would silently return zero candidates for
# every dominant intent, not because there's nothing to find, but because the
# bar doesn't fit that shape of intent. 1.1 filters genuinely anti-correlated
# words while still surfacing real candidates for both intent shapes.
MIN_LIFT = 1.1

# Spelled-out numbers, English and Hinglish, both scripts. The digit-run filter in
# _shape_ok only blocks numeric digits; a word like "four" or "चार" passes it
# cleanly and is a near-miss for anchor gaps specifically — caught on a real run
# ("Four? जी बोलिए." got flagged as a repeat_request anchor candidate purely from
# co-occurring near "जी बोलिए" a couple of times). Spelled numbers are almost
# always a misheard digit (phone number, OTP, amount), never genuine intent
# signal, so they're excluded from anchor-gap candidates specifically (not from
# uncovered-cluster mining, which is human-reviewed anyway).
_NUMBER_WORDS = {
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "zero", "hundred", "thousand", "lakh", "crore",
    "ek", "do", "teen", "char", "paanch", "panch", "chhe", "che", "saat", "aath",
    "nau", "das", "sau", "hazar", "hazaar",
    "एक", "दो", "तीन", "चार", "पांच", "छह", "सात", "आठ", "नौ", "दस", "सौ", "हज़ार", "हजार",
}


@dataclass
class AnchorGap:
    intent: str
    word: str
    call_count: int
    lift: float
    examples: list = field(default_factory=list)   # verbatim turn texts

    @property
    def decision_key(self) -> str:
        return f"anchor_gap:{self.intent}:{self.word.lower()}"

    @property
    def volume(self) -> int:
        return self.call_count

    @property
    def confidence(self) -> str:
        # >=2x: genuinely more common in this intent's calls than elsewhere —
        # true for rare/specialized intents (query_fee, address_error).
        # <2x: still passes the light sanity floor (not anti-correlated) but is
        # common for the WRONG reason on a dominant/pervasive intent (affirm) —
        # still worth surfacing, but the human should weigh the lift number.
        return "high" if self.lift >= 2.0 else "low"


@dataclass
class UncoveredCluster:
    cluster_id: int
    size: int
    call_count: int
    medoid_text: str
    samples: list = field(default_factory=list)     # (call_id, text)
    best_guess: str = ""
    best_score: float = 0.0
    runner_up: str = ""
    runner_score: float = 0.0

    @property
    def decision_key(self) -> str:
        h = hashlib.sha1(self.medoid_text.encode("utf-8")).hexdigest()[:10]
        return f"uncovered:{h}"

    @property
    def volume(self) -> int:
        return self.size


@dataclass
class NaturalOpener:
    old_line: str
    new_line: str          # candidate with particle prepended or doubled
    particle: str
    mechanism: str          # "insert" | "reduplicate"
    call_count: int
    examples: list = field(default_factory=list)
    line_idx: int = 0

    @property
    def decision_key(self) -> str:
        h = hashlib.sha1((self.old_line + "|" + self.particle).encode("utf-8")).hexdigest()[:10]
        return f"opener:{h}"

    @property
    def volume(self) -> int:
        return self.call_count

    @property
    def confidence(self) -> str:
        return "high" if self.call_count >= 20 else "low"


# ------------------------------------------------------------- natural openers --
_DANDA_RE = re.compile(r"[।॥]")
_LEADING_WORD_RE = re.compile(r"^([\wऀ-ॿ]+)")
# Python's \b treats Devanagari dependent vowel signs (ी/े/ो/...) and anusvara
# (ं) as non-word (Unicode category Mc/Mn), so \bजी\b silently never matches —
# most Devanagari words end in exactly this kind of mark. Verified directly:
# \bजी\b failed on real transcript text containing "जी जी" at position 0.
# Lookaround against the same extended word-char class used elsewhere in this
# module (_LEADING_WORD_RE) instead of \b avoids this everywhere it matters.
_WORDCHAR = r"\wऀ-ॿ"
# recording disclosure / OTP / T&C lines are never eligible, even though only the
# leading particle would change — same "don't touch compliance-adjacent lines"
# principle applied everywhere else in this pipeline.
COMPLIANCE_RE = re.compile(r"record|terms and conditions|\botp\b|\bverify\b|consent", re.IGNORECASE)
# a line that IS the greeting (नमस्ते) is reached via on-intent routing in this
# file (self_intro follows start()'s own opening exchange) but is still a fresh
# self-introduction, not an acknowledgment of something just said — "हां,
# नमस्ते..."/"जी, नमस्ते..." reads backwards. Verified directly: this was the
# one clearly-wrong candidate class response-position gating alone didn't catch.
GREETING_RE = re.compile(r"नमस्ते", re.IGNORECASE)


def _leading_word(text: str) -> str | None:
    text = _DANDA_RE.sub(" ", text).strip()
    m = _LEADING_WORD_RE.match(text)
    return m.group(1) if m else None


def _opener_counts(calls: list) -> Counter:
    """How often each ACK_WORDS particle opens a real customer turn."""
    from src.extract import ACK_WORDS
    counts = Counter()
    for c in calls:
        for t in c["turns"]:
            if t.get("speaker") != "customer":
                continue
            w = _leading_word(t.get("text", ""))
            if w and w.lower() in ACK_WORDS:
                counts[w.lower()] += 1
    return counts


def _redup_call_counts(calls: list, word: str) -> tuple:
    """(call_count, examples) for how often `word word` appears in customer speech,
    counting distinct calls (not raw turns) — same PII/genericity floor used
    everywhere else in this pipeline."""
    pat = re.compile(
        rf"(?<![{_WORDCHAR}]){re.escape(word)}\s+{re.escape(word)}(?![{_WORDCHAR}])",
        re.IGNORECASE)
    n = 0
    examples = []
    for c in calls:
        hit = False
        for t in c["turns"]:
            if t.get("speaker") != "customer":
                continue
            text = t.get("text", "")
            if pat.search(text):
                hit = True
                if len(examples) < 3:
                    examples.append(text[:100])
        if hit:
            n += 1
    return n, examples


def _response_targets(d: dsl_parse.DSL, intent_filter: str | None = None) -> set:
    """State names ever reached via on-intent routing (globally or nested). With
    intent_filter set, restricted to routes on that specific intent — used to
    decide whether हां (echoing the customer's own word) fits better than जी."""
    out = set()
    for i, tgt in d.global_routes.items():
        if tgt and (intent_filter is None or i == intent_filter):
            out.add(tgt)
    for st in d.states.values():
        for i, tgt in st.intent_routes + st.nested_routes:
            if tgt and (intent_filter is None or i == intent_filter):
                out.add(tgt)
    return out


def mine_natural_openers(d: dsl_parse.DSL, calls: list) -> list:
    """Real customer opener/reduplication words, proposed as small leading-particle
    insertions into say() lines — never mid-sentence, never a verb, never a
    compliance-adjacent line. See the plan doc for why this is scoped this way:
    a full bot-vs-customer vocabulary diff was tested and rejected (confounded by
    speaker-role asymmetry, not register), and unrestricted reduplication mining
    was tested and rejected (surfaces ASR artifacts like "sms sms"/"nine nine").
    This only uses extract.ACK_WORDS — a small, already-vetted particle set —
    and only touches lines that are in genuine response position (the containing
    state is reachable via on-intent routing, not bot-initiated)."""
    if not calls:
        return []
    from src.extract import ACK_WORDS

    response_targets = _response_targets(d)
    affirm_targets = _response_targets(d, intent_filter="affirm")
    opener_counts = _opener_counts(calls)

    out = []
    for line_idx, line in enumerate(d.lines):
        m = dsl_parse.SAY_RE.search(line)
        if not m:
            continue
        old_text = m.group(1)
        if COMPLIANCE_RE.search(old_text) or GREETING_RE.search(old_text):
            continue
        leading = _leading_word(old_text)
        leading_lo = leading.lower() if leading else None

        if leading_lo in ACK_WORDS:
            # already has an opener — propose reduplicating it, if customers do
            n, examples = _redup_call_counts(calls, leading)
            if n >= 2:
                new_text = old_text[:len(leading)] + " " + leading + old_text[len(leading):]
                out.append(NaturalOpener(
                    old_line=old_text, new_line=new_text, particle=leading,
                    mechanism="reduplicate", call_count=n, examples=examples,
                    line_idx=line_idx))
            continue

        # no opener at all — only eligible if this line is genuinely in response
        # position (the containing state is reached via on-intent routing)
        state_name = dsl_parse.containing_state(d, line_idx)
        if state_name is None or state_name not in response_targets:
            continue

        state_is_affirm_target = state_name in affirm_targets
        ranked = sorted(opener_counts.items(), key=lambda kv: -kv[1])
        if state_is_affirm_target:
            ranked = sorted(ranked, key=lambda kv: kv[0] not in ("हां", "haan"))
        proposed = 0
        for particle_lo, n in ranked:
            if n < 2 or proposed >= 2:
                break
            # use the canonical Devanagari/roman spelling as it's written in
            # ACK_WORDS's own particle rather than a raw corpus-cased variant
            particle = {"haan": "हां", "han": "हां", "ha": "हां", "ji": "जी",
                       "theek": "ठीक", "thik": "ठीक", "achha": "अच्छा",
                       "accha": "अच्छा"}.get(particle_lo, particle_lo)
            new_text = f"{particle}, {old_text}"
            examples_c = [c for c in calls
                         if any(t.get("speaker") == "customer" and
                                (_leading_word(t.get("text", "")) or "").lower() == particle_lo
                                for t in c["turns"])]
            examples = []
            for c in examples_c[:3]:
                for t in c["turns"]:
                    if t.get("speaker") == "customer" and \
                       (_leading_word(t.get("text", "")) or "").lower() == particle_lo:
                        examples.append(t.get("text", "")[:100])
                        break
            out.append(NaturalOpener(
                old_line=old_text, new_line=new_text, particle=particle,
                mechanism="insert", call_count=n, examples=examples,
                line_idx=line_idx))
            proposed += 1
    return out


# ------------------------------------------------------- anchor-based buckets --
def bucket_turns_by_anchors(d: dsl_parse.DSL, calls: list,
                            margin: float = MARGIN_DELTA,
                            floor: float = MATCH_FLOOR,
                            min_calls: int = 3) -> dict:
    """{intent: {call_id: joined_text}} — which real customer turns look like each
    intent, matched against that intent's OWN anchors instead of a classifier label.

    Why this exists: dsl_audit.INTENT_ALIASES bridges the classifier's ~30
    form-journey labels (customer_do_otp, customer_report_done) to the DSL's 28
    conversational intents (irate, security_concern), and only 5 map cleanly —
    the two taxonomies were built for different purposes. Every intent DOES carry
    hand-written anchors though, so matching turns against those needs no bridge
    and covers all 28.

    IMPORTANT — the output of this function is NOT trustworthy on its own.
    Embedding similarity cannot see negation: measured on real data, "जी OTP मिल
    गया है" ("I GOT the OTP") lands in otp_not_received, and "हां मिल गया SMS" in
    sms_not_received, because the negated and affirmative forms share nearly every
    token. Roughly 3 of 13 buckets were correct unvalidated. Callers MUST pass
    these through src.dsl_auto.validate_buckets() before mining words from them —
    a wrong bucket silently poisons every word mined for that intent, which is
    worse than having no bucket at all.

    Returns the same {intent: {call_id: text}} shape as _turns_by_call, so
    mine_anchor_gaps can consume either source interchangeably."""
    from collections import defaultdict
    try:
        import numpy as np
        from sentence_transformers import SentenceTransformer
    except ImportError:
        return {}

    model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    names, embs = _all_intent_anchor_embeddings(d, model)
    if not names:
        return {}

    turns = [(c["call_id"], t["text"]) for c in calls for t in c["turns"]
             if t.get("speaker") == "customer" and _shape_ok(t.get("text", ""))]
    if not turns:
        return {}
    T = model.encode([t for _, t in turns], normalize_embeddings=True,
                     show_progress_bar=False)

    grouped: dict = defaultdict(list)
    for i, (cid, txt) in enumerate(turns):
        scores = sorted(((float(np.max(T[i] @ e.T)), n) for n, e in zip(names, embs)),
                        reverse=True)
        if len(scores) < 2:
            continue
        # same margin discipline as mine_uncovered_clusters: a confident winner
        # must also clearly beat the runner-up, or the assignment is a coin flip
        if scores[0][0] >= floor and (scores[0][0] - scores[1][0]) >= margin:
            grouped[scores[0][1]].append((cid, txt))

    out: dict = {}
    for intent, items in grouped.items():
        by_call: dict = defaultdict(list)
        for cid, txt in items:
            by_call[cid].append(txt)
        if len(by_call) >= min_calls:      # recurrence guard, doubles as PII guard
            out[intent] = {cid: " ".join(v) for cid, v in by_call.items()}
    return out


# ---------------------------------------------------------------- anchor gaps --
def _turns_by_call(calls: list, predicate) -> dict:
    """{call_id: joined text} for customer turns matching `predicate(turn)`."""
    out: dict = {}
    for c in calls:
        matched = [t["text"] for t in c["turns"]
                  if t.get("speaker") == "customer" and predicate(t)]
        if matched:
            out[c["call_id"]] = " ".join(matched)
    return out


def mine_anchor_gaps(d: dsl_parse.DSL, calls: list, client_key: str,
                     max_per_intent: int | None = None,
                     extra_buckets: dict | None = None) -> list:
    """extra_buckets: {intent: {call_id: text}} from bucket_turns_by_anchors(),
    ALREADY validated by dsl_auto.validate_buckets(). These extend coverage beyond
    the handful of intents INTENT_ALIASES can bridge; passing unvalidated buckets
    here is a correctness bug (see bucket_turns_by_anchors' docstring)."""
    from src.extract import build_keyword_vocab

    aliases = dsl_audit.INTENT_ALIASES.get(client_key, {})
    if not calls:
        return []

    all_call_texts = _turns_by_call(calls, lambda t: True)
    n_total_calls = len(all_call_texts) or 1
    baseline_vocab = build_keyword_vocab(all_call_texts.values(), min_calls=2)

    # {intent: {call_id: text}} from both sources. Aliases win where they exist —
    # they were verified by reading real samples, so they're the stronger signal.
    sources: dict = {}
    for intent, observed_names in aliases.items():
        sources[intent] = _turns_by_call(
            calls, lambda t, names=set(observed_names): t.get("intent") in names)
    for intent, bucket in (extra_buckets or {}).items():
        sources.setdefault(intent, bucket)

    out = []
    for intent, target_texts in sources.items():
        if intent not in d.intents:
            continue
        existing_anchors = [a.lower() for a in d.intents[intent].anchors]
        if not target_texts:
            continue
        n_target = len(target_texts)
        target_vocab = build_keyword_vocab(target_texts.values(), min_calls=2)

        candidates = []
        for word, n_calls in target_vocab.items():
            if word in _NUMBER_WORDS:
                continue
            # already covered — an existing anchor contains this word (either direction)
            if any(word in a or a in word for a in existing_anchors):
                continue
            base_rate = baseline_vocab.get(word, 1) / n_total_calls
            target_rate = n_calls / n_target
            lift = target_rate / max(base_rate, 1e-6)
            if lift < MIN_LIFT:
                continue
            examples = []
            for cid, text in target_texts.items():
                if word in text.lower() and len(examples) < 3:
                    examples.append(text[:100])
            candidates.append(AnchorGap(intent, word, n_calls, lift, examples))

        # Secondary key is not cosmetic: build_keyword_vocab accumulates from a
        # set, so its dict insertion order varies per process (PYTHONHASHSEED).
        # Sorting on count alone leaves equal-count candidates in that unstable
        # order, which changes the LLM prompt text run to run — breaking the
        # response cache and making autonomous runs non-reproducible.
        candidates.sort(key=lambda g: (-g.call_count, g.word))
        out.extend(candidates if max_per_intent is None else candidates[:max_per_intent])
    return out


# ----------------------------------------------------------- uncovered clusters --
def _shape_ok(text: str) -> bool:
    from src.stopwords import STOPWORDS
    from src.extract import _FILLERS
    toks = _WORD_RE.findall(text)
    if not (2 <= len(toks) <= 12):
        return False
    if re.search(r"\d{4,}", text):
        return False
    lo = [t.lower() for t in toks]
    if lo.count(max(set(lo), key=lo.count)) >= 3:
        return False   # repetition garble
    stop_frac = sum(1 for t in lo if t in STOPWORDS or t in _FILLERS) / len(lo)
    if stop_frac > 0.6:
        return False
    return True


def _all_intent_anchor_embeddings(d: dsl_parse.DSL, model):
    import numpy as np
    names, embs = [], []
    for name, it in d.intents.items():
        if it.anchors:
            e = model.encode(it.anchors, normalize_embeddings=True, show_progress_bar=False)
            names.append(name)
            embs.append(np.asarray(e))
    return names, embs


def mine_uncovered_clusters(d: dsl_parse.DSL, calls: list,
                            margin: float = MARGIN_DELTA, floor: float = MATCH_FLOOR,
                            min_cluster_size: int = 5, max_clusters: int = 5) -> list:
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from src.extract import EMBED_MODEL
    from src.subcluster import discover_subclusters

    if not calls:
        return []

    turns = []   # (call_id, index, text)
    for c in calls:
        for t in c["turns"]:
            if t.get("speaker") == "customer" and _shape_ok(t.get("text", "")):
                turns.append((c["call_id"], t["index"], t["text"]))
    if len(turns) < min_cluster_size * 2:
        return []

    model = SentenceTransformer(EMBED_MODEL)
    names, anchor_embs = _all_intent_anchor_embeddings(d, model)
    texts = [t[2] for t in turns]
    T = np.asarray(model.encode(texts, normalize_embeddings=True, show_progress_bar=False))

    uncovered_idx = []
    for i in range(len(turns)):
        scores = sorted(
            ((float(np.max(T[i] @ e.T)), n) for n, e in zip(names, anchor_embs)),
            reverse=True)
        if not scores:
            uncovered_idx.append(i)
            continue
        best_score, best_name = scores[0]
        runner_score, runner_name = scores[1] if len(scores) > 1 else (0.0, "")
        if best_score < floor or (best_score - runner_score) < margin:
            uncovered_idx.append(i)

    if len(uncovered_idx) < min_cluster_size * 2:
        return []

    u_texts = [texts[i] for i in uncovered_idx]
    u_emb = T[uncovered_idx]
    cluster_ids = discover_subclusters(u_texts, model, min_cluster_size=min_cluster_size)

    from collections import defaultdict
    groups = defaultdict(list)
    for pos, cid in enumerate(cluster_ids):
        if cid == -1:
            continue
        groups[cid].append(pos)

    out = []
    for cid, positions in groups.items():
        call_ids = {turns[uncovered_idx[p]][0] for p in positions}
        if len(call_ids) < 2:      # PII / robustness guard: real recurring pattern, not one call
            continue
        sub_emb = u_emb[positions]
        centroid = sub_emb.mean(axis=0)
        sims_to_centroid = sub_emb @ centroid
        medoid_pos = positions[int(np.argmax(sims_to_centroid))]
        medoid_text = texts[uncovered_idx[medoid_pos]]
        samples = [(turns[uncovered_idx[p]][0], texts[uncovered_idx[p]]) for p in positions[:5]]

        best_score, best_name, runner_score, runner_name = 0.0, "", 0.0, ""
        if names:
            scores = sorted(
                ((float(np.max(centroid @ e.T)), n) for n, e in zip(names, anchor_embs)),
                reverse=True)
            (best_score, best_name) = scores[0]
            if len(scores) > 1:
                (runner_score, runner_name) = scores[1]

        out.append(UncoveredCluster(
            cluster_id=cid, size=len(positions), call_count=len(call_ids),
            medoid_text=medoid_text, samples=samples,
            best_guess=best_name, best_score=best_score,
            runner_up=runner_name, runner_score=runner_score,
        ))
    out.sort(key=lambda c: -c.size)
    return out[:max_clusters]


# --------------------------------------------------------- decision persistence --
def _decisions_path(client_key: str) -> Path:
    return config.CLIENTS_DIR / client_key / "anchor_decisions.json"


def load_decisions(client_key: str) -> dict:
    p = _decisions_path(client_key)
    if not p.exists():
        return {"accepted": [], "rejected": []}
    return json.loads(p.read_text())


def save_decision(client_key: str, decision_key: str, accepted: bool) -> None:
    d = load_decisions(client_key)
    bucket = "accepted" if accepted else "rejected"
    other = "rejected" if accepted else "accepted"
    if decision_key not in d[bucket]:
        d[bucket].append(decision_key)
    if decision_key in d[other]:
        d[other].remove(decision_key)
    # atomic, for the same reason as the LLM cache: a half-written decisions file
    # loses every prior accept/reject and the queue silently re-proposes them
    import os
    import tempfile
    p = _decisions_path(client_key)
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w") as fh:
            json.dump(d, fh, indent=2, ensure_ascii=False)
        os.replace(tmp, p)
    except Exception:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


# --------------------------------------------------------------------- queue --
def build_queue(d: dsl_parse.DSL, calls: list, client_key: str) -> list:
    """Combined, ranked, decision-filtered queue. Each item is an AnchorGap
    (auto-eligible), an UncoveredCluster (always propose-only), or a
    NaturalOpener (always propose-only — it changes existing say() text), sorted
    by real volume — the phrases customers say most, that the prompt currently
    handles worst, float to the top."""
    decisions = load_decisions(client_key)
    seen = set(decisions["accepted"]) | set(decisions["rejected"])

    items = (mine_anchor_gaps(d, calls, client_key) + mine_uncovered_clusters(d, calls)
            + mine_natural_openers(d, calls))
    items = [it for it in items if it.decision_key not in seen]
    items.sort(key=lambda it: -it.volume)
    return items


def render_queue(items: list) -> str:
    if not items:
        return "No new candidates — everything found so far has already been reviewed."
    out = []
    for n, it in enumerate(items, start=1):
        if isinstance(it, AnchorGap):
            tag = "" if it.confidence == "high" else "  [common corpus-wide too — weigh the lift before accepting]"
            out.append(f"[{n}]  anchor gap ({it.confidence} confidence) · intent \"{it.intent}\" · "
                       f"\"{it.word}\" appears in {it.call_count} calls "
                       f"(lift {it.lift:.2f}x vs. overall corpus){tag}")
            for ex in it.examples:
                out.append(f"       · {ex}")
            out.append(f"     auto-eligible on accept -> adds \"{it.word}\" to {it.intent}'s anchors")
        elif isinstance(it, NaturalOpener):
            verb = "doubles" if it.mechanism == "reduplicate" else "adds"
            out.append(f"[{n}]  natural opener ({it.confidence} confidence) · \"{it.particle}\" "
                       f"{verb} as a lead-in · {it.call_count} calls in real customer speech")
            out.append(f"       old: {it.old_line[:80]}")
            out.append(f"       new: {it.new_line[:80]}")
            for ex in it.examples:
                out.append(f"       · {ex}")
            out.append("     review only -> reworks an existing say() line, always needs a human look")
        else:
            out.append(f"[{n}]  uncovered cluster · {it.size} turns · {it.call_count} calls")
            for cid, text in it.samples:
                out.append(f"       · {text[:80]}")
            if it.best_guess:
                out.append(f"     best guess: {it.best_guess} ({it.best_score:.2f})  "
                           f"runner-up: {it.runner_up} ({it.runner_score:.2f})  "
                           f"margin: {it.best_score - it.runner_score:.2f}")
            out.append("     review only -> needs a human to name the intent and write the answer")
        out.append("")
    return "\n".join(out)


def render_queue_markdown(items: list, client_key: str, prompt_name: str) -> str:
    """The same queue as render_queue(), as a markdown file meant to live in the
    repo (see run_improve.py, which writes this to
    data/clients/<client>/review_queue.md every run) — so the findings are
    something to open in an editor, not just terminal output that scrolls away.
    Regenerated fresh each run; always reflects current file + data state."""
    import datetime
    gaps = [it for it in items if isinstance(it, AnchorGap)]
    clusters = [it for it in items if isinstance(it, UncoveredCluster)]
    openers = [it for it in items if isinstance(it, NaturalOpener)]

    out = [
        f"# Review queue — {prompt_name}",
        "",
        f"_Generated {datetime.date.today().isoformat()} · client `{client_key}` · "
        f"{len(items)} candidate(s), none applied yet_",
        "",
        "Every quote below is verbatim from a real call — nothing here is generated. "
        "Apply an item with:",
        "",
        "```",
        f"python run_improve.py <prompt.raven> --client {client_key} --accept N,M,K",
        "```",
        "",
        f"| | count |",
        f"|---|---|",
        f"| Anchor gaps (word missing from an existing intent) | {len(gaps)} |",
        f"| Natural openers (real customer particle for an existing say() line) | {len(openers)} |",
        f"| Uncovered clusters (no existing intent fits — needs a person) | {len(clusters)} |",
        f"| — high confidence | {sum(1 for g in gaps if g.confidence == 'high') + sum(1 for o in openers if o.confidence == 'high')} |",
        f"| — low confidence | {sum(1 for g in gaps if g.confidence == 'low') + sum(1 for o in openers if o.confidence == 'low')} |",
        "",
        "---",
        "",
    ]

    if not items:
        out.append("Nothing pending — everything found so far has already been reviewed.")
        return "\n".join(out)

    for n, it in enumerate(items, start=1):
        if isinstance(it, AnchorGap):
            conf_tag = "🟢 high confidence" if it.confidence == "high" else "🟡 low confidence"
            out.append(f"## [{n}] Add `\"{it.word}\"` to `{it.intent}`'s recognized phrases")
            out.append("")
            out.append(f"{conf_tag} · anchor gap · **{it.call_count} calls** · "
                       f"**{it.lift:.2f}x** lift vs. overall corpus")
            out.append("")
            if it.confidence == "low":
                out.append("> Common corpus-wide too, not just in this intent's calls — weigh "
                           "the lift number before accepting.")
                out.append("")
            out.append("Real customer turns:")
            out.append("")
            for ex in it.examples:
                out.append(f"> {ex}")
                out.append(">")
            if out[-1] == ">":
                out.pop()
            out.append("")
            out.append(f"**Accept:** `--accept {n}`")
        elif isinstance(it, NaturalOpener):
            conf_tag = "🟢 high confidence" if it.confidence == "high" else "🟡 low confidence"
            verb = "Double" if it.mechanism == "reduplicate" else "Add"
            out.append(f"## [{n}] {verb} `\"{it.particle}\"` as a lead-in")
            out.append("")
            out.append(f"{conf_tag} · natural opener ({it.mechanism}) · **{it.call_count} calls** "
                       "in real customer speech")
            out.append("")
            out.append("> This reworks an existing say() line — always review the fit yourself, "
                       "the system only knows the word is common, not whether it fits this "
                       "specific line.")
            out.append("")
            out.append(f"- old: `{it.old_line}`")
            out.append(f"- new: `{it.new_line}`")
            out.append("")
            out.append("Real customer turns:")
            out.append("")
            for ex in it.examples:
                out.append(f"> {ex}")
                out.append(">")
            if out[-1] == ">":
                out.pop()
            out.append("")
            out.append(f"**Accept:** `--accept {n}`")
        else:
            out.append(f"## [{n}] Uncovered cluster — {it.size} turns, {it.call_count} calls")
            out.append("")
            out.append("🔵 uncovered cluster · always needs a person — naming the intent and "
                       "writing its answer can't be automated")
            out.append("")
            if it.best_guess:
                margin = it.best_score - it.runner_score
                out.append(f"Best guess: `{it.best_guess}` ({it.best_score:.2f})  ·  "
                           f"runner-up: `{it.runner_up}` ({it.runner_score:.2f})  ·  "
                           f"margin: **{margin:.2f}**")
                out.append("")
            out.append("Sample turns:")
            out.append("")
            for cid, text in it.samples:
                out.append(f"> {text}  \n> <sub>`{cid}`</sub>")
                out.append(">")
            if out[-1] == ">":
                out.pop()
            out.append("")
            out.append(f"**Track (no automatic edit possible):** `--accept {n}` or `--reject {n}`")
        out.append("")
        out.append("---")
        out.append("")

    return "\n".join(out)


if __name__ == "__main__":
    import sys
    import warnings
    warnings.filterwarnings("ignore")
    dsl_path = sys.argv[1]
    client_key = sys.argv[2] if len(sys.argv) > 2 else "abcl"
    d = dsl_parse.parse(dsl_path)
    calls = dsl_audit._client_calls(client_key)
    items = build_queue(d, calls, client_key)
    print(f"{len(items)} candidate(s) for review\n")
    print(render_queue(items))
