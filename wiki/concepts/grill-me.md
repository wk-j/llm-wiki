---
title: Grill Me
type: concept
tags: [ai-skill, planning, alignment, pocock]
created: 2026-05-09
updated: 2026-05-12
sources: [matt-pocock-software-fundamentals.md, "New Skills! handoff, prototype, review and writing-*  Skills Changelog.md"]
---

# Grill Me / ทักษะการตั้งคำถามไล่บี้

**Grill Me** เป็นทักษะ (skill) หรือ prompt pattern ที่ [[matt-pocock]] คิดค้นขึ้นเพื่อแก้ปัญหา "AI ทำงานไม่ตรงใจ" โดยเปลี่ยนบทบาทของ AI จาก "ผู้รับคำสั่ง" มาเป็น "ผู้สอบสวน" (Investigator/Adversary)

## แก่นความคิด
แทนที่จะให้ AI เริ่มเขียนโค้ดทันที (Eager planning) เราสั่งให้ AI "สัมภาษณ์เราอย่างไม่ลดละ" (Interview me relentlessly) จนกว่าจะถึงจุดที่เรียกว่า **Shared Design Concept** หรือความเข้าใจในการออกแบบที่ตรงกัน 100%

- **เป้าหมาย**: เพื่อสร้าง "Design Concept" ซึ่งเป็นไอเดียที่ล่องลอยอยู่ระหว่างคนกับ AI ก่อนที่จะเริ่มลงมือสร้าง asset หรือเขียนโค้ด
- **กลไก**: AI จะไล่ถามตาม "Design Tree" (กิ่งก้านของการตัดสินใจ) เพื่อเคลียร์ข้อสงสัยในทุกมิติ

## ทำไมถึงสำคัญ
1. **ลดการแก้โค้ดซ้ำซ้อน**: การเสียเวลาคุยให้จบก่อน (Planning phase) ดีกว่าการให้ AI เขียนโค้ดผิดๆ แล้วต้องมาตามแก้ทีหลัง
2. **สร้าง Shared understanding**: ทำให้ AI รู้จัก context และขอบเขตของปัญหาจริงๆ ไม่ใช่แค่เดาจากคำสั่งสั้นๆ
3. **Better than default plan mode**: Pocock เชื่อว่าวิธีนี้ดีกว่า default plan mode ในเครื่องมืออย่าง [[claude-code]] เพราะลดความใจร้อนของ AI (Eagerness)

## วิธีใช้ (Prompt snippet)
> "Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one by one."

## ผลคือ (Payoff)
การพูดคุยที่เกิดขึ้นสามารถนำไปสรุปเป็น PRD (Product Requirements Document) หรือแตกเป็น GitHub Issues ให้ Agent ตัวอื่นไปทำงานต่อได้อย่างแม่นยำ

ใน changelog เรื่อง `/handoff` และ `/prototype`, Pocock เพิ่ม workflow ต่อจาก Grill Me: ถ้า grilling session ยาวแล้วเจอคำถามที่ต้องพิสูจน์ด้วย code ให้สร้าง [[agent-handoff-documents|handoff document]] ไปเปิด agent ใหม่เพื่อทำ [[throwaway-prototyping|prototype]] แล้วค่อยนำผลกลับมาคุยต่อ

## ดูเพิ่ม
- [[matt-pocock]]
- [[agentic-engineering]]
- [[alignment-bottleneck]]
- [[agent-handoff-documents]]
- [[throwaway-prototyping]]
