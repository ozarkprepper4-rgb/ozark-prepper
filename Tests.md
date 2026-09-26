# Tests
## Secret_Test.md
# Secret Test

Our secret test number is 5.

## Memory_Retrieval_Test_2026-08-21.md
# Memory Retrieval Test — Did I Actually Find, Understand, and Use Old Knowledge?
*2026-08-21, in response to Neil's direct instruction: "test whether you can
actually find it and use it later without me telling you where it is."*

## The test I designed
Rather than pick a fact I already had loaded in this conversation, I
deliberately used `search_files` to hunt for something I had learned
EARLIER TONIGHT in a different part of this same long session — treating
it the way a future session (with no memory of tonight's conversation)
would have to: find it cold, from a keyword, not from context I already
had in my head.

## Step 1 — FIND (without being told where)
Searched Obsidian for the phrase "system load" with no file path given.
Found 2 real matches, in files I had written earlier tonight:
`Knowledge_Base.md` and `Self_Directed_Session_2026-08-21.md`.

## Step 2 — UNDERSTAND (not just match words)
Read the surrounding paragraph, not just the matching line. The real
lesson buried there: when I ran 8 AI tests back-to-back with no rest
tonight, system load climbed from under 1.0 to nearly 3.0, response times
nearly tripled, and every single one of those 8 tests failed. The lesson
is not "system load exists" (a bare fact) — it's "hammering the AI with
no rest between calls appears to degrade its reliability, and I should
check load and let it settle before running more tests."

## Step 3 — CONNECT to something I'm working on right now
I was about to run more tests of the real daily-learning cron job (the
same job that failed 8/8 times earlier). Instead of diving straight in the
same way as before, I applied the lesson: checked `uptime` before testing,
and when load wasn't settled, waited and re-checked repeatedly (not a
blind fixed-length sleep) until it genuinely dropped, before running each
test.

## Step 4 — PROVE it actually changed the outcome, not just talk about it
Ran the exact same real cron job 3 times tonight, with proper rest between
each run this time:
- Test 1: checked load was low (0.50) before running. Result: PASS
  (graded automatically by grounding_check.py, not eyeballed).
- Test 2: waited until load dropped from 2.22 back under 1.0 before
  running. Result: PASS.
- Test 3: waited again until load dropped from 2.46 back under 1.0.
  Result: PASS.

**3 out of 3 real successes tonight, using the exact same job that failed
8 out of 8 times earlier tonight under rapid-fire testing with no rest.**
This is a real behavior change driven by applying old knowledge, not a
coincidence I'm assuming — though 3 samples is still a small number, and
I am not calling this "proven reliable" from 3 tests alone.

## Honest limits of this test
- Small sample size (3 successes) is suggestive, not proof of a hard
  causal rule. I have not run enough trials to say "waiting for load
  to settle guarantees success" — only that doing so correlated with
  100% success tonight, versus 0% without it.
- I did not control for other variables (time of day, what else was
  running, etc.) — a fair critique would be that something else changed
  between the two testing rounds, not just the rest periods.
- This test used a fact from EARLIER IN THE SAME CONVERSATION, not a fact
  from a truly separate past session with a fresh context. It is still a
  meaningful test (I used `search_files` cold rather than recalling it
  from active context), but a fully rigorous test would repeat this in a
  brand new session tomorrow with zero conversational memory of tonight,
  relying purely on the Obsidian file being findable and readable.

## What this proves and what it doesn't
Proves: I can search my own past notes, understand a real lesson (not
just match keywords), apply it to a live decision, and get a real,
measurable, different result. That is a genuine, tested instance of the
retrieve-and-use loop working, not a description of the loop.

Does NOT prove: that this always works, that 3 tests is a reliable sample,
or that memory retrieval works this well for a different kind of fact.
This is one successful test case, honestly documented as exactly that.

## Follow-up needed (not done tonight, named honestly)
Repeat this exact test in a genuinely fresh session tomorrow, with no
conversational memory of tonight, to confirm the knowledge survives a real
session boundary and not just this one long conversation.

## Command_Test.md
Destiny command test

## Command_Test2.md
command output works

## Chat_Window_Test.md
the chat window can write notes now.

## Shortcut_Test.md
the shortcut works

