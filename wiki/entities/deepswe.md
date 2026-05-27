---
title: DeepSWE
type: entity
tags: [ai, benchmarks, coding, agents]
created: 2026-05-27
updated: 2026-05-27
sources: [Piyalitt Ittichaiwong - DeepSWE FrontierSWE Benchmark.md]
---

# DeepSWE

benchmark วัดความสามารถของ AI coding agent ในงาน software engineering แบบ **long-horizon** (งานหลายขั้นตอนกินเวลานาน — ดู [[long-horizon-coding]]) สร้างโดยทีม [[datacurve|Datacurve]] เป้าหมายคือทำให้ความต่างที่ developer สัมผัสได้จริง แต่มองไม่เห็นบน benchmark สาธารณะเดิม ปรากฏออกมาเป็นตัวเลข

## ทำไมถึงสร้างขึ้นมา

ปัญหาของ benchmark สาธารณะเดิม (SWE-Bench Pro, SWE-Bench Verified) คือหลาย model ได้คะแนนใกล้กันจนแยกไม่ออก แต่พอใช้งานจริงกลับต่างชัด DeepSWE แก้จุดอ่อนนี้ด้วยการออกแบบ 4 อย่างพร้อมกัน:

1. **ปลอดการปนเปื้อน** — ทุกโจทย์เขียนใหม่หมด ไม่ดัดแปลงจาก commit/PR เดิม และไม่เคย merge กลับ repo ต้นทาง จึงไม่หลุดเข้า pre-training corpus (ดู [[benchmark-contamination]])
2. **หลากหลาย** — 113 โจทย์ ใน 91 repository, 5 ภาษา; repo ส่วนใหญ่มีโจทย์เดียว ไม่มี repo ไหนครอบงำคะแนน
3. **ซับซ้อนแบบงานจริง** — prompt สั้น เฉลยใหญ่
4. **verifier ตรวจพฤติกรรม** ไม่ใช่วิธีเขียน code (ดู [[behavioral-verifier]])

## โครงสร้างโจทย์

- 113 โจทย์ / 91 repository / 5 ภาษา: TypeScript 31%, Go 30%, Python 30%, JavaScript 4%, Rust 4% (ยังไม่มี C++, Java)
- prompt เฉลี่ย 2,158 ตัวอักษร (สั้นกว่า SWE-Bench Pro ที่ 4,614)
- เฉลยเพิ่ม code เฉลี่ย 668 บรรทัด แก้ 7 ไฟล์ (Pro: 120 บรรทัด / 5 ไฟล์; Verified: 10 บรรทัด / 1 ไฟล์)
- prompt บอกพฤติกรรมที่ต้องการสั้นๆ ไม่ยัด interface มาให้ agent ต้องสำรวจ codebase เองว่าจะแก้ตรงไหน

## ความแม่นของ verifier

วัดโดยให้ LLM อ่าน trajectory ตัดสินอิสระเทียบกับ verifier:

| | SWE-Bench Pro | DeepSWE |
|---|---|---|
| ผลบวกปลอม | 8.5% | 0.3% |
| ผลลบปลอม | 24.0% | 1.1% |
| LLM เห็นต่างจาก verifier | 32% | 1.4% |

## อันดับ (รันบน [[mini-swe-agent]], margin ~2–5%)

[[gpt-5-5|gpt-5.5]] 70% > gpt-5.4 56% > [[claude-opus-4-7|claude-opus-4.7]] 54% > claude-sonnet-4.6 32% > gemini-3.5-flash 28% > gpt-5.4-mini 24% / [[kimi-k2-6|kimi-k2.6]] 24% > mimo-v2.5-pro 19% > glm-5.1 18% > gemini-3.1-pro 10% > deepseek-v4-pro 8% > gemini-3-flash 5%

ช่วงคะแนนกว้าง 70% (เทียบกับ SWE-Bench Pro ที่ห่างกันแค่ 30%) สะท้อนความต่างจริงได้คมกว่า

## ข้อจำกัด

แยก model จาก harness ได้ด้วย [[mini-swe-agent]] แต่ลดความสมจริง; corpus เอาจาก repo ดาว ≥ 500 เท่านั้น; งาน bug localization / refactoring มีสัดส่วนน้อย

## See also

- [[frontierswe]] — benchmark อิสระที่ให้ภาพเดียวกัน
- [[datacurve]]
- [[mini-swe-agent]]
- [[benchmark-contamination]]
- [[behavioral-verifier]]
- [[reward-hacking]]
- [[long-horizon-coding]]
- [[piyalitt-deepswe-benchmark]]
