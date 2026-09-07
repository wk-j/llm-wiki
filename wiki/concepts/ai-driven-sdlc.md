---
title: AI-Driven Software Development Lifecycle
type: concept
tags: [ai, software-engineering, sdlc, agents, verification, workflow]
created: 2026-08-16
updated: 2026-08-16
sources: [the-new-software-lifecycle.md]
---

# AI-Driven Software Development Lifecycle / วงจรพัฒนาซอฟต์แวร์ที่มี AI เป็นแรงขับ

**AI-driven Software Development Lifecycle (AI-driven SDLC)** คือวงจรพัฒนาซอฟต์แวร์ที่ใช้ coding agent ช่วยตั้งแต่ requirement ไปถึง maintenance. มันไม่ได้ลบ phase เดิมออก แต่ทำให้แต่ละ phase เร็วขึ้นไม่เท่ากัน [[the-new-software-lifecycle|Addy Osmani]] จึงมองว่าจุดคอขวดกำลังย้ายจากการเขียน code ไปอยู่ที่ specification, architecture และ verification

## รูปร่างของ lifecycle เปลี่ยนอย่างไร

ก่อนมี agent implementation กินเวลาส่วนใหญ่ของ sprint. พอ agent สร้าง code ได้ในไม่กี่นาทีหรือชั่วโมง งานสองฝั่งของ implementation กลับเด่นขึ้น: ก่อนเขียนต้องบอกให้ชัดว่าจะสร้างอะไร หลังเขียนต้องพิสูจน์ว่าผลตรงโจทย์และไม่ทำของเดิมพัง

`requirement/spec → architecture → implementation → output + trajectory eval → review/deploy → production feedback → maintenance`

วงรอบนี้สั้นลงจากระดับสัปดาห์เป็นนาทีหรือชั่วโมงได้ในบางงาน แต่ไม่ได้แปลว่าทุกขั้นอัตโนมัติ งานที่ต้องรู้บริบทธุรกิจหรือรับผิดชอบความเสี่ยงยังต้องมีคนตัดสิน

**ได้อะไร:** ความเร็วของ agent มีค่าก็ต่อเมื่อ phase ก่อนและหลัง implementation รับ throughput นั้นไหว

## Verification ย้ายเข้ามาอยู่กลางวงรอบ

SDLC แบบนี้ไม่ได้รอให้ “เขียนเสร็จ” แล้วค่อยโยนให้ QA. Test กับ eval ทำหน้าที่บอก agent ตั้งแต่ระหว่างทำว่าอะไรคือ correct แล้วส่ง failure กลับเข้า loop

- **Test** เหมาะกับพฤติกรรม deterministic เช่น input นี้ต้องได้ output นี้
- **Output eval** ดูว่าผลสุดท้ายตรง rubric หรือไม่
- **Trajectory eval** ดูว่า agent ใช้ tool, permission และ check ตามขั้นที่ควรหรือไม่
- **Production monitoring** หา failure class ใหม่แล้วเติมกลับเข้า regression suite

วิธีนี้เชื่อมกับ [[evals-and-error-analysis]]: รันชุดวัด อ่านเคสที่พัง จัดกลุ่มสาเหตุ แก้ prompt/tool/context แล้วรันซ้ำ ถ้าไม่มีวงรอบนี้ demo ที่สำเร็จครั้งเดียวก็ยังไม่ใช่หลักฐานว่า workflow เชื่อถือได้

**ผลคือ:** verification ไม่ใช่ปลายทาง แต่เป็น feedback system ที่ทำให้ agent แก้งานตัวเองภายในขอบเขตที่วัดได้

## Spec กลายเป็นคอขวด แต่ไม่ใช่ source of truth ที่พอด้วยตัวเอง

เมื่อ implementation ถูกลง สิ่งที่ทีมยังต้องคิดหนักคือ scope, constraint, edge case และ tradeoff ทาง architecture. ตรงนี้ทำให้ specification quality สำคัญขึ้นและดูคล้าย [[spec-driven-development|Spec-Driven Development]]

แต่สองเรื่องไม่ควรถูกรวมเป็นอันเดียวกัน Spec ช่วยบอก intent และทำ handoff ได้ ส่วน test, schema, type และ production invariant คือ executable fact ที่เครื่องตรวจเองได้. Prose spec ยังตีความคลาดเคลื่อนได้และไม่แทน business judgement

**ได้อะไร:** ใช้ spec เพื่อทำ intent ให้เห็นชัด แล้วใช้ verifier พิสูจน์ว่าสิ่งที่สร้างตรงกับ intent จริง

## Harness กับ context คือ infrastructure ของ lifecycle

ตัว model ไม่ได้ขับ lifecycle คนเดียว [[coding-harness|Harness]] เป็นผู้จัด tool, sandbox, hook, memory, orchestration และ observability ส่วน [[context-engineering|context engineering]] เลือกว่ากฎหรือความรู้ใดต้องโหลดทุกครั้ง และอะไรค่อยดึงมาเมื่อ task ต้องใช้

เส้นแบ่งนี้กระทบสามอย่างพร้อมกัน:

1. **คุณภาพ** — context ขาดทำให้ agent เดา แต่ context ล้นทำให้ signal จมหาย
2. **ความปลอดภัย** — core guardrail บางข้อควรอยู่ตลอด ขณะที่ tool เฉพาะงานเปิดเมื่อจำเป็น
3. **ต้นทุน** — static context จ่ายซ้ำทุก call ส่วน dynamic context ต้องลงทุนใน trigger กับ retrieval

**ผลคือ:** SDLC แบบใหม่ต้อง version context policy และ harness เหมือน code ไม่ใช่เก็บเป็น prompt ส่วนตัวของใครคนหนึ่ง

## เลือกตำแหน่งบนช่วง vibe coding ถึง Agentic Engineering

งานทุกชิ้นไม่ต้องใช้ ceremony เท่ากัน Prototype ที่ทิ้งได้อาจยอมรับการลองแล้วดู ส่วนระบบ production ที่แตะข้อมูลหรือเงินต้องมี spec, automated checks, eval, permission gate และ human review

คำถามตัดสินแบบสั้น:

- ถ้าพัง ใครเสียหายและย้อนกลับได้ไหม
- Code ต้องอยู่กี่วัน และใครต้อง maintain ต่อ
- มี verifier ที่รันซ้ำได้หรือยัง
- Agent เห็น context ทางธุรกิจที่จำเป็นครบหรือไม่
- เวลาตรวจและแก้งานถูกนับในต้นทุนแล้วหรือยัง

**ได้อะไร:** เส้นแบ่งระหว่าง [[vibe-coding]] กับ [[agentic-engineering]] อยู่ที่ stake และหลักฐาน ไม่ได้อยู่ที่ชื่อ tool หรือ model

## ข้อจำกัดและคำถามเปิด

- Productivity ขึ้นกับชนิดงาน ประสบการณ์คน และ harness; งานบางชุดเร็วขึ้น ขณะที่บางชุดช้าลงเมื่อรวม review/rework
- การเร่ง implementation อาจสร้างคิวหน้า review และเพิ่ม [[orchestration-tax]] ถ้า verification ไม่โตตาม
- “Prototype กลายเป็น production agent โดยไม่ rewrite” จะจริงแค่ไหนขึ้นกับ permission, data governance, observability และ runtime ที่ prototype ไม่มี
- Agent อาจทำ 80% แรกเร็ว แต่ 20% ท้ายยังติด edge case และรอยต่อระหว่างระบบ
- การวัด trajectory อาจเพิ่มความปลอดภัย แต่ก็เสี่ยงกลายเป็น process theater ถ้า rubric ไม่โยงกับผลจริง

## See also

- [[the-new-software-lifecycle]]
- [[agentic-engineering]]
- [[vibe-coding]]
- [[coding-harness]]
- [[context-engineering]]
- [[evals-and-error-analysis]]
- [[spec-driven-development]]
- [[orchestration-tax]]
- [[engineering-role-shift]]
- [[software-ecology]]
