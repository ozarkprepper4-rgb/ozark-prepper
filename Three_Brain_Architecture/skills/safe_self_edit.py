from pathlib import Path
import ast
import shutil
from datetime import datetime, timezone

LOG = Path('/home/destiny/Obsidian/Destiny/Self_Edit_Log.md')

def edit(file_path, old_text, new_text, reason="self-repair"):
    target = Path(file_path)
    if not target.exists():
        return {"status": "failed", "error": "File does not exist: " + str(target)}

    original = target.read_text(encoding="utf-8")
    if old_text not in original:
        return {"status": "failed", "error": "old_text not found in file, no changes made"}
    if old_text == new_text:
        return {"status": "failed", "error": "proposed fix is identical to original text, no real change"}

    backup_path = target.with_suffix(target.suffix + ".backup_" + datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"))
    shutil.copy2(target, backup_path)

    updated = original.replace(old_text, new_text, 1)

    try:
        ast.parse(updated)
    except SyntaxError as e:
        entry = "\n\n## " + datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC') + "\n**File:** " + str(target) + "\n**Reason:** " + reason + "\n**Result:** FAILED - syntax error: " + str(e) + "\n**Backup:** " + str(backup_path) + "\n---\n"
        with LOG.open("a", encoding="utf-8") as f:
            f.write(entry)
        return {"status": "failed", "error": "New code has syntax error: " + str(e), "backup": str(backup_path)}

    target.write_text(updated, encoding="utf-8")
    entry = "\n\n## " + datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC') + "\n**File:** " + str(target) + "\n**Reason:** " + reason + "\n**Result:** SUCCESS\n**Backup:** " + str(backup_path) + "\n---\n"
    with LOG.open("a", encoding="utf-8") as f:
        f.write(entry)
    return {"status": "success", "backup": str(backup_path)}

def restore(file_path, backup_path):
    target = Path(file_path)
    backup = Path(backup_path)
    if not backup.exists():
        return {"status": "failed", "error": "Backup does not exist"}
    shutil.copy2(backup, target)
    return {"status": "restored", "from_backup": str(backup)}
