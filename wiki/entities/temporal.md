---
title: Temporal
type: entity
tags: [infrastructure, durable-execution, workflow, distributed-systems, agents]
created: 2026-06-05
updated: 2026-06-05
sources: [What we’ve learned building cloud agents.md]
---

# Temporal

**Temporal** คือ platform สำหรับ **durable execution** — รัน workflow ที่ทนต่อ failure ได้ โดยที่นักพัฒนาไม่ต้องเขียน retry, scheduling, และ state recovery เอง. ดูแนวคิดที่ [[durable-execution]].

มันแก้ปัญหาคลาสสิกของระบบกระจาย: เครื่องดับ, process ตาย, network สะดุด — แล้วงานที่ทำค้างไว้ต้องไม่หายและทำต่อได้จากจุดเดิม. Temporal จับ state ของ workflow ไว้ทนทาน แล้ว replay/resume ให้เองเมื่อมีอะไรล่ม.

## ทำไมโผล่ในวิกินี้ — Cursor ย้ายมาใช้ Temporal

ใน [[what-weve-learned-building-cloud-agents|บล็อก cloud agent ของ Cursor]] (2026-06-02) [[josh-ma|Josh Ma]] เล่าว่า [[cursor|Cursor]] เริ่มจาก **work-stealing architecture** ที่เปราะ (reliability แค่ "one 9"). พอ cloud agent โตขึ้น Cursor พบว่ากำลังจะสร้าง primitive แบบเดียวกับที่ Temporal มีอยู่แล้ว — retry, scheduling งานข้ามเครื่อง, durability ข้าม node failure — เลยย้ายไปใช้ Temporal แทนการสร้างเอง.

ผลลัพธ์:
- reliability ขึ้นเกิน **"two 9s"** จากการย้ายครั้งเดียว
- agent loop ทนต่อ inference สะดุด, pod hibernate/resume, และรันยาวข้ามวันข้ามสัปดาห์
- รองรับ **50 ล้าน+ action/วัน** ข้าม **7 ล้าน+ unique workflow** ของ Cursor

บทเรียนการออกแบบ: Cursor ย้ายจาก workflow แบบ "eternal" → หลาย workflow สั้นที่ exit เมื่อจบงานชิ้นเดียว (upgrade version ง่ายกว่า) และแยก activity ออกมาเพื่อจับ timeout/retry ให้ดีขึ้น.

> แง่คิดที่ใช้ซ้ำได้: agent loop ที่อยู่ยาว ๆ ก็เป็น distributed-system workload ตัวหนึ่ง — pattern durability ที่ data pipeline ใช้มานานก็ใช้กับ agent ได้เลย. ตรงกับมุมใน [[long-running-agents]] ที่บอกให้มอง agent เป็น long-running server process ไม่ใช่ request handler.

## See also

- [[durable-execution]]
- [[what-weve-learned-building-cloud-agents]]
- [[cursor]]
- [[cloud-agents]]
- [[long-running-agents]]
