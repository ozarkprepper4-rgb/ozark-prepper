#!/usr/bin/env python3
import json
from pathlib import Path

VAULT = Path("/home/destiny/Obsidian")
OUTPUT = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/extracted_notes.json")

def extract_all_notes():
    notes = []
    for md_file in VAULT.rglob("*.md"):
        try:
            content = md_file.read_text(encoding="utf-8", errors="ignore")
            notes.append({
                "path": str(md_file.relative_to(VAULT)),
                "title": md_file.stem,
                "content_length": len(content),
                "content_preview": content[:500]
            })
        except Exception:
            continue
    return notes

if __name__ == "__main__":
    notes = extract_all_notes()
    OUTPUT.write_text(json.dumps(notes, indent=2))
    print(f"EXTRACTED_{len(notes)}_NOTES")
    print(f"SAVED_TO: {OUTPUT}")
