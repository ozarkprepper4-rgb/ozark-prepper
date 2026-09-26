import subprocess
from pathlib import Path

OMARCHY = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/skills/omarchy_command.sh")

def run(command, environment="mint", timeout=60):
    env = environment.strip().lower()

    if env in ("mint", "host", "linuxmint"):
        args = ["bash", "-lc", command]
    elif env == "omarchy":
        args = [str(OMARCHY), command]
    elif env == "ubuntu":
        args = ["/bedrock/bin/strat", "ubuntu", "sh", "-c", command]
    elif env == "arch":
        args = ["/bedrock/bin/strat", "arch", "sh", "-c", command]
    elif env == "kali":
        args = ["docker", "exec", "destiny-kali", "sh", "-c", command]
    else:
        return {
            "status": "error",
            "environment": env,
            "command": command,
            "exit_code": 1,
            "stdout": "",
            "stderr": "Unknown or unverified environment: " + env
        }

    result = subprocess.run(
        args,
        capture_output=True,
        text=True,
        timeout=timeout
    )

    return {
        "status": "success" if result.returncode == 0 else "error",
        "environment": env,
        "command": command,
        "exit_code": result.returncode,
        "stdout": result.stdout.strip(),
        "stderr": result.stderr.strip()
    }
