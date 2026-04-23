---
title: Instruction Budget
type: concept
tags: [ai, llm, prompt-engineering, attention, harness]
created: 2026-04-18
updated: 2026-04-23
sources: [alex-ker-harnesses-optimize.md]
---

# Instruction Budget / งบคำสั่งของ LLM

**Instruction budget** คือเพดานของจำนวน *คำสั่ง / กฎ / rule* ที่ frontier LLM สามารถปฏิบัติตามได้ในเวลาเดียวกัน เมื่อเกินเพดานนี้ — ซึ่ง Kyle จาก [[humanlayer|HumanLayer]] เรียกว่า **"dumb zone"** — model จะเริ่มพลาดคำสั่งที่ควรทำตามและเกิด hallucination

ตัวเลขคร่าวๆ ที่ [[alex-ker|Alex Ker]] อ้างถึงคือ "a few hundred instructions" ก่อนที่จะเข้าสู่ dumb zone

## แตกต่างจาก [[context-rot]] อย่างไร

ทั้งสองเรื่องนี้มีอาการคล้ายกันคือ model จะดูไม่ฉลาด แต่มีตัวแปรที่แตกต่างกัน ซึ่งต้องแยกแยะให้ชัดเจน:

| | Instruction budget | [[context-rot\|Context rot]] |
|---|---|---|
| **ตัวแปร** | **จำนวนคำสั่ง / rule** ที่ต้องทำตามพร้อมกัน | **จำนวน token ทั้งหมด** ใน context |
| **กลไก** | attention ต้องถูกแบ่งไปตามแต่ละกฎ | attention ต้องถูกแบ่งไปตามทุก token |
| **อาการ** | model ลืมทำตามกฎ, hallucinate rule ที่ไม่มีอยู่จริง | model คิดช้า, ลืม fact เก่า, drift |
| **วิธีแก้** | [[progressive-disclosure]], ทำให้ CLAUDE.md สั้นลง | [[compaction]], subagent, เริ่ม session ใหม่ |

ในทางกลไก ทั้งสองปัญหานี้เกิดจาก attention ที่มีจำกัด — แต่ต้องแก้ไขคนละจุด หาก CLAUDE.md มีความยาว 300 บรรทัด แต่ total token ยังคงอยู่ที่ 50k นั่นคือปัญหา instruction budget ไม่ใช่ context rot

## ทำไม "การกำหนด if-else ทุกกรณี" ถึงไม่ได้ผล

สัญชาตญาณของวิศวกรคือการ front-load ทุกอย่างที่ model อาจต้องใช้ — โดยการเขียน `if ... else ...` อย่างละเอียดใน CLAUDE.md แต่ Alex Ker ชี้ว่าการทำเช่นนี้:

-   กิน attention budget — ทำให้ reasoning window เหลือน้อยลง
-   Model เริ่มพลาดกฎที่เขียนไว้ท่ามกลางกฎอื่นๆ — "เยอะจนลืม"
-   การให้ instruction มากเกินไปจะกระตุ้นให้ model เกิด hallucination

## คำแนะนำ (จากแหล่งข้อมูลเดียวกัน)

-   **CLAUDE.md / AGENTS.md ควรเขียนโดยคน ไม่ใช่ LLM generate** — งานวิจัยของ ETH ที่ Alex Ker อ้างถึงชี้ว่า LLM-generated prompt ทำให้ performance แย่ลงและใช้ inference เพิ่มขึ้น ~20%
-   **เขียน minimal requirements** — ระบุว่าโปรเจกต์คืออะไร, user คือใคร ทุก token ในไฟล์มีความสำคัญ
-   **อย่าใส่ rule ที่เป็น behavioral detail** ลงในไฟล์หลัก — ให้ย้ายไปไว้ในไฟล์ skill แยก แล้วใช้ [[progressive-disclosure]] เพื่อดึงมาใช้เมื่อจำเป็น
-   **ใช้คำอธิบาย skill/MCP tool ที่ชัดเจนและมี keyword-rich** — เพื่อให้ model สามารถค้นหาเครื่องมือเจอได้เร็วโดยไม่ต้อง load body ทั้งหมด

## ความเชื่อมโยงกับประเด็นอื่น

-   [[claude-md]] — CLAUDE.md คือที่ที่ instruction budget ถูกใช้เปลืองที่สุด; [[cyril-xbt|Cyril]] สนับสนุน template 7 ส่วนเต็ม, ในขณะที่ Alex Ker สนับสนุน minimal — อ่านตารางเปรียบเทียบใน `[[claude-md]]`
-   [[progressive-disclosure]] — เป็นเทคนิคหลักในการ *อยู่ภายใต้* instruction budget โดยไม่สูญเสียความสามารถในการครอบคลุม rule
-   [[coding-harness]] — harness ที่ดีจะถูกออกแบบมาเพื่อไม่ให้ instruction budget ถูกใช้ไปอย่างเปล่าประโยชน์
-   [[llm-coding-pitfalls]] — Karpathy ชี้ว่าหลายๆ pitfall ของ AI เกิดจากการไม่รู้ว่า model กำลังอยู่ในโหมด confident-but-wrong — instruction budget เป็นกลไกหนึ่งที่ทำให้เกิดปัญหานี้
-   [[claude-code-session-management]] — การ rewind / compact คือการ cleanup เพื่อให้ budget กลับมา

## ดูเพิ่มเติม

- [[claude-md]]
- [[humanlayer]]
- [[alex-ker]]
- [[alex-ker-harnesses-optimize]]
- [[cyril-xbt-claude-md-guide]]
- [[progressive-disclosure]]
- [[coding-harness]]
- [[context-rot]]
- [[compaction]]
- [[llm-coding-pitfalls]]
