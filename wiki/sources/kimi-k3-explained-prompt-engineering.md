---
title: "Kimi K3 Explained!"
type: source
tags: [ai, kimi, moonshot, coding, agents, open-weight, moe, benchmarks]
url: "https://www.youtube.com/watch?v=juvwvztWAyo"
author: "Prompt Engineering"
created: 2026-07-17
updated: 2026-07-17
sources: ["https://www.youtube.com/watch?v=juvwvztWAyo"]
---

# Kimi K3 Explained! / ทำความเข้าใจ Kimi K3

วิดีโอของ [[prompt-engineering|Prompt Engineering]] (ช่อง YouTube ที่อธิบายงาน AI engineering) มอง [[kimi-k3|Kimi K3]] ของ [[moonshot-ai|Moonshot AI]] ว่าเป็น “DeepSeek moment” รอบใหม่ แก่นของคลิปไม่ใช่คำว่า model ที่ดีที่สุดทุกด้าน แต่คือ **open-weight model อาจขึ้นแนวหน้าได้ในงานเฉพาะทางอย่าง agentic coding แม้ยังตามหลังในงานคุยทั่วไป**.

หน้านี้สรุป transcript ที่ผู้ใช้ให้มา ตัวเลข benchmark, ราคา, architecture และเรื่องบริษัทอื่นนำ Kimi ไป post-train ยังไม่ได้ตรวจจาก Kimi blog หรือ evaluator ต้นทาง. Transcript เองมีชื่อเพี้ยนหลายจุด เช่นเปิดด้วย “Kimi K6B” ทั้งที่ title และเนื้อหาหลักพูดถึง K3 จึงเก็บ claim เหล่านี้เป็นคำกล่าวของผู้พูด ไม่ใช่ model card.

## Frontier แบบเฉพาะทาง ไม่ใช่ชนะทุกงาน

ผู้พูดเสนอว่า K3 เป็น open-weight model ตัวแรกที่ไม่ได้แค่ไล่ตาม frontier แต่ขึ้นไปกำหนด frontier ในงาน coding โดยเฉพาะ web development, UI design และ agent ที่ใช้ terminal ทำงานหลายขั้น.

เขาอ้างว่า K3 อยู่อันดับสามบน “Artificial Intelligence Index” และเด่นบน Terminal-Bench 2.1 จนชนะ Opus-class models มาก. แต่พอเปลี่ยนเป็น general chat, Humanity's Last Exam หรือ hallucination rate ภาพกลับไม่เหมือนเดิม: คลิปบอกว่า K3 ตามหลัง [[fable|Claude Fable 5]] มากใน HLE และ hallucinate มากกว่า Opus 4.8.

จุดนี้คือคำเตือนของคลิปเอง: aggregate score เดียวกลบความสามารถแบบฟันปลาได้. K3 อาจเป็น “workhorse” ที่ดีมากสำหรับ agentic coding แต่ไม่ใช่ model ที่ดีที่สุดสำหรับการคุยหรือสร้างข้อความทั่วไป.

**ได้อะไร:** ต้องเลือก model ตาม workload และ benchmark ที่ใกล้งานจริง ไม่ใช่ย้ายคำว่า “อันดับหนึ่งด้าน coding” ไปเป็น “เก่งที่สุดทุกด้าน”.

## Architecture: 3T parameters แต่ใช้ expert บางส่วน

คลิปอธิบาย K3 ว่าเป็น [[mixture-of-experts|Mixture-of-Experts]] (MoE, model ที่ route token ไปใช้ subnetwork บางส่วน) ขนาดรวม 3T parameters. มี 896 experts และ route แต่ละ token ผ่าน 16 experts. ตัวเลขช่วงพูดหลุดเป็น “16 จาก 800” แต่ description ระบุ 896 จึงยังควรกลับไปตรวจ technical report.

ผู้พูดยังบอกว่า K3 มี vision ติดมาแต่แรกและอ่าน context ได้ 1M tokens. เขามองว่าเพียงพอกับ agentic coding จำนวนมาก แต่ context window ใหญ่ไม่ได้ยืนยันเองว่า model จะรักษาคุณภาพได้ตลอด 1M tokens.

MoE ทำให้ active compute ต่อ token น้อยกว่า dense model ขนาด 3T เต็มก้อน แต่ไม่ได้แปลว่ารันง่ายบนเครื่องผู้ใช้. ผู้พูดประเมินว่า model ระดับ 2–3T ยังเกิน consumer hardware และเหมาะกับผู้ให้บริการ inference หรือองค์กรที่มี compute มากกว่า.

**ผลคือ:** “เปิด weights” กับ “รันเองได้จริง” เป็นคนละเรื่อง. License อาจเปิด แต่ hardware ยังทำให้การใช้งานกระจุกอยู่กับองค์กรขนาดใหญ่.

## ทำไม ecosystem สนใจ Kimi เป็นฐาน

คลิปมองว่าจุดแข็งของตระกูล Kimi ไม่ได้จบที่ model สำเร็จรูป. ผู้พูดอ้างว่า Kimi รุ่นก่อนถูก Cursor, Cognition/Windsurf และ Thinking Machines นำไปต่อยอดหรือใช้สร้างข้อมูลสังเคราะห์ เพราะ base model ยังดันต่อด้วย post-training ได้อีก.

อย่างไรก็ดี transcript สะกดชื่อ model และบริษัทช่วงนี้ไม่คงที่ เช่น “Wren surf”, “Sweet 1.5” และ “Kimi 2.7”. จึงยังบอกไม่ได้จากแหล่งนี้อย่างเดียวว่าแต่ละบริษัทใช้ base รุ่นไหน ทำ mid-training หรือ post-training แบบใด และผลดีขึ้นมาจาก weights, data, reward หรือ harness.

นี่เป็นตัวอย่างของ [[self-learning-agents|การปรับชั้น model]]: องค์กรเปลี่ยน weights ด้วยข้อมูลและคะแนนใหม่ ต่างจากการแก้ prompt, tool หรือ memory รอบ model. แต่ต้นทุนการ post-train model 3T ทำให้โอกาสนี้เป็นเรื่อง enterprise มากกว่านักพัฒนารายย่อย.

**ได้อะไร:** K3 อาจมีผลกับผู้ใช้ทางอ้อมผ่าน product ที่บริษัทอื่นสร้างบน base นี้ แม้ผู้ใช้จะไม่รัน K3 เอง.

## ราคา token กับราคาต่องาน

ผู้พูดบอกว่า K3 มากับราคา “ระดับ Sonnet” แต่ให้ performance ใกล้ Opus หรือ Fable ในบางงาน. เขาย้ำว่าราคาต่อหนึ่งล้าน token ยังไม่พอ ต้องดูว่า model ใช้กี่ token กว่าจะปิดงานได้.

คลิปอ้างงานของ Databricks ว่า model ที่ราคาต่อ token ถูกกว่าอาจแพงกว่าต่องาน ถ้าต้องเขียนยาว วนซ้ำ หรือแก้หลายรอบ. ในทางกลับกัน model ราคาแพงต่อ token อาจจบเร็วและถูกกว่าเมื่อวัดต่อ task. ผู้พูดมองว่า K3 ดีขึ้นด้าน token efficiency เมื่อเทียบกับ Kimi รุ่นก่อน แต่ยังไม่ได้ให้ protocol ที่เทียบ task เดียวกันด้วย acceptance criteria เดียวกัน.

**ผลคือ:** metric ที่ผู้ใช้ควรสนใจคือ cost ต่อผลงานที่ผ่านเกณฑ์ รวม token, เวลา, retry, review และ rework ตามกรอบ [[ai-token-economics|AI token economics]].

## ผลต่อผู้ใช้และตลาด

สำหรับคนที่หวัง local model คลิปมองว่า K3 ไม่ได้เปลี่ยนชีวิตทันที เพราะขนาด model ใหญ่มาก. ถ้าใช้ผ่าน inference provider ข้อมูลก็ยังออกจากระบบของผู้ใช้เหมือน closed API เว้นแต่องค์กรจะ self-host เองได้.

ผลที่ผู้พูดคาดว่าจะชัดกว่าคือการแข่งขัน: บริษัททำ coding product อาจเอา K3 ไปต่อยอด และ model ที่เก่งเฉพาะทางในราคาต่ำกว่าจะกดดัน lab อื่นให้ลดราคา. ทั้งสองข้อยังเป็นการคาดการณ์ ไม่ใช่ผลตลาดที่เกิดขึ้นแล้ว.

## ประเด็นที่ยังเปิดอยู่

- K3 ปล่อย weights ให้ดาวน์โหลดแล้ว หรือในช่วงคลิปยังเป็นเพียงประกาศว่าจะปล่อย: title/description เรียก open-weights แต่ transcript พูดว่า “when the weights are available”.
- “Artificial Intelligence Index” ในคลิปหมายถึง index ของ [[artificial-analysis|Artificial Analysis]] หรือชุดจัดอันดับอื่น และใช้ snapshot/protocol วันที่ใด.
- Terminal-Bench 2.1, HLE และ hallucination comparison คุม harness, reasoning effort, tool access, budget และจำนวน run เท่ากันหรือไม่.
- 3T parameters, 896 experts, 16 experts ต่อ token, native vision และ 1M context ตรงกับ technical report ของ Moonshot แค่ไหน.
- Cursor, Cognition/Windsurf และ Thinking Machines ใช้ Kimi รุ่นใดและต่อยอดด้วย data/post-training/harness แบบไหนกันแน่.
- ถ้าวัด cost ต่อ task ที่ผ่านเกณฑ์เดียวกัน K3 ยังถูกกว่า Opus/Fable หรือไม่.
- Open-weight K3 ช่วย privacy ได้จริงแค่ไหน เมื่อ hardware ทำให้คนส่วนใหญ่ต้องพึ่ง inference provider.

## ดูเพิ่ม

- [[kimi-k3]]
- [[moonshot-ai]]
- [[kimi-k2-6]]
- [[prompt-engineering]]
- [[open-weight-models]]
- [[mixture-of-experts]]
- [[ai-token-economics]]
- [[self-learning-agents]]
- [[artificial-analysis]]
- [[fable]]
- [[benchmark-contamination]]

