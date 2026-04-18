---
title: Coding Harness
type: concept
tags: [ai, tools, agents, software-engineering, harness]
created: 2026-04-18
updated: 2026-04-18
sources: [alex-ker-harnesses-optimize.md]
---

# Coding Harness / ตัวครอบของ Coding Agent

**Coding harness** คือชั้นโครงที่อยู่ระหว่างคนกับ LLM ตัวจริง — [[claude-code|Claude Code]], [[openai-codex|Codex]], [[opencode|OpenCode]], Cursor, Deep Agent CLI, Roo Code เป็นต้น — ไม่ใช่ตัว model เอง แต่เป็นของที่ทำให้ model กลายเป็นเครื่องมือทำงานได้จริง

[[alex-ker|Alex Ker]] สรุปไว้สั้น ๆ ว่า "engineers used to argue about IDEs, now we argue about harnesses" (2026-04-18)

## นิยามแบบวิศวกร

ในทาง mechanic, harness = `while (have next message) do {tool}` loop — ลูปที่ทำหน้าที่สองอย่างนี้รอบ ๆ model ที่เป็น stateless อยู่ข้างใน:

1. **จัดการ context** — sessions, compaction, rewind, การสลับ session
2. **เชื่อม tool และ I/O** — tool call, การ parse output, guardrail, permission prompt

ถ้า model คือแหล่ง intelligence ตัว harness คือสิ่งที่ทำให้ intelligence นั้นใช้งานได้จริง — ลูปที่ smooth ช่วยขยาย speed และ quality ของ code ที่ตามมาได้ทั้งเส้น

## สองความหมายของคำว่า "harness"

คำว่า harness ในวงการ AI coding ตอนนี้มีใช้สองแบบ อย่าสับสน:

| นิยาม | ใช้โดย | หมายถึง |
|---|---|---|
| **Harness = ตัวครอบ / scaffolding** | Alex Ker, Kyle/[[humanlayer\|HumanLayer]] | ทั้ง tool (Claude Code, Codex ฯลฯ) — หน้านี้ |
| **Harness engineering = pipeline ของ review agent** | [[panutat-tejasen\|Panutat Tejasen]] | ลำดับของ agent ตรวจ code / ทดสอบ / audit |

ไม่ขัดกัน — Panutat pattern เป็น *เทคนิคย่อย* ที่เกิดขึ้น *ภายใน* harness ตัวใหญ่ ดู [[subagent-patterns]] ช่อง "pipeline" — Alex Ker บอกไว้ว่า `UX designer → architect → devil's advocate` คือรูปแบบเดียวกับที่ Panutat เสนอ เพียงแค่มองจากมุม productivity รายวันแทน pedagogy

## จุดที่วิจารณญาณวิศวกรเข้ามาใช้

Alex Ker ชี้ว่ามีสามจุดที่เปลี่ยน output จาก slop เป็นของใช้ได้ และทั้งสามจุดยังต้องใช้ human judgement:

### 1. เก็บ config ให้เบาและเขียนเอง

`CLAUDE.md` / `AGENTS.md` ควร **ให้คนเขียน ไม่ใช่ให้ LLM generate** — อ้าง ETH research ว่า system prompt ที่ LLM generate ทำ performance แย่ลง *และ* กิน inference ~20% มากกว่า ทุก token ต้องสู้ที่ในไฟล์ เพราะจะถูก inject ทุก session

วิธีที่ใช้ได้คือ [[progressive-disclosure]] — บอก agent ว่ามีอะไร แต่ไม่ load content เข้ามาจนกว่าจะต้องใช้จริง

### 2. ใช้ R.P.I. framework ตอน prompt

**R.P.I. = Research / Plan / Implement** — จาก [[humanlayer|HumanLayer]] prompt แต่ละรอบควรทำอย่างใดอย่างหนึ่งใน 3 อย่างนี้เท่านั้น:

1. **Research** — บอกปัญหาให้ agent ไปอ่าน code เอง: structure, prior art, function definition, ความสัมพันธ์ของไฟล์ *ยังไม่ให้แก้อะไร*
2. **Plan** — ให้ agent เขียน plan เป็นขั้น ๆ ออกมา **คนต้องอ่านและ verify plan นั้นจริง ๆ** Alex Ker ใช้คำแรงไว้ว่า "outsourcing thinking or being lazy at this step will cost you dearly later on"
3. **Implement** — รัน plan ใน context window ใหม่ (เรียก main window) ถ้า plan ยาวให้แยก subagent ไปทำเป็นช่วง ๆ

ภาพรวมที่ Alex Ker พูดคือ — คุมให้ harness ทำงานแบบ staff engineer เก่ง ๆ ทำ: แตกปัญหาเป็นปัญหาย่อย, plan ก่อนลงมือ, หาคนอ่าน plan ให้ก่อน abstraction ย้ายจาก "เขียน code ทีละบรรทัด" มาเป็น "ออกแบบ prompt" แต่วินัยเบื้องล่างไม่เปลี่ยน

### 3. ใช้ subagent เพื่อเก็บ main context ให้สะอาด

Heuristic ง่าย ๆ — **ถ้าแค่ต้องการ summary ของงาน ให้ delegate ไป subagent** ถ้าคิดว่าจะย้อนกลับมาถามว่า "อันนี้เกี่ยวกับที่อ่านเมื่อกี้ยังไง" เก็บไว้ใน window หลัก

สอง pattern ที่ Alex Ker แนะนำ ดูรายละเอียดที่ [[subagent-patterns]]:

- **Parallel fan-out** — เปิดหลาย subagent พร้อมกัน เหมาะกับ investigation/research
- **Pipeline** — ต่อ role เป็นลำดับ เหมาะกับงานที่ต้องมองหลายมุม

## ข้อสรุปที่ Alex Ker เน้น: commit

เวลา harness fail งานสักงาน คนมักอยากโดด harness — Alex Ker ไม่ห้ามให้ลอง แต่เตือนว่า constant switching แปลว่า institutional knowledge ที่อยู่ใน config file และ failure-case log หาย กลับไปนับหนึ่งใหม่ทุกครั้ง

คำแนะนำคือ — เลือก harness ที่ครอบ use case ของทีมได้ส่วนใหญ่ เจอ failure เมื่อไร บันทึก (*พังที่ไหน, ขั้นไหน, เงื่อนไขไหน*) ป้อนกลับเข้า `.md` file และปรับ prompting strategy เรื่อย ๆ

> "The best harness is the harness that you have customized and iterated on with human engineering; it's the one that can handle edge cases which are smoothed out through your team's usage."

## ทำไมเรื่องนี้สำคัญ

- [[instruction-budget]] และ [[context-rot]] ทำให้การ "ใส่ทุกอย่างเข้า prompt" ไม่ work อีกต่อไป — harness คือที่ที่ mitigation ทั้งหมดนั้นอยู่ (progressive disclosure, subagent, compaction)
- [[ai-orchestrator]] — orchestration skill ตอนนี้ถูกย้ายลงไปเป็นงาน entry-level (ดู [[engineering-role-shift]]) Harness คือ surface ที่ skill นั้นแสดงออก
- [[harness-engineering]] (Panutat) — pipeline review agent pattern อยู่ภายใน harness ตัวใหญ่ตัวนี้
- [[advisor-strategy]] — เป็นอีกรูปแบบ agent architecture ที่ harness ออกแบบรับรองได้

## See also

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
- [[claude-code-session-management]]
- [[ai-orchestrator]]
- [[advisor-strategy]]
