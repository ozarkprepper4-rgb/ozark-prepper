# Tools Directory

## What This Is
This folder contains every tool I, Pepper, and the agents can use. A tool is a capability — a way to read, write, search, compute, or act on the system or the outside world.

## Tool Registry
Tools are documented in this folder. Each tool has:
- **name** — the unique name
- **purpose** — what it does
- **inputs** — what it needs
- **outputs** — what it returns
- **when to use** — when you'd pick this tool

## Current Tools

### Core Skills (Python scripts in /home/destiny/Obsidian/Destiny/)
- **talk.py** — conversational responses, reads the whole Obsidian vault
- **forge_skill.py** — generates, tests, and installs new Python skills on request
- **self_run.py** — self-check and cleanup routine
- **clean_knowledge_base.py** — cleans up the knowledge base file
- **find_ozark.py** — searches for Ozark Prepper related content
- **vault_actions.py** — handles website building, note reading/writing, vault searches
- **environment_tool.py** — shared execution capability for Destiny, Pepper, CEOs, and all agents (selects the appropriate environment: Mint, Ubuntu, Arch, Kali, Omarchy)

### Web & Learning
- **web_search.py** — searches Wikipedia for real information
- **web_extract.py** — extracts content from web pages
- **browser_exec / browser_vault** — drives a real browser for video, login, and dynamic pages
- **video_watch.py** — pulls YouTube transcripts and summarizes them
- **video_search.py** — finds a YouTube video by title

### External Integrations
- **github CLI (gh)** — for GitHub operations
- **cronjob_manage** — schedules recurring jobs
- **terminal** — shell command execution

### Verification
- **verify.py** — checks if files exist, checks syntax, runs real commands and reports real output
- **agent_standard_check.py** — runs 15 tests on the agent standard
- **vera_check.py** — independent verification

## Tool Selection Rules
1. Check this folder before building anything new.
2. If a tool already exists to do the job, use it. Do not duplicate.
3. If you need a tool that does not exist, ask Neil before building it.
4. Never put passwords, keys, or vault secrets in any tool.
5. Never publish or run anything outside this computer without Neil's OK.

## Adding a New Tool
1. Define what it does (description)
2. Create the script or verify it exists
3. Document it in this file
4. Test it
5. Add to the toolbox and verify
