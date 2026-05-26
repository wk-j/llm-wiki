---
title: Reorganize Around Models
type: concept
tags: [ai, organization, strategy, management]
created: 2026-05-27
updated: 2026-05-27
sources: [software-after-software.md]
---

# Reorganize Around Models / จัดทีมรอบโมเดล ไม่ใช่ใส่โมเดลเข้าทีมเดิม

**Reorganize Around Models** คือข้อเสนอเชิงองค์กรของ [[thorsten-ball|Thorsten Ball]] ที่ว่า "ผู้ชนะ" ในยุคนี้จะไม่ใช่บริษัทที่ใส่ AI เข้าไปใน org chart และ process เดิม แต่คือบริษัทที่ **จัดทีมรอบ model ตั้งแต่ต้น**

มาจาก [[software-after-software|Software After Software]] ข้อ 9

## คีย์ของแนวคิด

> "It will not be enough to fit models into existing systems, org charts, and processes."

> "Agents are wasted when made to work like people."

> "A small team with strong judgment and many agents will outrun a large team trying to fit AI into processes from before the transformation."

> "Ability to keep up matters more than headcount."

## ทำไม "ใส่ AI เข้าทีมเดิม" ไม่พอ

ทีมและ process เก่าออกแบบบนสมมติฐานว่า:

- หน่วยงานคือคน 1 คน = 1 task ในเวลาหนึ่ง
- meeting ใช้ตัด decisions
- handoff เกิดเป็นจังหวะ (sprint, release)
- review เป็น sequential bottleneck
- speed ของทีม = sum ของ throughput รายคน

พอใส่ agent เข้ามาในโครงเดียวกัน agent จะถูกบังคับให้:

- ทำงานเสร็จเป็น turn ๆ ตามจังหวะ chat ([[delegation-mindset]] อธิบายปัญหานี้)
- รอคน approve ทีละขั้น
- ห้ามทำงานพร้อมกันกับ agent อื่นเพราะ process รองรับไม่ได้

ผลคือ agent ถูก "บังคับให้ทำงานแบบมนุษย์" — ตามที่ Ball เรียกว่า **"a wasted agent"**

## ทีมที่จัดรอบ model หน้าตาเป็นยังไง

Ball ไม่ได้ระบุ template ชัดเจน แต่ implication ที่ตามมาคือ:

- **เล็ก** — "small team with strong judgment"
- **คนที่อยู่ในทีมต้องมี judgment สูง** — เพราะหน้าที่ของเขาคือ shape/direct/judge ไม่ใช่ execute
- **มี agent หลายตัว** — "many agents" — implementation ทำโดย agent ไม่ใช่คน
- **process รองรับ parallel** — review หลาย agent พร้อมกัน, ทดลอง idea หลายแบบพร้อมกัน
- **ไม่ยึดติด ritual เก่า** — ดู [[process-drag|Process Drag]]

## ทำไม ability to keep up > headcount

Ball เปลี่ยน frame จาก "ทีมใหญ่ vs ทีมเล็ก" ไปเป็น "ทีมที่ตามทันความเปลี่ยนแปลงของ model vs ทีมที่ตามไม่ทัน"

ในข้อ 2 เขาบอกว่า model พัฒนาทุก 8 สัปดาห์ และคนควรปล่อย leash ยาวขึ้นเรื่อย ๆ ทีมที่ตามไม่ทันจะ "ติดอยู่ที่จุดต่ำของกราฟ" — ใช้ model ผิดวิธี เปลือง headcount เกินจำเป็น

ทีมเล็กที่ปรับ leash ทุก 8 สัปดาห์จึง outrun ทีมใหญ่ที่ปรับยาก ๆ ปีละครั้ง

ได้อะไร: speed ของ adaptation = competitive advantage ใหม่ ไม่ใช่ขนาด

## ปัญหาที่ Ball ไม่พูดถึง

แนวคิดนี้สวยใน manifesto แต่ในทางปฏิบัติมี friction:

- **Compliance / regulated industry** — financial services, healthcare, government ไม่สามารถ "ปล่อย leash ยาวขึ้น" ได้ง่าย ๆ
- **Acceptance bottleneck** — [[chrisza-stuff|ChrisZa]] ใน [[acceptance-bottleneck|Acceptance Bottleneck]] ชี้ว่าฝั่ง consumer (คนรับงาน) ยังเป็น human bottleneck ที่ AI ลดไม่ได้ ทีมเล็ก + agent เยอะ ผลิตของได้มาก แต่ฝั่งรับงานยังเท่าเดิม
- **ความรับผิดชอบ** — ใครรับผิดถ้า agent พัง? ทีมใหญ่กระจาย accountability ผ่าน role/process; ทีมเล็กที่ delegate ไป agent ทุกอย่างยังหาคำตอบที่ดีไม่เจอ
- **Talent supply** — "strong judgment" หาง่าย ๆ ไม่ได้ ทีมเล็กที่มีคน judgment สูงทุกคนเป็นของหายาก

Ball position ตัวเอง (Amp Labs) เป็นตัวอย่างของทีมแบบนี้ แต่ Amp Labs มี context เฉพาะ (frontier R&D ของบริษัทขายของ AI) ที่ไม่ใช่ทุกองค์กรเอามาใช้ตรง ๆ ได้

## ความสัมพันธ์กับแนวคิดอื่น

- [[frontier-camp]] — implementation pattern ของแนวคิดนี้ที่ Ball เสนอเป็นรูปธรรมที่สุด
- [[process-drag]] — ritual เก่าคือเหตุผลหนึ่งที่ใส่ AI เข้าทีมเดิมไม่ได้
- [[engineering-role-shift]] — บทบาทคนในทีมที่ reorg แล้วเปลี่ยน
- [[delegation-mindset]] — pattern ระดับ prompt ที่สะท้อนแนวคิดเดียวกัน
- [[acceptance-bottleneck]] — เตือนว่า "ทีมเล็ก + agent เยอะ" ผลิตของได้มาก ไม่ได้แปลว่า lead time ลด
- [[code-is-free]] — เงื่อนไขที่ทำให้ทีมเล็ก + agent เยอะ เป็นไปได้

## See also

- [[software-after-software]]
- [[frontier-camp]]
- [[process-drag]]
- [[value-migration-from-code]]
- [[engineering-role-shift]]
- [[delegation-mindset]]
- [[acceptance-bottleneck]]
