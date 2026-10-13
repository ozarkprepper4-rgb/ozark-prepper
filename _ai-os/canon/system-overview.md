# AI Operating System — Master Overview

## What This Is
This is the complete AI Operating System built for Neil Wilcox. It is based on the **Infinite Brain OS** framework shown in the video "I Built a Complete AI Operating System for my Company (Full Stack)."

The system is a git-backed knowledge operating system. Everything is plain Markdown and YAML. Nothing is hidden. Everything is versioned, owned by Neil, and readable by any file-reading agent.

## Core Layers

### 1. Canon (Principles)
- **core-doctrine.md** — identity, foundation, principles, architecture, entity types, values
- **agent-load-order.md** — who runs in what order, from Neil down to sub-agents

### 2. Tools (Capabilities)
- **README.md** — tool registry with name, purpose, inputs, outputs, usage rules
- **TOOLS.md** — existing tools catalog in the main vault

### 3. Memory (Knowledge)
- **README.md** — memory principles, types, protocol
- **Knowledge_Base.md** — confirmed facts and self inventory

### 4. Projects (Work)
- **INDEX.md** — project index with status
- Each project has its own folder with PLAN.md, NOTES.md, code/, test/, .bak/

### 5. Workflows (Processes)
- **README.md** — workflow principles and map
- **build-project.md** — create a new project
- **video-analysis.md** — watch and analyze a video
- **knowledge-update.md** — update the vault
- **session-start.md** — start a session
- **session-closeout.md** — end a session

### 6. Sessions (Tracking)
- **README.md** — session protocol
- **active/** — currently running sessions
- **closed/** — finished sessions with records
- **logs/** — detailed logs
- **reviews/** — after-action reviews

### 7. Operators (People)
- **INDEX.md** — the operator and his profile

## The Wire Map
```
Neil (operator)
   |
   v
[core-doctrine]
   |
   v
[agent-load-order] --> routes tasks to:
   |                       |
   v                       v
[tools]              [Pepper/operations]
   |                       |
   v                       v
[memory]           [Victoria/revenue]
   |                       |
   v                       v
[projects]        [Denise/capital]
   |                       |
   v                       v
[workflows]      [sub-agents/auditing]
   |                       |
   v                       v
[sessions]        [external research]
   |
   v
[git: full history]
```

## Independence Rules
1. Neil is the human. I never spend money without his OK.
2. No publishing or running outside this computer without Neil's OK.
3. No passwords, keys, or vault secrets in any tool.
4. Reuse before building — check the toolbox first.
5. Simple, plain, warm. One step at a time. No jargon.
6. Every session advances at least one capability.

## First-Time Setup Checklist
When setting up this system for the first time:
1. Clone or create the git-backed vault
2. Create the _ai-os/ namespace structure
3. Write core-doctrine.md
4. Write agent-load-order.md
5. Write tools/README.md
6. Write memory/README.md
7. Write projects/INDEX.md
8. Write workflows/README.md
9. Write sessions/README.md
10. Write operators/INDEX.md
11. Wire the master operations register
12. Commit to git
13. Test the system
14. Report to Neil

## Verification
After setup, run:
- `git log --oneline -5` — confirm commits exist
- `ls _ai-os/` — confirm namespace structure
- `cat _ai-os/canon/core-doctrine.md` — verify doctrine
- `cat _ai-os/tools/README.md` — verify tool registry
- `cat _ai-os/operators/INDEX.md` — verify operator profile
