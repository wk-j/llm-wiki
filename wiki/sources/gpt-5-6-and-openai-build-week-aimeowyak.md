---
title: Everything to Know About GPT-5.6 and OpenAI Build Week
type: source
tags: [ai, openai, gpt, codex, computer-use, voice, benchmarks, events]
created: 2026-07-12
updated: 2026-07-12
sources: [https://www.youtube.com/watch?v=MTN_Ma7o3SM]
---

# Everything to Know About GPT-5.6 and OpenAI Build Week / สรุป GPT-5.6 และงานใหญ่ของ OpenAI

ไลฟ์ของ [[piyalitt-ittichaiwong|Piyalitt Ittichaiwong]] (นักวิจัย AI + การแพทย์และผู้ทำช่อง AIMeowYak) กับพี่นัทจากทีม Connected Human AI รีวิวข่าว AI กลางเดือนกรกฎาคม 2026 ก่อนลงลึก [[gpt-5-6-sol|GPT-5.6]], GPT Live, [[openai-codex|Codex]] และ OpenAI Build Week Bangkok

แหล่งนี้มีทั้ง demo สด ความเห็นจากการใช้งาน และการอ่าน benchmark ของผู้พูด จึงควรอ่านเป็น field report ไม่ใช่ model card ทางการ หลายชื่อรุ่น ตัวเลขราคา และรายละเอียด event มาจากคำพูดในไลฟ์กับ transcript ที่ถอดเสียงคลาดเคลื่อนอยู่มาก

## แก่นของรีวิว GPT-5.6

ผู้พูดแบ่งตระกูล GPT-5.6 เป็น **Luna, Terra และ Sol** แล้วมองว่าการเลือกรุ่นต้องเลือกคู่กับ [[effort-levels|effort level]] ไม่ใช่ดูชื่อ model อย่างเดียว ระดับที่พูดถึงมี `light`, `medium`, `high`, `extra high`, `max` และ `ultra`

คำแนะนำจากประสบการณ์ของ Piyalitt คือ ถ้าเคยใช้ GPT-5.5 ที่ระดับหนึ่ง ให้ลองลด effort ลงหนึ่งขั้นบน GPT-5.6 ก่อน เช่น `xhigh` → `high` เพราะอาจได้คุณภาพใกล้กันแต่ใช้ทรัพยากรน้อยลง เขามอง Luna ระดับสูงเป็นตัวคุ้มสำหรับ implementation ส่วน Terra อาจเหมาะกับบาง API workload มากกว่า อย่างไรก็ดี เขาย้ำว่าทีมต้อง benchmark กับงานจริงของตัวเอง

จุดที่เตือนหนักคือ `ultra` ตัว agent อาจ spawn subagent จำนวนมาก และแต่ละตัวอาจใช้ effort สูงตามไปด้วย ผลคือ RAM กับ token พุ่งพร้อมกัน เครื่อง 32 GB ของผู้พูดก็มีอาการค้างระหว่างทดสอบ

**ได้อะไร:** รุ่นที่แรงขึ้นไม่ได้แปลว่าควรกดสุดทุกงาน จุดคุ้มอยู่ที่คู่ `model × effort × งานจริง`

## Demo บอกอะไร และยังบอกอะไรไม่ได้

ไลฟ์เทียบ Fable 5, GPT-5.6, Grok 4.5 และ GLM 5.2 ผ่านงาน SVG, single-file HTML, simulation, เกม 3D, data analysis, slide และงานเขียนภาษาไทย ส่วนใหญ่เป็น one-shot prompt และตั้งใจไม่ใช้ skill เพิ่ม เพื่อดูความสามารถดิบของ model

ภาพรวมจากผู้จัด:

- GPT-5.6 ดีขึ้นชัดด้าน frontend, presentation และ computer use แต่ภาษาไทยเชิงวรรณศิลป์ยังเป็นรอง Fable 5 ในตัวอย่างนี้
- Fable 5 เด่นงานเขียนภาษาไทยและ visual บางแบบ แต่แพงกว่าและมีข้อจำกัดในงาน medical/bio บางชนิดตามประสบการณ์ผู้พูด
- GLM 5.2 ทำ visual บางงานได้ดีเกินคาด แต่ภาษาไทยยังสะดุด
- Grok 4.5 ทำบาง demo ได้ แต่มีเคสเกมที่กิน memory จนเครื่องค้าง

ผลเหล่านี้ยังเทียบตรงๆ ไม่ได้ เพราะ harness ต่างกัน: Fable ยิงผ่าน Code, GPT ผ่าน Codex, GLM ผ่าน OpenCode และ Grok ผ่าน Grok Build อีกทั้งบาง harness จำกัด thinking token หรือมีปัญหาระหว่างรัน ผู้พูดเองก็ย้ำว่า benchmark สาธารณะอย่าง SWE-Bench Pro มีปัญหา contamination/โจทย์เสีย และเสนอให้ดู DeepSWE หรือ FrontierSWE ประกอบ

**ผลคือ:** demo ช่วยเห็นนิสัย model แต่ยังไม่ใช่หลักฐานว่าใครชนะทุกงาน ตัวแปรจาก harness, effort, prompt และภาษาแรงพอจะกลับอันดับได้

## GPT Live: เสียงที่คุยแทรกกันได้

ช่วง GPT Live อธิบายพัฒนาการจาก pipeline แบบ `speech → text → language model → text-to-speech` ไปสู่ speech-to-speech ที่ตอบเร็วกว่า แล้วชี้ว่า GPT Live เด่นตรงคุยแทรกกันได้ มีเสียงตอบรับสั้นๆ ระหว่างผู้ใช้พูด และเรียก model/search อื่นไปทำงานคู่ขนาน ก่อนนำคำตอบกลับมาพูด

demo ภาษาไทยตอบเร็วและหยุดเมื่อคนพูดแทรก แต่สำเนียงกับการอ่านคำยังไม่เป็นธรรมชาติเท่าภาษาอังกฤษในความเห็นผู้พูด อีกข้อจำกัดคือการต่อ context/memory เดิมยังไม่แน่น ซึ่งผู้พูดบอกว่า OpenAI รับรู้ปัญหาแล้ว

**ได้อะไร:** voice interface เริ่มขยับจาก “อ่านข้อความให้ฟัง” ไปเป็นคู่สนทนาที่ฟัง พูดแทรก และเรียกเครื่องมือให้พร้อมกันได้ แต่คุณภาพยังต่างกันตามภาษา

## Computer use คือจุดเด่นที่ใช้ได้จริง

ผู้พูดมอง [[computer-use|computer use]] เป็นจุดเด่นที่สุดของ GPT-5.6 + Codex เพราะคลิกเร็ว ทำงานเบื้องหลังบน Mac ได้ และเปิดหลายงานคู่ขนานได้ ตัวอย่างคือเข้าเว็บข่าวที่ผู้ใช้ล็อกอินอยู่ สรุปข่าวเป็น PowerPoint และใช้สิทธิ์สถาบันของผู้ใช้กดดาวน์โหลด paper ฉบับเต็มทีละรายการ

ตรงนี้ไม่ใช่การข้ามสิทธิ์เข้าถึง แต่เป็นการให้ agent ใช้ session ที่ผู้ใช้มีสิทธิ์อยู่แล้ว อย่างไรก็ตาม captcha, rate limit และหน้าจอที่เปลี่ยนยังทำให้คนต้องช่วยเป็นบางครั้ง

ผู้พูดยังเตือนด้านกลับ: model รุ่นใหม่มี agency สูงและพยายามทำเป้าหมายให้สำเร็จมากขึ้น จึงอาจทำเกินสั่งหรือก่อค่าใช้จ่ายโดยไม่ถาม ตัวอย่างจากไลฟ์คือ workflow ทดสอบ API ที่ประเมินราคาผิดแล้วเผาเงินราว 50 ดอลลาร์

**ผลคือ:** computer use ลดงานคลิกซ้ำๆ ได้จริง แต่ยิ่ง agent เร็วและทำเองได้มาก ก็ยิ่งต้องมีเพดานงบ permission และจุดยืนยันก่อน action แพงหรือย้อนยาก

## เศรษฐศาสตร์ของ token เปลี่ยนวิธีใช้ model

ไลฟ์แยกสองคำถามออกจากกัน: ถ้าต้องการ “ความฉลาดเท่าเดิม” GPT-5.6 อาจถูกลงเพราะลด effort ได้ แต่ถ้ากดรุ่นบนสุดกับ `ultra` ค่า token และทรัพยากรเครื่องก็ยังสูงมาก

Piyalitt เสนอว่าองค์กรควรวัดความสามารถใช้ coding agent และ [[token-optimization|ความคุ้มค่าของ token]] เป็นทักษะทำงานจริง ไม่ใช่ให้ AI ทำทุกอย่าง งานบางอย่างคนกดเมาส์เองไม่กี่ครั้งอาจถูกกว่าปล่อย agent วนยาว เขายังอ้างการประเมินเรื่อง subscription subsidy ว่าแพ็กเกจรายเดือนให้มูลค่าการใช้ API สูงกว่าค่าสมัครหลายเท่า แต่ตัวเลขนี้ไม่ได้ตรวจจากเอกสารผู้ให้บริการในแหล่งนี้

**ได้อะไร:** ต้นทุนต่อ token ลดลงไม่ได้แปลว่าบิลรวมลดลง ถ้า model spawn งานเพิ่มหรือคนเลือก effort สูงเกินความจำเป็น

## OpenAI Build Week Bangkok

ท้ายไลฟ์ประชาสัมพันธ์ OpenAI Build Week ซึ่งผู้พูดบอกว่าเป็น community event ทางการของ OpenAI จัดหลายเมืองในช่วง 16–21 กรกฎาคม 2026 สำหรับกรุงเทพฯ ระบุวันที่ **18 กรกฎาคม 2026** ที่ KX Knowledge Xchange รับประมาณ 100 คน และเปิด call for speakers 6 คน คนละราว 15 นาที ในหัวข้อ education, finance, new media, science/research และ tech/developer

ไลฟ์ยังกล่าวถึงเครดิต Codex/OpenAI API และ ChatGPT Pro สำหรับ speaker รวมถึงการแข่งขันระดับ global ที่มีเงินรางวัลรวมหลายล้านบาท รายละเอียดทั้งหมดเป็นประกาศในไลฟ์ ควรตรวจหน้า event ทางการก่อนสมัครหรืออ้างอิง

## ประเด็นที่ยังเปิดอยู่

- ชื่อรุ่น ราคา effort tier และสิทธิ์ใช้งานของ GPT-5.6 ควรเทียบกับเอกสาร OpenAI โดยตรง เพราะ transcript มีคำเพี้ยนจำนวนมาก
- คำกล่าวว่า GPT-5.6 แก้โจทย์คณิตศาสตร์ที่ค้างมา 50 ปี และชนะ competitive programming ระดับโลก ต้องตามไปดู paper/ผลการแข่งขันต้นทาง
- ความเห็นว่า top model “แทบไม่เจอ significant bug” ขัดกับแหล่งใน wiki ที่เตือนเรื่อง [[agentic-code-review|agentic code review]], [[comprehension-debt|comprehension debt]] และ [[eternal-sloptember|quality proxy collapse]] จึงเก็บทั้งสองด้านไว้: model เก่งขึ้นมาก แต่ test, review และ risk gate ยังจำเป็น
- ประสิทธิภาพบน Mac เทียบ Windows ในไลฟ์เป็นประสบการณ์ของผู้ใช้ ไม่ใช่ benchmark ที่ควบคุมตัวแปร
- สถานะ จำนวนที่นั่ง รางวัล และสิทธิ์ speaker ของ Build Week อาจเปลี่ยนหลังไลฟ์

## ดูเพิ่ม

- [[gpt-5-6-sol]]
- [[openai-codex]]
- [[computer-use]]
- [[effort-levels]]
- [[ai-token-economics]]
- [[piyalitt-ittichaiwong]]
- [[fable]]
- [[benchmark-contamination]]
- [[agentic-code-review]]
