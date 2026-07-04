---
title: Latitude
type: entity
tags: [ai, agents, observability, open-source, tooling]
created: 2026-07-04
updated: 2026-07-04
sources: [stop-building-ai-agents-old-way.md]
---

# Latitude / เครื่องมือ observability สำหรับ agent

Latitude คือเครื่องมือ [[agent-observability|agent observability]] ที่ถูกแนะนำในวิดีโอ [[stop-building-ai-agents-old-way|Stop Building AI Agents the Old Way]] ของ [[prompt-engineering|Prompt Engineering]]. คลิปบอกว่า Latitude เป็น open-source MIT licensed และมี hosted version สำหรับคนที่ไม่อยาก run เอง.

## บทบาทใน source

ในคลิป Latitude ถูกใช้เป็นตัวอย่างของหน้าควบคุมสำหรับ [[long-running-agents|long-running agents]]: ไม่ใช่แค่ดู log หลังจบ แต่ดูได้ว่า agent กำลังทำอะไร, อะไรพัง, และจะแก้ยังไง.

ฟีเจอร์ที่คลิปกล่าวถึง:

- trace ทุก run ด้วย cost, latency, และ span tree
- search traces ด้วยภาษาธรรมชาติ
- cluster conversations หลายพันรายการเป็น pattern เดียว
- รวม failure ซ้ำ ๆ เป็น issue view
- สร้าง eval จาก failure เดิม และ save search เป็น monitor
- ดึง failing traces เข้า editor ผ่าน [[model-context-protocol|MCP server]] เพื่อให้ coding agent แก้จากหลักฐานจริง

ข้อมูลนี้มาจากช่วง sponsor ในวิดีโอ จึงควรอ่านเป็น claim จาก source ก่อน ยังไม่ได้ตรวจ repo หรือ docs ของ Latitude โดยตรง.

## ทำไมสำคัญกับ wiki

Latitude เป็นตัวอย่างที่ทำให้ [[orchestration-tax|orchestration tax]] จับต้องได้ขึ้น. ถ้า agent รันนานหลายชั่วโมง คนไม่ควรต้องอ่าน transcript ดิบทั้งหมด. ระบบต้องจัด trace, error, cost, และ decision ให้อยู่ในรูปที่ตัดสินใจได้เร็ว.

## See also

- [[stop-building-ai-agents-old-way]]
- [[agent-observability]]
- [[long-running-agents]]
- [[orchestration-tax]]
- [[model-context-protocol]]
