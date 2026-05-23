---
title: Matt Pocock
type: entity
tags: [developer, typescript, ai, automation]
created: 2026-04-25
updated: 2026-05-12
sources: [matt-pocock-software-fundamentals.md, "New Skills! handoff, prototype, review and writing-*  Skills Changelog.md"]
---

# Matt Pocock

**Role:** Developer Advocate, TypeScript expert, และ AI automation builder.
**Twitter:** [@mattpocockuk](https://twitter.com/mattpocockuk)

เป็นที่รู้จักจากหลักสูตร "Total TypeScript" และการสร้างเวิร์กโฟลว์การพัฒนาซอฟต์แวร์ด้วย AI (Agentic Software Development) ในปี 2026 เขาได้นำเสนอแนวคิดการพัฒนาที่ใช้ [[claude-code]] ร่วมกับ [[sandcastle]] เพื่อจัดการ [[pr-dependency-dag]] สำหรับการทำงานแบบขนาน

## มุมมองต่อ AI Coding
Pocock เชื่อว่า **"Software Fundamentals Matter More Than Ever"** (พื้นฐานซอฟต์แวร์สำคัญกว่าที่เคย) เพราะแม้ AI จะเขียนโค้ดเก่ง แต่ถ้าขาดการออกแบบที่ดี โค้ดจะกลายเป็นขยะ (garbage) ได้เร็วขึ้น

- **Tactical Sergeant**: มอง AI เป็น "สิบเอก" ที่คอยคุมการรบหน้างาน (tactical level) เขียนโค้ดตามสั่ง
- **Strategist**: มนุษย์ต้องเป็น "นักยุทธศาสตร์" (strategic level) ที่มองภาพรวมของระบบและโครงสร้าง

## ผลงานและทักษะที่นำเสนอ
- **[[grill-me]]**: Skill ที่ทำให้ AI ตั้งคำถามกับผู้ใช้จนกว่าจะเข้าใจ "Shared Design Concept" ตรงกัน
- **[[agent-handoff-documents|/handoff]]**: Skill สำหรับเขียน handoff document ให้ agent session ใหม่รับงานต่อได้ โดยเก็บทั้ง context, intent, และ skill ที่ควรใช้ต่อ
- **[[throwaway-prototyping|/prototype]]**: Skill สำหรับสร้าง prototype แบบทิ้งได้ ทั้ง UI และ logic เพื่อทดลอง decision ก่อนให้ implementation agent ทำของจริง
- **[[dual-axis-code-review|/review]]**: แนวทาง review skill ที่แยกการตรวจเป็นสองแกน คือ standards ของ repo กับ fidelity ต่อ spec
- **[[writing-fragments|writing-*]]**: ชุด writing skill ที่เริ่มจาก fragments ไปเป็น beats แล้วค่อย shape งานเขียน
- **[[ubiquitous-language]]**: การใช้ภาษาเดียวกันระหว่างคนกับ AI (อิงจาก DDD) เพื่อลดความสับสน
- **Deep Modules**: การสนับสนุนให้สร้าง module ที่มี "interface เรียบง่ายแต่ข้างในซับซ้อน" เพื่อให้ง่ายต่อการทดสอบและ delegating งานให้ AI

## ดูเพิ่ม
- [[matt-pocock-software-fundamentals]]
- [[new-skills-handoff-prototype-review-writing]]
- [[coding-harness]]
- [[pr-dependency-dag]]
- [[sandcastle]]
- [[john-ousterhout]]
