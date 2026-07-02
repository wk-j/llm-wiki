---
title: Sparse Attention
type: concept
tags: [ai, attention, transformer, inference, long-context]
created: 2026-07-03
updated: 2026-07-03
sources: [chinas-models-no-longer-need-western-hardware.md, llm-loops-instead-of-chain-of-thought.md]
---

# Sparse Attention / สปาร์สแอทเทนชัน

Sparse attention คือวิธีทำ attention ที่ไม่ให้ทุก token มองทุก token ตลอดเวลา แต่เลือกมองเฉพาะส่วนที่น่าจะสำคัญ. ในแหล่ง [[chinas-models-no-longer-need-western-hardware|China's Models No Longer Need Western Hardware]] เทคนิคนี้ถูกใช้เพื่ออธิบายว่า [[longcat-2-0|LongCat 2.0]] ทำ long context ให้ถูกลงได้อย่างไร

## ปัญหาที่แก้

Attention แบบเต็มมีต้นทุนสูงมากเมื่อ context ยาว เพราะ token ใหม่ต้องมองย้อนกลับไปหา token เก่าจำนวนมาก ถ้า context ระดับแสนหรือล้าน token การมองทุกอย่างทุกครั้งแพงจนใช้งานจริงยาก

Sparse attention ลดงานด้วยการให้ model มองเฉพาะส่วนที่ relevant เช่น chunk ใกล้ ๆ, memory บางกลุ่ม, หรือ token ที่ตัวช่วยเลือกว่ามีผลต่อคำตอบ

## bottleneck ของตัวช่วยเลือก

แหล่งนี้ชี้ว่า sparse attention ไม่ได้ฟรี เพราะต้องมี helper เลือกว่าส่วนไหนสำคัญ ถ้า helper อ่าน memory แบบกระโดดไปมา หรือคำนวณซ้ำทุก layer ตัว helper เองจะกลายเป็น bottleneck

LongCat 2.0 ถูกเล่าว่าแก้ด้วยสามวิธี:

- อ่าน memory เป็น chunk ที่ predictable
- cache ผลการเลือกแล้ว reuse ข้ามหลาย layer
- เลือกแบบ coarse-to-fine คือคัดหยาบก่อนแล้วค่อยละเอียด

**ได้อะไร:** ลดต้นทุน long context โดยทำให้ทั้ง attention และตัวช่วยเลือกเป็นมิตรกับ memory bandwidth

## ความสัมพันธ์กับ KV cache

อีกด้านของปัญหา attention คือ [[kv-cache|KV cache]]: ยิ่ง context ยาวหรือ recursive depth เยอะ ยิ่งต้องเก็บ key/value มากขึ้น. Sparse attention ลดจำนวนตำแหน่งที่ต้องมอง ส่วน KV-cache optimization ลดข้อมูลที่ต้องเก็บ/อ่านเพื่อมองอดีตนั้น

ทั้งสองแนวคิดจึงแก้ bottleneck เดียวกันจากคนละด้าน: ทำให้การมองย้อนกลับไม่กิน memory bandwidth จนกลายเป็นเพดานของ inference

## ความสัมพันธ์กับ DeepSeek

คลิปบอกว่าแนวทางของ LongCat ได้แรงบันดาลใจจาก DeepSeek Sparse Attention. ใน wiki ตอนนี้มี [[mla-attention|MLA Attention]] ของ [[deepseek|DeepSeek]] อยู่แล้ว ซึ่งเป็นอีกเทคนิคหนึ่งที่ลดภาระ memory/KV cache. ทั้งสองอยู่ในตระกูลเดียวกันในแง่ "ลดราคาของการมองย้อนกลับ" แต่ไม่ควรถือว่าเป็นเทคนิคเดียวกันจนกว่าจะมี primary source ยืนยันรายละเอียด

## See also

- [[longcat-2-0]]
- [[n-gram-embeddings]]
- [[mla-attention]]
- [[kv-cache]]
- [[deepseek]]
- [[speculative-decoding]]
