---
title: Coding Harness
type: concept
tags: [ai, tools, agents, software-engineering, harness]
created: 2026-04-18
updated: 2026-07-01
sources: [alex-ker-harnesses-optimize.md, building-pi-world-of-slop.md, Agent Harness Engineering.md, software-writing-software-gone-right.md, improved-15-llms-harness-changed.md, "Introducing Omnigent A Meta-Harness to Combine, Control and Share Your Agents.md", "Matt Pocock’s Agentic Engineering Workflow (just copy him).md", "i don't want to use your agent — @RhysSullivan.md", l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# Coding Harness / ตัวครอบของ Coding Agent

**Coding harness** คือชั้นของซอฟต์แวร์ที่อยู่ระหว่างผู้ใช้กับ LLM จริง — เช่น [[claude-code|Claude Code]], [[openai-codex|Codex]], [[opencode|OpenCode]], Cursor, Deep Agent CLI, Roo Code — ซึ่งไม่ใช่ตัว model เอง แต่เป็นสิ่งที่ทำให้ model กลายเป็นเครื่องมือที่ใช้งานได้จริง

[[agent-harness-engineering|Addy Osmani]] สรุปประโยคที่คมที่สุดไว้ว่า **Agent = Model + Harness**. ถ้าคุณไม่ได้แก้ตัว model โดยตรง สิ่งที่คุณออกแบบอยู่ก็คือ harness: prompt, tools, context policy, filesystem, sandbox, hooks, subagent, memory, และ feedback loop

## โครงสร้างพื้นฐาน (The Formula)

[[matt-pocock|Matt Pocock]] (2026-05-04) ให้โครงสร้างที่ชัดเจนในการแยกแยะองค์ประกอบของระบบ AI:

- **Model (ตัวโมเดล)**: เป็นก้อน parameters (stateless blob) ที่ทำหน้าที่เดา token ถัดไปเท่านั้น (เช่น Opus)
- **Harness (ตัวครอบ)**: ทุกสิ่งที่อยู่รอบโมเดลที่ทำให้มันกลายเป็นเอเจนท์ได้ เช่น tools, system prompt, context management
- **Environment (สภาพแวดล้อม)**: โลกภายนอกที่เอเจนท์เข้าไปกระทำ เช่น file system, [[model-context-protocol|MCP]] servers
- **Agent (เอเจนท์)**: ผลลัพธ์จากการนำ **Model** มาใส่ **Harness** แล้วรันใน **Environment**

> **Agent = Model + Harnessed + In an Environment**

มุมมองนี้ช่วยให้เข้าใจว่าทำไมโมเดลตัวเดียวกัน (เช่น Opus) ถึงกลายเป็นเอเจนท์ที่ต่างกันได้ (เช่น Claude Code vs. Claude Web) เพราะพวกมันมี "Harness" ที่ต่างกันนั่นเอง

ในพอดแคสต์ปี 2026-06 (ดู [[matt-pocock-agentic-workflow]]) Pocock ดันมุมนี้ต่อด้วยอุปมา Formula 1: ทุกคนหมกมุ่นกับ "เครื่องยนต์" (model) ทั้งที่เครื่องยนต์เป็นแค่ส่วนเดียวของรถ. ประเด็นคือ **เราคุม harness ได้มากกว่าคุม model** — เขาเสนอให้คิดเป็น **50/50** ไม่ใช่ model 90% + harness 10%. ของจริงข้อหนึ่ง: อยากประหยัด token ให้ทำ codebase ที่แก้ง่าย แล้วใช้ model ถูก ๆ ทำงานเดิมได้ (guardrail ชัด → agent ไม่ต้องเอาหัวโขกกำแพง). มุมนี้ต่อกับ [[bitter-lesson|the bitter lesson]] (อย่าผูกตัวกับ trick ของ model รุ่นเดียว) และ [[agent-experience|AX]] (codebase ที่ดี = ส่วนหนึ่งของ harness ที่ดี)

## นิยามเชิงวิศวกรรม

ในทางเทคนิค, harness คือ `while (have next message) do {tool}` loop — ซึ่งเป็นลูปที่ทำหน้าที่สองอย่างรอบๆ model ที่เป็น stateless อยู่ข้างใน:

1.  **จัดการ context** — sessions, compaction, rewind, การสลับ session
2.  **เชื่อมต่อ tool และ I/O** — tool call, การ parse output, guardrail, permission prompt

ถ้า model คือแหล่งของ intelligence, harness คือสิ่งที่ทำให้ intelligence นั้นใช้งานได้จริง — ลูปที่ราบรื่นจะช่วยเพิ่มความเร็วและคุณภาพของโค้ดที่ได้

[[mario-zechner|Mario Zechner]] เพิ่มมุมที่แข็งกว่านี้ใน [[building-pi-world-of-slop|Building pi in a World of Slop]]: harness ไม่ใช่แค่ UX wrapper แต่เป็นเจ้าของ context โดยพฤตินัย ถ้า harness เปลี่ยน system prompt, tool definitions, reminders, หรือ inject feedback เองโดยผู้ใช้มองไม่เห็น workflow ของผู้ใช้ก็อาจพังได้ แม้ model ตัวเดิมจะยังเก่งเท่าเดิม

## Edit tool boundary (Can Bölük, 2026-02)

[[can-boluk|Can Bölük]] วัด 16 model บน benchmark แก้ bug ในไฟล์ React โดยเปลี่ยนแค่ **รูปแบบ edit tool** — Patch (`apply_patch`), Replace (`str_replace`), [[hashline|Hashline]] — ผลคือ mechanical edit failure ไปบังความสามารถจริงของ model โดยเฉพาะตัวอ่อน (เช่น Grok Code Fast 1 พุ่งจาก 6.7% → 68.3%)

แนว `str_replace` ที่ [[claude-code|Claude Code]] ใช้บังคับให้ model reproduce whitespace เป๊ะ ๆ; แนว patch ของ [[openai-codex|Codex]] ล้มหนักพอเจอ model ที่ไม่คุ้น OpenAI diff dialect ส่วน Cursor แม้จะ fine-tune model แยกมา merge edit เอง ก็ยังยอมรับว่าไฟล์สั้น ๆ rewrite ทั้งไฟล์ยังชนะ diff อยู่

**ได้อะไร:** ก่อนจะด่าว่า "model นี้เขียนโค้ดไม่เป็น" ลองเช็คก่อนว่า harness เปิดทางให้ model **แสดงออก** ได้แล้วหรือยัง — ดู [[edit-tool-formats]] และ [[improved-15-llms-harness-changed]]

## Component taxonomy จาก Agent Harness Engineering

[[addy-osmani|Addy Osmani]] เสนอให้มอง harness จาก behavior ที่ต้องการ ไม่ใช่จากชื่อ feature:

| Behavior | Component |
|---|---|
| durable state | filesystem, Git, worktree |
| general action | bash, code execution |
| safety | sandbox, permission gate, destructive-command hook |
| continual learning | memory files, search, MCP |
| context hygiene | [[compaction]], tool-output offloading, [[progressive-disclosure]] |
| long-horizon execution | loop, planner/executor split, self-verification |
| enforcement | hooks, lint/test/typecheck gate |
| observability | logs, traces, cost, latency meter |

หลักเช็คง่าย ๆ: ถ้าบอกไม่ได้ว่า component หนึ่งมีไว้สร้าง behavior อะไร ก็ควรเอาออก เพราะ component ทุกตัวกิน context, latency, หรือ maintenance cost

## Harness Ratchet

Addy เพิ่มวินัยสำคัญให้คำว่า harness: เมื่อ agent พลาด อย่าแค่ retry ให้แปลงความพลาดนั้นเป็น constraint ถาวรในระบบ ดู [[harness-ratchet]]

ตัวอย่าง: agent เคย comment out test เพื่อให้ผ่านงาน → เพิ่ม rule ใน `AGENTS.md`, เพิ่ม hook ดัก `.skip(`, และให้ reviewer subagent block ก่อน merge

**ได้อะไร:** harness ไม่ใช่ config file ตายตัว แต่เป็น living artifact ที่สะสมประวัติ failure ของทีม

## เส้นแบ่ง deterministic vs ยกให้ agent (Cursor, 2026-06)

[[cursor|Cursor]] เล่าใน [[what-weve-learned-building-cloud-agents|บล็อก cloud agent]] (2026-06-02) ว่าการสร้าง harness คือการตั้งคำถามซ้ำ ๆ ว่า **อะไรควรเป็น deterministic (harness คุม) กับอะไรควรยกให้ agent ตัดสินเอง** — และเส้นแบ่งนี้ขยับเรื่อย ๆ พอ model ฉลาดขึ้น แนวโน้มคือ **ย้าย logic ออกจาก harness ไปเป็น tool ที่ agent คุมเอง**:

- ช่วงแรกไม่ไว้ใจ agent — harness double-check ทุก task, บังคับ commit แล้ว push
- **multi-repo**: จาก hardcode พฤติกรรมไว้ใน harness → แค่บอก repo layout + เปิด tool branch/PR ให้ agent ตัดสินเอง
- **CI Autofix**: จาก harness ดึง log งานที่ fail มาเขียนลง VM → แค่ให้ agent เข้าถึง GitHub CLI แล้วเขียน output ก้อนใหญ่ลงไฟล์ให้มัน search เอง

> "The harness isn't going away so much as what it contains is changing."

harness ไม่หาย แต่เนื้อในเปลี่ยน. ตัวอย่างที่ยังต้องอยู่ใน harness คือ **computer use** — Cursor มี subagent type เฉพาะ มี model routing/prompt/screen recording ของตัวเอง (เพราะ model ยังทำเองล้วน ๆ ไม่ได้) แต่ agent ยังเลือกเองว่าจะเรียกตอนไหน. อีกจุด: cloud agent ต้อง prompt ให้ **autonomous กว่า local** เพราะ cost ของการบล็อกสูง — agent อาจนั่งรอ permission เป็นชั่วโมงโดยไม่มีคนเห็น (ต่อกับ [[orchestration-tax]]). ก้าวถัดไปคือ [[self-healing-environments]].

**ได้อะไร:** harness boundary ไม่ใช่ของตายตัว — ทบทวนเป็นระยะว่า logic ไหนเลื่อนไปให้ agent คุมเองได้แล้ว ทุกครั้งที่ model อัปเกรด

## สองความหมายของคำว่า "harness"

คำว่า "harness" ในวงการ AI coding ปัจจุบันมีการใช้งานสองแบบที่ต้องแยกแยะ:

| นิยาม | ผู้ใช้ | ความหมาย |
|---|---|---|
| **Harness = ตัวครอบ / scaffolding** | Alex Ker, Kyle/[[humanlayer\|HumanLayer]] | เครื่องมือทั้งหมด (Claude Code, Codex ฯลฯ) — ตามที่อธิบายในหน้านี้ |
| **Harness engineering = pipeline ของ review agent** | [[panutat-tejasen\|Panutat Tejasen]] | ลำดับของ agent ที่ทำหน้าที่ตรวจสอบโค้ด / ทดสอบ / audit |

ทั้งสองความหมายไม่ขัดแย้งกัน — pattern ของ Panutat เป็น *เทคนิคย่อย* ที่เกิดขึ้น *ภายใน* harness ตัวใหญ่ ดูที่ [[subagent-patterns]] ในส่วน "pipeline" — Alex Ker กล่าวว่า `UX designer → architect → devil's advocate` เป็นรูปแบบเดียวกับที่ Panutat เสนอ เพียงแค่มองจากมุมของ productivity รายวันแทนที่จะเป็น pedagogy

## harness ของผู้ใช้ vs ของผู้สร้าง (Böckeler, 2026-04)

[[birgitta-bockeler|Birgitta Böckeler]] (engineer ที่ [[thoughtworks|Thoughtworks]]) เพิ่มอีกมุมที่ชัด: ให้แยกคำว่า harness เป็นวงซ้อนกัน — **model** อยู่ในสุด, **builder harness** คือส่วนที่เจ้าของเครื่องมือสร้างมาให้ (system prompt, code retrieval, orchestration ภายใน), และ **user harness** คือชั้นนอกที่ "เรา" ในฐานะผู้ใช้สร้างเองให้เข้ากับ use case ของระบบเรา

มุมที่ต่อยอดคือ user harness ที่ดีควรมองเป็น **ระบบ control** ไม่ใช่กองของ skill กับ MCP ที่ตั้งมั่ว ๆ — ทำจาก **guides (feedforward)** ที่นำทาง agent ก่อนทำงาน + **sensors (feedback)** ที่จับงานหลังทำแล้วป้อนกลับเข้า self-correcting loop ของ agent เอง รายละเอียดเต็มที่ [[harness-guides-sensors]]

**ได้อะไร:** เวลาออกแบบ harness ให้ถามว่า control แต่ละตัวเป็น guide หรือ sensor, เป็น computational (เร็ว/แน่นอน) หรือ inferential (แพง/ตีความ) — แล้ววางให้ถูกจังหวะใน lifecycle

## จุดที่วิจารณญาณของวิศวกรเข้ามามีบทบาท

Alex Ker ชี้ว่ามีสามจุดที่เปลี่ยนผลลัพธ์จาก "slop" เป็นสิ่งที่ใช้งานได้ และทั้งสามจุดยังต้องใช้วิจารณญาณของมนุษย์:

### 1. ทำให้ config เบาและเขียนเอง

`CLAUDE.md` / `AGENTS.md` ควร **เขียนโดยคน ไม่ใช่ให้ LLM generate** — โดยอ้างอิงงานวิจัยของ ETH ที่ระบุว่า system prompt ที่ LLM สร้างขึ้นทำให้ performance แย่ลง *และ* ใช้ inference เพิ่มขึ้น ~20% ทุก token ในไฟล์มีความสำคัญเพราะจะถูก inject เข้าไปในทุก session

วิธีที่แนะนำคือ [[progressive-disclosure]] — บอก agent ว่ามีอะไรบ้าง แต่ยังไม่ load content เข้ามาจนกว่าจะจำเป็นต้องใช้จริงๆ

### 2. ใช้ R.P.I. framework ตอน prompt

**R.P.I. = Research / Plan / Implement** — จาก [[humanlayer|HumanLayer]], prompt แต่ละรอบควรทำเพียงอย่างใดอย่างหนึ่งใน 3 อย่างนี้เท่านั้น:

1.  **Research** — บอกปัญหาให้ agent ไปอ่านโค้ดเอง: structure, prior art, function definition, ความสัมพันธ์ของไฟล์ *โดยยังไม่ต้องแก้ไขอะไร*
2.  **Plan** — ให้ agent เขียนแผนเป็นขั้นตอนออกมา **ซึ่งคนต้องอ่านและตรวจสอบแผนนั้นจริงๆ** Alex Ker ใช้คำว่า "outsourcing thinking or being lazy at this step will cost you dearly later on"
3.  **Implement** — รันแผนใน context window ใหม่ (เรียก main window) หากแผนยาว ให้แยกไปให้ subagent ทำเป็นส่วนๆ

ภาพรวมที่ Alex Ker พูดถึงคือ — ควบคุมให้ harness ทำงานเหมือน staff engineer ที่เก่ง: แตกปัญหาเป็นปัญหาย่อย, วางแผนก่อนลงมือ, และหาคนรีวิวแผนก่อน ซึ่งเป็นการย้าย abstraction จาก "การเขียนโค้ดทีละบรรทัด" มาเป็น "การออกแบบ prompt" แต่วินัยพื้นฐานยังคงเดิม

### 3. ใช้ subagent เพื่อรักษา main context ให้สะอาด

Heuristic ง่ายๆ คือ — **ถ้าต้องการแค่ summary ของงาน ให้ delegate ไปที่ subagent** แต่ถ้าคิดว่าจะต้องย้อนกลับมาถามว่า "เรื่องนี้เกี่ยวข้องกับที่อ่านไปเมื่อกี้อย่างไร" ให้เก็บไว้ใน window หลัก

สอง pattern ที่ Alex Ker แนะนำ (ดูรายละเอียดที่ [[subagent-patterns]]):

-   **Parallel fan-out** — เปิดหลาย subagent พร้อมกัน เหมาะสำหรับ investigation/research
-   **Pipeline** — ต่อ role เป็นลำดับ เหมาะสำหรับงานที่ต้องมองจากหลายมุม

## ข้อสรุปที่ Alex Ker เน้น: commit

เมื่อ harness ทำงานพลาด คนส่วนใหญ่มักจะอยากเปลี่ยน harness — Alex Ker ไม่ได้ห้าม แต่เตือนว่าการเปลี่ยนไปมาตลอดเวลาหมายถึง institutional knowledge ที่อยู่ใน config file และ failure-case log จะหายไป และต้องเริ่มนับหนึ่งใหม่ทุกครั้ง

คำแนะนำคือ — เลือก harness ที่ครอบคลุม use case ส่วนใหญ่ของทีม และเมื่อเจอ failure ให้บันทึก (*พังที่ไหน, ขั้นตอนไหน, เงื่อนไขอะไร*) แล้วนำกลับไปปรับปรุง `.md` file และ prompting strategy ต่อไป

> "The best harness is the harness that you have customized and iterated on with human engineering; it's the one that can handle edge cases which are smoothed out through your team's usage."

## ความสำคัญของเรื่องนี้

-   [[instruction-budget]] และ [[context-rot]] ทำให้การ "ใส่ทุกอย่างเข้าไปใน prompt" ไม่ได้ผลอีกต่อไป — harness คือที่ที่ mitigation ทั้งหมดอยู่ (progressive disclosure, subagent, compaction)
-   [[ai-orchestrator]] — ทักษะ orchestration ปัจจุบันถูกย้ายลงมาเป็นงานระดับ entry-level (ดู [[engineering-role-shift]]) และ harness คือ surface ที่ทักษะนี้แสดงออก
-   [[harness-engineering]] (Panutat) — pipeline review agent pattern เป็นส่วนหนึ่งของ harness ตัวใหญ่นี้
-   [[advisor-strategy]] — เป็นอีกรูปแบบหนึ่งของ agent architecture ที่ harness สามารถออกแบบให้รองรับได้
-   [[malleable-tools]] — Mario เสนอว่า harness ในช่วงลองผิดลองถูกควรเป็น core เล็กที่ขยายได้ ไม่ใช่ feature spaceship ที่ตัดสินใจแทนผู้ใช้
-   [[just-in-time-software]] — TJ DeVries โชว์ harness ขนาดเล็กใน [[luaai-nvim|luai.nvim]]: function missing → generate → cache → improve ภายใน editor
-   [[harness-ratchet]] — วินัยการแปลง failure เป็น rule/hook/test เพื่อไม่ให้ agent พลาดซ้ำคลาสเดิม

## Product agent vs user harness

[[rhys-sullivan|Rhys Sullivan]] เสนออีกด้านใน [[i-dont-want-to-use-your-agent]]: บริษัทจำนวนมากสร้าง in-app agent ของตัวเอง แต่ power user มักมี harness ประจำวันอยู่แล้ว. เขาอยากใช้ model, local files, repo, terminal, และ memory ของตัวเอง แล้วให้ product เปิด expertise ผ่าน [[model-context-protocol|MCP]], API, CLI, docs, และ skills.

นี่คือ [[bring-your-own-agent]]: product ไม่ต้องแทน harness ของผู้ใช้. Product ควรทำให้ harness นั้นเข้าใจ product และทำ action ได้ถูกต้อง. สำหรับ user ทั่วไป in-app chat ยังดีอยู่ แต่สำหรับ power user source of truth ควรเป็น primitive ชุดเดียวกันที่ทั้ง in-app agent และ external agent ใช้ได้.

**ได้อะไร:** harness-first ไม่ได้แปลว่าทุกบริษัทต้องสร้าง harness ใหม่ให้ผู้ใช้. บางครั้งงานที่ถูกต้องคือทำ product ให้ harness อื่นใช้ง่าย.

## ชั้นถัดไป: Meta-Harness

[[omnigent|Omnigent]] จาก [[databricks|Databricks]] ชี้ว่า harness ที่เก่งขึ้นกำลังกลายเป็น silo ใหม่. Claude Code, Codex, Pi และ custom agent ต่างมี session, interface และ policy ของตัวเอง พอ workflow ใช้หลายตัว context กับ control จึงไม่ตามข้ามเครื่องมือ.

[[meta-harness|Meta-harness]] วาง common API, policy, sandbox, cost control และ collaboration ไว้เหนือ harness หลายตัว. มันไม่ได้แทน harness เดิม แต่ทำให้ harness เหล่านั้นกลายเป็นชิ้นส่วนที่สลับและประกอบกันได้.

**ได้อะไร:** ทีมเก็บ workflow และ governance ระดับบนไว้ได้ แม้เปลี่ยน model หรือ harness ด้านล่าง.

## Personal harness stack: Kun Chen

[[kun-chen|Kun Chen]] แสดงใน [[l8-principals-agentic-engineering-workflow-kun-chen|workflow walkthrough]] ว่า user harness หนึ่งชุดอาจไม่ได้อยู่ใน app เดียวเลย แต่เป็นกอง layer ที่ประกอบกัน:

| Layer | ตัวอย่างใน workflow | ทำหน้าที่ |
|---|---|---|
| Terminal surface | [[wezterm\|WezTerm]], [[tmux]], [[neovim\|Neovim]] | คุมหลาย session ด้วย keyboard และ persistent panes |
| Context/onboarding | global memory, project memory, skills | ทำให้ agent รู้ preference และ project convention |
| Tool ergonomics | [[axi\|AXI]] | ลด token/latency และทำ I/O ให้ agent อ่านง่าย |
| Planning surface | [[lavish\|Lavish]] | เปลี่ยน plan เป็น artifact ที่คน feedback ได้ละเอียด |
| Execution isolation | [[treehouse\|Treehouse]] + [[git-worktrees\|worktrees]] | ให้ agent หลายตัวทำงานไม่ชนไฟล์กัน |
| Validation | [[no-mistakes\|No Mistakes]] | แปลง first-pass code เป็น PR พร้อม evidence |
| Meta layer | [[first-mate\|First Mate]] | คุม crew หลายตัวแทนคนสลับ tab เอง |

นี่เป็นตัวอย่างชัดของ harness-first: ความเร็วไม่ได้มาจาก model ตัวเดียว แต่มาจากการออกแบบ surface รอบ model ให้คนและ agent ไม่เสียแรงผิดที่.

## ดูเพิ่มเติม

- [[alex-ker]]
- [[alex-ker-harnesses-optimize]]
- [[humanlayer]]
- [[claude-code]]
- [[openai-codex]]
- [[opencode]]
- [[instruction-budget]]
- [[progressive-disclosure]]
- [[subagent-patterns]]
- [[harness-engineering]]
- [[agent-harness-engineering]]
- [[harness-ratchet]]
- [[claude-code-session-management]]
- [[ai-orchestrator]]
- [[advisor-strategy]]
- [[building-pi-world-of-slop]]
- [[software-writing-software-gone-right]]
- [[just-in-time-software]]
- [[hashline]]
- [[edit-tool-formats]]
- [[improved-15-llms-harness-changed]]
- [[can-boluk]]
- [[oh-my-pi]]
- [[cursor]]
- [[cloud-agents]]
- [[what-weve-learned-building-cloud-agents]]
- [[self-healing-environments]]
- [[harness-guides-sensors]]
- [[birgitta-bockeler]]
- [[harness-engineering-bockeler]]
- [[thoughtworks]]
- [[meta-harness]]
- [[omnigent]]
- [[matt-pocock]]
- [[matt-pocock-agentic-workflow]]
- [[agent-experience]]
- [[bitter-lesson]]
- [[bring-your-own-agent]]
- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[kun-chen]]
- [[axi]]
- [[lavish]]
- [[no-mistakes]]
- [[treehouse]]
- [[first-mate]]
