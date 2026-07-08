---
title: Microsoft Azure
type: entity
tags: [cloud, microsoft, infrastructure, ai]
created: 2026-07-08
updated: 2026-07-08
sources: [claude-in-microsoft-foundry.md]
---

# Microsoft Azure

Azure คือแพลตฟอร์ม cloud ของ [[microsoft|Microsoft]] — ทั้ง compute, storage, identity, billing และ governance ที่องค์กรจำนวนมากใช้เป็นบ้านหลักอยู่แล้ว.

## บทบาทในwiki

ในwiki นี้ Azure ปรากฏในฐานะ **สภาพแวดล้อมองค์กรที่ model ไปวางไว้ให้ใช้**. [[microsoft-foundry|Microsoft Foundry]] ซึ่งเป็นแพลตฟอร์ม AI ของ Microsoft รันอยู่บน Azure.

จากประกาศ [[claude-in-microsoft-foundry|Claude in Microsoft Foundry]] (2026-06-29) องค์กรรัน inference ของ [[claude|Claude]] ในสภาพแวดล้อม Azure ของตัวเองได้ โดยใช้ Azure identity, billing, และ governance เดิม. ทางเลือก *hosted on Azure* หมายถึงให้ทุกอย่างอยู่ใต้ร่ม Azure; ลูกค้าที่มี Microsoft Enterprise Agreement ยังเอา Azure commitments มาจ่ายค่า Claude ได้ด้วย.

การที่ model ไปอยู่บน Azure ได้ คือหัวใจของ [[enterprise-model-deployment|การ deploy โมเดลระดับองค์กร]] — เข้าถึง model ผ่านคลาวด์ที่ทีมใช้อยู่แล้ว แทนที่จะต่อท่อไปหา vendor แยก.

## See also

- [[microsoft]]
- [[microsoft-foundry]]
- [[claude-in-microsoft-foundry]]
- [[enterprise-model-deployment]]
- [[anthropic]]
