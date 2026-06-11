---
title: Mellum2
type: entity
tags: [ai, llm, model, jetbrains, open-source, agents]
created: 2026-06-05
updated: 2026-06-05
sources: [Mellum2 Goes Open Source A Fast Model for AI Workflows  The JetBrains AI Blog.md]
---

# Mellum2

**Mellum2** คือ model 12B จาก [[jetbrains|JetBrains]] ที่เปิดภายใต้ Apache 2.0 เมื่อ 2026-06-01 ออกแบบมาให้เป็น model เร็วสำหรับ workflow ของ AI ในงาน software engineering เช่น routing, summarization, RAG, subagent ขั้นย่อย, และ private deployment

## ตำแหน่งของ model

Mellum2 ไม่ได้วางตัวเป็น frontier model ที่ฉลาดที่สุด แต่เป็น [[focal-models|focal model]] (model เฉพาะทางที่เร็วและคุมต้นทุนได้) สำหรับงานที่เกิดบ่อยและต้อง latency ต่ำ

ตัวอย่าง:

- อ่าน prompt แล้วเลือก model/tool ที่เหมาะ
- สรุป context จาก retrieval ก่อนส่งต่อ
- ทำขั้นย่อยใน agent pipeline เช่น context gathering, planning, validation
- รัน self-hosted หรือ local เพื่อเก็บ code/data ไว้ในระบบขององค์กร

**ผลคือ:** Mellum2 เหมาะเป็น worker model ใน [[ai-orchestrator|AI orchestrator]] มากกว่าเป็น assistant ตัวเดียวที่ทำทุกอย่าง

## Architecture

Mellum2 ใช้ [[mixture-of-experts|Mixture-of-Experts]] (MoE) รวม 12B parameters แต่ active แค่ 2.5B parameters ต่อ token ทำให้ค่า compute ต่อคำต่ำกว่า dense model ขนาดใกล้กัน

JetBrains ตั้งใจให้ model โฟกัส natural language กับ code ไม่ทำ multimodal ตรงนี้แลกความกว้างของ capability กับความเร็ว ความง่ายในการ deploy และต้นทุน inference ที่ต่ำกว่า

## ความเกี่ยวข้องกับ JetBrains

Mellum รุ่นแรกเริ่มจาก code completion ใน ecosystem ของ JetBrains ส่วน Mellum2 ขยับขึ้นมาเป็น model สำหรับระบบ AI ที่มีหลายขั้นตอน ไม่ใช่แค่เติมโค้ดใน editor

ตรงนี้สอดคล้องกับบทบาทของ JetBrains ในยุค agentic IDE: บริษัทไม่ได้ทำแค่ IDE UI แต่เริ่มมีทั้ง protocol ([[agent-client-protocol|ACP]]) และ model layer ของตัวเอง

## See also

- [[mellum2-goes-open-source]]
- [[jetbrains]]
- [[focal-models]]
- [[mixture-of-experts]]
- [[open-weight-models]]
- [[subagent-patterns]]
- [[ai-orchestrator]]
