# Master Operations Register

## What This Is
This is the central dashboard for the AI Operating System. It tells Neil (and any agent) at a glance:
- What is running
- What is pending
- What has been verified
- What needs Neil

It is the single source of truth for system state.

## Current State

### Running (active agent tasks)
- [x] Software Library setup (README.md + index)
- [x] software-library skill (YAML header + instructions)
- [x] AI OS namespace structure (canon, tools, memory, projects, workflows, sessions)
- [x] Core doctrine and agent load order
- [x] Tool registry and workflow definitions
- [x] Session management
- [x] Master system prompt created
- [x] AI OS project folder created (ai-os-projects/ai-operating-system/)
- [x] Project verification test: ALL CHECKS PASS

### Pending (waiting on Neil or verification)
- [ ] Live daily operations register (daily updates)
- [ ] Live session tracking (sessions/logs/)
- [ ] Populate the tools registry with live tests
- [ ] Wire workflows into actual daily operations

### Needs Neil (decisions, approvals, or input)
- [ ] Any project that will cost money
- [ ] Any publishing or outside-computer action
- [ ] New tool requests
- [ ] Any change that affects Neil's existing workflows

## System Components
- **Vault**: /home/destiny/Obsidian/Destiny/ (git-backed)
- **AI OS Framework**: _ai-os/ namespace (this directory)
- **Toolbox**: TOOLS.md + tools/README.md
- **Knowledge Base**: Knowledge_Base.md
- **Agent Load Order**: canon/agent-load-order.md
- **Core Doctrine**: canon/core-doctrine.md
- **System Overview**: canon/system-overview.md
- **Master System Prompt**: canon/master-system-prompt.md
- **Operations Register**: operators/INDEX.md
- **Tools**: tools/README.md
- **Memory**: memory/README.md
- **Projects**: projects/INDEX.md
- **Workflows**: workflows/README.md
- **Sessions**: sessions/README.md
- **References**: references/operations-register.md, references/vault-structure.md, references/git-protocol.md

## Daily Check
At each session start:
1. Read this file
2. Check each item above
3. Move items from pending to done or needs-neil as appropriate
4. Commit to git
5. Report a 3-bullet summary to Neil

## Wire Map
This register connects every part of the system:
- canon/ → defines principles and agent order
- tools/ → defines what I can do
- memory/ → defines how I remember
- projects/ → defines what is being built
- workflows/ → defines how work gets done
- sessions/ → defines how I track tasks
- operators/ → defines who Neil is and what he wants

## Git
All changes to this system are committed to git. The commit log is the full history.
