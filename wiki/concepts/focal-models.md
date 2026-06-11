---
title: Focal Models
type: concept
tags: [ai, llm, architecture, inference, orchestration]
created: 2026-06-05
updated: 2026-06-05
sources: [Mellum2 Goes Open Source A Fast Model for AI Workflows  The JetBrains AI Blog.md]
---

# Focal Models / โมเดลเฉพาะจุด

**Focal model** คือ model ที่ตั้งใจทำงานบางชุดให้เร็ว ถูก และคุมง่าย แทนที่จะพยายามเป็น frontier model ตัวเดียวที่ทำได้ทุกอย่าง คำนี้มาจากประกาศ [[mellum2|Mellum2]] ของ [[jetbrains|JetBrains]] ซึ่งเสนอว่า AI product รุ่นใหม่จะเป็น coordinated systems ไม่ใช่ single model

## แก่นความคิด

พอระบบ AI เริ่มมีหลายขั้นตอน bottleneck จะย้ายจาก "model ฉลาดพอไหม" ไปเป็น "ระบบตอบเร็วไหม, รับโหลดได้ไหม, ค่า inference แพงเกินไหม"

หลาย task ในระบบ agent เกิดซ้ำเยอะและไม่ต้องใช้ model ที่ฉลาดที่สุด เช่น:

- classify หรือ route prompt
- สรุป context ที่เพิ่ง retrieve มา
- ตรวจ output ขั้นย่อย
- วางแผนย่อยก่อนให้ model ใหญ่ทำงานต่อ
- ทำงานใน subagent ที่ขอบเขตแคบ

Focal model จึงเป็น model ที่ยอมแคบลงเพื่อให้ task พวกนี้เร็วขึ้นและถูกลง

**ได้อะไร:** ระบบไม่ต้องเผา frontier model ทุกครั้ง เพราะ pipeline วาง model แต่ละตัวไว้ในจุดที่เหมาะกับมัน

## ต่างจาก frontier model อย่างไร

Frontier model แข่งกันที่ capability สูงสุด เช่น reasoning ยาก ๆ, long-horizon coding, vision, cyber, หรือ task ที่ต้องใช้ judgement หนัก ส่วน focal model แข่งกันที่ system fit

| มิติ | Frontier model | Focal model |
|---|---|---|
| เป้าหมาย | ฉลาดที่สุด กว้างที่สุด | เร็ว ถูก คุมง่าย ในงานเฉพาะ |
| งานที่เหมาะ | ตัดสินใจยาก, synthesis, architecture, final answer | routing, summarization, validation, worker step |
| ต้นทุน | สูงกว่า | ต่ำกว่า |
| ความเสี่ยง | แพงถ้าใช้กับทุกขั้น | อาจไม่พอสำหรับงานเปิดกว้าง |

**ผลคือ:** focal model แบ่งภาระจาก frontier model เพื่อให้ระบบโดยรวม scale ได้ดีขึ้น

## ตัวอย่างจาก Mellum2

[[mellum2|Mellum2]] เป็นตัวอย่างตรง ๆ ของแนวคิดนี้ JetBrains ทำ model 12B ที่ใช้ [[mixture-of-experts|MoE]] รวม 12B parameters แต่ active 2.5B ต่อ token และไม่ทำ multimodal เพื่อรักษาความเร็ว

Use case ที่ JetBrains ชูคือ routing, RAG, subagent, และ private/local deployment ทั้งหมดเป็นงาน infrastructure ใน [[ai-orchestrator|AI orchestrator]] มากกว่างานคุยกับผู้ใช้ปลายทาง

**ได้อะไร:** Mellum2 ทำให้เห็น pattern ว่า model เล็ก/เร็วอาจมีค่ามากขึ้นเมื่อระบบ AI โตเป็น pipeline

## เชื่อมกับ pattern อื่น

- [[advisor-strategy|Advisor Strategy]] กลับด้าน orchestrator-worker: ให้ model เล็กทำงานหลัก แล้ว escalate ไป model ใหญ่ตอนเจอจุดยาก
- [[subagent-patterns|Subagent Patterns]] ต้องการ worker ที่เร็วพอสำหรับ fan-out/pipeline ไม่งั้นค่า orchestration แพงเกิน
- [[orchestration-tax|Orchestration Tax]] เตือนอีกด้านว่าเพิ่ม worker เร็ว ๆ ได้ แต่ review/judgement ของมนุษย์ยังเป็นคอขวด
- [[open-weight-models|Open-weight Models]] และ model ที่ self-host ได้ ทำให้องค์กรใช้ focal model กับ code/data ภายในได้ง่ายขึ้น

## See also

- [[mellum2]]
- [[mellum2-goes-open-source]]
- [[ai-orchestrator]]
- [[advisor-strategy]]
- [[subagent-patterns]]
- [[mixture-of-experts]]
- [[open-weight-models]]
