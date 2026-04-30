---
title: Panutat Tejasen
type: entity
tags: [person, thai, education, ai, software-engineering]
created: 2026-04-18
updated: 2026-04-30
sources: [harness-engineering-panutat.md, thclaws-announcement-panutat.md, panutat-tejasen-thclaws-positioning.md, thclaws-marketplace-panutat.md]
---

# Panutat Tejasen / ภานุทัต เตชะเสน

วิศวกรซอฟต์แวร์และผู้ประกอบการชาวไทย ผู้บุกเบิกแนวคิด **[[harness-engineering|Harness Engineering]]** และผู้สร้างโปรเจกต์ **[[thclaws]]**

## ผลงานและแนวคิดที่น่าสนใจ

### Harness Engineering (บังเหียนคุม AI)
Panutat เสนอว่าในยุคที่ AI เก่งขึ้นเรื่อยๆ จนคนตามไม่ทัน การที่คนจะไปนั่ง "รีวิว" หรือ "แนะนำ" AI แบบบรรทัดต่อบรรทัดนั้นเป็นเรื่องเสียเวลาและเป็นคอขวด
- **ทางแก้:** ให้คนเปลี่ยนหน้าที่มาเป็นผู้ออกแบบ **Harness** (บังเหียน) — คือการสร้างระบบ AI Agent ตัวอื่นๆ มาช่วยกันตรวจสอบ (Audit), ทดสอบ (Test), และควบคุม Agent หลักโดยอัตโนมัติแทนคน

### thClaws และ Open Source Governance
Panutat ให้ความสำคัญกับเรื่อง **[[open-source-governance|Governance]]** (ระบบการตัดสินใจ) มากกว่าแค่ความเปิดกว้างของ source code
- **นิยาม Open Source ปี 2026:** เขาเชื่อว่าความแตกต่างที่แท้จริงคือ "ใครเป็นคนตัดสินใจว่าจะชิปอะไร" (Who decides what to ship?)
- **thClaws Marketplace (v0.7.0):** เพิ่มระบบมาร์เก็ตเพลสสำหรับ Skills, MCP และ Plugins เพื่อรองรับการใช้งานระดับ Enterprise ที่ต้องการการควบคุมความปลอดภัยและสิทธิ์การใช้งาน (Private Marketplace)

### Host Bridge และ Agent-Generated Dashboard
เขานำเสนอแนวคิด **Host Bridge** (แรงบันดาลใจจาก Claude Cowork) ซึ่งใช้ HTML File System เพื่อรัน Webapp ใน Browser ให้สามารถอ่าน/เขียนข้อมูลในไดเรกทอรีที่ Agent ทำงานอยู่ได้
- **Payoff:** ทำให้ Agent มี Dashboard ใช้งาน และ Agent สามารถ "สร้างหน้าจอ Dashboard" ขึ้นมาเองเพื่อสื่อสารกับผู้ใช้ได้

### Product Overhang (ความเก่งที่ซ่อนอยู่)
เขาชี้ให้เห็นว่า AI model อย่าง Claude 3.5 นั้นเขียน code เก่งมาตั้งนานแล้ว แต่ไม่มีใครรู้ จนกระทั่งมีคนสร้างเครื่องมืออย่าง Claude Code ที่ยอมให้ model เข้าถึงไฟล์ได้ (filesystem access) ความเก่งนี้ถึงถูกปลดปล่อยออกมา ตรงนี้เรียกว่า **[[product-overhang|Product Overhang]]**

## ดูเพิ่ม

- [[thclaws]]
- [[harness-engineering]]
- [[product-overhang]]
- [[claude-code]]
- [[nattee-niparnan]]
- [[taste-paradox]]
