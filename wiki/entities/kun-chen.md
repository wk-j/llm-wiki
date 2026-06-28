---
title: Kun Chen
type: entity
tags: [ai, agents, software-engineering, solo-builder]
created: 2026-06-16
updated: 2026-06-16
sources: [Agentic Code Review.md]
---

# Kun Chen

**Kun Chen** คืออดีต Meta L8 engineer ที่ [[addy-osmani|Addy Osmani]] ยกเป็นตัวอย่างสุดขั้วใน [[agentic-code-review|Agentic Code Review]]: solo builder ที่ใช้ agent 20-30 ตัวและ ship ประมาณ 40 PR ต่อวัน โดยแทบไม่ review code แบบ line-by-line.

สิ่งที่น่าสนใจไม่ใช่ "เลิก review แล้วรอด" แต่คือเขาย้ายงานมนุษย์ไปอยู่ก่อนโค้ดเกิด. เขาเขียน plan ละเอียดมาก ให้ agent ทำงานหลายชั่วโมงตาม plan และใช้ automated gate ชื่อ No Mistakes ตรวจงานก่อน merge. เขายังอยู่บน escalation เมื่อ agent ติด.

Addy ใช้ Kun เป็นตัวอย่างของบริบทเฉพาะ: solo builder, ไม่มีทีมใหญ่, ไม่มี legacy system หนัก, และ blast radius คนละแบบกับ enterprise. Copy workflow นี้ไปใส่ระบบใหญ่โดยไม่ปรับ risk tier จะกลายเป็นปัญหา review capacity ทันที.

## See also

- [[agentic-code-review]]
- [[loop-engineering]]
- [[orchestration-tax]]
- [[cognitive-surrender]]
