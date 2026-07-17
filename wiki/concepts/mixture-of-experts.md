---
title: Mixture of Experts
type: concept
tags: [ai, architecture, transformer, deepseek, inference]
created: 2026-04-27
updated: 2026-07-17
sources: [deepseek-wikipedia.md, Mellum2 Goes Open Source A Fast Model for AI Workflows  The JetBrains AI Blog.md, chinas-models-no-longer-need-western-hardware.md, kimi-k3-explained-prompt-engineering.md]
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

## LongCat 2.0: เมื่อเพิ่ม expert เริ่มไม่คุ้ม

[[longcat-2-0|LongCat 2.0]] ในวิดีโอ [[chinas-models-no-longer-need-western-hardware|China's Models No Longer Need Western Hardware]] เป็นตัวอย่าง MoE อีกแบบหนึ่ง: model รวม 1.6T parameters แต่ active 48B ต่อ token ตามคำกล่าวในคลิป

ผู้พูดชี้ว่าเพิ่ม expert ไปเรื่อย ๆ มี diminishing returns. พอ network sparse มากขึ้น performance อาจไม่ขึ้นตาม parameter รวม เพราะ router และการกระจายข้อมูลระหว่าง expert กลายเป็นข้อจำกัด

LongCat จึงเพิ่ม [[n-gram-embeddings|n-gram embeddings]] เพื่ออัดข้อมูลวลีสั้นเข้า embedding table แทนการขยาย expert อย่างเดียว แล้วคุมต้นทุน long context ด้วย [[sparse-attention|sparse attention]]

**ผลคือ:** MoE เป็นแค่หนึ่งในชุด tradeoff. ถ้า active compute แพงเกินไป ทีมอาจเพิ่มข้อมูลใน embedding หรือทำ attention ให้ถูกลงแทนการเพิ่ม expert ตรง ๆ

## Kimi K3: sparse มากขึ้น แต่ยังใหญ่ระดับ enterprise

[[kimi-k3-explained-prompt-engineering|วิดีโอ Kimi K3]] อ้างว่า [[kimi-k3|K3]] มี parameter รวม 3T, แบ่งเป็น 896 experts และ route token ละ 16 experts. จุดสำคัญไม่ใช่แค่จำนวน expert เยอะ แต่คือ router เปิดใช้เพียงบางส่วนต่อ token จึงไม่ต้องจ่าย compute เท่า dense model 3T เต็มก้อน.

อย่างไรก็ดี “ใช้แค่บาง expert” ไม่เท่ากับ “รันบน laptop ได้”. Serving ยังต้องเก็บ weights จำนวนมหาศาลและจัดการการส่งข้อมูลระหว่าง expert. ผู้พูดจึงวาง K3 ไว้ที่ enterprise/inference-provider มากกว่า local consumer.

ตัวเลข architecture ยังต้องตรวจ technical report เพราะ transcript ช่วงหนึ่งพูด “16 จาก 800” ขณะที่ description ระบุ 896.

**ได้อะไร:** MoE ลด active compute แต่ total parameters, memory และ communication ยังเป็นต้นทุนจริง.

## Why this helps / ผลคือ

- **ฉลาดเท่าเดิมแต่ประหยัดกว่า:** เราสามารถมี model ที่มี parameter รวมมหาศาล (เช่น 1 ล้านล้านตัว) แต่ตอนรันจริงใช้แค่ไม่กี่พันล้านตัว ทำให้รันได้ไวและประหยัดไฟ
- **ความเชี่ยวชาญเฉพาะด้าน:** แต่ละ Expert สามารถเรียนรู้เรื่องเฉพาะทางได้ลึกซึ้งขึ้น

## See also

- [[deepseek]]
- [[mla-attention]]
- [[mellum2]]
- [[focal-models]]
- [[longcat-2-0]]
- [[n-gram-embeddings]]
- [[sparse-attention]]
- [[kimi-k3]]
- [[kimi-k3-explained-prompt-engineering]]
