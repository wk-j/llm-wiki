---
title: Developer Balance
type: concept
tags: [ai, agents, developer-experience, attention, burnout, health, productivity]
created: 2026-06-11
updated: 2026-06-11
sources: [How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md]
---

# Developer Balance / สมดุลของนักพัฒนาในยุค Agent

**Developer Balance** คือการออกแบบวิธีทำงานกับ AI agent ให้คนยังรักษาสมาธิ สุขภาพ judgement และความสามารถในการกลับมาทำงานดีได้วันถัดไป. [[zack-proser|Zack Proser]] (วิศวกร Applied AI ที่ [[workos|WorkOS]]) เสนอกรอบนี้ใน talk [[how-to-keep-shipping-away-from-desk|How to Keep Shipping When You Walk Away from Your Desk]].

> "The tools are nuclear now. Our nervous systems are still ancient."

ประโยคนี้ชี้ความไม่สมมาตรหลัก: agent เพิ่มจำนวนและวนทำงานได้เร็ว แต่ attention กับพลังงานของคนลดลงเมื่อรับโหลดมากขึ้น. ถ้าเอากำลัง agent ไปเพิ่ม WIP ตรง ๆ เราไม่ได้แก้คอขวด แค่เร่งให้คนหมดแรงเร็วขึ้น.

## ต่างจาก productivity optimization ยังไง

Productivity optimization มักถามว่า "วันนี้ ship ได้กี่ชิ้น". Developer Balance เพิ่มคำถามอีกข้อว่า **"วิธีนี้ทำให้พรุ่งนี้เรายังตัดสินใจได้ดีไหม"**.

จุดวัดจึงไม่ใช่จำนวน agent หรือจำนวน PR อย่างเดียว แต่รวมถึง:

- งานที่ ship ผ่าน verification จริง
- จำนวน context switch ที่คนต้องจ่าย
- คุณภาพของ review และ mental model ที่คนยังถืออยู่
- เวลาที่ได้ใช้กับ judgement แทนงานจุกจิก
- สภาพร่างกาย การนอน และความเหนื่อยสะสม

**ผลคือ:** throughput ที่ดีต้องยั่งยืน ไม่ใช่ output สูงสองวันแล้วพังปลายสัปดาห์.

## หลักออกแบบสี่ข้อ

### 1. กรองสัญญาณก่อนถึงคน

อย่าให้ทุก Slack thread, ticket, และ notification เข้ามาแย่ง attention เท่ากัน. ใช้ signal agent อ่าน inbox แล้วส่งเฉพาะเรื่องสำคัญหรือเรื่องที่ต้องใช้ judgement.

นี่คือ [[care-allocation|care allocation]] ในระดับ workflow: คนยังตัดสินใจ แต่ไม่ต้องเปิดทุกแหล่ง noise ด้วยตัวเอง.

**ได้อะไร:** attention รั่วน้อยลงและ deep work อยู่ได้นานขึ้น.

### 2. ให้ agent ปิด loop ที่พิสูจน์ได้

งานที่ delegate ควรมาพร้อมเครื่องมือและ acceptance criteria ที่ agent ใช้ตรวจเองได้ เช่น lint, test, browser flow, หรือ critic pass. คนควรกลับมาตอนมีหลักฐานหรือมี decision จริง ไม่ใช่ตอน agent แค่หยุดทำ.

หลักนี้ตรงกับ [[harness-guides-sensors|guides and sensors]], [[facts-first]], และวิธี "only spend the lock on judgement" ใน [[orchestration-tax]].

**ได้อะไร:** ลดการเรียกคนกลับมาแก้รายละเอียดที่ระบบตรวจเองได้.

### 3. แยกการ steer ออกจากการนั่งเฝ้า

Remote control ทำให้คนเริ่มงานที่โต๊ะ แล้วลุกไปเดินหรือเปลี่ยนกิจกรรมได้ ขณะที่ agent ยังทำงานต่อ. คนยัง steer ผ่านมือถือเมื่อมี insight หรือ decision สำคัญ.

เป้าหมายไม่ใช่ทำงานทุกนาทีแม้อยู่นอกโต๊ะ. เป้าหมายคือไม่บังคับให้การขยับร่างกายหรือเปลี่ยนโหมดคิดต้องแลกกับการหยุด agent ทั้งหมด.

**ได้อะไร:** agent เดินงานต่อ ส่วนคนได้ diffuse thinking และลดภาระทางกาย.

### 4. ให้ระบบเรียนจากความฝืด

ประวัติ conversation, จุดที่ต้องถามซ้ำ, และ failure ที่เกิดจริงควรถูกนำมาทบทวนเป็นรอบ. ถ้าพบ pattern ให้แปลงเป็น skill, hook, test, MCP integration, หรือ guide ใหม่.

นี่คือ [[harness-ratchet|Harness Ratchet]] ที่มอง session history เป็น telemetry ของวิธีทำงาน ไม่ใช่ขยะหลังจบ chat.

**ได้อะไร:** ความฝืดสัปดาห์นี้กลายเป็นการปรับระบบ ไม่ใช่งานซ้ำสัปดาห์หน้า.

## ความสัมพันธ์กับ Orchestration Tax

[[orchestration-tax|Orchestration Tax]] อธิบายคอขวด: agent ผลิตขนานได้ แต่คน review และ merge แบบ serial. Developer Balance คือคำตอบในระดับชีวิตการทำงาน:

| Orchestration Tax บอกว่า | Developer Balance ทำอะไร |
|---|---|
| คนคือ serial bottleneck | ปกป้องเวลาที่คนตัดสินใจได้ดีที่สุด |
| เปิด agent เกิน review rate แล้วพัง | จำกัด WIP และ batch review |
| context switch แพง | ใช้ signal layer และปล่อย agent มีสายป่าน |
| ต้องใช้ lock เฉพาะ judgement | เพิ่ม verification gate ให้ agent |
| cognitive surrender เกิดเมื่อ attention หมด | ใช้สุขภาพและความเหนื่อยเป็น constraint จริง |

**สรุป:** Developer Balance ไม่ได้ปฏิเสธความเร็วของ agent แต่จัดระบบให้ความเร็วนั้นไม่กินคนเป็นเชื้อเพลิง.

## กับดัก

- **Remote work กลายเป็น always-on work** — ถ้าถือว่ามือถือทำให้ต้องตอบ agent ตลอดเวลา การลุกจากโต๊ะจะไม่ใช่การฟื้นตัว.
- **ส่งงานเร็วกว่า review** — voice-first flow เพิ่ม input rate ได้มาก แต่ไม่ได้เพิ่ม judgement rate.
- **เอา health telemetry มา optimize คนเกินไป** — ข้อมูลสุขภาพควรช่วยจำกัดงาน ไม่ใช่ใช้บีบ output เพิ่ม.
- **คนใหม่ delegate เร็วเกินไป** — ถ้ายังไม่มี mental model ก็จับ hallucination และ design ที่ไม่ดีไม่ได้. ต้องกัน [[skill-atrophy]] ด้วยการลงมือทำเองในเรื่องที่กำลังเรียน.
- **Agent เข้าถึงข้อมูลกว้างเกินจำเป็น** — signal layer และ health integration ต้องมี permission, privacy, และ security boundary ที่ชัด.

## See also

- [[how-to-keep-shipping-away-from-desk]]
- [[zack-proser]]
- [[orchestration-tax]]
- [[cognitive-surrender]]
- [[care-allocation]]
- [[harness-ratchet]]
- [[harness-guides-sensors]]
- [[claude-code-remote-surfaces]]
- [[skill-atrophy]]
