---
title: Mellum2 Goes Open Source
type: source
tags: [ai, llm, open-source, jetbrains, agents, inference]
created: 2026-06-05
updated: 2026-06-05
sources: [Mellum2 Goes Open Source A Fast Model for AI Workflows  The JetBrains AI Blog.md]
---

# Mellum2 Goes Open Source / Mellum2 เปิดโอเพนซอร์ส

บทความนี้คือประกาศจาก [[jetbrains|JetBrains]] (บริษัททำ IDE อย่าง IntelliJ IDEA และ PyCharm) ว่าเปิดตัว [[mellum2|Mellum2]] เป็น model ขนาด 12B ภายใต้ Apache 2.0 จุดขายไม่ใช่ "ฉลาดที่สุด" แต่คือ "เร็วพอ ถูกพอ และ deploy ได้จริง" สำหรับ workflow ของ AI ในงาน software engineering

## ใจความสั้น

- [[mellum2|Mellum2]] เป็น model 12B ที่ trained from scratch และออกแบบมาให้ใช้กับ natural language + code
- ใช้ [[mixture-of-experts|Mixture-of-Experts]] (MoE, สถาปัตยกรรมที่เปิดใช้แค่ expert บางส่วนต่อ token) รวม 12B parameters แต่ active แค่ 2.5B parameters ต่อ token
- JetBrains วาง Mellum2 เป็น [[focal-models|focal model]] คือ model เฉพาะทางที่เร็วและคุมต้นทุนได้ สำหรับ task ที่เกิดบ่อยในระบบ AI
- Use case หลักคือ routing, summarization, RAG pipeline, intermediate reasoning step, subagent ขั้นย่อย, และ private/local deployment
- เผยแพร่ภายใต้ Apache 2.0 ทำให้เอาไปทดลอง, fine-tune, self-host, หรือใช้ในระบบภายในได้ง่ายกว่า closed API

## จาก code completion สู่ workflow model

Mellum รุ่นแรกเริ่มจาก code completion (เติมโค้ดใน IDE) แต่ Mellum2 ขยายมาเป็น model ที่รับทั้งภาษาเขียนทั่วไปและ code ได้พร้อมกัน

ตรงนี้สำคัญเพราะ JetBrains ไม่ได้ pitch Mellum2 เป็น chatbot หลักที่คุยกับผู้ใช้ทุกเรื่อง แต่ pitch เป็นชิ้นส่วนในระบบ AI ที่มีหลายขั้นตอน เช่น prompt เข้ามา -> route งาน -> ดึง context -> สรุป -> ให้ model ใหญ่ตอบ หรือแตกงานให้ subagent ทำ

**ผลคือ:** Mellum2 อยู่ในชั้น infrastructure ของ [[ai-orchestrator|AI orchestrator]] ไม่ใช่ชั้น "frontier assistant" ที่ผู้ใช้คุยด้วยตรง ๆ

## Architecture and performance

JetBrains บอกว่า bottleneck ของ production AI ไม่ได้มีแค่ capability แต่มี latency, throughput, และ cost ด้วย Mellum2 เลยเลือก design ที่ lean กว่า model ใหญ่ทั่วไป

- **MoE design:** มี parameter รวม 12B แต่ตอน infer แต่ละ token ใช้แค่ 2.5B active parameters ทำให้ compute ต่อ token ต่ำกว่า dense model ขนาดใกล้กัน
- **ไม่ multimodal:** Mellum2 ไม่พยายามทำภาพ/เสียง/video แต่โฟกัส natural language กับ code เพื่อให้ตัว model เบาและตรงกับงาน IDE / software engineering
- **inference time:** JetBrains อ้างว่า Mellum2 แข่งได้กับ model ขนาดใกล้กันใน benchmark ด้าน code, science, math, reasoning และใช้ inference time ต่ำกว่าครึ่งหนึ่ง

**ได้อะไร:** Mellum2 เป็นตัวอย่างว่า model release รุ่นใหม่อาจชนะด้วย system fit ไม่ใช่ benchmark headline อย่างเดียว

## Use case ที่ JetBrains ชู

หัวใจของ Mellum2 คือใช้กับงานที่เกิดถี่และต้องตอบเร็ว งานพวกนี้ไม่ควรเผา frontier model ทุกครั้ง

- **Route and orchestrate AI workloads:** อ่าน prompt แล้วช่วยเลือก model หรือ tool ที่เหมาะกับงานนั้น
- **Low-latency RAG pipeline:** ดึง context แล้วให้ Mellum2 สรุปก่อนตอบ เพื่อให้ pipeline เร็วขึ้น
- **Fast sub-agents:** ใช้กับขั้นย่อยอย่าง context gathering, planning, validation แทนการให้ model ใหญ่ทำทุกขั้น
- **Private/local AI:** self-host หรือรัน local เพื่อให้ code และ data ไม่ออกจากระบบขององค์กร

**ผลคือ:** Mellum2 เติมช่อง "worker model" ในระบบ agent ที่ model ใหญ่เป็นของแพงและควรถูกเรียกเฉพาะตอนจำเป็น

## Focal model philosophy

JetBrains เรียกแนวคิดนี้ว่า **focal model**: model ที่โฟกัสงานเฉพาะและปรับให้เร็ว ถูก และควบคุมง่าย แทนที่จะเป็น model ใหญ่ก้อนเดียวที่พยายามทำทุกอย่าง

ประโยคสำคัญจากบทความ:

> "At JetBrains, we believe the future belongs to coordinated systems, not single models."

แปลเป็นไทยแบบใช้งานได้: อนาคตของ AI product คือระบบที่เอา model หลายตัวมาแบ่งงานกันถูกจุด ไม่ใช่ model ตัวเดียวที่เก่งสุด

**ได้อะไร:** Mellum2 เชื่อมกับแนวคิด [[advisor-strategy|Advisor Strategy]] และ [[subagent-patterns|Subagent Patterns]] โดยตรง คือใช้ model เล็ก/เร็วเป็นตัวทำงานประจำ แล้วกัน model ใหญ่ไว้สำหรับจุดที่ต้องใช้ judgement หรือ reasoning หนักจริง ๆ

## See also

- [[mellum2]]
- [[jetbrains]]
- [[focal-models]]
- [[mixture-of-experts]]
- [[open-weight-models]]
- [[ai-orchestrator]]
- [[subagent-patterns]]
- [[advisor-strategy]]
