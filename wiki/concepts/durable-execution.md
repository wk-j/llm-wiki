---
title: Durable Execution
type: concept
tags: [infrastructure, distributed-systems, agents, reliability, durable-execution, cloud-agents]
created: 2026-06-05
updated: 2026-06-05
sources: [What we’ve learned building cloud agents.md]
---

# Durable Execution / การรันงานแบบทนทาน

**Durable execution** คือวิธีรัน workflow ที่ทนต่อ failure — เครื่องดับ, process ตาย, network สะดุด — โดยที่ state ของงานไม่หายและทำต่อจากจุดเดิมได้ โดยนักพัฒนาไม่ต้องเขียน retry, scheduling, และ recovery เองทุกครั้ง.

แนวคิดนี้สำคัญขึ้นมากกับ [[cloud-agents|cloud agent]] เพราะ agent ที่รันยาวข้ามชั่วโมง/ข้ามวันบน VM มีโอกาสเจอการสะดุดสูง.

## ปัญหาที่มันแก้

agent loop ที่อยู่ยาว ๆ คือ distributed-system workload ตัวหนึ่ง. ความเสี่ยงที่เลี่ยงไม่ได้:
- inference provider ล่มกลางคัน
- pod ต้องถูกแทนที่ / hibernate แล้ว resume
- node (เช่น EC2) ดับ

ถ้าเขียน loop แบบตรงไปตรงมา (รันจนจบบน worker เดียว) พอเจอการสะดุดอย่างใดอย่างหนึ่ง งานที่ทำค้างไว้ก็หาย ต้องเริ่มใหม่. durable execution ทำให้ state ถูกเก็บทนทานและ replay/resume ได้.

## กรณีศึกษา: Cursor ย้ายมา Temporal

ใน [[what-weve-learned-building-cloud-agents|บล็อก cloud agent ของ Cursor]] (2026-06-02, [[josh-ma|Josh Ma]]):

- เริ่มจาก **work-stealing architecture** — worker node คว้า agent มา loop จนจบ. มันคือการย้ายสิ่งที่ทำงานดีตอน local มาวางบน server ตรง ๆ และมัน **เปราะ** — reliability แค่ **"one 9"** (~90%)
- พอ cloud agent โต Cursor พบว่ากำลังจะสร้าง primitive แบบเดียวกับที่ [[temporal|Temporal]] มีอยู่แล้ว (retry, scheduling ข้ามเครื่อง, durability ข้าม node failure) เลยย้ายไปใช้ Temporal แทน
- การย้ายครั้งเดียวดัน reliability เกิน **"two 9s"** (~99%)
- ตอนนี้รองรับ **50 ล้าน+ action/วัน** ข้าม **7 ล้าน+ workflow**

บทเรียนการออกแบบ workflow:
- ย้ายจาก workflow แบบ **"eternal"** (อยู่ตลอด) → หลาย workflow **สั้น** ที่ exit เมื่อจบงานชิ้นเดียว → upgrade version ง่ายขึ้น
- แยก **activity** ออกมาเพื่อจับ timeout/retry ให้ดีขึ้น เพราะ async tool call, subagent, และ inference ล่ม เปลี่ยนสมมติฐานเดิม

## หลักคิดที่ใช้ซ้ำได้

> อย่าสร้าง durability primitive เองถ้ามี platform ที่แก้ปัญหานี้ครบแล้ว — Cursor เกือบ rebuild ทั้งชุดก่อนจะย้ายมา Temporal.

มุมนี้ต่อกับ [[long-running-agents]] โดยตรง: มอง agent เป็น **long-running server process** ไม่ใช่ request handler — checkpoint ความคืบหน้า, จัดการ partial failure, ทำให้ idempotent. เป็น engineering pattern เดียวกับที่ data pipeline ใช้มานาน เปลี่ยนแค่ subject จาก `data row` เป็น `agent decision`.

## See also

- [[temporal]]
- [[cloud-agents]]
- [[what-weve-learned-building-cloud-agents]]
- [[cursor]]
- [[long-running-agents]]
