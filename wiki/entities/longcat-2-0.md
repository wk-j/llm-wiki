---
title: LongCat 2.0
type: entity
tags: [ai, llm, china, moe, hardware]
created: 2026-07-03
updated: 2026-07-03
sources: [chinas-models-no-longer-need-western-hardware.md]
---

# LongCat 2.0 / ลองแคต 2.0

LongCat 2.0 คือ model ที่ [[meituan|Meituan]] เปิดตัวตามคำเล่าของ [[prompt-engineering|Prompt Engineering]] ในวิดีโอ [[chinas-models-no-longer-need-western-hardware|China's Models No Longer Need Western Hardware]]. คลิปบอกว่าเป็น 1.6T-parameter [[mixture-of-experts|MoE]] model ที่ train โดยไม่ใช้ NVIDIA GPUs หรือ Google TPUs.

## ภาพรวมจากแหล่งนี้

คลิปวาง LongCat 2.0 เป็นกรณีศึกษาว่า lab จีนเริ่ม scale model ใหญ่ได้ด้วย custom AI chips และ software stack ของตัวเอง ไม่ต้องพึ่ง CUDA เป็นแกนกลางเหมือน frontier labs ฝั่งตะวันตก

ตัวเลขที่คลิปให้ไว้:

- 1.6T total parameters
- 48B active parameters ต่อ token
- train บน custom AI chips มากกว่า 50,000 ตัว
- train ด้วยข้อมูลมากกว่า 35T tokens
- มีชื่อใช้งานบน OpenRouter ว่า Owl Alpha ตามคำกล่าวในคลิป

ตัวเลขเหล่านี้ควรอ่านเป็น source-attributed เพราะคลิปเองเตือนว่า benchmark เป็น self-reported in-house benchmarks.

## เทคนิคที่คลิปเน้น

LongCat 2.0 ไม่ได้พึ่ง scale ดิบอย่างเดียว แต่เอาหลายวิธีมาลดต้นทุนพร้อมกัน:

- [[n-gram-embeddings|n-gram embeddings]] เพื่อเพิ่มข้อมูลใน embedding table แทนการเพิ่ม expert อย่างเดียว
- [[sparse-attention|sparse attention]] แบบปรับให้ memory access คาดเดาได้และ cache ข้าม layer ได้
- [[speculative-decoding|speculative decoding]] ด้วย picker / draft network ที่เบากว่า
- hardware แยกมุมคิดระหว่าง prefill ที่ compute-bound กับ decode ที่ memory-bound

**ได้อะไร:** LongCat เป็นตัวอย่างของ model efficiency แบบทั้ง stack ตั้งแต่ architecture, inference, memory access, ไปจนถึง chip

## ข้อควรระวัง

Transcript สลับใช้ LongCat และ LongChat หลายจุด หน้านี้ใช้ชื่อ LongCat 2.0 ตาม title/description ของแหล่งข้อมูล แต่เก็บไว้เป็น open question ว่าชื่อผลิตภัณฑ์จริงและชื่อ model บน platform ต่าง ๆ ตรงกันแค่ไหน

สถานะ weights ก็ยังต้องตรวจจากแหล่งตรง เพราะคลิปบอกว่า weights กำลังจะ upload ไป Hugging Face และ "coming soon" ในช่วงที่พูด

## See also

- [[meituan]]
- [[chinas-models-no-longer-need-western-hardware]]
- [[mixture-of-experts]]
- [[n-gram-embeddings]]
- [[sparse-attention]]
- [[speculative-decoding]]
- [[sputnik-moment-ai]]
