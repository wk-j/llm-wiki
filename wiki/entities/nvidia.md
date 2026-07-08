---
title: NVIDIA
type: entity
tags: [company, ai, gpu, semiconductors, ai-infrastructure]
created: 2026-07-03
updated: 2026-07-08
sources: [review-lite-cohr-nok-aaoi.md, how-ai-became-more-expensive-than-workers-it-replaced.md, claude-in-microsoft-foundry.md]
---

# NVIDIA / เอ็นวิเดีย

[[nvidia|NVIDIA]] คือบริษัท GPU / AI infrastructure ที่วิดีโอ [[review-lite-cohr-nok-aaoi|Review LITE COHR NOK AAOI]] ใช้เป็นสัญญาณ demand ฝั่ง AI data center มากกว่าจะเป็นหุ้นหลักของคลิป

## บทบาทในคลิป

คลิปบอกว่า NVIDIA ลงเงินหรือให้ความไว้วางใจ [[coherent|Coherent]] ในระดับใหญ่ ทำให้ผู้พูดมองว่า Coherent มี credibility สูงในห่วงโซ่ [[photonic-interconnects|photonic interconnects]] สำหรับ AI data center

ในภาพใหญ่ NVIDIA ยังเป็นตัวแทนของคอขวดเดิมคือ GPU compute. คลิปเสนอว่าเมื่อ compute และ memory ถูก scale ขึ้น คอขวดถัดไปอาจเป็น network / optical links ที่ส่งข้อมูลระหว่างเครื่องและ switch

ใน [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]] NVIDIA โผล่อีกบทบาทหนึ่ง: ผู้ได้ประโยชน์จาก AI adoption และถูกเล่าว่า CEO กระตุ้นให้นักพัฒนาใช้ token มากขึ้น. คลิปใช้ประเด็นนี้เป็นส่วนหนึ่งของ [[tokenmaxxing|tokenmaxxing]] — การใช้ token เยอะกลายเป็นสัญญาณว่าทำงานกับ AI จริงจัง แม้บาง usage อาจไม่ได้สร้างมูลค่าจริง

## Claude บน GB300 (Microsoft Foundry, 2026-06-29)

ในประกาศ [[claude-in-microsoft-foundry|Claude in Microsoft Foundry]] NVIDIA โผล่เป็นลูกค้าตัวอย่าง. Justin Boitano (VP/GM Enterprise Computing) บอกว่า NVIDIA ปล่อย AI agent ทำงานอัตโนมัติทุกวัน และมองว่าความสามารถด้าน reasoning + coding ของ [[claude|Claude]] มีค่ากับงานเทคนิคซับซ้อน โดยเฉพาะตอนรันบน **NVIDIA GB300 GPUs**:

> "Claude models bring strong reasoning, coding and enterprise capabilities for complex technical work."

**ผลคือ:** ตอกย้ำ NVIDIA ในบทบาท "ชั้น hardware ที่ frontier model ทำงานอยู่บน" — คราวนี้เป็น Claude บน GB300 ผ่าน [[azure|Azure]].

## ข้อควรระวัง

ข้อมูลเงินลงทุนและรูปแบบดีลในหน้านี้มาจากคำกล่าวในคลิป ไม่ใช่การตรวจ filing หรือ press release โดยตรง จึงควรอ่านเป็นสัญญาณในเรื่องเล่าของคลิปก่อน

**ผลคือ:** NVIDIA ในหน้านี้ไม่ใช่ประเด็นหลัก แต่เป็นตัวชี้ว่า photonics ถูกผูกเข้ากับงบลงทุน AI data center แล้ว

## See also

- [[review-lite-cohr-nok-aaoi]]
- [[coherent]]
- [[ai-data-center-bottlenecks]]
- [[photonic-interconnects]]
- [[tokenmaxxing]]
- [[ai-token-economics]]
- [[claude-in-microsoft-foundry]]
- [[claude]]
- [[azure]]
