---
title: Claude Code
type: entity
tags: [ai, claude, tools, agents, cli, coding]
created: 2026-04-16
updated: 2026-07-04
sources: [Introducing Claude Opus 4.7.md, Using Claude Code Session Management & 1M Context.md, forrestchang andrej-karpathy-skills.md, alex-ker-harnesses-optimize.md, Create custom subagents - Claude Code Docs.md, opencode-vs-claude-code-morph.md, Remote Control - Claude Code Docs.md, cyril-xbt-claude-md-guide.md, This Anthropic Engineer Uses Claude Code Differently Than Everyone Else.md, why-im-against-claude-codes-grep-only-retrieval.md, Agent Harness Engineering.md, thariq-html-effectiveness.md, improved-15-llms-harness-changed.md, How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md, "รู้จักกับ Loop Engineering — mikelopster transcript", zoran-horvat-claude-no-planning-engine.md, planning-mode-dangerous-illusion.md, how-ai-became-more-expensive-than-workers-it-replaced.md, code-isnt-free-mario-zechner-hard-truths-coding-ai.md]
---

# Claude Code

Coding agent แบบ terminal-based จาก [[anthropic|Anthropic]] — เป็น CLI ที่ขับเคลื่อน [[claude|Claude]] ให้ทำงานด้านวิศวกรรมซอฟต์แวร์ต่างๆ โดยสามารถเข้าถึง shell, แก้ไขไฟล์, และใช้เครื่องมือได้ นอกจากนี้ยังมีในรูปแบบ desktop app (Mac/Windows), web (claude.ai/code), และ IDE extensions (VS Code, JetBrains)

ในกรอบของ [[agent-harness-engineering]] Claude Code เป็นตัวอย่างชัดของ [[coding-harness|coding harness]]: model ข้างในอาจเป็น Claude รุ่นเดียวกันกับ surface อื่น แต่พฤติกรรมต่างออกไปเพราะ CLI มี filesystem, bash, permissions, hooks, MCP, subagents, skills, memory, และ context management เป็นของตัวเอง

[[mario-zechner|Mario Zechner]] ให้ caveat จากมุมผู้ใช้ power user ใน [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]]: Claude Code เก่งและคนใช้ได้จริง แต่ release cadence ที่ถี่มากทำให้ system prompt, tool definitions, และ hidden reminders เปลี่ยนได้เรื่อย ๆ. สำหรับ workflow ที่พึ่ง prompt template, slash command, หรือ skill เฉพาะตัว ความเปลี่ยนแปลงใต้ harness อาจทำให้ behavior พังโดยผู้ใช้ไม่เห็นสาเหตุ. นี่เป็นเหตุผลหนึ่งที่เขาสร้าง [[pi-agent|pi]] เป็นเครื่องมือที่เล็กและคุมได้มากกว่า.

## Edit tool และ subagent I/O

Claude Code ใช้ **`str_replace`** เป็นหลัก — model ต้องหา old string ตรงทุกตัวอักษร (รวม whitespace ด้วย) แล้วแทน; ถ้าเจอหลาย match หรือไม่เจอเลยก็ reject (error "String to replace not found" ดังจนมีคนตั้ง megathread กันใน community) ใน benchmark ของ [[can-boluk|Can Bölük]] แนว Replace มักดีกว่า OpenAI-style **patch** แต่ยังสู้ [[hashline|Hashline]] ไม่ได้กับหลาย model — ดู [[edit-tool-formats]]

[[can-boluk]] ยังชี้อีกว่า Claude Code **leak raw JSONL จาก sub-agent output** กลับเข้า parent context กิน token เป็นหลักแสน — เป็นตัวอย่างชัดว่า subagent output format ที่ harness คุมเองได้สำคัญแค่ไหน

## กลยุทธ์การค้นหาข้อมูล (Retrieval Strategy)

Claude Code ขึ้นชื่อเรื่องการใช้ [[agentic-search]] หรือ "Grep-only Retrieval" ซึ่งเป็นการให้ Agent ใช้เครื่องมือ terminal ดั้งเดิม (grep, find) ค้นหาโค้ดด้วยตัวเองเหมือนมนุษย์ อย่างไรก็ตาม มีข้อถกเถียงในเชิงประสิทธิภาพ:

- **ข้อดี:** ยืดหยุ่น ไม่ต้องทำ indexing ล่วงหน้า เหมาะกับโปรเจกต์ขนาดเล็กถึงกลาง
- **ข้อเสีย:** เมื่อใช้กับ codebase ขนาดใหญ่ จะเกิดปัญหา "Token Bloat" (ดึงโค้ดที่ไม่เกี่ยวข้องมาเยอะ) และ "Time Tax" (เสียเวลาค้นหาซ้ำซ้อน)
- **ทางเลือก:** มีเครื่องมือเสริมอย่าง [[claude-context]] ที่นำ [[semantic-retrieval]] (Vector RAG) ผ่าน [[milvus]] มาช่วยเพิ่มความแม่นยำและลดการใช้ token ได้กว่า 40%

## สถาปัตยกรรมของ Session
...

ดูโมเดลเต็มๆ ได้ที่ [[claude-code-session-management]] ในแต่ละ turn ผู้ใช้สามารถเลือกได้ 5 อย่าง:

1.  **Continue** — ส่งข้อความต่อไป
2.  **`/rewind`** (esc esc) — ย้อนกลับไปยังข้อความก่อนหน้า และลบทุกอย่างหลังจากนั้นทิ้ง
3.  **`/clear`** — เริ่มใหม่ทั้งหมด; ผู้ใช้เขียน brief ใหม่
4.  **`/compact`** — ให้ AI สรุปประวัติการสนทนา; ดูที่ [[compaction]]
5.  **Subagent** — มอบหมายงานให้ agent ตัวใหม่ที่มี context สด; จะส่งคืนเฉพาะผลลัพธ์กลับมา

เหตุผลที่มีตัวเลือกเหล่านี้คือเพื่อจัดการกับ [[context-rot]] — คุณภาพของโมเดลจะลดลงเมื่อ context window เต็ม ถึงแม้ context 1M token ของ Claude Code จะใช้งานได้ แต่จุดที่ทำงานได้ดีที่สุด (sweet spot) นั้นต่ำกว่า 1M มาก

## ฟีเจอร์และคำสั่งต่างๆ

- **Slash commands** — คำสั่งที่มากับโปรแกรม (`/compact`, `/clear`, `/rewind`, `/ultrareview`, `/help`) และที่ผู้ใช้สร้างขึ้นเอง
- **Plan mode** — ในมุมของ [[zoran-horvat|Zoran Horvat]] เป็น [[plan-mode-as-prompting|prompt scaffold]] มากกว่า planning engine จริง: harness กันไม่ให้แก้ไฟล์ แล้วให้ model เขียน steps ก่อน implement. วิดีโอ [[planning-mode-dangerous-illusion]] ใช้ directory-upload demo ให้เห็นว่า Sonnet 4.6 พลาด client-side filtering/path bug ส่วน Opus 4.7 ดีขึ้นแต่ยังไม่ถามเรื่อง user data และ duplicated ignore list. ใช้เป็น draft ได้ แต่ต้องให้คนตรวจ judgement ที่กระทบ data, architecture, และ product semantics
- **`/ultrareview`** — session สำหรับ review code โดยเฉพาะ เพื่อหา bug และปัญหาด้าน design (เปิดตัวพร้อม [[claude-opus-4-7|Opus 4.7]]; ให้ใช้ฟรี 3 ครั้งสำหรับ Pro/Max)
- **Subagents** — สร้างขึ้นผ่าน Agent tool; มี context window ใหม่สำหรับแต่ละ agent สร้างโดยใช้ไฟล์ Markdown ที่มี YAML frontmatter ใน `.claude/agents/` (ของโปรเจกต์), `~/.claude/agents/` (ของผู้ใช้), หรือจาก plugin ชุดที่มาพร้อมโปรแกรม: **Explore** (ใช้ Haiku, อ่านอย่างเดียว), **Plan** (อ่านอย่างเดียว, ใช้ใน plan mode), **general-purpose** (ใช้ได้ทุก tool), และ agent ช่วยเหลืออื่นๆ เช่น **statusline-setup** และ **Claude Code Guide** สามารถตั้งค่าแต่ละ agent ได้: `tools` / `disallowedTools`, `model`, `permissionMode`, `skills` (จะถูก inject ตอนเริ่ม), `mcpServers` (จำกัดขอบเขตใน subagent), `memory: user|project|local` สำหรับ directory `MEMORY.md` แบบถาวร, `background: true`, `isolation: worktree`, lifecycle `hooks` เรียกใช้งานผ่าน natural language, mention `@agent-<name>`, หรือ `claude --agent <name>` เพื่อรันทั้ง session ด้วย system prompt นั้น Subagent ไม่สามารถสร้าง subagent ซ้อนได้ ดูเพิ่มเติมที่ [[claude-code-subagents-docs]] และ [[subagent-patterns]]
- **Skills** — แพ็กเกจของ prompt/instructions (เช่น [[llm-coding-pitfalls|karpathy-guidelines]] ของ [[forrestchang]])
- **Hooks** — คำสั่ง shell ที่จะทำงานเมื่อมี event ของ harness เกิดขึ้น (ตั้งค่าใน `settings.json`)
- **[[auto-mode|Auto mode]]** — permission mode แบบกลางๆ: มี classifier คอยตรวจสอบทุก tool call และอนุมัติอันที่ปลอดภัยโดยอัตโนมัติ, บล็อกอันที่เสี่ยง (เช่น ลบไฟล์จำนวนมาก, ขโมยข้อมูล, รันคำสั่งอันตราย), ชี้นำ Claude ใหม่, และจะถามผู้ใช้ก็ต่อเมื่อ Claude ยืนยันจะทำสิ่งที่ถูกบล็อก เปิดตัว 24 มี.ค. 2026 (research preview สำหรับ Team plan, Sonnet/Opus 4.6); ขยายให้ผู้ใช้ Max ตอน [[claude-opus-4-7|Opus 4.7]] ออก Admin สามารถปิดได้ผ่าน `"disableAutoMode": "disable"` ใน managed settings CLI: `claude --enable-auto-mode` แล้วกด **Shift+Tab** ที่มา: [[claude-code-auto-mode]]
- **MCP servers** — เชื่อมต่อกับเครื่องมือภายนอกผ่าน [[model-context-protocol]]; Claude Code มาพร้อม MCP tool-search index ในตัว ทำให้ตอนเริ่ม session จะโหลดแค่ชื่อ tool และ schema จะถูกโหลดเมื่อต้องการใช้งาน (Anthropic รายงานว่าลด context ได้ ~85% เมื่อเทียบกับ harness อื่นที่โหลด definition ของทุก MCP tool ตั้งแต่แรก) ดูที่ [[progressive-disclosure]]
- **[[claude-md|CLAUDE.md]]** — ไฟล์ Markdown ในระดับโปรเจกต์ที่จะถูกโหลดอัตโนมัติเมื่อเริ่ม session เพื่อใช้เป็น system prompt แบบถาวร มี 3 ชั้น: project root (`<repo>/CLAUDE.md`), monorepo subdir (`<repo>/<sub>/CLAUDE.md`), และ global (`~/.claude/CLAUDE.md`) สำหรับ preference ที่ใช้กับทุกโปรเจกต์ มี template 7 ส่วนที่เป็นที่ยอมรับจาก [[cyril-xbt|@cyrilXBT]]: Project Overview / Tech Stack / Coding Conventions / Never Do This / File Structure / Current Sprint Goals / Important Context ซึ่งอยู่ภายใต้ [[instruction-budget]] — ควรทำให้กระชับ และย้ายกฎที่มีรายละเอียดเยอะไปไว้ใน skills ผ่าน [[progressive-disclosure]]
- **Fast mode** — `/fast` เพื่อสลับไปใช้ variant ที่ให้ผลลัพธ์เร็วกว่า (มีใน Opus 4.6)
- **Remote Control** — ควบคุม session CC *บนเครื่อง local* จาก `claude.ai/code` หรือแอป Claude บนมือถือ Session จะอยู่บนเครื่องของคุณ (filesystem, MCP, `@` autocomplete ยังใช้ได้จากระยะไกล); Anthropic จะ relay ข้อความผ่าน outbound HTTPS เท่านั้น — ไม่ต้องเปิด inbound port มี 3 โหมดใน CLI: `claude remote-control` (server mode, รองรับ `--spawn worktree|same-dir|session`, default capacity 32), `claude --remote-control` (`--rc`, interactive), `/remote-control` (`/rc`, จาก session ที่มีอยู่) ใน VS Code: `/remote-control` (v2.1.79+) เปิดตลอด: `/config` → **Enable Remote Control for all sessions** Push notification บนมือถือผ่าน `/config` → **Push when Claude decides** (v2.1.110+) ต้องใช้ v2.1.51+ และ claude.ai OAuth (ใช้กับ API keys / Bedrock / Vertex / Foundry ไม่ได้) Ultraplan จะตัดการเชื่อมต่อ RC ดูที่ [[claude-code-remote-surfaces]] และ [[claude-code-remote-control-docs]]

## Loop / Goal / Scheduled work

[[mikelopster]] เล่าใน [[mikelopster-loop-engineering|คลิป Loop Engineering]] ว่า Claude Code เป็น surface ที่เขาลองสร้าง loop ได้ตรงที่สุด. `/loop` ใช้เมื่อ cadence ชัด เช่น เช็ค deploy / CI / PR เป็นระยะ. `/goal` ใช้เมื่อยังไม่แน่ใจว่าเป้าหมายควรถูกแตกเป็น loop หรือ subtask แบบไหน ให้ agent วิเคราะห์ก่อนแล้วสร้างขั้นตอนและตัว verify ตามมา.

ข้อควรจำจากมุมนี้คือคำสั่งไม่ใช่แก่น. งานที่ใช้ Claude Code ทำ loop ควรมี **feedback gate** ชัด เช่น test, lint, coverage, CI, หรือ PR status. ถ้าเกณฑ์เป็นรสนิยม เช่น "ทำให้สวยขึ้น" หรือ "เขียนให้ดีขึ้น" loop อาจวนยาวและเผา token โดยไม่มี proof ที่ไว้ใจได้. ดู [[loop-engineering]] และ [[orchestration-tax]].

[[zack-proser|Zack Proser]] ใช้ feature ชุดนี้เป็นส่วนหนึ่งของ [[developer-balance|Developer Balance]]: ให้ Claude Code อ่าน Slack/Linear ผ่าน MCP, ปิด verification loop ในระบบจริง, steer session เดิมจากมือถือระหว่างเดิน, แล้ววิเคราะห์ JSONL conversation history เป็นรอบเพื่อหา skill และ hook ที่ขาด ดู [[how-to-keep-shipping-away-from-desk]].

## Remote surfaces (ช่องทางทำงานนอก terminal)

CC มีหลายวิธีในการสั่งงาน agent เมื่อคุณไม่ได้อยู่ที่หน้า terminal ซึ่งทั้งหมดมีอยู่ใน [เอกสาร Remote Control](https://code.claude.com/docs/en/remote-control.md):

| Surface | Claude ทำงานบน | Trigger |
|---|---|---|
| **Remote Control** | เครื่องของคุณ (CLI / VS Code) | มนุษย์ผ่าน claude.ai/code หรือมือถือ |
| **Dispatch** | เครื่องของคุณ (Desktop) | ข้อความจาก Claude mobile |
| **Channels** | เครื่องของคุณ (CLI) | Event จาก Telegram / Discord / custom server |
| **Slack** | Anthropic cloud | `@Claude` mention |
| **Scheduled tasks** | CLI / Desktop / cloud | Cron |
| **Claude Code on the web** | Anthropic cloud | มนุษย์ผ่าน claude.ai/code |
| **Ultraplan** | Anthropic cloud | มนุษย์จาก terminal |

ดู [[claude-code-remote-surfaces]] สำหรับการจัดกรอบสองแกน (local vs cloud × human vs event)

## Effort levels

ตอน [[claude-opus-4-7|Opus 4.7]] ออก, effort เริ่มต้นใน Claude Code ถูกปรับขึ้นเป็น **`xhigh`** สำหรับทุก plan คำแนะนำเริ่มต้นสำหรับงาน coding/agentic คือ `high` หรือ `xhigh` ดูที่ [[effort-levels]]

## Ecosystem & Extensions (ระบบนิเวศและส่วนขยาย)

- **[[impeccable|Impeccable]]** — Open-source design skill ที่ช่วยเพิ่ม "taste" และมาตรฐานการออกแบบให้ Claude Code โดยเฉพาะ ช่วยแก้ปัญหาการสร้าง UI ที่เป็น [[ai-slop|AI Slop]] และมาพร้อมโหมดแก้ไขแบบเห็นผลทันที (Impeccable Live)
- **[[html-artifacts|HTML Artifacts]]** — เทคนิคการใช้ HTML เป็นสื่อกลางในการสื่อสารเพื่อเพิ่มความชัดเจน, information density, sharing, และ two-way interaction (เสนอโดย [[thariq-shihipar|Thariq Shihipar]] จากทีม Claude Code)

## การยอมรับและ Benchmarks (ก.พ. 2026, อ้างอิงจาก Morph / SemiAnalysis)

- ~71K GitHub stars; ~4% ของ public commit ทั้งหมดบน GitHub, ~135K/วัน; คาดการณ์ว่าจะถึง ~20% ภายในสิ้นปี 2026
- VS Code extension: 5.2M installs, 4.0/5 คะแนน
- เมื่อใช้ **WarpGrep v2**: **57.5% บน SWE-bench Pro**, **68.8% บน ARC-AGI-2** — เกือบ 2 เท่าของคะแนนเดิม
- เดโมสร้าง C compiler ขนาด 100K บรรทัด: ใช้ 16 agents, ค่า API ประมาณ ~$20K
- Core system prompt ~2,896 tokens (มี tool description ในตัว 20 ตัว); subagent prompts: Plan 633 / Explore 516 / Task 294 tokens; `/security-review` 2,610 tokens ดูที่ [[opencode-vs-claude-code-morph]] สำหรับที่มา

## Cost governance

ใน [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]] Claude Code ถูกยกเป็นตัวอย่างเครื่องมือ agentic coding ที่ต้นทุนองค์กรเริ่มต้องคุม คลิปอ้างว่า Microsoft ลด/ยกเลิกการใช้ Claude Code ภายในเพราะค่าใช้จ่ายสูง

ประเด็นนี้เข้ากับสิ่งที่หน้านี้มีอยู่แล้ว: Claude Code ทำงานได้ยาว, context ใหญ่, subagent ได้, และมี effort สูง แต่ความสามารถเหล่านี้ทำให้ [[agentic-usage|agentic usage]] มีต้นทุนจริง ต้องมี [[ai-token-economics|token economics]] และ [[enterprise-ai-roi|ROI]] มากำกับ ไม่ใช่ดูแค่ความสามารถของ model

## 1M token context window

ทำให้สามารถทำงาน autonomous ที่ยาวนานได้ (เช่น สร้าง full-stack app ใน session เดียว) แต่ก็ทำให้เกิด [[context-rot]] ที่ประมาณ 300k–400k tokens การจัดการ session จึงเป็นทักษะหลักที่ผู้ใช้ต้องเรียนรู้

## ดูเพิ่ม

- [[cal-rueb]]
- [[agentic-search]]
- [[claude]]
- [[anthropic]]
- [[claude-opus-4-7]]
- [[claude-code-session-management]]
- [[context-rot]]
- [[compaction]]
- [[effort-levels]]
- [[coding-harness]]
- [[progressive-disclosure]]
- [[instruction-budget]]
- [[subagent-patterns]]
- [[auto-mode]]
- [[plan-mode-as-prompting]]
- [[claude-code-remote-surfaces]]
- [[claude-code-remote-control-docs]]
- [[opencode]]
- [[opencode-vs-claude-code-morph]]
- [[pi-agent]] — ทางเลือกแนว Minimalist ที่สร้างขึ้นเพื่อแก้ปัญหา feature bloat ใน Claude Code
- [[agent-harness-engineering]]
- [[harness-ratchet]]
- [[thariq-shihipar]]
- [[edit-tool-formats]]
- [[hashline]]
- [[improved-15-llms-harness-changed]]
- [[developer-balance]]
- [[how-to-keep-shipping-away-from-desk]]
- [[loop-engineering]]
- [[mikelopster-loop-engineering]]
- [[ai-token-economics]]
- [[code-isnt-free-mario-zechner-hard-truths-coding-ai]]
- [[enterprise-ai-roi]]
