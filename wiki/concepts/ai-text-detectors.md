---
title: AI Text Detectors
type: concept
tags: [ai, ai-detection, education, academia, false-positives]
created: 2026-08-16
updated: 2026-08-16
sources: [claude-text-watermarking-squintist.md]
---

# AI Text Detectors / เครื่องตรวจงานเขียน AI จากสไตล์

เครื่องมืออย่าง GPTZero, [[pangram|Pangram]], Turnitin ที่อ่านข้อความแล้ว "เดา" ว่า AI เขียนหรือคนเขียน จุดที่ต้องแยกให้ขาด: พวกนี้**ไม่ใช่** [[llm-text-watermarking|watermark]] — ไม่มี secret key ไม่มีอะไรฝังมาจากต้นทาง มันตัดสินจากสไตล์ล้วน ๆ [[claude-text-watermarking-squintist|วิดีโอของ Squintist]] เปรียบว่า watermark คือ serial number ตอกจากโรงงาน ส่วน detector คือผู้เชี่ยวชาญลายมือ — และผู้เชี่ยวชาญลายมือคนนี้พลาดมาแล้วหลายครั้ง

## ทำงานยังไง

ยุคแรก (GPTZero รุ่นต้น) วัดสองอย่าง: **perplexity** — คำในข้อความเดาง่ายแค่ไหน และ **burstiness** — จังหวะความยาวประโยคสม่ำเสมอแค่ไหน เรียบเกิน+สม่ำเสมอเกิน = น่าจะเครื่องเขียน ปัจจุบัน vendor เองบอกว่าคำอธิบายนี้ล้าสมัยแล้ว — ระบบตอนนี้เป็น neural network ที่เทรนกับตัวอย่างงานคน/งาน AI หลายล้านชิ้น แล้วหา "family resemblance"

## ประวัติความแม่น

- **OpenAI classifier (2023)** — จับ AI ได้ ~26% แต่ flag งานคนผิด 9% [[openai|OpenAI]] ถอนออกเองภายในไม่กี่เดือน
- **งาน Stanford (2023)** — essay TOEFL ของคนที่ภาษาอังกฤษไม่ใช่ภาษาแม่ ผ่าน detector ดัง 7 ตัว โดน flag เป็น AI เฉลี่ย **61%** เพราะภาษาที่ระวังและเป็นทางการของ non-native ดู "เรียบ" แบบเดียวกับที่ระบบมองว่าเป็นเครื่อง
- **ปัจจุบันดีขึ้น** — Pangram รายงาน flag ชุด TOEFL เดิมเป็นศูนย์ และ GPTZero มี technical report ปี 2026 แต่ทั้งคู่เป็นเอกสาร vendor เขียนเอง failure mode เดิมไม่ได้หายไป

## เคสความเสียหายจริง

- นักเรียนจงใจพิมพ์ผิดเพื่อไม่ให้โดน flag
- อาจารย์สอนเขียน 25 ปี ขัดเรื่องสั้น comedy หกเดือนแบบ line-by-line — Pangram ตัดสิน **100% AI** เพราะ comedy อาศัย rule of three (เทคนิควาทศิลป์ของมนุษย์แท้ ๆ) ซึ่งตอนนี้ detector อ่านเป็นสัญญาณเครื่อง
- **NeurIPS 2026 Position Paper Track** — กติกาให้ใช้ AI แค่ copy-edit ทางงาน scan submissions ทั้ง 969 ฉบับด้วย Pangram แล้ว desk-reject **178 ฉบับ (18%) ก่อน peer review โดยไม่มี appeal** ผู้ถูก reject รายหนึ่งเอา paper ตีพิมพ์แล้วของ track chair เข้า detector เดียวกัน ได้คะแนน 24–69% — ไม่ถึง threshold แต่ก็ไม่ใช่ศูนย์

**ผลคือ:** โทษของ false positive ตกกับคนกลุ่มเฉพาะ — non-native writers และคนที่ craft จัด ๆ — ในสถานการณ์ที่ไม่มีช่องอุทธรณ์

## Arms race กับ humanizers

พอ detector มีตลาด ก็เกิด product ฝั่งตรงข้าม: **humanizer** (undetectable.ai, QuillBot, StealthGPT) — วางข้อความ AI แล้วได้กลับมาแบบขัดจน detector ให้คะแนนเป็นคน detector ก็ retrain สู้ humanizer, humanizer ก็ retool สู้ detector สองตลาดนี้เลยต่างฝ่ายต่างเลี้ยงกันให้โต

## ปัญหาเชิง premise: ความต่างกำลังจางหายไป

Style detector ใช้ได้ต่อเมื่องานเขียน AI ยัง "หน้าตาไม่เหมือน" งานเขียนคน แต่ความต่างนั้นกำลังแคบลงจากทั้งสองฝั่ง:

1. Model ถูกเทรนให้เขียนเหมือนคน — นั่นคือ objective ตรง ๆ
2. คนดูดสไตล์ model กลับ — งาน Max Planck (วิเคราะห์ ~280,000 วิดีโอ YouTube) พบคำโปรดของ ChatGPT อย่าง *delve*, *meticulous*, *realm* โผล่ในการพูดของคนเพิ่มถึง 50% หลัง ChatGPT ออก โดยผู้พูดไม่รู้ตัว

> "A style detector is a snapshot of a difference, and the difference is dissolving."
> (style detector คือภาพนิ่งของความต่าง ณ เวลาหนึ่ง — และความต่างนั้นกำลังจางหายไป)

ตรงนี้คือเหตุผลที่ [[eu-ai-act|EU]] ผลัก watermark ฝั่ง provider แทนที่จะพึ่ง detector ฝั่งผู้ตรวจ — และเป็นอีกหน้าของ [[quality-proxy-collapse]]: ทั้ง "เขียนลื่น = คนตั้งใจ" และ "เขียนเรียบ = เครื่องเขียน" เป็น proxy ที่กำลังพังพร้อมกัน

## วิธีอ่านผล detector อย่างมีสติ

- คะแนน detector เป็นความน่าจะเป็นจากสไตล์ ไม่ใช่หลักฐาน provenance — ต่างจาก watermark ที่ยืนยันด้วย key ได้
- อย่าใช้เป็นเกณฑ์ลงโทษเดี่ยว ๆ โดยไม่มีหลักฐานอื่นและไม่มีช่องอุทธรณ์ (บทเรียน NeurIPS)
- ระวังเป็นพิเศษกับงานของ non-native writers และงานที่ขัดเยอะ
- ตัวเลขความแม่นล่าสุดส่วนใหญ่มาจาก vendor เอง — อ่านแบบ source-attributed

## See also

- [[claude-text-watermarking-squintist]]
- [[llm-text-watermarking]]
- [[pangram]]
- [[eu-ai-act]]
- [[quality-proxy-collapse]]
- [[ai-slop]]
