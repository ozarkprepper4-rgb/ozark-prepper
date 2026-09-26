#!/usr/bin/env python3

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")

sys.path.insert(0, str(BASE))

from cognitive_orchestrator import run
from pre_execution_verifier import verify_task


ENGINE_LOG = BASE / "Logs/autonomous_task_engine.json"


def load_log():
    if not ENGINE_LOG.exists():
        return []

    try:
        return json.loads(ENGINE_LOG.read_text(encoding="utf-8"))
    except Exception:
        return []


def save_log(data):
    ENGINE_LOG.parent.mkdir(parents=True, exist_ok=True)
    ENGINE_LOG.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8"
    )


def execute(task):
    start = time.time()

    verification = verify_task(task)

    if verification.get("status") != "READY":
        return {
            "status": "BLOCKED",
            "pipeline": {
                "pre_execution_verification": "FAIL"
            },
            "verification": verification,
            "model_response": ""
        }

    result = run(task)

    duration = round(time.time() - start, 4)

    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "task": task,
        "duration": duration,
        "status": result.get("status", "UNKNOWN"),
        "pipeline": result.get("pipeline", {}),
        "model_response": (
            result.get("model_response")
            or result.get("dl_result", {}).get("model_response", "")
        )
    }

    history = load_log()
    history.append(entry)
    save_log(history)

    return entry


def main():
    if len(sys.argv) < 2:
        print('Usage: autonomous_task_engine.py "task"')
        sys.exit(1)

    task = " ".join(sys.argv[1:])

    print()
    print("=== DESTINY AUTONOMOUS TASK ENGINE ===")
    print("Task:", task)
    print()
    print("Phase 1: Three-Brain reasoning")
    print("Phase 2: Verification")
    print("Phase 3: Learning capture")
    print()

    result = execute(task)

    print("=== VERIFIED RESULT ===")
    print("Status:", result["status"])
    print("Duration:", result["duration"], "seconds")

    if result["model_response"]:
        print()
        print("Destiny:")
        print(result["model_response"])

    print()
    print("=== PIPELINE ===")

    for name, status in result["pipeline"].items():
        print(f"{name}: {status}")

    print()
    print("History:", ENGINE_LOG)
    print()
    print("DESTINY_AUTONOMOUS_TASK_COMPLETE")


if __name__ == "__main__":
    main()
