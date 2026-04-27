---
title: GitHub Copilot
type: entity
tags: [ai-tool, coding-assistant, agent, github]
created: 2026-04-27
updated: 2026-04-27
sources: [github-copilot-billing-update.md]
---

# GitHub Copilot / กิธับ โคไพล็อต

เครื่องมือ AI ช่วยเขียนโค้ดจาก [[github\|GitHub]] ที่พัฒนาจากการเป็น autocomplete ใน editor ไปสู่การเป็น "Agentic Platform" ที่ทำงานได้ซับซ้อนขึ้น

## วิวัฒนาการ (Evolution)

1.  **Autocomplete Era**: เน้นการเติมโค้ดสั้นๆ (Ghost text)
2.  **Chat & Context Era**: เริ่มคุยได้ ถามตอบเกี่ยวกับโค้ดในไฟล์ได้
3.  **Agentic Era (ปัจจุบัน)**: สามารถรัน session ยาวๆ, แก้ไขโค้ดข้ามหลายไฟล์, ทำ code review อัตโนมัติ และใช้ model ระดับแนวหน้า (เช่น [[claude-opus-4-7\|Claude Opus 4.7]], GPT-5)

## ระบบการคิดเงิน (Billing System)

ตั้งแต่ 1 มิถุนายน 2026 เป็นต้นไป เปลี่ยนไปใช้ระบบ [[usage-based-billing\|Usage-based billing]] ผ่าน [[github-ai-credits\|GitHub AI Credits]] เพื่อรองรับต้นทุนของ [[agentic-usage\|Agentic usage]] ที่สูงขึ้น

- **Pro/Pro+ Plans**: ยังจ่ายรายเดือนเท่าเดิมแต่จำกัดโควตาเครดิตตามราคาที่จ่าย
- **Unlimited Features**: Code completions และ Next edit suggestions ยังไม่เสียเครดิต

## See also
- [[github]]
- [[claude-code]] — คู่แข่งในตลาด AI CLI Agent
- [[opencode]] — ทางเลือก Open source
