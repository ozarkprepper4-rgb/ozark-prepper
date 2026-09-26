#!/usr/bin/env python3
"""ML Brain predictor: learning_predictor.py — analyzes experience patterns."""
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

LOG_FILE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/Logs/learning_log.json")
OUTPUT_LOG = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/ML_Brain/predictor.log")

def ensure_logs():
    if not LOG_FILE.exists():
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, 'w') as f:
            json.dump([], f)

def analyze_failures():
    """Identify patterns in recent failures."""
    ensure_logs()
    with open(LOG_FILE, 'r') as f:
        data = json.load(f)
    recent = [e for e in data if datetime.fromisoformat(e['timestamp']) > datetime.now(timezone.utc).replace(tzinfo=None) - timedelta(days=7)]
    failures = [e for e in recent if e.get('status') in ('failure', 'error', 'partial')]
    patterns = {}
    for f in failures:
        key = f.get('task_type', 'unknown')
        patterns[key] = patterns.get(key, 0) + 1
    return patterns

def predict_high_risk():
    """Return a simple list of high-risk patterns based on recent failures."""
    patterns = analyze_failures()
    warnings = []
    for key, count in patterns.items():
        if count >= 2:
            warnings.append(f"High frequency failure: {key} ({count} recent)")
    return warnings

def save_prediction_report(warnings):
    """Save structured prediction results for other Destiny components."""
    report_file = OUTPUT_LOG.parent / "prediction_results.json"

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "high_risk_patterns": warnings,
        "count": len(warnings)
    }

    report_file.write_text(
        json.dumps(report, indent=2),
        encoding="utf-8"
    )

    return report_file


def log_event(message: str):
    """Log predictor activity for auditing."""
    OUTPUT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_LOG, 'a') as f:
        f.write(f"[{datetime.now(timezone.utc).isoformat()}] {message}\n")

if __name__ == "__main__":
    warnings = predict_high_risk()

    for w in warnings:
        print(f"[ML PREDICTOR] {w}")
        log_event(w)

    if not warnings:
        print("[ML PREDICTOR] No high-risk patterns detected.")
        log_event("No high-risk patterns detected.")

    report = save_prediction_report(warnings)
    print(f"[ML PREDICTOR] Structured report: {report}")
