#!/usr/bin/env python3

import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
LOG = BASE / "Logs/pre_execution_verification.json"


def verify_task(task):
    checks = {}

    # Required task validation
    checks["task_present"] = bool(task and task.strip())
    checks["task_length_valid"] = 1 <= len(task.strip()) <= 20000

    # Required local infrastructure
    checks["architecture_exists"] = BASE.exists()
    checks["ollama_available"] = shutil.which("ollama") is not None

    # Required Three-Brain components
    required = [
        BASE / "ML_Brain",
        BASE / "Adaptive_Brain",
        BASE / "DL_Brain",
        BASE / "cognitive_integration.py",
        BASE / "cognitive_orchestrator.py",
    ]

    checks["three_brain_components"] = all(p.exists() for p in required)

    # Explicitly identify whether this is a research task
    research_terms = (
        "research",
        "investigate",
        "compare",
        "analyze",
        "look up",
        "find out",
        "verify information",
    )

    checks["research_task"] = any(
        term in task.lower() for term in research_terms
    )

    # Safety: verifier itself never executes the requested task.
    checks["execution_performed"] = False

    passed = all(
        checks[key]
        for key in (
            "task_present",
            "task_length_valid",
            "architecture_exists",
            "ollama_available",
            "three_brain_components",
        )
    )

    result = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "task": task,
        "status": "READY" if passed else "BLOCKED",
        "checks": checks,
        "verification_before_execution": True,
        "execution_performed": False,
    }

    LOG.parent.mkdir(parents=True, exist_ok=True)

    history = []
    if LOG.exists():
        try:
            history = json.loads(LOG.read_text(encoding="utf-8"))
        except Exception:
            history = []

    history.append(result)
    LOG.write_text(json.dumps(history, indent=2), encoding="utf-8")

    return result


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print('Usage: pre_execution_verifier.py "task"')
        raise SystemExit(1)

    task = " ".join(sys.argv[1:])
    result = verify_task(task)

    print("=== PRE-EXECUTION VERIFICATION ===")
    print("Task:", task)
    print()

    for name, value in result["checks"].items():
        print(f"{name}: {'PASS' if value else 'FAIL'}")

    print()
    print("Verification status:", result["status"])
    print("Execution performed:", result["execution_performed"])
    print("Evidence:", LOG)
