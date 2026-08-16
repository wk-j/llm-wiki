---
title: LLM Text Watermarking
type: concept
tags: [ai, watermarking, provenance, sampling, regulation]
created: 2026-08-16
updated: 2026-08-16
sources: [claude-text-watermarking-squintist.md]
---

# LLM Text Watermarking / ลายน้ำในข้อความที่ LLM เขียน

การฝังสัญญาณลับลงในข้อความที่ language model เขียน โดยไม่ให้คนอ่านรู้สึก และให้ตัวตรวจที่ถือ key ยืนยันทีหลังได้ว่า "ข้อความนี้ผ่าน model ตัวนี้มา" จุดที่ทำให้เรื่องนี้ต่างจาก watermark รูปภาพ: mark ไม่ได้อยู่ใน metadata หรืออักขระซ่อน แต่**อยู่ในการเลือกคำเอง** เลยติดไปกับ copy-paste ด้วย

แหล่งหลักตอนนี้คือ [[claude-text-watermarking-squintist|วิดีโอของ Squintist]] ที่อธิบายกลไกของ [[synthid|SynthID]] (Google DeepMind) และข่าวที่ [[anthropic|Anthropic]] เริ่ม watermark ข้อความของ [[claude|Claude]] รุ่นใหม่ (สิงหาคม 2026)

## ทำไม text ถึงเป็นเคสยาก

รูปภาพมี pixel เป็นล้านให้ขยับแบบตาไม่เห็น เสียงมี noise ให้ซ่อน แต่ text เหมือน barcode — เปลี่ยนคำเดียวทุกคนเห็น ทางลัดสองแบบที่ใช้ไม่ได้จริง:

- **อักขระล่องหน** (space หน้าตาเหมือนกันสลับเป็น pattern) — find & replace ครั้งเดียวหลุด
- **เดาจากสไตล์** — อันนั้นไม่ใช่ watermark แล้ว เป็น [[ai-text-detectors|AI detector]] ซึ่งเป็นคนละกลไกและคนละระดับความน่าเชื่อถือ

## กลไก: rig ลูกเต๋าตอน sampling

ใช้ข้อเท็จจริงว่า model ไม่เคยเลือกคำถัดไปตายตัว — ทุก step มันมีรายการคำ candidate พร้อมความน่าจะเป็น แล้วสุ่มเลือก (ระดับความสุ่มคือ temperature: งาน coding รันเย็นใกล้ศูนย์ งาน brainstorm รันอุ่น)

วิธีของ SynthID เรียกว่า **tournament sampling**:

1. ตอนจะเลือกคำ ให้ candidate (เช่น big / large / huge / vast) แข่งกันแบบแพ้คัดออก
2. ผู้ชนะแต่ละคู่ตัดสินด้วยคะแนนลับ ที่คำนวณจาก **secret key ผสมกับคำไม่กี่คำที่เพิ่งเขียน**
3. เพราะ key ผสมกับ context มันจึง reshuffle ทุก step — ไม่มีคำไหนถูกเชียร์ถาวร รันยาว ๆ ความถี่คำเท่ากับไม่ใส่ watermark ข้อความอ่านปกติ
4. แต่สำหรับ key ตัวที่ lab ใช้จริง คำที่ออกมาจะ "บังเอิญ" เป็นคำที่ key เชียร์ ณ step นั้นบ่อยกว่าที่โอกาสสุ่มอธิบายได้

**Detection คือกลับด้าน:** ตัวตรวจถือ key ไล่ redo คณิตของ sampler ทีละคำ แล้วนับว่าคำที่อยู่จริงได้คะแนนสูงบ่อยแค่ไหน — งานเขียนคนออกมาราวครึ่งเดียว (เหมือนโยนเหรียญ) งานจาก sampler ติด key สูงกว่าครึ่งชัดเจน แต่ต้องรวมหลายร้อยคำ ไม่มี database ไม่ต้องรัน model — คำในข้อความคือหลักฐานเอง

**ผลคือ:** ได้ signal ที่มองไม่เห็น ติดไปกับข้อความ และตรวจได้ด้วย key อย่างเดียว โดยแทบไม่กระทบคุณภาพ (การทดลอง ~20 ล้าน response ใน Gemini: thumbs-up ต่าง 0.01%, ช้าลง ~0.5%)

## จุดอ่อนที่มากับกลไก

จุดอ่อนทั้งคู่ตามมาจากวิธีทำงานตรง ๆ:

- **Low entropy = ไม่มีที่ซ่อน** — คำตอบข้อเท็จจริง ("Paris"), code (synonym ผิดตัวเดียว build พัง), ข้อความสั้น ล้วนมีคำรับได้แบบเดียว tournament เลยมีผู้แข่งคนเดียว watermark อาศัยอิสระทางภาษา ยิ่งพูดได้หลายแบบยิ่งมีที่ rig
- **ล้างออกได้ (paraphrase washing)** — แปลไปกลับหรือให้ model อื่น rewrite พอคำเปลี่ยน คะแนนลับไม่ตรงตำแหน่ง mark หาย preprint กรกฎาคม 2026 พบว่า paraphrase ลบ detection ได้ 58/59 เคส — บน reimplementation สาธารณะ (MarkLLM + Gemma-2-9B) ไม่ใช่ระบบ production ของ Google จึงเป็นผลแรก ไม่ใช่คำตัดสิน
- **บังคับได้เฉพาะ model ที่ provider คุม sampler** — [[open-weight-models|open model]] ที่รันเองบนเครื่องบ้าน คนรันคุมลูกเต๋าเอง จะไม่ mark ก็ได้ นี่คือช่องบังคับใช้ที่กฎแบบ [[eu-ai-act|EU AI Act]] ยังตอบไม่จบ

## Mark หมายถึง "ผ่าน model" ไม่ใช่ "model เป็นคนแต่ง"

ประเด็นที่คนเข้าใจผิดง่ายที่สุด: watermark ชนิดนี้ใส่ได้ตอน model เลือกคำเท่านั้น ดังนั้นงานทุกอย่างที่ออกจากปาก model — proofread, แปล, สรุป, เขียนใหม่หมด — ได้ mark แบบเดียวกัน คำของ Anthropic เอง: mark แปลว่า content "may have been processed by Claude"

ขอบเขตของ signal ก็ตามหลัก entropy: แก้ comma สองตัว = แทบไม่มี signal, copy-edit จริงที่ rephrase เยอะ = mark แรงได้ ผลข้างเคียงคือรายงานที่คุณเขียนเองพันคำ พอผ่าน Claude ขัด grammar ก็อาจติด mark — ทั้งที่ [[eu-ai-act|กฎ EU]] ยกเว้น standard editing แต่ Anthropic mark อยู่ดี (แยกที่ sampler ไม่ได้ว่างานไหนงานเล็ก)

## สิ่งที่ watermark ตอบได้และตอบไม่ได้

| คำถาม | Watermark ตอบได้ไหม |
|---|---|
| คำพวกนี้ผ่าน model ตัวนี้มาไหม | ได้ (ถ้า mark ยังอยู่ และข้อความยาว/มี entropy พอ) |
| ใครเป็นคนแต่งเนื้อหา | ไม่ได้ — คน dictate ให้ AI เรียบเรียงก็ติด mark |
| เนื้อหาจริงไหม ดีไหม | ไม่ได้ |
| ไม่เจอ mark = คนเขียนใช่ไหม | ไม่ได้ — อาจโดนล้าง, สั้นเกิน, หรือมาจาก model ที่ไม่ mark |

ตรงนี้เชื่อมกับ [[quality-proxy-collapse]]: prose ลื่น ๆ เคยเป็นหลักฐานว่ามีคนลงแรง ตอนนี้ใช้ไม่ได้แล้ว watermark คือความพยายามสร้าง proxy ใหม่ที่แคบแต่ตรวจได้จริง — ตอบแค่ provenance ไม่ตอบคุณภาพ

## สถานะของ Anthropic

Anthropic ยังไม่เปิดเผยกลไกของตัวเอง วิดีโออนุมานว่าเป็น sampling-time watermark แบบเดียวกับ SynthID (เพราะ stamp ทีหลังไม่ได้) — เก็บเป็นการอนุมานที่มีเหตุผล ไม่ใช่ spec ที่ยืนยัน คำถามเปิด: ใช้ key เดียวหรือหลาย key, ใครตรวจได้บ้าง, ครอบคลุม surface ไหน (API/Claude Code/consumer), และมีผลกับ code ที่ agent เขียนแค่ไหนเมื่อ code เป็น low-entropy โดยธรรมชาติ

## See also

- [[claude-text-watermarking-squintist]]
- [[synthid]]
- [[ai-text-detectors]]
- [[eu-ai-act]]
- [[quality-proxy-collapse]]
- [[open-weight-models]]
- [[llm-nondeterminism]]
- [[anthropic]]
