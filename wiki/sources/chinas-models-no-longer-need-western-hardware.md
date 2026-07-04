---
title: China's Models No Longer Need Western Hardware
type: source
tags: [ai, china, hardware, llm, inference, training, moe]
url: "https://www.youtube.com/watch?v=idp3wJCqNrU"
author: "Prompt Engineering"
created: 2026-07-03
updated: 2026-07-03
sources: [chinas-models-no-longer-need-western-hardware.md]
---

# China's Models No Longer Need Western Hardware / โมเดลจีนไม่ต้องพึ่ง hardware ตะวันตกเท่าเดิม

วิดีโอของ [[prompt-engineering|Prompt Engineering]] (ช่อง YouTube ที่อธิบายงาน AI engineering) เล่าเรื่อง [[longcat-2-0|LongCat 2.0]] ของ [[meituan|Meituan]] ว่าเป็นตัวอย่างใหม่ของจีนที่ train model ใหญ่มากโดยไม่ใช้ NVIDIA GPUs หรือ Google TPUs ตามคำกล่าวในคลิป

แก่นของคลิปไม่ใช่แค่ benchmark ว่า model เก่งแค่ไหน แต่คือคำถามว่า lab จีนเริ่มมีทางเลี่ยงทั้ง hardware และ software stack ตะวันตกได้จริงแค่ไหน โดยเฉพาะ NVIDIA + CUDA.

## ใจความสำคัญ

- Meituan open source / เปิดตัว LongCat 2.0 ซึ่งคลิปบอกว่าเป็น **1.6T-parameter MoE model** และมี **48B active parameters ต่อ token**
- คลิปอ้างว่า train บน custom AI chips มากกว่า 50,000 ตัว และข้อมูลกว่า 35T tokens โดยไม่ใช้ NVIDIA GPUs หรือ Google TPUs
- LongCat ลดต้นทุนด้วยหลายทางพร้อมกัน: [[mixture-of-experts|MoE]], [[n-gram-embeddings|n-gram embeddings]], [[sparse-attention|sparse attention]], และ [[speculative-decoding|speculative decoding]]
- จุดสำคัญของเรื่องนี้คือ software stack: การไม่ใช้ CUDA แปลว่าทีมต้องสร้าง tooling / runtime / optimization เองบน hardware ที่ memory และ ecosystem ยังสู้ NVIDIA ไม่ได้
- คลิปย้ำว่าคะแนน benchmark เป็น self-reported in-house benchmarks จึงควรอ่านเป็นสัญญาณ ไม่ใช่ข้อสรุปสุดท้าย

## ทำไม hardware สำคัญ

คลิปเริ่มจากภาพเดิมของ frontier labs: ทุกคนพึ่ง NVIDIA ไม่ใช่แค่เพราะ GPU แรงหรือ VRAM เยอะ แต่เพราะ CUDA และ ecosystem รอบ ๆ สุกมาก พอมี bug, kernel, compiler, communication library, profiler, และ framework integration ทีม model ไม่ต้องสร้างทุกอย่างเอง

LongCat 2.0 จึงน่าสนใจเพราะคลิปบอกว่า Meituan train model ใหญ่บน custom AI chips ที่ memory น้อยกว่าและ software stack อ่อนกว่ามาก ถ้าทำได้จริง นี่ไม่ใช่แค่ประหยัดเงิน แต่ลด dependency ทางยุทธศาสตร์จาก NVIDIA และ Google TPU.

**ได้อะไร:** การแข่ง AI ไม่ได้อยู่ที่ใครซื้อ H100/GB200 ได้เยอะอย่างเดียว แต่รวมถึงใครสร้าง algorithm + compiler/runtime + hardware stack ที่เข้ากันได้ด้วย

## MoE ไม่พอ ต้องเพิ่มข้อมูลใน embedding

LongCat 2.0 เป็น [[mixture-of-experts|Mixture-of-Experts]] (MoE, model ที่เลือกใช้ expert บางส่วนต่อ token) ขนาดรวม 1.6T parameters แต่ active แค่ 48B ต่อ token ตามคำกล่าวในคลิป

คลิปอธิบายว่าแนวทาง "เพิ่ม expert ไปเรื่อย ๆ" มีเพดาน พอ network sparse เกินไป performance อาจเริ่มได้กำไรน้อยลงหรือแย่ลง เพราะ router ต้องเลือก expert ให้ดี และแต่ละ expert เห็นข้อมูลน้อยลง

ทางที่ LongCat ใช้คือ [[n-gram-embeddings|n-gram embeddings]] (embedding สำหรับกลุ่มคำ 2-5 token ไม่ใช่แค่ token เดี่ยว) แนวคิดคือเพิ่มข้อมูลใน embedding table ให้ model เห็นวลีหรือ pattern สั้น ๆ ได้ตรงขึ้น การ lookup embedding ถูกกว่าการเพิ่ม expert ใหม่ เพราะเป็น dictionary lookup ไม่ใช่เพิ่ม compute path ทั้งก้อน

แต่ tradeoff คือ vocabulary / corpus side ใหญ่ขึ้น และ attention cost ตามมา ถ้า context ยาวมาก model ต้องจัดการการมองย้อนกลับให้ถูกและถูกเงิน

**ผลคือ:** LongCat พยายามเพิ่ม "ข้อมูลที่ model เห็น" โดยไม่เพิ่ม active compute ต่อ token แบบตรง ๆ

## Long context ต้องทำ attention ให้ถูกกว่าเดิม

ถ้า model อ่าน context ได้ยาวมาก การให้ทุก token มองย้อนกลับทุก token แบบเต็ม ๆ จะแพงเกินไป คลิปจึงโยงไปที่ [[sparse-attention|sparse attention]] (attention ที่เลือกมองเฉพาะส่วนสำคัญ) และบอกว่า LongCat ใช้แนวทางที่ได้แรงบันดาลใจจาก DeepSeek Sparse Attention.

ปัญหาของ sparse attention คือ "ตัวช่วยเลือก" เองอาจกลายเป็น bottleneck ถ้าต้องคำนวณเยอะหรืออ่าน memory กระโดดไปมา LongCat จึงทำให้ helper เบาลง 3 ทางตามคลิป:

- อ่าน memory เป็น chunk ที่คาดเดาได้ แทนการกระโดดสุ่ม
- คำนวณว่าส่วนไหนสำคัญครั้งหนึ่ง แล้ว cache / reuse ข้ามหลาย layer
- ใช้วิธี coarse-to-fine: มองหยาบก่อน แล้วค่อยเลือกละเอียด

**ได้อะไร:** long context ไม่ได้ฟรี แต่อาจทำให้ถูกลงได้ถ้าตัวเลือก attention เป็นมิตรกับ memory access และ cache

## Speculative decoding และ hardware แยกงาน

คลิปบอกว่า LongCat ใช้ [[speculative-decoding|speculative decoding]] (draft model เดา token ล่วงหน้า แล้ว target model ตรวจ) เพื่อเพิ่ม throughput และลด latency. ในคำอธิบายของคลิป LongCat มี picker / draft network ที่เบากว่า ช่วยเสนอคำต่อ ๆ ไป แล้ว model ใหญ่ตรวจแก้

ฝั่ง hardware คลิปแยกงาน LLM เป็นสองช่วง:

- **Prefill**: อ่าน prompt / context ยาว ๆ มักติด compute
- **Decode**: เขียนคำตอบทีละ token มักติด memory bandwidth

ดังนั้น custom ASICs อาจถูกจูนต่างกันสำหรับสองงานนี้ ไม่จำเป็นต้องมี hardware เดียวที่เก่งทุกอย่างเหมือน GPU general-purpose.

**ผลคือ:** ถ้ารู้ workload ของ LLM ชัด ทีมสามารถออกแบบ chip และ runtime ให้เหมาะกับ prefill/decode แยกกัน แทนการพึ่ง GPU stack มาตรฐานอย่างเดียว

## Demo และข้อควรระวัง

คลิป demo LongCat ผ่าน longcat.chat ให้สร้าง real-time 3D ISS tracker. ผู้พูดบอกว่าผลงาน render ดูดี แต่ตำแหน่ง ISS น่าจะไม่ใช่ real-time เพราะเคลื่อนที่เร็วผิดปกติและเวลาเหมือนคลาดเคลื่อน

ตรงนี้เป็นหลักฐานแบบ anecdote: model coding / UI generation ดูมีความสามารถ แต่ยังมี hallucination หรือ simulation error ในงานที่ต้องผูกกับ API จริงและเวลาโลกจริง

คลิปยังบอกว่า weights จะ upload ไป Hugging Face และ "coming soon" ในช่วงที่พูด ดังนั้นสถานะ open-weight จริงควรตรวจจากแหล่งตรงก่อนสรุปต่อ

## Open questions

- LongCat 2.0 ใช้ชื่อเดียวกันตลอดหรือไม่: transcript สลับคำว่า LongCat และ LongChat หลายจุด จึงใช้ LongCat 2.0 ตาม title/description และบันทึกความสับสนไว้
- custom AI chips คือ chip รุ่นใด จาก vendor ใด และใช้สัดส่วน prefill/decode อย่างไร
- benchmark ที่บอกว่าแข่งกับ OpenAI / Google / Anthropic ได้ วัดด้วยชุดใด และ third-party rerun เห็นผลเหมือนกันไหม
- weights ถูกปล่อยจริงในรูปแบบ open-weight หรือแค่ประกาศว่าจะปล่อย
- การไม่ใช้ NVIDIA/TPU หมายถึงไม่ใช้ใน training ทั้งหมดหรือไม่ใช้ใน cluster หลักเท่านั้น

## See also

- [[longcat-2-0]]
- [[meituan]]
- [[mixture-of-experts]]
- [[n-gram-embeddings]]
- [[sparse-attention]]
- [[speculative-decoding]]
- [[sputnik-moment-ai]]
