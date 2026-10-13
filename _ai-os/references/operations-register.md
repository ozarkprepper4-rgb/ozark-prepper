# Master Operations Register

## What This Is

The master operations register is the central dashboard for the AI Operating System. It tells Neil (and any agent) at a glance:
- What is running
- What is pending
- What has been verified
- What needs Neil

It is the single source of truth for system state.

## Structure

The register has 4 sections:

### 1. Running (active agent tasks)
Items currently being worked on. Each has:
- A checkmark [x] when done
- A note about what is being done

### 2. Pending (waiting on Neil or verification)
Items waiting on something:
- Waiting on Neil (decisions, approvals, input)
- Waiting on verification (test results, code review)
- Waiting on external resources

### 3. Needs Neil (decisions, approvals, or input)
Items that require Neil's action:
- Any project that will cost money
- Any publishing or outside-computer action
- New tool requests
- Any change that affects Neil's existing workflows

### 4. System Components
A list of all the components in the system and where they live:
- Vault location
- AI OS framework path
- Tool registry location
- Knowledge base location
- Agent load order location
- Core doctrine location
- Tools location
- Memory location
- Projects location
- Workflows location
- Sessions location
- Operators location

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

All changes to the AI OS are committed to git. The commit log is the full history.
