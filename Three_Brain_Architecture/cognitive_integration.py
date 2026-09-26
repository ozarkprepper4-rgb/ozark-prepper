#!/usr/bin/env python3

import json
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")

PREDICTION_FILE = BASE / "ML_Brain/prediction_results.json"
RULES_FILE = BASE / "Adaptive_Brain/behavior_rules.json"
OUTPUT_FILE = BASE / "Logs/cognitive_integration.json"


def load_json(path):
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def build_cognitive_directive():
    prediction = load_json(PREDICTION_FILE)
    rules = load_json(RULES_FILE)

    active_rules = []

    for key, rule in rules.items():
        if not isinstance(rule, dict):
            continue

        if rule.get("status") == "applied":
            active_rules.append({
                "rule": key,
                "instruction": rule.get("adaptation", ""),
                "trigger": rule.get("trigger", "")
            })

    directive = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "source": "ML_Brain → Adaptive_Brain",
        "high_risk_patterns": prediction.get("high_risk_patterns", []),
        "active_adaptive_rules": active_rules,
        "cognitive_directives": [
            rule["instruction"]
            for rule in active_rules
            if rule["instruction"]
        ],
        "status": "READY"
    }

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(
        json.dumps(directive, indent=2),
        encoding="utf-8"
    )

    return directive


if __name__ == "__main__":
    result = build_cognitive_directive()

    print()
    print("=== COGNITIVE INTEGRATION LAYER ===")
    print(f"ML patterns loaded: {len(result['high_risk_patterns'])}")
    print(f"Adaptive rules loaded: {len(result['active_adaptive_rules'])}")
    print(
        f"Cognitive directives generated: "
        f"{len(result['cognitive_directives'])}"
    )
    print(f"Status: {result['status']}")
    print()
    print("=== RESULT ===")
    print("COGNITIVE_INTEGRATION_LAYER_OK")
    print()
    print("Evidence:")
    print(OUTPUT_FILE)
