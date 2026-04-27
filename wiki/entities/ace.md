---
title: ACE
type: entity
tags: [product, tool, agents, collaboration, github-next]
created: 2026-04-28
updated: 2026-04-28
sources: [maggie-appleton-collaborative-ai-engineering.md]
---

# ACE (Agent Collaboration Environment) / เอซ

**ACE** (Agent Collaboration Environment) เป็นเครื่องมือต้นแบบ (Research Prototype) จาก [[github-next|GitHub Next]] ที่ออกแบบมาเพื่อแก้ปัญหาการทำงานร่วมกันระหว่างมนุษย์และ AI Agent ในระดับทีม

## ความสามารถหลัก (Features)

- **Multiplayer Chat**: หน้าตาคล้าย Slack ที่ให้คนและ Agent มาคุยงานและแก้ไข code ไปพร้อมๆ กันในช่องทางเดียว
- **Sandboxed MicroVMs**: ทุกการทำงานรันบน VM ขนาดเล็กใน cloud แยกตาม session (git branch) ทำให้ทีมสามารถสลับไปดูงานของเพื่อนได้ทันทีโดยไม่ต้องตั้งค่าเครื่องใหม่
- **Collaborative Planning**: มีโหมดสำหรับการร่างแผนงาน (Plan Mode) ที่ทุกคนสามารถช่วยกันแก้ได้ก่อนจะสั่งให้ Agent เริ่มเขียน code จริง
- **Team Pulse**: ระบบสรุปกิจกรรมของทีมโดยใช้ AI เพื่อลดปัญหาข้อมูลท่วมท้น (Information Overload) จากการที่ Agent ทำงานเร็วเกินไป
- **Real-time Editing**: รองรับการแก้ไข code ร่วมกันแบบสดๆ คล้าย VS Code Live Share แต่รันอยู่บนโครงสร้างพื้นฐานเดียวกันกับ Agent

## ทำไมต้องมี ACE?

[[maggie-appleton]] ผู้นำโปรเจกต์ระบุว่า เครื่องมือปัจจุบัน (Terminal, Slack, PR) กระจัดกระจายเกินไป ทำให้เมื่อเราใช้ Agent ที่ทำงานเร็วมาก ทีมจะเสีย "Alignment" (ความเข้าใจที่ตรงกัน) ACE จึงพยายามดึงการวางแผน (Planning), การสื่อสาร (Communication), และการสร้าง (Building) เข้ามาไว้ใต้หลังคาเดียวกัน

## ดูเพิ่ม

- [[github-next]]
- [[collaborative-ai-engineering]]
- [[alignment-bottleneck]]
