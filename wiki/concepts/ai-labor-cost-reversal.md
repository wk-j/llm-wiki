---
title: AI Labor Cost Reversal
type: concept
tags: [ai, labor, economics, automation, enterprise]
created: 2026-07-03
updated: 2026-07-03
sources: [how-ai-became-more-expensive-than-workers-it-replaced.md]
---

# AI Labor Cost Reversal / จุดกลับด้านต้นทุน AI กับแรงงาน

AI labor cost reversal คือสถานการณ์ที่ AI ซึ่งเคยถูกขายว่า “ถูกกว่าแรงงาน” เริ่มมีต้นทุนใกล้หรือแพงกว่าคนในบางงาน. วิดีโอ [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]] ใช้เรื่องนี้เป็น thesis หลัก

## ไม่ได้เกิดกับทุกงาน

คลิปไม่ได้บอกว่า AI แพงกว่าคนเสมอ. มันแยกงานออกเป็นหลายกลุ่ม:

- coding tasks: คลิปบอกว่า AI ยังถูกกว่าคนอย่างชัดเจน
- data entry: ส่วนต่างเริ่มน้อย
- call centers: คลิปอ้างว่าคนถูกกว่า AI ในบางกรณี

ตรงนี้สำคัญ เพราะคำว่า “AI replaces workers” มักถูกพูดเหมารวม แต่ economics จริงขึ้นกับ task, wage, quality requirement, latency, compliance, และปริมาณ oversight ที่ต้องใช้

**ได้อะไร:** Automation decision ต้องแยกตามงาน ไม่ใช่ใช้คำว่า AI เป็นคำตอบเดียวทั้งองค์กร

## ทำไมต้นทุนกลับด้านได้

ต้นทุน AI อาจขึ้นหรือดูแพงขึ้นจากหลายเหตุ:

- [[ai-token-economics|token price]] เพิ่ม
- usage ขยายทั้งองค์กร
- [[tokenmaxxing|tokenmaxxing]] ทำให้ demand เทียมปนกับ demand จริง
- data center / power / hardware supply ตึง
- model providers ลด subsidy หลังต้องทำกำไร
- งานที่ AI ทำยังต้องมีคนตรวจและแก้

ถ้างานนั้นค่าแรงถูกอยู่แล้ว หรือคุณภาพ AI ยังต้องใช้ oversight เยอะ AI อาจไม่ชนะต้นทุนรวม

## เมื่อเทียบกับกรอบเดิม

หน้า [[code-is-free|Code is Free]] ใน wiki วางกรอบว่า implementation cost ต่ำลงมากในงาน software. AI labor cost reversal เพิ่มเงื่อนไขว่า “ถูก” ต้องนับทั้ง token, infra, oversight, และ usage waste ด้วย

สองกรอบนี้อยู่ร่วมกันได้ถ้าแยก scope:

- ในงาน coding / refactor ที่ verify ได้ดี AI อาจทำให้ code production ถูกมากจริง
- ใน workflow enterprise กว้าง ๆ ที่วัด output ยากและต้องคุมเยอะ AI อาจแพงกว่าที่ demo ทำให้เชื่อ

## See also

- [[how-ai-became-more-expensive-than-workers-it-replaced]]
- [[enterprise-ai-roi]]
- [[ai-token-economics]]
- [[code-is-free]]
- [[usage-based-billing]]
- [[ai-brain-fry]]
