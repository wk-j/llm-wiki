---
title: Session Mining
type: concept
tags: [ai, agents, memory, harness, feedback-loop]
created: 2026-07-04
updated: 2026-07-04
sources: [stop-building-ai-agents-old-way.md]
---

# Session Mining / ขุดบทเรียนจาก session เก่า

**Session mining** คือการย้อนดู run หรือ session เก่าของ agent เพื่อหา pattern ที่เกิดซ้ำ แล้วเปลี่ยน pattern นั้นเป็น rule, memory, eval, hook, หรือ instruction ที่ run ต่อไปใช้ได้. แนวคิดนี้มองประวัติการทำงานของ agent เป็นข้อมูลฝึกระบบ ไม่ใช่ transcript ที่อ่านครั้งเดียวแล้วทิ้ง.

ในวิดีโอ [[stop-building-ai-agents-old-way|Stop Building AI Agents the Old Way]], [[prompt-engineering|Prompt Engineering]] เสนอว่า past agent runs คือ training data ฟรี. ถ้า agent พลาดแบบเดิมซ้ำ เช่น failed check เดิม, wrong path เดิม, หรือ shortcut เดิม เราควร mine pattern นั้นแล้วเขียนกลับเป็น rule ใน `AGENTS.md`, `prompt.md`, project instruction, หรือ agent config.

## ขุดอะไร

Session mining ไม่ได้หมายถึงสรุปทุกอย่าง. ของที่ควรมองหา:

- failure ที่เกิดซ้ำ เช่น test พังแบบเดิม หรือ agent ข้ามขั้นตอนเดิม
- path ที่เสียเวลา เช่น agent เดินไปทางผิดก่อนกลับมาแก้ทุกครั้ง
- จุดที่ context stale หรือขาด เช่น agent ใช้ข้อมูลเก่าเพราะไม่มี source ที่ถูก
- decision ที่คนแก้ซ้ำ เช่น reviewer ต้องบอก convention เดิมหลายรอบ
- evidence ที่หาย เช่น agent บอกว่าเสร็จ แต่ไม่มี log/screenshot/test มาให้

**ได้อะไร:** สิ่งที่เคยกินเวลาในหัวคนกลายเป็นข้อกำกับในระบบ.

## จาก memory เป็น rule

Session mining อยู่ระหว่าง [[agent-memory-types|episodic memory]] กับ [[agent-memory-types|procedural memory]]:

- ตอนแรกมันเริ่มจาก episodic memory: "run ครั้งก่อนเกิดอะไรขึ้น"
- ถ้า pattern ชัด มันถูกกลั่นเป็น procedural memory: "เคสแบบนี้ควรทำยังไง"

พอเขียนกลับเข้า `AGENTS.md`, skill, hook, eval, หรือ linter มันจะกลายเป็นส่วนหนึ่งของ [[harness-ratchet|harness ratchet]]: failure หนึ่งครั้งลดโอกาสเกิดซ้ำทั้งคลาส.

## ต่างจากเก็บ memory ทั่วไป

Memory ทั่วไปอาจเก็บ preference หรือ fact. Session mining เน้น **การแก้ระบบจาก failure จริง**. มันไม่ควรเพิ่ม rule เพราะกลัวล่วงหน้า แต่เพิ่มเพราะมีหลักฐานว่า pattern นั้นทำให้เสียเวลา เสียเงิน หรือทำให้งานผิด.

ข้อควรระวัง:

- rule ทุกข้อกิน instruction budget
- memory เก่าที่ไม่ prune อาจสร้าง [[memory-drift|memory drift]]
- ถ้าเขียน rule กว้างเกินไป agent อาจเลี่ยงงานถูกต้องบางอย่างไปด้วย
- บาง failure ควรแก้ด้วย deterministic check มากกว่าข้อความเตือนใน prompt

## เชื่อมกับ observability

จะทำ session mining ได้ดีต้องมี [[agent-observability|agent observability]] ก่อน. ถ้า trace, error, cost, artifact, และ decision ไม่ถูกเก็บไว้ การหา pattern จะต้องพึ่งความจำของคน. แต่ถ้า trace ถูกจัดเป็น issue class หรือ monitor ได้ session mining จะกลายเป็นงานประจำของ harness.

## See also

- [[stop-building-ai-agents-old-way]]
- [[agent-observability]]
- [[harness-ratchet]]
- [[agent-memory-types]]
- [[memory-drift]]
- [[harness-guides-sensors]]
- [[loop-engineering]]
