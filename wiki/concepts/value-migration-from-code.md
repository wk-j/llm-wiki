---
title: Value Migration from Code
type: concept
tags: [ai, business-model, software-industry, strategy]
created: 2026-05-27
updated: 2026-05-27
sources: [software-after-software.md]
---

# Value Migration from Code / มูลค่าย้ายออกจากตัวโค้ด

**Value Migration from Code** คือข้อสังเกตว่ามูลค่าในอุตสาหกรรมซอฟต์แวร์กำลังย้ายออกจาก **"code ที่คนอื่นเขียนให้เราใช้"** ไปอยู่กับสินทรัพย์ประเภทอื่นที่ agent copy ไม่ได้

แนวคิดนี้มาจาก [[software-after-software|Software After Software]] ของ [[thorsten-ball|Thorsten Ball]] ข้อ 8

## คีย์ของแนวคิด

> "Software to do X has no value when an agent can do X."

ถ้า agent ทำ X ได้ ซอฟต์แวร์ที่ขายความสามารถในการทำ X ก็ขายไม่ได้อีกแล้ว เพราะลูกค้าให้ agent ของตัวเองทำได้เลย

ตามที่ Ball list ไว้ มูลค่าจะย้ายจาก code ไปอยู่กับ:

1. **Data** — ข้อมูลที่หา/สร้างใหม่ไม่ได้ (transaction history, telemetry, label, user behavior)
2. **Permissions** — สิทธิ์ในการเข้าถึงระบบ ผู้คน หรือสถานที่
3. **Distribution** — ช่องทางถึงลูกค้าและการครอบครอง attention
4. **Trust** — ความไว้ใจที่สะสมจากการส่งมอบที่ดี
5. **Compliance** — การผ่านมาตรฐานและการตรวจสอบ
6. **Regulatory position** — สิทธิ์ตามกฎหมายและใบอนุญาต
7. **Physical assets** — สินทรัพย์ทางกายภาพที่ digital agent แตะไม่ได้

## ตัวอย่างเชิง business

| Software ที่ moat = "ลูกค้าสร้างเองไม่คุ้ม" | สิ่งที่อาจเข้าแทนเมื่อ agent ราคาถูก |
|---|---|
| invoicing SaaS ทั่วไป | agent สร้าง invoice flow ให้ลูกค้าเองในวันที่ต้องการ |
| project management tool พื้นฐาน | agent ทำ PM workflow ภายในที่ตรงกับทีม |
| boilerplate CRUD product | บริษัทใช้ agent generate ตรงความต้องการของตัวเอง |

vendor ในกลุ่มแรกถูก Ball เรียกว่า "squeezed" — moat ของมันคือ "การ build เองไม่คุ้ม" และ moat นี้กำลังหดลง

## ทำไม Software Companies จะยอมรับช้าที่สุด

> "The last ones to admit all of this will be software companies. Their business models were built on the old scarcity."

Ball ชี้ว่า software companies คือกลุ่มที่ business model อิงกับสมมติฐาน "code หายาก" มากที่สุด การยอมรับว่ามูลค่าย้ายไปอยู่ที่อื่นจึงเท่ากับการยอมรับว่า business เดิมพัง

incentive structure ของพวกเขาทำให้พวกเขาเป็นกลุ่มที่จะ rationalize ปัญหามากที่สุด ไม่ใช่กลุ่มที่จะมองเห็นปัญหาก่อน

## ข้อควรระวัง

Value migration ไม่ใช่ binary แบบ "code มูลค่า 0" Ball ไม่ได้พูดว่า code ไม่มีค่าเลย แต่พูดว่า:

- "Software to do X" — มูลค่าลดลงเร็ว
- "Workflow software" — มูลค่าลดลง
- Code ที่ผูกกับ data/distribution/trust/compliance ที่ลอกไม่ได้ — ยังมีค่า

ตัวอย่าง: code ของ payment processor มีค่าน้อยกว่า license และ banking partnership ที่อยู่กับมัน. code ของ healthcare EHR มีค่าน้อยกว่า compliance certification และ doctor adoption network ที่อยู่กับมัน

ได้อะไร: ถ้าจะวางกลยุทธ์บริษัทช่วงเปลี่ยนผ่าน ให้ถามว่า **moat ของเราคืออะไรที่ไม่ใช่ code**

## ใช้ในการตัดสินใจ

| คำถาม | ถ้าคำตอบเป็น code | ถ้าคำตอบเป็น data/distribution/trust |
|---|---|---|
| ทำไมลูกค้าซื้อเรา ไม่ build เอง? | เสี่ยง — agent อาจทำให้ build เองคุ้มในไม่ช้า | ปลอดภัยกว่า |
| คู่แข่งสร้าง clone ของเราใช้เวลานานแค่ไหน? | ถ้าตอบ "code complexity" — เสี่ยง | ถ้าตอบ "ต้องรอ data accumulation 5 ปี" — ปลอดภัยกว่า |
| ถ้า Anthropic/OpenAI ขายโดยตรง เราเหลืออะไร? | ทดสอบ moat ที่แท้จริง | คำตอบที่ดีคือ asset ที่ไม่ใช่ code |

## ความสัมพันธ์กับแนวคิดอื่น

- [[code-is-free]] — เหตุผลทาง engineering ที่ทำให้ value migration เกิดขึ้น
- [[process-drag]] — implication ฝั่ง process
- [[reorganize-around-models]] — implication ฝั่งองค์กร
- [[just-in-time-software]] — ถ้าซอฟต์แวร์สร้างได้เมื่อต้องการ vendor product จะแข่งกับการ "talk one into existence" ของลูกค้า

## See also

- [[software-after-software]]
- [[code-is-free]]
- [[process-drag]]
- [[reorganize-around-models]]
- [[just-in-time-software]]
- [[engineering-role-shift]]
