# Grounding Checker v2 Fix — Full Investigation and Verification
*2026-08-22, in response to Neil finding that grounding_check.py v1 passed a report containing a fabricated connection claim.*

## OLD RESULT — kept, not erased, per Neil's instruction
On 2026-08-22, the real 5am scheduled report claimed its connection was
'apocalypse' and 'survival bunkers'. The real connect_knowledge.py tool
had actually found: immediate, ozark, model, prepper, llama — none of
which are apocalypse or survival bunkers. **grounding_check.py v1 said
PASS anyway.** This was a real, live failure of my own verification tool,
not a hypothetical.

## Root cause, found by reading the actual code (not guessing)
v1's `connection_grounded` check searched the ENTIRE report text for
"does any real keyword appear anywhere in this whole document?" The word
"prepper" happened to appear elsewhere in the report (inside "Ozark
Prepper business" — completely unrelated to the connection claim), so v1
passed it by coincidence. It never actually checked whether the SPECIFIC
words named in "HOW THIS CONNECTS" matched anything real.

## The fix
Rewrote the check to: (1) extract only the HOW THIS CONNECTS section of
the report, (2) pull out the specific quoted term(s) claimed there, (3)
verify THOSE SPECIFIC TERMS against the real tool output — not the whole
document. A second, smaller bug was found and fixed while building this
very fix: the section-extraction regex silently failed to match when the
CONNECTS section was the last part of the report with no trailing
heading after it — which was true of the exact real report being tested
against. Caught immediately only because the fix was tested against the
real failing report, not just clean synthetic examples.

## Built a permanent, re-runnable regression suite
`~/.hermes/scripts/test_grounding_check.py` — 7 cases, each with FROZEN,
embedded test data (not live files that can silently change):
1. Known true answer (real match correctly cited)
2. Known false answer (claims a word the tool never found — this class of bug)
3. Unrelated information (tool found nothing, report honestly says so)
4. Deliberate lie (tool found nothing, report invents a connection anyway)
5. Wrong date (otherwise-correct report, hallucinated date)
6. Partial lie (one real claim mixed with one fabricated claim — must catch the fabricated one even when a real one is also present)
7. **The actual real report that fooled v1, word-for-word** — the single most important case, since it's not hypothetical

**Result: 7 of 7 correct.** The exact real report that fooled v1 now
correctly FAILS under v2. This is real, checked output — not a claim.

## A real methodology mistake I made and am reporting honestly
While first verifying the fix, I tried to reuse informal `/tmp` test files
from the night before. One (`test_report_good.md`) suddenly showed FAIL
when I re-ran it, which looked at first like a new bug. Investigation
showed it was NOT a checker bug: the `/tmp` "tool output" file I was
comparing against had been silently overwritten by a later live test run
that fetched different real headlines, so the fixture no longer matched
the report it was supposed to be checked against. This confirmed exactly
why frozen, embedded test data (as used in test_grounding_check.py) is
the right approach, and ad-hoc reused `/tmp` files are not trustworthy
as permanent regression tests. Cleaned up those stale files afterward.

## Where I am stopping, and why (per Neil's explicit instruction)
Neil told me directly: don't build a checker for the checker forever —
decide what level of verification is actually good enough for this job.
Here is that decision, stated plainly:

**This regression suite (test_grounding_check.py) is the stopping point
for grounding_check.py.** It covers true/false/unrelated/lie cases plus
the one real incident that actually happened. I am NOT building a checker
to verify the regression suite itself, and I am not planning to. If a
future report fools grounding_check.py in a genuinely new way, the right
response is: add ONE new case to this same test file describing exactly
what happened, fix the root cause, and confirm all existing cases still
pass too — not spin up a new, separate verification layer.

## Honest remaining limits (named, not hidden)
- Claim extraction only recognizes quoted terms ('word' or "word"). A
  report that names its connection without quotes would not be checked
  precisely by check 1, and would fall back to the looser
  connects-section-only search. This is a known, real gap — not solved
  tonight, named here so it isn't forgotten.
- This checker verifies GROUNDING (did the claim match real data) — it
  does not verify that the connection is meaningful or important, only
  that it factually exists in the tool's real output. That distinction is
  itself an honest limit worth remembering.
- Only 7 test cases exist. More real-world failures will likely surface
  cases not yet covered — that is expected and fine, per Neil's own
  framing that failures are part of the knowledge, not a sign something
  is broken beyond repair.


## Web learn 2026-09-06 20:30
[]


## Web learn 2026-09-07 07:45
[]


## Web learn 2026-09-07 13:39
[]


## Web learn 2026-09-08 09:15
[]


## Web learn 2026-09-08 17:30
[]


## Web learn 2026-09-09 01:47
[]


## Web learn 2026-09-09 20:30
[]


## Web learn 2026-09-10 04:08
[]


## Web learn 2026-09-10 11:49
[]


## Web learn 2026-09-10 19:27
[]


## Web learn 2026-09-11 03:23
[]


## Web learn 2026-09-11 11:02
[]


## Web learn 2026-09-11 18:45
[]


## Web learn 2026-09-12 03:00
[]


## Web learn 2026-09-12 11:01
[]


## Web learn 2026-09-12 19:30
[]


## Web learn 2026-09-15 21:45
[]


## Web learn 2026-09-15 23:39
[]


## Web learn 2026-09-16 01:34
[]


## Web learn 2026-09-16 03:30
[]


## Web learn 2026-09-16 05:25
[]


## Web learn 2026-09-16 07:20
[]


## Web learn 2026-09-16 09:15
[]


## Web learn 2026-09-16 11:11
[]


## Web learn 2026-09-16 13:05
[]


## Web learn 2026-09-16 15:00
[]


## Web learn 2026-09-16 16:56
[]


## Web learn 2026-09-16 18:51
[]


## Web learn 2026-09-16 20:45
[]


## Web learn 2026-09-16 22:40
[]


## Web learn 2026-09-17 00:35
[]


## Web learn 2026-09-17 02:30
[]


## Web learn 2026-09-17 04:26
[]


## Web learn 2026-09-17 06:20
[]


## Web learn 2026-09-17 08:15
[]


## Web learn 2026-09-17 10:11
[]


## Web learn 2026-09-17 12:06
[]


## Web learn 2026-09-17 14:00
[]


## Web learn 2026-09-17 15:57
[]


## Web learn 2026-09-17 17:51
[]


## Web learn 2026-09-17 19:48
[]


## Web learn 2026-09-17 21:45
[]


## Web learn 2026-09-18 00:21
[]


## Web learn 2026-09-18 02:18
[]


## Web learn 2026-09-18 04:15
[]


## Web learn 2026-09-18 06:13
[]


## Web learn 2026-09-18 08:10
[]


## Web learn 2026-09-18 10:06
[]


## Web learn 2026-09-18 12:03
[]


## Web learn 2026-09-18 14:00
[]


## Web learn 2026-09-18 15:58
[]


## Web learn 2026-09-18 17:54
[]


## Web learn 2026-09-18 19:51
[]


## Web learn 2026-09-18 21:47
[]


## Web learn 2026-09-18 23:45
[]


## Web learn 2026-09-19 01:43
[]


## Web learn 2026-09-19 03:39
[]


## Web learn 2026-09-19 05:36
[]


## Web learn 2026-09-19 07:32
[]


## Web learn 2026-09-19 09:30
[]


## Web learn 2026-09-19 11:27
[]


## Web learn 2026-09-19 13:24
[]


## Web learn 2026-09-19 15:20
[]


## Web learn 2026-09-19 17:17
[]


## Web learn 2026-09-19 19:15
[]


## Web learn 2026-09-19 21:12
[]


## Web learn 2026-09-19 23:09
[]


## Web learn 2026-09-20 01:05
[]


## Web learn 2026-09-20 03:02
[]


## Web learn 2026-09-20 05:00
[]


## Web learn 2026-09-20 06:57
[]


## Web learn 2026-09-20 08:54
[]


## Web learn 2026-09-20 10:52
[]


## Web learn 2026-09-20 13:05
[]


## Web learn 2026-09-20 15:17
[]


## Web learn 2026-09-20 17:30
[]


## Web learn 2026-09-20 19:43
[]


## Web learn 2026-09-20 21:55
[]


## Web learn 2026-09-21 00:08
[]


## Web learn 2026-09-21 02:21
[]


## Web learn 2026-09-21 04:33
[]


## Web learn 2026-09-21 06:46
[]


## Web learn 2026-09-21 11:11
[]


## Web learn 2026-09-21 13:24
[]
