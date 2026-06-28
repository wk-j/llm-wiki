---
title: Self-Learning Agents
type: concept
tags: [agent-memory, multi-agent, anthropic, vision, self-learning]
created: 2026-05-09
updated: 2026-06-26
sources: [memory-and-dreaming-self-learning-agents, Self Learning for Agents Clearly Explained.md]
---

# Self-Learning Agents / agent ที่เรียนรู้เอง

แนวคิดที่ [[anthropic|Anthropic]] วาง memory เป็น primitive ตัวต่อไป — agent ที่ "เก่งขึ้นเอง" จากงานของตัวเองและของ agent ตัวอื่นในระบบเดียวกัน โดย**ไม่ต้อง retrain โมเดล** ทุกอย่างเกิดจากการสะสมและ curate memory ระหว่างที่รัน

> ภาพรวมก่อนลงรายละเอียด: คำว่า "agent เรียนรู้เอง" จริง ๆ แตกได้เป็น 3 ชั้น (model / harness / context — ดู [[three-learning-layers]]). สิ่งที่ Anthropic ทำในหน้านี้คือ **ชั้น context** เป็นหลัก: เรียนผ่าน memory ที่เป็น text นอก model ไม่ใช่การแก้ weight. นั่นคือชั้นที่ product เกือบทุกตัวควรเริ่ม เพราะคุณเป็นเจ้าของมัน ส่วน weight เป็นของ lab.

## 3 อย่างที่ agent เรียนได้จาก memory

จาก talk ของ Mahes ([[anthropic|Anthropic]] PM, 2026-05-09):

1. **เรื่อง task** — success criteria, common mistake, strategy ที่ใช้ได้/ไม่ได้
2. **เรื่อง environment** — codebase ที่ทำงานด้วย, ไฟล์/asset ที่ต้อง keep up to date
3. **เรื่อง agent ตัวอื่น** — เห็น session ของคนอื่น (ผ่าน [[dreaming]]) แล้วเอามารวม

ข้อ 3 คือสิ่งที่ Mahes บอกว่าตื่นเต้นที่สุด เพราะ multi-agent system ขนาดใหญ่ที่ทำงานใน environment เดียวกัน จะค่อยๆ ก่อ "world model" ของระบบนั้นขึ้นมาเอง

## โครงที่ Anthropic วางให้

Self-learning ใน Managed Agents ตั้งอยู่บน 2 primitive:

1. **[[agent-memory-filesystem|Memory as file system]]** — Claude อ่าน/เขียน memory ใน-session เอง
2. **[[dreaming|Dreaming]]** — batch process นอก session อ่าน transcript ข้าม agent หา pattern ที่ตัวเดียวมองไม่เห็น แล้ว curate memory store

ผลคือวงจร "เรียนระหว่างทำ → ฝันรวมความรู้ตอน idle → ตื่นมาเริ่มงานใหม่ที่เก่งขึ้น" — แอบมีกลิ่น cognitive science (memory consolidation ระหว่างนอนหลับ) ปนอยู่ในการตั้งชื่อ

## หลักฐานเบื้องต้น (early customer)

- **Rocketin** — internal knowledge agent: first-pass mistake ลด **90%**
- **[[harvey-ai|Harvey]]** — legal benchmark: task completion rate **6 เท่า** หลังเปิด dreaming

ตัวเลขพวกนี้คือ "เก่งขึ้นจาก memory ล้วนๆ" โมเดลข้างหลังเป็นตัวเดิม

## เทียบกับ "self-improvement" รูปแบบอื่น

- **RLHF / fine-tune** — แก้ที่ weight ของโมเดล ใช้เวลานาน + ต้องใช้ infrastructure training
- **In-context learning** — โผล่ใน prompt session เดียวจบ ไม่ accumulate
- **Self-learning agents (memory-based)** — accumulate ข้าม session, ข้าม agent, อยู่ที่ "ภายนอกโมเดล" — ปรับได้เร็วและ portable

## ที่ทางในแผนที่ 3 ชั้น

[[ataiiam|@ataiiam]] ใน [[self-learning-for-agents-explained]] วางแนวทางแบบ Anthropic ลงในแผนที่ที่ใหญ่กว่า — เทียบกับเจ้าอื่นได้ชัดขึ้น:

- **Layer Model** (เรียนที่ weight) — Karpathy AutoResearch, MIT SEAL, DeepMind AlphaEvolve. รันได้แค่ที่มี "คะแนนฟรี" (code/math) → อยู่แต่ใน lab ไม่ใช่ที่ที่ product ส่วนใหญ่ควรแตะ
- **Layer Harness** (เรียนที่ scaffold) — [[loop-engineering|loop engineering]], LangChain Deep Agents (เขียน harness ใหม่จาก trace), Self-Harness, [[microsoft|Microsoft]] Agent Framework. ทำได้ใน product แต่ "harness จับได้ ≠ agent ฉลาดขึ้น"
- **Layer Context** (เรียนที่ memory + skill) — **ตรงนี้คือที่ที่ Anthropic อยู่**: [[dreaming]] = "เขียน memory ใหม่เบื้องหลัง" เวอร์ชัน Anthropic เทียบกับ [[letta|Letta]]/OpenClaw ที่ทำไอเดียเดียวกัน. memory แบ่งเป็น semantic/episodic/procedural ([[agent-memory-types]]) — self-learning จริงต้องใช้สองชนิดหลัง

ส่วนที่ thread ชูเพิ่มและหน้านี้ยังไม่ครอบ: สัญญาณที่ดีที่สุดไม่ใช่ run ของ agent เอง แต่คือ **การตัดสินของ user จริง** ที่ปลอมไม่ได้ ดู [[learning-from-users]].

## ความเสี่ยง / สิ่งที่ยังไม่ตอบ

- **Memory ผิดสะสม** — ถ้า agent หลายตัวเชื่อสิ่งเดียวกันที่ผิด dreaming จะแยก signal จาก noise ได้แค่ไหน
- **Staleness** — environment เปลี่ยน memory เก่ายังใช้ได้ไหม → [[memory-decay]] กับ verification step ของ dreaming พยายามตอบเรื่องนี้
- **Drift ข้าม agent** — multi-agent ที่ใช้ memory ร่วมอาจเริ่ม converge ไปทางเดียวกันและสูญเสีย diversity ของ approach

## See also

- [[three-learning-layers]]
- [[agent-memory-types]]
- [[learning-from-users]]
- [[self-learning-for-agents-explained]]
- [[dreaming]]
- [[agent-memory-filesystem]]
- [[claude-managed-agents]]
- [[anthropic]]
- [[memory-and-dreaming-self-learning-agents]]
- [[memory-drift]]
- [[memory-decay]]
- [[hybrid-memory]]
- [[letta]]
