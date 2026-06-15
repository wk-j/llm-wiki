---
title: WorkOS
type: entity
tags: [company, developer-tools, enterprise-software, ai]
created: 2026-06-11
updated: 2026-06-11
sources: [How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md]
---

# WorkOS

**WorkOS** เป็นบริษัท developer tools ที่ทำ API สำหรับช่วยให้ซอฟต์แวร์รองรับลูกค้าองค์กร เช่นระบบที่ใช้ขายผลิตภัณฑ์ขึ้นตลาด enterprise. [[zack-proser|Zack Proser]] ทำงานอยู่ในทีม Applied AI ของบริษัท.

ใน talk [[how-to-keep-shipping-away-from-desk|How to Keep Shipping When You Walk Away from Your Desk]] Zack ใช้งานจาก WorkOS เป็นตัวอย่าง: เขาสร้าง Slack bot สำหรับช่วยคนในบริษัททำ blog post แล้วให้ [[claude-code|Claude Code]] แก้ bug ของ sentence-case enforcer พร้อม verify ผ่าน Slack workflow จริง.

ตัวอย่างนี้สำคัญเพราะ agent ไม่ได้ตรวจแค่ source code. มันเข้าถึงระบบที่ feature ใช้งานจริง แล้วปิด loop ตั้งแต่แก้โค้ดจนเห็น output ปลายทาง.

## See also

- [[zack-proser]]
- [[how-to-keep-shipping-away-from-desk]]
- [[developer-balance]]
- [[claude-code]]
- [[model-context-protocol]]
