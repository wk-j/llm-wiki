---
title: "Zoran Horvat on Claude Having No Planning Engine"
type: source
tags: [claude, planning, llm, coding-agents, harness, judgment]
url: https://x.com/zoranh75/status/2063146369934651469
created: 2026-07-02
updated: 2026-07-02
sources: ["Zoran Horvat on X — Claude has no planning engine.md"]
---

# Zoran Horvat on Claude Having No Planning Engine / Claude ไม่มี planning engine

โพสต์ X ของ [[zoran-horvat|Zoran Horvat]] โจมตีความเข้าใจผิดเรื่อง Plan mode ใน [[claude-code|Claude Code]]. เขาไม่ได้บอกว่า plan ไม่มีประโยชน์. เขาบอกว่า plan ที่ดูฉลาดไม่ควรถูกอ่านเป็น proof ว่า Claude มี planner จริงหรือมี engineering judgment.

ประโยคเปิดของเขาคือ "Claude has no planning engine." แก่นของโพสต์ถูกแยกเป็นหน้า [[plan-mode-as-prompting]].

## สิ่งที่ Horvat โต้แย้ง

Horvat บอกว่า Plan mode ดูฉลาดเพราะมันเขียน numbered steps, พูดถึง obstacle, และอธิบาย feature ก่อนแก้ไฟล์. แต่ตามเขา สิ่งนี้ยังไม่ใช่ symbolic reasoning หรือ planning engine.

มุมของเขาคือ [[claude|Claude]] ยังอยู่บนฐาน LLM ที่ทำ pattern recognition. Plan mode จึงเป็น prompt และ harness behavior: sandbox ไม่ให้แก้ไฟล์ แล้วสั่ง model ให้ enumerate steps ก่อน implement. เขามองว่านี่คือเทคนิคเดียวกับที่ ChatGPT ทำได้ตั้งแต่ก่อนหน้า เพียงแต่ Claude Code ทำให้ polished กว่า.

**ได้อะไร:** plan output เป็น artifact ที่คนตรวจได้ ไม่ใช่หลักฐานว่า model เข้าใจปัญหาแบบ senior engineer.

## การทดสอบที่เขาเล่า

Horvat บอกว่าเขาทดสอบ prompt เดียวกับสอง model:

- Sonnet 4.6 วาง solution ที่ inefficient จนอาจทำให้ server เสี่ยง crash และปล่อย bug ที่เขามองว่าโง่มาก
- Opus 4.7 วางแผนเรื่อง performance ดีกว่า เลี่ยง bottleneck ชัด ๆ และสุดท้ายผลิต code ที่ทำงานได้

แต่เขาไม่ตีความว่า Opus เข้าใจปัญหาจริงกว่า. เขาบอกว่า Opus ดีกว่าเพราะ prompt/iteration strategy refined กว่า และ steering ไปทางคำตอบที่ดู senior มากขึ้น.

**ผลคือ:** model ที่แพงกว่าอาจให้ plan ดีกว่า แต่ยังต้องตรวจว่ามันถามคำถามถูกหรือยัง.

## สิ่งที่ทั้งสอง model ยังพลาด

จุดสำคัญของโพสต์ไม่ใช่ "Sonnet แย่ Opus ดี." Horvat บอกว่าทั้งคู่ยังพลาด senior moves ที่ชัด:

- ไม่ถามว่าการทิ้ง user data เป็น decision ที่ถูกต้องไหม
- ไม่เห็น duplicated information ที่อยู่ทั้ง server-side และ client-side code

นี่คือช่องว่างระหว่าง planning-looking text กับ [[judgement-vs-automation|engineering judgment]]. Model อาจเรียงขั้นตอนสวย แต่ยังไม่แตะคำถามที่เปลี่ยน architecture, data safety, หรือ product semantics.

**ได้อะไร:** plan mode อาจช่วยเริ่มงาน แต่ไม่ควรแทน review ของคนที่เข้าใจโดเมนและความเสี่ยง.

## Reply: ใช้ web search ช่วย verify plan

ใน conversation มี reply หนึ่งบอกว่าเขามักสั่ง agent ให้ verify plan ด้วย web search หา best patterns/practices โดยใช้ searxng และ Firecrawl fetch results. มุมนี้ไม่ได้หักล้าง Horvat โดยตรง แต่เสนอวิธีเพิ่ม [[grounding|grounding]] ให้ plan.

แปลเป็นภาษาของ wiki: ถ้า plan เป็น draft จาก pattern recognition เราควรเสริมด้วย external prior art, code evidence, และ deterministic checks. Search ไม่ได้ทำให้ model มี symbolic planner แต่ช่วยลดการเดาในเรื่องที่มี best practice ภายนอกให้เทียบ.

## ความตึงกับ dynamic workflows

wiki มีหน้า [[dynamic-workflows]] ที่บันทึก claim ฝั่ง Anthropic/Piyalitt ว่า Claude Code + Opus 4.8 สามารถ self-plan, dispatch subagents, self-verify, และทำ large-scale change ได้. โพสต์ของ Horvat ไม่ได้ลบ claim นั้น แต่เพิ่มคำถามสำคัญ:

> เวลาพูดว่า "Claude self-plans" เราหมายถึง planning engine จริง หรือหมายถึง harness ที่ prompt ให้ model ผลิต plan แล้ววนตรวจ?

คำตอบที่ปลอดภัยตอนนี้คือเก็บทั้งสองด้าน. Dynamic workflows อาจมี utility สูงในงานที่มี oracle เช่น test suite. แต่ plan ที่ออกมายังควรถูกอ่านเป็น draft + evidence request ไม่ใช่ judgement สุดท้าย.

## ข้อสังเกตของ wiki

โพสต์นี้เข้ากับ [[coding-harness]] โดยตรง. ถ้า Plan mode เป็น prompt strategy + sandbox + read-only subagent มันเป็น harness feature ไม่ใช่ความสามารถล้วนของ model. และถ้า plan quality เปลี่ยนตาม model/effort/prompt iteration แปลว่าผู้ใช้ต้องออกแบบ review gate รอบ plan ด้วย.

แก่นปฏิบัติ: ให้ agent plan ได้ แต่อ่าน plan แบบที่อ่าน junior engineer proposal. ถามว่า plan มี evidence ไหม, มี alternative ไหม, preserve user data ไหม, ลด duplication ไหม, และมี verification path อะไร.

## See also

- [[plan-mode-as-prompting]]
- [[zoran-horvat]]
- [[claude]]
- [[claude-code]]
- [[coding-harness]]
- [[dynamic-workflows]]
- [[judgement-vs-automation]]
- [[grounding]]
- [[agentic-code-review]]
