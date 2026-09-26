#!/usr/bin/env python3

import json
import time
from pathlib import Path

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
QUEUE = BASE / "Tasks/task_queue.json"

sys_path = str(BASE)

import sys
if sys_path not in sys.path:
    sys.path.insert(0, sys_path)

from task_queue import process_queue


POLL_SECONDS = 10


def pending_tasks():
    if not QUEUE.exists():
        return False

    try:
        data = json.loads(QUEUE.read_text(encoding="utf-8"))
        return any(
            item.get("status") == "pending"
            for item in data
        )
    except Exception:
        return False


def main():
    print("=== DESTINY AUTONOMOUS WORKER ===")
    print(f"Polling every {POLL_SECONDS} seconds.")
    print("Press Ctrl+C to stop.")
    print()

    while True:
        try:
            if pending_tasks():
                process_queue()
            else:
                print("No pending tasks. Waiting...")

            time.sleep(POLL_SECONDS)

        except KeyboardInterrupt:
            print()
            print("DESTINY_AUTONOMOUS_WORKER_STOPPED")
            break

        except Exception as exc:
            print("Worker error:", type(exc).__name__, str(exc))
            time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
