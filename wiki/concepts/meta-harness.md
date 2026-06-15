---
title: Meta-Harness
type: concept
tags: [ai, agents, harness, orchestration, interoperability, security, collaboration]
created: 2026-06-15
updated: 2026-06-15
sources: ["Introducing Omnigent A Meta-Harness to Combine, Control and Share Your Agents.md"]
---

# Meta-Harness / ชั้นควบคุมเหนือ Harness

**Meta-harness** คือชั้นซอฟต์แวร์ที่อยู่เหนือ [[coding-harness|agent harness]] หลายตัว. ถ้า harness ทำให้ model หนึ่งตัวใช้ tool, file และ context ได้ meta-harness จะทำให้ harness หลายแบบประกอบกัน, ใช้ policy กลาง และแชร์ session กับคนอื่นได้.

[[omnigent|Omnigent]] จาก [[databricks|Databricks]] เสนอคำนี้ในรูปผลิตภัณฑ์ open-source alpha. ปัญหาที่มันพยายามแก้คือ Claude Code, Codex, Pi และ custom agent ต่างมี session, interface และ control ของตัวเอง. พอ workflow ข้ามเครื่องมือเหล่านี้ context กับ policy กลับไม่ตามไปด้วย.

## อยู่ตรงไหนในกอง agent

มองเป็นชั้นได้แบบนี้:

| ชั้น | หน้าที่หลัก |
|---|---|
| Model | สร้างคำตอบและตัดสินใจ |
| [[coding-harness\|Harness]] | ทำให้ model ใช้ tool, file, context และ loop ได้ |
| [[loop-engineering\|Loop]] | หางาน, แจกงาน, ตรวจงาน และวนต่อเอง |
| **Meta-harness** | ทำให้หลาย harness/loop ใช้ interface, policy และ collaboration surface ร่วมกัน |

เส้นแบ่งระหว่าง loop กับ meta-harness ยังไม่ตายตัว. Loop เน้น workflow ที่ทำงานต่อเนื่อง ส่วน meta-harness เน้น interoperability และ control plane ข้าม harness. ระบบเดียวอาจทำทั้งสองหน้าที่ได้.

**ได้อะไร:** ทีมออกแบบ workflow ระดับบนโดยไม่ต้องผูกทุกอย่างกับ agent tool ตัวเดียว.

## สามหน้าที่หลัก

### Composition

Meta-harness ทำ adapter ให้ agent ต่างชนิดมี interface กลาง. Omnigent สรุป boundary ว่า messages/files เข้า และ text streams/tool calls ออก. ดังนั้น workflow เดิมสลับ Claude Code, Codex, Pi หรือ SDK ได้ง่ายขึ้น และ subagent ในงานเดียวกันใช้คนละ harness ได้.

**ได้อะไร:** เปลี่ยน model หรือ harness โดยกระทบ orchestration น้อยลง.

### Control

Meta-harness เห็น action history ข้าม session และบังคับ policy จาก state จริงได้. ตัวอย่างเช่น หลัง agent ดาวน์โหลด package ใหม่ ต้องขออนุมัติก่อน push หรือหยุด session เมื่อค่า LLM ถึง budget.

นี่คือ enforcement layer ที่อยู่นอก prompt. มันตรงกับ [[agent-runtime-untrusted|หลักที่ถือว่า runtime ของ agent เชื่อไม่ได้]]: อย่าขอให้ model อยู่ในกรอบอย่างเดียว ให้ระบบทำสิ่งนอกกรอบไม่สำเร็จด้วย.

**ได้อะไร:** policy เดียวใช้ข้าม agent หลายตัว และ audit ได้จากเหตุการณ์จริง.

### Collaboration

Meta-harness ทำให้ live session และ working directory เป็นพื้นที่ร่วมงาน. คนอื่นเข้าดูไฟล์, comment และ steer agent จาก state เดียวกันได้ แทนการ copy-paste ผลลัพธ์ระหว่าง chat, Docs และ Slack.

สิ่งนี้ลด context-switch และ handoff cost แต่ไม่กำจัด [[orchestration-tax|ภาษีค่าควบคุมวง]]. คนยังต้องใช้ judgement ตรวจและรับผิดชอบงานสุดท้าย.

**ได้อะไร:** ทีมคุยกันบนงานจริงที่กำลังรัน ไม่ใช่คำบอกเล่าที่หลุดจาก context.

## ความเสี่ยงและคำถามเปิด

- **Lowest-common-denominator API** — interface กลางอาจซ่อนความสามารถเฉพาะของแต่ละ harness
- **Control-plane concentration** — เมื่อ policy, credential, cost และ session รวมที่เดียว จุดนี้จะกลายเป็นระบบสำคัญที่ต้อง harden และ audit มาก
- **Adapter maintenance** — harness ด้านล่างเปลี่ยนเร็ว ตัวเชื่อมต้องตามให้ทัน
- **Governance ownership** — policy กลางช่วยลดความซ้ำ แต่ความผิดพลาดหนึ่งจุดอาจกระทบ agent ทั้ง fleet
- **Human bottleneck** — แชร์ session ง่ายขึ้นไม่ได้แปลว่า review bandwidth เพิ่มตาม

## ความสัมพันธ์กับแนวคิดใกล้เคียง

- [[harness-engineering]] ออกแบบ runtime และ control รอบ agent; meta-harness ยก control เหล่านั้นขึ้นไปใช้ข้ามหลาย harness
- [[loop-engineering]] ออกแบบระบบที่ prompt agent เอง; meta-harness เป็นพื้นกลางให้ loop ประกอบ agent ต่างชนิดและคุม policy ร่วมกัน
- [[model-context-protocol|MCP]] ทำ interface กลางระหว่าง agent กับ tool; meta-harness ทำ interface กลางระหว่าง harness/session/policy
- [[agent-runtime-untrusted]] ให้เหตุผลว่าทำไม policy ต้องอยู่นอก model; meta-harness เป็นจุดหนึ่งที่วาง policy นั้นได้

## See also

- [[introducing-omnigent-meta-harness]]
- [[omnigent]]
- [[databricks]]
- [[coding-harness]]
- [[harness-engineering]]
- [[loop-engineering]]
- [[agent-runtime-untrusted]]
- [[orchestration-tax]]
- [[model-context-protocol]]
