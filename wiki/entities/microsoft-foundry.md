---
title: Microsoft Foundry
type: entity
tags: [ai, microsoft, azure, cloud, platform, enterprise]
created: 2026-07-08
updated: 2026-07-08
sources: [claude-in-microsoft-foundry.md]
---

# Microsoft Foundry

Microsoft Foundry คือแพลตฟอร์ม AI สำหรับองค์กรของ [[microsoft|Microsoft]] ที่รันอยู่บน [[azure|Azure]]. มันเป็นที่ให้องค์กรเลือก, deploy, และรัน model จากหลายเจ้าภายใต้ระบบ identity, billing, และ governance ของ Azure เดิม. พูดง่าย ๆ คือ "ร้านโมเดล + ระบบควบคุม" ที่ทีม enterprise เข้าถึง model ต่าง ๆ ได้โดยไม่ต้องออกไปต่อท่อกับ vendor ทีละราย.

## บทบาทในwiki

Microsoft Foundry ถูกอ้างถึงเป็น **หนึ่งในช่องทางเสิร์ฟ (serving channel)** ของ [[claude|Claude]] มาตั้งแต่การเปิดตัว [[claude-opus-4-7|Opus 4.7]] (เม.ย. 2026) เคียงข้าง Amazon Bedrock และ Google Cloud Vertex AI.

จุดที่เป็น milestone คือประกาศ [[claude-in-microsoft-foundry|Claude in Microsoft Foundry is now generally available]] (2026-06-29): Claude ขยับจาก "มีให้ใช้" มาเป็น **generally available (GA)** เต็มตัวบน Foundry.

## สิ่งที่เปิดให้ใช้ (ณ 2026-06-29)

- **Model:** [[claude-opus-4-8|Claude Opus 4.8]] (flagship) และ Claude Haiku 4.5 ผ่าน Messages API
- **ฟีเจอร์:** prompt caching, extended thinking (คิดยาว)
- **สองทาง deploy:** *hosted on Azure* (governance/identity/billing แบบ native ของ Azure) หรือ *hosted on Anthropic* (ได้ชุดฟีเจอร์ API เต็มของ [[anthropic|Anthropic]])
- **[[data-residency|Data residency]]:** เลือก data zone ได้ เช่น US data zone; Anthropic เป็นผู้รัน inference และเป็น data processor
- **Billing:** unified invoicing; ลูกค้า Microsoft Enterprise Agreement เอา Azure commitments มาจ่ายค่า Claude ได้

ดูภาพใหญ่ของรูปแบบนี้ที่ [[enterprise-model-deployment]].

## หมายเหตุ

Microsoft Foundry เป็นชื่อที่ปรากฏในเอกสาร Anthropic; มันคือสายผลิตภัณฑ์ AI-platform บน Azure ของ Microsoft (ก่อนหน้านี้ตระกูลนี้รู้จักในชื่อ Azure AI Foundry / Azure OpenAI). wiki เก็บเฉพาะสิ่งที่ source ระบุ ส่วนความสัมพันธ์กับชื่อผลิตภัณฑ์ Azure อื่น ๆ ยังเป็นคำถามเปิดจนกว่าจะ ingest เอกสาร Microsoft โดยตรง.

## See also

- [[microsoft]]
- [[azure]]
- [[anthropic]]
- [[claude-in-microsoft-foundry]]
- [[enterprise-model-deployment]]
- [[data-residency]]
- [[claude-opus-4-8]]
