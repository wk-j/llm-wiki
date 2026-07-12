---
title: Specs-to-Code
type: concept
tags: [ai-coding, automation, workflow, hype]
created: 2026-05-09
updated: 2026-07-12
sources: [matt-pocock-software-fundamentals.md, "Stop Writing Specs. Start Writing Facts. The Entire SDD Movement Is Already Obsolete..md", new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets.md]
---

# Specs-to-Code / จากสเปกสู่โค้ด (โดยไม่ดูไส้ใน)

**Specs-to-Code** เป็นความเชื่อหรือกระบวนการทำงานที่ว่า "เราสามารถเขียนแค่รายละเอียดความต้องการ (Specification) แล้วให้ AI เปลี่ยนเป็นโค้ดที่ทำงานได้จริง โดยที่มนุษย์ไม่จำเป็นต้องอ่านหรือแก้ไขโค้ดนั้นเลย"

## แก่นความคิด
แนวคิดนี้มองว่า "Code is Cheap" (โค้ดมีราคาถูก) จนเราสามารถทิ้งแล้วสร้างใหม่จาก spec ได้ตลอดเวลาเหมือนการ compile โค้ด

- **Workflow**: เขียน Spec -> AI Generate Code -> รัน App -> ถ้ามีปัญหา กลับไปแก้ที่ Spec -> วนลูป
- **เป้าหมาย**: เพื่อข้ามขั้นตอนการเขียนโค้ดไปสู่การแก้ปัญหาเชิงธุรกิจโดยตรง

## คำเตือนจากผู้เชี่ยวชาญ
[[matt-pocock]] และผู้เชี่ยวชาญหลายคนมองว่าแนวคิดนี้เป็น "กับดัก" (Trap) เพราะ:
1. **Software Entropy**: โค้ดที่สร้างโดย AI ซ้ำๆ โดยไม่มีการออกแบบโครงสร้างที่ดีจะค่อยๆ เสื่อมสภาพ (Entropy) จนทำงานผิดพลาด
2. **Code is Not Cheap**: โค้ดแย่ๆ คือหนี้สินที่แพงที่สุด เพราะมันจะขัดขวางไม่ให้ AI ตัวอื่นๆ เข้ามาทำงานต่อได้ (Context ตัน หรือ AI เข้าใจผิด)
3. **Vibe Coding by another name**: หากทำโดยไม่มีระเบียบวินัย มันก็คือการ [[vibe-coding]] ที่ขาดการตรวจสอบคุณภาพ

## หลักฐานจากฝั่ง SDD เอง (2026-06-11)

คำเตือนของ Pocock ได้แรงหนุนจากคนที่เคยอยู่ฝั่งตรงข้าม: [[jaroslaw-wasowski|Jaroslaw Wasowski]] (อดีตคนเชียร์ [[spec-driven-development|SDD]] 6 บทความ) ถอนคำพูดใน [[stop-writing-specs-start-writing-facts]] ด้วยเหตุผลเชิงกลไก — spec ที่เป็น prose ต้องผ่านการตีความของ model ทุกครั้ง และ [[llm-nondeterminism|LLM ไม่ deterministic แม้ temperature 0]] ดังนั้น "เขียน spec แล้วให้ AI ปั่นโค้ด" จึงไม่มีวันได้ผลซ้ำเดิม เขาเสนอ [[facts-first]] (เก็บความจริงเป็น executable assertion) มาแทนใน inner loop

## สิ่งที่ควรจะเป็น
แทนที่จะละทิ้งโค้ด มนุษย์ควรใช้ AI เป็นเครื่องมือช่วยในการ implement แต่ยังต้องรักษาอำนาจในการตัดสินใจเชิงสถาปัตยกรรม (Architectural decisions) และตรวจสอบความถูกต้องของโค้ดที่ออกมาเสมอ โดยอาจใช้ [[html-artifacts]] เพื่อสร้างแผนงาน (Plans) ที่อ่านง่ายและมีรายละเอียดครบถ้วนแทนการใช้ Markdown เพียงอย่างเดียว

## `/to-spec` ไม่ได้แปลว่า Specs-to-Code

ชื่อ `/to-spec` ใน [[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets|Skills v1.1]] อาจดูเหมือนพากลับมาหา pattern นี้ แต่ flow ที่ Pocock เสนอมี boundary เพิ่มทั้งสองฝั่ง. ก่อน spec มี grilling/Wayfinder, prototype และ human decisions. หลัง spec มี ticket ต่อ session, TDD, type checking, tests, [[dual-axis-code-review|review สองแกน]] และ commit.

ดังนั้น tension ที่ควรเก็บคือ: Pocock ยังใช้ spec เป็น artifact กลาง แม้เขาวิจารณ์การ generate code แบบไม่ดูไส้ใน. สำหรับเขา ปัญหาไม่ใช่ “มี spec” แต่คือการเชื่อว่า spec ตัด judgement, verification และ ownership ออกจากวงจรได้.

**ผลคือ:** `/to-spec` เป็น handoff ใน engineering lifecycle ไม่ใช่เครื่อง compile prose เป็น code ที่ไว้ใจได้ทันที.

## ดูเพิ่ม
- [[matt-pocock]]
- [[vibe-coding]]
- [[software-entropy]]
- [[code-is-free]] — แนวคิดที่เกี่ยวข้องกันในมุมของต้นทุน
- [[html-artifacts]] — สื่อกลางที่ช่วยให้ specs อ่านง่ายและตรวจสอบได้จริง
- [[spec-driven-development]] — movement เต็มรูปของแนวคิดนี้ พร้อมขอบเขตที่มันยังชนะ
- [[facts-first]] — ข้อเสนอทดแทน: เขียน fact ที่รันได้แทน spec ที่ต้องตีความ
- [[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets]]
