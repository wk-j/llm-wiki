---
title: Instruction Budget
type: concept
tags: [ai, llm, prompt-engineering, attention, harness]
created: 2026-04-18
updated: 2026-04-18
sources: [alex-ker-harnesses-optimize.md]
---

# Instruction Budget / งบคำสั่งของ LLM

**Instruction budget** คือเพดานของจำนวน *คำสั่ง / กฎ / rule* ที่ frontier LLM ทำตามได้ในเวลาเดียวกัน เลยเพดานนี้ — ซึ่ง Kyle จาก [[humanlayer|HumanLayer]] เรียกว่า **"dumb zone"** — model เริ่ม miss คำสั่งที่ควรทำตาม และเริ่ม hallucinate

ตัวเลขคร่าว ๆ ที่ [[alex-ker|Alex Ker]] อ้างคือ "a few hundred instructions" ก่อนเข้า dumb zone

## ต่างจาก [[context-rot]] ยังไง

สองเรื่องเหมือนกันตรงที่ model เริ่มดูไม่ฉลาด แต่คนละตัวแปร — ต้องแยกให้ขาด:

| | Instruction budget | [[context-rot\|Context rot]] |
|---|---|---|
| ตัวแปร | **จำนวนคำสั่ง / rule** ที่ต้องทำตามพร้อมกัน | **จำนวน token รวม** ใน context |
| กลไก | attention ต้องหารไปตามกฎแต่ละข้อ | attention ต้องหารไปตาม token ทุกตัว |
| อาการ | model ลืมทำตามกฎ, hallucinate rule ที่ไม่มี | model คิดช้า, ลืม fact เก่า, drift |
| แก้ด้วย | [[progressive-disclosure]], CLAUDE.md สั้น | [[compaction]], subagent, session ใหม่ |

ในทาง mechanism ทั้งสองมาจาก attention ที่จำกัด — แต่แก้คนละจุด ถ้า CLAUDE.md ยาว 300 บรรทัดแต่ total token ยังแค่ 50k นั่นคือ instruction budget ไม่ใช่ context rot

## ทำไม "prescribe if-else ทุก case" ถึงไม่ work

สัญชาตญาณของ engineer คือ front-load ทุกอย่างที่ model อาจต้องใช้ — เขียน `if ... else ...` เป็นรายละเอียดยิบ ๆ ใน CLAUDE.md Alex Ker ชี้ว่าการทำแบบนี้:

- กิน attention budget — ตัว reasoning window เหลือน้อยลง
- Model เริ่ม miss กฎที่เขียนไว้ท่ามกลางกฎอื่น — "เยอะจนลืม"
- ให้ instruction มากเกิน functionally encourage model ให้ hallucinate

## คำแนะนำ (จากแหล่งเดียวกัน)

- **CLAUDE.md / AGENTS.md ให้คนเขียน ไม่ใช่ LLM generate** — ETH research ที่ Alex Ker อ้างชี้ว่า LLM-generated prompt ทำ performance แย่ลง และกิน inference ~20% มากกว่า
- **เขียน minimal requirements** — โปรเจกต์คืออะไร, user คือใคร ทุก token ต้องสู้ที่ในไฟล์
- **อย่าใส่ rule ที่เป็น behavioral detail** ลงไฟล์หลัก — ย้ายไปไฟล์ skill แยก แล้วใช้ [[progressive-disclosure]] pull มาเมื่อจำเป็น
- **ใช้คำอธิบาย skill/MCP tool ที่ชัดและ keyword-rich** — เวลา model search หาเครื่องมือ จะได้เจอได้เร็วโดยไม่ต้อง load body เต็ม

## เชื่อมกับประเด็นอื่น

- [[progressive-disclosure]] — เทคนิคหลักในการ *อยู่ใต้* instruction budget โดยไม่เสียความสามารถในการครอบ rule
- [[coding-harness]] — harness ที่ดีออกแบบให้ instruction budget ไม่ถูกใช้สุ่มสี่สุ่มห้า
- [[llm-coding-pitfalls]] — Karpathy ชี้ว่า AI หลาย pitfall มาจากการไม่รู้ว่า model ตอนนั้นอยู่ในโหมด confident-but-wrong อยู่ — instruction budget เป็นกลไกหนึ่งที่ทำให้เกิด
- [[claude-code-session-management]] — การ rewind / compact คือการไล่ cleanup ให้ budget กลับมา

## See also

- [[humanlayer]]
- [[alex-ker]]
- [[alex-ker-harnesses-optimize]]
- [[progressive-disclosure]]
- [[coding-harness]]
- [[context-rot]]
- [[compaction]]
- [[llm-coding-pitfalls]]
