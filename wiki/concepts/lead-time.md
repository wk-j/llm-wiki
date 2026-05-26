---
title: Lead Time
type: concept
tags: [metrics, agile, software-delivery]
created: 2026-04-28
updated: 2026-05-25
sources: [jeeraphan-lairat-ai-coding-speed.md, fundamental-productivity-ai-world.md]
---

# Lead Time / ระยะเวลาส่งมอบงาน

ระยะเวลาทั้งหมดที่งานเดินทางจาก "จุดเริ่มต้น" (เช่น ลูกค้าสั่งงาน หรือเริ่ม Sprint) ไปจนถึง "จุดสิ้นสุด" (งานถึงมือลูกค้า)

ในยุค AI ที่ Coding เร็วขึ้น:
- **Focus Shift:** เราต้องเลิกโฟกัสที่ "Coding Time" แล้วหันมาดู "Lead Time" แทน
- **Wait Time:** สาเหตุหลักที่ Lead Time ยาวนานมักไม่ใช่เพราะเขียนโค้ดช้า แต่เพราะงาน "นอนรอ" อยู่ตามจุดต่างๆ ใน pipeline
- **Visibility:** การวัดผลที่แม่นยำต้องแยกแยะระหว่างเวลาที่ทำงานจริง (Processing Time) กับเวลาที่รอคอย (Waiting Time)
- **Interaction:** [[interaction-productivity|Productivity ที่เกิดจากการส่งต่อ]] ช่วยอธิบายว่า lead time มักติดตรงจังหวะที่คนถัดไปต้อง accept งาน ไม่ใช่ตรงการผลิต artifact อย่างเดียว

## กลยุทธ์การลด Lead Time
- [[shift-left-testing]] (เตรียมเทสล่วงหน้า)
- [[limit-wip]] (จำกัดงานไม่ให้ล้น)
- Break down tasks ให้เล็กลง (1-2 วันจบ) เพื่อให้ Flow ลื่นไหลขึ้น

## See also
- [[theory-of-constraints]]
- [[local-optimization-trap]]
- [[acceptance-bottleneck]]
