---
title: Malleable Tools
type: concept
tags: [ux, development, flexibility, philosophy]
created: 2026-04-28
updated: 2026-04-28
sources: [mario-zechner-pi-agent.md]
---

# Malleable Tools / เครื่องมือที่ดัดแปลงได้

**Malleable Tools** คือแนวคิดในการสร้างซอฟต์แวร์หรือเครื่องมือที่ไม่ได้มีสถานะ "คงที่" (Rigid) แต่เปิดโอกาสให้ผู้ใช้สามารถแก้ไขโครงสร้างภายใน วิธีการทำงาน หรือหน้าตาของมันได้โดยตรงและรวดเร็วในขณะที่ใช้งานอยู่

## ในบริบทของ AI Agent

[[mario-zechner]] เสนอว่าในยุค AI ที่เรายังไม่รู้ว่า "workflow ที่ดีที่สุด" คืออะไร เครื่องมือไม่ควรจะตีกรอบให้เรา แต่ควรจะ:
- **Expose Internals**: เปิดให้เห็นว่า system prompt และกลไกของ tool ทำงานอย่างไร
- **Hot-reloading**: แก้ไขการทำงานของเครื่องมือ (เช่น สั่งให้ bash tool ทำงานผ่าน SSH) แล้วเห็นผลทันที
- **User-defined Primitives**: ให้ผู้ใช้สร้าง "เครื่องมือพื้นฐาน" ชุดใหม่ขึ้นมาได้เองตามความถัดของโปรเจกต์

## Payoff / ผลคือ
ช่วยให้ Developer สามารถสร้าง workflow ส่วนตัวที่ทรงพลังกว่าเครื่องมือสำเร็จรูปทั่วไป และลดการพึ่งพิง vendor ที่อาจเปลี่ยนพฤติกรรมของ AI ภายหลัง ([[alignment-bottleneck]])

## ดูเพิ่ม

- [[pi-agent]]
- [[harness-engineering]]
