---
title: Intent Artifact (intent.md)
type: concept
tags: [ai, software-engineering, intent, requirements, sdlc, artifacts]
created: 2026-09-09
updated: 2026-09-14
sources: [claude-codes-new-intent-md-rob-shocks.md, ai-native-sdlc-playbook.md]
---

# Intent Artifact (intent.md) / เก็บเจตนาก่อนเขียนสเปก

**`intent.md`** คือ proto-spec แบบ Markdown ที่บันทึกว่าใครอยากเปลี่ยนอะไร เพราะอะไร กระทบใคร มี constraint อะไร และยังมีคำถามไหนค้างอยู่ [[anthropic|Anthropic]] วางไฟล์นี้ไว้เป็น artifact ชิ้นแรกของ AI-Native SDLC ชื่อไฟล์ใช้ตัวพิมพ์เล็กตามต้นทาง แม้ชื่อวิดีโอของ [[rob-shocks|Rob Shocks]] จะเขียน `INTENT.MD`

คนต้นเรื่องหรือ originator อาจเป็นลูกค้า product manager หรือ developer ก็ได้ เขาคุยกับ agent จนโจทย์ชัด แล้วต้องอ่านและแก้ไฟล์ด้วยตัวเองก่อนส่งให้ product owner

**ได้อะไร:** คำของคนที่รู้ปัญหายังอยู่ใน artifact ก่อนผ่านการตีความและ handoff หลายรอบ

## ไม่ใช่ PRD และยังไม่ใช่ spec

`intent.md` อยู่ก่อน `spec.md` ทำหน้าที่เก็บ problem, desired outcome, affected users/systems, constraints และ open questions โดยยังไม่ต้องตัดสิน design ทั้งหมด

`spec.md` รับ intent ไปแปลงเป็น requirement กับ design ที่ลงรายละเอียดมากขึ้น ส่วน `plan.md` บอกว่าจะเปลี่ยนไฟล์ไหน ทำตามลำดับใด เสี่ยงตรงไหน และพิสูจน์ผลอย่างไร เมื่อแยกเป็นสามชิ้น ทีมจะเห็นว่าข้อไหนมาจากคนต้นเรื่อง ข้อไหนเป็น design decision และข้อไหนเป็นแผน implementation

**ผลคือ:** ถ้า design เปลี่ยน ทีมยังย้อนดูได้ว่าแก้เพราะ constraint ใหม่ หรือเผลอหลุดจากปัญหาเดิม

## ขั้นต่ำที่ควรมี

- Originator และสถานะ draft/accepted
- ปัญหาที่เจอในคำของคนต้นเรื่อง
- ผลลัพธ์ที่อยากได้ ไม่ใช่แค่ feature name
- ผู้ใช้และระบบที่กระทบ
- Constraint และสิ่งที่อยู่นอก scope
- คำถามที่ยังไม่มีคำตอบ

ไฟล์ควรอยู่ในระบบที่เก็บ version และมี owner รับช่วงต่อ Anthropic เสนอให้เริ่มด้วย directory `intent/` ใน product repo ส่วนระบบ requirement เดิมยังใช้ต่อได้ แต่ทีมต้องบอกให้ชัดว่าอะไรเป็น source of truth และเชื่อมสองฝั่งด้วย record ID กับ commit SHA

## จุดที่ช่วยและจุดที่ช่วยไม่ได้

`intent.md` ช่วยลดข้อมูลหายระหว่าง handoff และทำให้ agent session ใหม่เริ่มจาก artifact เดียวกันได้ แต่ไม่ได้ทำให้ความหมายใน prose ตรวจด้วยเครื่องได้

ตรงนี้ต้องอ่านคู่กับ [[intent-gap|Intent Gap]] ฝั่ง `intent.md` แก้ปัญหา "ไม่มีใครเขียนเจตนาไว้" ส่วน test, schema, invariant และ [[facts-first|executable fact]] แก้ปัญหา "เครื่องพิสูจน์ไม่ได้ว่า code ทำตามเจตนา" สองชั้นนี้เสริมกัน ไม่มีชิ้นไหนแทนอีกชิ้น

**ผลคือ:** `intent.md` ใช้นำทางและย้อนดูการตัดสินใจได้ แต่รับรองไม่ได้ว่า implementation ถูก

## ต้นเรื่องไม่จำเป็นต้องเป็นคน

[[ai-native-sdlc-playbook|ตัว playbook]] ให้ช่วง Maintain สร้าง `intent.md` ได้ด้วย เมื่อค่าทะลุ [[control-bands|control band]] agent จะเข้าไปวินิจฉัย แล้วบันทึกปัญหาที่เจอ หลักฐานจาก log ผลที่อยากได้ และระบบที่กระทบลงไฟล์ จากนั้นจึงส่งกลับเข้า Stage 1 ให้ on-call เป็นคน triage

งานจากไอเดียของคนกับงานจาก incident จึงเดินผ่านขั้นตอนและ gate ชุดเดียวกัน พร้อมเก็บ audit trail แบบเดียวกัน

**ได้อะไร:** maintenance เลิกเป็นงานที่รอคนเริ่มสืบ กลายเป็นข้อเสนอที่มีหลักฐานประกอบรออยู่ในคิวแล้ว

## คำถามเปิด

- ใครมีสิทธิ์แก้ intent หลัง `spec.md` หรือ code เริ่มแล้ว
- ถ้า Jira กับ repo มีข้อมูลไม่ตรงกัน ฝั่งไหนชนะ
- ทีมจะวัด survival rate ของ intent โดยไม่เร่งให้ product owner รับทุกไฟล์เพื่อทำ metric ให้สวยได้อย่างไร
- งานเล็กแค่ไหนที่เขียน intent แล้ว ceremony แพงกว่าประโยชน์

## See also

- [[ai-native-sdlc-playbook]]
- [[claude-codes-new-intent-md-rob-shocks]]
- [[artifact-chain]]
- [[ai-driven-sdlc]]
- [[spec-driven-development]]
- [[intent-gap]]
- [[facts-first]]
- [[shaping-the-build]]
- [[control-bands]]
