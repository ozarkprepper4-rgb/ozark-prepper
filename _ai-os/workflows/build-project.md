# Build Project Workflow

## What This Does
Turns a new project idea into a live, tested, documented project folder inside the Software Library.

## Inputs
- A project name
- A one-line goal
- A folder name for the project

## Steps

### 1. Check the toolbox
- Look in _ai-os/tools/README.md for existing tools that do the job
- Look in the vault for existing code that might be reused
- If something already exists, reuse it (never duplicate)

### 2. Create the project folder
- Created in Software_Library/
- Name: /home/destiny/Obsidian/Destiny/Software_Library/<project-name>/

### 3. Write the files
- **NOTES.md** — what it does, how to run it, what it needs
- **PLAN.md** — the full plan (goals, scope, decisions, next steps)
- **test/** — a test that runs the real output
- **code/** — the finished code
- **.bak/** — backup of old versions (if applicable)

### 4. Back up old files
- Before changing any existing file related to the project, copy it to .bak/

### 5. Test it
- Run the test
- Show the real output to Neil (or log it)

### 6. Update the index
- Add one line to the Software_Library README index

### 7. Wire it
- Add the project to _ai-os/projects/INDEX.md
- Add to the master operations register (Running / Pending / Needs Neil)

## Notes
- Every project needs a test with REAL output. Fake output is not allowed.
- Every project needs a NOTES.md explaining what it does, how to run it, what it needs.
- Older versions are .bak files, never deleted.
- Never delete a project folder without Neil's OK.
- Keep it simple. One thing at a time.

## Test
- Create a real test script that verifies the project works
- Run it and save the output to test/results.txt

## Example Project
```
Software_Library/
  my-project/
    NOTES.md
    PLAN.md
    code/
    test/
      results.txt
    .bak/
```

## When to Use
- Any time you need to build something new
- If you have a new capability or feature in mind

## Reference
- _ai-os/canon/core-doctrine.md — why we build this way
- _ai-os/tools/README.md — what tools are available
