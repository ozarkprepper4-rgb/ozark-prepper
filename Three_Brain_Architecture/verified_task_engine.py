#!/usr/bin/env python3

import sys
from pathlib import Path

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")

sys.path.insert(0, str(BASE))

from pre_execution_verifier import verify_task
from cognitive_orchestrator import run


def main():
    if len(sys.argv) < 2:
        print('Usage: verified_task_engine.py "task"')
        raise SystemExit(1)

    task = " ".join(sys.argv[1:])

    print()
    print("=== DESTINY VERIFIED TASK ENGINE ===")
    print("Task:", task)
    print()

    verification = verify_task(task)

    print("Pre-execution verification:", verification["status"])

    if verification["status"] != "READY":
        print("TASK BLOCKED: environment verification failed.")
        raise SystemExit(2)

    print("Verification passed.")
    print("Executing through Three-Brain architecture...")
    print()

    result = run(task)

    print()
    print("=== VERIFIED EXECUTION RESULT ===")
    print("Status:", result.get("status", "UNKNOWN"))

    response = (
        result.get("model_response")
        or result.get("dl_result", {}).get("model_response", "")
    )

    if response:
        print()
        print("Destiny:")
        print(response)

    print()
    print("=== PIPELINE ===")

    for name, status in result.get("pipeline", {}).items():
        print(f"{name}: {status}")

    print()
    print("DESTINY_VERIFIED_TASK_COMPLETE")


if __name__ == "__main__":
    main()
