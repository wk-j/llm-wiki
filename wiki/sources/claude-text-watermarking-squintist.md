---
title: Claude Now Watermarks Its Text. How Do You Even Do That?
type: source
url: https://www.youtube.com/watch?v=3FhxdhVMJoU
author: Squintist (YouTube)
tags: [ai, watermarking, ai-detection, regulation, anthropic, google]
date_ingested: 2026-08-16
created: 2026-08-16
updated: 2026-08-16
sources: [claude-text-watermarking-squintist.md]
---

# Claude Now Watermarks Its Text — Squintist

วิดีโอจากช่อง [[squintist|Squintist]] (ช่อง YouTube ที่ทำวิดีโอด้วย AI เกือบทั้งหมด และบอกเองตรง ๆ) เล่าข่าวว่า [[anthropic|Anthropic]] เริ่ม watermark ข้อความที่ Claude เขียน แล้วถอยออกมาอธิบายว่า watermark ข้อความทำงานยังไง ต่างจาก AI detector ตรงไหน และทำไม EU ถึงบังคับ

## ประกาศของ Anthropic (สิงหาคม 2026)

เดือนสิงหาคม 2026 Anthropic ออก support page ใหม่ บอกว่า **Claude model รุ่นใหม่ทุกตัวจะ watermark ข้อความที่มันเขียนแบบมองไม่เห็น** จุดสำคัญคือ mark ไม่ได้อยู่ใน metadata ของไฟล์ ไม่ใช่อักขระซ่อน แต่**อยู่ในการเลือกคำเอง** เลย copy-paste ไปไหน mark ก็ตามไปด้วย

ความหมายของ mark ก็ระบุชัด — เจอ mark แปลว่า Claude "แตะ" ข้อความนี้ ไม่ได้บอกว่าใครเป็นคนเขียน คำของ Anthropic เองตามที่วิดีโอยกมา:

> "A detected mark means the content may have been processed by Claude."

แปลว่า proofread, แปลภาษา, สรุป, หรือเขียนใหม่หมด — ได้ mark แบบเดียวกัน เคสที่วิดีโอใช้เปิดเรื่อง (อ้างโพสต์ของ Peter Harrell): เขียนรายงานพันคำเองทุกคำ แล้วให้ Claude ช่วย copy-edit สิ่งที่ได้กลับมาอาจติด mark ที่เครื่องอ่านว่า "AI ทำ"

## ทำไม text ถึง watermark ยาก

รูปภาพมี pixel เป็นล้าน ขยับไม่กี่พันจุดตาคนไม่เห็น เสียงมี background noise ให้ซ่อนสัญญาณ แต่ text ไม่มีที่ซ่อนแบบนั้น — วิดีโอเปรียบว่า text เหมือน barcode เปลี่ยนคำเดียวทุกคนเห็น

ทางลัดที่คนมักคิดถึงมีสองแบบ และทั้งคู่ไม่เวิร์กจริง:

1. **ซ่อนอักขระล่องหน** เช่นสลับ space ธรรมดากับ space หน้าตาเหมือนกันเป็น pattern ลับ — ใส่ง่าย แต่ find & replace ครั้งเดียวก็หลุด
2. **ไม่ watermark เลย แต่เดาจากสไตล์** เช่นนับ em dash นับคำว่า "delve" — อันนี้คือสิ่งที่คนส่วนใหญ่เข้าใจว่าเป็น "AI detection" (ดู [[ai-text-detectors|AI detectors]])

## กลไกจริง: rig การทอยลูกเต๋าตอน sampling

คำตอบจริงคือฝัง signal ตอนที่ model กำลังเลือกคำ เวอร์ชันของ Google ชื่อ [[synthid|SynthID]] หลักการ (ดูรายละเอียดที่ [[llm-text-watermarking]]):

- Language model ไม่เคยเลือกคำถัดไปแบบตายตัว ทุก step มันคำนวณรายการคำที่เป็นไปได้พร้อมความน่าจะเป็น แล้ว "ทอยลูกเต๋า" เลือกหนึ่งคำ ระดับความสุ่มคุมด้วย **temperature**
- SynthID แทรก **tournament** เข้าไปในการทอย: คำ candidate (เช่น big / large / huge / vast) แข่งกันเป็นคู่ ผู้ชนะตัดสินด้วยคะแนนลับที่มาจาก **secret key ผสมกับคำไม่กี่คำก่อนหน้า**
- Key เลย reshuffle ทุก step — step นี้ key อาจเชียร์ big กับ vast, step ถัดไปกลับไปเชียร์ large กับ huge ไม่มีคำไหนถูกเชียร์ถาวร รันล้าน step ความถี่ของแต่ละคำเท่ากับตอนไม่มี tournament — ข้อความอ่านปกติ สถิติคำไม่ขยับ
- **Detection คือกลับด้านของ trick เดิม**: ตัวตรวจถือ key เดียวกัน ไล่ตามข้อความ redo คณิตของ sampler ทีละคำ แล้วดูว่าคำที่อยู่ตรงนั้นได้คะแนนสูงบ่อยแค่ไหน ข้อความคนเขียนจะออกมาราวเหรียญออกหัวครึ่งเดียว ข้อความจาก sampler ที่ติด key จะสูงกว่าครึ่งอย่างเห็นได้ — แต่ต้องดูรวมหลายร้อยคำ ไม่ใช่คำเดียว

## ผลทดลอง 20 ล้าน response ใน Gemini

Google รัน SynthID จริงใน Gemini แล้วตีพิมพ์ใน Nature: ประมาณ 20 ล้าน response ครึ่งหนึ่งติด watermark ครึ่งหนึ่งไม่ติด อัตรากด thumbs-up ต่างกัน 1/100 ของเปอร์เซ็นต์ (สถิติถือว่าไม่ต่าง) และช้าลงราวครึ่งเปอร์เซ็นต์ — คนให้คะแนนคำตอบแยกไม่ออกว่ามี watermark

## จุดอ่อนสองข้อ

**ข้อแรก: ไม่มีที่ให้ซ่อนใน "Paris"** — tournament ต้องมีผู้แข่ง ถามเมืองหลวงฝรั่งเศส คำตอบรับได้มีคำเดียว code ก็มีปัญหาเดียวกัน (synonym ผิดตัวเดียว build พัง) ข้อความสั้นก็เช่นกัน watermark อาศัย "อิสระทางภาษา" — ยิ่งพูดได้หลายแบบ ยิ่งมีที่ rig

**ข้อสอง: ล้างออกได้** — แปลไปภาษาอื่นแล้วแปลกลับ หรือให้เครื่องมือ paraphrase เขียนใหม่ พอคำเปลี่ยน คะแนนลับก็ไม่ตรงตำแหน่ง mark หาย งานวิจัยหนึ่งทีม (preprint กรกฎาคม 2026) ทดสอบกับ implementation สาธารณะ (MarkLLM บน Gemma-2-9B): paraphrase แล้ว detection หายไป **58 จาก 59 เคส** — ตัวเลขนี้มาจาก "home version" ไม่ใช่ระบบ production ของ Google ให้อ่านเป็นผลแรก แต่ตัว attack ใช้ได้จริงแน่

## กลับมาที่รายงานที่คุณเขียนเอง

Anthropic **ยังไม่เปิดเผยว่า mark ของตัวเองทำงานยังไง** แต่วิดีโอให้เหตุผลว่า watermark ประเภทนี้ใส่ได้ตอน model กำลังเลือกคำเท่านั้น stamp ทีหลังไม่ได้ — เพราะฉะนั้นตอน Claude copy-edit ข้อความ ผลลัพธ์ก็ออกผ่าน sampler ตัวเดียวกับทุกอย่างที่ Claude เขียน (ตรงนี้เป็น **การอนุมานของวิดีโอ** ไม่ใช่คำยืนยันจาก Anthropic)

ขอบของมันอยู่ตรงนี้: ถ้า Claude แก้แค่ comma สองตัว แทบทุก step มีคำรับได้คำเดียว — ไม่มี tournament ไม่มี signal ยิ่ง model rephrase มาก mark ยิ่งแรงได้ และ copy-edit จริง ๆ ก็ rephrase เยอะ

## เหตุผลที่ lab ทำ: Brussels

[[eu-ai-act|EU AI Act]] Article 50 บอกว่าตั้งแต่ 2 สิงหาคม (2026) output ของ generative AI ต้องถูก mark แบบ machine-readable โดยมีข้อยกเว้นสำหรับ "standard editing" — แก้สะกด แก้ grammar แปลภาษา ไม่ต้อง mark

จุดตึงที่วิดีโอชี้: **กฎหมายยกเว้น spell check แต่ Anthropic ก็ mark อยู่ดี** (เพราะ mark ฝังที่ sampler แยกไม่ได้ว่างานไหนคืองานแก้เล็ก)

Code of Practice ของ European Commission เติมรายละเอียด: watermark ข้อความ free-form ที่ยาวกว่าหนึ่งย่อหน้าจริงจัง ให้คนตรวจ mark ได้ฟรี — แต่สำหรับ plain text ยอมให้ lab จำกัดตัวตรวจไว้กับ verified experts ก่อน เพราะ text mark เป็นชนิดที่เชื่อถือได้น้อยที่สุด ผู้ลงนาม: Anthropic, Google, OpenAI, Meta, Microsoft, Mistral — code เป็น voluntary แต่กฎหมายข้างหลังไม่ใช่ วิดีโอสรุปว่าถ้าแผนคือย้ายไป model ที่ไม่ watermark — ทุกเจ้าลงชื่อแล้ว

## AI detectors เป็นคนละเรื่องกันเลย

เครื่องมือที่คนส่วนใหญ่เจอจริง (GPTZero, [[pangram|Pangram]], Turnitin) **ไม่มี key ไม่มี tournament** — มันอ่านข้อความแล้วตัดสินจากสไตล์ ยุคแรกวัด perplexity (คำเดาง่ายแค่ไหน) กับ burstiness (จังหวะประโยคสม่ำเสมอแค่ไหน) ตอนนี้เป็น neural network เทรนกับตัวอย่างคน/AI หลายล้านชิ้น วิดีโอเปรียบ: watermark คือ serial number ตอกจากโรงงาน ส่วน detector คือผู้เชี่ยวชาญลายมือ

ประวัติของผู้เชี่ยวชาญลายมือ (ดูเต็มที่ [[ai-text-detectors]]):

- OpenAI ทำ detector เองปี 2023 — จับ AI ได้ ~26% flag คนผิด 9% ถอนออกภายในไม่กี่เดือน
- งาน Stanford ปี 2023: essay TOEFL ของคนที่อังกฤษไม่ใช่ภาษาแม่ ผ่าน detector ดัง 7 ตัว โดนตัดสินเป็น AI เฉลี่ย 61%
- Pangram รายงานว่าปัจจุบัน flag ชุดข้อมูลเดิมเป็นศูนย์ — เป็น claim ของ vendor เอง และ failure mode (ภาษาอังกฤษทางการ ระวัง ๆ ของ non-native) ยังเป็นจุดอ่อนโดยธรรมชาติ
- อาจารย์สอนเขียน 25 ปี ขัดเรื่องสั้นแนว comedy หกเดือน — Pangram ตัดสิน 100% AI (rule of three ซึ่งเป็นเทคนิคเขียนของมนุษย์ กลายเป็นสัญญาณ "เครื่องเขียน")
- NeurIPS 2026 Position Paper Track (กติกา: ใช้ AI ได้แค่ copy-edit) scan 969 submissions ด้วย Pangram, desk-reject 178 ฉบับ (18%) ก่อน peer review โดยไม่มี appeal — ผู้ถูก reject รายหนึ่งเอา paper ของ track chair ไปเข้า detector เดียวกัน ได้ 24–69%

## ล้าง mark / arms race

อยากให้ mark หาย: แปลไปกลับ หรือส่งให้ model ตัวที่สองแล้วสั่ง "rewrite" — model นั้นเป็น open model 9B ที่รันบนเครื่องบ้านก็ได้ ไม่มี provider ใน loop ไม่มี watermark และ **open model บังคับให้ mark ไม่ได้ เพราะคนที่รันคุมลูกเต๋าเอง** (เชื่อมกับ [[open-weight-models]])

ฝั่ง detector ก็ retrain สู้กับ "humanizer" (undetectable.ai, QuillBot, StealthGPT — product category ที่มีอยู่เพราะ detector มี) สองตลาดนี้เลยต่างฝ่ายต่างเลี้ยงกันให้โต แต่ปัญหาลึกกว่านั้นคือ premise: style detector ใช้ได้ต่อเมื่องานเขียน AI ยังดูต่างจากงานเขียนคน — และความต่างนั้นกำลังแคบลงจากทั้งสองฝั่ง model ถูกเทรนให้เหมือนคน ส่วนคนก็ดูดสไตล์ model กลับ (งาน Max Planck ~280,000 วิดีโอ YouTube พบคำโปรดของ ChatGPT อย่าง delve / meticulous / realm โผล่ในการพูดของคนเพิ่มถึง 50%)

> "A style detector is a snapshot of a difference, and the difference is dissolving."
> (style detector คือภาพนิ่งของความต่าง ณ เวลาหนึ่ง — และความต่างนั้นกำลังจางหายไป)

## Watermark ตอบอะไรได้จริง

ก่อนหน้านี้ prose ที่ลื่นเป็นสัญญาณว่ามีคนตั้งใจขัด ตอนนี้ shortcut นั้นหายไป (ตรงกับ [[quality-proxy-collapse]]) — watermark ตอบได้หนึ่งคำถาม: **คำพวกนี้ผ่าน model ตัวนี้มาหรือเปล่า** style detector พยายามเดาคำถามเดียวกันโดยไม่มี mark ทั้งคู่ตอบไม่ได้ว่า claim จริงไหมหรือของดีไหม — อันนั้นยังเป็นหน้าที่คนอ่าน

## Meta: ช่องนี้ทำยังไง

ผู้ทำช่องบอกเองว่า script เกือบทุกคำมาจาก AI model สักตัว เสียงพากย์ก็ generate ใช้หลาย model + code ช่วย research/draft แต่ rewrite เยอะ บางไอเดียก็ทิ้ง ทำมาไม่กี่เดือน ใกล้ 10,000 subscribers — เป็นการทดลองว่าทำ YouTube ได้ไหมโดยไม่โชว์หน้า ไม่ใช้เสียงจริง ไม่ทำ thumbnail หน้าตกใจ

## คำถามเปิด / สิ่งที่ยังไม่ยืนยัน

- กลไก watermark ของ Anthropic เป็น sampling-time แบบ SynthID จริงไหม — วิดีโออนุมานจากธรรมชาติของ watermark ชนิดนี้ ไม่ใช่ spec ที่ Anthropic เปิดเผย
- ตัวเลข 58/59 มาจาก reimplementation สาธารณะ ไม่ใช่ detector production ของ Google
- ความแม่นปัจจุบันของ Pangram/GPTZero เป็น vendor claim (GPTZero technical report 2026 ก็ vendor-authored)
- "ทุกเจ้าลงชื่อ" ครอบคลุมแค่ code of practice ฝั่ง EU — ภาระผูกพันจริงต่อผู้ใช้นอก EU ยังไม่ชัดจากวิดีโอ
- OpenAI ณ เวลาวิดีโอ ใส่ C2PA/SynthID ในรูปภาพ ส่วน text provenance ยัง "planned"

## See also

- [[llm-text-watermarking]]
- [[ai-text-detectors]]
- [[synthid]]
- [[eu-ai-act]]
- [[pangram]]
- [[squintist]]
- [[anthropic]]
- [[quality-proxy-collapse]]
- [[open-weight-models]]
