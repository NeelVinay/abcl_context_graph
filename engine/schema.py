"""Per-call extraction schema — the contract the (Claude) extractor must fill.

Redesigned to capture what the manager asked for:
  1. SENTIMENT / state    -> Turn.sentiment   (customer happy / skeptical / distrustful …)
  2. TRIGGER points       -> Turn.intent      (action-oriented "who did what" = the trigger)
  3. TOOL / API calls     -> Turn.tool        (SMS sent, pushed/fetched CRM, OTP, transfer …)
  4. KEYWORDS not sentences -> Turn.keywords  (the short signal phrases; the "intent words")
  5. clearer graph        -> action-oriented, actor-aware intent names
                             (e.g. agent_request_pan -> customer_provide_pan, not a shared
                              "enter_pan" slapped on both speakers)

Design notes:
  - `intent` is a free string but MUST follow the convention <actor>_<verb>_<object>
    (agent_request_pan, customer_provide_pan, customer_express_distrust). This is what
    makes the flow graph read sensibly and serves as the trigger point.
  - `keywords` are SHORT signal phrases lifted from the turn ("scam", "don't want to give
    access"), NOT the full utterance. Reports show these, not `text`.
  - `sentiment` is set for customer turns (None for agent/system).
  - `tool` is set when a turn corresponds to a system/API event; such turns may also use
    speaker = system and type = tool_call.
  - `text` is kept only as provenance; it is not what reports display.
"""
from __future__ import annotations  # allows `X | None` style on Python 3.9

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Speaker(str, Enum):
    agent = "agent"
    customer = "customer"
    system = "system"          # tool / API events (no human speaker)


class TurnType(str, Enum):
    action = "action"          # something the agent or customer DOES (a trigger point)
    sentiment = "sentiment"    # the customer's state / feeling
    tool_call = "tool_call"    # a system / API event (SMS, CRM push/pull, OTP, transfer)


class Sentiment(str, Enum):
    happy = "happy"
    satisfied = "satisfied"
    neutral = "neutral"
    confused = "confused"
    skeptical = "skeptical"
    frustrated = "frustrated"
    distrustful = "distrustful"   # scam / fraud fear ("is this a scam", "don't want to give access")


class Tool(str, Enum):
    send_sms = "send_sms"
    send_whatsapp = "send_whatsapp"
    send_otp = "send_otp"
    push_to_crm = "push_to_crm"
    fetch_from_crm = "fetch_from_crm"
    transfer_to_rm = "transfer_to_rm"
    schedule_callback = "schedule_callback"
    other = "other"


class Entity(BaseModel):
    type: str = Field(description="e.g. loan_amount, emi, pan, pincode, processing_fee")
    value: str


class Turn(BaseModel):
    index: int
    speaker: Speaker

    type: TurnType = Field(
        default=TurnType.action,
        description="action = a trigger (agent/customer did something); sentiment = customer state; "
                    "tool_call = a system/API event",
    )
    intent: str = Field(
        description="action-oriented, actor-aware label <actor>_<verb>_<object>, "
                    "e.g. agent_request_pan, customer_provide_pan, customer_express_distrust",
    )
    keywords: list[str] = Field(
        default_factory=list,
        description="SHORT signal phrases that imply the intent/sentiment (the 'intent words'), "
                    "e.g. ['scam', \"don't want to give access\"] — NOT full sentences",
    )
    sentiment: Optional[Sentiment] = Field(
        default=None,
        description="the customer's state for this turn (None for agent/system turns)",
    )
    tool: Optional[Tool] = Field(
        default=None,
        description="set when this turn triggers a system/API event (SMS, CRM, OTP, transfer …)",
    )

    text: str = Field(default="", description="raw utterance — provenance only; reports show keywords, not this")
    entities: list[Entity] = Field(default_factory=list)


class Outcome(str, Enum):
    transferred = "transferred"     # handed to a relationship manager
    callback = "callback"
    not_interested = "not_interested"
    completed = "completed"         # application/journey finished
    dropped = "dropped"
    other = "other"


class CallGraph(BaseModel):
    """The full structured representation of one call."""
    call_id: str
    language: str = "hi-en"
    outcome: Outcome = Outcome.other
    turns: list[Turn]
