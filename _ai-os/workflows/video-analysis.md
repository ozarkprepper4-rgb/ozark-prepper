# Video Analysis Workflow

## What This Does
Loads a YouTube video, extracts its content, and figures out how it applies to the current task.

## Inputs
- A YouTube URL (or video ID)

## Steps

### 1. Load the video
- Open the URL in the browser
- Wait for the page to load fully

### 2. Extract metadata
- Get the title (document.title)
- Get the description (meta tags, og:description, twitter:description)
- If available, get the transcript

### 3. Summarize
- What does the video show?
- What are the main points?
- What is the key takeaway?

### 4. Apply
- How does this relate to the current task?
- What does it mean for my operations?

### 5. Report
- Summarize findings in plain language
- Note any actions to take

## Notes
- Never publish or run anything outside this computer without Neil's OK.
- The video may contain marketing links or external content. Focus on the educational content.
- Videos change. Always read the current description, not a cached one.

## Test
- Run the workflow on a sample video
- Save the output to test/video-analysis-results.txt

## Example Output
```
Title: The AI Operating System (2026)
Summary: The video shows how to build an AI OS for a company...
Application to current task: This is exactly what we are building in _ai-os/.
Action: None needed. Framework is already built and committed.
```

## When to Use
- After watching a video
- When Neil shares a link
- When researching new capabilities

## Reference
- _ai-os/canon/core-doctrine.md — what we are building
