#!/usr/bin/env python3
import json
import urllib.request
import urllib.parse

def web_search(query, max_results=3):
    url = "https://en.wikipedia.org/w/api.php?" + urllib.parse.urlencode({
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": max_results
    })
    request = urllib.request.Request(url, headers={"User-Agent": "DestinyResearchBot/1.0"})
    with urllib.request.urlopen(request, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
    results = []
    for item in data.get("query", {}).get("search", []):
        title = item.get("title", "")
        snippet = item.get("snippet", "").replace('<span class="searchmatch">', '').replace('</span>', '')
        results.append({"title": title, "snippet": snippet})
    return results

if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else "test query"
    print(json.dumps(web_search(q), indent=2))
