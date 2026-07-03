---
title: Tokenmaxxing
type: concept
tags: [ai, tokens, economics, workplace, metrics]
created: 2026-07-03
updated: 2026-07-03
sources: [how-ai-became-more-expensive-than-workers-it-replaced.md]
---

# Tokenmaxxing / การปั่น token ให้ดู productive

Tokenmaxxing คือพฤติกรรมใช้ AI token เยอะเกินจำเป็น เพื่อแสดงว่าใช้ AI หนัก ทำงานทันสมัย หรือทำ KPI ได้ดี. ในวิดีโอ [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]] คำนี้เป็นกลไกสำคัญที่ทำให้ demand AI ถูก inflate

## ทำไมเกิดขึ้น

ถ้าองค์กรวัดการใช้ AI ด้วยจำนวน token หรือยกย่องคนที่ “ใช้ token เยอะ” token จะเริ่มกลายเป็น status signal. คนอาจใช้ model กับงานเล็กมาก หรือให้ agent ลองหลายรอบทั้งที่ไม่จำเป็น

ปัญหาคือ token consumed ไม่ใช่งานที่เสร็จ. มันเป็นต้นทุนที่ถูกเผาเพื่อให้ได้ output หนึ่งชุด และ output นั้นอาจยังต้องให้คนตรวจต่อ

**ได้อะไร:** วัด token เป็น proxy ของ productivity เสี่ยงมาก เพราะมันให้คะแนน input cost แทน outcome

## ความเสี่ยงทางเศรษฐศาสตร์

Tokenmaxxing ทำให้ [[ai-token-economics|AI token economics]] เพี้ยนสองทาง:

1. ฝั่งบริษัทผู้ใช้เห็น bill สูงขึ้น แต่ไม่รู้ว่า usage ไหนสร้าง value จริง
2. ฝั่งตลาด infrastructure เห็น demand สูงขึ้น อาจลงทุน data center ตาม demand ที่มีส่วนหนึ่งเป็น demand เทียม

ถ้า demand เทียมไปเจอกับ supply ที่ตึง เช่น GPU, data center, power, และ networking ราคา token ก็อาจสูงขึ้นสำหรับทุกคน แม้บาง usage ไม่ได้สร้างมูลค่าจริง

**ผลคือ:** tokenmaxxing ไม่ใช่แค่พนักงานใช้ของเปลือง แต่มันทำให้สัญญาณตลาด AI infrastructure อ่านยากขึ้น

## วิธีแก้เชิง workflow

- วัด outcome ไม่ใช่ token consumed
- แยกงานที่ควรใช้ model ใหญ่กับงานที่ model เล็กพอ
- ใช้ [[usage-based-billing|usage-based billing]] พร้อม budget guardrail ไม่ใช่แค่เปิด faucet
- ทำ [[token-optimization|token optimization]] ที่ไม่ทำให้คุณภาพตก
- ผูก AI usage กับ artifact ที่ตรวจได้ เช่น diff, test, report, ticket closed, หรือ customer outcome

## See also

- [[how-ai-became-more-expensive-than-workers-it-replaced]]
- [[ai-token-economics]]
- [[enterprise-ai-roi]]
- [[agentic-usage]]
- [[usage-based-billing]]
- [[token-optimization]]
