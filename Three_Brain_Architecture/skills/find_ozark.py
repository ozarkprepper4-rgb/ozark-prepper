from pathlib import Path

ROOT = Path("/home/destiny/Obsidian")

def run(*a, **k):
    hits = []
    for f in sorted(f for f in ROOT.rglob("**/*") if f.is_file()):
        if f.is_file() and ("ozark" in f.name.lower()):
            hits.append(str(f.relative_to(ROOT).as_posix()))
    return '\n'.join(sorted(hits)) if hits else 'none found'
