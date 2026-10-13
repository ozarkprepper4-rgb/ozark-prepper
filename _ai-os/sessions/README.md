# Sessions Directory

## What This Is
This folder tracks every session I run. Each session is:
- **active/** — sessions currently running
- **closed/** — finished sessions with records
- **logs/** — detailed logs of what happened
- **reviews/** — after-action reviews of sessions

## Session Protocol
1. **Start** — record a new session in sessions/active/ with a timestamp
2. **Work** — do the task, with notes in sessions/logs/
3. **Close** — when done, move to closed/, write a record, update the operations register
4. **Review** — weekly, review sessions for patterns, improvements

## Session Record Contents
Each session record should have:
- **date** — when it ran
- **title** — brief description of what was done
- **goal** — what Neil asked for
- **steps** — what I did
- **results** — what happened (with real output)
- **next steps** — what is still pending
- **verdict** — done, in progress, blocked, needs Neil

## Rules
- Every session has a record. Never start a session without logging it.
- Never delete a session record. If it's wrong, add a correction.
- Sessions are plain text. Neil can read them.
