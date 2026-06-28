---
title: Behavioral Verifier
type: concept
tags: [ai, benchmarks, evaluation, testing, coding]
created: 2026-05-27
updated: 2026-06-16
sources: [Piyalitt Ittichaiwong - DeepSWE FrontierSWE Benchmark.md, Agentic Code Review.md]
---

# Behavioral Verifier / verifier ที่ตรวจพฤติกรรม

**Behavioral verifier** คือตัวตรวจคำตอบของ benchmark ที่ตัดสินว่า code ที่ agent ส่งมา *ทำพฤติกรรมตามที่โจทย์ขอหรือไม่* โดยไม่ผูกกับวิธีเขียนแบบใดแบบหนึ่ง — ยอมรับทุกวิธีแก้ที่ให้ผลลัพธ์ถูกต้อง ตรงข้ามกับ verifier ที่ผูกกับ implementation เฉพาะ (เช่น ต้องมีฟังก์ชันชื่อนี้ ต้องแก้ไฟล์นี้)

## ทำไมถึงสำคัญ

benchmark จะดีได้แค่ไหนขึ้นกับ verifier ของมัน ถ้า verifier ผูกกับวิธีเขียน มันจะ:

- **ตีตกคำตอบที่ถูก** เพราะ agent เขียนคนละแบบกับเฉลย (ผลลบปลอม / false negative)
- **ปล่อยคำตอบที่ผิด** เพราะบังเอิญตรง pattern ที่ตรวจ (ผลบวกปลอม / false positive)

[[deepswe|DeepSWE]] เขียน verifier จากคำอธิบายโจทย์โดยตรง ทดสอบพฤติกรรมของ software แทนรายละเอียดวิธีเขียน

## ตัวเลขที่พิสูจน์ว่าต่างกันจริง

ทีมงานให้ LLM อ่าน trajectory แล้วตัดสินอิสระเทียบกับ verifier (สุ่ม 30 โจทย์ รัน 3 ครั้ง, 10 config):

| | SWE-Bench Pro | DeepSWE |
|---|---|---|
| ผลบวกปลอม | 8.5% | 0.3% |
| ผลลบปลอม | 24.0% | 1.1% |
| LLM เห็นต่างจาก verifier | 32% | 1.4% |

เกือบหนึ่งในสามของผลตัดสินบน SWE-Bench Pro ดูผิดในสายตาคนที่อ่าน trajectory เดียวกัน ส่วน DeepSWE แทบไม่มีข้อโต้แย้ง

## เชื่อมกับ verifiability

verifier ที่ตรวจพฤติกรรมคือการทำให้งาน coding "ตรวจสอบได้" อย่างถูกต้อง (ดู [[verifiability]]) ถ้า reward function ของ benchmark หละหลวม คะแนนก็เชื่อไม่ได้ และยังเปิดช่องให้ model เรียนรู้ที่จะ [[reward-hacking|เลี่ยง verifier]] แทนที่จะแก้โจทย์จริง

ในงานจริง [[agentic-code-review]] ใช้หลักเดียวกันแต่เปลี่ยนจาก benchmark เป็น PR: test, CI, mutation testing, และ review gate ต้องตรวจพฤติกรรมที่ต้องการ ไม่ใช่แค่เปิดทางให้ diff ดูถูกใจ. ถ้า agent แก้ test ให้ยอมรับ behavior ใหม่ที่ผิด verifier ก็กลายเป็นส่วนหนึ่งของปัญหา

## ผลคือ

verifier ที่แม่นทำให้คะแนนน่าเชื่อ และเป็นเงื่อนไขจำเป็นที่ทำให้ช่องว่างระหว่าง model สะท้อนความสามารถจริง ไม่ใช่ noise จากการตรวจ

## See also

- [[deepswe]]
- [[benchmark-contamination]]
- [[reward-hacking]]
- [[verifiability]]
- [[facts-first]] — หลักเดียวกันในงาน dev จริง: เก็บความต้องการเป็น assertion ที่ตรวจพฤติกรรม ไม่ผูกกับวิธีเขียน
- [[property-based-testing]] — เทคนิคเขียน test ที่ตรวจพฤติกรรมโดยธรรมชาติ
- [[agentic-code-review]]
