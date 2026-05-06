# Hotcache

Last updated: 2026-05-05 (Agentic Coding is a Trap ingest)

## Wiki state

- **72 sources ingested**, **119 concept pages**, **96 entity pages**, **0 analysis pages** (all indexed)
- **All concept and entity pages are now Thai-primary.** Source summaries remain in English, except for Thai-source summaries which are in Thai.
- Topics: **Cognitive Debt**, **Skill Atrophy**, **Vendor Lock-In**, **Care Allocation**, **Agentic Engineering**, **Software 3.0**, **Jagged Intelligence**, **Vibe Coding**, **Verifiability**, **Agent-Native Infrastructure**, **The Harness is the Backend**, **WTF Primitives**, **iii (Triple I)**, **thClaws Marketplace**, **Rabbit Hole**, **Host Bridge**, **Enterprise AI Security**, **Agent Dashboards**, **Playback Pattern**, **Grounding**, **Cheaper to Correct**, **Mercury Agent Memory**, **Memory Drift**, **Selective Injection**, **Memory Scoring**, **Memory Decay**, **Hybrid Memory Architecture**, UI/UX design styles, **Impeccable**, **AI Slop**, **Text Slop**, **Theory of Constraints**, **Local Optimization Trap**, **Lead Time**, **Malleable Tools**, **Tree-structured Sessions**, **TerminalBench**, **Hidden Context**, **Clanker Slop**, **Vibecoded Slop**, **Coding Harness**, **Alignment Bottleneck**, **ACE**, **BullshitBench**, **Reasoning Regression**, **Harness Engineering**, **Code is Free**, **Token Billionaire**, **Just-in-Time Context**, **Eh Gland**, **Horror Vacui**, **Advisor Strategy**, **Claude Code Session Management**, **Holographic UI**, **Soviet Cosmism**, **Cassette Futurism**, **AI + 3D Workflow**, **Agentic Search**.

## Recent activity

- Ingested **Agentic Coding is a Trap** (2026-05-05). Lars Faye warns against the "Spec Driven Development" trend, arguing that delegating implementation to agents causes **Skill Atrophy** and **Cognitive Debt**. Advocates for the human staying engaged with coding to avoid **Vendor Lock-In** on reasoning abilities.
- Ingested **This Anthropic Engineer Uses Claude Code Differently Than Everyone Else** (2026-05-04). Cal Rueb (Anthropic) details Claude Code best practices. Key concepts: **Agentic Search** (vs RAG indexing), managing **CLAUDE.md** as agent memory, double-escape for rewind, and auto mode workflows.
- Ingested **AI Language Crisis Phenomenon** (2026-05-04). Thairath Plus article highlighting the cliché "Not just... but..." formula (Text Slop) and the threat to human language depth if models keep training on averaged, synthetic output.
- Ingested **Matt Pocock - 4 AI Terms Defined** (2026-05-04). Concise structural definitions: **Model** (stateless blob), **Harness** (tools/prompt/context), **Environment** (file system/MCP), and **Agent** (Model + Harness + Environment). Explains why the same model can be different agents (Claude Code vs. Claude Web).
- Ingested **Building pi in a World of Slop — Mario Zechner** (2026-05-03). AI Engineer talk tying [[pi-agent]] to a broader warning about agent-generated slop. Key points: harnesses can silently take ownership of context, pi favors a tiny self-modifying extension core, clanker PR/issue spam drains OSS maintainer attention, and critical agent-written code still has to be read line by line by humans.
- Ingested **JRT Investment — I Don't Give a Fuck Skill** (2026-05-02). Thai Facebook post reframing "I don't give a fuck" as **Care Allocation**: attention/care is a scarce resource, so the skill is choosing what deserves it. Key points: ignore low-value internet judgment, care about work and meaningful people, reduce mental load, lower the perceived cost of failure, and decide faster.
- Ingested **thClaws Marketplace / มาร์เก็ตเพลสสำหรับ thClaws** (2026-04-30). Panutat Tejasen announces thClaws v0.7.0 with a Marketplace for Skills, MCP, and Plugins. Key highlights: **Enterprise Security** via Private Marketplaces, the **Host Bridge** concept for **Agent Dashboards** (inspired by Claude Cowork), and the **Rabbit Hole** phenomenon in complex coding tasks.
- Ingested **Andrej Karpathy: From Vibe Coding to Agentic Engineering** (2026-04-30). Karpathy explores the transition from **Vibe Coding** (raising the floor) to **Agentic Engineering** (raising the ceiling/discipline). He introduces **Software 3.0** (programming by prompting/context window), **Jagged Intelligence** (AI peaks in verifiable tasks but valleys in common sense), and the need for **Agent-Native Infrastructure** (docs/APIs designed for agents).
- Ingested **The Harness Is the Backend** (2026-04-29). @mfpiccolo introduces the **iii (Triple I)** framework and the **WTF Primitives** (Worker-Trigger-Function). Argues that agent infrastructure (harness) should not be extrinsic but should use the same primitives as traditional backends. Key features: **Agent as a Worker**, **Live Discovery/Extensibility**, and **Unified Observability**.
- Ingested **Compound Engineering - 4/28/2026** (2026-04-29). Trevin (Every Inc.) announces v3.3.0 of the **Compound Engineering** skill suite. Focuses on making agents **Cheaper to Correct** through the **Playback Pattern** (Stated, Inferred, Out-of-scope) and preventing hallucination via **Grounding** ideas in code evidence. Also addresses reducing "ceremony" by automating obvious agent fixes.
- Ingested **Why Karpathy’s Second Brain Breaks at Agent Scale. How Mercury Solves It.** (2026-04-28). @Ctrl_Alt_Zaid analyzes why human-centric wikis fail for autonomous agents. Proposes **Hybrid Memory Architecture** (Markdown for humans, Structured substrate for agents) and introduces the **Mercury** project. Key concepts: **Memory Drift**, **Selective Injection**, **Memory Scoring**, and **Memory Decay**.
- Ingested **ทำไม AI ช่วยให้เขียนโค้ดเร็วขึ้น 10 เท่า แต่โปรเจกต์ยังเสร็จช้าเท่าเดิม?** (2026-04-28). Jeeraphan Lairat (Senestia) explores why AI coding speed doesn't translate to faster delivery if bottlenecks (waiting for reviews/tests) aren't addressed. Key concepts: **Theory of Constraints**, **Local Optimization Trap**, **Lead Time**, **Shift-Left Testing**, and **Limit WIP**.

## Directory layout

```
raw/                    # Immutable source documents
wiki/
  index.md              # Page catalog by type
  log.md                # Chronological operation log
  sources/              # One summary per ingested source (72 files)
  entities/             # People, orgs, products (96 files)
  concepts/             # Ideas, frameworks, themes (119 files)
  analysis/             # Saved query results (0 pages)
CLAUDE.md               # Schema and workflows
hotcache.md             # This file — read first each session
```