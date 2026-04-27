---
title: GitHub AI Credits
type: concept
tags: [github, billing, tokens, ai-resource]
created: 2026-04-27
updated: 2026-04-27
sources: [github-copilot-billing-update.md]
---

# GitHub AI Credits

สกุลเงินจำลอง (Virtual currency) ของ [[github\|GitHub]] ที่ใช้สำหรับควบคุมและคิดค่าการใช้งานฟีเจอร์ AI ต่างๆ ในระบบ โดยเฉพาะ [[github-copilot\|GitHub Copilot]]

## กลไกการทำงาน
- **Token-based**: เครดิตถูกหักตามจำนวน Token (Input, Output, และ Cached Tokens)
- **Model-dependent Rates**: แต่ละ model มีราคาต่อ 1M tokens ไม่เท่ากัน (เช่น ใช้ GPT-5.5 อาจจะแพงกว่า Sonnet)
- **Included Monthly**: สมาชิก Pro ($10) จะได้เครดิตติดตัวมา $10 ต่อเดือน (ใช้หมดคือจบ หรือซื้อเพิ่ม)

## สิ่งที่ต้องใช้เครดิต (Credit-consuming)
- การคุยกับ Chat
- การสั่งให้ Agent แก้โค้ดข้ามไฟล์ (Agentic sessions)
- Copilot Code Review (ใช้อันนี้ร่วมกับ GitHub Actions minutes)

## สิ่งที่ไม่ต้องใช้เครดิต (Free/Unlimited)
- Code completions (Ghost text)
- Next edit suggestions

## ผลกระทบ
ทำให้ผู้ใช้ต้องเริ่มใส่ใจเรื่อง [[token-optimization\|Token optimization]] และการเลือก model ให้เหมาะกับงาน (เช่น งานง่ายใช้ model ถูก, งานยากใช้ model แพง) เพื่อบริหารเครดิตให้พอใช้ทั้งเดือน

## See also
- [[usage-based-billing]]
- [[agentic-usage]]
- [[github-copilot]]
