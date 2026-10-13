# Knowledge Update Workflow

## What This Does
Reads, updates, and commits changes to the Obsidian vault. This is the core knowledge maintenance workflow.

## Inputs
- What to update (file path or topic)
- What to change (new content, corrections, additions)

## Steps

### 1. Read the relevant files
- Identify the files that need updating
- Read the current content of each file
- Understand what is already there

### 2. Find what needs updating
- Check for contradictions
- Check for outdated information
- Check for missing information

### 3. Make the changes
- Edit the file(s) with the new or corrected content
- Keep changes small and focused
- Match the existing style and conventions

### 4. Git commit
- Stage the specific files
- Commit with a clear message: "Action on target: description"
- Verify the commit with git log

### 5. Verify
- Confirm the changes are correct
- Show real output to Neil (or log it)
- Do not claim verification until you have done it

### 6. Report
- Tell Neil what changed and why
- Keep it short and plain

## Rules
- Never invent facts. Only add what is verified.
- Never store secrets in the vault. No passwords, keys, or credentials.
- Every change must be committed to git.
- Never delete history. If a change is wrong, add a correction.

## Test
- Run a git log check to confirm the commit exists
- Run a file existence check to confirm the file was written
- Save the verification output for the session record

## When to Use
- After any new information is learned
- After corrections are needed
- After completing a task that updates the system

## Reference
- _ai-os/canon/core-doctrine.md — how we manage knowledge
- _ai-os/references/git-protocol.md — how to commit
