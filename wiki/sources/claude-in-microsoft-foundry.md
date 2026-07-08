---
title: Claude in Microsoft Foundry is now generally available
type: source
tags: [ai, anthropic, microsoft, azure, enterprise, deployment, claude, cloud]
created: 2026-07-08
updated: 2026-07-08
sources: [claude-in-microsoft-foundry.md]
url: https://claude.com/blog/claude-in-microsoft-foundry
---

# Claude in Microsoft Foundry is now generally available

ประกาศจาก [[anthropic|Anthropic]] (2026-06-29) ว่าโมเดล [[claude|Claude]] เปิดให้ใช้แบบ **generally available (GA)** ผ่าน **[[microsoft-foundry|Microsoft Foundry]]** แล้ว. Microsoft Foundry คือแพลตฟอร์ม AI สำหรับองค์กรของ [[microsoft|Microsoft]] ที่รันอยู่บน [[azure|Azure]]. ใจความคือ ทีมองค์กรรัน inference ของ Claude ได้ในสภาพแวดล้อม Azure ของตัวเอง โดยใช้ระบบ authentication, billing, และ governance ที่มีอยู่แล้ว ไม่ต้องต่อท่อไปหา vendor ข้างนอกแยกต่างหาก.

จุดที่น่าสนใจของ source นี้: มันเป็นเรื่อง **การกระจายสินค้า (distribution) ระดับองค์กร** ไม่ใช่ความสามารถของ model. Anthropic ไม่ได้ขายว่า model เก่งขึ้น แต่ขายว่าเอา Claude ไปวางไว้ในที่ที่ทีม enterprise อยู่แล้ว (Azure) พร้อมของที่ฝ่าย IT ต้องการ — เรื่อง data อยู่ที่ไหน, ใครจ่ายบิล, ใครคุม access.

## โมเดลและฟีเจอร์ที่เปิดให้ใช้

- **[[claude-opus-4-8|Claude Opus 4.8]]** (flagship) และ **Claude Haiku 4.5** (ตัวเร็ว/ถูก) เรียกผ่าน **Messages API**
- รองรับ **prompt caching** และ **extended thinking** (โหมดคิดยาว)

## สองทางเลือกในการ deploy

source แยกวิธี deploy เป็นสองทาง ให้องค์กรเลือกตามว่าอยากได้อะไรเป็นหลัก:

1. **Hosted on Azure** — เหมาะกับทีมที่อยาก integrate กับสภาพแวดล้อม Azure เป็นหลัก. ได้ Azure identity, billing, และ governance controls แบบ native. เหมาะกับองค์กรที่อยากให้ทุกอย่างอยู่ใต้ร่ม Azure เดิม.
2. **Hosted on Anthropic** — เหมาะกับทีมที่อยากได้ **ชุดฟีเจอร์ API เต็ม** ของ Anthropic (full API feature set)

**ผลคือ:** เป็นการแลกกัน — อยู่ใน Azure เต็มตัวแลกกับความ native ด้าน governance, หรือไปทาง Anthropic เพื่อได้ฟีเจอร์ครบ.

## Data zone / ที่อยู่ของข้อมูล

- องค์กรเลือกตำแหน่งที่ประมวลผลได้ (processing location) รวมถึง **US data zone** สำหรับงานที่มีข้อกำหนดเรื่อง **data residency** (ข้อมูลต้องอยู่ในเขตที่กำหนด)
- **Anthropic เป็นผู้รัน inference เอง และทำหน้าที่เป็น data processor**

ดูแนวคิดเต็มที่ [[data-residency]] และ [[enterprise-model-deployment]].

## Billing และ governance

- **Unified invoicing** — รวมค่าใช้จ่ายเป็นบิลเดียว
- ลูกค้าที่มี **Microsoft Enterprise Agreement** เอา Azure commitments (ยอดที่ตกลงจ่ายกับ Azure ไว้แล้ว) มาใช้จ่ายค่า Claude ได้. ตรงนี้สำคัญ: มันลดแรงเสียดทานด้านจัดซื้อ เพราะทีมไม่ต้องตั้งสัญญาผู้ขายใหม่ ใช้งบก้อนเดิมได้เลย.

## ตัวอย่างลูกค้า (ตามที่ source เล่า)

source ยกลูกค้าสี่รายเป็นตัวอย่างการใช้งานจริง:

- **[[nvidia|NVIDIA]]** — Justin Boitano (VP/GM, Enterprise Computing) บอกว่า NVIDIA ปล่อย AI agent ทำงานอัตโนมัติทุกวัน และมองว่าความสามารถด้าน reasoning + coding ของ Claude มีค่ากับงานเทคนิคที่ซับซ้อน โดยเฉพาะตอนรันบน **NVIDIA GB300 GPUs**
  > "Claude models bring strong reasoning, coding and enterprise capabilities for complex technical work."
- **Bolt** — Gary Ballabio (VP Partnerships): รัน Claude บน Azure แล้วได้ throughput และความน่าเชื่อถือระดับที่ลูกค้า enterprise คาดหวัง
  > "Running Claude models on Azure has given us the sustained throughput and reliability our enterprise customers expect."
- **Everstar** — Matt Huang (Founding Product Lead): งานวิเคราะห์ความปลอดภัยนิวเคลียร์ (nuclear safety analysis) ที่ปกติใช้แรงคนราว **200 human days บีบเหลือทำเสร็จภายในวันเดียว**
  > "Between Anthropic and Azure, we get the best capabilities and security...compressed 200 human days into one day."
- **Momentic** — Jeff An (Co-founder & CTO): แปลงคำอธิบาย test เป็นภาษาอังกฤษธรรมดาให้กลายเป็นการตรวจสอบหน้าจอ (interface verification) เสิร์ฟระดับ **หลายล้าน token ต่อนาที**
  > "Serving millions of tokens per minute with the reliability our customers depend on."

**ข้อควรระวัง:** คำพูดลูกค้าและตัวเลข (200 วัน→1 วัน, ล้าน token/นาที) เป็น marketing claim จากหน้า announcement ของ Anthropic เอง ยังไม่ใช่ผลที่ wiki ตรวจอิสระ เก็บไว้เป็น source-attributed.

## เริ่มใช้งาน

เอกสารอยู่ที่ **Microsoft Learn** และ **platform.claude.com**.

## แรงตึงกับ source อื่นในwiki

น่าสนใจที่ source นี้ขัดกับภาพใน [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive]] ที่เล่าว่า Microsoft สั่งวิศวกรภายในหยุดใช้ Claude Code เพราะต้นทุนสูง. สองเรื่องนี้อยู่คนละชั้น: ชั้นหนึ่งคือ Microsoft ในฐานะ **ผู้ใช้ภายใน** (คุมค่าใช้จ่าย tooling ของตัวเอง), อีกชั้นคือ Microsoft ในฐานะ **แพลตฟอร์มขาย** (ยอมขาย Claude ให้ลูกค้า Azure เพราะมี demand). ดังนั้นไม่ได้ contradict ตรง ๆ — Microsoft ขาย Claude บน Azure ได้ ขณะที่ยังคุมค่า Claude Code ในทีมตัวเอง.

## เชื่อมกับ wiki

- [[enterprise-model-deployment]] — แก่นของ source: เอา frontier model ไปวางในคลาวด์ของลูกค้าพร้อม governance/billing
- [[data-residency]] — data zone / ข้อมูลต้องอยู่ในเขตที่กำหนด
- [[microsoft-foundry]] — แพลตฟอร์มที่ Claude ไปอยู่
- [[claude-opus-4-8]] / Claude Haiku 4.5 — model ที่เปิดให้ใช้
- [[enterprise-ai-roi]] / [[ai-token-economics]] — บริบทต้นทุน/ROI ของ AI องค์กร

## See also

- [[anthropic]]
- [[microsoft]]
- [[microsoft-foundry]]
- [[nvidia]]
- [[claude-opus-4-8]]
- [[enterprise-model-deployment]]
- [[data-residency]]
