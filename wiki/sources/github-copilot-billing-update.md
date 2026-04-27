---
title: GitHub Copilot Usage-Based Billing Update
type: source
tags: [github, ai-billing, copilot, agentic-usage]
created: 2026-04-27
updated: 2026-04-27
url: "GitHub Copilot Billing Email"
date_ingested: 2026-04-27
sources: ["github-copilot-billing-email.md"]
---

# GitHub Copilot Usage-Based Billing Update / การอัปเดตระบบคิดเงินตามการใช้งานของ GitHub Copilot

ประกาศจาก GitHub เรื่องการเปลี่ยนโมเดลการคิดเงินของ Copilot Pro และ Pro+ จากเดิมที่เป็นแบบเหมา/PRUs ไปเป็นระบบ **Usage-based billing** โดยใช้ **GitHub AI Credits** เริ่มมีผล 1 มิถุนายน 2026

## Key Takeaways / สาระสำคัญ

- **การขยับสู่ Agentic Platform**: GitHub ระบุว่า Copilot ไม่ได้เป็นแค่เครื่องมือช่วยเขียนโค้ดใน editor อีกต่อไป แต่กลายเป็น platform สำหรับ "agentic usage" (การทำงานยาวๆ หลายขั้นตอน ข้าม repository) ซึ่งกิน resource สูงมาก
- **GitHub AI Credits**: จะเข้ามาแทนที่ Premium Request Units (PRUs) โดยคำนวณตามจำนวน token (input, output, cached) ตามเรทของแต่ละ model
- **ราคาเดิม แต่จำกัดการใช้งาน**:
    - **Copilot Pro ($10/mo)**: ได้เครดิต $10
    - **Copilot Pro+ ($39/mo)**: ได้เครดิต $39
- **ส่วนที่ยังฟรี (Unlimited)**: Code completions และ Next edit suggestions ยังรวมอยู่ใน plan ปกติ ไม่หักเครดิต
- **Copilot Code Review**: จะหักทั้ง AI Credits และ **GitHub Actions minutes**
- **ไม่มี Fallback**: เมื่อเครดิตหมด จะใช้งานฟีเจอร์ที่ต้องใช้เครดิตไม่ได้จนกว่าจะรอบถัดไป หรือซื้อเพิ่ม (ต่างจากเดิมที่อาจจะมีประสบการณ์แบบจำกัดความเร็ว)

## Implications / ผลกระทบและมุมมอง

การเปลี่ยนผ่านครั้งนี้สะท้อนว่า "ต้นทุนของการทำ Agent" นั้นสูงเกินกว่าจะคิดราคาแบบ Flat rate เดิมได้ (Sustainability) และเป็นการเตรียมพร้อมรองรับ model หลากหลายตัวที่ GitHub นำเข้ามาให้เลือกใช้ ซึ่งแต่ละตัวมีต้นทุนไม่เท่ากัน

## See also
- [[github-copilot]]
- [[usage-based-billing]]
- [[agentic-usage]]
- [[github-ai-credits]]
