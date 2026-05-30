---
title: Local Optimization Trap
type: concept
tags: [efficiency, software-engineering, ai-productivity]
created: 2026-04-28
updated: 2026-05-25
sources: [jeeraphan-lairat-ai-coding-speed.md, fundamental-productivity-ai-world.md]
---

# Local Optimization Trap / กับดักของการเร่งสปีดผิดจุด

สภาวะที่องค์กรพยายามเพิ่มประสิทธิภาพในจุดที่ "เห็นชัด" หรือ "ทำง่าย" (เช่น การใช้ AI ช่วยเขียนโค้ด) แต่จุดนั้นไม่ใช่ [[theory-of-constraints|คอขวด (Bottleneck)]] ของระบบ

## ทำไมถึงเป็นกับดัก?
- **หลอกตา:** เรารู้สึกว่าเราทำงานเร็วขึ้น (โค้ดเสร็จใน 30 นาทีแทนที่จะเป็น 3 วัน) แต่ [[lead-time]] รวมกลับเท่าเดิม
- **สร้างปัญหาใหม่:** การผลิตโค้ดออกมาเร็วเกินไปโดยไม่มีระบบ Review หรือ Testing ที่รองรับ จะทำให้เกิด [[vibecoded-slop|ขยะ]] และงานค้างสะสม (Inventory) ในระบบมากขึ้น
- **เสียทรัพยากร:** พลังงานและเงินทุนถูกใช้ไปกับการแก้จุดที่ไม่ใช่ปัญหาหลัก

## ตัวอย่าง
- ทีมพัฒนาใช้ AI เขียนโค้ดเร็วขึ้น 10 เท่า แต่ต้องรอคนมาเทสนาน 3 วันเท่าเดิม ผลคือ Productivity รวมขององค์กรเท่าเดิม แต่ความเครียดของฝ่าย Testing เพิ่มขึ้น 10 เท่า
- ทีมใช้ AI สร้าง requirement หรือ design spec ได้เร็วมาก แต่คนถัดไปยังต้องอ่านและยอมรับงานเอง จุดคอขวดจึงย้ายไปที่ [[acceptance-bottleneck|Acceptance Bottleneck]] ตามเลนส์ของ [[interaction-productivity|Interaction Productivity]]
- เปิด AI agent 20 ตัวขนานกัน รู้สึกว่าผลิตเยอะ แต่ judgement ของมนุษย์ (review + merge) ยังเป็น serial ตัวเดียว — เปิด agent คือ optimize จุดที่ไม่ใช่คอขวด งานเลยกองหน้าขั้น review ดู [[orchestration-tax|Orchestration Tax]] ของ [[addy-osmani|Addy Osmani]]

## See also
- [[theory-of-constraints]]
- [[lead-time]]
- [[interaction-productivity]]
- [[acceptance-bottleneck]]
- [[orchestration-tax]]
- [[process-drag]]
- [[software-after-software]]
