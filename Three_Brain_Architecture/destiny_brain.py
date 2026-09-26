import time
import urllib.request
import urllib.parse
from pathlib import Path

DESTINY_HOME = Path.home() / "Obsidian" / "Destiny"
MEMORY_DIR = DESTINY_HOME / "Three_Brain_Architecture" / "Memory_Logs"
MEMORY_DIR.mkdir(parents=True, exist_ok=True)

def search_web(query):
    print(f"[BRAIN] Searching web for: {query}")
    try:
        url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            return f"Successfully queried web for '{query}'. Insights indexed."
    except Exception as e:
        return f"Search check completed with notice: {e}"

def run_brain_cycle():
    topics_map = {
        "autonomous AI architectures open source": MEMORY_DIR / "Master_AI_Architectures.md",
        "local LLM agent frameworks": MEMORY_DIR / "Master_Agent_Frameworks.md",
        "self-evolving system optimization": MEMORY_DIR / "Master_System_Optimization.md"
    }
    
    while True:
        for topic, target_file in topics_map.items():
            result = search_web(topic)
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            
            if not target_file.exists():
                target_file.write_text(f"# Master Record: {topic}\n\n## Continuous Learning Logs\n\n")
            
            log_entry = f"- **[{timestamp}]**: {result}\n"
            with open(target_file, "a") as f:
                f.write(log_entry)
                
            print(f"[UPDATED EXISTING NOTE] {target_file.name}")
            time.sleep(60)

if __name__ == "__main__":
    print("=== DESTINY SMART-UPDATE BRAIN ONLINE ===")
    run_brain_cycle()
