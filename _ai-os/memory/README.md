# Memory Directory

## What This Is
This folder contains how I remember and retrieve information. Memory is my long-term knowledge store. It is separate from the working knowledge base (Knowledge_Base.md).

## Memory Principles
1. **Facts, not instructions** — Memory stores facts about people, projects, decisions, and preferences, not task progress or tool output.
2. **Standing rules, not task logs** — Procedures and workflows belong in skills, not memory.
3. **One sentence per fact** — Keep facts short and standalone.
4. **Supersede old facts** — When something changes, add the new fact with `supersedes=` pointing to the old one.
5. **Link by entity** — Use one-word entities so facts link together (e.g., "Neil", "Pepper", "Victoria").
6. **Never secrets** — Never store passwords, keys, or the vault contents in memory.

## How Memory Works Here
The Obsidian vault is the external memory. The git repo backing the vault tracks every change. Memory is organized as:

- **facts/** — short, standalone fact entries
- **contradictions/** — things we learned and corrected
- **references/** — pointers to sources and documentation

## Memory Types
1. **People** — who they are, their preferences, their role in the system
2. **Projects** — what we are building, decisions made, status
3. **Decisions** — what was decided, why, and when
4. **Preferences** — how Neil likes things done
5. **Corrections** — things that changed and what replaced them

## Memory Protocol
When I encounter a fact:
1. Check if it already exists (search for similar terms)
2. If yes and it changed: add a new fact with `supersedes=<old_id>`
3. If no: add the fact as a new standalone sentence
4. Rate recalled facts when helpful or wrong

## Tools for Memory
- **fact_store** — the local memory store for quick access
- **session_search** — search past conversations
- **Obsidian vault** — the deep persistent knowledge
- **Knowledge_Base.md** — confirmed facts and self inventory

## Writing to Memory
1. Do not repeat what Neil already knows.
2. Do not store instructions (those are skills).
3. Do not store task progress (that goes in the session log).
4. Keep it short and declarative.
