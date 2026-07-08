---
title: Data Residency
type: concept
tags: [ai, enterprise, data, compliance, governance, cloud]
created: 2026-07-08
updated: 2026-07-08
sources: [claude-in-microsoft-foundry.md]
---

# Data Residency / ที่อยู่ของข้อมูล

Data residency คือข้อกำหนดว่า **ข้อมูลต้องถูกเก็บและประมวลผลอยู่ในเขตภูมิศาสตร์ที่กำหนด** เช่นในสหรัฐฯ หรือในสหภาพยุโรปเท่านั้น. หลายองค์กร โดยเฉพาะสายการเงิน สุขภาพ รัฐ หรือธุรกิจที่มีสัญญากับลูกค้าเข้ม จะมีกฎว่าข้อมูลของตัวเอง (และของลูกค้า) ห้ามออกนอกเขตที่ตกลงไว้.

พอมาใช้ AI ปัญหานี้ยิ่งชัด เพราะการเรียก model ก็คือการส่งข้อมูล (prompt, เอกสาร, โค้ด) ไปประมวลผลที่ไหนสักที่. ถ้าที่นั่นอยู่นอกเขต ก็อาจผิดข้อกำหนดทันที.

## data zone แก้ปัญหานี้ยังไง

แพลตฟอร์มที่เสิร์ฟ model ให้องค์กรจึงเปิดให้เลือก **data zone** — เขตที่จะให้ inference ทำงาน. ตัวอย่างจาก [[claude-in-microsoft-foundry|Claude in Microsoft Foundry]] (2026-06-29): องค์กรเลือก **US data zone** ได้ เพื่อให้การประมวลผลอยู่ในสหรัฐฯ ตามข้อกำหนด. คู่กับเรื่องนี้คือการระบุชัดว่าใครเป็น **data processor** (ผู้ประมวลผลข้อมูล) — ในกรณีนั้น [[anthropic|Anthropic]] เป็นผู้รัน inference และเป็น data processor.

**ได้อะไร:** ทีม compliance ตอบได้ว่าข้อมูลอยู่เขตไหนและผ่านมือใคร ทำให้เอา frontier model เข้ามาใช้ได้โดยไม่ชนกฎ.

## ทำไมมันเป็นเงื่อนไขซื้อ ไม่ใช่แค่ฟีเจอร์

สำหรับองค์กรที่มีข้อผูกมัดด้าน residency, ถ้า model ไม่มี data zone ที่ถูกเขต มันก็ตกรอบตั้งแต่ต้น ไม่ว่าจะเก่งแค่ไหน. เพราะงั้น data residency จึงเป็นส่วนหนึ่งของ [[enterprise-model-deployment|การ deploy ระดับองค์กร]] ที่ตัดสินว่า model จะได้เข้าบริษัทหรือไม่ พอ ๆ กับคะแนน benchmark.

## เชื่อมกับ wiki

- [[enterprise-model-deployment]] — ภาพใหญ่ที่ data residency เป็นเสาหนึ่ง
- [[microsoft-foundry]] / [[azure]] — ช่องทางที่ให้เลือก data zone
- [[anthropic]] — data processor ในกรณี Foundry
- [[enterprise-ai-roi]] — เงื่อนไข non-functional อื่น ๆ ของ AI องค์กร

## See also

- [[claude-in-microsoft-foundry]]
- [[enterprise-model-deployment]]
- [[microsoft-foundry]]
