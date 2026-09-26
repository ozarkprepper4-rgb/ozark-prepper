#!/usr/bin/env python3
"""Adaptive Brain: adaptive_brain.py — detects new preferences and updates behavior rules."""
import json
from datetime import datetime
from pathlib import Path

OBSERVED_LOG = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/Adaptive_Brain/observed_preferences.json")
BEHAVIOR_LOG = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/Adaptive_Brain/adaptation_log.json")
RULES_FILE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/Adaptive_Brain/behavior_rules.json")

def init_all():
    for f in [OBSERVED_LOG, BEHAVIOR_LOG, RULES_FILE]:
        f.parent.mkdir(parents=True, exist_ok=True)
        if not f.exists():
            with open(f, 'w') as file:
                json.dump([] if f == OBSERVED_LOG or 'log' in f.name else {}, file)

def observe_new_preference(source_text: str, preference_type: str, value: str):
    """Record a new observed preference from interaction."""
    init_all()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "source": source_text[:200],
        "preference_type": preference_type,
        "value": value,
        "verified": False  # Requires a future behavior change to verify
    }
    with open(OBSERVED_LOG, 'r+') as f:
        data = json.load(f)
        data.append(entry)
        f.seek(0)
        json.dump(data, f, indent=2)
    return entry

def apply_behavior_rule(rule: dict) -> str:
    """Apply a behavior rule and return the adapted response style instruction."""
    # Minimal behavior change: return an instruction string
    preference_type = rule.get('preference_type')
    value = rule.get('value')
    if preference_type == 'response_length':
        if value == 'short':
            return "Use 1-2 short paragraphs. No jargon. Yes/No when possible."
        elif value == 'detailed':
            return "Provide full explanation with context."
    elif preference_type == 'communication_tone':
        if value == 'warm_simple':
            return "Keep explanations warm and extremely simple."
        elif value == 'direct':
            return "Direct, brief, no extra warmth."
    return "Default behavior."

def save_rule(preference_type: str, value: str, source: str):
    """Save a verified rule to rules file and update behavior."""
    init_all()
    rule = {
        "timestamp": datetime.now().isoformat(),
        "preference_type": preference_type,
        "value": value,
        "source": source[:100],
        "applied": True
    }
    with open(RULES_FILE, 'r+') as f:
        rules = json.load(f)
        rules[preference_type] = value  # Overwrite with latest verified rule
        f.seek(0)
        json.dump(rules, f, indent=2)
    with open(BEHAVIOR_LOG, 'a') as f:
        f.write(f"[{datetime.now().isoformat()}] Applied rule: {preference_type}={value}\n")
    return rule

def get_current_rules() -> dict:
    init_all()
    with open(RULES_FILE, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    import sys
    # Demo: observe and apply a new preference
    observe_new_preference("User asked 'Keep it short, please'", "response_length", "short")
    current = get_current_rules()
    if "response_length" not in current:
        save_rule("response_length", "short", "User interaction 2026-08-23")
    print(f"Rules: {get_current_rules()}")
    print(f"Behavior instruction: {apply_behavior_rule({'preference_type': 'response_length', 'value': 'short'})}")
