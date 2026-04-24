---
title: Agent Enablement Role
type: concept
tags: [ai, agents, careers, enterprise, roles, automation]
created: 2026-04-24
updated: 2026-04-24
sources: [aaron-levie-agent-automation-jobs.md]
---

# Agent Enablement Role / บทบาท "คนเอา Agent ไปใช้จริง" ในองค์กร

บทบาทใหม่ในองค์กรที่ **เป็นเจ้าของการเอา AI agent ไปใช้กับ workflow จริง** [[aaron-levie|Aaron Levie]] (CEO ของ Box) เสนอใน X post ปี 2026 ว่าบริษัทส่วนใหญ่ต้องจ้างคนตำแหน่งนี้เพิ่ม ไม่ใช่ปล่อยให้พนักงานแต่ละคนหา agent มาใช้กันเอง

ตำแหน่งนี้ยังไม่มีชื่อมาตรฐาน — Levie บอกตรงๆ ว่า *"จะเรียกต่างกันตามบริษัท"* บางที่อยู่ใต้ IT บางที่อยู่ใต้ engineering บางที่อยู่ใน business function ตรงๆ แต่ job spec จะคล้ายกัน

## แก่นความคิด

ระยะห่างระหว่างสองสถานะนี้ไกลกว่าที่คิด:

- **chatbot** — พนักงานเปิด ChatGPT/Claude ถามคำถาม ได้คำตอบกลับมา
- **agent ที่ automate process จริง** — agent ทำงานเองในระบบขององค์กร ดึง context ที่ถูกต้อง เรียก API ภายใน ส่งงานต่อให้คนเมื่อต้องการ และทำซ้ำได้ทุกวัน

การข้ามจาก chatbot → agent นี้ Levie บอกว่า *"requires a real amount of work"* — งานเทคนิคจริงจัง บวกกับงาน change management ในองค์กร — มากเกินกว่าจะทำเป็น side project ระหว่างวัน

## Job spec (ตามที่ Levie ระบุ)

คนคนเดียวต้องครอบคลุมทั้ง 8 ข้อนี้:

1. **Map out workflows กับ agent** — มองว่า process ไหนเหมาะ และ agent จะเสียบเข้ากับ flow เดิมอย่างไร
2. **Deploy agent เข้าระบบ** — host จริง ไม่ใช่ POC
3. **ดูแล context ให้สดใหม่** — agent ต้องเห็นข้อมูลล่าสุด ไม่ใช่ snapshot ที่ตกขอบ
4. **ต่อ internal system** — wiring ระหว่าง agent กับ DB / SaaS / API ภายใน
5. **สร้าง eval** — มีตัววัดคุณภาพที่ใช้ได้ระยะยาว
6. **ออกแบบ Human-in-the-Loop** — จุดไหนคนต้อง approve, จุดไหน agent ทำเองได้
7. **Manage system ตอน upgrade** — model เปลี่ยน version, behavior เลื่อน, ต้อง regression-test
8. **Change management** — เปลี่ยนวิธีที่คนทำงานเดิมให้เข้ากับ agent

ข้อ 1, 6, 8 เป็นงาน *กระบวนการธุรกิจ* ข้อ 2–5, 7 เป็นงาน *เทคนิค* — บทบาทนี้กิน scope ทั้งสองฝั่ง ซึ่งเป็นเหตุผลที่ Levie บอกว่ามอบหมายเป็น side project ของใครคนใดคนหนึ่งไม่ได้

## ทำไมต้องเป็นคนเฉพาะ ไม่ใช่ทุกคน

Levie ให้เหตุผลสองข้อ:

- **งานเทคนิคกว่าที่คิด** — eval design, context plumbing, HITL boundary, model-upgrade triage — ไม่ใช่แค่ "เขียน prompt เก่งๆ"
- **ทำเป็น side project ไม่ได้** — ทั้ง 8 ข้อข้างบนต้องการ ownership ต่อเนื่อง ไม่ใช่ใครว่างก็มาแตะ

ความหมายในทางปฏิบัติคือ: **ตำแหน่งงานใหม่ที่มี title และ JD ของตัวเอง** ไม่ใช่หน้าที่แถม

## บทบาทนี้อยู่ตรงไหนใน org

Levie เสนอ 3 บ้านที่เป็นไปได้:

| บ้าน | จุดแข็ง | จุดอ่อน |
|---|---|---|
| **IT** | คุ้นเคยกับ deploy + integrate ระบบเดิม | อาจไม่เข้าใจ workflow ของ business เพียงพอ |
| **Engineering** | คุ้นเคยกับ eval / context / model — ฝั่ง craft | ห่างจาก process ของหน่วยธุรกิจ |
| **อยู่ใน business function ตรงๆ** | เข้าใจ workflow และ change management ดีที่สุด | อาจขาด muscle เทคนิค |

ไม่มีคำตอบเดียว — แต่ละองค์กรจะแก้ไม่เหมือนกัน ตรงนี้คือเหตุผลที่ title ต่างกันได้

## คำทำนายที่น่าสนใจ

> "...in some sense it's the future of software engineering that you'll see a huge growth of in non-tech companies."

Levie มองว่า *บริษัท non-tech* จะเป็นที่ที่ headcount ของ "software-engineering-shaped jobs" โตเร็วที่สุดในยุค agent ไม่ใช่บริษัท tech — เพราะบริษัท tech มีคนเหล่านี้พอใช้แล้ว (ในนาม engineer) แต่บริษัท non-tech ยังไม่มี และ workflow ที่จะ automate ยังเหลืออีกมหาศาล

## ความสัมพันธ์กับบทบาทอื่นในวิกินี้

มุมของ Levie เป็นการมองจากฝั่ง **enterprise consumer** ของ AI ซึ่งเสริมกับมุมที่วิกินี้เก็บไว้แล้วจากฝั่ง builder/practitioner:

- [[ai-orchestrator]] (เนยขัวภาพ pipeline ของ agent) — **ตรงกับข้อ 1, 6, 7** ของ Levie แต่ ai-orchestrator มองในระดับ pipeline-builder ส่วน agent-enablement-role มองในระดับ org-deployer
- [[domain-to-ai-translator]] (แปลความต้องการธุรกิจเป็น AI spec) — **ตรงกับข้อ 1 และ 8** ของ Levie ในมุมที่ต้องคุยกับ stakeholder ก่อนเอา agent ลงไปใส่ workflow
- [[harness-engineering]] ([[panutat-tejasen|Panutat]]) — **ตรงกับข้อ 5, 6** ของ Levie — design pipeline ของ review/test/eval agent
- [[long-running-agents]] (Google Cloud 5 patterns) — **ตรงกับข้อ 2, 3, 6, 7** เป็น mechanic ที่ agent-enablement role ต้องรู้: checkpoint-and-resume, delegated approval (HITL), memory-layered context, fleet orchestration
- [[engineering-role-shift]] — Levie คือกรณีตัวอย่างชัดของ "downstream/upstream ขยาย ตรงกลางหด" ในโลก enterprise: ตำแหน่งนี้กิน upstream (workflow design, change management) + downstream (eval, HITL, upgrade triage) แต่ middle (เขียน CRUD เอง) หายไป — agent ทำเอง

## ความแตกต่างจาก "AI Engineer" ทั่วไป

ในวิกิและ discourse ทั่วไป "AI Engineer" มักหมายถึงคนที่ build agent — เขียน prompt, integrate model, เลือก framework แต่ Agent Enablement Role ของ Levie กว้างกว่านั้น เพราะรวม **change management** เข้ามาด้วย

ผลคือ: ตำแหน่งนี้ไม่ใช่แค่งานเทคนิค ต้องมีทักษะ stakeholder management, business analysis, internal communication ด้วย — ใกล้เคียง **AI-era version ของ Solutions Engineer** มากกว่า ML Engineer

## ดูเพิ่ม

- [[aaron-levie]]
- [[aaron-levie-agent-automation-jobs]]
- [[engineering-role-shift]]
- [[ai-orchestrator]]
- [[domain-to-ai-translator]]
- [[long-running-agents]]
- [[harness-engineering]]
- [[judgement-vs-automation]]
