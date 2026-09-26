from pathlib import Path
import json
from datetime import datetime, timezone

STORE_PATH = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/.idea_memory.json")

def save_idea(topic, context, reason_deferred=""):
    ideas = []
    if STORE_PATH.exists():
        try:
            ideas = json.loads(STORE_PATH.read_text())
        except Exception:
            ideas = []
    ideas.append({
        "topic": topic,
        "context": context,
        "reason_deferred": reason_deferred,
        "date_saved": datetime.now(timezone.utc).isoformat(),
        "revisited": False
    })
    STORE_PATH.write_text(json.dumps(ideas, indent=2))
    return "Idea saved: " + topic

def check_for_revisits(days_threshold=30):
    if not STORE_PATH.exists():
        return []
    ideas = json.loads(STORE_PATH.read_text())
    now = datetime.now(timezone.utc)
    due = []
    for idea in ideas:
        if idea.get("revisited"):
            continue
        saved = datetime.fromisoformat(idea["date_saved"])
        age_days = (now - saved).days
        if age_days >= days_threshold:
            due.append(idea)
    return due

def mark_revisited(topic):
    if not STORE_PATH.exists():
        return "No ideas stored."
    ideas = json.loads(STORE_PATH.read_text())
    for idea in ideas:
        if idea["topic"] == topic:
            idea["revisited"] = True
    STORE_PATH.write_text(json.dumps(ideas, indent=2))
    return "Marked revisited: " + topic
