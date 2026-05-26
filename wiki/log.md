# Log

## [2026-05-27] ingest | Software After Software

Ingested Thorsten Ball's 12-point manifesto from X (2026-05-26) on how AI agents transform software development economics, organization, and practice. Manifesto announces the positioning of Amp Labs (Sourcegraph) as a frontier R&D unit.

- Created source page: `[[software-after-software]]`
- Created entity pages: `[[thorsten-ball]]`, `[[amp]]`, `[[amp-labs]]`, `[[sourcegraph]]`
- Created concept pages: `[[process-drag]]`, `[[value-migration-from-code]]`, `[[reorganize-around-models]]`, `[[frontier-camp]]`
- Updated concepts: `[[code-is-free]]` (added Ball's industry-level framing), `[[engineering-role-shift]]`, `[[agent-native-infrastructure]]`, `[[just-in-time-software]]`, `[[acceptance-bottleneck]]`, `[[ai-era-standard-balance]]`, `[[local-optimization-trap]]`, `[[delegation-mindset]]`
- Updated `[[index]]`, `[[log]]`, and `hotcache.md`

Key takeaways: (1) **Code abundance** — AI makes implementation trivial; bottleneck moves from writing code to making decisions; "review will shift from code to decisions". (2) **Process drag** — Planning, prioritization, sequential review become drag when code is abundant; "AI is not only an accelerator for X — it changes whether X should exist at all". (3) **Value migration** — Software that does X loses value when agents can do X; moats shift to data, permissions, distribution, trust, compliance, regulatory position, and physical assets; software companies will be the last to admit it. (4) **Reorganize around models** — "A small team with strong judgment and many agents will outrun a large team trying to fit AI into processes from before the transformation"; ability to keep up beats headcount. (5) **Frontier camp** — Small autonomous team near real systems whose output is software + people + practice; Amp Labs as Ball's worked example. (6) The unit of work becomes the **delegated task**, not the code to be written.

## [2026-05-25] ingest-refresh | Using Claude Code: The Unreasonable Effectiveness of HTML
- Created source page: `[[software-writing-software-gone-right]]`
- Created concept pages: `[[personalized-development-environment]]`, `[[just-in-time-software]]`
- Created entity pages: `[[tj-devries]]`, `[[luaai-nvim]]`
- Updated concepts/entities: `[[malleable-tools]]`, `[[coding-harness]]`, `[[just-in-time-context]]`, `[[neovim]]`
- Updated `[[index]]`, `[[log]]`, `hotcache.md`

Key takeaways: (1) AI does not need to own the whole coding task; it can materialize tiny personal functions exactly when needed; (2) caching generated code turns one-off prompts into reusable personal software; (3) prompt/error history attached to a generated function lets the user improve it without redescribing everything; (4) this is a micro-scale example of malleable tools and a tiny coding harness embedded in an editor.

## [2026-05-09] ingest | Using Claude Code: The Unreasonable Effectiveness of HTML

Ingested Thariq S.'s post on why HTML is a superior communication medium to Markdown for AI agents.

- Created source page: `[[thariq-html-effectiveness]]`
- Created concept pages: `[[html-artifacts]]`, `[[custom-editing-interfaces]]`
- Updated entities: `[[claude-code]]`
- Updated concepts: `[[cognitive-debt]]`, `[[specs-to-code]]`
- Updated `[[index]]`, `[[log]]`, `hotcache.md`

Key takeaways: (1) **HTML vs Markdown**: Markdown fails at scale (>100 lines), while HTML offers rich density (SVG, CSS, JS) and visual clarity; (2) **Custom Editing Interfaces**: Building "throwaway editors" with export buttons helps humans stay in the loop for complex data tasks; (3) **Information Density**: HTML is a high-signal medium that reduces cognitive debt by making complex plans and code reviews navigable.

## [2026-05-09] ingest | Matt Pocock — Software Fundamentals Matter More Than Ever

Ingested Matt Pocock's talk arguing that software fundamentals (design, architecture, testing) are more critical in the AI age to prevent "Software Entropy."

- Created source page: `[[matt-pocock-software-fundamentals]]`
- Created concept pages: `[[grill-me]]`, `[[ubiquitous-language]]`, `[[deep-modules]]`, `[[software-entropy]]`, `[[specs-to-code]]`
- Created/Updated entity pages: `[[matt-pocock]]`, `[[john-ousterhout]]`
- Updated concepts: `[[vibe-coding]]`, `[[agentic-engineering]]` (added Tactical vs Strategic framing)
- Updated `[[index]]`, `[[log]]`, `hotcache.md`

Key takeaways: (1) **Specs-to-Code Trap**: Ignoring the code leads to garbage; (2) **Deep Modules**: Simplify interfaces to delegate implementation to AI safely; (3) **Grill Me**: Force AI into a shared design concept before execution; (4) **Ubiquitous Language**: Shared vocabulary (DDD) aligns AI with the domain and reduces verbosity.

## [2026-05-09] ingest | Memory and dreaming for self-learning agents

Ingested an Anthropic talk by Mahes (Platform PM) introducing Memory (public beta) and Dreaming (research preview, launched today) in the Claude Managed Agents API.

- Created source page: `[[memory-and-dreaming-self-learning-agents]]`
- Created concept pages: `[[dreaming]]`, `[[agent-memory-filesystem]]`, `[[self-learning-agents]]`
- Created entity pages: `[[claude-managed-agents]]`, `[[harvey-ai]]`
- Updated `[[anthropic]]` to list Managed Agents API as a product surface
- Updated `[[index]]`, `[[log]]`, `hotcache.md`

Key takeaways: (1) Anthropic models memory as a **file system Claude manages with bash/grep**, mirroring the skills design — leaning on Opus 4.7's SOTA file-system memory; (2) **Dreaming** runs out-of-band across multiple agents' transcripts to produce curated diffs to memory stores, separating "memory quality" from "task completion" as discrete objectives; (3) Multi-agent enterprise needs drove **permission scopes**, **optimistic concurrency** via content hashes, and **version history with attribution**; (4) Early customers report ~90% mistake reduction (Rocketin) and 6× task completion (Harvey on a legal benchmark).

## [2026-05-08] ingest | Helldivers 2 Just Fell to “Mostly Negative” Reviews

Ingested a video by SwanyPlaysGames reporting on the 2026 review crisis of Helldivers 2. The source highlights the "Lightning in a Bottle" tragedy where a successful game stalls due to a focus on monetization over core systems and late-game progression.

- Created source page: `[[helldivers-2-mostly-negative-reviews]]`
- Created/Updated entity pages: `[[helldivers-2]]`, `[[arrowhead-game-studios]]`, `[[sony-interactive-entertainment]]`, `[[swanyplaysgames]]`
- Created Thai-primary concept pages: `[[monkey-paw-balancing]]`, `[[live-service-stagnation]]`
- Updated `[[index]]`, `[[log]]`, and `hotcache.md`

Key takeaways: (1) **Monkey Paw Balancing** creates distrust by countering every player buff with a hidden or explicit nerf; (2) **Live Service Stagnation** occurs when revenue loops (Warbonds) outpace core maintenance and endgame features (Ship Modules); (3) Community fragmentation and "Mosty Negative" reviews signal a breakdown in the developer-player relationship despite 1.5+ years of content updates.

## [2026-05-02] ingest | JRT Investment — I Don't Give a Fuck Skill

Ingested a Thai Facebook post by JRT Investment framing "I don't give a fuck" as a selective-care skill, not apathy. The useful idea is **care allocation**: attention is a scarce resource, so the work is deciding which people, work, and feedback deserve it.

- Created raw capture: `raw/JRT Investment - I dont give a fuck skill.md`
- Created source page: `[[jrt-investment-idgaf-skill]]`
- Created entity page: `[[jrt-investment]]`
- Created concept page: `[[care-allocation]]`
- Updated `[[index]]`, `[[log]]`, and `hotcache.md`

Key takeaways: (1) mental load often comes from letting external judgment set the agenda; (2) reducing low-value care lowers the perceived cost of failure; (3) this connects to existing wiki themes around scarce human attention in [[code-is-free]], [[cheaper-to-correct]], and [[delegation-mindset]].

## [2026-04-30] ingest | Andrej Karpathy: From Vibe Coding to Agentic Engineering

Ingested Sequoia AI Ascent 2026 talk by Andrej Karpathy. Explored the transition from "vibe coding" (raising the floor) to "agentic engineering" (raising the ceiling/discipline). Introduced Software 3.0, Jagged Intelligence (Ghosts vs. Animals), and the need for Agent-Native Infrastructure.

- Created source page: `[[andrej-karpathy-vibe-coding-to-agentic-engineering]]`
- Created/Updated entity page: `[[andrej-karpathy]]` (Updated with 2026 perspectives)
- Created Thai-primary concept pages: `[[vibe-coding]]`, `[[agentic-engineering]]`, `[[software-3-0]]`, `[[jagged-intelligence]]`, `[[verifiability]]`, `[[agent-native-infrastructure]]`
- Updated `[[index]]` and this log

Key takeaways: (1) **Software 3.0** defines programming as using the context window as a lever over an LLM interpreter; (2) **Agentic Engineering** is a discipline for maintaining professional quality while using powerful but "jagged" agents; (3) **Jagged Intelligence** describes how AI peaks in verifiable domains (math/code) but fails in common sense (ghosts vs. animals); (4) **Agent-Native Infrastructure** calls for docs and APIs designed for agent legibility, not just human readability.

## [2026-04-25] ingest | Matt Pocock — High-Concurrency Agent Workflow

Ingested a tweet from Matt Pocock (@mattpocockuk) describing a "New Flow" for software development using swappable agent dependencies. The workflow features Slack-driven triage, a planning agent that generates a Directed Acyclic Graph (DAG) of PRs/branches, and implementer agents working in parallel within Sandcastle sandboxes.

- Created source page: `[[matt-pocock-agent-workflow]]`
- Created concept page: `[[pr-dependency-dag]]`
- Created entity pages: `[[matt-pocock]]`, `[[sandcastle]]`, `[[vercel]]`
- Updated `[[subagent-patterns]]` — added "Parallel DAG" pattern (v1.5) as an evolution of Parallel Fan-out for complex dependencies.
- Updated `[[index]]` and this log

## [2026-04-24] ingest | Piyalitt Ittichaiwong — GPT-5.5 Launch Commentary

Ingested a Thai Facebook post by Piyalitt Ittichaiwong (early-access tester, Thai PhD researcher + 20yr programmer) framing OpenAI's GPT-5.5 launch (2026-04-23) in two layers: subjective reaction ("first model I can't compete with"; near-Mythos Preview capability but accessible to all; SWE-Bench Pro memorization sign; pricing inversion — GPT-5.5 > Opus 4.7) and a structured Thai summary of OpenAI's launch materials.

- Created raw: `raw/Piyalitt Ittichaiwong - GPT-5.5 Launch.md`
- Created source page: `[[piyalitt-gpt-5-5-launch]]`
- Created entity pages: `[[piyalitt-ittichaiwong]]`, `[[openai]]`, `[[gpt-5-5]]`
- Updated `[[claude-opus-4-7]]` — added "การแข่งขันกับ GPT-5.5" section with pricing inversion, CyberGym gap (73.1 vs 81.8), senior-engineer testimonial, Piyalitt's "ไม่ต้องพูดถึง Opus 4.7 เลยครับ" quote
- Updated `[[openai-codex]]` — linked to `[[openai]]` parent entity; added internal-OpenAI usage section (85%+ weekly, finance K-1 case, 20% traffic-splitter speedup, Edu/Go plans, 400K ctx)
- Updated `[[index]]` and this log

## [2026-04-24] ingest | Aaron Levie — Agent automation jobs

Ingested an X post by Aaron Levie (CEO of Box) arguing companies will need dedicated headcount for the chatbot→agent-automation transition, with an 8-item job spec spanning workflow design, deploy, context, integration, evals, HITL, upgrades, and change management.

- Created raw: `raw/Aaron Levie - Agent Automation Jobs.md`
- Created source page: `[[aaron-levie-agent-automation-jobs]]`
- Created entity page: `[[aaron-levie]]`
- Created Thai-primary concept page: `[[agent-enablement-role]]` — cross-linked to ai-orchestrator, domain-to-ai-translator, harness-engineering, long-running-agents, engineering-role-shift
- Updated `[[engineering-role-shift]]` — added agent-enablement-role to "บทบาทใหม่" list
- Updated `[[index]]` and this log

## [2026-04-23] ingest | Stop Slop

Ingested the "Stop Slop" GitHub repository by Hardik Pandya. This is a skill for LLMs to avoid "AI tells" and write more human-like prose.

- Created source page: `[[stop-slop-source]]`
- Created concept page: `[[stop-slop-concept]]`
- Created entity page: `[[hardik-pandya]]`
- Updated `[[index]]`



## [2026-04-23] convention | Thai-primary rewrite of all concept and entity pages

In accordance with the new bilingual content policy, rewrote all existing concept (56) and entity (40) pages to be Thai-primary. Source summary pages remain in English. This completes the migration of the core wiki content to Thai.

- Updated `CLAUDE.md` to reflect the new Thai-primary writing style.
- Rewrote all 56 files in `wiki/concepts/` to Thai.
- Rewrote all 40 files in `wiki/entities/` to Thai.

## [2026-04-23] ingest | 5 Agent Design Patterns for Long-running AI Agents (Google Cloud Tech, Addy Osmani + Shubham Saboo)

Source: <https://x.com/GoogleCloudTech/status/2046989964077146490> — 2026-04-22 X post + Google Cloud blog by Addy Osmani (@addyosmani) and Shubham Saboo (@Saboo_Shubham_). Announces Cloud Next '26 feature: Agent Runtime now supports 7-day long-running agent state. Created/updated:

- `sources/google-cloud-long-running-agent-patterns.md` — new source; covers all 5 patterns + governance triad + composition heuristic; flags as vendor blog (patterns general, implementations Google-specific)
- `entities/google-cloud.md` — new entity
- `entities/gemini-enterprise-agent-platform.md` — new entity; catalogs Agent Runtime / ADK / Mission Control / Memory Bank / Memory Profiles / Agent Identity / Agent Registry / Agent Gateway / Agent Observability / BYOC / Batch + Event-Driven Agents
- `concepts/long-running-agents.md` — new Thai-primary concept; explains request-handler vs server-process framing, walks through each of the 5 patterns, calls out memory drift as a net-new failure mode, cross-links to subagent-patterns / agent-runtime-untrusted / auto-mode / agent-swarm / advisor-strategy
- `concepts/subagent-patterns.md` — added "Fleet Orchestration" section positioning Google's Pattern 5 as the cross-process, cross-container sibling of fan-out/pipeline
- `concepts/agent-runtime-untrusted.md` — added Agent Gateway as the product-form of APTS-SC-020 (out-of-model allowlist)
- `wiki/index.md` — indexed new source, 2 entities, 1 concept

Net-new vocabulary: **memory drift** (agent behavior warps via accumulated atypical experience), **pause-in-place HITL** (vs serialize → webhook → rehydrate), **governance triad** (Identity / Registry / Gateway as IAM + service discovery + API gateway for agents), ambient agents as first-class category, 7-day state as platform capability. Composes with existing [[agent-swarm]] (Kimi K2.6 scale-out) and [[subagent-patterns]] (in-session fan-out) as three scale tiers of the same coordinator/worker shape.

## [2026-04-22] ingest | Claude Mythos Preview — Cybersecurity Capabilities (Anthropic red.anthropic.com)

Source: <https://red.anthropic.com/2026/mythos-preview/> — Nicholas Carlini et al. Full assessment of [[claude-mythos-preview|Claude Mythos Preview]]'s cybersecurity capabilities. Created/updated:

- `raw/Claude Mythos Preview /Claude Mythos Preview.md` — saved verbatim
- `sources/claude-mythos-preview-red-anthropic.md` — new source; headline claims (zero-days in every major OS/browser, fully autonomous, not explicitly trained for security), scaffold methodology, 7 case studies (OpenBSD SACK 27yr, FFmpeg H.264 16yr, FreeBSD NFS RCE CVE-2026-4747, Linux kernel priv esc chains, browser JIT heap sprays, memory-safe VMM guest-to-host, crypto lib weaknesses), N-day exploit walkthroughs (ipset PTE flip, unix socket OOB UAF → root), scale of findings (thousands, 89% human severity agreement, zero false positives), defensive recommendations, SHA-3 commitments
- `entities/claude-mythos-preview.md` — new entity; full profile: restricted release, capabilities table, Opus 4.6 benchmark comparison, how capabilities emerged, notable findings, cost, relationship to Opus 4.7, Cyber Verification Program
- `entities/project-glasswing.md` — new entity; what it does, coordinated disclosure process, scale, defensive posture, future plans
- `concepts/model-cyber-capability-emergence.md` — new Thai-primary concept; "offensive = defensive = same side effect of general capability"; Mythos numbers; patterns (vuln chaining, low cost, friction-based defense weakens); cross-links to agent-runtime-untrusted / graduated-autonomy / auto-mode / advisor-strategy; "memory-safe ≠ 100% safe" note
- `concepts/agent-runtime-untrusted.md` — added Mythos Preview case study section (full-scale validation of APTS hypothesis; model that can root machines autonomously in a container = why you scope by construction); added sources + see-also
- `entities/anthropic.md` — updated Project Glasswing bullet with detail; expanded Cyber strategy section with Mythos findings scale (thousands, 89% agreement, zero FP)
- `entities/claude.md` — updated Mythos Preview table row with concrete detail
- `entities/claude-opus-4-7.md` — updated Mythos comparison bullet (cyber capabilities differentially reduced in Opus 4.7)
- `index.md` — indexed new source, 2 entities, 1 concept

Net-new value: (1) **Emergence as framing** — cyber capability is not a feature you build; it's a side effect you must manage. First in-wiki source to demonstrate this with production-scale evidence. (2) **Validates [[agent-runtime-untrusted]]** — APTS says "don't rely on model restraint"; Mythos is the "why": a model that can autonomously root machines cannot be trusted to restrain itself. (3) **Cost asymmetry** — <$50 per successful zero-day, <$1000 per N-day exploit, <1 day. Orders of magnitude cheaper/faster than human experts. (4) **Project Glasswing as release strategy** — Anthropic voluntarily restricts their most capable model, acknowledging attacker advantage in the short term. No contradictions with prior wiki content. `claude-opus-4-7` already had "cyber capabilities differentially reduced" — this source provides the *reason* (Mythos-class capabilities exist and are too dangerous for broad release).

## [2026-04-22] ingest | cyrilXBT — CLAUDE.md Guide (X post)
Source: https://x.com/cyrilXBT/status/2046589854776009208 (2026-04-21) — opinionated how-to for structuring `CLAUDE.md` in Claude Code. Created/updated:
- `raw/How to Build a CLAUDE.md File That Makes Claude Code Actually Listen to You - FULL GUIDE.md` — saved verbatim
- `sources/cyril-xbt-claude-md-guide.md` — new source; 3 file locations (project root / monorepo subdir / global `~/.claude/CLAUDE.md`), 7-section anatomy (Project Overview / Tech Stack / Coding Conventions / **Never Do This** / File Structure / Current Sprint Goals / Important Context), global preference layer, non-code usage (writing/content), 5 common mistakes (vague / never-updated / goals-vs-context / no-NEVER / no-global), composition with `.claude/commands/*.md` slash commands; explicit tension section vs Alex Ker's [[instruction-budget]] (agree on human-written + specific; disagree on volume)
- `entities/cyril-xbt.md` — new minimal entity; solo builder on X; crypto signal bot (Next.js + Supabase + Binance) as paid Gumroad product; uses CLAUDE.md for content projects too
- `concepts/claude-md.md` — new Thai-primary concept; location table, 7-section anatomy with "ได้อะไร" summary, global layer, non-code usage, tension table vs instruction-budget (Cyril ยอม rule cost / Alex Ker กลัว dumb zone), "How to apply" for frontier models (Opus 4.7), 5 common mistakes, composition with slash commands, positioning ("instance ของ [[coding-harness]] configuration")
- `concepts/instruction-budget.md` — added cross-link bullet to `[[claude-md]]` with explicit Cyril-vs-Alex-Ker tension framing; added `[[claude-md]]` + `[[cyril-xbt-claude-md-guide]]` to See also
- `entities/claude-code.md` — added **CLAUDE.md** bullet to Features section (3 layers + 7-section template + instruction-budget link); added source to frontmatter
- `index.md` — indexed new source, entity, concept

Net-new value: (1) first dedicated `claude-md` concept page consolidating the user-facing mechanics of Claude Code's flagship config file across canonical docs (3 locations) + opinionated template (Cyril 7 sections); (2) crystallizes a **real disagreement** between two in-wiki authorities — Cyril (volume-pays-back) vs Alex Ker (volume-kills-attention) — with a reconciliation heuristic rather than picking a side; (3) surfaces the "Never Do This" section as highest-leverage (Cyril's claim) while cautioning it's the section most likely to push instruction-budget; (4) confirms CLAUDE.md ≠ TODO list framing (goals live only in Current Sprint; rest is stable briefing context). No contradictions flagged — Cyril's mechanics overlap with canonical docs; the template is opinionated but not incorrect.

## [2026-04-21] ingest | Kimi K2.6 Tech Blog (Moonshot AI)
Source: https://www.kimi.com/blog/kimi-k2-6 — Moonshot AI's launch post for **Kimi K2.6**, open-source flagship for coding + long-horizon agents (262k context). Created/updated:
- `raw/Kimi K2.6 Tech Blog Advancing Open-Source Coding.md` — saved verbatim
- `sources/kimi-k2-6-tech-blog.md` — new source; headline claims (long-horizon coding / agent swarm / Claw Groups / coding-driven design / proactive agents), benchmark comparison table (K2.6 vs GPT-5.4 xhigh / Opus 4.6 max / Gemini 3.1 Pro thinking-high — note: Opus 4.7 excluded), two long-horizon showcases (Qwen3.5 Zig port, exchange-core overhaul), Kimi Design Bench / Claw Bench / Kimi Code Bench internal suites
- `entities/moonshot-ai.md` — new entity; surfaces (Kimi.com / App / API / Kimi Code / Agent Swarm / Claw Groups / KVV), internal eval suites, positioning (open-source challenger on coding + agentic, not reasoning/vision)
- `entities/kimi-k2-6.md` — new entity; capabilities, API details (262,144 token ctx, temp 1.0 / top-p 1.0, 10-run avg on coding), benchmark highlights (SWE-Bench Pro 58.6 leads Opus 4.6 53.4; HLE-tools leads; BrowseComp-swarm unique axis; trails on AIME/GPQA/vision), ecosystem (CodeBuddy, Ollama, OpenCode, Qoder, Hermes, KiloClaw, OpenClaw)
- `concepts/agent-swarm.md` — new Thai-primary concept; "scaling out, not up" axis vs subagent-patterns (300 sub-agents × 4000 steps vs K2.5's 100 × 1500); comparison table with fan-out at subagent-pattern scale; Document-to-Skill structural/stylistic DNA extraction; Claw Groups BYO-Agents extension; cautions (marketing vs measurable, latency vs cost, oversight → harness-engineering + graduated-autonomy, blast radius → agent-runtime-untrusted); scale-up vs scale-out framing (Opus 4.7 = scale-up, K2.6 = scale-out)
- `concepts/subagent-patterns.md` — added "ขยายขึ้นไปอีกระดับ — Agent Swarm" subsection linking the two patterns at different scales; source list updated
- `index.md` — indexed new source, 2 entities, 1 concept

Net-new value: (1) explicit **scale-out axis** as distinct from scale-up — first model launch in wiki to pitch on subagent count rather than model size; (2) Document-to-Skill (auto-extracted structural DNA) extends Claude Code's hand-authored Skills pattern; (3) open-source coding parity claim — SWE-Bench Pro 58.6 beats Opus 4.6 53.4, directional signal that open-source caught up on coding specifically (not reasoning/vision); (4) Claw Groups BYO-Agents is a new org pattern — heterogeneous multi-vendor agents + humans as peers with K2.6 as adaptive coordinator, distinct from owned-fleet swarm; (5) **contradiction flag**: launch excludes Claude Opus 4.7 from comparison despite being released 2026-04-16, 5 days before this ingest — treat benchmarks as curated by Moonshot.

## [2026-04-21] ingest | Somkiat — Model Choice by Domain Expertise (FB screenshot)
Source: short Thai Facebook post by Somkiat Khitwongwattana (2026-04-21), saved verbatim. Two-case heuristic: (1) Domain Expert lần code เอง → Claude Sonnet 4.5 เพียงพอกับงานส่วนใหญ่, model ใหม่กว่าเกือบไม่จำเป็น; (2) Vibe โดยไม่มี knowledge → จ่าย model ใหม่เพื่อ "ความมั่นใจในผลลัพธ์". Created/updated:
- `raw/Somkiat - Model Choice by Expertise.md` — saved Thai text verbatim
- `sources/somkiat-model-choice-by-expertise.md` — new source; two-case framing + verbatim Thai quote; cross-links to taste-paradox / judgement-vs-automation / effort-levels / delegation-mindset
- `entities/somkiat-khitwongwattana.md` — new entity (Thai SE blogger, somkiat.cc)
- `concepts/model-choice-by-expertise.md` — new Thai-primary concept; framework = คุณภาพงาน = *คน × model*; model ใหม่ = premium ที่จ่ายให้ "ต่อมเอ๊ะ ของ model"; side-by-side with taste-paradox (Somkiat = runtime; Nattee = origin); axis table vs effort-levels / task-budgets / delegation-mindset / auto-mode
- `entities/claude.md` — added Claude Sonnet 4.5 row ("good-enough baseline for dev work by domain experts")
- `concepts/taste-paradox.md` — new section "ฝั่งคู่กัน: เมื่อ *มี* taste แล้วเลือก model ยังไง" linking Somkiat's heuristic as the complement question
- `index.md` — indexed new source + entity + concept

Net-new value: (1) explicit inversion of the "newer model always better" default — model upgrade = *compensation for taste the user lacks*, not a universal gain; (2) connects cleanly to the existing Nattee taste-paradox (origin of taste) and Andrew Price judgement-vs-automation (what taste looks like across domains), giving the wiki a three-way framing around *taste*: *where it comes from* (Nattee) × *what it looks like* (Andrew) × *how to monetize what you have* (Somkiat); (3) surfaces Sonnet 4.5 explicitly as the "good-enough baseline" — previously the wiki only tracked 4.6+.

## [2026-04-21] ingest | Claude Code Remote Control docs
Source: https://code.claude.com/docs/en/remote-control.md (Anthropic docs). Feature landed in CC v2.1.51; mobile push in v2.1.110; VS Code `/remote-control` in v2.1.79. Created/updated:
- `raw/Remote Control - Claude Code Docs.md` — saved verbatim
- `sources/claude-code-remote-control-docs.md` — new source; local+relay architecture, three CLI modes + VS Code, server-mode flags (`--spawn same-dir|worktree|session`, `--capacity`, `--sandbox`), connect-from-device flow, push notifications, limitations (Ultraplan conflict, ~10min timeout, local-only pickers), auth disqualifiers (API key / setup-token / Bedrock / Vertex / Foundry), five-way comparison table
- `concepts/claude-code-remote-surfaces.md` — new Thai-primary concept; two-axis framing (local vs cloud execution × human vs event trigger) covering Remote Control / Dispatch / Channels / Slack / Scheduled / CC on the web / Ultraplan; deep dive on RC's local+relay model; cross-links to auto-mode / agent-runtime-untrusted / subagent-patterns
- `entities/claude-code.md` — added Remote Control bullet under Features with full mechanics; new "Remote surfaces" section with comparison table; see-also updated; source list updated
- `index.md` — indexed new source + new concept

Net-new value: (1) canonical "work away from terminal" taxonomy — the wiki had `/ultrareview`, auto mode, subagents but no organizing framework for mobile/web/chat/cron access; (2) architectural point that RC is **local execution + Anthropic relay** (outbound-HTTPS-only, short-lived credentials) — session never leaves the machine; contrasts cleanly with CC-on-the-web; (3) `--spawn worktree` for RC server mode connects to the existing fan-out pattern at a new layer (session rather than subagent); (4) Ultraplan-vs-RC conflict and local-only picker commands are explicit interop constraints worth remembering. Dangling wikilinks added to watchlist: `claude-code-on-the-web`, `ultraplan` (mentioned but no page).

## [2026-04-20] ingest | OWASP APTS v0.1.0 (Autonomous Penetration Testing Standard)
Source: OWASP Incubator project at github.com/OWASP/APTS (CC BY-SA 4.0). Governance standard, not a testing methodology — 173 tier-required requirements across 8 domains (SE / SC / HO / AL / AR / MR / TP / RP), plus 10 advisory practices. Three cumulative tiers (Foundation 72 / Verified 157 / Comprehensive 173). Created/updated:
- `raw/OWASP APTS.md` — saved README + Introduction verbatim
- `sources/owasp-apts.md` — new source; full domain + tier tables, L1–L4 table, capability-frontier requirements map, relationship-to-other-standards, prescriptive-value interpretation rules
- `entities/owasp.md` — new entity; OWASP Foundation with references to APTS, WSTG, ASVS, Top 10, Agentic Apps Top 10 (2026)
- `concepts/graduated-autonomy.md` — new Thai-primary concept; four-level autonomy framework (Assisted/Supervised/Semi-Autonomous/Autonomous); explicit Tier-vs-Level distinction; controls that must be added at each level; cross-links to auto-mode / subagent-patterns / advisor-strategy / harness-engineering / delegation-mindset
- `concepts/agent-runtime-untrusted.md` — new Thai-primary concept; architectural stance that agent runtime is untrusted; fail-by-construction vs verify-alignment split; maps the stance to seven specific APTS requirements (SC-019, SC-020, MR-023, AR-020, AL-028, TP-021/022, SE-026); cross-link to auto-mode / subagent-patterns / harness-engineering
- `concepts/auto-mode.md` — added see-also links to graduated-autonomy and agent-runtime-untrusted (classifier-outside-the-model = APTS-SC-020 at harness layer)
- `index.md` — indexed 1 source + 1 entity + 2 concepts

Net-new value beyond what the wiki already had: (1) APTS supplies a governance vocabulary (L1–L4) that crystallizes patterns the wiki had been circling — [[auto-mode]] / [[subagent-patterns]] / [[advisor-strategy]] / [[harness-engineering]] all fit into it. (2) The "Capability Frontier and Containment Assumptions" section states the **fail-by-construction vs. verify-alignment** split cleanly — a stance the wiki had implied but never named. (3) Explicit architectural requirements (sandbox kernel-enforced, allowlist external to model, audit trail on unreachable host, re-assess on model change) give concrete anchor points to cite against vendor hand-waving.

## [2026-04-20] ingest | OpenCode vs Claude Code (Morph, 2026-02-28)
Source: Morph vendor blog comparing [[opencode|OpenCode]] and [[claude-code|Claude Code]] ~3 weeks after the Anthropic OAuth block. Treated as directional not audited. Created/updated:
- `raw/OpenCode vs Claude Code (2026) Open Source Freedom vs Anthropic Polish.md` — saved raw
- `sources/opencode-vs-claude-code-morph.md` — new source; OAuth block timeline, Black/Zen gateways, SST→Anomaly rebrand, GitHub metrics, benchmarks (SWE-bench Pro 57.5%, ARC-AGI-2 68.8% with WarpGrep v2), system-prompt token extraction, interactivity axis (Tab/@mention/HTTP API), explicit contradiction with later Tauri→Electron move
- `entities/opencode.md` — added repo/rebrand/metrics line; new "Interactivity" subsection; new "Anthropic OAuth block (2026-01-09)" section covering Black/Zen gateways and OpenAI counter-positioning
- `entities/claude-code.md` — added "Adoption and benchmarks" section (4% of GitHub commits, VS Code install count, WarpGrep v2 benchmarks, system-prompt token counts)
- `entities/anthropic.md` — added business-metrics line ($380B valuation, $14B ARR, "Claude Code Moment") and OpenCode OAuth block section
- `index.md` — indexed new source

Net-new value despite vendor framing: (1) OAuth block event and OpenCode's Black/Zen response were not in the wiki; (2) Tab/@mention/HTTP-API interactivity axis for OpenCode complements the provider-breadth/shell-architecture framing from earlier sources; (3) system-prompt token extractions (core 2896, Plan 633, Explore 516, Task 294) ground the abstract subagent discussion. Contradiction noted: source says OpenCode desktop is Tauri — stale as of 2026-03-25, see [[opencode-desktop-electron-brendonovich]].

## [2026-04-20] ingest | Auto mode for Claude Code (Anthropic blog, 2026-03-24)
Source: Anthropic blog post announcing **auto mode** — a new permission mode in [[claude-code|Claude Code]] where a classifier reviews each tool call before it runs (auto-approves safe, blocks risky like mass delete / exfiltration / malicious exec, redirects Claude, prompts user only if Claude keeps insisting). Middle path between default (ask every action) and `--dangerously-skip-permissions`. Launched as research preview on Team plan with Sonnet/Opus 4.6; later extended to Claude Code Max users with Opus 4.7 launch (already referenced in existing 4.7 announcement). Created/updated:
- `raw/Auto mode for Claude Code.md` — saved raw
- `sources/claude-code-auto-mode.md` — new source; how it works, classifier block list, caveats, enablement paths
- `concepts/auto-mode.md` — new Thai-primary concept; permission-mode spectrum table (default / auto / dangerously-skip), classifier mechanics, when not to enable, cross-links to delegation-mindset / coding-harness / subagent-patterns
- `entities/claude-code.md` — fleshed out the one-liner Auto mode bullet into full mechanics + dates + enablement commands
- `entities/claude-opus-4-7.md` — clarified that auto mode itself shipped earlier (2026-03-24); 4.7 launch extended it to Max
- `concepts/delegation-mindset.md` — linked auto-mode concept from the Pachaar "three moves" section
- `index.md` — indexed new source + new concept

Notable: this source predates [[claude-opus-4-7|Opus 4.7]] by ~3 weeks — auto mode is a harness-level feature tied to plan tier, not to model version. Works with Sonnet 4.6 + Opus 4.6 at launch. Classifier-gate pattern parallels harness-side [[subagent-patterns|pipeline subagents]] at a lower layer: the harness inserts the reviewer, not the user.

## [2026-04-20] ingest | Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6 (Akshay Pachaar)
Source: third-party migration guide by @akshay_pachaar (X, 2026-04-20). Most content confirms the two existing Anthropic sources; net-new value is reframing the official behavior-change list as workflow problems with concrete prompt fixes. Created/updated:
- `raw/Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6.md` — saved raw
- `sources/claude-opus-4-7-migration-pachaar.md` — new source; explicit "net-new vs. Anthropic sources" table
- `concepts/delegation-mindset.md` — new Thai-primary concept: 4.7 triggers reasoning every user turn → front-load context in turn 1 (intent / constraints / acceptance criteria / paths); batch questions; auto mode (Shift+Tab) for trusted tasks
- `concepts/find-vs-filter.md` — new Thai-primary concept: split code review into coverage-first find + downstream filter; concrete prompt with confidence+severity metadata; generalizes to security audit / moderation / triage; links to subagent-patterns (pipeline) and advisor-strategy (executor finds, advisor filters)
- `entities/claude-opus-4-7.md` — added prefilled-response deprecation (starting 4.6; 400 on Mythos Preview), turn-triggers-reasoning note, literal-following-drops-code-review-recall note
- `effort-levels.md` — noted `low` tier as third-party unverified claim; added mid-task effort toggling pattern (xhigh design → high impl → max debug)
- `index.md` — indexed new source and two new concepts

Explicit contradiction recorded: Pachaar lists 5 effort tiers (low/medium/high/xhigh/max); Anthropic docs list 4 (medium/high/xhigh/max). Flagged in source page + effort-levels.

## [2026-04-19] ingest | Moving OpenCode Desktop to Electron (@brendonovich primary source)
Source: @brendonovich's canonical X writeup (2026-03-25) — the primary source behind the earlier Grok summary. Created/updated:
- `raw/Moving OpenCode Desktop to Electron.md` — saved raw
- `sources/opencode-desktop-electron-brendonovich.md` — new source
- `entities/tauri.md` — added WebKit-on-macOS/Linux caveat, CEF effort, Rust-heavy-core sweet spot
- `entities/electron.md` — folded in WebKit-vs-Chromium parity + Bun→Node framing + bundle-size trade-off
- `entities/opencode.md` — restructured desktop-shell section with 3 combined reasons; noted Bun-API plugin breakage deferred to OpenCode 2.0
- `sources/opencode-tauri-to-electron.md` — added cross-reference note pointing to the primary source
- `index.md` — indexed new source

Net-new beyond the earlier Grok summary: (1) **WebKit rendering perf + style parity** on macOS/Linux was a first-class reason, not just "Chromium is more consistent"; Tauri has a CEF effort but stabilization documentation timing is uncertain. (2) **Bun → Node migration** was underway for other reasons and unlocked the in-process architecture — it's a cascading cause, not just a consequence. (3) **Plugin fallout:** Bun-specific-API plugins stop working; full story deferred to OpenCode 2.0. (4) Tauri-fit condition stated crisply: "Rust heavy core" (Cap video encoding is the canonical fit); shell-only Rust doesn't move the needle.

## [2026-04-19] ingest | What's new in Claude Opus 4.7 (Anthropic docs)
Source: Anthropic developer docs page for Opus 4.7 — developer-facing companion to the earlier marketing announcement. Created/updated:
- `raw/Whats new in Claude Opus 4.7 - Anthropic Docs.md` — saved raw
- `sources/claude-opus-4-7-whats-new-docs.md` — new source (API breaking changes, behavior changes, migration)
- `concepts/task-budgets.md` — new Thai-primary concept (beta feature; model-aware countdown; distinct from `max_tokens`)
- `concepts/adaptive-thinking.md` — new Thai-primary concept (only thinking-on mode on 4.7; off by default; thinking content also hidden by default)
- `entities/claude-opus-4-7.md` — added API breaking changes + behavior changes sections; linked new concepts
- `concepts/effort-levels.md` — added 4.7 recommendation (start xhigh for coding); added "Relation to adaptive thinking" section
- `index.md` — indexed new source + 2 new concepts

Key additions beyond what the announcement covered: `thinking.budget_tokens` → 400 error (extended thinking budgets removed); non-default `temperature`/`top_p`/`top_k` → 400 error; thinking content omitted by default (silent change — streaming products will see a long pause before output); `task_budget` is advisory/model-aware while `max_tokens` is a hidden hard cap; adaptive thinking is OFF by default on 4.7.

## [2026-04-18] ingest | OpenCode: Tauri to Electron switch reasons
Source: Grok chat summarizing @brendonovich's explanation for OpenCode's desktop shell migration. Created/updated:
- `sources/opencode-tauri-to-electron.md` — new source
- `entities/tauri.md` — new entity (Rust desktop framework, native webviews)
- `entities/electron.md` — new entity (Chromium + Node.js desktop framework)
- `entities/opencode.md` — added "Desktop shell: Tauri → Electron" section + cross-links
- `index.md` — indexed new source and two new entities

Key point: not a Tauri-vs-Electron verdict; pick the shell whose main-process runtime matches where your app's heavy logic already lives. OpenCode's `opencode serve` is a JS/Bun server — Electron hosts it in-process; Tauri required a sidecar with IPC overhead and cross-platform reliability issues (especially Windows/Linux).

## [2026-04-12] init | Wiki initialized
Set up directory structure, CLAUDE.md schema, index, and log.

## [2026-04-12] ingest | UI Style Categories
Source: Claude conversation cataloging UI/UX design styles. Created 5 wiki pages:
- `sources/ui-style-categories.md` — full taxonomy with 11 categories, ~40+ styles
- `concepts/diegetic-ui.md` — in-world UI with 5 sub-styles
- `concepts/glassmorphism.md` — frosted glass aesthetic
- `concepts/brutalism.md` — raw/anti-decorative UI
- `concepts/retro-futurism.md` — 80s sci-fi aesthetic with related style spectrum

## [2026-04-13] ingest | Retro Futuristic UI Design
Source: Two clips from a Claude conversation providing a complete retro-futurism UI design system. Created/updated 5 wiki pages:
- `sources/retro-futuristic-ui-design.md` — full source summary with five subgenres, palettes, typography, implementation patterns
- `concepts/retro-futurism.md` — major update: broadened from "80s sci-fi" to full 1930s–80s spectrum with five subgenres, design principles, aesthetic rules
- `concepts/cassette-futurism.md` — new: 1970s–80s terminal/VHS subgenre
- `concepts/atompunk.md` — new: 1950s–60s atomic age subgenre
- `concepts/raygun-gothic.md` — new: 1930s–50s art deco/chrome subgenre

## [2026-04-13] ingest | GitNexus: The Zero-Server Code Intelligence Engine
Source: GitHub README for GitNexus by Abhigyan Patwari / Akon Labs. Created 6 wiki pages:
- `sources/gitnexus.md` — full source summary: architecture, capabilities, tech stack, MCP integration
- `entities/gitnexus.md` — product entity: open-source code intelligence engine
- `entities/akon-labs.md` — company entity: enterprise offering behind GitNexus
- `concepts/code-knowledge-graphs.md` — knowledge graphs built from codebase structure
- `concepts/graph-rag.md` — Graph RAG pattern and precomputed vs. traditional approaches
- `concepts/model-context-protocol.md` — MCP: open protocol for AI agent tool integration

## [2026-04-13] ingest | Soviet Cosmism UI Style
Source: Claude conversation describing Soviet Cosmism as a UI design language. Created/updated 3 wiki pages:
- `sources/soviet-cosmism-ui-style.md` — source summary: philosophical roots, visual DNA, UI patterns
- `concepts/soviet-cosmism.md` — new: constructivist/Soviet space program UI subgenre within retro-futurism
- `concepts/retro-futurism.md` — updated: added wikilink to soviet-cosmism in subgenre table

## [2026-04-12] ingest | LLM Knowledge Bases Thread by @karpathy
Source: Twitter thread (2026-04-02) describing the LLM wiki pattern. Created 3 wiki pages:
- `sources/karpathy-llm-knowledge-bases.md` — full thread summary with workflow and insights
- `entities/andrej-karpathy.md` — AI researcher who originated the pattern
- `concepts/llm-knowledge-bases.md` — the meta-concept: LLM-maintained knowledge bases

## [2026-04-14] ingest | The Four Horsemen of Game UI Design
Source: Corporation Pop article classifying game UI into four types. Created/updated 5 wiki pages:
- `sources/four-horsemen-game-ui.md` — source summary: diegetic/non-diegetic/spatial/meta taxonomy with trade-offs
- `concepts/non-diegetic-ui.md` — new: traditional overlay UI external to game world
- `concepts/spatial-ui.md` — new: UI placed in 3D space but invisible to characters
- `concepts/meta-ui.md` — new: screen effects reflecting character state
- `concepts/diegetic-ui.md` — updated: added game UI taxonomy context, examples, limitations, comparison table

## [2026-04-14] ingest | Helix Release 25.07 Highlights
Source: Helix editor release notes (2025-07-15). Created 4 wiki pages:
- `sources/helix-release-25-07.md` — source summary: file explorer, LSP document colors, command mode rewrite, Tree-house deep dive
- `entities/helix.md` — post-modern modal text editor with built-in tree-sitter/LSP
- `concepts/tree-sitter.md` — parsing framework: incremental, error-tolerant, query-based
- `concepts/tree-house.md` — Helix's new tree-sitter integration crate with injection tree architecture

## [2026-04-14] ingest | Soviet Cosmism Philosophy
Source: Claude conversation building a comprehensive Soviet Cosmism UI skill with deep philosophical grounding. Created/updated 7 wiki pages:
- `sources/soviet-cosmism-philosophy.md` — new: full source summary with five pillars, three palettes, animation vocabulary, CSS foundation, component library
- `entities/nikolai-fedorov.md` — new: originator of Cosmism, resurrection philosophy
- `entities/konstantin-tsiolkovsky.md` — new: rocket pioneer, key Cosmist thinker
- `entities/vladimir-vernadsky.md` — new: noosphere creator
- `concepts/noosphere.md` — new: Earth's collective thinking layer, bridges Cosmism and modern collective intelligence
- `concepts/soviet-cosmism.md` — major update: added five pillars, three canonical palettes, typography hierarchy, iconographic vocabulary, animation vocabulary, layout principles, components, philosophical quotes

## [2026-04-14] ingest | Holographic UI
Source: Claude conversation defining a complete Holographic UI design skill. Created/updated 5 wiki pages:
- `sources/holographic-ui.md` — new: source summary with 5 variants, rendering techniques, animation library, component recipes, layout patterns, 10 design rules
- `concepts/holographic-ui.md` — new: holographic UI as a distinct design language bridging glassmorphism and diegetic UI
- `concepts/diegetic-ui.md` — updated: wikilinked Holographic Projection sub-style, added holographic-ui to See Also
- `concepts/glassmorphism.md` — updated: added holographic-ui to See Also
- `sources/ui-style-categories.md` — updated: wikilinked Holographic UI in sci-fi sub-styles

## [2026-04-14] ingest | Imetomi/retro-futuristic-ui-design
Source: GitHub README for open-source React + TypeScript CRT/LCD component library. Created/updated 6 wiki pages:
- `sources/imetomi-retro-futuristic-ui.md` — new: source summary with CSS layering technique, color palettes, component breakdown
- `entities/imetomi.md` — new: developer behind the project
- `entities/nathan-david-jones.md` — new: concept artist whose work inspired the components
- `concepts/cassette-futurism.md` — updated: added CSS CRT technique section with implementation details
- `concepts/retro-futurism.md` — updated: added link to Imetomi implementation in See Also

## [2026-04-14] ingest | forrestchang/andrej-karpathy-skills (Karpathy Guidelines)
Source: `SKILL.md` from forrestchang's Claude Code skills repo, packaging Karpathy's observations on LLM coding pitfalls into four behavioral rules. Created/updated 4 wiki pages:
- `sources/karpathy-guidelines.md` — new: source summary with the four principles and their rules
- `concepts/llm-coding-pitfalls.md` — new: meta-concept cataloging hidden confusion, overcomplication, scope drift, weak success criteria
- `entities/forrestchang.md` — new: developer who packaged the skill
- `entities/andrej-karpathy.md` — updated: added coding-pitfalls observations alongside the knowledge-bases pattern; noted both use lightweight markdown schemas

## [2026-04-15] ingest | What's new in C# 14
Source: Microsoft Learn article by Bill Wagner covering C# 14 (ships with .NET 10). Created 4 wiki pages:
- `sources/csharp-14-whats-new.md` — new: full feature list with code samples for all nine additions
- `entities/csharp.md` — new: C# language entity, anchored to C# 14 as current release
- `concepts/extension-members.md` — new: `extension<T>(Receiver)` block syntax generalizing extension methods to properties, static members, and operators
- `concepts/field-keyword.md` — new: contextual `field` keyword inside property accessors for compiler-synthesized backing fields

## [2026-04-16] ingest | Karpathy's LLM Wiki: The Complete Guide to His Idea File
Source: antigravity.codes deep dive into Karpathy's LLM Wiki GitHub gist (Apr 4 2026). Created 4 new pages, updated 2:
- `sources/karpathy-llm-wiki-idea-file.md` — new: full summary covering idea file concept, wiki vs RAG comparison, three-layer architecture, three operations, tool stack (qmd, Web Clipper, Marp, Dataview, Git), Memex connection, community patterns
- `concepts/idea-file.md` — new: Karpathy's concept of sharing abstract patterns for LLM agents to instantiate rather than sharing code
- `concepts/memex.md` — new: Vannevar Bush's 1945 Memex as ideological ancestor of LLM wikis; the maintenance problem LLMs solve
- `entities/vannevar-bush.md` — new: Bush biography, "As We May Think," influence on Engelbart/Nelson/Berners-Lee
- `concepts/llm-knowledge-bases.md` — updated: added explicit RAG vs wiki comparison table, compounding loop, qmd tool, Memex connection, schema co-evolution
- `entities/andrej-karpathy.md` — updated: added vibe coding coinage, idea file gist, Memex reference, research wiki scale details

## [2026-04-16] ingest | The Advisor Strategy: Give Agents an Intelligence Boost
Source: Anthropic blog post (2026-04-09) introducing the advisor strategy and `advisor_20260301` API tool. Created 2 new pages, updated 1:
- `sources/advisor-strategy.md` — new: source summary with core idea (inverted orchestrator-worker), benchmark results (SWE-bench, BrowseComp, Terminal-Bench), API shape, pricing, cost controls
- `concepts/advisor-strategy.md` — new: advisor pattern as agent architecture — cheap executor escalates to expensive advisor only at hard decisions; comparison table vs orchestrator-worker; when to use
- `concepts/ai-orchestrator.md` — updated: added "The advisor inversion" section with wikilink to advisor-strategy

## [2026-04-16] ingest | I Made a Terminal Pager — Leo Robinovitch
Source: theleo.zone blog post on building a reusable Go viewport component and lore terminal pager. Created 4 new pages, updated 1:
- `sources/leo-robinovitch-terminal-pager.md` — new: viewport architecture (item/viewport/filterableviewport), Unicode terminal-width handling, $PAGER mechanism, lore pager, kl/wander TUIs
- `entities/leo-robinovitch.md` — new: Go TUI developer; viewport, lore, kl, wander
- `concepts/tui.md` — new: Terminal User Interfaces — alt screen, keyboard-driven, grid-cell constraint, Bubble Tea/Ratatui frameworks
- `concepts/terminal-pager.md` — new: $PAGER programs — less, bat, delta, lore; how programs invoke pagers; pager vs TUI distinction
- `entities/helix.md` — updated: added [[tui]] to See Also

## [2026-04-16] ingest | Using Claude Code: Session Management & 1M Context
Source: Twitter/X thread by @trq212 (2026-04-16) on Claude Code session management against the 1M token context window. Created 3 new pages, updated 2:
- `sources/claude-code-session-management.md` — new: full guide summary — context rot threshold, five branching options per turn, rewind habit, compact vs clear, bad compacts, subagents for context isolation
- `concepts/context-rot.md` — new: model performance degradation as context fills; ~300–400k token threshold; mitigations table
- `concepts/compaction.md` — new: /compact mechanism, manual vs autocompact, what causes bad compacts, compact vs /clear comparison table, steering instructions
- `concepts/ai-orchestrator.md` — updated: added "Subagents as context management" section linking context-rot and compaction
- `wiki/index.md` — updated: added new source and two new concepts

## [2026-04-16] ingest | Introducing Claude Opus 4.7
Source: Anthropic announcement blog (2026-04-16) for Claude Opus 4.7. Created 6 new pages, updated 5:
- `sources/claude-opus-4-7-announcement.md` — new: full summary — SWE gains, self-verification, 2576px vision, file-system memory, xhigh effort, /ultrareview, auto mode, tokenizer migration (1.0–1.35×), Project Glasswing cyber posture
- `entities/anthropic.md` — new: company entity; products, platform distribution, originated patterns (advisor, MCP, effort levels, compaction)
- `entities/claude.md` — new: model family entity; Opus/Sonnet/Haiku/Mythos table, capabilities, surfaces
- `entities/claude-opus-4-7.md` — new: flagship model entity; improvements, regressions, new controls, cyber posture, availability
- `entities/claude-code.md` — new: Anthropic's CLI coding agent; session architecture, commands, subagents, skills, hooks, auto mode
- `concepts/effort-levels.md` — new: medium/high/xhigh/max tiers and their effect on token usage; cost controls
- `wiki/index.md` — updated: 1 new source, 4 new entities, 1 new concept
- Inbound linking: advisor-strategy (source + concept), claude-code-session-management (source), context-rot, compaction updated to reference new entities

## [2026-04-17] ingest | A Guide to vim.pack
Source: Blog post by Evgeni Chasnovski (2026-03-13) on Neovim 0.12's built-in plugin manager. Created 5 new pages, updated 2:
- `sources/vim-pack-guide.md` — new: full summary — API, lockfile, autocmd hooks, lazy-loading patterns, migration from mini.deps/lazy.nvim, limitations
- `concepts/vim-pack.md` — new: Neovim 0.12 built-in plugin manager; three-function API, all-opt design, trade-offs vs lazy.nvim, hook ordering gotcha
- `concepts/plugin-manager.md` — new: general pattern; five core responsibilities, Neovim manager landscape, transparent-vs-declarative trade-off, lockfiles
- `entities/neovim.md` — new: Lua-embedded Vim fork; runtime conventions, 0.12 plugin manager milestone, position vs Helix/VS Code
- `entities/evgeni-chasnovski.md` — new: mini.nvim and mini.deps author; design influence on vim.pack; moderate lazy-loading philosophy
- `entities/helix.md` — updated: added cross-links to neovim, plugin-manager, vim-pack in plugin-system contrast
- `wiki/index.md` — updated: 1 new source, 2 new entities, 2 new concepts

## [2026-04-18] ingest | Will AI Replace 3D Software? — Andrew Price
Source: Andrew Price X thread (2026-04-17) answering top three questions from North American Blender Conference on AI + 3D. Created 7 new pages, updated 2, and closed prior index lint gap:
- `sources/will-ai-replace-3d-software.md` — new: thread summary with three Q&As (AI won't replace 3D; hybrid artist wins; judgement-heavy skills survive) plus moon-base workflow walkthrough
- `entities/andrew-price.md` — new: Blender Guru; AI + 3D advocate
- `entities/blender.md` — new: open-source 3D creation suite; anchor tool for the workflow
- `entities/comfyui.md` — new: node-based diffusion workflow UI; hosts Flux.1 Depth template
- `entities/flux.md` — new: Black Forest Labs diffusion family; Flux.1 Depth supports geometry-conditioned generation
- `concepts/ai-3d-workflow.md` — new: hybrid pipeline — AI for ideation/rendering, 3D for precision/control; canonical moon-base example
- `concepts/judgement-vs-automation.md` — new: "if you can predict it, you can train it" skill framework; generalizes to software via engineering-role-shift
- `concepts/engineering-role-shift.md` — updated: added judgement-vs-automation and ai-3d-workflow to See also
- `wiki/index.md` — updated: added 1 new source, 4 new entities, 2 new concepts; closed prior lint gap by indexing `software-engineer-role-ai-era`, `engineering-role-shift`, `ai-orchestrator`, `domain-to-ai-translator`
- Meshy (image-to-3D service) folded into source and ai-3d-workflow prose rather than a standalone entity page — narrow-scope tool, one-off mention

## [2026-04-18] convention | Bilingual Thai+English for concept pages
Added `## Bilingual content` section to CLAUDE.md. First iteration allowed general mixing with English-primary default; same-day revision tightened the rule per-page-type: concept pages default to Thai-primary body with English kept for technical terms, product/tool/library names, code identifiers, and direct English-source quotes; source/entity/analysis pages default to English (source pages switch to Thai when the source is Thai). Tooling stays English (filenames, wikilink targets, frontmatter `title:`/`tags:`, index.md entries). `wiki/concepts/ai-3d-workflow.md` rewritten as the Thai-primary reference demo. Existing 36 other concept pages NOT retrofitted — pending user confirmation.

## [2026-04-18] ingest | Harness Engineering — Panutat Tejasen
Source: Thai Facebook post (2026-04-18) by Panutat Tejasen arguing against teaching students to "review" or "advise" AI coding agents and proposing "Harness Engineering" as the curriculum alternative. First concept page written as Thai-primary from scratch. Created 4 new pages, updated 2:
- `sources/harness-engineering-panutat.md` — new (Thai body): post summary, core claims, verbatim quote of the central proposal, links to related concepts
- `entities/panutat-tejasen.md` — new (English, minimal): scoped to what the source reveals — author of the Harness Engineering proposal
- `concepts/harness-engineering.md` — new (Thai-primary): harness = pipeline of AI agents for Review, Inspection, Test Cases, E2E Testing, Security Audit; human role shifts to harness design; comparisons with advisor-strategy and ai-orchestrator; open questions on model diversity in pipelines
- `concepts/ai-orchestrator.md` — updated: added harness-engineering and panutat-tejasen to See also; bumped `updated` date
- `concepts/engineering-role-shift.md` — updated: added harness-engineering and panutat-tejasen to See also
- `wiki/index.md` — updated: 1 new source, 1 new entity, 1 new concept

## [2026-04-18] ingest | วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง (Ep. 1 + Ep. 2) — Nattee Niparnan
Source: Two-part Thai Facebook series by Nattee Niparnan (Chula CEDT). Ep. 1 (2026-04-10) catalogs pedagogy experiments (LLM-in-grader with Socratic-only prompt + −10 pts/click cost capping at 70 after 3 clicks, chat-log-as-submission, อ. สมชาย's prompt-as-exam, flip classroom find-the-bug). Ep. 2 (~2026-04-17) introduces the "taste paradox" via a $140 PoC Web App (Claude Code + Antigravity + Figma Make) that replaced 3–4 RAs; includes an authorization war story where every endpoint passed unit tests but Buyer could delete Seller's resources. Created 3 new pages, updated 5:
- `sources/llm-era-computer-engineering-nattee.md` — new (Thai body): both episodes summarized; Ep. 1 pedagogy enumerated as a table (not blurred into prose); Ep. 2 PoC story with dollar figures and the taste-paradox lead-in; explicit Nattee–Panutat dialogue
- `entities/nattee-niparnan.md` — new (English, minimal): Chula CEDT faculty, cafe-grader maintainer (from Jittat + Pramook), series author; faculty name-drops catalogued without dedicated entity pages
- `concepts/taste-paradox.md` — new (Thai-primary): recursive skill-acquisition loop; side-by-side comparison with harness-engineering (Panutat = scope of reviewability vs. Nattee = origin of the reviewer); open curricular questions on depth threshold and anchor-domain choice
- `concepts/engineering-role-shift.md` — updated: added "Core theory becomes more important, not less" section (DS/Algo/Discrete Math as AI-verification substrate); added "Design choices pushed down to juniors" section; new source in frontmatter
- `concepts/harness-engineering.md` — updated: added "ดูควบคู่กับ taste-paradox" comparison section framing the two as complementary at different layers (technology vs pedagogy); new source in frontmatter
- `concepts/judgement-vs-automation.md` — updated: added "The compromise criteria rotate" section with Nattee's framework-selection table (pre-Agent "team fluency / dev speed" vs Agent-era "Agent stability / token cost"); added "Entry-level hiring signal" ($140 vs 3–4 RAs) section
- `concepts/ai-orchestrator.md` — updated: added "Downward pressure on seniority requirements" section — orchestration work lands on juniors before they've built the judgment it requires
- `concepts/llm-coding-pitfalls.md` — updated: added authorization-bug war story as concrete multi-pitfall illustration (scope kept too narrowly per-endpoint + weak success criterion + unchallenged default interpretation = silent cross-cutting failure)
- `wiki/index.md` — updated: 1 new source, 1 new entity, 1 new concept

## [2026-04-18] ingest | Harnesses are everything — Alex Ker (@thealexker)
Source: X post (2026-04-18) by Alex Ker synthesizing harness-optimization advice: lean human-written CLAUDE.md, progressive disclosure (CLIs / Skills / MCP), R.P.I. prompt pattern, subagent patterns (parallel fan-out vs pipeline), commit-to-one-harness. Introduces a second sense of the word "harness" — the scaffolding tool (Claude Code, Codex, OpenCode, Cursor) — distinct from Panutat's curriculum sense. Created 9 new pages, updated 5:
- `sources/alex-ker-harnesses-optimize.md` — new (English body, source is English): full post summary with key claims attributed
- `entities/alex-ker.md` — new: GitHub handle `AlexKer`, Twitter `@thealexker`, contributor to Roo Code / DeepAgent CLI / HumanLayer, formerly Baseten (gpt-oss-swarm)
- `entities/humanlayer.md` — new: company cited as source for the "dumb zone" instruction-budget framing and the R.P.I. framework
- `entities/openai-codex.md` — new: OpenAI coding harness; converges with Claude Code on skills progressive disclosure but diverges on MCP handling
- `entities/opencode.md` — new: open-source harness; loads all MCP tool definitions at startup (docs warn users to limit server count)
- `concepts/coding-harness.md` — new (Thai-primary): the harness as scaffolding layer; while-loop + context-mgmt + tool-wiring; Alex Ker's three levers (lean config, R.P.I., subagents); "commit to one harness" rationale. R.P.I. section folded in here rather than a separate page
- `concepts/instruction-budget.md` — new (Thai-primary): the "dumb zone" past few-hundred instructions; explicit disambiguation table vs context-rot (instruction count vs total token count — different cause, similar symptom)
- `concepts/progressive-disclosure.md` — new (Thai-primary): lazy-loading pattern with three illustrations — CLIs (--help discovery), Skills (name+description only, body on demand), MCP tools (Claude Code tool search 85% context reduction vs Codex/OpenCode load-all)
- `concepts/subagent-patterns.md` — new (Thai-primary): parallel fan-out (breadth, investigation) vs pipeline (depth, multi-lens review); explicit parallel to Panutat's review-agent pipeline — same pattern, productivity vs pedagogy lens
- `concepts/harness-engineering.md` — updated: added disambiguation note pointing to `coding-harness` for Alex Ker's sense; added section "เชื่อมกับ subagent-patterns ของ Alex Ker" framing Panutat's pipeline as the same pattern Alex Ker calls a pipeline subagent
- `concepts/ai-orchestrator.md` — updated: added "R.P.I. — a prompt-level discipline that mirrors orchestration" section
- `concepts/advisor-strategy.md` — updated: added "Advisor as pipeline judge" section (frontier model consolidating subagent fan-out output)
- `entities/claude-code.md` — updated: MCP tool-search (~85% context reduction) added to feature description; See also expanded
- `sources/claude-code-session-management.md` — updated: cross-links to coding-harness / subagent-patterns / progressive-disclosure / instruction-budget
- `wiki/index.md` — updated: 1 new source, 4 new entities, 4 new concepts

## [2026-04-18] ingest | Claude Code Subagents Docs (code.claude.com/docs/en/sub-agents.md)
Source: Anthropic's official Claude Code subagent reference. Canonical mechanics complement Alex Ker's design patterns and Panutat's harness-engineering framing.
- `raw/Create custom subagents - Claude Code Docs.md` — raw fetched doc
- `sources/claude-code-subagents-docs.md` — new source summary: built-in agents (Explore/Plan/general-purpose), full frontmatter field table, scope priority, persistent memory scopes, hooks (frontmatter + SubagentStart/Stop), invocation (natural / @-mention / `--agent`), foreground vs background, resumption via SendMessage, cross-links to existing concept pages
- `entities/claude-code.md` — updated: subagent bullet expanded with concrete mechanics (built-in list, frontmatter fields, invocation modes, nested-spawn constraint)
- `concepts/subagent-patterns.md` — updated: new "Mechanics ใน Claude Code" section mapping fan-out/pipeline to Claude Code primitives (`Explore`, `.claude/agents/`, `model: haiku`, `memory: project`)
- `wiki/index.md` — updated: 1 new source entry
## [2026-04-25] ingest | RTK (RTK-AI)
Ingested RTK-AI GitHub repository. Created source summary `wiki/sources/rtk-github.md`, entity `wiki/entities/rtk.md`, and Thai-primary concept `wiki/concepts/token-optimization.md`. Updated index. RTK is a Rust-based CLI proxy for token compression (60-90% reduction).

## [2026-04-25] ingest | Guillermo Rauch - Building the Generative Web
Ingested Sequoia talk by Guillermo Rauch (Vercel CEO). Created source `wiki/sources/rauch-generative-web.md`, entities `wiki/entities/guillermo-rauch.md`, `wiki/entities/vercel.md`, `wiki/entities/v0-dev.md`, and concepts `wiki/concepts/generative-ui.md`, `wiki/concepts/ephemeral-apps.md`. Updated index. Key themes: ephemeral apps, generative UI, LLMs as customers, and the "Pit of Success" framework strategy.

## [2026-04-27] ingest | Annabel - Your Wealth Architect — Response to Controversy

สรุปโพสต์ชี้แจงจากคุณแอมนาเบล (Annabel) ต่อประเด็นดราม่าเรื่องประวัติการทำงานและสไตล์คอนเทนต์ "Financial Poetry" พร้อมให้ข้อมูลเชิงลึกเกี่ยวกับกระบวนการทำงานจริงในระบบ Private Banking

- สร้างหน้า raw: `raw/annabel-wealth-architect-response.md`
- สร้างหน้า source: `[[annabel-wealth-architect-response]]`
- สร้างหน้า concept: `[[alternative-assets]]` (Thai-primary) — อธิบายเรื่อง Hedge Fund, Private Equity ในพอร์ต UHNW
- สร้างหน้า entity: `[[ubs]]`, `[[lgt-bank]]`, `[[abn-amro]]`
- อัปเดตหน้า `[[annabelle]]`: เพิ่ม Career Timeline (SCB -> ABN -> LGT -> UBS) และสรุปคำชี้แจงต่อประเด็นต่างๆ
- อัปเดตหน้า `[[private-banking]]`: เพิ่มรายละเอียดกระบวนการ Call Report, 4-eyes principle และการทำงานภายใต้ Securities and Futures Act
- อัปเดตหน้า `[[financial-poetry]]`: เพิ่มมุมมองจากฝั่งผู้ผลิตคอนเทนต์เรื่องการ Simplify สำหรับมือใหม่
- อัปเดต `[[index]]`

ประเด็นสำคัญ: (1) ยืนยันกระบวนการ Voice Log และ Call Report ทำให้การแอบเทรดเป็นไปไม่ได้; (2) เส้นทางการทำงานจริงในสิงคโปร์และสวิตเซอร์แลนด์ช่วงปี 2018-2025; (3) การใช้ AI เป็นเครื่องมือในการทำงาน; (4) การจัดพอร์ตแบบ Subjective ที่มีตั้งแต่เน้นรักษาเงินต้นไปจนถึงเน้นสินทรัพย์ทางเลือก 60%

## [2026-04-27] ingest | Gee Money & More — Singapore Private Banking

สรุปโพสต์จากเพจ Facebook "Gee Money & More" โดย Private Banker จากสิงคโปร์ เพื่อชี้แจงความเข้าใจผิดเกี่ยวกับงานของ Private Banker และมาตรฐานของศูนย์กลางการเงินสิงคโปร์ (Singapore Finance Hub)

- สร้างหน้า raw: `raw/gee-money-sg-pb.md`
- สร้างหน้า source: `[[gee-money-sg-pb]]`
- สร้างหน้า concept: `[[private-banking]]` (Thai-primary) — อธิบายความแตกต่างระหว่าง PB (Relationship Manager) กับ Portfolio Manager, เรื่อง Unauthorized Trading, และความสำคัญของ Voice Log
- สร้างหน้า entity: `[[singapore]]`, `[[gee-money-more]]`
- อัปเดต `[[index]]`

ประเด็นสำคัญ: (1) Private Banker ไม่มีสิทธิ์เทรดเองโดยพลการ ทุกรายการต้องมี voice log; (2) หากต้องการให้ธนาคารจัดการแทนต้องเซ็น Discretionary Mandate; (3) ลูกค้า PB เน้น "ความปลอดภัยและยั่งยืน" (Wealth Protection) มากกว่ากำไรหวือหวา 2-หลัก; (4) จุดเด่นของสิงคโปร์คือ Regulatory Framework ที่แข็งแกร่งและความโปร่งใส

## [2026-04-27] ingest | thClaws Announcement (Panutat Tejasen)
สรุปโพสต์ของ [[panutat-tejasen|Panutat Tejasen]] เกี่ยวกับการเปิดตัว [[thclaws]] (โปรเจกต์แกะรอย [[claude-code]] ด้วยภาษา Rust) และการเปลี่ยนผ่านจากยุค "LLM Wrapper" ไปสู่ยุค "Harness Engineering" (วิศวกรรมบังเหียน) 

สร้างหน้าใหม่:
- [[thclaws-announcement-panutat]] (Source summary - Thai)
- [[product-overhang]] (Concept - Thai-primary)
- [[thclaws]] (Entity - Thai-primary)

อัปเดตหน้าเดิม:
- [[panutat-tejasen]] (Entity - Thai-primary refinement)
- [[harness-engineering]] (Concept - Added sections on Agentic Apps and thClaws elements)
- [[index]] (Updated with new pages)


## [2026-04-27] ingest | GitHub Copilot Usage-Based Billing Update
GitHub announcement regarding the move to usage-based billing starting June 1, 2026. Transitioning from PRUs to **GitHub AI Credits** driven by the compute demands of **Agentic Usage**. Code completions remain unlimited, while multi-step repo-wide sessions and code reviews draw from a monthly credit allotment.

- Created source page: `[[github-copilot-billing-update]]`
- Created entity pages: `[[github]]`, `[[github-copilot]]`
- Created Thai-primary concept pages: `[[agentic-usage]]`, `[[usage-based-billing]]`, `[[github-ai-credits]]`
- Updated `[[index]]` and this log

## [2026-04-27] Ingest | thClaws Positioning
Ingested Panutat Tejasen's post on thClaws' positioning as an open-source project. Created source summary, updated thClaws and Panutat Tejasen entities. Created new concepts: [[open-source-governance]] and [[papercut-features]].

## [2026-04-27] ingest | DeepSeek Wikipedia
Ingested the Wikipedia page for DeepSeek. Created source summary, entity pages for DeepSeek, High-Flyer, and Liang Wenfeng, and concept pages for MLA, GRPO, Mixture of Experts, Open-weight models, and the "Sputnik Moment" in AI.

## [2026-04-28] ingest | The Next Phase of the Microsoft OpenAI Partnership

Ingested the Microsoft announcement (2026-04-27) regarding the restructuring of their partnership with OpenAI. The relationship has shifted from exclusive to non-exclusive, allowing OpenAI to license models to other cloud providers while Microsoft doubles down on its own "Microsoft AI" division and home-grown models.

- Created raw: `raw/microsoft-openai-partnership-2026.md`
- Created source page: `[[microsoft-openai-partnership-2026]]`
- Created entity page: `[[microsoft]]` (Thai-primary, Bilingual H1)
- Updated entity page: `[[openai]]` (Thai-primary) — added section on the partnership shift and infrastructure diversification.
- Updated `[[index]]` and this log

## [2026-04-28] ingest | วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง Ep. 3 — Nattee Niparnan

Ingested Episode 3 of Nattee Niparnan's series. Key takeaways include using AI to close personal weaknesses (testing, UI/UX), the observation that the generalist ("เป็ด") moat is shrinking, and the introduction of the "Eh Gland" (ต่อมเอ๊ะ) as a core judgment requirement.

- Created raw: `raw/LLM Era Computer Engineering Ep 3 - Nattee Niparnan.md`
- Created source page: `[[llm-era-computer-engineering-ep3-nattee]]`
- Created Thai-primary concept pages: `[[eh-gland]]`, `[[horror-vacui]]`
- Updated entity page: `[[nattee-niparnan]]` — added Ep 3 details and "Eh Gland" coinage.
- Updated concept pages: `[[taste-paradox]]` (linked Eh Gland), `[[engineering-role-shift]]` (added Shrinking Generalist Moat section).
- Updated `[[index]]` and this log

## [2026-04-28] ingest | Ryan Lopopolo Harness Engineering
Ingested Ryan Lopopolo's talk on Harness Engineering.
- Created source summary: [[ryan-lopopolo-harness-engineering]]
- Created entity: [[ryan-lopopolo]]
- Updated entity: [[openai]]
- Updated concept: [[harness-engineering]]
- Created concepts: [[code-is-free]], [[token-billionaire]], [[just-in-time-context]]

## [2026-04-28] ingest | Maggie Appleton Collaborative AI Engineering
Ingested Maggie Appleton's talk on Collaborative AI Engineering. Explored the shift from individual agent productivity to team-based alignment. Introduced the concept of the "Alignment Bottleneck" and the ACE (Agent Collaboration Environment) prototype.
- Created source `maggie-appleton-collaborative-ai-engineering`
- Created entities `maggie-appleton`, `github-next`, `ace`
- Created concepts `collaborative-ai-engineering`, `alignment-bottleneck`, `vibecoded-slop`, `team-pulse`
- Updated entity `github`

## [2026-04-28] ingest | Peter Gostev What Models Still Suck At
Ingested Peter Gostev's talk on model failure modes and Arena.ai data. Explored the "BullshitBench" for nonsense detection and the concept of "Reasoning Regression" where thinking models over-justify false premises.
- Created source `peter-gostev-what-models-suck-at`
- Created entities `peter-gostev`, `arena-ai`
- Created concepts `bullshitbench`, `dissatisfaction-rate`, `reasoning-regression`

## [2026-04-28] ingest | Mario Zechner I Hated Every Coding Agent, So I Built My Own
Ingested Mario Zechner's talk on the **pi** coding agent. Explored the critique of "spaceship" agents, the power of minimalism, and the need for malleable tools. Introduced tree-structured sessions and the defense against "clanker slop" in Open Source.
- Created source `mario-zechner-pi-agent`
- Created entities `mario-zechner`, `pi-agent`, `terminus-agent`, `vouch-oss`
- Created concepts `malleable-tools`, `tree-structured-sessions`, `terminalbench`, `clanker-slop`
- Updated entity `claude-code` and concept `vibecoded-slop`

## [2026-04-28] ingest | ทำไม AI ช่วยให้เขียนโค้ดเร็วขึ้น 10 เท่า แต่โปรเจกต์ยังเสร็จช้าเท่าเดิม?
Ingested article by Jeeraphan Lairat (Senestia) on the local optimization trap of AI coding speed. Created source summary `jeeraphan-lairat-ai-coding-speed`, entities `jeeraphan-lairat`, `senestia`, and concepts `theory-of-constraints`, `local-optimization-trap`, `lead-time`, `shift-left-testing`, and `limit-wip`. Updated `alignment-bottleneck` to link back to TOC and Lead Time.

## [2026-04-28] ingest | Chase AI — Claude Code + Impeccable = Design CHEAT CODE

สรุปวิดีโอจาก [[chase-ai|Chase AI]] เกี่ยวกับการใช้งาน [[impeccable|Impeccable]] ซึ่งเป็น design skill สำหรับ [[claude-code|Claude Code]] เพื่อแก้ปัญหา "AI Slop" ในงาน frontend โดยเน้นการใช้ภาษาและมาตรฐานการออกแบบระดับมืออาชีพ และการใช้โหมด Live Editing ผ่าน browser

- สร้างหน้า raw: `raw/Claude Code + Impeccable = Design CHEAT CODE.md`
- สร้างหน้า source: `[[chase-ai-claude-code-impeccable]]`
- สร้างหน้า entity: `[[chase-ai]]`, `[[impeccable]]`
- สร้างหน้า concept: `[[ai-slop]]` (Thai-primary) — รวบรวมนิยามของ Slop ในแง่ Design, Code และ Vibes
- อัปเดตหน้า entity: `[[claude-code]]` — เพิ่มหมวด Ecosystem & Extensions และข้อมูลของ Impeccable
- อัปเดต `[[index]]` และ log นี้

ประเด็นสำคัญ: (1) AI มักสร้างงานที่ไม่มีรสนิยมเพราะผู้ใช้ไม่ใช้ศัพท์เทคนิคของ designer (Nomenclature); (2) Impeccable เพิ่มเสาหลักการออกแบบ 7 ประการให้ Claude Code; (3) Impeccable Live ช่วยให้การแก้ UI แบบ micro-adjustments ทำได้ง่ายผ่าน Graphic Interface; (4) การทำ Design Audit เพื่อหาจุดที่เป็น anti-patterns และ AI slop

## [2026-04-28] ingest | Why Karpathy’s Second Brain Breaks at Agent Scale
Ingested technical critique by @Ctrl_Alt_Zaid on agent memory architecture. Created source summary, entity pages for @Ctrl_Alt_Zaid and Mercury, and several concept pages related to machine-efficient memory (Selective Injection, Memory Drift, Scoring, Decay, Hybrid Architecture). Updated Andrej Karpathy entity with the critique.
## [2026-04-29] ingest | Compound Engineering v3.3.0
Ingested release notes for [[compound-engineering]] v3.3.0. Created source summary, entities for [[trevin]] and [[every-inc]], and new concept pages for [[playback-pattern]], [[grounding]], and [[cheaper-to-correct]]. Updated [[judgement-vs-automation]] to include agent operational judgment and reduced ceremony.
## [2026-04-29] ingest | The Harness Is the Backend
Ingested [[the-harness-is-the-backend]] by [[mf-piccolo]]. Introduced the [[iii-triple-i]] framework and the [[wtf-primitives]] (Worker-Trigger-Function) architectural pattern. Updated [[harness-engineering]] to reflect the shift from extrinsic harness scaffolding to integrated backend primitives.

## [2026-04-30] ingest | thClaws Marketplace / มาร์เก็ตเพลสสำหรับ thClaws
Ingested Facebook post by [[panutat-tejasen|Panutat Tejasen]] regarding thClaws v0.7.0.
- Created source summary: `[[thclaws-marketplace-panutat]]`
- Updated entity pages: `[[panutat-tejasen]]`, `[[thclaws]]`
- Created concept pages: `[[rabbit-hole]]`, `[[host-bridge]]`
- Updated `[[wiki/index.md]]`

## [2026-05-03] ingest | Building pi in a World of Slop — Mario Zechner

Ingested Mario Zechner's AI Engineer talk connecting pi's design to a broader critique of agent-generated slop.
- Created source summary: `[[building-pi-world-of-slop]]`
- Updated entities: `[[mario-zechner]]`, `[[pi-agent]]`
- Updated concepts: `[[malleable-tools]]`, `[[clanker-slop]]`, `[[vibecoded-slop]]`, `[[coding-harness]]`
- Updated `[[wiki/index.md]]`

## [2026-05-04] ingest | Matt Pocock - 4 AI Terms Defined
Ingested Matt Pocock's concise structural definitions of **Model**, **Harness**, **Environment**, and **Agent**. Key takeaway: an Agent is a combination of a Model, a Harness (prompt/tools/state), and an Environment (file system/MCP). This clarifies how the same model results in different agents (e.g., Claude Code vs. Claude Web). 
- Created source summary: `[[matt-pocock-4-ai-terms]]`
- Created entity: `[[claude-web]]`
- Updated entity: `[[matt-pocock]]`
- Updated concept: `[[coding-harness]]`
- Updated `[[wiki/index.md]]`

## [2026-05-04] ingest | AI Language Crisis Phenomenon
Ingested an article from Thairath Plus about "Text Slop" and the "AI Language Crisis." Highlights the cliché "Not just... but..." formula and the threat to human language depth if models keep training on averaged, synthetic output.
- Created source summary: `[[ai-language-crisis-phenomenon]]`
- Updated concept: `[[ai-slop]]`, `[[stop-slop-concept]]`
- Updated `[[wiki/index.md]]`

## [2026-05-04] ingest | This Anthropic Engineer Uses Claude Code Differently Than Everyone Else
Ingested a video presentation by Anthropic engineer Cal Rueb about Claude Code best practices.
- Created source summary: `[[anthropic-engineer-claude-code]]`
- Created entity: `[[cal-rueb]]`
- Created concept: `[[agentic-search]]`
- Updated entity: `[[claude-code]]`
- Updated concept: `[[claude-md]]`
- Updated `[[wiki/index.md]]`

## [2026-05-05] ingest | Agentic Coding is a Trap
Ingested Lars Faye's article "Agentic Coding is a Trap". The article warns against over-reliance on coding agents, highlighting the risks of cognitive debt and skill atrophy.
- Created source summary: `[[agentic-coding-trap]]`
- Created entities: `[[lars-faye]]`, `[[simon-willison]]`, `[[dax]]`
- Created concepts: `[[cognitive-debt]]`, `[[skill-atrophy]]`, `[[vendor-lock-in]]`
- Updated `[[index]]`, `[[log]]`, and `hotcache.md`

## [2026-05-07] ingest | Accelerating Gemma 4: Multi-Token Prediction Drafters
Ingested Google blog post by Olivier Lacombe and Maarten Grootendorst announcing MTP drafters for Gemma 4. Up to 3x lossless inference speedup via speculative decoding; drafter shares activations and KV cache with the target. Reported ~2.2x on Apple Silicon (batch 4–8) and similar gains on A100; supports Transformers, MLX, vLLM, SGLang, Ollama, LiteRT-LM.
- Created source summary: `[[multi-token-prediction-gemma-4]]`
- Created entity: `[[gemma]]`
- Created concepts: `[[speculative-decoding]]`, `[[multi-token-prediction]]`
- Updated `[[index]]`, `[[log]]`, and `hotcache.md`

## [2026-05-08] ingest | Why I’m Against Claude Code’s Grep-only Retrieval
Ingested Milvus blog post critiquing Claude Code's reliance on Agentic Search (grep). Proposes Vector Search and Semantic Retrieval as a more token-efficient alternative (40%+ reduction). Highlights AST-based chunking and Merkle Tree-based sync for performance.
- Created source summary: `[[why-im-against-claude-codes-grep-only-retrieval]]`
- Created entities: `[[milvus]]`, `[[zilliz]]`, `[[claude-context]]`
- Created concepts: `[[semantic-retrieval]]`, `[[ast-based-chunking]]`, `[[merkle-tree-sync]]`
- Updated concepts: `[[agentic-search]]`
- Updated entities: `[[claude-code]]`
- Updated `[[index]]`, `[[log]]`, and `hotcache.md`

## [2026-05-09] ingest | Granite 4.1 - The Fastest ASR?
Ingested Sam Witteveen's video on IBM Granite Speech 4.1 and its three 2B ASR variants: base, Plus, and NAR.
- Created source summary: `[[granite-4-1-fastest-asr]]`
- Created entities: `[[ibm]]`, `[[granite-speech]]`, `[[sam-witteveen]]`
- Created concepts: `[[automatic-speech-recognition]]`, `[[non-autoregressive-asr]]`, `[[keyword-biasing]]`, `[[speaker-attributed-asr]]`, `[[word-error-rate]]`
- Updated `[[index]]`, `[[log]]`, and `hotcache.md`

Key takeaway: Granite Speech 4.1 is best understood as a choice of ASR bottleneck: base for low WER and keyword biasing, Plus for structured transcripts with speaker labels/timestamps, and NAR for extremely high-throughput raw transcription.

## [2026-05-10] ingest | Agent Harness Engineering
Ingested Addy Osmani's X post synthesizing the broader "Agent = Model + Harness" framing for coding agents.
- Created source summary: `[[agent-harness-engineering]]`
- Created concept: `[[harness-ratchet]]`
- Created entities: `[[addy-osmani]]`, `[[vtrivedy]]`, `[[fred-schott]]`, `[[flue]]`
- Updated concepts: `[[coding-harness]]`, `[[harness-engineering]]`, `[[progressive-disclosure]]`, `[[context-rot]]`, `[[just-in-time-context]]`
- Updated entities: `[[humanlayer]]`, `[[google-cloud]]`, `[[claude-code]]`
- Updated `[[index]]`, `[[log]]`, and `hotcache.md`

Key takeaway: harness engineering is now broader than a review-agent pipeline. It is the discipline of shaping the full runtime around a model — prompts, tools, filesystem, sandbox, hooks, memory, context policy, subagents, observability, and recovery paths. The reusable pattern is the Harness Ratchet: every real agent failure should become a durable rule, hook, lint/test gate, or reviewer behavior.

## [2026-05-12] ingest | New Skills! /handoff, /prototype, /review and /writing-* | Skills Changelog
Ingested Matt Pocock's skills changelog covering new `/handoff` and `/prototype` skills plus in-progress `/review` and `writing-*` workflows.
- Created source summary: `[[new-skills-handoff-prototype-review-writing]]`
- Created concepts: `[[agent-handoff-documents]]`, `[[throwaway-prototyping]]`, `[[dual-axis-code-review]]`, `[[writing-fragments]]`
- Updated entity: `[[matt-pocock]]`
- Updated concepts: `[[context-rot]]`, `[[subagent-patterns]]`, `[[ai-orchestrator]]`, `[[grill-me]]`
- Updated `[[index]]`, `[[log]]`, and `hotcache.md`

Key takeaway: Pocock's new skills treat agent work as phase routing. Use handoff when context should move to a fresh session, prototype when unknowns need an artifact, review as two separate axes (standards/spec), and writing-* as a fragment-first workflow that keeps human voice as the raw material.
