---
title: Agent Experience (AX)
type: concept
tags: [ai, agents, codebase, dx, harness, software-engineering]
created: 2026-06-21
updated: 2026-07-01
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md", "i don't want to use your agent — @RhysSullivan.md", l8-principals-agentic-engineering-workflow-kun-chen.md]
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

## AX ของ product ภายนอก

[[rhys-sullivan|Rhys Sullivan]] เพิ่มมุมว่า AX ไม่ได้อยู่แค่ใน codebase ของเรา. ถ้า agent ประจำวันต้องทำงานกับ [[linear|Linear]], [[cloudflare|Cloudflare]], หรือ [[posthog|PostHog]], product เหล่านั้นก็มี AX ของตัวเองเหมือนกัน.

In-app agent อาจเห็น dashboard ชัด แต่ daily-driver agent เห็น local repo, files, git branches, terminal, และ memory ส่วนตัว. แนว [[bring-your-own-agent]] จึงบอกว่า product ควรเปิด docs, skills, MCP/API/CLI และ deeplink ให้ agent ภายนอกใช้. แบบนี้ agent ไม่ต้องเดา product และไม่ต้องทิ้ง context ท้องถิ่นของผู้ใช้.

**ได้อะไร:** AX เป็น product surface. Product ที่ agent ภายนอกใช้ยาก จะถูก power user ใช้ได้น้อยลง แม้ in-app chat จะดูดี.

## AX ของการ review

AX ไม่ได้จบที่ตอน agent เขียนโค้ด — รวมถึงตอน **คน review งานของ agent** ด้วย. Matt ยกตัวอย่างที่เจ๋ง: ให้ AI อัด **วิดีโอเดินผ่านโค้ดที่เปลี่ยน** + เสียง TTS พากย์ทับ แล้วแปะบน PR เพื่อให้คน review ได้เร็วขึ้น. GitHub สร้างมานานก่อนยุค agentic อาจต้องมี surface (เช่น HTML) ที่ออกแบบมาเพื่อ review งาน agent โดยเฉพาะ — รู้จักเรา รู้ pattern ของ bug เก่า ๆ

> ได้อะไร: เวลาจะปรับให้ agent ทำงานดีขึ้น อย่าคิดแค่ "เปลี่ยน model" หรือ "เพิ่ม skill" — ถามด้วยว่า codebase และ review surface ของเราเอื้อให้ agent (และคนที่ตรวจ agent) ทำงานง่ายแค่ไหน

## AX ของ tool output

[[kun-chen|Kun Chen]] เพิ่มมุมที่จับต้องได้ใน [[l8-principals-agentic-engineering-workflow-kun-chen|workflow walkthrough]]: external tool ที่ agent เรียกใช้ก็มี AX ของตัวเอง. ถ้า tool คืน JSON ยาว, latency สูง, หรือ output มี noise มาก agent จะเสีย token และ turn ไปกับการแปลผล. ถ้า tool คืน output ที่ token-efficient และตรงกับ task agent ก็ทำงานเร็วและแม่นขึ้น.

เขาเรียกทิศนี้ว่า [[axi|AXI]]: ออกแบบ tool โดยถือว่า agent เป็น first-class user. ตัวอย่างคือ benchmark GitHub access ที่เขาอ้างว่า GitHub MCP ใช้ token/latency สูงกว่า CLI มาก และ AXI-style tool ทำงานถูกกว่า.

**ได้อะไร:** AX ไม่ได้อยู่แค่ repo หรือ PR. API/CLI/MCP/output format ทุกตัวที่ agent แตะคือส่วนหนึ่งของ experience.

## AX ของ planning

[[lavish|Lavish]] เป็นอีกมุมของ AX: คน feedback agent ได้ดีขึ้นเมื่อ plan เป็น visual artifact ไม่ใช่ text wall. พอ requirement ถูกถกบนหน้าที่หน้าตาคล้าย product จริง agent ก็รับ signal ที่คมขึ้นก่อนลงมือ implement.

**ได้อะไร:** AX ที่ดีไม่ใช่แค่ทำให้ agent สบาย แต่ทำให้มนุษย์ส่ง judgement กลับเข้า agent ได้ชัดขึ้น.

## ดูเพิ่ม

- [[matt-pocock]]
- [[matt-pocock-agentic-workflow]]
- [[coding-harness]]
- [[harness-guides-sensors]]
- [[strategic-vs-tactical-programming]]
- [[agentic-code-review]]
- [[html-artifacts]]
- [[bring-your-own-agent]]
- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[axi]]
- [[lavish]]
- [[no-mistakes]]
