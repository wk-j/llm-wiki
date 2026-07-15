---
title: GPT-5.6 Sol
type: entity
tags: [ai, models, openai, gpt, science]
created: 2026-07-01
updated: 2026-07-14
sources: ["https://openai.com/index/introducing-genebench-pro/", piyalitt-codex-keynote-attention-not-token.md, gpt-5-6-and-openai-build-week-aimeowyak.md, gpt-5-6-sol-fable-killer-prompt-engineering.md]
---

# GPT-5.6 Sol / ตระกูล GPT-5.6

[[openai|OpenAI]] model ในตระกูล **GPT-5.6** — หน้านี้รวมข้อมูลจาก [[introducing-genebench-pro|GeneBench-Pro]] และ keynote Codex ที่ [[ai-engineer-worlds-fair|AI Engineer World's Fair]] (สรุป [[piyalitt-codex-keynote-attention-not-token]]). ตัวเลขจาก keynote ยัง source-attributed จนกว่าจะตรวจจาก OpenAI โดยตรง

## ผลบน GeneBench-Pro

บน [[genebench-pro|GeneBench-Pro]] ซึ่งวัด scientific judgement ใน computational biology:

| Mode | Pass rate |
|---|---:|
| highest/max reasoning | 28.7% |
| Pro mode | 31.5% |

OpenAI บอกว่า highest reasoning ของ GPT-5.6 Sol แก้โจทย์ได้เกือบ 6 เท่าของ GPT-5.2 และใช้ token ประมาณสองในสามของ GPT-5.2 ในระดับ reasoning สูงสุด

## Pattern ที่ OpenAI ยก

ในโจทย์ pharmacogenomic time-to-event response, GPT-5.6 Sol เลือก new-user marginal structural Cox model พร้อม stabilized inverse-probability weights และ 90-day efficacy lag เพื่อจัดการ treatment-confounder feedback

ความหมายคือ model ไม่ได้แค่รัน method ที่รู้จัก แต่ปรับ causal inference strategy ตาม data structure ซึ่งเป็นตัวอย่างของ [[research-taste|research taste]]

## ตระกูล 5.6 บนเวที Codex (source-attributed)

จาก [[piyalitt-codex-keynote-attention-not-token]] ทีม Codex ยกตัวอย่างในกรอบ [[value-maxing|value maxing]]:

| Variant | Claim บนเวที |
|---|---|
| **Terra** | ความฉลาดระดับ [[gpt-5-5\|GPT-5.5]] ในราคาครึ่งเดียว |
| **Luna** | ชนะ model ดังหลายตัว ราคา $1/1M input, $6/1M output |
| Frontier บน Cerebras | 750 token/วินาที — เปิดใช้เดือนถัดไป |
| รุ่นบนสุดตระกูล 5.6 | ขึ้นนำ Terminal Bench (ตามกราฟบนเวที) |

OpenAI preview ตระกูล 5.6 สัปดาห์ก่อนงาน World's Fair — สอดคล้องกับจังหวะปล่อย model ใหม่ทุก ~6 สัปดาห์ (เคยทุก ~15 เดือน)

## Field report หลังเปิดใช้ (AIMeowYak, 2026-07-12)

ใน [[gpt-5-6-and-openai-build-week-aimeowyak|ไลฟ์รีวิว GPT-5.6]] [[piyalitt-ittichaiwong|Piyalitt Ittichaiwong]] แบ่งการเลือกใช้ออกเป็นสองแกน: variant (Luna/Terra/Sol) กับ [[effort-levels|effort]]. เขาแนะนำให้ผู้ใช้ GPT-5.5 ลองลด effort ลงหนึ่งขั้นบน 5.6 ก่อน และมอง Luna effort สูงเป็นตัวคุ้มสำหรับงาน implementation ส่วน Terra อาจมีที่ยืนใน API workload บางแบบ ทั้งหมดนี้เป็นคำแนะนำจากประสบการณ์ ไม่ใช่กฎจาก OpenAI

คำเตือนสำคัญคือ `ultra` อาจ spawn subagent จำนวนมากจน RAM และ token พุ่งพร้อมกัน ขณะที่จุดเด่นที่ผู้พูดเห็นชัดคือ frontend/presentation ดีขึ้น, [[computer-use|computer use]] เร็วขึ้น และ GPT Live คุยแทรกพร้อมเรียก search/model อื่นคู่ขนานได้ ภาษาไทยยังดูเป็นรองภาษาอังกฤษใน voice demo และเป็นรอง Fable 5 ในงานเขียนบางชนิด

ไลฟ์ยังเก็บความตึงไว้สองด้าน: GPT-5.6 ทำ coding/demo ซับซ้อนได้ดีขึ้นมาก แต่ high-agency behavior ทำให้มันอาจทำเกินสั่งหรือเผาค่าใช้จ่ายโดยไม่ถาม จึงต้องเพิ่ม permission, budget และ approval gate ตามความสามารถที่เพิ่มขึ้น

## มุม cost, งานยาว และ automated research (Prompt Engineering, 2026-07-14)

[[gpt-5-6-sol-fable-killer-prompt-engineering|รีวิวของ Prompt Engineering]] วาง Sol เป็นคู่แข่งตรงของ [[fable|Claude Fable 5]] และบอกว่าเรื่องใหญ่คือ cost-efficiency: coding/terminal benchmark บางชุดสูสีหรือดีกว่าในต้นทุนต่ำกว่า. แต่ผู้พูดก็ทักว่าบางกราฟใช้ effort ฝั่ง Claude ไม่ถึงระดับสูงสุด จึงยังเทียบแบบ apples-to-apples ไม่ได้.

คลิปเพิ่มอีกสองมุม. หนึ่งคือ early tester ปล่อย model วนสร้าง Manhattan แบบ voxel เกือบหนึ่งสัปดาห์ ซึ่งเป็นตัวอย่างของ [[loop-engineering|loop engineering]]. สองคือคำกล่าวว่า OpenAI ใช้ Sol ทำ internal research, optimize AI infrastructure และออกแบบ experiment เพื่อ post-train Luna. ถ้าตรงกับเอกสารต้นทาง ส่วนหลังคือ [[self-learning-agents|self-improvement ที่เปลี่ยน model]] ไม่ใช่การเรียนผ่าน memory อย่างเดียว.

อย่างไรก็ดี ผู้พูดยังเข้าใช้ Sol ไม่ได้และ demo ตัวติดตาม ISS บนรุ่นที่เขาใช้มีแผนที่แสดงไม่ครบ. หน้า wiki จึงเก็บคำว่า “Fable killer” เป็นคำถามเปิด: benchmark กับราคาให้เหตุผลว่าน่าจับตา แต่ประสบการณ์ตรงในคลิปยังไม่ยืนยันคำโฆษณา.

## ข้อควรระวัง

หน้านี้รวมข้อมูลจาก GeneBench-Pro (OpenAI blog), keynote summary และรีวิวจาก Piyalitt/Prompt Engineering — ยังไม่ควรสรุป capability กว้าง ๆ นอกเหนือจากแหล่งเหล่านี้. ชื่อ variant, effort tier, ราคา, ความเร็ว, benchmark, ARC-AGI-3 และ cheating rate ควรตรวจกับเอกสาร OpenAI/ผู้ประเมินต้นทางก่อนอ้างเป็นข้อเท็จจริง

## See also

- [[openai]]
- [[genebench-pro]]
- [[introducing-genebench-pro]]
- [[research-taste]]
- [[gpt-5-5]]
- [[value-maxing]]
- [[piyalitt-codex-keynote-attention-not-token]]
- [[gpt-5-6-and-openai-build-week-aimeowyak]]
- [[computer-use]]
- [[gpt-5-6-sol-fable-killer-prompt-engineering]]
- [[fable]]
- [[self-learning-agents]]
- [[reward-hacking]]
