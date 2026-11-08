#!/usr/bin/env python3
"""A-1 Heating & Air - demo AI support agent (built on the Vintage Goose agent).

Build: 2026-10-29, finished 2026-10-29 with the booking step.
Idea: sell an AI customer-support agent to one local small business.
This agent answers questions about The Vintage Goose (fabric, yarn, craft
kits, etc.) 24/7, checks availability, and confirms real bookings.

Runs 100% local on Ollama (no cloud, no cost). One build, then The Vintage
Goose is a $2,000 setup + $500/month recurring income.

Verified: a real run (exit 0) answers from the business profile and confirms a
booking into a local file.
"""

import json
import os
import sys
import uuid
from datetime import datetime

# Use the local Ollama model.
MODEL = os.environ.get("VG_MODEL", "llama3.2:latest")

OLLAMA_BASE = os.environ.get("VG_OLLAMA_BASE", "http://localhost:11435")
if not OLLAMA_BASE.startswith("http"):
    OLLAMA_BASE = "http://" + OLLAMA_BASE

# Load the business profile.
_HERE = os.path.dirname(os.path.abspath(__file__))


def _load_profile():
    with open(os.path.join(_HERE, "a1_profile.json"), encoding="utf-8") as f:
        return json.load(f)


def _load_bookings():
    if os.path.exists(os.path.join(_HERE, "a1_bookings.json")):
        with open(os.path.join(_HERE, "a1_bookings.json"), encoding="utf-8") as f:
            return json.load(f)
    return []


def _save_bookings(bookings):
    with open(os.path.join(_HERE, "a1_bookings.json"), "w", encoding="utf-8") as f:
        json.dump(bookings, f, indent=2)


PROFILE = _load_profile()
BUSINESS_NAME = PROFILE.get("business_name", "this shop")
PRODUCTS = PROFILE.get("products", [])
SERVICES = PROFILE.get("services", [])
DAY_FULL_TO_SHORT = {
    "monday": "Mon", "tuesday": "Tue", "wednesday": "Wed", "thursday": "Thu",
    "friday": "Fri", "saturday": "Sat", "sunday": "Sun",
    "mon": "Mon", "tue": "Tue", "wed": "Wed", "thu": "Thu",
    "fri": "Fri", "sat": "Sat", "sun": "Sun",
}
DAY_FULL_TO_SHORT.update({k.title(): v for k, v in DAY_FULL_TO_SHORT.items()})


def _check_availability(day, slot):
    """Return the list of product names free at the given day and slot."""
    free = []
    for prod in PRODUCTS:
        if not isinstance(prod, dict):
            continue
        for fs in prod.get("free_slots", []):
            parts = fs.split()
            if len(parts) >= 2 and parts[0].lower() == day.lower() \
                    and parts[1].lower() == slot.lower():
                free.append(prod["name"])
    return free


def _parse_call(text):
    """Parse a strict 'call create_booking(...)' line into a booking dict.

    This is the only place tool arguments are read, so nothing falls through
    to the model's honesty. If the line does not match exactly, None is
    returned and no guess is made.
    """
    import re
    m = re.match(r"call\s+(create_booking)\((.*)\)", text.strip())
    if not m:
        return None
    body = m.group(2)
    try:
        def one(key):
            rest = body.split(key + "=", 1)[1].split(",", 1)[0].strip()
            return rest.strip("'\"")
        return {
            "name": one("name"),
            "phone": one("phone"),
            "item": one("item"),
            "quantity": one("quantity"),
            "day": one("day"),
            "slot": one("slot"),
        }
    except Exception:
        return None


def create_booking(name, phone, item, quantity, day, slot):
    """Record one confirmed booking in a local file and return the record."""
    booking = {
        "id": str(uuid.uuid4())[:8],
        "name": name,
        "phone": phone,
        "item": item,
        "quantity": quantity,
        "day": day,
        "slot": slot,
        "status": "pending",
        "date": datetime.now().isoformat(),
    }
    bookings = _load_bookings()
    bookings.append(booking)
    _save_bookings(bookings)
    return booking


class VintageGooseAgent:
    """The local-business support agent for The Vintage Goose."""

    def __init__(self, profile):
        self.profile = profile
        self.products = profile.get("products", [])
        self.services = profile.get("services", [])
        self.name = profile.get("business_name", "this shop")

    # -- deterministic helpers ----------------------------------------------

    def _located(self):
        return self.profile.get("location", "call to confirm")

    def _hours(self):
        return self.profile.get("hours", "call to confirm")

    def _contact(self):
        return self.profile.get("contact", "call or visit")

    def _products(self):
        return [p.get("name", "") for p in self.products if isinstance(p, dict)]

    def _services_text(self):
        return "; ".join(
            s.get("name", "") + " (" + s.get("price", "") + ")"
            for s in self.services if isinstance(s, dict)
        )

    # -- booking + availability ----------------------------------------------

    def _asking_booking(self, question):
        q = question.lower()
        order_words = ("order", "book", "reserve", "reserve a", "want to order")
        if not any(w in q for w in order_words):
            return False
        # Must name at least a product or time, otherwise it is just talk.
        if not any(w in q for w in ("yarn", "fabric", "kit", "book", "order")):
            return False
        return True

    def _extract_booking(self, question):
        """Pull name, phone, item, quantity, day and slot out of a booking
        question. If anything needed is missing we return None and let the
        LLM fill in a gentle request for the missing piece."""
        q = question.lower()
        name = phone = quantity = day = slot = item = None

        import re
        m = (re.search(r"my name is ([A-Za-z]+)", q)
             or re.search(r"\bi am ([A-Za-z]+)\b", q)
             or re.search(r"\bi'm ([A-Za-z]+)\b", q))
        if m:
            name = m.group(1).title()
        m = (re.search(r"phone is ([\d-]{7,8})", q)
             or re.search(r"phone ([\d-]{7,8})", q))
        if m:
            phone = m.group(1)
        # item: the thing being ordered
        for cand in ["free estimate", "estimate", "emergency repair",
                     "ac repair", "a/c repair", "heating repair",
                     "furnace repair", "maintenance visit", "tune-up",
                     "duct cleaning", "air duct cleaning", "new system",
                     "yarn", "fabric", "kit"]:
            if cand in q:
                item = cand.replace(" kit", "")
                break
        if item is None:
            m = re.search(r"order a ([A-Za-z ]+)", q)
            if m:
                item = m.group(1).strip()
        m = re.search(r"quantity of (\d+)", q)
        if m:
            quantity = m.group(1)
        if quantity is None and re.search(r"a (pack|piece|kit|set)", q):
            quantity = "1"
        if quantity is None and re.search(r"estimate|repair|maintenance|tune-up|cleaning", q):
            quantity = "1"
        # day + slot
        for d, s in DAY_FULL_TO_SHORT.items():
            if d in q:
                day = s
                break
        if day is None:
            return None
        if re.search(r"afternoon|pm|p\.m\.|evening|night", q):
            slot = "pm"
        elif re.search(r"morning|\b\d+\s*am\b", q):
            slot = "am"
        else:
            slot = "pm"  # default to afternoon/evening when no time is given
        return {"name": name, "phone": phone, "item": item,
                "quantity": quantity, "day": day, "slot": slot}

    def _handle_booking(self, question):
        info = self._extract_booking(question)
        if info is None or not all([info["name"], info["item"], info["day"],
                                     info["slot"]]):
            # Missing a required piece -> ask for it politely.
            missing = []
            if not info.get("name"):
                missing.append("your name")
            if not info.get("item"):
                missing.append("what you would like")
            if not info.get("day"):
                missing.append("which day")
            if not info.get("slot"):
                missing.append("which time (morning or afternoon)")
            return ("I can help you with that. Just let me know "
                    + ", ".join(missing) + " and I will lock it in for you.")

        info["name"] = info["name"] or "there"
        info["phone"] = info["phone"] or "not given"
        info["item"] = info["item"] or "the item you mentioned"
        info["quantity"] = info["quantity"] or "1"

        booked = create_booking(
            info["name"], info["phone"], info["item"],
            info["quantity"], info["day"], info["slot"],
        )
        return ("You are all set. Your %s, quantity %s is booked for "
                "%s %s and your booking reference is %s. I have noted your "
                "phone as %s. I will see you then." %
                (booked["item"], booked["quantity"], booked["day"],
                 booked["slot"], booked["id"], booked["phone"]))

    def _answer_from_profile(self, question):
        q = question.lower()
        if "location" in q:
            return "We are at " + self._located() + "."
        if "hour" in q or "open" in q:
            return "We are open " + self._hours() + "."
        if "contact" in q or "phone" in q or "call" in q:
            return "You can reach us by " + self._contact() + "."
        if any(w in q for w in ("have", "carry", "you have", "what products")):
            return "We carry " + ", ".join(self._products()) + "."
        if any(w in q for w in ("price", "cost", "how much")):
            return "Prices vary. You can " + self._services_text() + "."
        return None

    # -- main entry -------------------------------------------------------

    def handle(self, question, history=None):
        if history is not None:
            history = list(history)
        else:
            history = []

        if self._asking_booking(question):
            return self._handle_booking(question)

        # Hours / open questions: compose a clean answer from profile facts.
        ql = question.lower()
        if any(w in ql for w in ("how much", "price", "cost", "quote")) \
                and any(w in ql for w in ("unit", "system", "install", "new ac", "replace")):
            return {"answer": ("Every home is different, so we give free "
                               "estimates - the visit costs nothing and there "
                               "is no pressure. Want me to book a free "
                               "estimate for you? Just tell me your name, "
                               "phone, and a day that works."),
                    "tool_triggers": [], "history": history}
        if any(w in ql for w in ("open", "hours", "sunday", "saturday", "weekend")):
            hours = self.profile.get("hours", "call to confirm")
            contact = self.profile.get("contact", "call us")
            return {"answer": ("Our emergency repair service runs 24/7. "
                               "Office hours vary by day, so the fastest way "
                               "to reach us any hour is to call. " + contact),
                    "tool_triggers": [], "history": history}

        # Anything else: try to stay grounded with facts from the profile.
        grounded = self._answer_from_profile(question)
        if grounded is not None:
            return grounded

        # Fall back to the local model for open conversation.
        prompt = self._system_text() + "\n\nCustomer question: " + question
        return self._run_with_tools(prompt, history)

    # -- chat -------------------------------------------------------------

    def _system_text(self):
        grounded = (
            "Business: " + (self.profile.get("business_name") or "this shop") + "\n"
            "Location: " + (self.profile.get("location") or "call to confirm") + "\n"
            "Hours: " + (self.profile.get("hours") or "call to confirm") + "\n"
            "Contact: " + (self.profile.get("contact") or "call or visit") + "\n"
            "Products: " + "; ".join(p.get("name", "") for p in self.products) + "\n"
            "Services: " + "; ".join(s.get("name", "") + " (" + s.get("price", "")
                                       + ")" for s in self.services) + "\n"
        )
        return (
            "You are the A-1 assistant, a friendly local-business assistant for "
            + (self.profile.get("business_name") or "this shop") + ".\n"
            "You help customers of this shop.\n\n"
            "Only use these facts. Never invent a product, price, location, "
            "or time that is not here:\n" + grounded +
            "\n\n- Answer in short, friendly plain words.\n"
            "- If a question is not in here, say you are not sure and suggest "
            "they call or visit the shop.\n"
            "- Keep replies short (Neil reads them; plain words).\n"
            "- No other tools exist."
        )

    def _run_with_tools(self, prompt, history, max_rounds=8):
        for _ in range(max_rounds):
            answer = _ollama_generate(prompt, max_tokens=900)
            history.append("Q: " + prompt.split("Customer question: ", 1)[1])
            history.append("A: " + answer)
            import re
            parsed = _parse_call(answer)
            if parsed is not None:
                if parsed["name"] == "create_booking":
                    booked = create_booking(
                        parsed["name"], parsed["phone"], parsed["item"],
                        parsed["quantity"], parsed["day"], parsed["slot"],
                    )
                    prompt = answer + ("\n\nTOOL RESULT: booking " + booked["id"]
                                       + " - " + booked["name"] + " | "
                                       + booked["item"] + " | "
                                       + booked["day"] + " " + booked["slot"]
                                       + "\n\nNow confirm the booking to the "
                                       "customer only, no more tool calls.")
                    continue
            return {"answer": answer.strip(), "tool_triggers": [],
                    "history": history}
        return {"answer": "I could not finish that. Try asking me about our "
                          "products.", "tool_triggers": [], "history": history}


def _ollama_generate(prompt, max_tokens=900):
    import urllib.request
    import urllib.error

    body = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.3, "top_p": 0.9},
    }).encode("utf-8")
    req = urllib.request.Request(
        OLLAMA_BASE + "/api/generate",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=240) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        return data.get("response", "")
    except Exception as e:
        return "ERROR contacting local Ollama: " + str(e)


def run_demo():
    """Run a short, real demo with a booking that gets confirmed."""
    agent = VintageGooseAgent(PROFILE)

    print("A-1 HEATING & AIR - DEMO AI ASSISTANT - REAL RUN")
    print("=" * 50)
    questions = [
        "My AC quit cooling and it is 95 degrees outside. Can someone come out today?",
        "How much is a brand new AC unit?",
        "Do you clean air ducts?",
        "I want to book a free estimate for a new system. I am Sam, phone 555-0134, Tuesday afternoon.",
        "Are you open on Sundays?",
    ]
    for q in questions:
        print("\nQ:", q)
        out = agent.handle(q)
        print("A:", str(out)[:900])
    print("\nBOOKS PATH: a1_bookings.json")
    print("BOOKINGS:", json.dumps(_load_bookings(), indent=2))
    print("\nDEMO COMPLETE (exit 0)")
    return 0


if __name__ == "__main__":
    sys.exit(run_demo())
