---
title: "Loop Engineering — mikelopster"
type: source
tags: [ai, agents, loops, harness, automation, workflow, thai]
created: 2026-06-28
updated: 2026-06-28
url: https://www.youtube.com/watch?v=qlIuFfs-7pY
sources: ["รู้จักกับ Loop Engineering — mikelopster transcript"]
---

# Loop Engineering — mikelopster / รู้จักกับ Loop Engineering

วิดีโอของ [[mikelopster]] (creator ไทยที่ทำคอนเทนต์สาย software และ AI) อธิบาย [[loop-engineering|Loop Engineering]] จากมุมคนลองใช้จริงกับ [[claude-code|Claude Code]] และ [[openai-codex|Codex]]. จุดสำคัญของคลิปไม่ใช่แค่ "ลูปคืออะไร" แต่คือความลังเลหลังลองแล้ว: คอนเซปต์ดูดี แต่ใช้ผิดงานแล้วจะเผา token, สร้างงานค้างให้คนรีวิว, หรือซ้ำกับ workflow ที่ agent ทำอยู่แล้ว.

แก่นของคลิปอยู่ตรงนี้: **loop engineering เหมาะเมื่อมี goal ชัด, feedback gate ชัด, และระบบตรวจเองได้จริง.** ถ้างานยังต้องใช้รสนิยมมนุษย์หรือมนุษย์เป็นคอขวดสุดท้าย ลูปอาจไม่ได้เพิ่ม productivity เท่าที่รู้สึก.

## เส้นทางจาก Prompt → Context → Loop

ช่วงต้นคลิปวางเรื่องนี้เป็นวิวัฒนาการของการทำงานกับ agent:

- **Prompt Engineering** - เราออกแบบ prompt ดี ๆ แล้วหวังให้ output ดีขึ้น
- **Context Engineering** - เราจัด context, memory, file, tool, และ harness ให้ agent ไม่หลงทาง
- **Loop Engineering** - เราไม่ได้ prompt ทีละรอบเอง แต่ระบุ **goal** แล้วออกแบบระบบให้ agent สร้าง prompt, ลงมือทำ, ตรวจผล, และวนจนผ่าน

mikelopster อธิบายว่า agent ปกติมี loop ย่อยอยู่แล้ว: รับ prompt → reason/listening → action → observe → ทำต่อจนจบ. Loop Engineering เพิ่ม "วงนอก" เข้าไปอีกชั้น. วงนอกนี้เริ่มจาก **goal prompt** ไม่ใช่ prompt งานเดียว แล้วมีตัวตรวจว่า goal สำเร็จหรือยัง.

> ได้อะไร: จุดเปลี่ยนคือจาก "เราสั่งทีละ step" ไปเป็น "เราบอกเป้าหมายและเกณฑ์จบ" แล้วให้ agent วนหาวิธีไปถึงเป้าหมายนั้นเอง.

## Loop Engineering ต่างจาก cronjob ยังไง

คลิปแยกเรื่องนี้ชัด เพราะหลายคนได้ยินคำว่า loop แล้วนึกถึง cronjob ทันที.

**Cronjob** คือ script ชุดเดิมที่ทำงานตามเวลา. ทุก 1 นาที, ทุก 5 นาที, ทุกวัน. มันไม่เข้าใจสถานการณ์มากนัก. ต่อให้มีเงื่อนไข ก็เป็นเงื่อนไขที่เราเขียนตายตัวไว้.

**Loop Engineering** เพิ่ม agent เข้าไปในวง. พอมี trigger ตัว agent จะดู state ปัจจุบัน, ตีความว่าเกิดอะไรขึ้น, เลือก action, ตรวจผล, แล้วตัดสินใจว่าจะวนต่อหรือหยุด. ตัวอย่างในคลิปคือ PR watcher: มี PR ใหม่ → agent investigate → review / แก้ CI → ส่งให้มนุษย์ตรวจ → กลับไปรอ PR ใหม่.

สิ่งที่ทำให้ loop ไม่ใช่ cronjob ธรรมดาคือ **feedback gate**. นี่คือจุดวัดว่า "ผ่านหรือยัง". ถ้า gate ไม่ดี ลูปจะพังสองแบบ:

- gate เข้ม/คลุมเครือเกินไป - agent วนแก้ไม่จบและเผา token
- gate หลวมเกินไป - agent บอกว่าผ่าน ทั้งที่งานจริงยังไม่ผ่าน แล้วมนุษย์ต้องมาแก้ซ้ำ

> ได้อะไร: loop ที่ดีไม่ได้เริ่มจาก "ให้มันวน" แต่เริ่มจาก "เราจะรู้ได้ยังไงว่าควรหยุด".

## Claude Code และ Codex ในมุมผู้ใช้

mikelopster เล่าว่าลองกับสองเครื่องมือหลัก:

- **Claude Code** - ใช้ `/loop` สำหรับงานที่รู้ cadence ชัด เช่น "ทุก 5 นาทีเช็คว่า deploy เสร็จหรือยัง" หรือ "คอยดู CI/PR". ถ้ายังไม่แน่ใจว่าควร loop แบบไหน เขาแนะนำให้ใช้ `/goal` เพื่อให้ agent วิเคราะห์ก่อนว่าควรแตกงาน/สร้าง loop ยังไง. ใน UI ฝั่ง Claude ยังมี routine / scheduled task เป็นอีกผิวหนึ่งของแนวคิดเดียวกัน
- **Codex** - ไม่มี `/loop` แบบเดียวกับ Claude Code ในคลิป แต่มี schedule / scheduled task และมีแนว `/goal` ที่ระบุเป้าหมายให้ agent แตกงาน, dispatch subagent, และ verify ต่อเองได้

สิ่งที่เขาย้ำคือคำสั่งไม่ใช่สาระหลัก. เครื่องมือหลายเจ้ามี primitive คล้ายกันแล้ว. สาระคือเราออกแบบ trigger, goal, skill, และ feedback gate ได้ดีแค่ไหน.

## Use case ที่ดูเหมาะ

คลิปรวม use case ที่คนพูดถึง และแยกจากประสบการณ์ของ mikelopster เอง.

งานที่ดูเหมาะคือ:

- **Development loop** - แก้ error จน build ผ่าน, แก้ test จนผ่าน, เพิ่ม coverage ตาม threshold, ไล่ lint ให้สะอาด
- **PR loop** - มี PR ใหม่หรือ CI แดง → agent ดึง context, แก้เบื้องต้น, เปิดหรืออัปเดต PR, ส่งให้คนตรวจ
- **Support loop** - issue/ticket ใหม่ → agent อ่านรายละเอียด, หาแนวแก้, อาจเปิด PR ให้
- **Monitoring loop** - log/metric ผิดปกติ → agent investigate, สรุปสาเหตุ, หรือแก้เบื้องต้น
- **Research/content loop** - ดึง source หลายที่, สรุป, เขียน draft

แต่เขาชี้ว่าความเหมาะไม่เท่ากัน. กลุ่ม code quality / CI / lint / test มีเกณฑ์จบชัดกว่า. กลุ่ม content มีปัญหาเพราะ "อ่านแล้วรู้สึกแปลก" เป็นเกณฑ์ที่นิยามยาก.

## ประสบการณ์ลองจริง: บาง loop ซ้ำกับ workflow เดิม

mikelopster เล่าว่าเขามี workflow ปกติที่ให้ Claude Code ทำ plan, เขียน pending task, review, refactor, และ run test อยู่แล้ว. พอลองสร้าง loop เพิ่มเพื่อ review/refactor ซ้ำ ผลลัพธ์กลับไม่ได้ต่างจากเดิมมาก เพราะในงานนั้น agent มี loop ตรวจงานอยู่ใน task เดียวแล้ว.

ตรงนี้เป็นข้อสังเกตสำคัญ: **loop engineering ไม่ได้จำเป็นกับทุกงานที่ทำซ้ำ.** ถ้างานเป็น todo list ที่ agent ใหญ่ ๆ อย่าง Sonnet/Opus หรือ GPT-5.5 จัดการได้ใน session เดียว การเพิ่ม loop อาจเป็น ceremony ที่เพิ่ม cost มากกว่าคุณค่า.

เขาบอกว่าลูปจะมีประโยชน์ขึ้นเมื่อใช้ model/agent ตัวเล็กกว่า หรือเมื่องานต้องรอ trigger ภายนอกจริง ๆ เช่น CI, PR, issue, log, หรือ schedule.

## งาน content เป็นตัวอย่างของคอขวดมนุษย์

เขาลองทำ loop ที่ทุกครึ่งวันดึงข่าว/source มาเขียน content. ผลคือ source ที่เลือก "ดี" และ draft "โอเค" แต่พออ่านจริงยังมีการเชื่อมโยงแปลก ๆ และยังไม่ใช่งานที่เขาอยากใช้ทันที.

ปัญหาคือถ้านิยามความแปลกนั้นเป็น rule ไม่ได้ คนก็ต้องกลับมา review เอง. และถ้า agent ผลิต content ทุกครึ่งวัน ผ่านไปสองวันจะมี draft กองเต็มไปหมด. คอขวดเลยไม่ใช่การสร้าง draft แต่เป็น **คนที่ต้องอ่าน ตัดสิน และแก้**.

ตรงนี้ต่อกับ [[orchestration-tax|Orchestration Tax]] ตรง ๆ: agent ผลิตงานได้ขยันมาก แต่ judgement ของคนยังเป็น serial resource. ปล่อย agent 10 ตัวไม่ได้แปลว่า productivity คูณ 10 ถ้าคนตรวจยังมีคนเดียว.

## เกณฑ์ว่าเหมาะหรือไม่เหมาะ

คลิปสรุป criteria แบบใช้งานง่าย:

**เหมาะกับ loop เมื่อ:**

- มี exit condition ชัด
- วัดผลได้ชัด เช่น test, lint, coverage, CI, metric, rule
- มีจุดวนซ้ำที่เกิดจริงจาก trigger หรือ schedule
- agent ตรวจเองได้โดยไม่ต้องรอคนทุกขั้น

**ยังไม่เหมาะเมื่อ:**

- งานใช้รสนิยมสูง เช่น "ทำให้สวยขึ้น", "เขียนให้น่าอ่านขึ้น", "เลือก angle คอนเทนต์ให้ดีขึ้น"
- งานพลาดไม่ได้และต้องมี validation จากคนก่อน เช่น production data, security key, policy-sensitive action
- คนยังเป็นคอขวดของทุก output

> ได้อะไร: loop ไม่ใช่ปุ่มเร่งทุกอย่าง. มันเร่งได้ดีเฉพาะงานที่มี scorer ชัดและไม่เอา attention ของคนมาเป็น gate ทุกครั้ง.

## Guardrail ที่ต้องมี

ข้อควรระวังที่คลิปย้ำ:

- ตั้งเพดานจำนวนรอบของ loop
- ตั้ง token / budget limit
- เขียน definition of done ให้ชัด
- ให้ agent ตรวจงานตัวเองด้วยหลักฐาน ไม่ใช่แค่บอกว่าเสร็จ
- ถ้าเป็นไปได้ แยก maker/checker หรือให้ `/goal` ออกแบบตัว verify เพิ่ม

ถ้าไม่มี guardrail พอ ลูปจะเกิดสองปัญหาพร้อมกัน: **ผลลัพธ์ไม่ถูก และ token หมดไปเยอะ**.

## บทสรุปของคลิป

mikelopster สรุปด้วยความไม่ตกผลึกเต็มที่แบบตั้งใจ. เขาเห็นว่า Loop Engineering เป็นไอเดียที่น่าสนใจ แต่ยังหางานของตัวเองที่ "ต้องใช้ loop จริง ๆ" ไม่เจอมากนัก. หลายอย่างที่ลองเหมือนซ้ำกับ workflow agent เดิม หรือสุดท้ายยังตันที่การตัดสินของคน.

ประโยคที่ควรจำจากคลิปนี้ไม่ใช่ "ต้องทำ loop" แต่คือ: **ก่อนทำ loop ให้ถามว่างานนี้มี feedback gate ที่วัดเองได้ไหม และเมื่อมันผลิต output มาแล้ว ใครเป็นคอขวดจริง ๆ.**

## ประเด็นหลักที่ดึงออกมา

- [[loop-engineering]] - เพิ่มมุมผู้ใช้ไทย: goal prompt + feedback gate สำคัญกว่าแค่ trigger
- [[queues-over-loops]] - สนับสนุนมุมว่าไม่ใช่ทุกงานต้องเป็น loop; หลายเคสคือคิวงาน scoped ที่ agent หยิบไปทำ
- [[orchestration-tax]] - content loop และ multi-agent output สุดท้ายตันที่ human review
- [[claude-code]] / [[openai-codex]] - ตัวอย่าง primitive ของ `/loop`, `/goal`, routine, schedule

## See also

- [[loop-engineering]]
- [[mikelopster]]
- [[claude-code]]
- [[openai-codex]]
- [[orchestration-tax]]
- [[queues-over-loops]]
- [[agentic-code-review]]
- [[harness-guides-sensors]]
- [[behavioral-verifier]]
