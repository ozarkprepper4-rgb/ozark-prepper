#!/usr/bin/env python3
import subprocess
import json

def search_youtube(title, max_results=1):
    cmd = [
        "yt-dlp",
        f"ytsearch{max_results}:{title}",
        "--print", "%(id)s|%(title)s",
        "--no-warnings",
        "--skip-download",
        "--flat-playlist"
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    results = []
    for line in result.stdout.strip().split("\n"):
        if "|" in line:
            vid, vtitle = line.split("|", 1)
            results.append({"video_id": vid, "title": vtitle, "url": f"https://www.youtube.com/watch?v={vid}"})
    return results

if __name__ == "__main__":
    import sys
    title = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "test video"
    print(json.dumps(search_youtube(title), indent=2))
