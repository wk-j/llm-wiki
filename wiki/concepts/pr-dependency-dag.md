---
title: PR Dependency DAG
type: concept
tags: [ai, agents, workflow, git, dag, concurrency]
created: 2026-04-25
updated: 2026-08-04
sources: [matt-pocock-agent-workflow.md, about-stacked-pull-requests-github-docs.md]
---

# PR Dependency DAG / กราฟความสัมพันธ์ของ PR แบบ DAG

**PR Dependency DAG** (Directed Acyclic Graph) คือโครงสร้างข้อมูลที่ใช้จัดการความซับซ้อนของการทำงานแบบขนาน (parallelism) ในระบบ [[subagent-patterns|Agentic Workflow]] โดยการสร้างกราฟระบุว่ากิ่ง (branch) หรือ Pull Request (PR) ไหนต้องเสร็จก่อนตัวไหน

แนวคิดนี้ถูกนำเสนออย่างชัดเจนใน [[matt-pocock-agent-workflow|Matt Pocock's workflow]] เพื่อให้ "Implementer Agents" สามารถทำงานพร้อมกันได้หลายตัวโดยไม่เกิด conflict ที่รุนแรง

## ทำไมต้องเป็น DAG?

ในการพัฒนาซอฟต์แวร์ งานมักจะมีความเกี่ยวข้องกัน (เช่น feature A ต้องใช้ API ที่สร้างใน feature B)
- **Nodes:** แทนแต่ละงาน หรือ PR
- **Edges:** แทนความสัมพันธ์ "Depends On"
- **Directed:** ความสัมพันธ์มีทิศทางชัดเจน
- **Acyclic:** ห้ามเกิดวงกลม (circular dependency)

## ประโยชน์ในการใช้งาน

1. **Massive Parallelism:** ระบบสามารถสั่งให้ Implementer Agents เริ่มทำงานใน node ที่ไม่มี dependencies ได้ทันทีพร้อมกัน
2. **Auto-Recomputation:** เมื่อมีงานใหม่เพิ่มเข้ามา (เช่น การสั่ง `/implement` ซ้ำ) ตัว Planning Agent สามารถคำนวณกราฟใหม่และจัดลำดับความสำคัญของงานได้โดยอัตโนมัติ
3. **Collision Avoidance:** การรู้ลำดับความสัมพันธ์ช่วยลดโอกาสที่จะเกิดการแก้ไขไฟล์เดียวกันในเวลาเดียวกัน หรือทำให้การ merge เป็นไปตามลำดับที่ถูกต้อง

## การเชื่อมโยงกับ Subagent Patterns

PR Dependency DAG คือส่วนขยายของ [[subagent-patterns#แบบที่-1-parallel-fan-out-กว้าง|Parallel Fan-out]]
- **Parallel Fan-out พื้นฐาน:** แตกงานที่อิสระต่อกัน (เช่น ค้นหา log 3 แหล่ง)
- **PR Dependency DAG:** แตกงานที่มีความเกี่ยวพันกัน โดยมี coordinator คอยควบคุมจังหวะการปล่อยงาน (orchestration) ตามสภาพของกราฟ

## ความสัมพันธ์กับ Stacked Pull Requests

[[stacked-pull-requests|Stacked pull requests]] คือ DAG แบบง่ายที่เหลือเป็นสายเดียว ทุก PR พึ่ง branch ที่อยู่ข้างล่างโดยตรง เช่น schema → API → UI จึงเหมาะกับงานที่เดินต่อกันทีละชั้น

DAG เต็มรูปแบบแตกแขนงได้ เช่น API และ mobile client อาจพึ่ง schema ตัวเดียวกัน แต่สองงานนั้นไม่พึ่งกันเอง ตรงนี้ stack เดียวแทนกราฟทั้งหมดไม่ได้ อาจต้องแยกหลาย stack แล้วให้ coordinator ดู dependency ระหว่างสาย

GitHub รองรับ stack แบบเส้นตรงเป็น native feature ใน public preview ตาม [[about-stacked-pull-requests-github-docs|เอกสารทางการ]] แต่การวางแผน DAG ที่แตกแขนงยังเป็นหน้าที่ของ workflow หรือ orchestration layer

**ผลคือ:** ใช้ stack เมื่องานเป็น chain ชัด ๆ และใช้ DAG เมื่อต้องเปิดงานอิสระหลายแขนงพร้อมกัน

## ดูเพิ่มเติม
- [[matt-pocock-agent-workflow]]
- [[subagent-patterns]]
- [[ai-orchestrator]]
- [[sandcastle]]
- [[stacked-pull-requests]]
- [[about-stacked-pull-requests-github-docs]]
