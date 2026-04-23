---
title: OWASP
type: entity
tags: [security, organization, standards, open-source]
created: 2026-04-20
updated: 2026-04-23
sources: [owasp-apts.md]
---

# OWASP

Open Worldwide Application Security Project — มูลนิธิไม่แสวงหาผลกำไรที่เผยแพร่มาตรฐานและเครื่องมือด้านความปลอดภัยที่ดูแลโดยชุมชนและเป็นโอเพ่นซอร์ส เนื้อหาทั้งหมดของ OWASP เป็น open-license (โดยทั่วไปคือ CC BY-SA 4.0) โครงการต่างๆ จะมีวงจรชีวิต (Incubator → Lab → Flagship)

## โครงการที่อ้างอิงใน Wiki นี้

- **[[owasp-apts|APTS]]** — Autonomous Penetration Testing Standard (Incubator, v0.1.0, 2026) กรอบการกำกับดูแลสำหรับแพลตฟอร์ม pentesting อัตโนมัติ ดูที่ [[owasp-apts]]
- **WSTG** — Web Security Testing Guide (ระเบียบวิธีทดสอบ, อ้างอิงเป็นส่วนเสริมของ APTS)
- **ASVS** — Application Security Verification Standard (สิ่งที่ระบบอัตโนมัติภายใต้ APTS ควรทดสอบ *เทียบกับ*)
- **OWASP Top 10** — รายการความเสี่ยงของแอปพลิเคชันสุดคลาสสิก
- **OWASP Top 10 for Agentic Applications (2026)** — รายการความเสี่ยงเฉพาะสำหรับ agent; APTS จะจัดการความเสี่ยงของ agent ที่เฉพาะเจาะจงกับการทำ pentesting

## ตำแหน่งในภูมิทัศน์ความปลอดภัยของ Agent

ในปี 2026 OWASP ได้ขยับเข้ามาในพื้นที่ของ agentic-AI อย่างมีนัยสำคัญ APTS เป็นโครงการระดับ governance-layer สำหรับ agent ที่เป็นเครื่องมือเชิงรุก (offensive-tooling); ส่วน Agentic Apps Top 10 เป็นเหมือนแคตตาล็อกความเสี่ยงที่มาคู่กัน ทั้งสองอย่างนี้ช่วยให้ทีมความปลอดภัยมีชุดคำศัพท์สำหรับทำ threat modeling ของ agent-runtime ซึ่งเกิดขึ้นมาก่อนเฟรมเวิร์กส่วนใหญ่ของผู้จำหน่าย

## ดูเพิ่ม

- [[owasp-apts]]
- [[graduated-autonomy]]
- [[agent-runtime-untrusted]]
