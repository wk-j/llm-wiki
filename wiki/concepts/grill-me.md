---
title: Grill Me
type: concept
tags: [ai-skill, planning, alignment, pocock]
created: 2026-05-09
updated: 2026-07-12
sources: [matt-pocock-software-fundamentals.md, "New Skills! handoff, prototype, review and writing-*  Skills Changelog.md", "Matt Pocock’s Agentic Engineering Workflow (just copy him).md", a-field-guide-to-fable-finding-your-unknowns.md, wayfinder-skill.md, new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets.md]
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

## grill me คือ procedure ไม่ใช่ ability

ในพอดแคสต์กับ [[david-ondrej|David Ondrej]] (2026-06-19) Matt ยก grill me เป็นตัวอย่างของ **procedure** — skill ที่ user สั่งเอง (ดู [[skill-procedures-vs-abilities]]) — ไม่ใช่ ability ที่ model หยิบใช้เอง. เขาเน้นว่ามันสั้นแค่ ~5 ประโยคแต่ "unreasonably effective" และเขาใช้มันแทน plan mode มาตลอด: "interview me, let's reach a shared understanding" ก่อนเริ่มเขียนโค้ดจริง. นี่คือขั้น scope งานก่อนส่งเข้า [[afk-agents|AFK]]

David เสริมเวอร์ชันของตัวเอง: แทนที่จะสั่ง "one-shot this app" ให้บอก vision แล้วสั่ง "list out the 10 most consequential decisions... interview me until you understand 98%"

## หลักฐานอิสระจากทีม Claude Code

[[thariq-shihipar|Thariq Shihipar]] (ทีม Claude Code) ใช้ pattern เดียวกันใน [[field-guide-to-fable-finding-unknowns|A Field Guide to Fable]] โดยเรียกว่า "Interviews" — หลัง brainstorm แล้วยังเหลือความคลุมเครือ ให้ Claude สัมภาษณ์กลับ prompt ของเขา: "Interview me one question at a time about anything ambiguous, prioritize questions where my answer would change the architecture."

จุดที่เพิ่มจากมุมของ Pocock คือเกณฑ์จัดลำดับ: ถามเรื่องที่คำตอบ *เปลี่ยน architecture* ก่อน เพราะนั่นคือ [[unknowns-matrix|unknown]] ที่แพงที่สุดถ้าไปเจอทีหลัง — สองแหล่งอิสระ (educator ภายนอก + คนในทีมผู้สร้างเครื่องมือ) มาบรรจบที่วิธีเดียวกัน ทำให้ pattern นี้น่าเชื่อขึ้น

## v1.1: confirmation gate และ facts vs decisions

[[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets|Skills v1.1]] เพิ่ม boundary ให้ grilling ชัดขึ้น. Agent ควรสำรวจ codebase เพื่อหา **facts** เอง แต่ **decisions** ต้องถามผู้ใช้. ถ้า agent ตอบ decision แทนคน เท่ากับมัน “grill ตัวเอง” และเปลี่ยน best guess เป็น intent โดยไม่มีเจ้าของยืนยัน.

ตอนจบยังมี confirmation gate: ห้าม enact plan จนผู้ใช้ยืนยันว่า shared understanding ตรงกัน. Gate นี้แก้ failure mode ที่ session ถามครบแล้วไหลไป implementation ทันที.

**ผลคือ:** skill แยกงานค้นข้อมูลออกจากงานใช้วิจารณญาณ และรักษาคนไว้ตรง decision boundary.

## ดูเพิ่ม
- [[matt-pocock]]
- [[field-guide-to-fable-finding-unknowns]]
- [[unknowns-matrix]]
- [[matt-pocock-agentic-workflow]]
- [[david-ondrej]]
- [[skill-procedures-vs-abilities]]
- [[afk-agents]]
- [[agentic-engineering]]
- [[alignment-bottleneck]]
- [[agent-handoff-documents]]
- [[throwaway-prototyping]]
- [[wayfinding]]
- [[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets]]
