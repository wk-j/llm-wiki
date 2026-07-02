---
title: Mixture of Recursions
type: concept
tags: [ai, llm, architecture, inference, efficiency, routing]
created: 2026-07-03
updated: 2026-07-03
sources: [llm-loops-instead-of-chain-of-thought.md]
---

# Mixture of Recursions / การผสมความลึกแบบ recursive

Mixture of Recursions (MoR) คือแนวคิดให้ token แต่ละตัวใช้จำนวน recurrence ไม่เท่ากัน. Token ง่ายออกเร็ว Token ยากวนต่อ

ใน [[llm-loops-instead-of-chain-of-thought|LLM that loops instead of Doing Chain-of-Thought]] bycloud ใช้ MoR เป็นคำตอบของปัญหาใน [[looped-transformers|looped transformer]] แบบตรง ๆ: ถ้าทุก token วนเท่ากัน เราเสีย compute กับ token ที่ไม่ต้องคิดเยอะ

## Router เลือกความลึก

MoR เพิ่ม router เพื่อเลือกว่า token ต้องผ่าน recursion กี่รอบ. คลิปเล่าสองแบบ:

- **Token choice routing**: ก่อนวน ให้ token ถูกส่งไป depth bucket ที่กำหนดไว้ เช่น 1, 2, 3 recurrence วิธีนี้ง่ายและ efficient แต่ถ้าทายความยากผิดตั้งแต่ต้นก็แก้ไม่ได้
- **Expert choice routing**: ตัดสินทีละรอบว่า token ควร continue หรือ exit วิธีนี้ยืดหยุ่นกว่า เพราะเห็น representation ระหว่างทางแล้ว แต่ train และ stabilize ยากกว่า

ตัวเลขในคลิป: expert choice routing ได้ average few-shot accuracy 42.6% ส่วน token choice routing ได้ 40% ภายใต้ setup recursion 3 รอบ

**ได้อะไร:** การตัดสิน "ต้องคิดต่อไหม" หลังเห็น state ระหว่างทางมักดีกว่าการเดาความยากก่อนเริ่มคิด

## ความสัมพันธ์กับ Mixture-of-Experts

ชื่อคล้าย [[mixture-of-experts|Mixture-of-Experts]] แต่แกนต่างกัน:

- MoE เลือก expert หรือ subnetwork ไหนจะทำงาน
- MoR เลือกจำนวนรอบของ recursive computation

สองแนวคิดอาจอยู่ร่วมกันได้ เพราะอันหนึ่ง route ตามความเชี่ยวชาญ อีกอัน route ตามความลึก/compute budget

## KV cache เป็นโจทย์ตามมา

ถ้า token ออกจาก recursion ไม่พร้อมกัน [[kv-cache|KV cache]] ต้องตาม state ของ token ที่ยัง active ให้ถูก. MoR จึงต้องคิดเรื่อง recursion-wise caching หรือ recursive KV sharing ไม่อย่างนั้น memory traffic อาจกลืนกำไรจาก adaptive compute

## See also

- [[looped-transformers]]
- [[kv-cache]]
- [[mixture-of-experts]]
- [[focal-models]]
- [[speculative-decoding]]
