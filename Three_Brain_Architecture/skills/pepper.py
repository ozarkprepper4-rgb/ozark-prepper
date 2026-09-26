# Pepper - Destiny's Chief Operations Assistant
# Operational dispatcher under Destiny's direct authority.

from pathlib import Path
import environment_tool

BASE = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture")
PEPPER_LOG = Path("/home/destiny/Obsidian/Pepper/Pepper_Operations_Log.md")


def run_environment(command, environment="mint"):
    """Use Destiny's shared Linux environment executor."""
    return environment_tool.run(command, environment, timeout=60)


def run_victoria():
    """Run one existing Victoria/Ozark Prepper team cycle."""
    import victoria_team_cycle
    return victoria_team_cycle.run()


def dispatch(task_type="status", **kwargs):
    """Central operational dispatcher used under Destiny's authority."""
    task_type = task_type.strip().lower()

    if task_type == "environment":
        command = kwargs.get("command", "")
        environment = kwargs.get("environment", "mint")
        if not command:
            return {"status": "error", "agent": "pepper", "error": "No command supplied."}

        result = run_environment(command, environment)
        return {
            "status": result["status"],
            "agent": "pepper",
            "delegated_to": environment,
            "result": result,
        }

    if task_type in ("victoria", "ozark_prepper"):
        result = run_victoria()
        return {
            "status": "success",
            "agent": "pepper",
            "delegated_to": "victoria",
            "result": result,
        }

    if task_type == "status":
        return {
            "status": "success",
            "agent": "pepper",
            "role": "Chief Operations Assistant under Destiny",
            "shared_environment_tool": True,
            "victoria_workflow": True,
        }

    return {
        "status": "error",
        "agent": "pepper",
        "error": "Unknown dispatch type: " + task_type,
    }


def run():
    return dispatch("status")


if __name__ == "__main__":
    print(run())
