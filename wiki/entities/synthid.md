---
title: SynthID
type: entity
tags: [ai, watermarking, google, provenance, tools]
created: 2026-08-16
updated: 2026-08-16
sources: [claude-text-watermarking-squintist.md]
---

# SynthID

เทคโนโลยี watermark เนื้อหา AI ของ [[google-deepmind|Google DeepMind]] ครอบคลุมทั้งรูปภาพ วิดีโอ และ **ข้อความ** ใน wiki นี้โฟกัสที่ SynthID Text ซึ่งเป็นตัวอย่างสาธารณะที่ชัดที่สุดของ [[llm-text-watermarking|LLM text watermarking]]: ฝัง signal ตอน model เลือกคำ (sampling) ไม่ใช่ stamp ใส่ไฟล์ทีหลัง

## กลไกโดยย่อ

ใช้ **tournament sampling** — ตอน model จะเลือกคำถัดไป ให้คำ candidate แข่งกันแบบแพ้คัดออก ผู้ชนะตัดสินด้วยคะแนนลับจาก secret key ผสมกับคำไม่กี่คำก่อนหน้า key เลย reshuffle ทุก step ทำให้สถิติคำระยะยาวไม่เปลี่ยนและข้อความอ่านปกติ ส่วน detector ที่ถือ key เดียวกันไล่ redo คะแนนทีละคำแล้วดูว่าสูงกว่าโอกาสสุ่มไหม (รายละเอียดเต็มที่ [[llm-text-watermarking]])

## หลักฐานที่ตีพิมพ์

- **Nature paper** (Scalable watermarking for identifying large language model outputs) — รวมการทดลอง live ใน Gemini ราว **20 ล้าน response**: ครึ่งติด watermark ครึ่งไม่ติด อัตรา thumbs-up ต่างกัน 0.01% (ถือว่าไม่ต่าง) ช้าลง ~0.5% — ผู้ใช้แยกไม่ออก
- **Open-source reference implementation** — repo `google-deepmind/synthid-text` เปิดให้ใครก็สร้างเวอร์ชันเล็กมาทดสอบได้ ซึ่งเป็นดาบสองคม: งาน preprint กรกฎาคม 2026 ใช้ implementation สาธารณะ (MarkLLM บน Gemma-2-9B) แสดงว่า paraphrase ลบ detection ได้ 58/59 เคส — เป็นผลบน "home version" ไม่ใช่ detector production ของ Google
- **Developer docs** — ระบุ detection states และ thresholds

## บริบทใน wiki

- [[anthropic|Anthropic]] ประกาศ watermark ข้อความ Claude (สิงหาคม 2026) แต่ไม่เปิดกลไก — [[claude-text-watermarking-squintist|Squintist]] อนุมานว่าน่าจะเป็น sampling-time watermark ตระกูลเดียวกับ SynthID
- [[openai|OpenAI]] ใช้ C2PA + SynthID กับ**รูปภาพ**ที่ generate แล้ว ส่วน text provenance ยังเป็นแผน
- แรงขับเชิงกฎหมายมาจาก [[eu-ai-act|EU AI Act]] Article 50 และ Code of Practice ที่ Google ร่วมลงนาม

## See also

- [[llm-text-watermarking]]
- [[google-deepmind]]
- [[claude-text-watermarking-squintist]]
- [[eu-ai-act]]
- [[ai-text-detectors]]
