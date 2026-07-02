---
title: "Planning Mode is a Dangerous Illusion"
type: source
tags: [claude, planning, llm, coding-agents, harness, judgment, youtube]
url: https://www.youtube.com/watch?v=MnwHP8h5JlM
created: 2026-07-02
updated: 2026-07-02
sources: ["Planning Mode is a Dangerous Illusion — Zoran on C#.md"]
---

# Planning Mode is a Dangerous Illusion / Plan mode เป็นภาพลวงตาที่อันตราย

วิดีโอของ [[zoran-horvat|Zoran Horvat]] จากช่อง **Zoran on C#** เป็น breakdown ยาวของ thesis ที่อยู่ในโพสต์ X [[zoran-horvat-claude-no-planning-engine]]. เขาเทียบ [[claude-code|Claude Code]] Plan mode ระหว่าง Sonnet 4.6 กับ [[claude-opus-4-7|Opus 4.7]] โดยใช้ prompt เดียวกัน แล้วดูว่าแผนกับ implementation ต่างกันอย่างไร.

แกนของวิดีโอคือ Plan mode ดูเหมือนคิดเป็นขั้นตอน แต่ Horvat ย้ำว่าไม่มี planning engine แยกอยู่ข้างใต้. สิ่งที่มีคือ LLM + prompt/harness ที่บังคับให้เขียน plan ก่อนลงมือ. แนวคิดนี้ถูกรวมไว้ในหน้า [[plan-mode-as-prompting]].

## Setup การทดลอง

Horvat เริ่ม Claude Code โดยปิด auto memory เพื่อไม่ให้ run เก่าเข้ามาปน. เขาให้โจทย์ web app แบบจงใจไม่มาตรฐาน: ให้ผู้ใช้ upload source-code directory ผ่านเว็บ, ignore directory บางชนิด เช่น binaries หรือ `node_modules`, เก็บข้อมูลเป็น JSON document เดียวบน server เพื่อ demo, แล้ว render ตาราง path/name/line count ถ้ามี JSON อยู่.

เขาสั่งชัดว่าให้เข้า Plan mode และ "don't change anything" เพื่อให้เขารีวิวแผนก่อน. จุดนี้สำคัญ เพราะเขาไม่ได้ทดสอบแค่ code generation แต่ทดสอบว่า Plan mode เห็น risk ก่อน implementation ไหม.

**ได้อะไร:** plan ที่ดีควรจับ risk จาก requirement ได้ก่อน code ถูกเขียน ไม่ใช่แค่เรียงขั้นตอน implementation.

## Sonnet 4.6: แผนดูถูกต้องบางส่วน แต่ขาด client-side filtering

ใน run ของ Sonnet 4.6 แผน server-side ดูเหมือนถูก: มีการกรอง directory ที่ควร ignore, นับ line, และเก็บ metadata ของไฟล์ที่เหลือ. แต่ Horvat กังวลทันทีเมื่อไม่เห็น logic ฝั่ง client.

พอ implement จริง frontend เป็นแค่ bare input element สำหรับ upload directory. ไม่มี client-side filtering. ผลคือผู้ใช้อาจ upload binary files จำนวนมากขึ้น server ก่อนที่ server จะโยนทิ้ง. Horvat มองว่านี่ไม่ใช่แค่ inefficient แต่เสี่ยงทำให้ server crash ถ้า directory ใหญ่เกินไป.

Sonnet ยังมี bug อีกตัว: หลัง refresh แล้ว file paths หาย เพราะ implementation ใส่ file name ลงทั้ง path และ name field.

**ผลคือ:** Plan mode ที่ดูมี structure ยังพลาด performance/safety issue ที่ควรเห็นตั้งแต่ก่อน implement.

## ไม่มี planning engine: plan คือ prompt scaffold

Horvat อธิบายกลไกแบบตรงมาก: plan เป็นผลของ prompt อีกอันที่ craft มาอย่างดี และถูก wrap ด้วย sandbox เพื่อไม่ให้แก้ไฟล์. เขาเปรียบกับ prompt สมัย ChatGPT ก่อนหน้า: "อย่า implement ให้เขียน numbered steps ก่อน."

สิ่งที่ Claude Code เพิ่มคือ prompt และ harness polish. แต่ Horvat บอกว่านั่นไม่ได้แปลว่า plan correct ขึ้นโดยอัตโนมัติ. Plan อาจดูดีขึ้นเพราะ prompt ดีขึ้น แต่ยังขาด "depth of thought".

ตัวอย่าง depth gap คือ server ได้ content ของไฟล์มาแล้ว แต่สุดท้ายทิ้ง content ทั้งหมดเพื่อเก็บแค่ line count ตาม requirement. Horvat บอกว่ามนุษย์ที่มีประสบการณ์จะถามลูกค้าว่าแน่ใจไหมว่าจะทิ้ง user data เพราะ feature ถัดไปอาจต้องใช้.

**ได้อะไร:** ความสามารถในการถาม requirement กลับเป็นส่วนหนึ่งของ engineering judgment ไม่ใช่แค่การทำตาม requirement ให้ครบ.

## Opus 4.7: แผนดีขึ้น แต่ยังไม่ใช่ความเข้าใจแบบมนุษย์

run ของ Opus 4.7 ใช้ prompt เดิม. แผนละเอียดกว่าและเห็น client-side filtering ซึ่งเป็นจุดที่ Horvat อยากเห็น. Implementation ก็ดีกว่า: มี JavaScript สำหรับกรอง ephemeral directories ฝั่ง client, repopulate file paths ที่ browser strip ออกไป, และ output path/name ถูกต้อง.

Horvat ยอมรับว่า Opus ทำงานตามที่ขอได้ดีมากกว่า Sonnet. แต่เขายังตีความว่าเป็นผลจากการ prompt/iterate หลายรอบและ steering ให้คำตอบไปทาง senior-level content ไม่ใช่ symbolic logic หรือ planning engine จริง.

**ผลคือ:** model ที่แพงกว่าและขับด้วย harness ที่ดีกว่าอาจลด blind spots ได้มาก แต่ยังไม่ควรถูกนับเป็น senior engineer.

## สิ่งที่ Opus ยังพลาด

แม้ Opus ทำ implementation ผ่าน แต่ Horvat ยังชี้สอง blind spots:

- data ของผู้ใช้ยังถูกทิ้งทั้งหมด เหลือแค่ metadata/line count
- ignore list มีอยู่สองที่ ทั้ง client และ server ทำให้เกิด duplicated logic

ข้อแรกเป็น product/data question: เราควรทิ้งข้อมูลนั้นไหม. ข้อสองเป็น design issue: source of truth ซ้ำกันหรือเปล่า. Horvat บอกว่าทั้งสอง model ขาด depth of analysis ในส่วนที่ไม่ได้ถูกสั่งตรง ๆ แต่ควรอยู่ใน development culture ของ senior developer.

**ได้อะไร:** "ทำตาม prompt สำเร็จ" ไม่เท่ากับ "ออกแบบ feature ได้ดี".

## แหล่งเรียนรู้และ disclosure

ท้าย description มี resource/affiliate links หลายรายการ เช่น *Artificial Intelligence: A Modern Approach* โดย Peter Norvig และ Stuart Russell, *Modern Software Engineering* โดย David Farley, *Designing Data-Intensive Applications* โดย Martin Kleppmann, course OOP/C#/AI/ML, Discord, Patreon, และข้อมูลว่า Horvat มีประสบการณ์ software developer/architect/team lead มากกว่า 25 ปี และเขียน C# มาตั้งแต่ต้นยุค 2000s.

wiki ใช้ข้อมูลนี้เป็น context ของ author ไม่ใช่ independent credential verification.

## ข้อสังเกตของ wiki

วิดีโอนี้ทำให้หน้า [[plan-mode-as-prompting]] แข็งขึ้น เพราะมี concrete demo ไม่ใช่แค่ claim สั้น ๆ จาก X. มันยังต่อกับ [[judgement-vs-automation]] ชัดมาก: plan drafting อาจ automate ได้ แต่การถามคำถามที่ควรถาม, รักษาข้อมูลผู้ใช้, ลด duplicated logic, และมอง server-load risk ยังเป็น judgement.

ต้องเก็บ tension กับ [[dynamic-workflows]] ต่อไป. ถ้างานมี test suite/verifier ที่จับ outcome ได้ Dynamic Workflows อาจมีประโยชน์มาก. แต่สำหรับ decision ที่ไม่มี oracle เช่น "ควรเก็บข้อมูลผู้ใช้ไหม" plan mode ยังต้องมี human review.

## See also

- [[plan-mode-as-prompting]]
- [[zoran-horvat-claude-no-planning-engine]]
- [[zoran-horvat]]
- [[claude-code]]
- [[claude-opus-4-7]]
- [[coding-harness]]
- [[dynamic-workflows]]
- [[judgement-vs-automation]]
- [[grounding]]
