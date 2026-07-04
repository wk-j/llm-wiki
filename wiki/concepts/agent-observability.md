---
title: Agent Observability
type: concept
tags: [ai, agents, observability, harness, operations]
created: 2026-07-04
updated: 2026-07-04
sources: [stop-building-ai-agents-old-way.md]
---

# Agent Observability / การมองเห็นการทำงานของ agent

**Agent observability** คือการออกแบบให้คนและระบบเห็นว่า agent กำลังทำอะไร ทำไมพัง ใช้ต้นทุนเท่าไร และควรแก้ตรงไหน. มันสำคัญเป็นพิเศษกับ [[long-running-agents|long-running agents]] เพราะงานรันนานเป็นชั่วโมงหรือเป็นวัน คนไม่สามารถนั่งเฝ้า transcript ดิบตลอดเวลาได้.

ในวิดีโอ [[stop-building-ai-agents-old-way|Stop Building AI Agents the Old Way]], [[prompt-engineering|Prompt Engineering]] วาง observability เป็นหนึ่งใน 7 component ของ agent ที่รันยาวได้. จุดสำคัญคือ observability เป็น **หน้าควบคุม** ระหว่างทาง ไม่ใช่ report ที่อ่านหลังงานจบ.

## ไม่ใช่แค่ log

Log ดิบตอบว่า "เกิดอะไรขึ้น" แต่ agent observability ต้องตอบคำถามที่ใช้ตัดสินใจได้:

- agent ทำ task ไหนอยู่
- cost และ latency ของ run เป็นเท่าไร
- error ซ้ำแบบไหนกำลังเกิด
- screenshot หรือ artifact ล่าสุดบอกอะไร
- key decision ที่ agent เลือกคืออะไร
- failure นี้ควร feedback กลับเข้า loop หรือควรเรียกคน

คลิปเสนอให้แยก raw logs/data ออกจาก presentation. Raw trace ต้อง search ได้ ส่วน dashboard ต้องย่อยให้คนเห็นภาพเหมือน Kanban หรือ Linear board.

**ได้อะไร:** คนใช้ judgement กับจุดที่ต้องตัดสิน ไม่ใช่เสียเวลาไล่อ่านทุก token.

## Trace กลายเป็น input ของการแก้

ในช่วง sponsor คลิปยก [[latitude|Latitude]] เป็นตัวอย่างเครื่องมือที่ trace run ด้วย cost, latency, span tree, search trace ด้วยภาษาธรรมชาติ, cluster conversation, สร้าง issue จาก failure ซ้ำ, และดึง failing trace กลับเข้า editor ผ่าน [[model-context-protocol|MCP server]].

ส่วนสำคัญไม่ใช่ชื่อ tool แต่คือ pattern: production failure ควรถูกเก็บเป็น dataset ที่ agent ใช้แก้และ verify fix ได้. ตรงนี้ทำให้ observability ต่อกับ [[harness-ratchet|harness ratchet]] และ [[session-mining|session mining]] โดยตรง.

## ความสัมพันธ์กับ orchestration tax

[[orchestration-tax|Orchestration tax]] บอกว่าคอขวดของระบบ agent มักอยู่ที่คน review และตัดสินใจ. Agent observability ไม่ได้ลบคอขวดนั้น แต่ช่วยลดงานที่ไม่ใช่ judgement:

- แทนที่จะถามว่า "agent ตัวไหนต้องดู" dashboard บอกตัวที่ error ซ้ำหรือ cost พุ่ง
- แทนที่จะอ่าน transcript ทั้งหมด trace สรุป span, artifact, และ decision ที่สำคัญ
- แทนที่จะจำเองว่าเคยพังอะไร issue view รวม failure class ให้

**ผลคือ:** observability ที่ดีทำให้คน step in เร็วและตรงจุดกว่าเดิม. Observability ที่แย่แค่เพิ่ม dashboard อีกอันให้เฝ้า.

## เชื่อมกับ harness

ใน [[harness-guides-sensors]], observability เป็น sensor ชนิดหนึ่ง. บางส่วนเป็น computational เช่น cost, latency, exit code, test result. บางส่วนเป็น inferential เช่น agent review, issue clustering, การสรุป key decision.

ใน [[harness-engineering]] และ [[coding-harness]], observability อยู่ใน component taxonomy ของ harness: logs, traces, cost, latency meter. หน้านี้ขยายว่า observability ต้องเป็น feedback surface ที่ส่งผลกลับเข้า loop ได้ ไม่ใช่ metric เฉย ๆ.

## See also

- [[stop-building-ai-agents-old-way]]
- [[latitude]]
- [[long-running-agents]]
- [[orchestration-tax]]
- [[harness-guides-sensors]]
- [[harness-ratchet]]
- [[session-mining]]
- [[coding-harness]]
