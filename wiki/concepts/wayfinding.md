---
title: Wayfinding
type: concept
tags: [ai, agents, planning, issue-tracking, workflow]
created: 2026-07-12
updated: 2026-07-12
sources: [wayfinder-skill.md, new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets.md]
---

# Wayfinding / ค่อยหาเส้นทางผ่านงานที่ยังมองไม่ครบ

**Wayfinding คือการวางแผนงานใหญ่แบบยอมรับว่าเรายังเห็นเส้นทางไม่ครบ.** แทนที่จะเดาแผนยาวตั้งแต่ต้น เราตั้ง destination ให้ชัด แล้วค่อยปิดคำถามหนึ่งเรื่องต่อ session. ทุกคำตอบทำให้ขอบของสิ่งที่มองเห็นขยับไปข้างหน้า.

คำนี้มาจาก skill `wayfinder` ของ [[matt-pocock|Matt Pocock]] (ผู้สร้าง workflow สำหรับ coding agent) ใน [[wayfinder-skill|Wayfinder Skill]]. Artifact หลักคือ issue map ที่เก็บ destination, decision ที่ปิดแล้ว, fog ที่ยังตั้งคำถามไม่ได้ และขอบเขตที่ตัดออก.

## โมเดลหลัก

Wayfinding แยกงานออกเป็นสี่ชั้นที่เปลี่ยนตามสิ่งที่เรียนรู้:

1. **Destination** — นิยามว่าการหาเส้นทางจบตรงไหน
2. **Frontier** — คำถามที่คมพอและพร้อมให้ session หยิบไปปิดตอนนี้
3. **Blocked tickets** — คำถามที่คมแล้ว แต่ต้องรอ decision อื่น
4. **Fog** — พื้นที่ใน scope ที่รู้ว่าต้องกลับมาดู แต่ยังถามให้ precise ไม่ได้

พอปิด frontier ticket หนึ่งใบ fog บางส่วนอาจชัดพอจะกลายเป็น ticket. บาง ticket อาจถูกลบหรือย้ายออกนอก scope เพราะคำตอบใหม่เปลี่ยนภาพเดิม.

**ได้อะไร:** แผนไม่แข็งจนขัดกับ evidence ใหม่ และไม่หลวมจนไม่มีคำถามถัดไปให้ทำ.

## ต่างจาก project backlog

Backlog ปกติมักเก็บสิ่งที่ต้อง “ทำ”. Wayfinding map เก็บสิ่งที่ต้อง “รู้หรือตัดสินใจ” ก่อน implementation. Research, prototype, grilling และ task มีค่าเพราะมันลดความไม่รู้หรือปลด blocker ของ decision ไม่ใช่เพราะมันผลิต deliverable ได้เยอะ.

อีกจุดต่างคือ map ตั้งใจไม่ครบ. `Not yet specified` ไม่ใช่ backlog ชั้นสอง แต่เป็นที่วาง fog จนเรามองเห็นคำถามจริง. ถ้าฝืนแตก fog เป็น task เร็วเกินไป จะได้รายการละเอียดที่อิงกับสมมติฐานผิด.

**ผลคือ:** จำนวน ticket ไม่ถูกใช้แทนความเข้าใจ; ticket ใหม่เกิดเมื่อข้อมูลพร้อม ไม่ใช่เพื่อทำให้ roadmap ดูแน่น.

## ทำไมเหมาะกับหลาย agent session

Agent session มี context จำกัด. Wayfinding เก็บ state ระยะยาวไว้ใน tracker แล้วให้แต่ละ session โหลด map แบบ low-resolution ก่อน zoom เข้า ticket เดียว. Assignee ทำหน้าที่ claim ส่วน dependency ทำให้ frontier มองเห็นได้.

นี่ทำให้หลาย session ทำงานขนานได้เฉพาะ decision ที่ไม่ติดกัน. รูปแบบนี้สอดคล้องกับ [[queues-over-loops]]: ไม่ต้องมี agent ตัวเดียววนแบกทุกอย่าง แค่มีคิว frontier ที่ scope ชัด แล้วเก็บผลกลับเข้า map.

**ได้อะไร:** ความต่อเนื่องอยู่ใน artifact ร่วม ไม่ได้ผูกกับ transcript หรือความจำของ agent ตัวเดียว.

## ความสัมพันธ์กับ unknowns

Wayfinding แปลง [[unknowns-matrix]] ให้เป็นกลไกทำงาน:

- รู้คำถามแล้วแต่ยังไม่รู้คำตอบ → ticket
- ยังไม่รู้ว่าจะตั้งคำถามอย่างไร → fog
- รู้คำตอบแล้ว → decision pointer ไปยัง ticket ที่ปิด
- รู้ว่าเรื่องนั้นไม่จำเป็นต่อ destination → out of scope

ส่วน [[map-vs-territory]] เตือนว่า issue map ก็ยังเป็นเพียงตัวแทนของ codebase และข้อจำกัดจริง. Wayfinding จึงไม่พยายามทำ map ให้สมบูรณ์ตั้งแต่ต้น แต่ให้ map เปลี่ยนตาม territory ที่เพิ่งค้นพบ.

**ผลคือ:** unknown ไม่ถูกซ่อนใต้ task ที่เขียนเหมือนรู้คำตอบแล้ว.

## จาก map ไปสู่ implementation lifecycle

[[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets|Skills v1.1 changelog]] บอก downstream หลัง map ชัด: ส่ง map เข้า `/to-spec`, แตก spec ด้วย `/to-tickets`, แล้วทำ ticket ละหนึ่ง coding session ผ่าน `/implement` ก่อน [[dual-axis-code-review|code review สองแกน]] และ commit.

ตรงนี้ย้ำว่า Wayfinder อยู่ใน **pre-spec**. Ticket ใน map ปิดคำถามเพื่อหาเส้นทาง ส่วน ticket หลัง `/to-tickets` ใช้ลงมือทำ spec. ชื่อเหมือนกันแต่หน้าที่ต่างกัน: decision ticket ผลิตความเข้าใจ; implementation ticket ผลิต change.

**ได้อะไร:** แผนที่มีจุดจบและ handoff ชัด ไม่กลายเป็น planning system ที่สะสม decision ไปเรื่อย ๆ โดยไม่เริ่มสร้างของ.

## เมื่อไหร่ไม่ควรใช้

- งานเล็กพอจบใน session เดียวและไม่มี fog
- destination ยังไม่มีเจ้าของตัดสินใจ จนแม้แต่ grilling ก็หาคำตอบไม่ได้
- ทีมไม่มีวินัยปิด decision และอัปเดต map; artifact จะ stale เร็ว
- ค่า ceremony ของ issue/dependency มากกว่าความเสี่ยงจากการหลงทาง

Wayfinding เหมาะกับงานที่ “เส้นทางยังไม่ชัด” มากกว่างานที่ “เส้นทางชัดแต่ลงมือเยอะ”. แบบหลังควรใช้ execution plan หรือ task queue ตรง ๆ.

## See also

- [[wayfinder-skill]]
- [[map-vs-territory]]
- [[unknowns-matrix]]
- [[queues-over-loops]]
- [[grill-me]]
- [[domain-modeling]]
- [[agent-handoff-documents]]
- [[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets]]
