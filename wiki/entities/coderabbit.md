---
title: CodeRabbit
type: entity
tags: [ai, code-review, developer-tools]
created: 2026-06-16
updated: 2026-06-16
sources: [Agentic Code Review.md]
---

# CodeRabbit

**CodeRabbit** คือ AI code review tool ที่ใช้ตรวจ pull request อัตโนมัติ. ใน [[agentic-code-review|Agentic Code Review]] ของ [[addy-osmani|Addy Osmani]] มันเป็นตัวอย่างของ reviewer แบบ inferential sensor: อ่าน diff แล้วชี้ bug, correctness issue, readability issue, และบาง workflow มี one-click fix.

บทความอ้างรายงานของ CodeRabbit ที่ศึกษา open-source PR 470 รายการ (320 AI-coauthored, 150 human-only) แล้วพบว่า AI-written code มี issue ประมาณ 1.7 เท่าของ human-only PR. Addy เตือนด้วยว่าต้องอ่านแบบรู้ว่า CodeRabbit เป็น vendor ในตลาดนี้ แต่ pattern รวมยังสอดคล้องกับข้อมูลแหล่งอื่น.

## ที่ทางในวิกินี้

CodeRabbit สำคัญในฐานะเครื่องมือหนึ่งในระบบ [[agentic-code-review|agentic code review]] ไม่ใช่คำตอบเดี่ยว. บทเรียนจาก Addy คืออย่าหา reviewer ตัวเดียวที่ดีที่สุด. งานเสี่ยงควรใช้ reviewer ที่ต่าง character กัน เพื่อให้ blind spot ไม่ซ้อนกันทั้งหมด.

## See also

- [[agentic-code-review]]
- [[greptile]]
- [[harness-guides-sensors]]
- [[orchestration-tax]]
