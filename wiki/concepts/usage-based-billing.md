---
title: Usage-Based Billing
type: concept
tags: [business-model, ai-economy, cloud-computing]
created: 2026-04-27
updated: 2026-04-27
sources: [github-copilot-billing-update.md]
---

# Usage-Based Billing / ระบบคิดเงินตามการใช้งาน

โมเดลธุรกิจที่เก็บค่าบริการตามปริมาณการใช้งานจริง (Consumption) แทนที่จะเป็นราคาเหมาจ่าย (Flat rate) ต่อเดือน

## ในบริบทของ AI (AI Context)
เนื่องจากต้นทุนการรัน AI model (Inference) ผันแปรตาม:
1.  **Model Size**: รุ่นใหญ่อย่าง [[claude-opus-4-7\|Opus]] แพงกว่ารุ่นเล็ก
2.  **Token Count**: จำนวนคำที่อ่านและเขียน
3.  **Time/Compute**: ระยะเวลาที่ใช้ประมวลผล (เช่น [[github\|GitHub Actions]] minutes)

## การปรับตัวของตลาด
ผู้ให้บริการเริ่มขยับจากระบบ Subscription แบบเดิม มาเป็นระบบที่ "ให้โควตาเริ่มต้น" (Included Credits) และถ้าใช้เกินต้องจ่ายเพิ่ม:
- **[[github-copilot]]**: เปลี่ยนมาใช้ [[github-ai-credits\|GitHub AI Credits]] เพราะ [[agentic-usage\|Agentic usage]] มีต้นทุนสูงจนแบบเหมาจ่ายไม่ยั่งยืน

## ข้อดี/ข้อเสีย
- **ข้อดี**: จ่ายตามจริง ผู้ให้บริการรักษากำไรได้ (Sustainable), รองรับ model ใหม่ๆ ที่ต้นทุนสูงได้ทันที
- **ข้อเสีย**: ผู้ใช้คาดการณ์ค่าใช้จ่ายรายเดือนได้ยากขึ้น (Budgeting difficulty), อาจเกิดอาการ "ประหยัด token" จนทำให้งานออกมาไม่ดีพอ

## See also
- [[github-ai-credits]]
- [[token-optimization]]
- [[instruction-budget]]
