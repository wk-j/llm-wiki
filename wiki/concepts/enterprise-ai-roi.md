---
title: Enterprise AI ROI
type: concept
tags: [ai, enterprise, economics, productivity, roi]
created: 2026-07-03
updated: 2026-07-03
sources: [how-ai-became-more-expensive-than-workers-it-replaced.md]
---

# Enterprise AI ROI / ผลตอบแทนจาก AI ในองค์กร

Enterprise AI ROI คือคำถามว่า AI ในองค์กรให้ผลตอบแทนคุ้มกับเงิน เวลา และความเสี่ยงหรือไม่. ในวิดีโอ [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]] คำถามนี้กลับมาแรงเมื่อบิล token โตเร็วและบางงานเริ่มแพงเท่าแรงงานมนุษย์

## ROI ไม่ใช่แค่ซื้อ tool แล้วประหยัดคน

AI อาจลดต้นทุนบางงานจริง แต่ ROI ระดับองค์กรต้องรวมหลายชั้น:

- ค่า token / subscription / API
- ค่า infra และ data governance
- ค่า human oversight / review / rework
- ค่า training และ change management
- ค่าเสียโอกาสเมื่อคนใช้ AI กับงานที่ไม่จำเป็น
- ค่า risk ถ้า output ผิดหรือ compliance พัง

ถ้าวัดแค่ “งานหนึ่งชิ้น AI ทำเร็วกว่าคน” จะเห็นแค่ครึ่งเดียว. ต้องถามว่าทั้ง workflow ดีขึ้นไหม และคนยังต้องตรวจอะไรอยู่

**ได้อะไร:** ROI ของ AI ต้องวัดที่ outcome หลังคนรับผิดชอบผลสุดท้ายแล้ว ไม่ใช่จำนวน prompt หรือจำนวนงานที่ agent claim ว่าทำเสร็จ

## Tokens or humans

คลิปใช้กรอบ “tokens or humans” เพื่อบอกว่าฝ่ายการเงินอาจต้องเปรียบเทียบค่า AI กับค่าแรงโดยตรงมากขึ้น ถ้า model providers ลด subsidy หรือขึ้นราคาเพื่อทำกำไร

แต่คำตอบไม่ใช่เลือกข้างเดียว. งานบางประเภท AI ถูกกว่าและเร็วกว่า เช่น coding tasks ตามที่คลิปยอมรับ งานบางประเภทเช่น call center อาจยังถูกกว่าด้วยคนเมื่อคิดต้นทุนจริง

ตรงนี้โยงกับ [[ai-labor-cost-reversal|AI labor cost reversal]]: เมื่อ unit economics เปลี่ยนจากถูกเป็นแพง บริษัทต้องกลับมาถามใหม่ว่างานไหนควร automate งานไหนควร augment และงานไหนควรให้คนทำ

## ความสัมพันธ์กับ Orchestration Tax

[[orchestration-tax|Orchestration Tax]] บอกว่าขีดจำกัดอยู่ที่ human judgement / review. Enterprise AI ROI คือมุม CFO ของปัญหาเดียวกัน: ถ้าคนยังต้องตรวจหนัก และ token ก็แพงขึ้น ผลตอบแทนจริงจะต่ำกว่าภาพ demo มาก

**ผลคือ:** AI ที่ดีสำหรับ enterprise ต้องลดงานทั้งฝั่ง production และ oversight ไม่ใช่แค่เพิ่ม output ให้คนตรวจมากขึ้น

## See also

- [[how-ai-became-more-expensive-than-workers-it-replaced]]
- [[ai-token-economics]]
- [[tokenmaxxing]]
- [[ai-labor-cost-reversal]]
- [[orchestration-tax]]
- [[ai-brain-fry]]
- [[usage-based-billing]]
