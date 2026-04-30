---
title: Agentic Engineering
type: concept
tags: [ai, engineering, agents, automation]
created: 2026-04-30
updated: 2026-04-30
sources: [Andrej Karpathy From Vibe Coding to Agentic Engineering.md]
---

# Agentic Engineering / วิศวกรรมเชิงเอเจนท์

**Agentic Engineering** คือระเบียบวินัยทางวิศวกรรม (Engineering Discipline) ที่เน้นการใช้ AI Agents ในการทำงานที่ซับซ้อนโดยยังคงรักษามาตรฐานคุณภาพ (Quality Bar) และความปลอดภัยของซอฟต์แวร์ระดับมืออาชีพไว้ได้ ซึ่งเป็นขั้นที่พัฒนาต่อยอดมาจาก [[vibe-coding]]

## แก่นความคิด
ในขณะที่ [[vibe-coding]] เน้นการ "ยกระดับพื้นฐาน" (Raising the floor) ให้ทุกคนเข้าถึงการสร้างซอฟต์แวร์ได้ **Agentic Engineering** เน้นการ "ยกระดับเพดาน" (Raising the ceiling) ให้กับวิศวกรมืออาชีพ เพื่อให้สามารถทำงานได้เร็วขึ้น 10x-100x โดยไม่เสียการควบคุม

- **จาก Implementer สู่ Director**: มนุษย์ไม่ได้เลิกเขียนโค้ด แต่เปลี่ยนบทบาทไปควบคุม "ทิศทาง" (Taste & Judgment) และการออกแบบระดับสูง
- **การจัดการ Jagged Intelligence**: เข้าใจว่า AI มีความสามารถแบบฟันปลา ([[jagged-intelligence]]) คือเก่งงานยากแต่พลาดงานง่าย จึงต้องมีระบบตรวจสอบ (Verification) ที่รัดกุม

## องค์ประกอบสำคัญ
1. **Spec & Planning**: การเขียนรายละเอียดและแผนงานที่ชัดเจนเพื่อให้ Agent นำไปปฏิบัติ (Execution)
2. **Verification Loop**: การใช้ระบบ Automated Tests และการตรวจสอบด้วยมนุษย์เพื่อให้มั่นใจว่า Agent ไม่ได้สร้างช่องโหว่หรือ Bug
3. **Coordination**: การจัดการ Agent หลายตัว ([[agent-swarm]]) ให้ทำงานร่วมกันในโปรเจกต์ขนาดใหญ่
4. **Agent-Native Workflow**: การปรับเปลี่ยนกระบวนการทำงานให้เอื้อต่อการทำงานของ AI (เช่น การเตรียม docs และ infra ให้ AI อ่านง่าย)

## Payoff / ผลคือ
วิศวกรสามารถขยายขอบเขตการทำงาน (Scale) ได้มหาศาล โดยหนึ่งคนสามารถคุมงานที่เคยต้องใช้ทีมงานขนาดใหญ่ได้ ในขณะที่ยังคงรักษาความสมบูรณ์แบบ (Integrity) ของระบบไว้ได้

## ดูเพิ่ม
- [[vibe-coding]]
- [[software-3-0]]
- [[jagged-intelligence]]
- [[agent-swarm]]
- [[andrej-karpathy]]
