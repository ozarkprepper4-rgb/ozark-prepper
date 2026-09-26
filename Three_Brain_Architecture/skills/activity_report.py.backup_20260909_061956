#!/usr/bin/env python3

from pathlib import Path
from datetime import datetime, time, timedelta
import re

VAULT = Path("/home/destiny/Obsidian/Destiny")
SELF_LOG = VAULT / "Self_Check_Log.md"


def _last_night_window():
    """
    'Last night' = yesterday 6:00 PM through today 8:00 AM.
    If it is currently before 8:00 AM, use now as the end.
    """
    now = datetime.now()

    today_8am = datetime.combine(now.date(), time(8, 0))
    start = datetime.combine(now.date() - timedelta(days=1), time(18, 0))

    end = min(now, today_8am) if now < today_8am else today_8am
    return start, end


def _read_self_check_entries(start, end):
    if not SELF_LOG.exists():
        return []

    entries = []

    for raw in SELF_LOG.read_text(encoding="utf-8", errors="replace").splitlines():
        m = re.match(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\s+(.*)$", raw.strip())
        if not m:
            continue

        try:
            stamp = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M")
        except ValueError:
            continue

        if start <= stamp <= end:
            entries.append((stamp, m.group(2).strip()))

    return entries


def run(task=None):
    start, end = _last_night_window()
    entries = _read_self_check_entries(start, end)

    if not entries:
        return (
            f"I don't have any recorded autonomous activity between "
            f"{start.strftime('%Y-%m-%d %I:%M %p')} and "
            f"{end.strftime('%Y-%m-%d %I:%M %p')}."
        )

    errors = []
    web_events = []
    inventory_events = []
    deletion_events = []
    skill_snapshots = []

    for stamp, text in entries:
        lower = text.lower()

        if "error" in lower:
            errors.append((stamp, text))

        if "web_learn" in lower or "web " in lower:
            web_events.append((stamp, text))

        if "inventory" in lower:
            inventory_events.append((stamp, text))

        if "deleted" in lower:
            deletion_events.append((stamp, text))

        if "skills:" in lower or "skills=" in lower:
            skill_snapshots.append((stamp, text))

    lines = [
        f"Last night's recorded activity from {start.strftime('%I:%M %p')} "
        f"to {end.strftime('%I:%M %p')}:",
        "",
        f"- I recorded {len(entries)} autonomous self-check cycles."
    ]

    if web_events:
        # Show unique web-learning results without dumping repeated cycles.
        unique = []
        seen = set()

        for _, text in web_events:
            piece = text
            if piece not in seen:
                seen.add(piece)
                unique.append(piece)

        lines.append(f"- I recorded {len(web_events)} web-learning activity entries.")

        for text in unique[:3]:
            lines.append(f"  Evidence: {text}")

    if inventory_events:
        lines.append(f"- I recorded {len(inventory_events)} inventory activity entries.")
        lines.append(f"  Evidence: {inventory_events[-1][1]}")

    if deletion_events:
        deleted_something = [
            text for _, text in deletion_events
            if "deleted empty: none" not in text.lower()
            and "deleted=none" not in text.lower()
        ]

        if deleted_something:
            lines.append("- I recorded cleanup activity that deleted something.")
            for text in deleted_something[:3]:
                lines.append(f"  Evidence: {text}")
        else:
            lines.append(
                "- My cleanup checks ran, but the recorded entries say there "
                "were no empty notes to delete."
            )

    if errors:
        lines.append(f"- I recorded {len(errors)} error entries.")
        for _, text in errors[:3]:
            lines.append(f"  Error: {text}")
    else:
        lines.append("- I found no error entries in the recorded self-check activity for that window.")

    lines.extend([
        "",
        "This report comes from Self_Check_Log.md. "
        "I am reporting only recorded activity, not guessing about anything I may have done."
    ])

    return "\n".join(lines)


if __name__ == "__main__":
    print(run())
