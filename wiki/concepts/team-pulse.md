---
title: Team Pulse
type: concept
tags: [collaboration, agents, context]
created: 2026-04-28
updated: 2026-04-28
sources: [maggie-appleton-collaborative-ai-engineering.md]
---

# Team Pulse / จังหวะชีพจรของทีม

**Team Pulse** คือแนวคิดการใช้ AI Agent เพื่อช่วยให้สมาชิกในทีมรับรู้สถานะและความคืบหน้าของงานที่เกิดขึ้นในวงกว้าง โดยไม่ต้องจมกองข้อมูล (Information Overload)

## ทำไมถึงสำคัญ?

ในสภาพแวดล้อมที่ใช้ Agent ทำงาน ความเร็วในการเปลี่ยนแปลงจะสูงมาก จนเป็นไปไม่ได้ที่มนุษย์จะติดตามทุกอย่าง (เช่น การอ่าน PR 5-10 ตัวต่อวัน) Team Pulse ทำหน้าที่เป็น "ตัวกรอง" และ "ตัวสรุป" เพื่อให้ทุกคนยังรักษา [[alignment-bottleneck|Alignment]] ไว้ได้

## กลไกการทำงาน (ตัวอย่างจาก [[ace]])

- **Active Summarization**: Agent คอยอ่านการพูดคุยและประวัติการแก้ code ใน session ต่างๆ แล้วสรุปเป็นประเด็นสั้นๆ (เช่น "Nate กำลังแก้เรื่อง Lobby channel")
- **Context Injection**: เมื่อสมาชิกทีมคนหนึ่งเข้าไปดูงานของอีกคน Agent จะช่วยบรีฟข้อมูลให้ทันทีว่า "งานนี้มาถึงไหนแล้ว และติดปัญหาอะไรอยู่"
- **Proactive Notification**: แจ้งเตือนเมื่อมีการตัดสินใจสำคัญ หรือเมื่อมีคนกำลังแก้ไข code ในส่วนที่เราเคยดูแล

## ดูเพิ่ม

- [[ace]]
- [[collaborative-ai-engineering]]
- [[just-in-time-context]] — แนวคิดการให้ข้อมูลเฉพาะเมื่อจำเป็น
