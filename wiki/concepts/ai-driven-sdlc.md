---
title: AI-Driven Software Development Lifecycle
type: concept
tags: [ai, software-engineering, sdlc, agents, verification, workflow]
created: 2026-08-16
updated: 2026-09-14
sources: [the-new-software-lifecycle.md, claude-codes-new-intent-md-rob-shocks.md, ai-native-sdlc-playbook.md]
---

# AI-Driven Software Development Lifecycle / วงจรพัฒนาซอฟต์แวร์เมื่อ AI เข้ามาช่วย

**AI-driven Software Development Lifecycle (AI-driven SDLC)** คือวงจรพัฒนาซอฟต์แวร์ที่ใช้ coding agent ช่วยตั้งแต่เก็บ requirement จนถึง maintenance ช่วงต่าง ๆ ยังอยู่ครบ แต่เร็วขึ้นไม่เท่ากัน [[the-new-software-lifecycle|Addy Osmani]] จึงมองว่าคอขวดกำลังย้ายจากการเขียน code ไปอยู่ที่ specification, architecture และ verification

## SDLC เปลี่ยนตรงไหน

ก่อนมี agent งาน implementation กินเวลาส่วนใหญ่ของ sprint พอ agent สร้าง code ได้ในไม่กี่นาทีหรือไม่กี่ชั่วโมง งานสองฝั่งของ implementation ก็เด่นขึ้นมาแทน ก่อนเขียนต้องบอกให้ชัดว่าจะสร้างอะไร หลังเขียนต้องพิสูจน์ว่าผลตรงโจทย์และไม่ทำของเดิมพัง

`requirement/spec → architecture → implementation → output + trajectory eval → review/deploy → production feedback → maintenance`

วงรอบนี้สั้นลงจากระดับสัปดาห์เป็นนาทีหรือชั่วโมงได้ในบางงาน แต่ไม่ได้แปลว่าทุกขั้นอัตโนมัติ งานที่ต้องรู้บริบทธุรกิจหรือรับผิดชอบความเสี่ยงยังต้องมีคนตัดสิน

**ได้อะไร:** ความเร็วของ agent มีค่าก็ต่อเมื่อ phase ก่อนและหลัง implementation รับ throughput นั้นไหว

## Anthropic ใช้ artifact ส่งงานข้ามแต่ละช่วง

ใน [[claude-codes-new-intent-md-rob-shocks|คำอธิบาย playbook ของ Rob Shocks]] วงจรนี้มีโครงส่งต่องานที่ชัดขึ้น เริ่มจาก [[intent-md|`intent.md`]] ที่ originator ตรวจเอง แล้วไป `spec.md`, `plan.md`, diff กับ test, PR กับ review findings และ incident record ทั้งชุดเรียกว่า [[artifact-chain|artifact chain]]

Artifact แต่ละชิ้นส่ง context ให้ agent หรือคนในช่วงถัดไป พร้อมเก็บ audit trail ว่าใครขอ ตัดสิน แก้ และอนุมัติอะไร ถ้าทีมพร้อมทำ automation ก็ใช้ commit ที่รับ artifact เป็น trigger เริ่มช่วงถัดไปได้

คนยังต้องอนุมัติ intent, spec, plan และ production gate ตามระดับความเสี่ยง ส่วน monitoring อัตโนมัติเริ่มจาก deterministic control band แล้วค่อยให้ agent ทำงานผ่าน route ที่อนุมัติไว้ เช่นเปิด PR หรือเรียก rollback runbook

**ผลคือ:** ระบบทำงานอัตโนมัติระหว่าง gate ได้ ส่วนคนเก็บแรงไว้ตัดสินใจในจุดที่ต้องรับผิดชอบ

[[ai-native-sdlc-playbook|The AI-Native SDLC Playbook]] ลงรายละเอียดมากกว่าที่คลิปเล่าอยู่สามเรื่อง เรื่องแรกคือชั้นควบคุมสามระดับ: skills ใช้แนะนำ hooks ใช้บังคับ และ managed settings ป้องกันไม่ให้ปลายทางแก้เอง ดู [[policy-as-code-for-agents]] เรื่องที่สองคือช่วง Maintain ต้องตรวจจับความผิดปกติโดยไม่ใช้ model แล้วค่อยเพิ่มสิทธิ์ตามระดับความเบี่ยง ดู [[control-bands]] เรื่องสุดท้ายคือตัววัด leading/lagging ของแต่ละช่วง ซึ่งหลายตัวดึงจาก git กับ PR metadata ได้ทันที

## วาง Verification ไว้กลางวงรอบ

SDLC แบบนี้ไม่รอให้ "เขียนเสร็จ" แล้วค่อยโยนให้ QA Test กับ eval บอก agent ระหว่างทำว่างานผ่านเกณฑ์หรือยัง ถ้ายังไม่ผ่านก็ส่ง failure กลับเข้า loop

- **Test:** เหมาะกับพฤติกรรม deterministic เช่น input นี้ต้องได้ output นี้
- **Output eval:** ดูว่าผลสุดท้ายตรง rubric หรือไม่
- **Trajectory eval:** ดูว่า agent ใช้ tool, permission และ check ตามขั้นที่ควรหรือไม่
- **Production monitoring:** หา failure class ใหม่แล้วเติมกลับเข้า regression suite

วิธีนี้เชื่อมกับ [[evals-and-error-analysis]]: รันชุดวัด อ่านเคสที่พัง จัดกลุ่มสาเหตุ แก้ prompt/tool/context แล้วรันซ้ำ ถ้าไม่มีวงรอบนี้ demo ที่สำเร็จครั้งเดียวก็ยังไม่ใช่หลักฐานว่า workflow เชื่อถือได้

**ผลคือ:** verification เกิดตลอดทาง agent จึงแก้งานตัวเองได้ก่อนส่งต่อ โดยยังมีเกณฑ์วัดคุมอยู่

## Spec สำคัญขึ้น แต่ยังพิสูจน์อะไรเองไม่ได้

เมื่อ implementation ใช้แรงน้อยลง ทีมยังต้องคิดเรื่อง scope, constraint, edge case และ tradeoff ทาง architecture เหมือนเดิม specification quality จึงสำคัญขึ้น และวิธีทำงานเริ่มคล้าย [[spec-driven-development|Spec-Driven Development]]

แต่สองเรื่องนี้ทำหน้าที่ไม่เหมือนกัน Spec ช่วยบอก intent และส่งต่องาน ส่วน test, schema, type และ production invariant เป็น executable fact ที่เครื่องตรวจเองได้ Prose spec ยังตีความคลาดเคลื่อนได้ และใช้แทน business judgement ไม่ได้

**ได้อะไร:** ใช้ spec เพื่อทำ intent ให้เห็นชัด แล้วใช้ verifier พิสูจน์ว่าสิ่งที่สร้างตรงกับ intent จริง

## Harness กับ context เป็นโครงพื้นฐานของ lifecycle

ตัว model ไม่ได้ขับ lifecycle คนเดียว [[coding-harness|Harness]] เป็นผู้จัด tool, sandbox, hook, memory, orchestration และ observability ส่วน [[context-engineering|context engineering]] เลือกว่ากฎหรือความรู้ใดต้องโหลดทุกครั้ง และอะไรค่อยดึงมาเมื่อ task ต้องใช้

เส้นแบ่งนี้กระทบสามอย่างพร้อมกัน:

1. **คุณภาพ:** context ขาดทำให้ agent เดา แต่ context ล้นทำให้ signal จมหาย
2. **ความปลอดภัย:** core guardrail บางข้อควรอยู่ตลอด ขณะที่ tool เฉพาะงานเปิดเมื่อจำเป็น
3. **ต้นทุน:** static context จ่ายซ้ำทุก call ส่วน dynamic context ต้องลงทุนใน trigger กับ retrieval

**ผลคือ:** SDLC แบบใหม่ต้อง version context policy และ harness เหมือน code ไม่ใช่เก็บเป็น prompt ส่วนตัวของใครคนหนึ่ง

## เลือกวิธีทำตามความเสี่ยงของงาน

งานทุกชิ้นไม่ต้องใช้ ceremony เท่ากัน Prototype ที่ทิ้งได้อาจยอมรับการลองแล้วดู ส่วนระบบ production ที่แตะข้อมูลหรือเงินต้องมี spec, automated checks, eval, permission gate และ human review

คำถามตัดสินแบบสั้น:

- ถ้าพัง ใครเสียหายและย้อนกลับได้ไหม
- Code ต้องอยู่กี่วัน และใครต้อง maintain ต่อ
- มี verifier ที่รันซ้ำได้หรือยัง
- Agent เห็น context ทางธุรกิจที่จำเป็นครบหรือไม่
- เวลาตรวจและแก้งานถูกนับในต้นทุนแล้วหรือยัง

**ได้อะไร:** เส้นแบ่งระหว่าง [[vibe-coding]] กับ [[agentic-engineering]] อยู่ที่ผลเสียเมื่อพังและหลักฐานที่ต้องมี ไม่ได้อยู่ที่ชื่อ tool หรือ model

## ข้อจำกัดและคำถามเปิด

- Productivity ขึ้นกับชนิดงาน ประสบการณ์คน และ harness; งานบางชุดเร็วขึ้น ขณะที่บางชุดช้าลงเมื่อรวม review/rework
- การเร่ง implementation อาจสร้างคิวหน้า review และเพิ่ม [[orchestration-tax]] ถ้า verification ไม่โตตาม
- "Prototype กลายเป็น production agent โดยไม่ rewrite" จะจริงแค่ไหนขึ้นกับ permission, data governance, observability และ runtime ที่ prototype ไม่มี
- Agent อาจทำ 80% แรกเร็ว แต่ 20% ท้ายยังติด edge case และรอยต่อระหว่างระบบ
- การวัด trajectory อาจเพิ่มความปลอดภัย แต่ก็เสี่ยงกลายเป็น process theater ถ้า rubric ไม่โยงกับผลจริง
- Artifact chain อาจลด handoff loss แต่เพิ่ม ceremony และ drift ถ้า `intent.md`, `spec.md`, `plan.md` กับ code ไม่มี owner คอย sync
- คำว่า autonomous maintenance ต้องอ่านเป็น gated autonomy ต้นทางยังวาง deterministic trigger, permission tier, PR gate และ human triage ไว้

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
- [[ai-native-sdlc-playbook]]
- [[claude-codes-new-intent-md-rob-shocks]]
- [[intent-md]]
- [[artifact-chain]]
- [[control-bands]]
- [[policy-as-code-for-agents]]
