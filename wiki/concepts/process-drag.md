---
title: Process Drag
type: concept
tags: [ai, software-engineering, organization, workflow]
created: 2026-05-27
updated: 2026-05-27
sources: [software-after-software.md]
---

# Process Drag / พิธีกรรมเก่ากลายเป็นแรงต้าน

**Process Drag** คือสภาวะที่กระบวนการทำงานเก่า (planning, prioritization, handoff, review) — ที่เคยช่วยให้ทีมไม่พังในยุค "code แพง" — กลายเป็น **แรงต้าน (drag)** เมื่อ implementation ราคาถูกลงมาก

แนวคิดนี้มาจาก [[software-after-software|Software After Software]] ของ [[thorsten-ball|Thorsten Ball]] (manifesto จาก [[amp-labs|Amp Labs]], 2026-05-26) ข้อ 6: "The old processes and practices of working with software are no longer apt"

## ที่มา

Ball เริ่มจากข้อสังเกตง่าย ๆ: rituals ทั้งหมดที่เราใช้ในวงการ software dev — sprint planning, prioritization meeting, requirements grooming, prototype proposal, code review — ถูกออกแบบในโลกที่ implementation **ช้า แพง พลาดง่าย และผูกกับคน**

พอ implementation ราคาถูกลงเพราะ agent ทำได้ ([[code-is-free]]), เงื่อนไขที่ทำให้ ritual เหล่านี้คุ้มก็หายไป

## ตัวอย่างที่ Ball ยกมา

Ball ยก rhetorical question 4 ข้อในข้อ 6.2 ที่กลายเป็น signature ของบทความ:

- "Why spend an hour prioritizing what can be done in thirty minutes?"
- "Why consider building a prototype when you can talk one into existence?"
- "Why wait for a review when you can spin up five agents to review in parallel?"
- "Why pick a single idea to try when you can try them all in parallel and dismiss four out of five without hurting a single ego?"

แต่ละข้อชี้ที่ ritual คนละแบบ:

| Ritual เก่า | ทำไมเคยจำเป็น | ทำไมตอนนี้กลายเป็น drag |
|---|---|---|
| Sprint prioritization | implementation แพง ต้องเลือกแค่บางอย่าง | implementation ราคาถูก ทำได้ทั้งหมด |
| Prototype proposal | ทำ prototype กินเวลาเป็นวัน | "talk one into existence" ได้ทันที |
| Sequential code review | reviewer มีจำนวนจำกัด | "spin up five agents to review in parallel" |
| เลือก idea เดียวลอง | resource จำกัด ต้องเลือก | ทำพร้อมกันได้ ทิ้ง 4/5 ไม่เจ็บใจใคร |

## คีย์ของแนวคิด

> "AI is not only an accelerator for X. It changes whether X should exist at all."

ประเด็นไม่ใช่ "ทำ X ให้เร็วขึ้นด้วย AI" แต่คือ **"X ควรมีอยู่ไหม"** เลย เพราะ ritual หลายอย่างเกิดขึ้นเพราะข้อจำกัดที่ไม่มีอยู่อีกแล้ว

ได้อะไร: ก่อนจะ optimize ritual เก่าด้วย AI ให้ถามก่อนว่า ritual นั้นยังจำเป็นอยู่ไหม

## ระวังจุดที่ Ball พูดเกินไป

Process drag ไม่ได้แปลว่าทุก ritual ตาย. หลาย ritual ยังจำเป็น เพราะมันแก้ปัญหาที่ไม่ใช่แค่ "implementation แพง":

- **Code review** ยังจำเป็นถ้า review นั้นเป็นช่วงที่ team align ความเข้าใจระบบ (mental model transfer) ไม่ใช่แค่หา bug
- **Prioritization** ยังจำเป็นถ้ามี constraint อื่นที่ไม่ใช่ engineering capacity — เช่น attention ของลูกค้า, regulatory approval, brand consistency
- **Handoff** ยังจำเป็นเพราะ [[acceptance-bottleneck|acceptance]] ยังเป็น human bottleneck ที่ AI ลดไม่ได้

Ball เขียน manifesto ในมุมที่ assume implementation cost = ปัญหาหลักของทุก ritual ซึ่งจริงบางส่วน ไม่จริงบางส่วน

[[chrisza-stuff|ChrisZa]] ใน [[interaction-productivity]] เตือนว่าถ้าเรา optimize แค่ฝั่ง producer (เร่ง ritual ให้สั้น) โดยไม่ดูฝั่ง consumer (คนรับงาน accept ทัน) ก็จะเพิ่ม waste

## วิธีคัด ritual ที่เป็น drag จริง

ถามสองคำถามต่อ ritual:

1. **ritual นี้แก้ปัญหา "code implementation ราคาแพง" หรือเปล่า** — ถ้าใช่ มีแนวโน้ม drag
2. **ถ้าตัดทิ้งวันนี้ จะรู้ภายในกี่วันว่าพังตรงไหน** — ถ้ารู้เร็ว ตัดได้ ถ้ารู้ช้า ระวัง

ritual ที่ผ่านทั้งสองข้อคือผู้สมัครให้ตัดทิ้ง อันที่ไม่ผ่านควรเก็บไว้ก่อนแล้วค่อย optimize

## ความสัมพันธ์กับแนวคิดอื่น

- [[code-is-free]] — เงื่อนไขที่ทำให้ process drag เกิด (implementation ราคาถูก)
- [[reorganize-around-models]] — Ball เสนอว่าตัด ritual เก่าก็ยังไม่พอ ต้อง re-org ทีมรอบ model
- [[interaction-productivity]] — มุมที่ต่าง: optimize ritual ฝั่ง producer ไม่พอ ต้องดูฝั่งคนรับงาน
- [[acceptance-bottleneck]] — เตือนว่า "spin up 5 agents to review" ไม่ใช่คำตอบถ้า reviewer ที่ตัดสินใจจริงคือมนุษย์
- [[ai-era-standard-balance]] — แนวคิดคล้ายกัน: standard เก่าไม่เหมาะกับโลกที่ producer ผลิตของได้ง่ายขึ้น 10 เท่า
- [[lead-time]] — process drag คือสาเหตุที่ลด lead time ไม่ได้แม้ implementation จะเร็วขึ้น

## See also

- [[software-after-software]]
- [[code-is-free]]
- [[reorganize-around-models]]
- [[value-migration-from-code]]
- [[frontier-camp]]
- [[acceptance-bottleneck]]
- [[ai-era-standard-balance]]
- [[local-optimization-trap]]
