---
title: Chain-of-Thought
type: concept
tags: [ai, llm, reasoning, prompting, inference]
created: 2026-07-03
updated: 2026-09-19
sources: [llm-loops-instead-of-chain-of-thought.md, jev-the-ultimate-classification-model.md]
---

# Chain-of-Thought / การคิดเป็นลำดับข้อความ

Chain-of-thought คือการให้ LLM เขียน intermediate reasoning ออกมาเป็นข้อความก่อนตอบสุดท้าย. Model ได้พื้นที่ให้แยกปัญหาเป็นขั้น ๆ แล้ว condition บนข้อความที่ตัวเองเขียนไว้

ใน [[llm-loops-instead-of-chain-of-thought|LLM that loops instead of Doing Chain-of-Thought]] bycloud ใช้ chain-of-thought เป็นคู่เทียบกับ [[looped-transformers|looped transformer]]: แบบหนึ่งคิดผ่าน token อีกแบบคิดผ่าน hidden state

## ทำไมได้ผล

ปัญหาหลายอย่างยากถ้าต้องตอบใน forward pass เดียว. พอ model เขียนขั้นกลางออกมา มันสามารถ:

- ระบุ subproblem
- เก็บ intermediate fact
- อ่าน trace กลับเข้า context
- อัปเดตคำตอบรอบถัดไป

นี่ทำให้ chain-of-thought เป็นรูปแบบหนึ่งของ test-time compute: ยอมจ่าย token เพิ่มเพื่อให้ model iterate

## ทำไม bycloud มองว่าไม่ elegant

ทุก thought token ต้องถูก decode เป็น text แล้ว embed กลับเป็น hidden state. Reasoning จึงวิ่งผ่านภาษาธรรมชาติและ sampling แทนที่จะปรับ representation ภายในโดยตรง

ข้อเสียคือ latency, token cost, context cost, และ trace ที่อาจผิดตั้งแต่ต้นแล้วทำให้รอบถัดไป condition ผิดตาม

**ได้อะไร:** chain-of-thought เป็นวิธีที่ practical และ supervise ได้ แต่ไม่ใช่วิธีเดียวในการเพิ่ม compute ตอน inference

## บางงานไม่ต้องการ reasoning trace ตั้งแต่แรก

[[jev-the-ultimate-classification-model|วิดีโอของ Sam Witteveen เรื่อง Jev]] เสนอคู่เทียบอีกแบบ คือ [[system-one-models|System One Models]] ตัว model ไม่ได้พยายามคิดลึกขึ้นใน hidden state แต่ตัดงานสร้างข้อความออกเมื่อโจทย์ต้องการเพียง class, score หรือ yes-probability

ตัวอย่างอย่าง route support ticket หรือเช็กว่า message เร่งด่วนไหม มี output แคบอยู่แล้ว การใช้ reasoning model อาจเพิ่ม latency กับ token cost โดยไม่เพิ่มคุณค่าพอ แต่ข้อสรุปนี้ใช้ไม่ได้กับโจทย์ที่ class ขึ้นกับเหตุผลหลายทอดหรือ evidence ที่ต้องอธิบายให้คนตรวจ

**ผลคือ:** ก่อนเลือกวิธี reasoning ต้องถามก่อนว่างานต้อง reasoning จริง หรือเพียงต้องตีความภาษาแล้วคืนค่าจำกัดรูปแบบ

## จุดแข็งที่ latent reasoning ยังไม่มี

Chain-of-thought มี trace ชัด. เราสามารถสอน model ด้วยตัวอย่าง reasoning, distill จาก model ใหญ่, filter trace ที่ผิด, หรือ reinforce trace ที่นำไปสู่คำตอบดี

[[latent-reasoning|Latent reasoning]] และ looped transformer ไม่มี trace แบบนี้โดยธรรมชาติ จึง train ยากกว่า ถึงแม้จะดู compact กว่าทางสถาปัตยกรรม

## See also

- [[looped-transformers]]
- [[latent-reasoning]]
- [[multi-hop-reasoning]]
- [[reasoning-regression]]
- [[system-one-models]]
- [[jev]]
