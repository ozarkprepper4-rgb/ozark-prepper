#!/usr/bin/env python3

import sys
from pathlib import Path

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")

sys.path.insert(0, str(BASE))

from cognitive_orchestrator import run

if len(sys.argv) < 2:
    print("Usage: run_three_brain.py \"your task here\"")
    sys.exit(1)

task = " ".join(sys.argv[1:])

print()
print("=== DESTINY THREE-BRAIN ===")
print("Task:", task)
print()

result = run(task)

print()
print("=== THREE-BRAIN RESULT ===")
print("Status:", result.get("status", "UNKNOWN"))

if result.get("model_response"):
    print()
    print("Destiny:")
    print(result["model_response"])

print()
print("=== PIPELINE ===")

for name, status in result.get("pipeline", {}).items():
    print(f"{name}: {status}")

print()
print("THREE_BRAIN_TASK_COMPLETE")
