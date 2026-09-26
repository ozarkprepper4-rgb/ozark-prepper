from pathlib import Path
import sys
sys.path.insert(0, "/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
from video_watch import watch_video

LOG = Path("/home/destiny/Obsidian/Destiny/Video_Learning_Log.md")
url = sys.argv[1] if len(sys.argv) > 1 else ""
if not url:
    print("no url")
    raise SystemExit(1)

r = watch_video(url, max_chars=800)
vid = r.get("video_id", "unknown")
text = (r.get("transcript_summary") or "").strip()
if not text:
    print("no transcript")
    raise SystemExit(2)

block = f"""
## Learned {vid}
URL: {url}
Real transcript used. No fake tools.
Summary:
{text}

How Destiny uses this:
Save the useful idea in the vault. Do not install extra cloud apps. Use only tools that already exist on this machine.
"""
LOG.parent.mkdir(parents=True, exist_ok=True)
with LOG.open("a", encoding="utf-8") as f:
    f.write(block)
print("SAVED", vid)
print(text[:300])
