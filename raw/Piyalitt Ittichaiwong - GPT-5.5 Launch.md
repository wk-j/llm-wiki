Piyalitt Ittichaiwong

9h

โมเดล GPT 5.5 เป็น Model แรกที่ทำให้ผมรู้สึกว่าการเรียนและเขียนโปรแกรมมา 20 ปี ของผมสู้มันไม่ได้เลยจริงๆ และที่มากไปกว่านั้นคือ ตอนนี้ที่ผมยังคิดว่าผมเหนือกว่ามัน คือ ผม connect the dot เพื่อให้มันทำงานการแพทย์ได้ แต่ตอนนี้กลับกลายเป็นว่ามันเป็นอาจารย์แพทย์ที่ Coding ได้เหรียญทองโอลิมปิก พูดตามตรงว่าถ้าไม่ใช่งาน PhD ที่ผมทำอยู่นั้น แทบจะจบใน 1 prompt (ถ้ารอได้ เพราะ มันทำงานช้าครับ)

Note: เดี๋ยวจากนี้จะมีแชร์ Content เรื่อยๆ โดยเฉพาะท่านที่อยากใช้แบบ Claude Cowork สามารถเข้าไปรอได้ใน OpenAI Codex Community คร้าบ (มี Post บางส่วนแล้วดูในสารบัญตรง features ด้านบนได้เลย) ส่วนท่านที่เป็น Coder ต้องระวังด้วยนะครับ ราคา GPT-5.5 แพงกว่าเดิม 2 เท่า ดังนั้นเรื่อง Prompt Management ก็เป็นเรื่องสำคัญที่ต้องติดตามเช่นเดียวกันครับ

โดยอันนี้อ้างอิงจากที่ผมได้ทดสอบก่อนอยู่ช่วงหนึ่ง โดยเฉพาะตัวเต็มที่ออกมาเมื่อวาน พูดโดยสรุปคือเป็น Model ที่เก่งใกล้ Anthropic Mythos preview มากๆ (เว้น SWE-Bench Pro ที่ในการ์ดของ Anthropic ก็เขียนเหมือนกันว่ามี sign ของ Memorization แต่ผมคิดว่าเขาไม่ได้ตั้งใจ Benchmaxx น่าจะพลาด) แต่ว่าทุกคนสามารถเข้าถึงได้...

ดังนั้นไม่ต้องพูดถึง Opus 4.7 เลยครับ ผมคิดว่า Anthropic เหนื่อยแน่นอน แม้แต่ frontend พอ GPT ใช้ gpt-image-2 ได้ ผมว่าถ้า prompt ดีๆ ให้ design system GPT-5.5 ทำได้ดีกว่า อย่างไรก็ตามกลับกลายเป็นว่า GPT-5.5 แพงกว่า Opus เล็กน้อยทั้งๆที่ปกติแล้วจะถูกกว่าประมาณครึ่งหนึ่งแปลว่าเขาใช้ทรัพยากรมากจริงๆ

Note: และเสาร์นี้เรามีเปิดตัว Hackthon OpenAI x สมาคมปัญญาประดิษฐ์ประเทศไทยนะครับบ credit รวมเป็นล้าน อ่านหรือมีคำถามเพิ่มเติมเชิญ ได้ที่ https://www.facebook.com/piyalitt/posts/27391274130460334

═══════════════════

GPT-5.5 คืออะไร
- OpenAI เปิดตัว GPT-5.5 ซึ่งเป็นโมเดลที่ฉลาดที่สุดและใช้งานง่ายที่สุดเท่าที่เคยมีมา และเป็นก้าวถัดไปสู่วิธีการทำงานบนคอมพิวเตอร์รูปแบบใหม่
- จุดเด่นของ GPT-5.5 คือเข้าใจสิ่งที่ผู้ใช้ต้องการทำได้เร็วขึ้น และสามารถแบกรับภาระงานด้วยตัวเองได้มากขึ้น
- เก่งในการเขียนโค้ดและ debug, การค้นคว้าวิจัยบน internet, การวิเคราะห์ข้อมูล, สร้างเอกสารและ spreadsheet, ใช้งาน software ต่างๆ และเคลื่อนย้ายข้ามเครื่องมือจนกว่างานจะเสร็จ
- แทนที่เราต้องควบคุมทุกขั้นตอนอย่างละเอียด เราสามารถมอบงานที่ซับซ้อนหลายส่วนแบบยุ่งเหยิงให้ GPT-5.5 แล้วเชื่อใจให้มันวางแผน ใช้เครื่องมือ ตรวจสอบผลงานตัวเอง นำทางผ่านความคลุมเครือ และทำงานต่อไปเรื่อยๆ

ฉลาดขึ้นโดยไม่เสียความเร็ว
- โมเดลที่ใหญ่และเก่งขึ้นมักทำงานช้าลง แต่ GPT-5.5 ให้ latency ต่อ token เท่ากับ GPT-5.4 ในการใช้งานจริง
- ขณะเดียวกันก็ทำงานได้ในระดับสติปัญญาที่สูงกว่ามาก
- ยังใช้ token น้อยลงอย่างมีนัยสำคัญในการทำงาน Codex แบบเดียวกัน

ความสามารถด้าน Agentic Coding
- GPT-5.5 เป็นโมเดล agentic coding ที่แข็งแกร่งที่สุดของ OpenAI จนถึงปัจจุบัน
- Terminal-Bench 2.0: 82.7% (SOTA)
- SWE-Bench Pro: 58.6% (มี sign ของ memorization ตามการ์ดของ Anthropic — น่าจะไม่ได้ตั้งใจ benchmaxx)
- Expert-SWE (งาน 20 ชม./มนุษย์ — internal): ดีกว่า GPT-5.4
- ปรับปรุงคะแนนพร้อมกับใช้ token น้อยลง

ความเข้าใจเชิงโครงสร้างของระบบ
- Dan (CEO of Every): GPT-5.5 เป็นโมเดลเขียนโค้ดตัวแรกที่มี conceptual clarity จริงจัง — แก้ bug หลังเปิดตัวที่ GPT-5.4 ทำไม่ได้
- Pietro (CEO of MagicPath): merge branch ที่มีการเปลี่ยนแปลงหลักร้อยครั้งเข้ากับ main ในครั้งเดียว ~20 นาที
- วิศวกรอาวุโส: แข็งแกร่งกว่า GPT-5.4 และ Claude Opus 4.7 อย่างชัดเจน — จับปัญหาได้ล่วงหน้า คาดการณ์ความต้องการ test/review โดยไม่ต้องสั่ง; re-architect comment ใน markdown editor แบบ collaborative = กลับมาพบ stack ที่มี 12 diff เกือบสมบูรณ์

Knowledge Work
- GDPval (44 อาชีพ): 84.9%
- OSWorld-Verified: 78.7%
- Tau2-bench Telecom: 98.0% (ไม่ต้องปรับ prompt)
- FinanceAgent: 60.0%; internal investment-banking modeling: 88.5%; OfficeQA Pro: 54.1%
- OpenAI ใช้ Codex ภายใน 85%+ ของพนักงาน — ฝ่ายการเงินตรวจ K-1 จำนวน 24,771 ฟอร์ม/71,637 หน้า เร็วขึ้น 2 สัปดาห์; GTM อัตโนมัติรายงานรายสัปดาห์ประหยัด 5-10 ชม./สัปดาห์

วิจัยวิทยาศาสตร์
- GeneBench: ชนะ GPT-5.4 อย่างชัดเจน
- BixBench (bioinformatics): 80.5% (นำทุก published model)
- Derya (Jackson Laboratory): GPT-5.5 Pro วิเคราะห์ gene expression 62 samples × 28,000 genes = รายงานที่ทีมจะใช้เวลาหลายเดือน
- Bartosz (Adam Mickiewicz University): ใช้ Codex สร้าง app ด้าน algebraic geometry ใน 11 นาที จาก prompt เดียว
- Brandon (Axiom Bio): ความแม่นยำเพิ่มขึ้นอย่างมีนัยสำคัญบน eval การค้นพบยาที่ยากที่สุด

คณิตศาสตร์
- GPT-5.5 เวอร์ชันภายใน + harness พิเศษ ค้นพบบทพิสูจน์ใหม่เกี่ยวกับ off-diagonal Ramsey numbers (combinatorics) — ต่อมาถูกตรวจสอบใน Lean

Infrastructure
- ออกแบบร่วม / ฝึก / serve บน NVIDIA GB200 และ GB300 NVL72
- Codex + GPT-5.5 เขียน custom heuristic algorithm แบ่งและกระจาย traffic = เพิ่มความเร็ว token generation > 20%

Cybersecurity
- Preparedness Framework: High (ไม่ถึง Critical)
- CyberGym: 81.8% (GPT-5.4 = 79.0%, Claude Opus 4.7 = 73.1%)
- Redteam ภายใน+ภายนอก + early-access partners ~200 ราย

Access & Pricing
- ChatGPT: Plus/Pro/Business/Enterprise; GPT-5.5 Pro: Pro/Business/Enterprise
- Codex: Plus/Pro/Business/Enterprise/Edu/Go; context window 400K
- Fast mode: 1.5x token generation speed ที่ 2.5x ราคา
- API (เร็วๆ นี้): gpt-5.5 — $5/M input, $30/M output, 1M context
- GPT-5.5 Pro API: $30/M input, $180/M output
- Batch/Flex: ครึ่งราคา; Priority: 2.5x
- แพงกว่า GPT-5.4 2 เท่า และแพงกว่า Opus 4.7 เล็กน้อย (ปกติถูกกว่า Opus ครึ่งหนึ่ง)

สรุปภาพรวม
- Artificial Analysis Coding Agent Index: SOTA ที่ครึ่งราคาของคู่แข่ง frontier coding
- Justin (VP Enterprise AI, NVIDIA): "ไม่ใช่แค่การเขียนโค้ดที่เร็วขึ้น แต่เป็นวิธีการทำงานรูปแบบใหม่"
