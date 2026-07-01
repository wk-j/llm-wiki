---
title: Matt Pocock
type: entity
tags: [developer, typescript, ai, automation]
created: 2026-04-25
updated: 2026-06-29
sources: [matt-pocock-software-fundamentals.md, "New Skills! handoff, prototype, review and writing-*  Skills Changelog.md", "Matt Pocock’s Agentic Engineering Workflow (just copy him).md", matt-pocock-dumb-zone-compaction.md]
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
- **[[teach-skill|teach skill]]**: stateful skill ที่เปลี่ยน agent เป็นครูส่วนตัว สร้างหลักสูตรสด ๆ — เริ่มจาก `mission.md`, ทำบทเรียนเป็น HTML, มี quiz, อิงหลัก [[knowledge-skills-wisdom]] + zone of proximal development
- **[[grill-me]]**: Skill ที่ทำให้ AI ตั้งคำถามกับผู้ใช้จนกว่าจะเข้าใจ "Shared Design Concept" ตรงกัน
- **[[agent-handoff-documents|/handoff]]**: Skill สำหรับเขียน handoff document ให้ agent session ใหม่รับงานต่อได้ โดยเก็บทั้ง context, intent, และ skill ที่ควรใช้ต่อ
- **[[throwaway-prototyping|/prototype]]**: Skill สำหรับสร้าง prototype แบบทิ้งได้ ทั้ง UI และ logic เพื่อทดลอง decision ก่อนให้ implementation agent ทำของจริง
- **[[dual-axis-code-review|/review]]**: แนวทาง review skill ที่แยกการตรวจเป็นสองแกน คือ standards ของ repo กับ fidelity ต่อ spec
- **[[writing-fragments|writing-*]]**: ชุด writing skill ที่เริ่มจาก fragments ไปเป็น beats แล้วค่อย shape งานเขียน
- **[[ubiquitous-language]]**: การใช้ภาษาเดียวกันระหว่างคนกับ AI (อิงจาก DDD) เพื่อลดความสับสน
- **Deep Modules**: การสนับสนุนให้สร้าง module ที่มี "interface เรียบง่ายแต่ข้างในซับซ้อน" เพื่อให้ง่ายต่อการทดสอบและ delegating งานให้ AI

## เวิร์กโฟลว์ปัจจุบัน (พอดแคสต์กับ David Ondrej, 2026-06)

ในพอดแคสต์ [[matt-pocock-agentic-workflow]] กับ [[david-ondrej|David Ondrej]] Pocock สรุปวิธีทำงานและจุดยืนหลายอย่าง:

- **Harness over model** — อุปมา F1: ทุกคนหมกมุ่นกับ "เครื่องยนต์" (model) ทั้งที่ harness เป็นส่วนที่เราคุมได้จริง คิดเป็น 50/50 ไม่ใช่ model 90%. อยากประหยัด token ให้ทำ codebase ที่แก้ง่าย แล้วใช้ model ถูก ๆ ได้ ดู [[coding-harness]], [[bitter-lesson]]
- **[[queues-over-loops|Queues, not loops]]** — มองงานเป็นคิวที่หลาย node หยิบไปทำ ไม่ใช่ลูปเดียววิ่งไม่จบ; กระแสลูปครึ่งหนึ่งคือ lab อยากขาย token (ที่มา: [[ralph|Ralph]] ของ [[jeffrey-huntley|Jeffrey Huntley]])
- **[[afk-agents|AFK]]** — ทำงานส่วนใหญ่แบบ away-from-keyboard: โยนงานที่ scope แล้วให้ agent ไปทำเอง = มี "เรา" หลายคนทำงานขนาน
- **[[agent-experience|AX]]** — แยก DX กับ Agent Experience; codebase ที่ดี = AX ที่ดี (คนมักลืม)
- **[[skill-procedures-vs-abilities|Skills = procedures, not abilities]]** — ชอบ skill ที่ user สั่งเอง เก็บความรู้ไว้ในหัวคน ไม่ leak description เข้า context
- **Self-improving systems** — "ถ้ามีคนขโมยจักรยานเรื่อย ๆ ก็ซื้อกุญแจล็อก": อย่าแค่ให้ model แพง ๆ เจอ bug ลึก ให้รัน cron review ด้วย model ถูก ๆ แทน
- **Setup** — [[claude-code|Claude Code]] + [[claude-opus-4-8|Opus 4.8]] effort `medium`; งาน AFK ผ่าน [[sandcastle|Sandcastle]] บน GitHub Actions; รอ ~1 เดือนก่อนรับ model ใหม่; ยังไม่ตัดสินใจเรื่อง Fable
- **Skills repo** — `github.com/mattpocockuk/skills` (`npx skills latest add`), เว็บ/นิวส์เลตเตอร์ที่ aihero.dev

**ทักษะของคุณคือเพดานของ AI** ("your skills are the ceiling on what AI can do") — AI ทำให้ senior เก่งขึ้น 10 เท่า แต่ junior ได้นิดเดียว ดู [[strategic-vs-tactical-programming]]

## Dumb zone และ context hygiene (X, 2026-06)

ในโพสต์ [[matt-pocock-dumb-zone-compaction]] Pocock เสนอวิธีจับ [[dumb-zone|dumb zone]] แบบเร็ว: เมื่อ agent ทำเรื่องโง่ ให้ `/rewind` ก่อนจุดพลาด แล้ว `/compact` ก่อนรันใหม่. ถ้ารอบใหม่ดีขึ้น แปลว่าปัญหาไม่ได้อยู่ที่ model อย่างเดียว แต่อยู่ที่ active context ที่รกด้วย trajectory ผิดและ noise.

มุมนี้ต่อจาก harness-first ของเขาโดยตรง: session management เป็นส่วนหนึ่งของ [[coding-harness|harness]] ที่คนควบคุมได้. เขาไม่ได้เสนอให้ compact ตลอดเวลา แต่ให้ compact ตอนมี phase boundary ที่สรุป state ได้จริง.

## ดูเพิ่ม
- [[matt-pocock-software-fundamentals]]
- [[matt-pocock-agentic-workflow]]
- [[matt-pocock-dumb-zone-compaction]]
- [[matt-pocock-4-ai-terms]]
- [[new-skills-handoff-prototype-review-writing]]
- [[david-ondrej]]
- [[coding-harness]]
- [[queues-over-loops]]
- [[afk-agents]]
- [[agent-experience]]
- [[strategic-vs-tactical-programming]]
- [[skill-procedures-vs-abilities]]
- [[teach-skill]]
- [[sandcastle]]
- [[john-ousterhout]]
