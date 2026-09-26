from pathlib import Path
import re
import ast
import json
import urllib.request
from datetime import datetime, timezone

SKILLS = Path('/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/skills')
LOG = Path('/home/destiny/Obsidian/Destiny/Forge_Log.md')

def _ask_model(prompt):
    payload = {"model": "qwen2.5:14b", "prompt": prompt, "stream": False, "options": {"num_predict": 400, "temperature": 0.2}}
    req = urllib.request.Request("http://127.0.0.1:11434/api/generate", data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode()).get("response", "").strip().replace("```python", "").replace("```", "").strip()

def _test_run(code):
    namespace = {}
    try:
        import io
        from contextlib import redirect_stdout

        exec(code, namespace)
        if "run" not in namespace:
            return False, "No run() function found in generated code"

        captured = io.StringIO()
        with redirect_stdout(captured):
            namespace["run"]()

        return True, "OK"
    except Exception as e:
        return False, str(e)

TOOLS_CATALOG = Path('/home/destiny/Obsidian/Destiny/TOOLS.md')

def already_exists(name):
    if not TOOLS_CATALOG.exists():
        return False
    catalog = TOOLS_CATALOG.read_text().lower()
    return name.lower().replace('.py', '') in catalog

def run(name, purpose='do the job'):
    if already_exists(name):
        return {"skill": name, "purpose": purpose, "status": "already_exists", "note": "Check TOOLS.md - this capability may already exist"}
    name = re.sub(r'[^A-Za-z0-9_\-]', '_', name).strip('_') or 'new_skill'
    if not name.endswith('.py'):
        name = name + '.py'
    path = SKILLS / name

    prompt = "Write a single Python function called run() that: " + purpose + ". The function should work with no arguments. Only output valid Python code, no explanation, no markdown formatting, just the code."
    code = _ask_model(prompt)

    result = None
    for attempt in range(3):
        try:
            ast.parse(code)
            works, msg = _test_run(code)
            if works:
                path.write_text(code)
                result = {"skill": name, "purpose": purpose, "status": "installed", "path": str(path), "attempts": attempt + 1}

                if TOOLS_CATALOG.exists():
                    catalog = TOOLS_CATALOG.read_text(encoding="utf-8")
                    entry = f"- {name} - {purpose}\n"
                    if name not in catalog:
                        TOOLS_CATALOG.write_text(catalog.rstrip() + "\n" + entry, encoding="utf-8")

                break
            else:
                fix_prompt = "This Python code failed when run with this error: " + msg + "\n\nHere is the code:\n" + code + "\n\nFix the error. Only output the corrected Python code, no explanation, no markdown."
                code = _ask_model(fix_prompt)
        except SyntaxError as e:
            fix_prompt = "This Python code has a syntax error: " + str(e) + "\n\nHere is the code:\n" + code + "\n\nFix the syntax error. Only output the corrected Python code, no explanation, no markdown."
            code = _ask_model(fix_prompt)

    if result is None:
        result = {"skill": name, "purpose": purpose, "status": "failed_after_retries", "error": "Could not produce working code after 3 attempts"}

    entry = "\n\n## " + datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC') + "\n**Skill:** " + name + "\n**Purpose:** " + purpose + "\n**Result:** " + str(result) + "\n---\n"
    with LOG.open("a", encoding="utf-8") as f:
        f.write(entry)

    return result
