---
title: Self-Healing Agent Environments
type: concept
tags: [ai, agents, cloud-agents, environment, autonomy, harness]
created: 2026-06-05
updated: 2026-06-05
sources: [What we’ve learned building cloud agents.md]
---

# Self-Healing Agent Environments / Environment ที่ซ่อมตัวเองได้

**Self-healing environment** คือทิศทางที่ [[cursor|Cursor]] มองว่าเป็นก้าวถัดไปของ [[cloud-agents|cloud agent]]: แทนที่จะเลือกแค่ระหว่าง "จูงมือ agent" กับ "หลบให้มันทำเอง" ให้ **ติดอาวุธ agent ด้วย tool ที่ใช้เข้าใจระบบรอบตัวมันเอง** แล้วให้มันแก้ปัญหา environment ของตัวเองได้.

## ปัญหา: ทางเลือกแบบ binary มันไม่พอ

harness ของ cloud agent มักติดอยู่ระหว่างสองขั้ว:
- **จูงมือ (hold its hand)** — harness double-check ทุกอย่าง, hardcode พฤติกรรม → agent ทำอะไรนอกกรอบไม่ได้
- **หลบให้ทำเอง (get out of the way)** — ยกให้ agent ตัดสินใจ → แต่พอ environment พัง (secret หาย, network บล็อก) agent ก็แค่ติดตัน ทำงานไม่คืบ

Cursor อยากข้ามทางเลือก binary นี้. ดูบริบทเรื่อง "รู้จักหลบให้ agent ทำงาน" ที่ [[cloud-agents]] และ [[coding-harness]].

## แนวคิด: ให้ agent ตรวจและซ่อม environment เอง

เป้าหมายคือให้ cloud agent **รายงานได้เองเมื่อติดขัด** แล้ว **แก้เองแบบ self-healing**:

- **secret หาย** → ตรวจเจอและรายงาน/ขอ/ตั้งค่าเอง
- **network access ถูกบล็อก** → ตรวจเจอและจัดการ
- **environment ขวางไม่ให้คืบหน้า** → วินิจฉัยตัวเองแล้วซ่อม

ตรงนี้ต่อยอดจากบทเรียนว่า [[agent-development-environment|environment ที่ไม่ครบทำให้คุณภาพงานตกแบบเงียบ ๆ]] — ถ้า agent ตรวจ environment ของตัวเองได้ อาการพังเงียบ ๆ ก็กลายเป็นปัญหาที่ตรวจจับและซ่อมได้.

## "autoinstall"

แนวทางหนึ่งที่ Cursor เล่าในบล็อกวิจัย (bootstrapping Composer with autoinstall) คือสิ่งที่เรียกว่า **"autoinstall"** — เส้นทางหนึ่งสู่ environment ที่ตั้งค่า/ซ่อมตัวเองได้.

**ได้อะไร:** ลด toil ของคนในการเตรียม environment ให้ agent ทุกครั้ง และลดเคสที่ agent นั่งติดตันเงียบ ๆ เพราะ environment ไม่พร้อม — agent ขยับเข้าใกล้การดูแลตัวเองได้มากขึ้น.

## See also

- [[cloud-agents]]
- [[agent-development-environment]]
- [[what-weve-learned-building-cloud-agents]]
- [[cursor]]
- [[coding-harness]]
