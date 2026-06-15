---
title: Omnigent
type: entity
tags: [ai, agents, harness, orchestration, security, open-source]
created: 2026-06-15
updated: 2026-06-15
sources: ["Introducing Omnigent A Meta-Harness to Combine, Control and Share Your Agents.md"]
---

# Omnigent / ออมนิเจนต์

**Omnigent** คือ open-source [[meta-harness|meta-harness หรือชั้นควบคุมเหนือ harness หลายตัว]] จาก [[databricks|Databricks]]. เปิดตัวแบบ alpha เมื่อ 13 มิถุนายน 2026 ภายใต้ Apache 2.0.

Omnigent ไม่ได้พยายามแทน Claude Code, Codex, Pi หรือ agent SDK. มันครอบเครื่องมือเหล่านี้ด้วย interface กลาง แล้วเพิ่มความสามารถที่ต้องมองข้ามหลาย harness พร้อมกัน เช่น composition, contextual policy, cost control, sandbox และ live collaboration.

## สถาปัตยกรรม

- **Runner** — ครอบ agent ใน sandboxed session และแปลง interface ให้เหมือนกัน
- **Server** — เก็บ policy และ sharing แล้วเปิด session ผ่าน terminal, app และ web API
- **Common boundary** — รับ messages/files และส่ง text streams/tool calls

Policy ของ Omnigent จำสิ่งที่เกิดใน session ได้. เช่น ถ้า agent เพิ่งลง package จาก npm ระบบบังคับให้ขออนุมัติก่อน `git push` ได้ หรือ inject credential ที่ egress proxy เฉพาะ request ที่ผ่านกฎ โดยไม่ให้ agent เห็น secret.

**ผลคือ:** policy และ skill ระดับบนเดินทางข้าม model และ harness ได้ง่ายขึ้น.

## สถานะและข้อควรระวัง

Omnigent ยังเป็น alpha. แนวคิด common API ทำให้สลับ agent ง่าย แต่ adapter อาจซ่อนหรือลดความสามารถเฉพาะของ harness แต่ละตัว. คำเปรียบเทียบว่า meta-harness จะเป็นชั้นแบบ Kubernetes/Terraform ของ agent จึงยังเป็นเดิมพันของผู้สร้าง.

## See also

- [[introducing-omnigent-meta-harness]]
- [[databricks]]
- [[meta-harness]]
- [[coding-harness]]
- [[agent-runtime-untrusted]]
