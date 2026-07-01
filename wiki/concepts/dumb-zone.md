---
title: Dumb Zone
type: concept
tags: [ai, agents, context-management, compaction, ai-coding]
created: 2026-06-29
updated: 2026-06-29
sources: [matt-pocock-dumb-zone-compaction.md]
---

# Dumb Zone / โซนที่ agent เริ่มโง่

**Dumb zone** คือช่วงที่ coding agent ยังมี context window เหลือ แต่คุณภาพการคิดเริ่มตก. [[matt-pocock|Matt Pocock]] ใช้คำนี้ในโพสต์ [[matt-pocock-dumb-zone-compaction]] เพื่ออธิบายอาการที่ agent ทำเรื่องโง่ใน session ยาว แล้วกลับมาดูฉลาดขึ้นหลัง `/rewind` + `/compact`.

มันเป็นญาติใกล้ ๆ ของ [[context-rot|context rot]]. ต่างกันนิดเดียว: context rot คือชื่ออาการทั่วไป ส่วน dumb zone คือวิธีพูดแบบคนใช้ agent หน้างานว่า "มันยังรันได้ แต่เริ่มคิดแปลกแล้ว".

## อาการที่เห็น

อาการสำคัญไม่ใช่ error ชัด ๆ. หลายครั้ง agent ยังตอบยาว ดูมั่นใจ และยังใช้ tool ได้ แต่คุณภาพการเลือกทางเริ่มแย่.

ตัวอย่าง:

- ยึด assumption ผิดจากช่วงก่อนหน้า
- วนแก้ bug เดิมด้วยวิธีคล้ายเดิม
- มองข้ามข้อกำหนดที่ user เพิ่งย้ำ
- อ่าน log ยาวแล้วจับ signal ผิด
- สรุปว่าเสร็จทั้งที่ test หรือ requirement ยังไม่ผ่าน

ผลคือ: dumb zone อันตรายเพราะมันดูเหมือน agent ยังทำงานได้ แต่ output เริ่มต้องใช้แรง review มากขึ้น.

## ทำไม context ใหญ่ยังไม่พอ

context window คือ "ใส่ได้เท่าไหร่" ไม่ใช่ "ใช้ได้ดีเท่าไหร่". พอ transcript ยาวขึ้น model ต้องเลือกว่าจะสนใจอะไรในกอง token ที่ใหญ่ขึ้น. ของที่เคยเป็นประโยชน์อาจกลายเป็น noise: error log เก่า, branch ที่เลิกแล้ว, plan ที่ถูกยกเลิก, หรือคำอธิบายที่ agent สร้างตอนมันกำลังหลงทาง.

ในงาน coding/debugging/design ปัญหานี้ยิ่งชัด เพราะงานไม่ได้ถามแค่ว่า "ข้อมูลอยู่ตรงไหน" แต่ถามว่า "ข้อมูลไหนควรเชื่อ" และ "ทางไหนควรทิ้ง". ถ้า context มีทางผิดเยอะ model จะโดนลากกลับไปทางเดิมง่าย.

ได้อะไร: โมเดลที่รองรับ 1M tokens อาจยังเข้า dumb zone ก่อนเต็ม window ถ้างานต้องใช้ judgement หนักและ transcript มี noise เยอะ.

## Pattern: rewind แล้ว compact

Matt เสนอวิธีทดสอบแบบง่าย:

1. ปล่อยให้ agent ทำพลาด
2. `/rewind` กลับไปก่อนจุดพลาด
3. `/compact` ถ้าอยู่ตรงจุดที่สรุป state ได้
4. ให้ agent ทำใหม่

ถ้ารอบใหม่ดีขึ้น แปลว่า failure ส่วนหนึ่งไม่ได้มาจาก model "โง่ถาวร" แต่มาจาก active context ที่ปนเปื้อน. `/rewind` ตัด trajectory ผิดออก. `/compact` เปลี่ยน transcript ที่ยาวเป็น state สั้นที่ใช้งานต่อได้.

ผลคือ: เราไม่ได้เพิ่ม intelligence ให้ model แต่ลดแรงเสียดทานที่ context สร้างให้มัน.

## Phase boundary สำคัญกว่า compact บ่อย

Compaction ที่ดีควรทำตอนจบเฟส ไม่ใช่กลางความสับสน. หลัง research, หลังตัดสินใจ, หลัง debug เจอสาเหตุแล้ว, หรือก่อน handoff ไป session ใหม่ คือจุดที่ดี.

ถ้า compact ตอนยังไม่รู้ว่าอะไรสำคัญ summary จะบันทึกของผิด. Agent ตัวถัดไปจะได้ state ที่ดูเรียบร้อยแต่ขาดเหตุผลว่าทำไมบางทางถูกทิ้ง.

ได้อะไร: `/compact` ไม่ใช่ปุ่มล้างความรกแบบปลอดภัยเสมอไป. มันเป็นการย่อความจำ และการย่อความจำผิดจังหวะทำให้ลืมของสำคัญได้.

## ทางแก้ที่ทนกว่า transcript ยาว

วิธีแก้ระยะยาวคืออย่าให้ transcript เป็น memory หลักของงาน.

- เก็บข้อสรุปในไฟล์ decision หรือ issue
- ให้ test และ lint เป็น evidence แทนคำบอกเล่าของ agent
- ใช้ [[agent-handoff-documents|handoff document]] เมื่อเปิด session ใหม่
- ใช้ subagent สำหรับงานที่ต้องการแค่ผลสรุป
- ออกแบบ [[coding-harness|harness]] ให้ offload tool output ยาวออกจาก context
- ใช้ [[agent-memory-types|episodic/procedural memory]] เมื่ออยากให้ agent เรียนรู้ข้าม session

ผลคือ: เริ่มใหม่ได้บ่อยขึ้นโดยไม่เสีย progress จริง. Agent ไม่ต้องแบก transcript ยาวเพื่อจำสิ่งที่ระบบควรเก็บไว้เอง.

## See also

- [[matt-pocock-dumb-zone-compaction]]
- [[context-rot]]
- [[compaction]]
- [[claude-code-session-management]]
- [[agent-handoff-documents]]
- [[coding-harness]]
- [[agent-memory-types]]
- [[durable-execution]]
