---
title: N-gram Embeddings
type: concept
tags: [ai, embeddings, transformer, llm, efficiency]
created: 2026-07-03
updated: 2026-07-03
sources: [chinas-models-no-longer-need-western-hardware.md]
---

# N-gram Embeddings / เอ็มเบดดิงแบบ n-gram

N-gram embeddings คือการทำ embedding ให้กลุ่ม token สั้น ๆ เช่น 2, 3, 4, หรือ 5 token แทนที่จะทำแค่ token เดี่ยว. ในวิดีโอ [[chinas-models-no-longer-need-western-hardware|China's Models No Longer Need Western Hardware]] เทคนิคนี้ถูกใช้เพื่ออธิบายว่า [[longcat-2-0|LongCat 2.0]] เพิ่มข้อมูลให้ model ได้ถูกกว่าการเพิ่ม expert ไปเรื่อย ๆ.

## แก่นความคิด

Embedding คือ vector ที่แทน token ให้ transformer เอาไปคำนวณต่อ ปกติ token หนึ่งตัวมี embedding หนึ่งชุด แต่หลาย pattern ในภาษามีความหมายจากคำติดกัน เช่นชื่อเฉพาะ, idiom, code phrase, หรือวลีทางเทคนิค

พอใช้ n-gram embeddings model จะมี vector สำหรับกลุ่ม token เหล่านี้ด้วย คล้ายให้ model เห็น "วลีสั้น" ตั้งแต่ต้น ไม่ต้องประกอบความหมายจาก token เดี่ยวทุกครั้ง

## ทำไมถูกกว่าการเพิ่ม expert

ใน [[mixture-of-experts|MoE]] การเพิ่ม expert ทำให้ model มี parameter รวมสูงขึ้น แต่ไม่ได้แปลว่าคุ้มเสมอ ถ้า expert เยอะเกิน router เลือกยากขึ้น และ active path อาจ sparse จนได้กำไรน้อยลง

N-gram embeddings เพิ่ม parameter ใน embedding table แทน งานหลักคือ lookup ใน dictionary ซึ่งถูกกว่าเพิ่ม expert ที่ต้องผ่าน compute path ใหญ่

**ผลคือ:** เป็นวิธีเพิ่ม corpus information โดยไม่เพิ่ม active compute ต่อ token เท่าการขยาย MoE ตรง ๆ

## Tradeoff

ข้อเสียคือ dictionary ใหญ่ขึ้นมาก เพราะจำนวน n-gram โตเร็ว พอ context ยาวและ embedding vocabulary ใหญ่ขึ้น attention / memory access ก็กลายเป็นปัญหาตามมา แหล่งนี้จึงโยง n-gram embeddings เข้ากับ [[sparse-attention|sparse attention]] เพื่อคุมต้นทุน long context

## See also

- [[longcat-2-0]]
- [[mixture-of-experts]]
- [[sparse-attention]]
- [[speculative-decoding]]
