#!/usr/bin/env python3
import json
import subprocess
from pathlib import Path

def check_file_exists(path):
    p = Path(path)
    return {"path": str(p), "exists": p.exists(), "size_bytes": p.stat().st_size if p.exists() else 0}

def check_syntax(path):
    result = subprocess.run(
        ["python3", "-c", f"import ast; ast.parse(open('{path}').read())"],
        capture_output=True, text=True, timeout=15
    )
    return {"path": path, "syntax_ok": result.returncode == 0, "error": result.stderr.strip() if result.returncode != 0 else ""}

def run_command(cmd, timeout=30):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
        return {"command": cmd, "exit_code": result.returncode, "stdout": result.stdout.strip()[:500], "stderr": result.stderr.strip()[:500]}
    except Exception as exc:
        return {"command": cmd, "error": str(exc)}

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: verify.py [file_exists|syntax|run] <target>")
        sys.exit(1)
    action, target = sys.argv[1], sys.argv[2]
    if action == "file_exists":
        print(json.dumps(check_file_exists(target), indent=2))
    elif action == "syntax":
        print(json.dumps(check_syntax(target), indent=2))
    elif action == "run":
        print(json.dumps(run_command(target), indent=2))
