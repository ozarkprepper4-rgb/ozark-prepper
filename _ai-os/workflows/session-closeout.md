# Session Closeout Workflow

## What This Does
Closes a session by moving the active record to closed, writing a session record, updating the operations register, and committing.

## Steps

### 1. Save active session to closed
- Move the active session record from sessions/active/ to sessions/closed/
- Use a timestamped filename

### 2. Write a session record
- Record the date, title, goal, steps, results, next steps, and verdict
- Log the real output (not claims)
- Include what was verified

### 3. Update the operations register
- Move items from Pending to Running or Done as appropriate
- Add new items if new work started
- Note anything that needs Neil

### 4. Commit to git
- Stage the session record and any changed files
- Commit with a clear message: "Session closeout: date - description"
- Verify the commit with git log

### 5. Report
- Tell Neil a 3-bullet summary of what was done
- Keep it plain and warm

## Rules
- Never delete a session record. If it is wrong, add a correction.
- Never promise verification without doing it.
- Keep the session record plain text. Neil can read it.

## Test
- Verify the session was moved from active/ to closed/
- Verify the session record has all required fields
- Verify the operations register was updated
- Verify the commit was made

## When to Use
- When a task is done
- At the end of a session
- When Neil asks for a status update

## Reference
- _ai-os/sessions/README.md — session protocol
- _ai-os/operators/INDEX.md — operations register
