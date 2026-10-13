# Workflows Directory

## What This Is
This folder contains all the repeatable processes I use to get work done. A workflow is a sequence of steps that turns an input into an output.

## Workflow Principles
1. **Simple and specific** — Each workflow does one thing well.
2. **Reusable** — The same workflow works for different inputs.
3. **Verifiable** — Every workflow has a test and real output.
4. **Documented** — Each workflow has NOTES.md explaining what it does, how to run it, and what it needs.

## Current Workflows

### Build Project Workflow
1. Check the toolbox for existing tools that do the job
2. Reuse what exists; do not duplicate
3. Create a project folder with code, NOTES.md, and tests
4. Back up old files as .bak before changing them
5. Run the test and show real output
6. Add one line to the README Index
7. Wire it into the master operations register

### Video Analysis Workflow
1. Load the video in the browser
2. Extract the title and description
3. Get the transcript/description metadata
4. Summarize what the video shows
5. Figure out how it applies to the current task
6. Report findings in plain language

### Knowledge Update Workflow
1. Read the relevant files
2. Find what needs updating
3. Make the changes
4. Git commit the changes
5. Verify with real output
6. Report back to Neil

### Session Start Workflow
1. Check the master operations register
2. Check for pending work from yesterday
3. Load the relevant canon (core doctrine, tool registry, workflow map)
4. Route the task to the right agent
5. Log the session in sessions/active/
6. Report back in plain language

### Session Closeout Workflow
1. Save active session to closed
2. Write a session record with decisions and next steps
3. Update the operations register
4. Commit to git
5. Report summary to Neil

## Workflow Map
Each workflow has its own file with full documentation. The workflow map is a quick reference:

- **build-project.md** — create a new project
- **video-analysis.md** — watch and analyze a video
- **knowledge-update.md** — update the vault
- **session-start.md** — start a session
- **session-closeout.md** — end a session

## Adding a New Workflow
1. Define the purpose and inputs
2. Write the step-by-step procedure
3. Create a test
4. Document in NOTES.md
5. Add to this workflow map
6. Wire it into the operations register
