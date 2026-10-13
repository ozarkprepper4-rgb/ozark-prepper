# Session Start Workflow

## What This Does
Starts a new session by checking the current state, loading the relevant canon, and routing the task.

## Steps

### 1. Read the master operations register
- Check _ai-os/operators/INDEX.md
- See what is running, pending, and needs Neil

### 2. Check for pending work
- Look at what was blocked or waiting yesterday
- Check the session logs for unfinished work

### 3. Load the relevant canon
- Read _ai-os/canon/core-doctrine.md (why we are here)
- Read _ai-os/canon/agent-load-order.md (who does what)
- Read _ai-os/tools/README.md (what I can do)
- Read _ai-os/workflows/README.md (how work gets done)

### 4. Route the task
- To Pepper: operations, maintenance, 24/7 stuff
- To Victoria: content, marketing, e-commerce, revenue
- To Denise: capital, investments, wealth
- To sub-agents: specialized tasks (security, pantry, solar, comms)
- To myself: research, analysis, knowledge management

### 5. Log the session
- Create a new session record in sessions/active/
- Include the date, title, and goal

### 6. Report
- Tell Neil what we are working on and why
- Keep it plain and simple

## Notes
- Every session has a record. Never start a session without logging it.
- If you are unsure where a task belongs, escalate to Neil.
- Keep it small. One step at a time.

## Test
- Verify the session record was created in sessions/active/
- Verify the session record has the required fields

## When to Use
- At the start of every session
- When an unexpected task arrives
- When Neil asks "what are you working on?"

## Reference
- _ai-os/sessions/README.md — session protocol
- _ai-os/operators/INDEX.md — current state
