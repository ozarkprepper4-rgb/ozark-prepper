from pathlib import Path
import json
import urllib.request
import sys
import ast

sys.path.insert(0, '/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/skills')
import safe_self_edit

def _ask_model(prompt):
    payload = {"model": "qwen2.5:14b", "prompt": prompt, "stream": False, "options": {"num_predict": 600, "temperature": 0.1}}
    req = urllib.request.Request("http://127.0.0.1:11434/api/generate", data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode()).get("response", "").strip()

def run(file_path, problem_description):
    target = Path(file_path)
    if not target.exists():
        return {"status": "failed", "error": "File does not exist"}

    original_code = target.read_text(encoding="utf-8")
    code = original_code

    for attempt in range(3):
        prompt = (
            "Here is a Python file:\n\n" + code +
            "\n\nProblem: " + problem_description +
            "\n\nIdentify the exact broken line or lines, copied exactly as they appear "
            "in the file. Respond in this exact format with no extra text:\n"
            "BROKEN:\n<exact broken line(s)>\n"
            "FIXED:\n<corrected line(s)>"
        )

        response = _ask_model(prompt)

        if "BROKEN:" not in response or "FIXED:" not in response:
            return {
                "status": "diagnosis_failed",
                "attempt": attempt + 1,
                "raw_response": response
            }

        try:
            broken = response.split("BROKEN:", 1)[1].split("FIXED:", 1)[0].strip()
            fixed = response.split("FIXED:", 1)[1].strip()
        except Exception as e:
            return {
                "status": "parse_failed",
                "attempt": attempt + 1,
                "error": str(e),
                "raw_response": response
            }

        if broken not in code:
            return {
                "status": "broken_text_not_found",
                "attempt": attempt + 1,
                "attempted": broken
            }

        test_code = code.replace(broken, fixed, 1)

        try:
            ast.parse(test_code)

            verify_prompt = (
                "A fix was proposed for this problem: " + problem_description +
                "\n\nOriginal broken code:\n" + broken +
                "\n\nProposed fix:\n" + fixed +
                "\n\nTrace through this fix step by step with a real example input. "
                "Show the actual calculation or logic result. "
                "Then on the final line only, write VERDICT: YES or VERDICT: NO."
            )
            verify_response = _ask_model(verify_prompt).strip().upper()

            if "VERDICT: YES" not in verify_response:
                if attempt < 2:
                    problem_description = (
                        problem_description +
                        "\n\nA previous fix attempt did not actually solve the problem: " + fixed +
                        "\nTry a genuinely different, correct approach."
                    )
                    continue
                return {
                    "status": "fix_did_not_solve_problem",
                    "attempt": attempt + 1,
                    "attempted_fix": fixed
                }
        except SyntaxError as e:
            if attempt < 2:
                problem_description = (
                    problem_description +
                    "\n\nPrevious repair attempt produced this syntax error: " +
                    str(e) +
                    "\nDo not repeat that mistake. Produce valid Python."
                )
                continue

            return {
                "status": "fix_has_syntax_error",
                "attempt": attempt + 1,
                "error": str(e)
            }

        result = safe_self_edit.edit(
            str(target),
            broken,
            fixed,
            reason="auto-diagnosed: " + problem_description
        )

        return {
            "status": "applied" if result.get("status") == "success" else "failed",
            "attempt": attempt + 1,
            "details": result
        }

    return {"status": "failed", "error": "Repair attempts exhausted"}

