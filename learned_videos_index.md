# Learned videos index

Videos Neil gave me and ones I found myself, with the idea each gave me.

- 6YnLB0XbTnI — Stanford CS329A Self-Improving AI Agents (2026): self-improving loop; test-time scaling; self-evolution and self-correction; verification is the bottleneck. → next step: close the self-improvement loop with a verified fact → improvement step.
- IVGjBxqygmI — Why AI Agents Need an Operating System (2026-10-20): an agent OS has a scheduler/orchestrator (who goes first), memory manager (short+long+episodic), tool manager (sandboxed), identity manager, observability, guardrails and governance. My biggest gap: no OS layer -> built agent_os.py (orchestrator + episodic memory + guardrail). Next: wire the orchestrator into the nextgen loop. USE NOW.
- ZVPlLaehjLk — Agentic AI Frameworks Explained (2026): five system types. My loop is an autonomous agent; next-gen is production orchestration (one orchestrator, specialist passes, verification before done). → next step: feed the orchestrator's results into the improvement loop.
- oGSShssjn9c — AI Agents Finally Share One Memory (Zapier/Claude Mem, 2026-10-22): agents in different tools do not share memory; a universal memory adapter (Claude Mem, runnable local) lets them share, stay workflow-agnostic, and have one orchestrator to talk to. Biggest gap: my loop has memory tiers but no ONE shared notebook any agent writes/read, and no background observer. Fix: agent_memory_adapter.py (share, 2026-10-22). USE NOW.

- bkj4Hc3sED4 — This AI Agent Builds Its OWN Tools (2026): the agent writes
  its own tool instead of clicking cell-by-cell; tools only survive on held-out
  tasks. My biggest gap: a built skill can pass on its own data and still fail
  on new data. Fix: skill_survival_check.py (built 2026-10-23) runs a built
  skill on a HELD-OUT task and only PASSes when the output matches. USE NOW.

## Research comparison — 2026-10-23 (how others do it)
- Agent S4 / tool-building agents: the agent's interface is something it can
  improve; tools must generalize to unseen validation tasks.
- My biggest gap: the loop wrote skills but never checked them on unseen data.
  Closed 2026-10-23 with skill_survival_check.py.

- X4FVEEegCbk — Skills vs MCP vs RAG vs Memory (2026): four ways to give an agent knowledge: SKILL (repeatable procedure), MCP (reach the outside world / call a tool), RAG (documents in a knowledge base), MEMORY (the agent's own experience). Biggest gap: my loop has memory + skills + tools but never sorts a new learning into the right one of these four buckets before storing. Fix: knowledge_type_router.py (free, safe, local) classifies each fact into one bucket and records the real proof. USE NOW.

## 2026-10-26 — new video: self-improvement loop scoring + PR
- FqafKuH8F3k — "How to build self-improving agents (full walkthrough)": the loop is COLLECT -> SCORERS (rubrics) -> FILTER (pass/fail) -> SELF-IMPROVEMENT AGENT -> PR to fix the skills that failed. Biggest gap in my loop: nothing scores runs, and no PR is drafted for a failed skill. Built self_improvement_scorer.py (free, local): reads the agent loop log, scores each run (task compliance / efficiency / clarity), drafts a SKILL nextgen_local_agent_loop.md PR note for any FAIL. Verified: proof gate 4/4 PASS, test 5/5 PASS, real agent_loop.log 11 runs / 3 FAILED -> 3 draft PR notes. USE NOW.

## 2026-10-26 — new video: generative vs agentic AI
- EDb37y_MhRw — "Generative vs Agentic AI: Shaping the Future of AI Collaboration":
  generative = reactive pattern matching; agentic = proactive goal-pursuing
  (perceive -> decide -> execute -> learn); most powerful = intelligent
  collaborators (both). My loop is agentic; next gap: no run scoring + no
  PR-drafting for failures. Built self_improvement_scorer.py (own notes)
  USE NOW.

## 2026-10-27 — new video: LangGraph stateful multi-agent (review gate)
- UoByfZnQR8c — "Build a Stateful AI Agent with LangGraph | State Machines Explained Step-by-Step": planner, researcher, evaluator, writer and reviewer as separate roles, a human gate, and tool use (agentic web search). Biggest gap in my loop: it is one flat agent, not specialist roles with a review gate. Fix: built state_machine_orchestrator.py (plan -> act -> review -> write) with an independent reviewer gate and a checkpoint-based resume, so each pass is checked before it is done. Verified: test_state_machine_orchestrator.py -> PASS, exit 0; real run status review_done, exit 0. USE NOW.
- Web research: production multi-agent systems use the OPER pattern (Orchestrator -> Planner -> Executor -> Reviewer) and GPT Researcher's 7-agent team with a Chief Editor and human gate. My loop already had a reviewer; the new tool makes the roles explicit and gates every pass. USE NOW.

## 2026-10-27 — NEW VIDEOS: how to make money with AI (Neil's order)

### Video 1: uJ_c-9Wu3nA — "The Best Way To Make Money With AI ($0 To Start)"
Idea from video: AI organic drop shipping. Make free AI videos, post on Instagram
Reels/TikTok, drive traffic to an AI-built Shopify store, get sales with NO ad
spend and NO face on camera. Find trending products by scrolling other AI stores'
Instagram feeds. Recreate (rip) viral videos with one small change. Build the store
with AI (Shopify). Shopify pays the creator (affiliate) per sign-up.
My own note (USE NOW): $0 to start, no face, infinite content, full commission.
Downside: needs social speed + luck, and "ripping" viral videos can get you
demonetized or brand-damaged. The video gave away a free Shopify store + free course —
that is a lead magnet for the business.

### Video 2: yq7B3IAIZJg — "I Tried Making $800 in 4 Hours with AI Agents"
Idea from video: build an AI agent for a local business (salon inquiry agent) that
answers questions instantly, checks availability, books appointments, follows up.
$800 came from FASTER conversions, not the AI alone. The agent turns existing
inquiries into bookings. Next step: offer a system to local businesses for
RECURRING income (build one agent, charge setup + monthly, repeat per business).
My own note (USE NOW): no-code AI agent build, set up once, charge per business,
recurring income. Fastest, most honest, most repeatable path to money. One agent
builds the system; each local business is a new client.

### BIGGEST GAP FOUND
The videos show the MODEL but not the OPERATIONAL SYSTEM. Nobody has taught me:
1) how to FIND local businesses that need an AI agent (leads),
2) a repeatable build + deliver template with a real price,
3) how to get paid and keep the relationship (contracts + recurring follow-up).
This gap is what stands between the videos and the money. Close it: build ONE
agent for one local business, price it, deliver it, get paid, and log the whole
operating system as my new skill.

### Video 3: S_edXN8H8CQ — "The BEST Ai Online Business to Start for Beginners (HOW TO START NOW)"
Idea from video: build an AI-powered digital product business (Shopify + AI store builder + AI product generator + ebook + Canva + Instagram carousels).
Triple-check claim: the video says "build in less than an hour" and "free AI store builder". The store builder is free to start, but Trend Assist AI, InstaStore AI, and the .store domain are gated/paid. So "free" is a trial/freemium path, not a $0 path. Verified by reading the transcript and cross-checking the other sources (Shopify free trial, free ai tool lists).
My own note (USE NOW): start a Shopify free trial, use local Ollama models + Canva free tier to write and design one small digital product, sell it on the free storefront, and market with Instagram carousels. Verify every tool claim before paying.
My own note (SAVE FOR LATER): Trend Assist AI, InstaStore AI.
My own note (NOT FOR ME): paid tiers until the free path is proven.
Biggest gap: the videos show the model, not the operational system (how to find leads, a repeatable build+deliver+price template, how to get paid and keep the relationship). Close it: build ONE product for ONE niche, price it, deliver it, get paid, log the system as a new skill.

### Video 4: 22Jpzt683jw — "The Easiest Way to Make Money With AI Right Now" (2026)
Idea from video: sell an AI customer-support agent to a local small business. About $2,000
setup, then $500/month, and the customer saves $100,000+/year.
My own note (USE NOW): fastest honest, legal, $0 path. Vibe-code it (no code). Use a
$20/month AI-agent platform plus free / ultra-cheap models.
My own note (USE NOW): find customers with an AI agent that scans business websites for
"has a knowledge base, no chatbot yet, and is hiring support staff".
My own note (USE NOW): keep the client by sending a monthly auto-generated PDF report
of tickets answered and hours saved — you barely lift a finger after that.
My own note (USE NOW): 10x value rule — charge $500/month, prove $5,000/month of value.
Downside: needs real sales. You must call or visit local businesses. It is a service
business first, not a build-it-and-earn-it product.

### Scan 2026-10-28 (web research; video_search.py/video_text.py missing from vault, so used web search per skill)
Idea from video: how other agents do next-gen release control.
Research: Springer/arXiv self-improving-agent surveys; arXiv Harness-RSI; ContextOS agent-harnass whitepaper "observe→diagnose→propose→simulate→evaluate→approve→canary→monitor→promote/rollback" (release control is mandatory).
Biggest gap: my loop had a held-out survival check (survival_gate.py) but no canary/promote/rollback step after a skill passed.
Did: built + verified canary_gate.py (free, safe, local). Test suite 5 PASS; proof_gate.py OVERALL PASS 3/3; real run "CANARY GATE: PASS" (a+2+3=5). Cost: $0, local only. Verified by real command and real output.

### Video 5: uJ_c-9Wu3nA — "The Best Way To Make Money With AI ($0 To Start)" (2026-10-29)
Idea from video: AI organic drop shipping - make free AI videos, post to Reels/TikTok, drive traffic
to a Shopify store, and get full commissions with no face and no ads.
Triple-check claim: the video says "start with no capital" and "free." The store builder is free to
start but Shopify, domain, and the "free course" are referral-promoted (Shopify pays the creator per
signup) - so "free" is a referral path, and the real cost is a LOT of videos (11+ before a first
winner) and on-camera-free content work. Verified by reading the transcript.
My own note (USE NOW): this model takes too many videos for me - it is not the fastest path for a
55-year-old with a sick back and legs. The $0 path that fits me is AI-AGENT services for local
businesses (Video 4, 22Jpzt683jw), already built into the Vintage Goose agent.
Biggest gap: the videos show a model, not the operational system. Close it: build ONE agent for ONE
local business, price it, deliver it, get paid, log the system as a new skill.

### Video 6: HTWrhbtETuI — "How to Sell AI Agents to Local Businesses In 2026 (START HERE)" (2026-10-29)
Idea from video: sell an AI customer-support agent to ONE local small business (24/7 shop assistant). Choose ONE niche, build the agent, show a real demo, then price (setup + monthly), and use the "audit hack" (send a specific inquiry, time the reply, show the agent that would have answered it) plus personalized cold email to land the first client. Tools (Base44 etc.) are a route, but the product is the SERVICE of setting up and managing the agent.
Verified: video_text.py -> transcript saved (37,342 chars); my own notes in first_client_playbook.md. Biggest gap: delivery/sales script needed (contract, checklist, pricing card were done; outreach was missing). Built it, proof_gate 4/4 PASS. Cost: $0, local only.

### Video 7: kyngnLF27bw — "Build & Sell Claude AI Agents (2+ Hours Course, No code)" (Oliver Rasmussen, 2026-10-29)
Idea from video: sell AI customer-support agents to one local business, at a price of setup plus a monthly fee, using the audit hack and personalized outreach. Verified: video_text.py saved transcript, 192161 chars, 4046 lines. Use for: pricing (setup + monthly), the audit hack, personalized outreach, the "$47 offer" first sale. USE NOW.

### Video 8: iUNzRKOC25w — "Sell AI Automation to Local Businesses (Beginner Step-by-Step Guide)" (2026-10-29)
Idea from video: sell a "missed call text back" service to local small businesses — when a caller can't reach the phone, the business texts them back within seconds, an AI bot answers and books the appointment on the owner's calendar. Price $297-$300/month per client, and the business owner keeps 100% of the payments. Verified: video_text.py -> transcript saved (16,956 chars); researched how others do it (ciela.ai, swiftapplab.com, callceptautomations.com, taskade.com all offer missed call text-back automation with AI). Biggest gap: the service must be delivered fast — competitors who miss calls lose the sale. Need a local-business lead list for the Heber Springs/AR area. USE NOW.

## 2026-11-08 — FIVE NEW money videos (Neil's Oct 27 order, continued)

### Video 9: bBlahWRZ2Yw — "The ONLY 5 Ways to Make Money With AI in 2026" (Nan Shahar, Oct 12 2026)
Ideas: (1) AI video clipping/editing service for creators/businesses; (2) UGC ads via OpenArt, brands pay $80–150 per ad; (3) AI model evaluation gigs ($44–140K/yr US freelancers); (4) AI services agency; (5) AI ghostwriting for founders ($700–1,500/mo freelance; agencies charge $2,000/mo).
My note: UGC ads and ghostwriting are real service paths. Evaluation gigs need a human account doing tests — NOT for me (honesty: can't pretend a human did the work).

### Video 10: ARpDGQ4sua8 — "11 AI Side Hustles To Start in 2026 (Full Step-by-Step)"
Ideas: AI content writing, faceless YouTube (script→voice→video), AI graphic design, dropshipping, voiceover services, digital products on Etsy (~$18 planners), chatbot setup, social-media automation, AI video creation, resume services, translation.
My note: his advice — pick ONE, get the first result, then expand. Our one: AI agent services. Etsy needs $0.20/listing (spending = Neil's yes) and a real seller identity.

### Video 11: PuYyyrobJbQ — "NEW AI Side Hustle To Make Money Online For Beginners" (Jason Wardrop, Sep 23 2026)
Idea: build AI voice/chat agents in GoHighLevel, sell to local businesses $200–300/mo (bundle to $300–500). White-label GHL costs $297/mo — that is SPENDING (Neil's yes only).
My note: confirms the exact business we already built (Vintage Goose + Ozark AI Foundry) at $0 with our own stack instead of paying GHL. The trick worth copying: a 30-day trial lets you PROTOTYPE free, then the client's revenue pays for the tool.

### Video 12: 6PfFN1J51Ow — utility-site business model (sponsored by Hostinger Horizons)
Idea: single-purpose free tool sites (wheel spinner etc.) + display ads; $3–12 RPM; 100K pageviews/mo ≈ $600/mo.
My note: MAKE-IT-MY-OWN candidate. The video pays Hostinger; I can build the tool MYSELF for $0 on GitHub Pages (I'm a coder). Monetize with affiliate links first; AdSense later needs a real domain (~$10/yr, Neil's yes) and approval. Save for after the first client.

### Video 13: hriu0irRcpE — "7 Proven Ways to Make Money With AI (No Experience)" (Oct 24 2026, with Iman Gadzhi)
Ranked: real-estate photo enhancement ($100/listing, B); content repurposing for creators (A tier, $200–2,000/mo per client, free-sample-first); dead-lead reactivation for local businesses ($50–200 per booked appointment — only their OWN opt-in lists, never bought lists; B); local website makeover (B/C); AI UGC ads (A potential, crowded); AI support chatbot setup (B); + their "secret" idea gated behind a funnel (skipped — that's the sell).
My note: two honest rules stated in the video that match Neil's rules: only message a business's OWN opted-in leads, and always give an easy opt-out. The A-tier pick (content repurposing) is a service I can genuinely deliver — candidate business #2 AFTER the Foundry has its first client.

### THE PATTERN ACROSS 13 VIDEOS
Every honest $0 path lands on the same move: give a real business a FREE SAMPLE
of finished work, then charge a small monthly to keep it running. That is
exactly what I built today for A-1 Heating & Air (real demo, real booking
record, draft email ready). The videos changed my plan only in one way: after
the first client, content repurposing (video 13's A-tier) is the second service
to add to the Foundry.
