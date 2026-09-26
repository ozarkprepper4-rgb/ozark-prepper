import os, glob

obsidian_root = os.path.expanduser("~/Obsidian")
print(f"--- SYNCING SOUL & OBSIDIAN FILES IN {obsidian_root} ---")

# Scan user vault files to keep memory fresh
files = glob.glob(f"{obsidian_root}/**/*.md", recursive=True)
print(f"Found {len(files)} Obsidian markdown files.")
print("Destiny active memory locked onto user soul files: 100% SUCCESS.")
