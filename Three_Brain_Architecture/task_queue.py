#!/usr/bin/env python3

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
QUEUE = BASE / "Tasks/task_queue.json"
HISTORY = BASE / "Logs/task_queue_history.json"

sys.path.insert(0, str(BASE))

from cognitive_orchestrator import run
from pre_execution_verifier import verify_task


def load_json(path, default):
    if not path.exists():
        return default

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8"
    )


def add_task(task):
    queue = load_json(QUEUE, [])

    entry = {
        "id": len(queue) + 1,
        "task": task,
        "status": "pending",
        "created": datetime.now(timezone.utc).isoformat()
    }

    queue.append(entry)
    save_json(QUEUE, queue)

    print(f"TASK_ADDED: {entry['id']}")


def process_queue():
    queue = load_json(QUEUE, [])
    history = load_json(HISTORY, [])

    pending = [x for x in queue if x.get("status") == "pending"]

    print()
    print("=== DESTINY PERSISTENT TASK QUEUE ===")
    print("Pending tasks:", len(pending))
    print()

    for entry in pending:
        task = entry["task"]

        print(f"Processing task #{entry['id']}")
        print("Task:", task)
        print()

        verification = verify_task(task)

        if verification.get("status") != "READY":
            entry["status"] = "blocked"
            entry["completed"] = datetime.now(timezone.utc).isoformat()
            entry["verification"] = verification

            print("Pre-execution verification: BLOCKED")
            continue

        print("Pre-execution verification: PASS")

        start = time.time()
        result = run(task)
        duration = round(time.time() - start, 4)

        response = (
            result.get("model_response")
            or result.get("dl_result", {}).get("model_response", "")
        )

        entry["status"] = (
            "completed"
            if result.get("status") == "PASS"
            else "failed"
        )
        entry["completed"] = datetime.now(timezone.utc).isoformat()
        entry["duration"] = duration
        entry["response"] = response
        entry["pipeline"] = result.get("pipeline", {})

        history.append(entry.copy())

        print("Status:", entry["status"])
        print("Duration:", duration, "seconds")
        print()

    save_json(QUEUE, queue)
    save_json(HISTORY, history)

    print("=== QUEUE COMPLETE ===")
    print("Tasks processed:", len(pending))
    print("History:", HISTORY)


def main():
    if len(sys.argv) < 2:
        print('Usage:')
        print('  task_queue.py add "task"')
        print('  task_queue.py run')
        print('  task_queue.py status')
        raise SystemExit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            raise SystemExit('Missing task.')
        add_task(" ".join(sys.argv[2:]))

    elif command == "run":
        process_queue()

    elif command == "status":
        queue = load_json(QUEUE, [])

        print()
        print("=== TASK QUEUE STATUS ===")

        for entry in queue:
            print(
                f"#{entry['id']} "
                f"[{entry['status']}] "
                f"{entry['task']}"
            )

        print()

    else:
        raise SystemExit("Unknown command.")


if __name__ == "__main__":
    main()
