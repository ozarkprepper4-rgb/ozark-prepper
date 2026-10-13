# Git Protocol for the AI OS

## Why Git

Git is the version control system for the AI OS. Every change to the vault is tracked. The commit log is the full history of the system.

## Commit Protocol

1. **Before making changes**: Check git status
2. **After making changes**: Stage the specific files and commit with a clear message
3. **Commit message format**: `"Action on target: description"` (e.g., `"Add AI OS: core doctrine"`)
4. **After commit**: Verify with `git log --oneline -5`

## Branch Protocol

- Always commit to the main branch
- Never rewrite history
- Never delete commits
- If a mistake is made, add a corrective commit

## Verifying Changes

After committing, run:
```bash
git log --oneline -5          # show recent commits
git status                    # confirm working tree is clean
```

## What to Commit

- New files in _ai-os/ (canon, tools, memory, projects, workflows, sessions, operators)
- Changes to existing files
- The master operations register

## What Not to Commit

- Do not commit secrets, keys, or passwords
- Do not commit the vault itself (it is for human reading, not a tool)
- Do not commit outside files

## Recovery

If something breaks:
1. Check `git log` for recent commits
2. Checkout the last known good state: `git checkout <commit-hash>`
3. Revert the specific file: `git checkout <commit-hash> -- <file>`
