---
title: Collaborative AI Engineering
type: concept
tags: [ai, engineering, collaboration, team, agents]
created: 2026-04-28
updated: 2026-04-28
sources: [maggie-appleton-collaborative-ai-engineering.md]
---

# Collaborative AI Engineering / วิศวกรรม AI แบบร่วมมือกัน

**Collaborative AI Engineering** คือแนวคิดการพัฒนาซอฟต์แวร์ที่เปลี่ยนจากการใช้ AI Agent เพื่อเพิ่มผลิตภาพรายบุคคล (Individual Productivity) ไปสู่การสร้างระบบที่ Agent และมนุษย์หลายคนสามารถทำงานร่วมกันอย่างสอดประสาน

## ปัญหาของแนวทางปัจจุบัน (The Solo Story)

[[maggie-appleton]] ชี้ให้เห็นว่าเครื่องมือ AI ในปัจจุบัน (เช่น [[claude-code|Claude Code]], Terminal-based agents) มักเป็น "Single Player" ซึ่งนำไปสู่ปัญหา:
- **Duplicate Work**: ต่างคนต่างสั่ง Agent ทำงานที่ซ้ำซ้อนกัน
- **Conflicting Changes**: Agent ของแต่ละคนแก้ไข code ในจุดที่ขัดแย้งกันโดยไม่มีใครรู้
- **Coordination Debt**: หนี้จากการประสานงานที่เพิ่มขึ้นเมื่อ Agent สร้าง code ปริมาณมหาศาลออกมาเร็วเกินกว่าที่คนจะอ่านทัน

## เสาหลักของความร่วมมือ

1. **Shared Context**: ทุกคนในทีมและ Agent ต้องเห็นข้อมูลชุดเดียวกัน ตั้งแต่ประวัติการคุย ไปจนถึงสถานะของระบบ
2. **Alignment-First**: เน้นการตกลงกันว่า "จะสร้างอะไร" (Should we build) ก่อนจะเริ่ม "ลงมือสร้าง" (Implementation)
3. **Proactive Summarization**: การใช้ Agent ช่วยดึงประเด็นสำคัญจากการทำงานของคนอื่นมาสรุปให้ฟัง ([[team-pulse]]) เพื่อรักษาจังหวะการทำงานของทีม

## ดูเพิ่ม

- [[ace]] — เครื่องมือที่สร้างตามแนวคิดนี้
- [[alignment-bottleneck]] — เหตุผลที่ต้องเน้นการร่วมมือกัน
- [[vibecoded-slop]] — ผลลัพธ์ของการทำลายความร่วมมือเพื่อเน้นความเร็ว
