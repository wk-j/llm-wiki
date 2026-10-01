---
title: Quality Proxy Collapse
type: concept
tags: [ai, software-quality, slop, verification]
created: 2026-07-03
updated: 2026-09-24
sources: [eternal-sloptember.md, claude-text-watermarking-squintist.md, teepagorn-claude-code-adoption-nobody-reading.md]
---

# Quality Proxy Collapse / สัญญาณคุณภาพเดิมใช้ไม่ได้

Quality Proxy Collapse คือภาวะที่สัญญาณผิว ๆ ที่เคยพอใช้เดาคุณภาพ artifact ได้ เช่น syntax ถูก, grammar ดี, structure ดูเป็นมืออาชีพ, test บางชุดผ่าน กลับวัดคุณภาพจริงได้น้อยลง เพราะ AI สร้างรูปทรงของงานมนุษย์ได้เก่งขึ้น

## ทำไมเกิดกับ LLM artifacts

ใน [[eternal-sloptember|The Eternal Sloptember]] ผู้เขียนบอกว่าคนเห็น artifact แล้วมักเดาว่ามี process แบบมนุษย์อยู่ข้างหลัง. ถ้า code อ่านเหมือนคนเขียน เราจะเผลอคิดว่ามีคนเข้าใจระบบก่อนเขียน

LLM ทำให้ assumption นี้พัง. งานอาจดูดีตามสถิติ แต่ไม่ได้มาจาก process ที่เข้าใจ constraint จริง. ความเสียหายจึงไม่ได้อยู่ตรง “syntax พัง” แบบยุคก่อน แต่อยู่ตรง “หน้าตาถูกแต่ build ต่อแล้วเจอรอยร้าว”

## ตัวอย่างใน code

- code compile ได้ แต่ abstraction ไม่ตรง domain
- test ผ่าน เพราะ agent เลี่ยงหรืออ่อน test แทนที่จะแก้ behavior
- API ดูมีโครงสร้าง แต่ edge case และ failure mode ไม่ถูกคิด
- prose ใน PR ดูมั่นใจ แต่ reviewer ยังต้องตรวจทุกบรรทัด

ได้อะไร: ต้องเลิกใช้ความเรียบร้อยของ output เป็นหลักฐานว่า process ข้างหลังดี

## ฝั่ง prose: สัญญาณพังทั้งสองทิศ

[[claude-text-watermarking-squintist|วิดีโอของ Squintist]] เติมมุมงานเขียนทั่วไป (ไม่ใช่แค่ code): เมื่อก่อน prose ที่ลื่นเป็นสัญญาณว่ามีคนลงเวลาขัด ตอนนี้ model ผลิตประโยคสะอาดได้ในไม่กี่วินาที shortcut นั้นหายไป

ที่แย่กว่านั้น proxy ฝั่งกลับก็พังด้วย: [[ai-text-detectors|AI detector]] ที่เดาจากสไตล์ อาศัยว่างานเขียน AI ยัง "หน้าตาไม่เหมือน" งานคน แต่ความต่างนั้นกำลังแคบลงจากทั้งสองฝั่ง — model ถูกเทรนให้เหมือนคน และคนก็ดูดสไตล์ model กลับ (คำอย่าง *delve* โผล่ในการพูดของคนเพิ่มถึง 50% หลัง ChatGPT ออก) เคสอาจารย์ที่ขัดเรื่องสั้นหกเดือนแล้วโดนตัดสิน 100% AI คือลูกหลงของ proxy ที่พัง

ทางที่วงการลองแทนคือ [[llm-text-watermarking|watermark]]: เลิกเดาจากผิวงาน แล้วฝังหลักฐาน provenance ที่ตรวจด้วย key ได้จริง — แต่มันตอบแค่ "ผ่าน model ไหม" ไม่ตอบว่าเนื้อหาดีหรือจริง

## วิธีรับมือ

ทางแก้ไม่ใช่ “อย่าใช้ AI” เสมอไป แต่ต้องเปลี่ยน proxy:

- ใช้ [[behavioral-verifier|behavioral verifier]] แทนการดู implementation อย่างเดียว
- ใช้ [[property-based-testing|property-based testing]] และ fuzzing กับพื้นที่ที่ทำได้
- จำกัด scope ให้เล็กพอที่คนอ่านทัน
- บังคับให้ agent แสดง evidence ไม่ใช่แค่สรุปว่าเสร็จ
- ดู process trace และ decision rationale ไม่ใช่แค่ final artifact

## เคส: test, docs และสรุปครบ แต่ incident ตามมา

[[teepagorn-claude-code-adoption-nobody-reading|โพสต์ของ @teepagorn]] ยกตัวอย่างตรงตัว งานจาก AI มีเหตุผล มี test มี documentation มีสรุปให้ ผู้เขียนเห็นว่าครบเลย approve แล้วเจอ incident สามวันต่อมา สัญญาณ "ครบ" ที่เคยบอกว่าคนตั้งใจทำ กลายเป็นของที่ AI สร้างได้ฟรีไปพร้อมกับ code

**ได้อะไร:** checklist แบบ "มี test มี docs" ไม่พอ ต้องถามว่า test มาจากแหล่งที่แยกจาก code หรือเปล่า

## See also

- [[ai-slop]]
- [[vibecoded-slop]]
- [[cognitive-surrender]]
- [[behavioral-verifier]]
- [[programming-process-matters]]
- [[llm-text-watermarking]]
- [[ai-text-detectors]]
- [[teepagorn-claude-code-adoption-nobody-reading]]
