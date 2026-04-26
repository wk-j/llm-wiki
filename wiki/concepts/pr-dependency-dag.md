---
title: PR Dependency DAG
type: concept
tags: [ai, agents, workflow, git, dag, concurrency]
created: 2026-04-25
updated: 2026-04-25
sources: [matt-pocock-agent-workflow.md]
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

## ดูเพิ่มเติม
- [[matt-pocock-agent-workflow]]
- [[subagent-patterns]]
- [[ai-orchestrator]]
- [[sandcastle]]
