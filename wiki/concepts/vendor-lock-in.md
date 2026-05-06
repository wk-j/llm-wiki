---
title: Vendor Lock-In (AI Era)
type: concept
tags: [business, ai]
created: 2026-05-05
updated: 2026-05-05
sources: [agentic-coding-trap.md]
---

# Vendor Lock-In / การผูกขาดโดยผู้ให้บริการ (ในยุค AI)

ในยุคของ Agentic Coding คำว่า **Vendor Lock-In** ไม่ได้หมายถึงแค่การที่ระบบของเราผูกติดกับ API ของค่ายใดค่ายหนึ่งเท่านั้น แต่ยังรวมถึง **การผูกขาดทักษะส่วนบุคคลและทีมงาน (Skill Lock-in)** ด้วย

[[lars-faye]] ชี้ให้เห็นว่า เมื่อทีมพัฒนาหันไปพึ่งพา AI Agent (เช่น [[claude-code]] หรือ [[opencode]]) เป็นหลักจนกลายเป็น workflow มาตรฐาน ทักษะในการคิดแก้ปัญหาและการเขียนโค้ดแบบเดิมจะเริ่มหายไป ([[skill-atrophy]]) ผลที่ตามมาคือ เมื่อผู้ให้บริการ AI ระบบล่ม (outage) ปรับลดความสามารถของโมเดล (nerfed) หรือขึ้นราคาค่าใช้งาน ([[usage-based-billing]]) ทีมพัฒนาก็จะหยุดชะงักและไม่สามารถทำงานต่อได้ด้วยตัวเอง

การปล่อยให้ Model provider เข้ามาผูกขาด workflow การทำงาน เท่ากับว่าต้นทุนในการทำงาน (ซึ่งเคยเป็นเงินเดือนที่คงที่) จะกลายเป็นตัวแปรที่ไม่สามารถควบคุมได้ตามราคา Token

## See also

- [[usage-based-billing]]
- [[agentic-usage]]
- [[skill-atrophy]]
