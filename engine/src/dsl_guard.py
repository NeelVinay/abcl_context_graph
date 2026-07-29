"""Mechanical self-check for LLM-generated say() copy.

This is the piece that makes autonomous operation defensible. The LLM is asked to
follow the prompt's own language{} rules and to avoid asserting loan terms — but
"asked to" is not a control. Every generated line is checked HERE, in code, before
it can be applied, and a line that fails is retried once (with the reason fed back)
and then discarded. Nothing that fails these checks is ever written.

Two categories, different stakes:

  compliance  — the regulated-lending boundary. Generated copy may motivate and
                reframe; it must never assert a rate, an amount, a fee, a
                timeline, or an approval outcome. A line inventing "sirf 2 din
                mein approval" or "10% se kam interest" is a real problem, not a
                style nit, so these are hard failures.
  style       — the client's own language{} block (female verb forms, आप address,
                Roman-script term list, no करेंगे/बताएंगे, no unresolved
                <<placeholder>>). Cheap to check, and keeps generated lines
                indistinguishable in register from the hand-written ones.

Deliberately conservative: a false rejection costs one discarded suggestion, a
false acceptance ships a non-compliant line to real customers.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------- compliance --
# Any digit at all — Devanagari or ASCII. Loan terms are inherently numeric, so
# the simplest reliable rule is that generated copy carries no numbers whatsoever.
# The hand-written lines that legitimately quote a rate stay untouched; this only
# constrains what the LLM may ADD.
_DIGITS = re.compile(r"[0-9०-९]")


def _has_any_digit(s: str) -> bool:
    """Any Unicode decimal digit, not just ASCII + Devanagari. A hardcoded class
    missed fullwidth (５) and Arabic-Indic (٥) forms, which let a bare EMI figure
    through. unicodedata covers every script's digits without enumeration."""
    import unicodedata
    return any(unicodedata.category(ch) == "Nd" for ch in s)
_CURRENCY = re.compile(r"[₹$]|\brs\.?\b|\brupees?\b|रुपए|रुपये", re.IGNORECASE)
_PERCENT = re.compile(r"%|\bpercent\b|प्रतिशत|फीसदी", re.IGNORECASE)
# spelled-out quantities that dodge a pure digit check
# Two hard-won corrections, both found by real generated copy being wrongly rejected:
#   1. The Devanagari alternation MUST be boundary-anchored. Unanchored, "दो"
#      matched inside "दोबारा" (= "again") and killed a good line.
#   2. Bare "एक" is Hindi's indefinite article ("एक offer" = "an offer"), not a
#      quantity. Flagging it rejects ordinary sentences. Only flag a number when
#      it is actually attached to a money/tenure unit — which is where the
#      compliance risk genuinely lives ("एक लाख", "दो साल", "तीन महीने").
# Hindi numerals are NOT compositional — every value 11-99 is its own word, so
# each must be listed. 11-19 and 60-90 were missing, which let real tenure
# claims through: "बारह महीने" (12 months), "साठ महीने की EMI", "इक्कीस दिन".
_DEV_NUM = (r"एक|दो|तीन|चार|पांच|पाँच|छह|सात|आठ|नौ|दस|"
            r"ग्यारह|बारह|तेरह|चौदह|पंद्रह|पन्द्रह|सोलह|सत्रह|अठारह|उन्नीस|"
            r"बीस|इक्कीस|पच्चीस|तीस|पैंतीस|चालीस|पैंतालीस|पचास|पचपन|"
            r"साठ|पैंसठ|सत्तर|पचहत्तर|अस्सी|नब्बे|सौ")
_UNIT = (r"लाख|करोड़|हज़ार|हजार|percent|प्रतिशत|महीने|महीना|साल|दिन|हफ़्ते|हफ्ते|"
         r"रुपए|रुपये|lakh|crore|thousand|month|months|year|years|day|days")
_NUMBER_WORDS = re.compile(
    # English cardinals are unambiguous — no article problem, flag them directly.
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|twenty|"
    r"thirty|forty|fifty|hundred|thousand|lakh|lakhs|crore|crores|zero|point)\b"
    # Devanagari: only when bound to a unit, or a magnitude word standing alone.
    rf"|(?<![\wऀ-ॿ])({_DEV_NUM})\s*({_UNIT})(?![\wऀ-ॿ])"
    rf"|(?<![\wऀ-ॿ])(लाख|करोड़|हज़ार|हजार)(?![\wऀ-ॿ])",
    re.IGNORECASE)
# ...but a bare counting word is not a loan-term claim. "एक बार फिर देख लीजिए"
# ("have a look once more") and "एक minute रुकें" are conversational idiom, and
# the hand-written prompt already uses both. Found by simulation: the guard
# rejected a perfectly compliant line purely for containing "एक बार".
# Only these low-stakes units are exempt — anything followed by a money or
# tenure unit (रुपए/हज़ार/लाख/महीने/दिन/साल/percent) stays blocked, which is
# where the actual compliance risk lives.
_SAFE_COUNTING = re.compile(
    r"(एक|दो|one|two)\s+(बार|second|seconds|minute|minutes|moment|पल|मिनट)\b",
    re.IGNORECASE)
# claims about outcome/speed that are promises even without a number
# "pre-approved" is this product's established name and appears in every existing
# pitch line — it is not a promise of approval and must not be treated as one.
_PREAPPROVED = re.compile(r"pre[- ]?approved", re.IGNORECASE)
_PROMISE = re.compile(
    r"\bguarantee|\bguaranteed|\bapprov(al|ed)\b|\binstant\b|\bimmediate\b|"
    r"\bsure\s+shot\b|गारंटी|ज़रूर मिलेगा|जरूर मिलेगा|मिल ही जाएगा|पक्का"
    # Romanised Hinglish promises were entirely absent — this is a Hinglish
    # product, so "pakka ho jayega" / "turant mil jayega" are as likely as
    # the Devanagari forms and were sailing through.
    r"|\bpakka\b|\bzaroor\b|\bturant\b|\bmil jayega\b|\bho jayega\b|"
    r"\bconfirm hai\b|\bguarantee\b|\bgaranti\b|\bpass ho\b",
    re.IGNORECASE)

# ------------------------------------------------------------------- style --
# from the prompt's own language{} block
_MALE_VERB = re.compile(r"\b(सकता हूँ|सकता हूं|रहा हूँ|रहा हूं|करता हूँ|करता हूं|"
                        r"दूँगा|दूंगा|बताऊँगा|बताऊंगा|करूँगा|करूंगा)")
_FORBIDDEN_FORMAL = re.compile(r"(करेंगे|बताएंगे|सकते हैं\?)")
_GENDERED_TITLE = re.compile(r"\b(sir|madam|ma'?am)\b", re.IGNORECASE)
_UNRESOLVED_PLACEHOLDER = re.compile(r"<<(\w+)>>")
_LITERARY = {
    "वेतन": "salary", "ऋण": "loan", "दस्तावेज़": "documents",
    "स्वीकृति": "approval", "भुगतान": "payment",
}


def check_compliance(line: str) -> list:
    """Hard failures. Non-empty result = never apply this line."""
    problems = []
    if _has_any_digit(line):
        problems.append("contains a digit — generated copy must not state rates, "
                        "amounts, fees, or timelines")
    if _CURRENCY.search(line):
        problems.append("contains a currency reference")
    if _PERCENT.search(line):
        problems.append("contains a percentage")
    # strip the safe conversational counting idioms before looking for quantities
    probe = _SAFE_COUNTING.sub(" ", line)
    if _NUMBER_WORDS.search(probe):
        problems.append("contains a spelled-out quantity")
    if _PROMISE.search(_PREAPPROVED.sub(" ", line)):
        problems.append("promises an outcome (approval/guarantee/speed)")
    return problems


def check_style(line: str, known_placeholders: set | None = None) -> list:
    """language{} conformance. Non-empty = retry, then discard."""
    problems = []
    if _MALE_VERB.search(line):
        problems.append("male verb form — language{} requires female forms")
    if _FORBIDDEN_FORMAL.search(line):
        problems.append("uses करेंगे/बताएंगे/सकते हैं — language{} forbids these")
    if _GENDERED_TITLE.search(line):
        problems.append("uses a gendered title — language{} requires आप only")
    for ph in _UNRESOLVED_PLACEHOLDER.findall(line):
        if known_placeholders is not None and ph not in known_placeholders:
            problems.append(f"unknown placeholder <<{ph}>>")
    for lit, better in _LITERARY.items():
        if lit in line:
            problems.append(f"literary Hindi {lit!r} — language{{}} requires {better!r}")
    return problems


def check_line(line: str, known_placeholders: set | None = None) -> list:
    """All checks. Empty list = safe to apply."""
    return check_compliance(line) + check_style(line, known_placeholders)


# Devanagari punctuation sits INSIDE the ऀ-ॿ block (danda is U+0964), so a naive
# [\wऀ-ॿ] class swallows it and "हूँ।" never equals "हूं". Strip it first.
_PUNCT = re.compile(r"[।॥,.—\-!?()]")
# The agent's own name appears both transliterated and in Devanagari across the
# prompt; without folding these, two self-introductions look like different text.
_ALIASES = {"priya": "प्रिया", "प्रिया": "प्रिया",
            "aditya": "abcl", "आदित्य": "abcl", "birla": "abcl", "बिरला": "abcl",
            "capital": "abcl", "कैपिटल": "abcl", "abcl": "abcl"}
# spelling variants of the same Hindi word (nasalisation is written inconsistently)
_NASAL = re.compile(r"[ंँ]")


def _content_tokens(line: str) -> set:
    """Meaning-bearing tokens: drop the particles and filler the natural-opener
    feature deliberately adds, so "जी, X" and "X" don't look different."""
    from src.stopwords import STOPWORDS
    line = _PUNCT.sub(" ", line.lower())
    toks = re.findall(r"[\wऀ-ॿ]{3,}", line)
    drop = STOPWORDS | {"जी", "हां", "हाँ", "बिलकुल", "बिल्कुल", "ठीक", "कोई", "बात",
                        "नहीं", "करें", "बताएं", "आपको", "आपकी", "आपका", "मुझे", "रही",
                        "हूँ", "हूं", "यहां", "यहाँ", "एक"}
    out = set()
    for t in toks:
        t = _NASAL.sub("", t)          # हूँ / हूं -> हू
        t = _ALIASES.get(t, t)
        if t and t not in drop:
            out.add(t)
    return out


def check_redundancy(new_line: str, existing_lines: list,
                     threshold: float = 0.6) -> list:
    """Is this new line saying what a line in the same state already says?

    The LLM proposes ADDITIONS, and nothing else in the pipeline notices when an
    addition restates neighbouring speech. Caught in real output: it added
    "मैं Priya हूँ — Aditya Birla Capital की digital voice assistant" to a state
    whose existing line was already "मैं प्रिया हूँ, Aditya Birla Capital की तरफ
    से बोल रही हूँ", so the agent introduced itself twice in a row. Also caught
    two near-identical rate-transparency lines proposed for the same state.

    Overlap is measured against the SHORTER line's content tokens, so a short
    restatement buried inside a long line is still caught."""
    new_t = _content_tokens(new_line)
    if len(new_t) < 3:
        return []
    problems = []
    for ex in existing_lines:
        ex_t = _content_tokens(ex)
        if len(ex_t) < 3:
            continue
        overlap = len(new_t & ex_t) / max(1, min(len(new_t), len(ex_t)))
        if overlap >= threshold:
            problems.append(
                f"{overlap:.0%} content overlap with a line already in this state "
                f"— would repeat itself: {ex[:70]!r}")
            break
    return problems


def check_structure(old_line: str, new_line: str) -> list:
    """For edits that MODIFY an existing say() rather than add one: verify the
    change is additive at the edges, not a rewrite of the content. Protects
    against an LLM 'placement' quietly rewording the middle of a scripted line."""
    problems = []
    if old_line not in new_line:
        problems.append("existing line text was altered, not merely prefixed/suffixed")
    return problems
