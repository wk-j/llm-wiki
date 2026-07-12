---
title: Queues over Loops
type: concept
tags: [ai, agents, loops, afk, workflow, orchestration]
created: 2026-06-21
updated: 2026-07-12
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md", "รู้จักกับ Loop Engineering — mikelopster transcript", wayfinder-skill.md]
---

# Queues over Loops / มองงานเป็นคิว ไม่ใช่ลูป

**Queues over loops คือมุมของ [[matt-pocock|Matt Pocock]] ที่บอกว่า hype เรื่อง "agentic loop" มองภาพผิด — สิ่งที่เราต้องการจริง ๆ ไม่ใช่ลูปเดียวที่วิ่งทำทุกอย่างไม่จบ แต่เป็น "คิวของงาน" ที่มีหลายตัวคอยหยิบไปทำทีละชิ้น.** Matt พูดเรื่องนี้ในพอดแคสต์กับ [[david-ondrej|David Ondrej]] (2026-06-19)

## ปัญหาที่ Matt เห็นกับคำว่า "ลูป"

ช่วงนั้นบน Twitter คนแห่กันพูดเรื่อง agentic loop. Matt มองว่าครึ่งหนึ่งของกระแสคือ "lab อยากขาย token" — ยิ่งรันลูปตลอดเวลา ยิ่งจ่ายเงินค่า token ตลอด

ที่มาของลูปคือ **[[ralph|Ralph]]** ของ [[jeffrey-huntley|Jeffrey Huntley]] (14 ก.ค. ปีก่อน): `while` loop ที่ส่ง prompt เดิมให้ Claude Code ซ้ำ ๆ จนกว่าจะเสร็จ. แต่ Matt บอกว่าพอลองจริง เขา **ไม่ได้ต้องการ "ลูป"** สิ่งที่ต้องการมีแค่ AFK agent มารับงานที่ scope แล้วไปทำให้จบ (ดู [[afk-agents]])

## มองเป็นคิว

> "The way I mostly think about these things as queues, okay, queues, not loops."
> (ผมมองของพวกนี้เป็นคิวมากกว่า — คิว ไม่ใช่ลูป)

queue = backlog ของงานที่ต้องทำ. กลไกง่าย ๆ:

- PM / คน / observability tool (เช่น Sentry) **เติมงานเข้าคิว** (เปิด issue)
- มีหลาย **node** (agent หรือ dev) คอย **หยิบงานออกจากคิว**ไปทำ
- งาน **หลุดคิว**เมื่อ PR ถูก merge

นี่คือวิธีที่ทีม dev ทำงานกันมาตลอดอยู่แล้ว. ไอเดียที่ว่ามี "ลูปเดียววิ่งทำทุก task" ไม่ตรงกับการทำงานจริงของทีม. ตัวอย่างของ Matt: ใช้ GitHub issue ของ [[sandcastle|Sandcastle]] เป็นคิว, ติด label (เช่น `agent explore` / `agent implement`) ให้ agent หยิบงานไปทำผ่าน GitHub Actions เอง — ใคร (agent หรือคน) ก็ trigger งานได้

## ดันจุดที่ต้องมีคนตรวจไปทางขวา

ในกรอบ queue งานแต่ละชิ้นจะวิ่งผ่าน stage: bug report → exploration → fix → review. Matt บอกให้ออกแบบ **human-in-the-loop checkpoint** แล้วค่อย ๆ ดันมันไปทาง production เรื่อย ๆ. สิ่งที่ได้จาก checkpoint คือ (1) **gate ของอันตราย** (กัน security / โค้ดลับเข้า prod) และ (2) **insight เข้าระบบตัวเอง** เพื่อเอาไปปรับ harness. ถ้าจะถอด checkpoint ออก ต้องตอบให้ได้ว่า **"ใครจะ review ตัว AI ที่ตัดสินว่า PR ไหนไม่ต้อง review"**

> ได้อะไร: ภาระของเราไม่ใช่ "ออกแบบลูปที่วิ่งไม่จบ" แต่เป็น "จัดลำดับคิว + วาง checkpoint" เหมือนกษัตริย์ที่มีคิวปัญหาเข้ามาให้ตัดสิน ไม่ใช่ปล่อยรัฐมนตรีไปวิ่งเองในดินแดนไกล ๆ โดยไม่รายงาน (อุปมาของ David)

## ไม่ได้ขัดกับ loop engineering แรง ๆ

Matt ไม่ได้ปฏิเสธ [[loop-engineering|loop engineering]] ของ [[addy-osmani|Addy Osmani]] ทั้งหมด — เขาบอกเองว่า "ลูปมีประโยชน์ แต่ไม่ใช่ภาพทั้งหมด". ที่จริงทั้งสองมุมเสริมกัน:

- Addy เน้น **maker/checker split, state file, verifiable stop condition** — ซึ่งล้วนเป็นกลไกที่คิวก็ใช้
- Matt เน้นว่า **โครงควรเป็นคิวที่หลาย node หยิบงาน** ไม่ใช่ลูปเดี่ยว — และเน้นว่าส่วนมากของกระแสลูปเป็นเรื่อง AFK agent ธรรมดา ๆ ที่ถูกเรียกให้ดูหรูเกินจริง

มองอีกแบบ: คิวคือมุมมอง *เชิงระบบงานของทีม* ส่วนลูปคือมุมมอง *เชิงกลไกของ automation ตัวเดียว* — ใช้ด้วยกันได้

## มุมจาก mikelopster: บางงานเป็น todo ไม่ใช่ loop ใหม่

[[mikelopster]] เสริมมุมนี้จากการลองจริงใน [[mikelopster-loop-engineering|คลิป Loop Engineering]]. เขาพบว่าบางงานที่ดูเหมือนควรทำเป็น loop เช่น review/refactor/run test หลังแก้โค้ด แท้จริงเป็น loop ย่อยที่ coding agent ทำใน task เดียวอยู่แล้ว. ถ้า agent ใหญ่พอและมี pending task / checklist ชัด การเพิ่ม loop ข้างนอกอาจไม่ได้ให้ผลลัพธ์เพิ่ม.

ตรงนี้เข้ากับคำว่า "queues over loops": งานจำนวนมากควรถูก scope เป็น item ในคิว แล้วให้ agent หยิบไปทำจนจบ พร้อมหลักฐานว่าผ่าน. ไม่จำเป็นต้องสร้างลูปยาว ๆ รอบทุกอย่าง. ลูปค่อยมีน้ำหนักเมื่อมี trigger ภายนอกจริง เช่น PR ใหม่, CI แดง, ticket ใหม่, log ผิดปกติ, หรือ schedule ที่ต้องกลับมาดูซ้ำ.

> ได้อะไร: อย่าใช้คำว่า loop กลบความจริงว่างานนั้นอาจเป็นแค่ checklist ที่ต้องทำให้จบหนึ่งรอบ.

## ดูเพิ่ม

- [[afk-agents]]
- [[ralph]]
- [[loop-engineering]]
- [[matt-pocock]]
- [[matt-pocock-agentic-workflow]]
- [[orchestration-tax]]
- [[sandcastle]]
- [[agentic-code-review]]
- [[mikelopster-loop-engineering]]
- [[wayfinding]]
