---
title: "Introducing Omnigent: A Meta-Harness to Combine, Control and Share Your Agents"
type: source
tags: [ai, agents, harness, orchestration, security, collaboration]
url: https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents
date_ingested: 2026-06-15
created: 2026-06-15
updated: 2026-06-15
sources: []
---

# Introducing Omnigent: A Meta-Harness to Combine, Control and Share Your Agents / เปิดตัว Omnigent

บทความของ [[databricks|Databricks]] (บริษัท data และ AI infrastructure) เสนอว่า agent workflow กำลังต้องการชั้นใหม่เหนือ [[coding-harness|harness]] รายตัว. ทีมเรียกชั้นนี้ว่า **[[meta-harness|meta-harness]]** และเปิด source [[omnigent|Omnigent]] ภายใต้ Apache 2.0 เพื่อเป็นตัวอย่างแรกของแนวคิดนี้.

ปัญหาตั้งต้นคือแต่ละ harness เช่น Claude Code, Codex, Pi หรือ custom agent มี interface, session, policy และวิธีรันของตัวเอง. พอใช้หลายตัว คนเลยต้องคอย copy-paste context ระหว่าง agent, Docs และ Slack. ฝั่งคนสร้าง agent ก็ต้องเขียน integration ใหม่ทุกครั้งที่เปลี่ยน harness หรือ model.

## ทำไมต้องมี meta-harness

Databricks มองว่า agent engineering ขยับจาก "เลือก model และ harness ที่ดีที่สุดหนึ่งตัว" ไปสู่ "ประกอบหลาย agent ให้ทำงานร่วมกัน". ตัวอย่างที่บทความยกมาคือ Harvey ให้ worker model เรียก frontier advisor, Anthropic ใช้ lead agent คุม subagent หลายตัว และ Genie แยก model สำหรับ planning, search และ code generation.

แต่ละ pattern ข้ามขอบเขตของ harness เดียว. ถ้าจะประกอบ agent หลายแบบ, บังคับ policy กลาง และให้คนหลายคนร่วมกันดู session ต้องมีชั้นที่มองเห็นทุก harness พร้อมกัน.

Omnigent แบ่งคุณค่าของชั้นนี้เป็นสามอย่าง:

- **Composition** — สลับหรือผสม Claude Code, Codex, Pi, SDK และ custom agent โดยไม่เขียนระบบใหม่ทั้งก้อน
- **Control** — ใช้ policy ที่จำ state ของ session ได้ เช่น หลังดาวน์โหลด package ใหม่ ต้องขออนุมัติก่อน `git push`
- **Collaboration** — แชร์ live session ผ่าน URL ให้คนอื่นดูไฟล์, comment และส่งคำสั่งได้

**ได้อะไร:** orchestration, governance และ teamwork ไม่ต้องผูกติดกับ harness ตัวใดตัวหนึ่ง.

## Interface กลาง: messages และ files เข้า, streams และ tool calls ออก

แก่นทางเทคนิคของ Omnigent คือมองข้ามรายละเอียดภายในของแต่ละ agent. ไม่ว่า harness จะเรียก LLM ยังไง interface ที่ผู้ใช้เห็นคล้ายกัน:

- ขาเข้า: messages และ files
- ขาออก: text streams และ tool calls

Omnigent ใช้ **runner** ครอบ agent แต่ละตัวใน sandboxed session แล้วเปิด uniform API. จากนั้น **server** ดูแล policy, sharing และเปิด session เดียวกันผ่าน terminal, app และ web API.

จุดนี้ต่างจากการสร้าง universal agent ใหม่. Omnigent ไม่ได้แทน harness เดิม แต่ครอบ harness ที่มีอยู่ให้กลายเป็นชิ้นส่วนที่สลับและประกอบกันได้.

**ได้อะไร:** ทีมเก็บ workflow ระดับบนไว้ได้ แม้เปลี่ยน model หรือ harness ด้านล่าง.

## ความสามารถใน alpha

Omnigent รุ่นแรกเน้นสิ่งที่ harness รายตัวมักหยุดก่อนถึง:

- **Real-time collaboration** — เชิญคนเข้าดู session, comment ไฟล์ และช่วย steer agent
- **หลาย interface ต่อ session เดียว** — เข้า agent เดิมจาก web, mobile, macOS app หรือ API
- **Cloud execution** — รันบนเครื่องตัวเองหรือ sandbox provider เช่น Modal และ Daytona
- **Contextual security policies** — policy ตัดสินจากสิ่งที่เกิดก่อนหน้า ไม่ใช่แค่ allow/deny แบบตายตัว
- **Cost policies** — ติดตามค่า LLM ต่อ session และ pause เพื่อขออนุมัติเมื่อถึง budget
- **Strong OS sandbox** — จำกัด OS access และแปลง network request ผ่าน proxy เช่น inject GitHub token เฉพาะ request ที่อนุมัติ โดยไม่ให้ agent เห็น token
- **Multi-harness authoring** — เขียน custom agent เป็น YAML แล้วเปลี่ยน harness หรือผสม subagent ต่าง harness ได้ด้วยการแก้เพียงเล็กน้อย

Policy ที่อิง state คือจุดสำคัญ. Prompt บอก agent ว่า "อย่า push หลังลง package แปลก" เป็นเพียงคำขอ แต่ meta-harness เห็น action history แล้ว block `git push` ได้จริง. แนวนี้ตรงกับ [[agent-runtime-untrusted|หลักที่ถือว่า runtime ของ agent เชื่อไม่ได้]].

**ผลคือ:** control ย้ายจากคำเตือนใน prompt ไปอยู่ใน enforcement layer ที่ audit และใช้ข้าม harness ได้.

## Session กลายเป็นพื้นที่ร่วมงาน

บทความเสนอการเปลี่ยน UX ที่สำคัญ: session และ working directory ไม่ใช่พื้นที่ส่วนตัวระหว่างคนหนึ่งกับ agent อีกต่อไป แต่กลายเป็นพื้นที่ร่วมงานสดของทีม.

คนอื่นเปิด URL เข้ามาดูสิ่งที่ agent ทำ, comment บนไฟล์ และส่งคำสั่งต่อได้. แนวนี้ลดการ copy-paste ผลลัพธ์ออกไปคุยใน Docs หรือ Slack แล้วค่อยย้อนกลับมาสั่ง agent ใหม่.

แต่ collaboration ไม่ได้ลบ [[orchestration-tax|ภาษีค่าควบคุมวง]]. มันลดต้นทุนการส่ง context และช่วยให้ review เกิดตรง session เดิม แต่ judgement และความรับผิดชอบสุดท้ายยังเป็นงานของคน.

**ได้อะไร:** handoff และ review เกิดบน state จริงของงาน แทนการเล่าซ้ำผ่านข้อความแยกส่วน.

## Roadmap และข้อจำกัด

Omnigent ยังเป็น open-source alpha. Roadmap มี automatic optimization ระดับ meta-harness ด้วย GEPA, code-based introspection แบบ MemEx/RLM, Omnigent Server MCP เพื่อให้ agent ทำงานข้าม session และ integration กับ harness เพิ่ม.

ข้อเสนอ "ชั้นใหม่แบบ Kubernetes/Terraform สำหรับ agent" ยังเป็นวิสัยทัศน์ของผู้สร้าง ไม่ใช่มาตรฐานที่พิสูจน์แล้ว. Common API แบบ messages/files/tool calls ช่วย interoperability ได้มาก แต่ความสามารถเฉพาะของแต่ละ harness อาจถูกลดทอนหรือยังต้องมี adapter เฉพาะ.

## แก่นที่ควรจำ

1. **Harness กลายเป็น silo ใหม่.** พอแต่ละตัวเก่งขึ้นแต่คุยกันไม่ได้ ปัญหาย้ายจาก model capability ไปเป็น interoperability.
2. **Meta-harness เป็น control plane เหนือ agent หลายชนิด.** มันคุม composition, policy, cost, sandbox และ collaboration.
3. **Policy ที่จำ state ได้แข็งกว่า prompt.** ระบบบังคับจาก action history จริง ไม่ต้องหวังให้ model ยับยั้งตัวเอง.
4. **Session เป็น collaboration surface ได้.** คนหลายคนดูและ steer งานจาก working state เดียวกัน.
5. **แนวคิดยังอยู่ช่วง alpha.** ประโยชน์ระยะยาวขึ้นกับ adapter quality, การรักษาความสามารถเฉพาะ harness และการยอมรับจาก ecosystem.

## See also

- [[omnigent]]
- [[databricks]]
- [[meta-harness]]
- [[coding-harness]]
- [[harness-engineering]]
- [[loop-engineering]]
- [[agent-runtime-untrusted]]
- [[orchestration-tax]]
