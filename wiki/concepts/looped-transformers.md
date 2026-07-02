---
title: Looped Transformers
type: concept
tags: [ai, llm, architecture, transformer, reasoning, inference]
created: 2026-07-03
updated: 2026-07-03
sources: [llm-loops-instead-of-chain-of-thought.md]
---

# Looped Transformers / ทรานส์ฟอร์เมอร์แบบวนซ้ำ

Looped transformer คือ transformer ที่เอา block ชุดเดิมมาวนหลายรอบ ให้ hidden state ค่อย ๆ เปลี่ยนและ refine แทนการใช้ layer ไม่ซ้ำกันจำนวนมากแล้วผ่านครั้งเดียว

ใน [[llm-loops-instead-of-chain-of-thought|LLM that loops instead of Doing Chain-of-Thought]] bycloud ใช้แนวคิดนี้เป็นทางเลือกของ [[chain-of-thought|chain-of-thought]]: เพิ่ม test-time compute ภายใน model แทนการเขียน reasoning token ออกมาเป็น text

## แก่นความคิด

Transformer ปกติคือ stack ของ layer ที่ต่างกัน. Token เข้า layer 1, layer 2, layer 3 ไปเรื่อย ๆ แล้วได้ output. Looped transformer ย่อ block ให้เล็กลง แล้วรัน block เดิมซ้ำหลายรอบ

ภาพง่าย ๆ คือ model มี "กฎ update" ชุดเดียว แล้วใช้ซ้ำ:

- รอบแรกสร้าง representation หยาบของปัญหา
- รอบกลาง propagate ความสัมพันธ์และรวมข้อมูล
- รอบท้าย stabilize representation เพื่อออกคำตอบ

ถึง weight จะ shared แต่ input hidden state ของแต่ละรอบไม่เหมือนกัน function เดิมจึงทำงานต่างบทบาทได้

**ได้อะไร:** จำนวน loop กลายเป็น compute dial. ถ้าปัญหายากขึ้น อาจให้ model วนเพิ่มโดยไม่เพิ่ม parameter

## ต่างจาก Chain-of-Thought

[[chain-of-thought|Chain-of-thought]] ให้ model คิดผ่านภาษา. มันเขียน intermediate step ออกมาเป็น token แล้วอ่าน token นั้นกลับเข้า context

Looped transformer ให้ model คิดผ่าน hidden state. มัน update representation โดยตรง ไม่ต้อง decode เป็น text แล้ว embed กลับทุกครั้ง

ข้อดีเชิงสถาปัตยกรรมคือ compact กว่าและอาจประหยัด token/context. ข้อเสียคือเราไม่เห็น trace ชัด ๆ และ train/supervise intermediate step ยากกว่า

## Stability เป็นเรื่องใหญ่

พอใช้ block เดิมวนซ้ำ เรากำลังทำ [[residual-stream|residual stream]] ให้เป็น dynamical system. ถ้า update rule มีแนวโน้มเล็ก ๆ ไปทางใดทางหนึ่ง การวนหลายรอบอาจขยาย error, ทำให้ norm โต, หรือทำให้ loss spike

ดังนั้น looped transformer ต้องมี normalization/constraint ที่คุม recurrence ไม่ให้ hidden state หลุด trajectory

**ผลคือ:** looped transformer ไม่ใช่ optimization trick ง่าย ๆ แต่เป็นการออกแบบ process การคิดของ model

## ข้อจำกัด

ถ้าไม่ติดข้อจำกัด parameter หรือ memory การเพิ่ม layer/width แบบ standard transformer ยัง expressive กว่า เพราะแต่ละ layer เรียน transformation คนละแบบได้ ไม่ต้องใช้ function เดิมซ้ำ

Looped transformer จึงน่าสนใจที่สุดใน regime ที่อยากได้ effective depth เพิ่ม แต่ไม่อยากเพิ่ม parameter เช่น model เล็ก, edge deployment, distillation, หรือ synthetic data generation

## See also

- [[latent-reasoning]]
- [[multi-hop-reasoning]]
- [[mixture-of-recursions]]
- [[kv-cache]]
- [[chain-of-thought]]
- [[reasoning-regression]]
