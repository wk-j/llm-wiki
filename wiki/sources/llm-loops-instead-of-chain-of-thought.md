---
title: LLM that loops instead of Doing Chain-of-Thought
type: source
tags: [ai, llm, reasoning, architecture, transformer, inference]
url: "https://www.youtube.com/watch?v=nYwid6Q5HXk"
author: "bycloud"
created: 2026-07-03
updated: 2026-07-03
sources: [llm-loops-instead-of-chain-of-thought.md]
---

# LLM that loops instead of Doing Chain-of-Thought / LLM ที่วน layer แทน Chain-of-Thought

วิดีโอของ [[bycloud|bycloud]] (ช่อง YouTube ที่อธิบายงาน AI/LLM) เล่าแนวคิด [[looped-transformers|looped transformer]]: ให้ model "คิดเพิ่ม" ด้วยการวน transformer block เดิมซ้ำ ๆ ภายใน hidden state แทนการเขียน [[chain-of-thought|chain-of-thought]] ออกมาเป็น token ยาว ๆ

แก่นของคลิปคือ test-time compute มีได้มากกว่าหนึ่งรูปแบบ. Chain-of-thought เพิ่ม compute ผ่าน text. Looped transformer เพิ่ม compute ผ่าน recurrence ภายใน model.

## สรุปสั้น

- Chain-of-thought ทำงานดีเพราะให้ model iterate ได้ แต่ต้อง decode ความคิดเป็น text แล้ว embed กลับเข้า model ซ้ำ ๆ
- Looped transformer ใช้ block เดิมวนหลายรอบ ให้ hidden state ค่อย ๆ refine โดยไม่ต้อง externalize ความคิดเป็น token
- คลิปโยง looped transformer กับ [[multi-hop-reasoning|multi-hop reasoning]]: ถ้าปัญหาต้องไล่ความสัมพันธ์หลาย hop การเพิ่มจำนวน loop ตอน inference อาจช่วย extrapolate ไปไกลกว่าที่ train ไว้
- งานแบบนี้เจอปัญหา stability เพราะการวน transformation เดิมซ้ำ ๆ อาจทำให้ hidden state drift, norm โต, loss spike, หรือ diverge
- [[mixture-of-recursions|Mixture-of-Recursions]] เพิ่ม router ให้ token ง่ายออกเร็ว ส่วน token ยากวนต่อ จึงทำ adaptive compute ต่อ token
- [[kv-cache|KV cache]] กลายเป็น bottleneck ใหม่ เพราะ recursive depth อาจทำให้ต้องเก็บ key/value หลายชุด แม้ parameter จะ reuse ก็ตาม
- คลิปย้ำ caveat สำคัญ: looped transformer ยังไม่ได้พิสูจน์ว่าดีกว่า standard transformer + chain-of-thought ในงานจริงขนาดใหญ่

## ทำไม Chain-of-Thought ดูไม่สวย

Chain-of-thought คือการให้ model เขียนขั้นคิดออกมาเป็น token. วิธีนี้มีข้อดีตรงที่ model ได้พื้นที่สำหรับ intermediate step: เขียนความคิด อ่านกลับ อัปเดต state แล้วเขียนต่อ

แต่ bycloud มองว่ามันไม่ elegant เพราะทุก reasoning token ต้องผ่านวงจรนี้:

1. hidden state ถูก decode เป็น text
2. text ถูก append เข้า context
3. text ถูก embed กลับเป็น hidden state
4. model ทำ forward pass ต่อจาก trace นั้น

ตรงนี้ทำให้ reasoning ถูก mediate ผ่าน sampled textual trace. Model ไม่ได้แก้ latent representation โดยตรง แต่ปล่อย token ออกมาก่อน แล้วค่อย condition บน token ที่ตัวเองปล่อย

**ได้อะไร:** chain-of-thought เป็นวิธีเพิ่ม iteration ที่ใช้ได้จริง แต่จ่ายด้วย token, latency, context, และความเปราะของ text trace

## Looped transformer คืออะไร

[[looped-transformers|Looped transformer]] คือสถาปัตยกรรมที่ใช้ transformer block ชุดเล็กกว่าเดิม แล้วเอา block เดิมวนซ้ำหลายรอบ. Output hidden state ของรอบก่อนเป็น input ของรอบถัดไป

แทนที่จะมี layer ไม่ซ้ำกันยาว ๆ model จะ reuse weight เดิมเป็น recurrent update rule. จำนวน recurrence จึงเป็น compute dial: ตอน inference อาจเพิ่ม loop เพื่อให้ model "คิดนานขึ้น" ได้โดยไม่เพิ่ม parameter

คลิปยก paper **Loop, Think, & Generalize: Implicit Reasoning in Recurrent-Depth Transformers** (เม.ย. 2026) เป็นตัวอย่างหลัก. ผลที่ bycloud เล่าคือ model เรียน [[multi-hop-reasoning|multi-hop reasoning]] ได้เป็นสามช่วง:

- ช่วงแรกจำ training set ได้
- ช่วงสอง generalize ใน distribution เดิมได้
- ช่วงสามเริ่ม systematic generalization คือประกอบความรู้ในรูปแบบที่ไม่ได้เห็นตรง ๆ ตอน train

ถ้าเพิ่มจำนวน loop ตอน inference มากกว่าตอน train model สามารถทำ hop ได้มากขึ้นในบาง benchmark. นี่คือเหตุผลที่คนสนใจว่า recurrence อาจเป็น test-time compute ที่ compact กว่า chain-of-thought

## ปัญหา stability

พอวน layer เดิมซ้ำ ๆ เราไม่ได้แค่สร้าง network แล้วจบ แต่กำลังออกแบบ dynamical system. Hidden state ใน [[residual-stream|residual stream]] จะถูก update ซ้ำจาก rule เดิม ถ้า update rule มี bias เล็ก ๆ bias นั้นอาจถูกขยายทุก loop

คลิปโยงไปที่ paper **Parcae: Scaling Laws For Stable Looped Language Models**. ประเด็นคือ naive looped transformer อาจไม่ stable: hidden state norm โตขึ้น, loss spike, หรือ model ไม่ converge

วิธีแก้ที่คลิปสรุปคือ constrain และ normalize recurrence เพื่อให้ update ไม่สะสมแบบไร้คุม

**ผลคือ:** looped transformer ไม่ใช่แค่ "เอา layer มาวน" ต้องคุม dynamics ของ hidden state ด้วย ไม่อย่างนั้น compute ที่เพิ่มอาจทำให้แย่ลง

## รู้ได้อย่างไรว่ามัน reasoning จริง

คลิปใช้ paper **A Mechanistic Analysis of Looped RLMs** เพื่อดูว่าภายใน model เกิดอะไรขึ้น. นักวิจัย track latent states ข้าม recurrence แล้ว project ด้วย PCA (principal component analysis, วิธีบีบมิติ activation ให้ดูเป็นแผนที่ 2D/3D ได้)

bycloud เล่าว่า looped models มักเคลื่อนไปหา stable trajectory:

- บางเคสเข้าใกล้ fixed point คือ representation ค่อย ๆ นิ่ง
- บางเคสเป็น cycle คือ hidden state กลับไปชุด state ที่สม่ำเสมอ
- attention head behavior ก็นิ่งขึ้นตาม ไม่ใช่แค่ activation ดิบ

ที่น่าสนใจคือ recurrence ต้น กลาง ท้ายทำหน้าที่ต่างกันได้ แม้ weight จะ shared. รอบแรก ๆ จัดรูปปัญหา รอบกลาง ๆ propagate ความสัมพันธ์ รอบท้าย ๆ ลด update และ stabilize คำตอบ

**ได้อะไร:** ถ้า analysis นี้ถือได้ loop ไม่ได้แค่ทำงานเดิมซ้ำ แต่ใช้ input state ที่เปลี่ยนไปทำให้ function เดิมรับบทต่างกันในแต่ละรอบ

## Mixture-of-Recursions: คิดไม่เท่ากันทุก token

looped transformer แบบตรง ๆ ให้ทุก token วนจำนวนรอบเท่ากัน. นี่เสีย compute เพราะ token ง่ายกับ token ยากถูกคิดนานเท่ากัน

[[mixture-of-recursions|Mixture-of-Recursions]] แก้ด้วย router ที่ตัดสินว่า token ไหนควรวนกี่รอบ:

- **Token choice routing**: ตัดสินตั้งแต่ต้นว่า token จะไป depth bucket ไหน ประหยัดและง่าย แต่ถ้าประเมินยากผิดตั้งแต่แรกก็แก้ไม่ได้
- **Expert choice routing**: ตัดสินทีละรอบว่าจะ continue หรือ exit ยืดหยุ่นกว่า แต่ train/stabilize ยากกว่า

ในตัวเลขที่คลิปยกมา expert choice routing ทำ few-shot accuracy เฉลี่ย 42.6% ส่วน token choice routing ได้ 40% ภายใต้ setup recursion 3 รอบ

**ผลคือ:** adaptive recursion สำคัญเพราะความยากไม่ได้อยู่เท่ากันทุก token การตัดสินหลังเห็น representation ระหว่างทางมักดีกว่าการตัดสินก่อนเริ่มคิด

## KV cache เป็น bottleneck ใหม่

ถึง looped model จะ reuse parameter แต่ inference ยังต้องจ่าย memory traffic. ใน transformer ปกติ [[kv-cache|KV cache]] เก็บ key/value ของแต่ละ layer/token เพื่อ decode เร็วขึ้น. ถ้ามี recursive depth แบบ naive เราอาจต้องเก็บ KV แยกตาม depth ทำให้ memory ไม่ได้ประหยัดเท่าที่คิด

คลิปสรุปสองทางใน Mixture-of-Recursions:

- **Recursion-wise caching**: เก็บ KV เฉพาะ token ที่ยัง active ในแต่ละ recursion token ที่ exit แล้วไม่ต้องลากไปลึกต่อ แม่นกว่า แต่ใช้ memory มากกว่า
- **Recursive KV sharing**: cache KV ครั้งแรกแล้ว reuse ใน recursion ต่อ ๆ ไป ประหยัด memory มาก แต่ representation รอบหลังจะ stale เล็กน้อย

**ได้อะไร:** recurrence ลด parameter ได้ แต่ไม่ได้ลบปัญหา memory bandwidth. ถ้า KV cache ไม่ถูกออกแบบให้เข้ากับ recursion ระบบอาจแพงตอนรันจริงอยู่ดี

## ข้อจำกัดและภาพรวม

bycloud ปิดด้วย caveat ว่า looped transformer ยังไม่ได้ชนะ standard transformer แบบกว้าง ๆ. ถ้าไม่มีข้อจำกัดด้าน memory หรือ parameter การเพิ่ม layer/width แบบปกติยัง expressive กว่า เพราะ layer แต่ละชั้นมี transformation ของตัวเอง ไม่ต้อง reuse function เดิม

อีกเรื่องคือ chain-of-thought มี training signal ชัดกว่า. เราสามารถ supervise, distill, filter, หรือ reinforce textual reasoning traces ได้ แต่ latent recursion ไม่มี trace ภาษาธรรมชาติบอกว่า step 1/2/3 ควรเป็นอะไร model ต้องค้นโครงสร้างเองจาก objective ปลายทาง

ดังนั้น use case ที่น่าสนใจของ looped transformer อาจอยู่ใน model เล็ก, edge deployment, distillation, หรือ synthetic data generation ที่อยากแลก compute เป็น effective depth โดยไม่เพิ่ม parameter มาก

## Open questions

- bycloud บอกว่ามีคนสงสัยว่า Claude 3 ใช้แนวคิด recurrence เบื้องหลังเพราะทำ Graph Walk BFS ได้ดี แต่คลิปไม่ได้ให้หลักฐานจาก Anthropic จึงควรเก็บเป็น speculation ไม่ใช่ข้อเท็จจริง
- ผล multi-hop benchmark และ depth extrapolation จะ scale ไปงาน real-world language/code/research ได้แค่ไหน
- ถ้าเทียบกับ standard transformer ที่ optimize ดีแล้ว looped transformer ชนะตรง latency/throughput จริงหรือแค่ชนะใน parameter budget
- latent reasoning จะ train หรือ supervise อย่างไรโดยไม่ต้องกลับไปพึ่ง textual chain-of-thought
- adaptive recursion กับ KV cache แบบไหนให้ tradeoff ดีสุดใน production inference

## Sponsor / context

วิดีโอมี sponsor คือ [[crusoe|Crusoe]] serverless fine-tuning และโปรโมต [[intuitive-ai-academy|Intuitive AI Academy]] ของ bycloud. ส่วนนี้เป็นบริบทของ source ไม่ใช่หลักฐานด้าน looped transformer.

## See also

- [[bycloud]]
- [[looped-transformers]]
- [[latent-reasoning]]
- [[multi-hop-reasoning]]
- [[mixture-of-recursions]]
- [[kv-cache]]
- [[chain-of-thought]]
- [[claude]]
