---
title: Coding Harness
type: concept
tags: [ai, tools, agents, software-engineering, harness]
created: 2026-04-18
updated: 2026-05-03
sources: [alex-ker-harnesses-optimize.md, building-pi-world-of-slop.md]
---

# Coding Harness / ตัวครอบของ Coding Agent

**Coding harness** คือชั้นของซอฟต์แวร์ที่อยู่ระหว่างผู้ใช้กับ LLM จริง — เช่น [[claude-code|Claude Code]], [[openai-codex|Codex]], [[opencode|OpenCode]], Cursor, Deep Agent CLI, Roo Code — ซึ่งไม่ใช่ตัว model เอง แต่เป็นสิ่งที่ทำให้ model กลายเป็นเครื่องมือที่ใช้งานได้จริง

[[alex-ker|Alex Ker]] สรุปไว้ว่า "engineers used to argue about IDEs, now we argue about harnesses" (2026-04-18)

## นิยามเชิงวิศวกรรม

ในทางเทคนิค, harness คือ `while (have next message) do {tool}` loop — ซึ่งเป็นลูปที่ทำหน้าที่สองอย่างรอบๆ model ที่เป็น stateless อยู่ข้างใน:

1.  **จัดการ context** — sessions, compaction, rewind, การสลับ session
2.  **เชื่อมต่อ tool และ I/O** — tool call, การ parse output, guardrail, permission prompt

ถ้า model คือแหล่งของ intelligence, harness คือสิ่งที่ทำให้ intelligence นั้นใช้งานได้จริง — ลูปที่ราบรื่นจะช่วยเพิ่มความเร็วและคุณภาพของโค้ดที่ได้

[[mario-zechner|Mario Zechner]] เพิ่มมุมที่แข็งกว่านี้ใน [[building-pi-world-of-slop|Building pi in a World of Slop]]: harness ไม่ใช่แค่ UX wrapper แต่เป็นเจ้าของ context โดยพฤตินัย ถ้า harness เปลี่ยน system prompt, tool definitions, reminders, หรือ inject feedback เองโดยผู้ใช้มองไม่เห็น workflow ของผู้ใช้ก็อาจพังได้ แม้ model ตัวเดิมจะยังเก่งเท่าเดิม

## สองความหมายของคำว่า "harness"

คำว่า "harness" ในวงการ AI coding ปัจจุบันมีการใช้งานสองแบบที่ต้องแยกแยะ:

| นิยาม | ผู้ใช้ | ความหมาย |
|---|---|---|
| **Harness = ตัวครอบ / scaffolding** | Alex Ker, Kyle/[[humanlayer\|HumanLayer]] | เครื่องมือทั้งหมด (Claude Code, Codex ฯลฯ) — ตามที่อธิบายในหน้านี้ |
| **Harness engineering = pipeline ของ review agent** | [[panutat-tejasen\|Panutat Tejasen]] | ลำดับของ agent ที่ทำหน้าที่ตรวจสอบโค้ด / ทดสอบ / audit |

ทั้งสองความหมายไม่ขัดแย้งกัน — pattern ของ Panutat เป็น *เทคนิคย่อย* ที่เกิดขึ้น *ภายใน* harness ตัวใหญ่ ดูที่ [[subagent-patterns]] ในส่วน "pipeline" — Alex Ker กล่าวว่า `UX designer → architect → devil's advocate` เป็นรูปแบบเดียวกับที่ Panutat เสนอ เพียงแค่มองจากมุมของ productivity รายวันแทนที่จะเป็น pedagogy

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
- [[claude-code-session-management]]
- [[ai-orchestrator]]
- [[advisor-strategy]]
- [[building-pi-world-of-slop]]
