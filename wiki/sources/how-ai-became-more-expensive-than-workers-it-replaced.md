---
title: How AI Became More Expensive Than The Workers It Replaced
type: source
tags: [ai, economics, labor, enterprise, tokens, data-center]
url: "https://www.youtube.com/watch?v=cfaZZPjA3g0"
author: "Economy Media"
created: 2026-07-03
updated: 2026-07-03
sources: [how-ai-became-more-expensive-than-workers-it-replaced.md]
---

# How AI Became More Expensive Than The Workers It Replaced / เมื่อ AI แพงกว่าคนที่มันแทนที่

วิดีโอของ [[economy-media|Economy Media]] เล่าเรื่องกลับด้านของเศรษฐศาสตร์ AI: ตอนแรก AI ถูกขายว่าแทนแรงงานได้ถูกกว่า แต่เมื่อบริษัทใช้ AI ระดับ enterprise หนักขึ้น ต้นทุน token, agent, data center, และการใช้งานแบบโชว์ตัวเลขเริ่มทำให้บิล AI บาน

แก่นของคลิปคือ [[ai-labor-cost-reversal|AI labor cost reversal]]: บางงาน AI ยังถูกกว่าคน โดยเฉพาะ coding ตามที่คลิปยอมรับ แต่บางงาน เช่น data entry หรือ call center ส่วนต่างเริ่มแคบ หรือคนอาจถูกกว่าแล้ว

## ใจความสำคัญ

- คลิปเริ่มจาก narrative หลัง ChatGPT ปี 2022: AI ถูกมองว่าเร็ว ถูก และแทนทีมงานจำนวนมากได้
- พอองค์กรบังคับหรือกระตุ้นให้พนักงานใช้ AI การใช้ token กลายเป็น KPI / status signal จนเกิด [[tokenmaxxing|tokenmaxxing]] คือใช้ token เยอะเพื่อดู productive
- การคิดเงินตาม token ทำให้การใช้งานที่เหมือนฟรีในระดับคนเดียว กลายเป็นบิลหลักร้อยล้านดอลลาร์เมื่อคูณกับพนักงานหลายหมื่นคน
- คลิปอ้างว่าค่า token เฉลี่ยของ LLM มากกว่าสองเท่าจากปลายปี 2025 ถึงพฤษภาคม 2026 ตาม Bloomberg Finance; ตัวเลขควรอ่านเป็น source-attributed
- [[ai-data-center-bottlenecks|Data center bottlenecks]] และชิ้นส่วนอิเล็กทรอนิกส์ขาด ทำให้ supply compute ไม่ทัน demand และดันต้นทุนขึ้น
- [[anthropic|Anthropic]] และ [[openai|OpenAI]] ได้ประโยชน์จาก enterprise agent adoption แต่ถ้าต้องทำกำไรหรือ IPO บริษัท AI อาจต้องขึ้นราคา token มากขึ้น
- Enterprise เริ่มถาม [[enterprise-ai-roi|enterprise AI ROI]]: ถ้าบิล AI ใกล้หรือแพงกว่าคนที่เลิกจ้างไป จะใช้ AI ต่ออย่างไรให้คุ้ม
- คลิปขัดกับคำขวัญ [[code-is-free|Code is Free]] แบบตรง ๆ บางส่วน แต่ไม่ได้ลบคำขวัญนั้น: ใน coding AI ยังอาจถูกกว่าแรงงานมาก ส่วนคำถามใหม่คือ “ฟรีเมื่อเทียบกับอะไร และรวมต้นทุนทั้งระบบหรือยัง”

## จาก cheap automation เป็น budget shock

ช่วงแรก AI ถูกมองเป็นเครื่องจักรที่ทำงานแทนคนได้เร็วและถูกกว่า คลิปยกภาพ layoffs, fast-food drive-thru AI, และบริษัทเทคโนโลยีที่ลดทีมเป็นฉากหลัง

แต่พอการใช้ AI กลายเป็น policy ในองค์กร demand ก็ไม่ใช่แค่ “งานที่ AI คุ้มจริง” อีกต่อไป พนักงานอาจใช้ AI กับงานเล็กมาก เพราะบริษัทบอกให้ใช้ หรือเพราะอยากโชว์ว่าใช้เครื่องมือใหม่ได้เต็มที่

**ได้อะไร:** adoption ที่ดูเหมือน productivity อาจรวม demand เทียมจาก KPI และวัฒนธรรมองค์กร ไม่ใช่ demand จากงานที่คุ้มเงินจริงทั้งหมด

## Tokenmaxxing / ใช้ token เพื่อโชว์ performance

[[tokenmaxxing|Tokenmaxxing]] ในคลิปหมายถึงการใช้ token เยอะเกินจำเป็น เพื่อแสดงว่าใช้ AI หนักและทำงานแบบ “ทันสมัย” ผู้พูดยก quote แนวว่า engineer เงินเดือนสูงควรใช้ token จำนวนมาก ไม่งั้นน่ากังวล

ปัญหาคือ token ไม่ใช่ output. คนอาจเผา token เพื่อถามเรื่องเล็ก ๆ, ให้ agent ลองหลายทาง, หรือใช้ model แพงกับงานที่ model ถูกพอแล้ว

พอค่าใช้จ่ายถูกวัดจาก token ระบบจูงใจจึงเพี้ยนได้สองชั้น:

1. ถ้าวัดพนักงานจาก token consumed คนจะใช้เยอะเพื่อดูดี
2. ถ้าวัดผู้ให้บริการจาก revenue/token บริษัท model ยิ่งมีแรงจูงใจให้ usage โต

**ผลคือ:** token กลายเป็นตัวเลขที่ดูเหมือน productivity แต่จริง ๆ อาจเป็นแค่ cost center ที่โตเร็ว

## Data center supply ทำให้ราคาไม่ลงตาม adoption

คลิปโยง token cost กับ infrastructure. ถ้า demand AI โตเร็ว แต่ data center, power, GPU, networking, cooling, และ electronic components สร้างไม่ทัน ต้นทุน compute ก็ไม่ลดตามเส้น adoption

นี่ต่อจากหน้า [[ai-data-center-bottlenecks|AI Data Center Bottlenecks]]: ก่อนหน้านี้ wiki มีกรอบว่า AI scaling ไม่ได้ติดแค่ GPU แต่ติดทั้งระบบ data center. แหล่ง Economy Media เพิ่มมุมเศรษฐศาสตร์: เมื่อ supply ไม่ทัน demand ต้นทุน token ที่ enterprise จ่ายอาจสูงขึ้นแทนที่จะถูกลง

คลิปอ้างว่าโครงการ data center ในสหรัฐฯ สำหรับปี 2026 เกือบ 50% ถูกยกเลิกหรือเลื่อนตาม Bloomberg และ demand infrastructure ยังเกิน supply ตาม Economic Times. Wiki เก็บตัวเลขนี้เป็นคำกล่าวจากคลิปจนกว่าจะตรวจแหล่งตรง

**ได้อะไร:** token price ไม่ใช่แค่ราคา software. มันสะท้อน supply chain ของ hardware, power, และ data center ด้วย

## Enterprise AI ROI: tokens or humans?

คลิปใช้ภาพ “Tokens or humans?” เพื่อบอกว่าฝ่ายการเงินเริ่มต้องเลือกระหว่างจ่ายบิล AI กับจ้างคน

ตัวอย่างที่คลิปยก:

- พนักงานใช้ token มูลค่า 200 ดอลลาร์ต่อสัปดาห์ → 10,000 ดอลลาร์ต่อปีต่อคน
- ถ้ามีพนักงาน 40,000 คน → 400 ล้านดอลลาร์ต่อปี
- ถ้ามีพนักงาน 90,000 คน → 900 ล้านดอลลาร์ต่อปี
- AT&T ถูกเล่าว่าใช้เกือบ 8 พันล้าน token ต่อวัน
- Meta ถูกเล่าว่าใช้เกือบ 60 ล้านล้าน token ต่อเดือน คิดเป็นราว 900 ล้านดอลลาร์ตาม blended price ของ Anthropic ในคลิป

ตัวเลขเหล่านี้ไม่ควรใช้เป็นข้อเท็จจริงแข็งโดยไม่ตรวจ Reuters / Bloomberg / company disclosure. แต่กรอบคิดสำคัญคือ **AI unit economics ต้องคูณด้วย usage ทั้งองค์กร** ไม่ใช่ดูแค่ราคา prompt เดี่ยว

**ผลคือ:** enterprise AI ROI ต้องรวม adoption policy, model choice, human oversight, token waste, และงานที่ AI ถูกกว่าคนจริง ๆ แยกจากงานที่แค่ดูทันสมัย

## เมื่อเทียบกับ “Code is Free”

หน้า [[code-is-free|Code is Free]] ใน wiki บอกว่า implementation cost ต่ำลงมาก และ scarcity ย้ายไปที่ human judgement, attention, และ token budget. คลิปนี้ไม่ได้ลบกรอบนั้น แต่เพิ่มคำเตือนว่า “token budget” อาจไม่ได้เล็กพอจะมองข้ามได้

คลิปเองแยกงาน coding ออกมา: ใน coding tasks AI ยังถูกกว่าคน “undeniably cheaper” ตามคำกล่าวในคลิป แต่ใน data entry ส่วนต่างอาจน้อย และ call center คนอาจถูกกว่า

ดังนั้นความขัดแย้งที่ควรเก็บไว้คือ:

- ฝั่ง agentic engineering: code generation อาจถูกจน strategy เปลี่ยน
- ฝั่ง enterprise finance: การใช้ AI แบบกว้างทั้งองค์กรอาจแพงกว่าที่คิด โดยเฉพาะเมื่อ tokenmaxxing และ model choice ไม่มี guardrail

**ได้อะไร:** คำว่า “AI ถูกกว่าแรงงาน” ต้องแยกตามงาน ไม่ควรเหมารวมทั้งองค์กร

## ข้อควรระวัง

- Transcript เป็น auto-generated captions และมีการตัดต่อ quote / news clip หลายแหล่ง จึงควรตรวจ source เดิมก่อนยึดตัวเลข
- คลิปใช้ภาษากว้าง เช่น “AI was wiping out almost any type of job” ซึ่งควรอ่านเป็น narrative ของผู้ผลิต ไม่ใช่ข้อสรุปตลาดแรงงานทั้งหมด
- ตัวเลข Bloomberg, Reuters, Fortune, Gartner, WSJ, Economic Times, Meta, AT&T, Microsoft, และ Anthropic ในหน้านี้เป็น source-attributed ผ่านคลิป ไม่ใช่ wiki ตรวจแหล่งตรงแล้ว
- คลิปมีมุม dramatic/finance-media สูง จึงควรใช้เป็นแหล่งตั้งคำถามเรื่อง ROI มากกว่าเป็นหลักฐานเดียวสำหรับการตัดสินนโยบาย AI

## See also

- [[economy-media]]
- [[tokenmaxxing]]
- [[ai-token-economics]]
- [[enterprise-ai-roi]]
- [[ai-labor-cost-reversal]]
- [[usage-based-billing]]
- [[agentic-usage]]
- [[ai-data-center-bottlenecks]]
- [[code-is-free]]
- [[orchestration-tax]]
- [[ai-brain-fry]]
- [[anthropic]]
- [[openai]]
- [[microsoft]]
- [[meta]]
- [[nvidia]]
