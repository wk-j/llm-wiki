---
title: Piyalitt Ittichaiwong
type: entity
tags: [people, thai, ai, medical, phd]
created: 2026-04-24
updated: 2026-05-27
sources: [Piyalitt Ittichaiwong - GPT-5.5 Launch.md, Piyalitt Ittichaiwong - DeepSWE FrontierSWE Benchmark.md]
---

# Piyalitt Ittichaiwong

นักวิจัยสาย AI + การแพทย์ชาวไทย ระดับ PhD ที่เขียนโปรแกรมมา 20 ปี เป็นคนเขียน content ภาษาไทยเกี่ยวกับโมเดลรุ่นใหม่ๆ บน Facebook อย่างสม่ำเสมอ — โดยเฉพาะในมุมของ **early-access tester** ที่ได้ลองรุ่นเต็มก่อน launch และ framing ในบริบท **Thai developer community**

## ทำไมถึงน่าฟัง

- เป็นหนึ่งในไม่กี่คนในไทยที่ได้เข้าถึง frontier models ก่อนเปิดตัวทั่วไป — มีมุมมองจากการ *ใช้งานจริงในงาน PhD ด้านการแพทย์* ไม่ใช่แค่อ่าน model card
- **Connect-the-dots** ระหว่างความสามารถ coding ของโมเดลกับงานการแพทย์ — framing ที่ขาดในหลายๆ launch review
- เป็นผู้ดูแล/โปรโมทคอมมิวนิตี้ **OpenAI Codex Community** ในไทย และเป็นหนึ่งในทีมเปิดตัว Hackathon OpenAI × สมาคมปัญญาประดิษฐ์ประเทศไทย (credit รวมเป็นล้าน, เสาร์ 2026-04-25)

## มุมมองที่ชัดเจน

- ใน post เปิดตัว [[gpt-5-5|GPT-5.5]] เขาเขียนว่าเป็น "Model แรกที่ทำให้รู้สึกว่า 20 ปี สู้มันไม่ได้จริงๆ" — งาน PhD "แทบจะจบใน 1 prompt" ถ้ารอได้
- ระบุว่า GPT-5.5 เก่งใกล้ [[claude-mythos-preview|Claude Mythos Preview]] มาก — แต่*เปิดให้ทุกคนเข้าถึงได้* ต่างจาก Mythos ที่ถูก gate ผ่าน [[project-glasswing|Project Glasswing]]
- ฟ้อง **SWE-Bench Pro memorization sign** ใน GPT-5.5 card ตรงกับที่ Anthropic เคย flag ใน Mythos — ตีความว่าเป็นความพลาด ไม่ใช่การ benchmaxx ตั้งใจ
- **Prompt management** จะยิ่งสำคัญเมื่อราคา GPT-5.5 แพงขึ้น 2 เท่าจาก GPT-5.4

- ใน post เรื่อง benchmark เขาวางตัวเป็น "ที่พึ่งทางความจริง" ให้คอมมิวนิตี้ — เบื่อการเถียงกันด้วย benchmark สาธารณะ (เช่น "Gemini 3.5 Flash ดีบน benchmark" หรือ "Opus เก่ง backend กว่า GPT ตาม lmarena" ทั้งที่ lmarena ดู frontend เป็นหลัก) เลยชี้ไปที่ [[deepswe|DeepSWE]] + [[frontierswe|FrontierSWE]] ที่ออกแบบให้ใกล้งานจริง ว่าสะท้อนความต่างได้ดีกว่า
- จุดยืนสอดคล้องกันสองโพสต์: GPT-5.5 นำชัดในงาน coding จริง ตามด้วย Opus 4.7 แล้วค่อยห่างลงมา

## โพสต์ที่ ingest

- **[[piyalitt-gpt-5-5-launch]]** (2026-04-23) — layered commentary ว่า subjective reaction + OpenAI launch summary ภาษาไทย
- **[[piyalitt-deepswe-benchmark]]** (2026-05-27) — สรุป benchmark DeepSWE + FrontierSWE เพื่อตอบคำถาม "เขียนโปรแกรมใช้ AI ตัวไหนดี"; เน้นว่า benchmark ที่ปลอดการปนเปื้อนและ verifier ที่ตรวจพฤติกรรมเผยช่องว่างจริงของ model

## ดูเพิ่ม

- [[openai]]
- [[gpt-5-5]]
- [[claude-mythos-preview]]
- [[deepswe]]
- [[frontierswe]]
