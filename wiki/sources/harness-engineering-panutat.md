---
title: Harness Engineering — Panutat Tejasen
type: source
tags: [ai, software-engineering, education, curriculum, orchestration, thai-source]
author: Panutat Tejasen
date_ingested: 2026-04-18
sources: ["Harness Engineering - Panutat Tejasen.md"]
---

# Harness Engineering — Panutat Tejasen

โพสต์ Facebook สั้น ๆ โดย [[panutat-tejasen|Panutat Tejasen]] (2026-04-18) ตอบข้อเสนอของอาจารย์หลายท่านที่ว่า ควรสอนให้นักศึกษา "ตรวจงาน" และ "แนะนำ" AI Agent เรื่องการเลือก Framework — มุมมองของ Panutat คือ แนวทางนั้นทำไม่ได้อีกแล้ว AI รู้มากกว่ามนุษย์ และสิ่งที่ควรสอนแทนคือ *Harness Engineering*

## ใจความหลัก

- **"ตรวจ" และ "แนะนำ" AI ไม่ไหวแล้ว.** Framework / Library ที่ AI Agent เลือกใช้ เกินความรู้ของมนุษย์ส่วนใหญ่ ถ้าพยายามแทรกแซง ความเร็วที่หวังว่าจะได้ x10 จาก AI จะกลายเป็น /100 เพราะคอขวดย้ายมาอยู่ที่คน
- **สิ่งที่ควรสอน: Harness Engineering.** ออกแบบ AI Agent หลายตัวที่ทำหน้าที่ Review Code, ตรวจสอบ, สร้าง Test Cases, End-to-End Testing, Security Audit — ประกอบกันเป็น pipeline ตรวจงาน agent หลัก
- **ขอบเขตที่มนุษย์ยังมีค่า.** ออกแบบ harness (การประสาน agent หลายตัวและเกณฑ์การตรวจ) คือจุดที่คนทำได้ดีกว่า — ไม่ใช่การลงไปแข่งเขียน code หรือแข่งความรู้ library
- **น้ำเสียง.** ปิดท้ายด้วย "อย่าดราม่านะครับ แค่ความเห็นส่วนตัว" — ระบุชัดว่าเป็น observation จากประสบการณ์ใช้งานจริง ไม่ใช่ prescription

## ประโยคสำคัญ (verbatim)

> "สิ่งที่ควรทำคือ สอน 'Harness Engineering' ครับ คือ ควบคุมมันด้วยการออกแบบ AI Agent อีกหลายตัวที่ให้มัน Review Code, ตรวจสอบ, ทำ Test Cases, และ End-to-End Testing รวมถึง Security Audit ให้ได้ดี นั่นคือสิ่งที่มนุษย์ทำได้ในเวลานี้"

## ความเชื่อมโยงกับบทความอื่นใน wiki

- ยืนยันและขยายรูปแบบของ [[engineering-role-shift]] — งาน downstream (review / verification) ขยายตัว แต่ไม่จำเป็นต้องทำด้วยคน; สามารถให้ agent อีกตัวทำแทนได้
- Harness Engineering ทำให้ [[ai-orchestrator]] กลายเป็นระบบ ไม่ใช่แค่คนสั่ง agent เดี่ยว ๆ
- เทียบได้กับ [[advisor-strategy]] — แต่ advisor เป็นการเรียก advisor ที่จุดตัดสินใจเดียว ในขณะที่ harness คือ pipeline ของ agent หลายบทบาท
- ตอบ failure mode ที่ [[llm-coding-pitfalls]] (Karpathy) อธิบาย — AI เขียน code "ดูมั่นใจแต่ผิดเงียบ ๆ" harness คือการทำให้การจับ failure เหล่านี้เป็นระบบ
- สอดคล้องกับ [[judgement-vs-automation]] — งานออกแบบ harness คืองานที่ต้องใช้วิจารณญาณ จึงยังอยู่กับมนุษย์

## See also

- [[harness-engineering]]
- [[panutat-tejasen]]
- [[engineering-role-shift]]
- [[ai-orchestrator]]
- [[advisor-strategy]]
- [[llm-coding-pitfalls]]
- [[judgement-vs-automation]]
