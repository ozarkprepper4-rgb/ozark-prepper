#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
VAULT = Path("/home/destiny/Obsidian/Destiny")
log = VAULT / "Pipeline_Log.md"
task = VAULT / "next_youtube_task.md"
stamp = datetime.now().isoformat(timespec="seconds")
line = f"{stamp} pipeline ran. Next: one Ozark Prepper YouTube idea from the book list.\n"
log.write_text((log.read_text(encoding="utf-8") if log.exists() else "# Pipeline Log\n\n") + line, encoding="utf-8")
task.write_text("Pick one book from Ozark_Ebook_Catalog.md.\nWrite one YouTube title.\nDo not publish.\nDo not touch ozarkprepper.com.\n", encoding="utf-8")
print("PIPELINE_OK")
print(line.strip())
