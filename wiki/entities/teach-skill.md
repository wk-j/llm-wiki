---
title: teach skill
type: entity
tags: [ai-skill, education, claude-code, pocock, stateful]
created: 2026-06-21
updated: 2026-06-21
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md"]
---

# teach skill

**Type:** Agent skill (procedure) ของ [[matt-pocock|Matt Pocock]]
**ติดตั้ง:** `npx skills latest add` แล้วเลือก teach (จาก `github.com/mattpocockuk/skills`); ใช้ได้ทั้ง [[claude-code|Claude Code]] และ Codex; รายละเอียดที่ aihero.dev/skills

teach คือ skill ที่เปลี่ยน agent ให้เป็น **ครูส่วนตัว** ที่สร้างหลักสูตรสด ๆ เรื่องอะไรก็ได้ Matt อิงประสบการณ์สอน 10 ปี (สอนร้องเพลงมาก่อน แล้วมาสอน dev) เข้ารหัสหลักการสอนจริงลงไป. โชว์ในพอดแคสต์กับ [[david-ondrej|David Ondrej]] (2026-06-19) — สอน David (สมมติเป็น vibe coder) ให้เริ่มจาก git

## เป็น stateful skill

Matt แยก skill เป็น **stateless** (ไม่ต้องจำอะไร) กับ **stateful** (เก็บ state ไว้ใน workspace local). teach เป็น stateful เพราะครูที่ดีต้องจำได้ว่าผู้เรียนทำอะไรไปแล้ว ต้องไปไหนต่อ. ต้องรันใน workspace เพราะมันเซฟไฟล์ลงที่นั่น

## กลไก

1. สร้าง **`mission.md`** ก่อน — ผู้เรียนเป็นใคร อยากสร้างอะไร ทำไมถึงสำคัญ success คืออะไร. mission นี้ orient ทุกอย่างที่ skill ทำต่อ
2. ค้น **trusted resources** บนเว็บ
3. สร้าง **reference cheat sheet** + บทเรียนเป็น **HTML** (เปิดในเบราว์เซอร์ อ่านง่ายกว่า terminal มาก; เซฟ local ย้อนดูได้)
4. ให้แบบฝึกหัดจริงในเครื่อง (มันเช็คด้วยว่าเครื่องเรามี git ติดตั้งหรือยัง) + **quiz** เพื่อเพิ่ม storage strength
5. เก็บ **learning record** — มองความรู้เป็น "ป่า/graph" แล้วสร้าง linear path เดินผ่านมัน
6. ชี้ไป **primary source** (เช่นหนังสือ Pro Git) แล้วชวนถามต่อ / สร้างบทเรียนถัดไป

หลักการสอนที่ฝังไว้: **zone of proximal development** (สอนของที่เอื้อมถึงได้ถ้ามีคนช่วย), แยก **[[knowledge-skills-wisdom|knowledge/skills/wisdom]]**, และ quiz เพื่อ storage strength

## ตัวอย่างการใช้

- Matt สอนตัวเองแก้ Rubik's cube จาก memory ได้ด้วย teach
- ลองถามว่า "จะเป็น senior dev ต้องเรียนอะไร" → skill ไปค้น resource แล้วสร้าง curriculum ออกมา

## เป็น procedure ไม่ใช่ ability

teach เป็น **procedure** (user invoke เอง) ตามปรัชญา skill ของ Matt ดู [[skill-procedures-vs-abilities]]

## ดูเพิ่ม

- [[matt-pocock]]
- [[matt-pocock-agentic-workflow]]
- [[knowledge-skills-wisdom]]
- [[skill-procedures-vs-abilities]]
- [[grill-me]]
- [[html-artifacts]]
