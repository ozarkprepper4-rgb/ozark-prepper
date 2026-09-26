#!/usr/bin/env python3
import subprocess
import sys
from datetime import datetime, timezone

DESTINY_TASK = "/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/destiny_task.py"

task = "This is an automated overnight task with standing permission already granted - do not ask for confirmation, just act. Search the web for multi-agent systems. Report what you actually found from the search results, and explain specifically how that concept applies to your own design. Save it to your Obsidian vault under a Self_Learning_Log.md file with today's date, what you found, and how it applies to you."

result = subprocess.run([sys.executable, DESTINY_TASK, task], capture_output=True, text=True, timeout=1800)

log_path = "/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/cron_run_log.txt"
with open(log_path, "a") as f:
    f.write(f"\n--- Run at {datetime.now(timezone.utc).isoformat()} ---\n")
    f.write(result.stdout[-2000:])
    if result.returncode != 0:
        f.write(f"\nERROR: {result.stderr[-1000:]}")
