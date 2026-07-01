---
title: Three Learning Layers (Model / Harness / Context)
type: concept
tags: [ai, agents, self-learning, harness, memory, context-engineering]
created: 2026-06-26
updated: 2026-06-29
sources: [Self Learning for Agents Clearly Explained.md, "i don't want to use your agent — @RhysSullivan.md"]
---

# Three Learning Layers / agent เรียนรู้ได้ 3 ชั้น

เวลาคนพูดว่า agent "เรียนรู้เอง" จริง ๆ แล้วมันเรียนได้ที่ไหนบ้าง? กรอบที่ชัดที่สุดมาจาก **Harrison Chase** ([[langchain|LangChain]]) แล้ว [[ataiiam|@ataiiam]] เอามาขยายใน thread [[self-learning-for-agents-explained]]: agent หนึ่งตัวแยกได้ 3 ชั้น และแต่ละชั้นปรับให้ดีขึ้นได้ **เอง โดยไม่ต้องแตะอีกสองชั้น**.

- **The Model** = weight (พารามิเตอร์จากการเทรน) — ความฉลาดดิบ
- **The Harness** = code รอบ model (loop, tool, prompt, check) — ตัวกำหนดว่าความฉลาดถูกใช้ยังไง
- **The Context** = memory กับ skill ที่เก็บเป็น text นอก harness และโตขึ้นได้

ใน [[claude-code|Claude Code]] คุณใช้ครบทั้งสามอยู่แล้ว: model คือ [[claude|Claude]], harness คือตัว Claude Code, context คือ `CLAUDE.md` กับ skills ของคุณ.

> ประโยคที่ยึดทั้งกรอบ: **"The model belongs to the labs. The harness and the context are yours."** — model เป็นของ lab, harness กับ context เป็นของคุณ. ในงาน product จริง self-learning เกือบทุกครั้งหมายถึงสองชั้นหลัง.

## ทำไมการแบ่งนี้ถึงสำคัญ

กรอบนี้ตอบคำถามที่คนสับสนบ่อย: "ผมอยากให้ agent เก่งขึ้นเรื่อย ๆ ต้อง fine-tune model ไหม?" คำตอบคือ **เกือบไม่เคย** — เพราะคุณไม่ได้เป็นเจ้าของ weight และการแก้ weight ต้องมี "คะแนนฟรี" ที่งานส่วนใหญ่ไม่มี. ที่ที่คุณคุมได้จริงคือ harness กับ context.

แต่ละชั้นมีคำถามสองข้อ: **เรียนตรงนั้นได้ไหม** และ **เราเป็นเจ้าของการเรียนนั้นไหม**.

## ตัวร่วมของทุกชั้น: ต้องมีคนให้คะแนน

แก่นที่วิ่งผ่านทั้งกรอบคือ — **การเรียนรู้แบบอัตโนมัติรันได้ก็ต่อเมื่อมีตัวให้คะแนน (scorer)**. ตรงนี้ทับกับกรอบ [[harness-guides-sensors|computational vs inferential]] ของ Böckeler พอดี:

- **คะแนนฟรีจาก machine** (kernel เร็วขึ้นไหม, test ผ่านไหม) = computational → loop รันเองได้
- **ต้องคนตัดสิน** (refund นี้ถูกไหม, คำตอบ support นี้ดีไหม) = inferential → loop ไม่มีอะไรให้ให้คะแนน เลยไม่รัน

นี่คือเหตุผลที่ Model/Harness self-learning เด่นใน code กับ math (มี free scorer) แต่งาน support/sales/operations เรียนเองไม่ได้ — ต้องดึงสัญญาณจากคน ดู [[learning-from-users]].

## Layer 1: Model — อยู่แต่ใน lab

agent ปรับ weight ตัวเอง. lab ทำ 3 วิธี (ทั้งหมดคือ loop เดียวกัน รันได้เมื่อมี free scorer): [[andrej-karpathy|Karpathy]] AutoResearch (แก้ training code เก็บที่ดีขึ้น, +11%), MIT SEAL (เขียน training data ตัวเองแล้ว retrain — แต่ช้า 30–45 วิ/ครั้ง และลืมงานเก่า), [[google-deepmind|DeepMind]] AlphaEvolve (วิวัฒน์ code เทียบ scorer, kernel +32.5%, AI ปรับ AI ตัวเอง).

> ได้อะไร: น่าทึ่งในงานวิจัย แต่ **ไม่ใช่ชั้นที่ product ของคุณควรแตะ** — เพราะต้องมีคะแนนฟรีที่งานจริงส่วนใหญ่ไม่มี.

## Layer 2: Harness — ทำได้ใน product วันนี้

ปรับ scaffold รอบ model. 4 วิธี เรียงตาม "คุณทำเอง vs harness ทำเอง":

1. **[[loop-engineering|Loop Engineering]]** — ครอบ loop เพิ่ม (verification loop สำคัญสุด: grader ตัวสองส่ง output กลับถ้าไม่ผ่าน)
2. **Deep Agents (LangChain)** — เขียน harness ใหม่จาก trace, คน *อนุมัติ* (Terminal-Bench 2.0: 52.8→66.5 โดยตรึง model)
3. **Self-Harness** — harness เขียนตัวเองไม่มีคนดู (ยก 3 model ที่ตรึง weight ได้หมด → harness คือสิ่งที่รั้งมันไว้)
4. **[[microsoft|Microsoft]] Agent Framework** — harness สำเร็จรูปติดตั้งใช้

ทั้งสี่สร้าง harness **ไว้ล่วงหน้า**. ทิศใหม่คือ agent ประกอบ harness สดต่อหนึ่งงาน (เทียบ [[just-in-time-context]]).

> ได้อะไร: harness ปรับได้ใน product แต่ "harness จับได้ ≠ agent ฉลาดขึ้น" — verification loop หยุด refund เกินลิมิตได้ แต่เคสหน้า agent ก็ลองเดิม **มันไม่ได้เรียนรู้** เพราะการเรียนรู้จริงอยู่ที่ context.

## Layer 3: Context — ชั้นเดียวที่เรียนจาก user ได้

memory + skill เป็น text นอก model. memory มี 3 ชนิด (semantic/episodic/procedural ดู [[agent-memory-types]]) — self-improving agent ต้องใช้ episodic + procedural แต่ส่วนใหญ่มีแค่ semantic. 3 วิธีเขียน text: [[letta|Letta]]/OpenClaw (เขียน memory ใหม่เบื้องหลัง = [[dreaming]]), Hermes (อ่าน failure แก้ skill), [[anthropic|Anthropic]] skills/Manus (เปลี่ยน run ดีเป็น `SKILL.md`).

> ได้อะไร: text อยู่ถาวรกว่า weight — ย้าย model/roll back ได้ และเป็น **ชั้นเดียวที่รับสัญญาณจาก user ได้** เพราะ text เดียวกันเป็น memory ของ agent, preference ของ user, หรือความรู้ทั้งทีมก็ได้.

## Product company อยู่ชั้นไหน

[[i-dont-want-to-use-your-agent]] ของ [[rhys-sullivan|Rhys Sullivan]] ทำให้กรอบนี้ชัดในมุม SaaS/product. บริษัทไม่จำเป็นต้องเป็นเจ้าของทั้งสามชั้น:

- **Model** — power user อาจจ่ายและเลือกเอง
- **Harness** — power user อาจใช้ daily-driver agent ของตัวเอง
- **Context** — บริษัทควรส่ง product knowledge, docs, skills, MCP/API/CLI และ deeplink ให้

นี่คือ [[bring-your-own-agent]]: product ไม่ต้องชนะ agent ของผู้ใช้. Product ต้องทำให้ context ของตัวเองเข้า agent นั้นได้ดี.

## เชื่อมกับเรื่องอื่นในวิกินี้

- **[[self-learning-agents]]** — กรอบ Anthropic (memory + dreaming) คือ instance หนึ่งของ Layer 3 (Context). thread นี้วางมันลงในแผนที่ที่ใหญ่กว่า
- **[[harness-engineering]]** — ขยาย Layer 2 เต็ม ๆ; Self-Harness / Deep Agents คือ harness ที่ปรับ *ตัวเอง*
- **[[harness-guides-sensors]]** — อธิบายว่าทำไมแต่ละชั้นต้องมี scorer (computational vs inferential)
- **[[learning-from-users]]** — สิ่งที่ทั้งสามชั้นพลาด: สัญญาณจากคนจริงที่ปลอมไม่ได้
- **[[knowledge-skills-wisdom]]** — มุมของ [[matt-pocock|Pocock]] ว่า skill (Layer 3) คือเพดานของสิ่งที่ AI ทำได้
- **[[bring-your-own-agent]]** — product company เปิด context layer ให้ agent ของผู้ใช้ แทนที่จะล็อกไว้ใน in-app agent อย่างเดียว

## See also

- [[self-learning-for-agents-explained]]
- [[self-learning-agents]]
- [[harness-engineering]]
- [[loop-engineering]]
- [[agent-memory-types]]
- [[learning-from-users]]
- [[harness-guides-sensors]]
- [[langchain]]
- [[dreaming]]
- [[just-in-time-context]]
- [[bring-your-own-agent]]
