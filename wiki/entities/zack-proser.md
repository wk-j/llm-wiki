---
title: Zack Proser
type: entity
tags: [people, ai, software-engineering, developer-experience, workos]
created: 2026-06-11
updated: 2026-06-11
sources: [How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md]
---

# Zack Proser

**Zack Proser** เป็นวิศวกรในทีม Applied AI ของ [[workos|WorkOS]]. ใน talk [[how-to-keep-shipping-away-from-desk|How to Keep Shipping When You Walk Away from Your Desk]] เขาเสนอกรอบ [[developer-balance|Developer Balance]] สำหรับใช้ coding agent ให้เดินงานต่อได้ โดยไม่บังคับให้คนต้องนั่งเฝ้าหน้าจอหรือรับ context switch ตลอดวัน.

## แนวทางที่น่าจำ

- ให้ [[claude-code|Claude Code]] แตะ Slack และ Linear ผ่าน MCP เพื่อหา signal และปิด verification loop ในระบบจริง
- ใช้ voice-first flow เพื่อส่ง brief เร็วขึ้น
- ใช้ [[claude-code-remote-surfaces|Remote Control]] steer session บนเครื่องเดิมผ่านมือถือ
- ใช้ lint/build/test, browser verification, และ critic agent เป็น gate ก่อนเรียกคนกลับมา
- วิเคราะห์ conversation history เป็นรอบ เพื่อหา skill, hook, และ MCP integration ที่ขาด
- มองสุขภาพและการนอนเป็น constraint ของระบบทำงาน ไม่ใช่เรื่องแยกจาก productivity

จุดยืนของเขาคือ คนยังต้องรับผิดชอบ judgement, คุณภาพ, review, และการ ship. Agent ควรรับงานจุกจิกกับงานที่ตรวจเองได้ เพื่อให้คนเหลือแรงกับส่วนที่ขนานไม่ได้.

## See also

- [[how-to-keep-shipping-away-from-desk]]
- [[developer-balance]]
- [[workos]]
- [[claude-code]]
- [[orchestration-tax]]
- [[harness-ratchet]]
