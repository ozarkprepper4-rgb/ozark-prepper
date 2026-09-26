import json, os

vault_dir = "/home/destiny/Obsidian/Destiny/Three_Brain_Architecture"
notes_dir = os.path.join(vault_dir, "Vault_Sync")
os.makedirs(notes_dir, exist_ok=True)

# 1. Sync Memory
memory_file = os.path.join(vault_dir, ".idea_memory.json")
try:
    with open(memory_file, "r") as f:
        mem_data = json.load(f)
except Exception:
    mem_data = []

mem_note = "# Destiny Live Memory Log\n\n> *Synced automatically from core system memory.*\n\n"
for item in mem_data:
    mem_note += f"## {item.get('topic', 'Untitled')}\n"
    mem_note += f"- **Context:** {item.get('context', 'N/A')}\n"
    mem_note += f"- **Action Plan:** {item.get('action_plan', 'N/A')}\n"
    mem_note += f"- **Saved:** {item.get('date_saved', 'N/A')}\n\n"

with open(os.path.join(notes_dir, "Destiny_Memory_Sync.md"), "w") as f:
    f.write(mem_note)

# 2. Sync Task History
task_file = os.path.join(vault_dir, "Logs", "task_queue_history.json")
try:
    with open(task_file, "r") as f:
        task_data = json.load(f)
except Exception:
    task_data = []

task_note = "# Destiny Task & Operations History\n\n> *Real execution records from background runs.*\n\n"
for t in task_data[-10:]:
    task_note += f"### Task ID: {t.get('id', 'N/A')}\n"
    task_note += f"- **Task:** {t.get('task', 'N/A')}\n"
    task_note += f"- **Status:** {t.get('status', 'N/A')}\n"
    task_note += f"- **Completed:** {t.get('completed', 'N/A')}\n"
    task_note += f"- **Response Summary:** `{str(t.get('response', 'N/A'))[:150]}...`\n\n"

with open(os.path.join(notes_dir, "Destiny_Task_Sync.md"), "w") as f:
    f.write(task_note)

print("SUCCESS: All background files synced into Obsidian notes directory under Vault_Sync/.")
