---
title: AI Orchestrator
type: concept
tags: [ai, software-engineering, agents, roles]
created: 2026-04-15
updated: 2026-04-23
sources: [software-engineer-role-ai-era.md, Using Claude Code Session Management & 1M Context.md, llm-era-computer-engineering-nattee.md, alex-ker-harnesses-optimize.md]
---

# AI Orchestrator / ผู้อำนวยการวง AI

บทบาททางวิศวกรรมที่นิยามโดย **การกำกับดูแล pipeline ของ AI agent** แทนที่จะเขียนโค้ดที่ agent เหล่านั้นสร้างขึ้นมาโดยตรง ในโพสต์ต้นฉบับได้วางกรอบไว้ว่านี่คือนิยามใหม่ของงานระดับ senior developer

## ความรับผิดชอบ

- **ออกแบบ pipeline:** agent ใดมีอยู่บ้าง, แต่ละตัวทำอะไร, แต่ละตัวได้รับ context อะไร
- **ตัดสินใจลำดับการทำงาน:** agent ทำงานเมื่อไหร่, อะไรเป็นตัวกระตุ้น, ส่งมอบงานต่ออย่างไร
- **นิยามการส่งมอบงาน:** output จาก agent หนึ่งจะกลายเป็น input สำหรับตัวถัดไปได้อย่างไร
- **ตั้ง quality gates:** จุดที่ต้องมีการรีวิวโดยมนุษย์หรือการประเมินผลอัตโนมัติจะอยู่ระหว่างขั้นตอนใด

## ทำไมจึงเป็นบทบาทของ senior developer

การควบคุม agent เป็น abstraction ที่อยู่เหนือการเขียนโค้ดหนึ่งระดับ ต้องใช้:

- A system-level mental model (ทักษะเดียวกับงานของ [[engineering-role-shift|Systems Architect]])
- ความคุ้นเคยกับ failure mode ของแต่ละ agent เพื่อที่คุณจะสามารถหลีกเลี่ยงมันได้
- วิจารณญาณในการตัดสินใจว่าขั้นตอนใดควรเป็นโค้ดที่ deterministic และขั้นตอนใดควรเป็นการเรียก LLM

A junior สามารถรัน agent ตัวเดียวตาม prompt ได้ แต่ orchestration คือการประกอบ agent *หลายตัว* ซึ่งแต่ละตัวก็ไม่น่าเชื่อถือ ให้กลายเป็นระบบที่โดยรวมแล้วน่าเชื่อถือ — ซึ่งมีลักษณะคล้ายกับวิศวกรรมระบบแบบกระจาย (distributed systems engineering) มากกว่า prompt engineering

## Subagents ในฐานะเครื่องมือจัดการ context

การสร้าง subagent ยังเป็นเทคนิคในการลดผลกระทบจาก [[context-rot]] ด้วย subagent แต่ละตัวจะได้รับ context window ใหม่; output ของ tool ที่อยู่ระหว่างทางจะถูกแยกเก็บไว้ มีเพียงผลลัพธ์สุดท้ายเท่านั้นที่ถูกส่งกลับไปยัง session หลัก ข้อทดสอบในใจคือ: *"ฉันต้องการ output ระหว่างทางนี้อีกหรือไม่ หรือต้องการแค่ข้อสรุป?"* หากเป็นอย่างหลัง ให้ delegate งานไปให้ subagent ดู [[compaction]] สำหรับทางเลือกอื่นเมื่อ context โตขึ้นแล้ว

## Infrastructure ที่เกี่ยวข้อง

Orchestration สร้างขึ้นบน tooling layer ที่บทบาท AI Tool Builder สร้างขึ้น:

- [[model-context-protocol|MCP]] servers — ทำให้ agent เข้าถึงเครื่องมือและข้อมูลได้
- Agent frameworks — โครงสร้างสำหรับ workflow ที่มีหลายขั้นตอนและหลาย agent
- Evaluation pipelines — เพื่อจับ regression ที่เกิดขึ้นเงียบๆ เมื่อ agent หรือ prompt เปลี่ยนไป
- RAG systems — เพื่อให้ output ของ agent อ้างอิงกับ knowledge base ที่เฉพาะเจาะจง (เทียบกับ [[llm-knowledge-bases]])

## The advisor inversion (การกลับด้านด้วย advisor)

[[advisor-strategy]] ได้กลับด้านรูปแบบ orchestrator-worker อย่างชัดเจน: แทนที่จะให้โมเดลใหญ่แตกงานและมอบหมาย, จะให้โมเดลเล็กขับเคลื่อนงานตั้งแต่ต้นจนจบและ escalate ไปหาโมเดลใหญ่เฉพาะเมื่อเจอจุดตัดสินใจที่ยาก วิธีนี้อาจถูกกว่าการใช้โมเดลเล็กเพียงอย่างเดียว เพราะคำแนะนำจาก advisor ช่วยป้องกัน tool loop ที่ไม่มีทางออกซึ่งมีราคาแพง

## R.P.I. — วินัยระดับ prompt ที่สะท้อน orchestration

**R.P.I. framework** ของ [[humanlayer|HumanLayer]] — `Research` → `Plan` → `Implement` — แสดงออกถึงวินัยแบบ orchestration เดียวกันในระดับ single-harness แต่ละ prompt ควรทำหน้าที่เพียงอย่างใดอย่างหนึ่งจากสามอย่างนี้; โดยมนุษย์จะรีวิวแผนก่อนเริ่ม implement เป็นงานที่ต้องใช้วิจารณญาณระดับซีเนียร์ตั้งแต่วันแรก: ดูส่วน R.P.I. ใน [[coding-harness]] และหน้า source [[alex-ker-harnesses-optimize]]

นี่คือทักษะ orchestration ที่ใช้กับ agent ตัวเดียวข้าม turn แทนที่จะเป็นข้าม agent หลายตัวใน subagent pipeline (ดู [[subagent-patterns]])

## แรงกดดันที่ลดทอนความต้องการ senior

[[nattee-niparnan|อ.ณัฐที นิภาชน์]] (Ep. 2, 17 เม.ย. 2026) ได้ชี้ให้เห็นผลข้างเคียงของ orchestration: **การตัดสินใจเชิงออกแบบระดับสูงกำลังถูกผลักลงไปยัง junior ไม่ใช่ขึ้นไปยัง senior** การเลือก framework, การประเมิน library, ข้อกังวลที่ตัดขวางระบบเช่น authorization — ในอดีตสิ่งเหล่านี้เป็นการตัดสินใจของ Senior developer ในขณะที่ junior สร้าง implementation แต่ตอนนี้ agent ทำ implementation ดังนั้นงานจริงชิ้นแรกของ junior จึงกลายเป็นคำถามระดับ orchestration: *"Agent นี้สร้างโค้ดที่เสถียรใน framework ไหน? มัน hallucinate น้อยลงใน library ใด? pipeline นี้บังคับให้เกิดข้อแลกเปลี่ยนอะไรบ้าง?"*

เส้นทางการเติบโตกลับด้าน: แทนที่ junior จะเรียนรู้ implementation ก่อนแล้วค่อยเติบโตไปสู่การออกแบบ, พวกเขากลับ **ถูกโยนเข้าไปในการตัดสินใจเชิงออกแบบก่อนที่จะได้สั่งสม taste เพื่อใช้ในการตัดสินใจ** สิ่งนี้เชื่อมโยงโดยตรงกับ [[taste-paradox]] — การตัดสินใจระดับ senior กลายเป็นงานระดับ entry-level แต่ judgment ที่จำเป็นสำหรับงานนั้นยังไม่ได้ย้ายตามมา

**ผลกระทบต่อหลักสูตร:** orchestration ไม่ใช่หัวข้อขั้นสูงที่จะสอนในช่วงท้ายๆ อีกต่อไป; แต่เป็นทักษะที่ต้องมีตั้งแต่วันแรก

## ดูเพิ่ม

- [[advisor-strategy]]
- [[harness-engineering]]
- [[coding-harness]]
- [[subagent-patterns]]
- [[engineering-role-shift]]
- [[domain-to-ai-translator]]
- [[model-context-protocol]]
- [[llm-coding-pitfalls]]
- [[software-engineer-role-ai-era]]
- [[panutat-tejasen]]
- [[taste-paradox]]
- [[nattee-niparnan]]
- [[llm-era-computer-engineering-nattee]]
- [[alex-ker]]
- [[humanlayer]]
