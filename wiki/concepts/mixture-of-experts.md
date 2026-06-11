---
title: Mixture of Experts
type: concept
tags: [ai, architecture, transformer, deepseek, inference]
created: 2026-04-27
updated: 2026-06-05
sources: [deepseek-wikipedia.md, Mellum2 Goes Open Source A Fast Model for AI Workflows  The JetBrains AI Blog.md]
---

# Mixture of Experts (MoE) / มิกซ์เจอร์ ออฟ เอ็กซ์เพิร์ตส์

สถาปัตยกรรม model ที่ไม่ได้ทำงานพร้อมกันทุกส่วน แต่จะเลือกใช้ "ผู้เชี่ยวชาญ" (Experts) เฉพาะจุดมาตอบคำถามแต่ละประเภท เพื่อความประหยัดและรวดเร็ว

## แก่นความคิด

แทนที่จะสร้าง model ขนาดใหญ่ยักษ์ที่เป็นก้อนเดียว (Dense Model) เราแบ่งภายในออกเป็นเครือข่ายย่อยๆ หลายตัว (Experts) พอมีคำถามเข้ามา จะมีตัวช่วยเลือก (Router) ส่งคำถามนั้นไปให้ Expert ที่เก่งเรื่องนั้นที่สุดเพียง 1-2 ตัวทำงาน

**DeepSeekMoE** (ฉบับปรับปรุงโดย DeepSeek) ได้เพิ่มแนวคิด:
- **Shared Experts:** Expert ส่วนกลางที่ต้องทำงาน "ทุกครั้ง" เพื่อเก็บความรู้พื้นฐาน
- **Routed Experts:** Expert เฉพาะทางที่จะถูกเรียกใช้ตามความเหมาะสม

## ตัวอย่าง production-focused: Mellum2

[[mellum2|Mellum2]] ของ [[jetbrains|JetBrains]] ใช้ MoE ในมุมที่ practical มาก: model มี parameter รวม 12B แต่ active แค่ 2.5B parameters ต่อ token เป้าหมายคือ latency, throughput, และ cost ของงาน software engineering workflow เช่น routing, RAG, และ subagent ขั้นย่อย

ตรงนี้ขยับ MoE ออกจากเรื่อง "model ใหญ่แต่ฉลาด" อย่างเดียว Mellum2 ใช้ MoE เพื่อทำ [[focal-models|focal model]] ที่ deploy ง่ายและตอบเร็ว

**ผลคือ:** MoE ไม่ได้มีค่าแค่ทำ model ใหญ่ขึ้น แต่มีค่าเมื่ออยากทำ model เฉพาะทางที่ต้นทุน inference ต่ำลง

## Why this helps / ผลคือ

- **ฉลาดเท่าเดิมแต่ประหยัดกว่า:** เราสามารถมี model ที่มี parameter รวมมหาศาล (เช่น 1 ล้านล้านตัว) แต่ตอนรันจริงใช้แค่ไม่กี่พันล้านตัว ทำให้รันได้ไวและประหยัดไฟ
- **ความเชี่ยวชาญเฉพาะด้าน:** แต่ละ Expert สามารถเรียนรู้เรื่องเฉพาะทางได้ลึกซึ้งขึ้น

## See also

- [[deepseek]]
- [[mla-attention]]
- [[mellum2]]
- [[focal-models]]
