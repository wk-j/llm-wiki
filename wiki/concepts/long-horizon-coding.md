---
title: Long-Horizon Coding
type: concept
tags: [ai, coding, agents, benchmarks]
created: 2026-05-27
updated: 2026-05-27
sources: [Piyalitt Ittichaiwong - DeepSWE FrontierSWE Benchmark.md]
---

# Long-Horizon Coding / งาน coding ที่ยาวหลายขั้น

**Long-horizon coding** คืองาน software engineering ที่ต้องใช้หลายขั้นตอนและกินเวลานานกว่าการแก้ bug เล็กๆ — agent ต้องสำรวจ codebase เอง วางแผน แก้หลายไฟล์ และตรวจงานตัวเอง ไม่ใช่แค่เติม code ตามสเปกที่ระบุมาครบแล้ว เป็นมิติที่ benchmark รุ่นใหม่อย่าง [[deepswe|DeepSWE]] และ [[frontierswe|FrontierSWE]] ตั้งใจวัด

## ทำไมงานยาวถึงวัดยาก (และวัดได้คม)

benchmark เดิมอย่าง SWE-Bench เก็บโจทย์จาก pull request เล็ก-กลาง เฉลยเฉลี่ยแค่ราว 10–120 บรรทัด ซึ่งเล็กกว่างานจริงที่ developer ใช้ agent ทำทุกวันนี้มาก พอโจทย์เล็ก model หลายตัวก็ทำได้ใกล้กัน เลยดูสูสี แต่พองานยาวและเปิดกว้างขึ้น ความต่างเรื่องการวางแผน การจำข้อกำหนด และการไม่หลงทาง ก็เผยออกมา

ลักษณะเด่นของโจทย์ long-horizon:

- **prompt สั้น เฉลยใหญ่** — DeepSWE prompt สั้นกว่า SWE-Bench Pro ครึ่งหนึ่ง แต่เฉลยเพิ่ม code เฉลี่ย 668 บรรทัด แก้ 7 ไฟล์ (Pro: 120 บรรทัด / 5 ไฟล์)
- **ต้องสำรวจเอง** — prompt บอกแค่พฤติกรรมที่ต้องการ ไม่ยัด interface มาให้ agent ต้องไปค้นเองว่าจะแก้ตรงไหน
- **ultra-long-horizon** — FrontierSWE ดันไปสุด ให้เวลา 20 ชั่วโมง/โจทย์ (optimize compiler, สร้าง optimizer ฯลฯ) จนยัง **ไม่อิ่มตัว** เพราะ model ส่วนใหญ่ยังแทบไม่คืบ

## นิสัยที่งานยาวเผยให้เห็น

- Claude มักลืมข้อกำหนดเมื่อโจทย์มีหลายส่วน (ดู [[missed-requirement]])
- model ที่เก่งกว่าเขียน test เองโดยไม่ต้องสั่ง (Opus 4.7 / GPT-5.4 ทำ >80% ของการรันบน DeepSWE)
- ทรัพยากรที่ใช้ (token/เวลา/เงิน) ไม่สัมพันธ์กับ pass rate — รันนานกว่าไม่ได้แปลว่าทำได้มากกว่า

## ผลคือ

ยิ่งโจทย์ยาวและใกล้งานจริง ช่องว่างระหว่าง coding agent ยิ่งกว้างและตรงกับประสบการณ์ developer มากกว่าตาราง pass rate บนโจทย์สั้นๆ

## See also

- [[deepswe]]
- [[frontierswe]]
- [[missed-requirement]]
- [[long-running-agents]]
- [[agentic-engineering]]
