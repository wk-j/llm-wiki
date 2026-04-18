---
title: Harness Engineering
type: concept
tags: [ai, software-engineering, orchestration, education, curriculum]
created: 2026-04-18
updated: 2026-04-18
sources: [harness-engineering-panutat.md, llm-era-computer-engineering-nattee.md, alex-ker-harnesses-optimize.md]
---

# Harness Engineering

เมื่อ AI Agent เขียน code ได้ในระดับที่มนุษย์ "ตรวจ" หรือ "แนะนำ" ตามไม่ทัน สิ่งที่มนุษย์ควรสร้างคือ *harness* — ระบบของ AI Agent ตัวอื่น ๆ ที่ล้อมรอบ agent หลัก ทำหน้าที่ review, test, audit แบบอัตโนมัติ — เสนอโดย [[panutat-tejasen|Panutat Tejasen]] (2026-04-18)

> **หมายเหตุ**: คำว่า *harness* ในวงการ AI coding มีใช้สองแบบ หน้านี้เล่าแบบที่ Panutat หมายถึง — pipeline ของ review agent ถ้ามองหาความหมายแบบ [[alex-ker|Alex Ker]] / [[humanlayer|HumanLayer]] (ตัว tool อย่าง Claude Code / Cursor / Codex ที่ครอบ LLM) ดู [[coding-harness]]

## ปัญหาตั้งต้น

ข้อเสนอที่พบบ่อย: สอนนักศึกษาให้ "ตรวจงาน AI Agent" และ "แนะนำให้ AI เลือก Framework ที่ถูก" ฟังดูสมเหตุสมผล แต่ในทางปฏิบัติ:

- Framework / Library ที่ AI Agent เลือกใช้ **เกินความสามารถที่คนจะไปแนะนำ** — "มันรู้มากกว่าเรามาก" (คำของ Panutat)
- ถ้าพยายามแทรกแซงการเลือกของ agent ความเร็วที่ควรได้ **x10 จะกลายเป็น /100** เพราะคอขวดย้ายมาอยู่ที่คน
- งาน "แนะนำ" จึงให้ ROI ติดลบ — ยิ่งคนรู้น้อยกว่า agent ยิ่งไม่ควรไปขวาง

## สิ่งที่ควรสอนแทน

ออกแบบและควบคุม AI Agent หลายตัวให้ทำงานประกอบกัน — นั่นคือ **Harness Engineering**:

| บทบาทของ Agent | หน้าที่หลัก |
|---|---|
| Code Review Agent | ตรวจ code quality, naming, architectural fit |
| Inspection / Validation Agent | เทียบ output กับ spec / acceptance criteria |
| Test Case Generator | สร้าง unit test และ integration test |
| E2E Testing Agent | รัน scenario จริงจาก user perspective |
| Security Audit Agent | หาช่องโหว่ — OWASP, secret leak, supply-chain risk |

งานของมนุษย์ย้ายไปที่ **การออกแบบ harness** ไม่ใช่การไปแข่งกับ agent ตัวใน:

- เลือก agent ตัวไหนบ้างที่ต้องมีใน pipeline
- ออกแบบ prompt และ criteria ของแต่ละ agent
- วางลำดับการทำงาน (sequencing) และ handoff
- ตั้ง quality gate และจุดที่ต้องให้คนดูก่อน ship

## ทำไมแนวทางนี้เข้าท่า

- **Scale งาน downstream ด้วย agent ไม่ใช่คน.** [[engineering-role-shift]] ชี้ว่างาน review / verification คืองานที่ขยายตัวในยุค AI — Harness Engineering คือวิธี scale งานนั้นโดยไม่ติดคอขวดที่คน
- **ตรงกับ pattern agent-verify-agent อื่น ๆ.** เทียบได้กับ [[advisor-strategy]] (executor model เรียก advisor ที่จุดตัดสินใจยาก) แต่ harness แผ่ออกเป็น pipeline ถาวรที่มี agent หลายบทบาท ไม่ใช่การเรียกครั้งเดียว
- **แก้ blind spot ที่ [[llm-coding-pitfalls]] อธิบาย.** Karpathy ชี้ว่า AI เขียน code "ดูมั่นใจแต่ผิดเงียบ ๆ" — harness คือการทำให้การจับ failure mode เหล่านั้นเป็นระบบ
- **สอดคล้องกับ [[ai-orchestrator]].** วิศวกรยุคใหม่คือคนออกแบบ pipeline ของ agent หลายตัว ไม่ใช่ coder เดี่ยว
- **เคารพ [[judgement-vs-automation]].** ออกแบบ harness คืองานที่ต้องใช้วิจารณญาณและคาดเดาไม่ได้ — ยังเป็นพื้นที่ของคน ในขณะที่ coding ที่คาดเดาได้ถูก automate ไปให้ agent

## นัยทางหลักสูตร

- **อย่าสอนให้นักศึกษา "แข่ง" กับ AI Agent** ในเรื่องเลือก library หรือตรวจ code ด้วยตาเปล่า — ไล่ไม่ทัน และฝึกแล้วไม่ scale
- **สอน design skills ของ harness** — prompt engineering สำหรับ agent แต่ละบทบาท, criteria ของ security audit agent, การต่อ agent หลายตัวเป็น pipeline ที่เชื่อถือได้
- **ย้ายสกิลหลัก** จาก "เขียน code ให้ถูก" ไปที่ "ออกแบบระบบตรวจ-สอบที่ไว้ใจได้"

## ดูควบคู่กับ [[taste-paradox]] — สองปัญหาคนละ layer

Harness Engineering (Panutat) และ [[taste-paradox]] (Nattee) พูดถึงปัญหาเดียวกัน — การ review งาน Agent แบบ manual ทำไม่ไหว — แต่มองจากคนละจุด:

- **Panutat = *scope of reviewability*.** คนรู้น้อยกว่า Agent ไปแล้ว ตรวจ library choice ไม่ทัน → ตอบด้วย agent harness (แทนแรงคนด้วย agent ตัวอื่น)
- **Nattee = *origin of the reviewer*.** ต่อให้มี harness ก็ยังต้องมีคน *ออกแบบ* harness — คนนั้นต้องมี taste — taste มาจากการฝึกมือ — Agent ทำให้ข้ามการฝึกมือได้ จะปิด loop นี้ยังไง?

ไม่ได้ขัดกัน — harness ตอบคำถาม *"ตรวจยังไงให้ scale"* (technology); taste paradox ถามต่อว่า *"แล้วคนที่มี taste พอไปออกแบบ harness จะปั้นขึ้นมาจากไหน"* (pedagogy). ทั้งสองชิ้นต้องตอบไปพร้อมกันในหลักสูตรยุค Agent

## เชื่อมกับ [[subagent-patterns]] ของ Alex Ker

[[alex-ker|Alex Ker]] (2026-04-18) สรุป "pipeline" subagent pattern ไว้ว่า — push งานหนึ่งผ่าน role หลาย ๆ อันเป็นลำดับ (UX designer → architect → devil's advocate) **pattern นี้คือ pattern เดียวกันที่ Panutat เสนอ** เพียงแต่:

- Alex Ker เสนอในแง่ *เทคนิคการใช้งาน harness รายวัน* (ดูใน [[coding-harness]])
- Panutat เสนอในแง่ *สิ่งที่ curriculum ควรสอนแทนการตรวจ code ด้วยตา*

คน ๆ เดียวกันใช้ pattern นี้ได้ทั้งสองบริบท — เครื่องมือในการทำงาน และหัวข้อที่ต้องสอน

## ข้อสังเกตเพิ่มเติม (wiki)

ส่วนนี้เป็นการต่อยอดจากฝั่ง wiki ไม่ได้อยู่ในโพสต์ต้นทางของ Panutat:

- Harness มี cost ของตัวเอง — token, latency, agent-coordination bug ทั้ง pipeline อาจ fail พร้อมกันได้หาก agent base model เหมือนกัน
- ประเด็นเปิด: ควรใช้ model ต่างชนิดใน harness เพื่อ diversity ของ failure mode หรือไม่?
- ยังไม่มี tooling มาตรฐานสำหรับ harness orchestration — ยังเป็นพื้นที่ที่กำลังก่อตัว
- ประเด็นเปิด (จาก taste paradox): ถ้า junior เรียน debugging ผ่าน *output ของ harness* ตลอด จะเกิด taste เองหรือแค่ไว้ใจ harness?

## See also

- [[panutat-tejasen]]
- [[harness-engineering-panutat]]
- [[taste-paradox]]
- [[nattee-niparnan]]
- [[llm-era-computer-engineering-nattee]]
- [[coding-harness]]
- [[subagent-patterns]]
- [[alex-ker]]
- [[alex-ker-harnesses-optimize]]
- [[ai-orchestrator]]
- [[engineering-role-shift]]
- [[advisor-strategy]]
- [[llm-coding-pitfalls]]
- [[judgement-vs-automation]]
