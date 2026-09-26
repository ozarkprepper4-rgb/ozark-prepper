#!/usr/bin/env python3

import sys
import json
from pathlib import Path

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")

sys.path.insert(0, str(BASE))

from cognitive_orchestrator import run
from pre_execution_verifier import verify_task


def main():
    if len(sys.argv) < 2:
        print('Usage: destiny-task "task to perform"')
        sys.exit(1)

    task = " ".join(sys.argv[1:])

    print()
    print("=== DESTINY TASK ENGINE ===")
    print("Task:", task)
    print()
    print("Processing through Three-Brain architecture...")
    print()

    result = run(task)

    if result.get("status") == "BLOCKED":
        print("PRE-EXECUTION VERIFICATION: FAILED")
        sys.exit(1)

    print("=== RESULT ===")
    print("Status:", result.get("status", "UNKNOWN"))

    dl = result.get("dl_result", {})

    reply = dl.get("model_response") or result.get("model_response")
    if reply:
        print()
        print("Destiny:")
        print(reply)

    print()
    print("=== PIPELINE ===")

    for name, status in result.get("pipeline", {}).items():
        print(f"{name}: {status}")

    print()
    print("DESTINY_TASK_COMPLETE")


if __name__ == "__main__":
    main()
