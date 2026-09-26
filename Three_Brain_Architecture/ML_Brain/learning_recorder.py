#!/usr/bin/env python3
"""ML Brain: learning_recorder.py — Records task outcomes for pattern analysis."""
import json
import os
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/Logs")
LOG_FILE = LOG_DIR / "learning_log.json"

def init_log():
    """Create log file if it doesn't exist."""
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    if not LOG_FILE.exists():
        with open(LOG_FILE, 'w') as f:
            json.dump([], f)

def record_experience(task_type: str, status: str, duration: float, outcome: str, notes: str = ""):
    """Record a single learning experience."""
    init_log()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "task_type": task_type,
        "status": status,  # "success", "failure", "partial"
        "duration": duration,
        "outcome": outcome,
        "notes": notes
    }
    with open(LOG_FILE, 'r+') as f:
        data = json.load(f)
        data.append(entry)
        f.seek(0)
        json.dump(data, f, indent=2)
    print(f"Recorded: {task_type} | {status} | {duration}s")
    return entry

def get_recent(n=10):
    """Get last n experiences."""
    init_log()
    with open(LOG_FILE, 'r') as f:
        data = json.load(f)
    return data[-n:] if len(data) > n else data

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        record_experience(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 0.0, sys.argv[4] if len(sys.argv) > 4 else "")
        recent = get_recent(3)
        print(f"Recent entries: {len(recent)}")
    else:
        print("Usage: python learning_recorder.py <task_type> <status> <duration> <outcome>")