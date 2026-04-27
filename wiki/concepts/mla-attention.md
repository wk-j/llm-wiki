---
title: Multi-head Latent Attention
type: concept
tags: [ai, deepseek, architecture, transformer]
created: 2026-04-27
updated: 2026-04-27
sources: [deepseek-wikipedia.md]
---

# Multi-head Latent Attention (MLA) / มัลติเฮด เลเทนท์ แอทเทนชัน

กลไก Attention รูปแบบใหม่ที่พัฒนาโดย **[[deepseek|DeepSeek]]** เพื่อลดภาระการใช้ memory และเพิ่มความเร็วในการประมวลผลของ Transformer model

## แก่นความคิด

ใน Transformer ปกติ ยิ่งเราใส่ context ยาวขึ้น ตัว "KV Cache" (ที่เก็บ Key และ Value ในแต่ละขั้นตอน) จะใหญ่ขึ้นเรื่อยๆ จนเต็ม memory ของ GPU ทำให้การประมวลผลช้าลงหรือรับ context ยาวมากๆ ไม่ไหว

MLA แก้ปัญหานี้โดยการ **"บีบอัด" (compress)** ข้อมูล Key และ Value ให้อยู่ในรูปของ Low-rank Latent Vector ก่อนที่จะนำไปใช้งาน ผลคือมันช่วยลดขนาดของ KV Cache ลงได้อย่างมหาศาล (บางกรณีลดลงได้ถึง 90% เมื่อเทียบกับ Multi-head Attention แบบเดิม) โดยที่แทบไม่เสียความแม่นยำ

## Why this helps / ผลคือ

- **ประหยัด RAM GPU:** ทำให้สามารถรัน model ขนาดใหญ่บน hardware ที่เล็กลงได้
- **รองรับ Context ยาวขึ้น:** เมื่อ KV Cache เล็กซะอย่าง เราก็ใส่ข้อมูลเข้าไปได้เยอะขึ้นโดยที่เครื่องไม่ค้าง
- **Inference เร็วขึ้น:** ลดคอขวดด้าน I/O (การอ่านเขียนข้อมูล) ทำให้ model ตอบโต้ได้ไวขึ้น

## See also

- [[deepseek]]
- [[token-optimization]]
