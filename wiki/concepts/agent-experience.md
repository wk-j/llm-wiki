---
title: Agent Experience (AX)
type: concept
tags: [ai, agents, codebase, dx, harness, software-engineering]
created: 2026-06-21
updated: 2026-06-21
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md"]
---

# Agent Experience (AX) / ประสบการณ์ของ agent ในโค้ดเบส

**AX (agent experience) คือ "ประสบการณ์ที่ agent ได้เวลาเข้ามาทำงานในโค้ดเบสของเรา" — คู่ขนานกับ DX (developer experience) ที่เป็นประสบการณ์ของคน.** [[matt-pocock|Matt Pocock]] เสนอคำนี้ในพอดแคสต์กับ [[david-ondrej|David Ondrej]] (2026-06-19)

## นิยาม

> "Agent experience is the experience that the agent has working in the codebase."

อะไรก็ตามที่ทำให้ agent ทำงานในโค้ดได้ดีขึ้น คือการลงทุนใน AX:

- **skill ที่ดี** — intent เขียนไว้ให้ agent อ่าน
- **harness ที่ดี** — guides + sensors (ดู [[harness-guides-sensors]])
- **model ที่แรงขึ้น** — ก็ช่วย แต่เป็นแค่ส่วนเดียว
- **และที่คนมักลืม: codebase ที่ดี** — Matt ย้ำว่าคนมัวแต่คิดเรื่อง skill กับ model จนลืมว่าการปรับ codebase เองนี่แหละให้ AX ที่ดีที่สุด

## DX ดี มัก = AX ดี

Matt ชี้ว่ามี **overlap สูง** ระหว่าง DX ที่ดีกับ AX ที่ดี — codebase ที่คนทำงานด้วยง่าย (โครงสร้างชัด, interface เรียบ, test ดี, doc พอชี้ทาง) ก็มักเป็น codebase ที่ agent ทำงานด้วยง่ายเหมือนกัน

นี่คือเหตุผลที่ **senior dev มีค่าในยุค AI**: senior ที่เก่งรู้วิธีสร้าง DX ดี ซึ่งแปลงเป็น AX ดีโดยตรง. ส่วน junior ที่ "เป็น AI believer" ก็แค่มองปัญหาจากอีกมุม — ถ้าจับคู่ความกระตือรือร้นเข้ากับ software fundamentals นิดหน่อยก็ thrive ได้ (ดู [[strategic-vs-tactical-programming]])

ของจริงที่ตามมา: อยากให้ agent ใช้ token น้อยลงและทำงานถูกขึ้น ก็ทำ codebase ให้แก้ง่าย — guardrail ชัด agent ไม่ต้องเอาหัวโขกกำแพง ใช้ model ถูก ๆ ก็พอ (ดู [[coding-harness]])

## AX ของการ review

AX ไม่ได้จบที่ตอน agent เขียนโค้ด — รวมถึงตอน **คน review งานของ agent** ด้วย. Matt ยกตัวอย่างที่เจ๋ง: ให้ AI อัด **วิดีโอเดินผ่านโค้ดที่เปลี่ยน** + เสียง TTS พากย์ทับ แล้วแปะบน PR เพื่อให้คน review ได้เร็วขึ้น. GitHub สร้างมานานก่อนยุค agentic อาจต้องมี surface (เช่น HTML) ที่ออกแบบมาเพื่อ review งาน agent โดยเฉพาะ — รู้จักเรา รู้ pattern ของ bug เก่า ๆ

> ได้อะไร: เวลาจะปรับให้ agent ทำงานดีขึ้น อย่าคิดแค่ "เปลี่ยน model" หรือ "เพิ่ม skill" — ถามด้วยว่า codebase และ review surface ของเราเอื้อให้ agent (และคนที่ตรวจ agent) ทำงานง่ายแค่ไหน

## ดูเพิ่ม

- [[matt-pocock]]
- [[matt-pocock-agentic-workflow]]
- [[coding-harness]]
- [[harness-guides-sensors]]
- [[strategic-vs-tactical-programming]]
- [[agentic-code-review]]
- [[html-artifacts]]
