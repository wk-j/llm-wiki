---
title: Frontier Camp
type: concept
tags: [ai, organization, strategy, corporate, r-and-d]
created: 2026-05-27
updated: 2026-05-27
sources: [software-after-software.md]
---

# Frontier Camp / ค่ายแนวหน้าในองค์กร

**Frontier Camp** คือทีมเล็ก autonomous ที่บริษัทใหญ่ตั้งขึ้นมาเพื่อ **เรียนรู้วิธีทำงานใหม่ในยุค AI** ไม่ใช่เพื่อเอา AI มาใส่กับวิธีทำงานเดิม

แนวคิดนี้มาจาก [[software-after-software|Software After Software]] ของ [[thorsten-ball|Thorsten Ball]] ข้อ 10 และ [[amp-labs|Amp Labs]] เป็นตัวอย่างของ frontier camp ที่ Ball position ให้ดู

## คีย์ของแนวคิด

> "Every serious institution needs a camp at the frontier."

> "They cannot learn the future through committee."

> "Its purpose is not to add AI to the old way of working. Its purpose is to discover the new way of working and pull the corporation toward it."

## ลักษณะของทีม Frontier Camp

ตามที่ Ball ระบุ:

- **เล็ก** — autonomous, ไม่ติดกับ approval chain เดิม
- **สร้างรอบ model** — ไม่ใช่ทีม AI ที่ถูกแปะเข้ากับโครง org เดิม (ดู [[reorganize-around-models]])
- **อยู่ใกล้กับ "real systems, real data, real constraints, and real consequences"** — ไม่ใช่ sandbox เปล่า
- **output สองชั้น**:
  1. ซอฟต์แวร์ (เครื่องมือ, prototype, system ใหม่)
  2. **คนและ practice** — สิ่งที่ใหญ่กว่าซอฟต์แวร์เพราะมันคือสิ่งที่จะดึงบริษัทตามไป

## ทำไมเรียนรู้ผ่าน committee ไม่ได้

Ball ชี้ว่าการเปลี่ยนแปลงครั้งนี้ไม่ใช่ topic ที่จะมีคำตอบจาก research deck หรือ vendor pitch:

- model เปลี่ยนทุก 8 สัปดาห์ — committee meeting ตามไม่ทัน
- pattern ที่ใช้ได้กับองค์กรหนึ่งอาจไม่ work กับอีกองค์กร — ต้องลองในระบบจริง
- "new way of working" ไม่ใช่ best practice ที่ปรึกษาทำได้ — ต้องค้นหาจาก context เฉพาะของบริษัทตัวเอง

ผลคือ committee/consulting แบบเดิมจะให้คำตอบที่ "ปลอดภัยทางกระดาษ" แต่ใช้ไม่ได้จริง

ได้อะไร: ทีมต้องลงไปแตะ system จริงด้วยตัวเอง

## เทียบกับ "AI team" / "Innovation lab" แบบเดิม

หลายบริษัทเคยมีทีม Innovation Lab, Digital Transformation Office, หรือ AI Center of Excellence แล้ว Frontier Camp ของ Ball ต่างจากกลุ่มนี้ตรง:

| Innovation Lab แบบเดิม | Frontier Camp |
|---|---|
| ห่างจาก operation จริง | ใกล้กับ real systems, real data, real consequences |
| output = report, recommendation | output = ซอฟต์แวร์ + คน + practice |
| งานหลักคือทำ pilot/PoC | งานหลักคือ "discover new way of working" |
| ส่ง output ให้ business unit ไปใช้ | "pull the corporation toward it" — เป็นแรงดึงเอง |

ความต่างที่ตามมาในระดับ org คือ: Innovation Lab ทำงาน parallel กับ business; Frontier Camp ทำงานเพื่อ **เปลี่ยน business**

## ตัวอย่าง

[[amp-labs|Amp Labs]] (ภายใน Sourcegraph) คือ frontier camp ที่ Ball ใช้เป็นตัวอย่างของตัวเอง

## ปัญหาที่ Ball ไม่พูดถึง

- **Frontier camp ที่ขาด authority** — ถ้าทีมเล็กไม่มีอำนาจ "pull the corporation" จริง ก็จะกลายเป็น lab โดดเดี่ยวที่ไม่มีใครฟัง
- **Frontier camp ที่ขาด credibility** — สมาชิกของทีมต้องมาจาก senior ที่บริษัทเชื่อ ไม่ใช่ทีม junior ที่เก่ง AI อย่างเดียว
- **ความเป็นเจ้าของระบบจริง** — "อยู่ใกล้ real systems" ในทางปฏิบัติแปลว่าทีมต้องมี production access ซึ่งทีมเล็กที่ autonomous มักไม่ได้รับใน enterprise

[[aaron-levie|Aaron Levie]] เสนอ frame คล้าย ๆ กันใน [[agent-enablement-role]] — บริษัท non-tech ต้องมี role พิเศษมาจัดการเรื่องนี้ ไม่ใช่ side project ของอาสาสมัคร

## ความสัมพันธ์กับแนวคิดอื่น

- [[reorganize-around-models]] — frontier camp คือ implementation pattern หนึ่งของแนวคิดนี้
- [[amp-labs]] — ตัวอย่างของ frontier camp
- [[agent-enablement-role]] — บทบาทใน enterprise ที่จับงานคล้ายกัน
- [[process-drag]] — เหตุผลที่ต้องมี frontier camp: process เก่าทำให้บริษัทตามไม่ทัน
- [[engineering-role-shift]] — ทักษะของคนใน frontier camp

## See also

- [[software-after-software]]
- [[amp-labs]]
- [[reorganize-around-models]]
- [[process-drag]]
- [[value-migration-from-code]]
- [[engineering-role-shift]]
- [[agent-enablement-role]]
