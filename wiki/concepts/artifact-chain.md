---
title: Artifact Chain
type: concept
tags: [ai, software-engineering, sdlc, artifacts, handoff, governance]
created: 2026-09-09
updated: 2026-09-14
sources: [claude-codes-new-intent-md-rob-shocks.md, ai-native-sdlc-playbook.md]
---

# Artifact Chain / ส่งต่องานด้วย artifact

**Artifact chain** คือการให้แต่ละช่วงเขียนผลลัพธ์ไว้ เพื่อให้ช่วงถัดไปอ่านต่อได้ ใน AI-Native SDLC ที่ [[rob-shocks|Rob Shocks]] อธิบาย แต่ละ agent ไม่จำเป็นต้องมี conversation history ชุดเดียวกัน เจตนา การตัดสินใจ และหลักฐานจึงส่งต่อผ่านไฟล์กับ record ที่เก็บ version

`intent.md → spec.md → plan.md → diff + tests → PR + review findings → incident record`

ชิ้นแรกตอบว่าอยากเปลี่ยนอะไรและเพราะอะไร ชิ้นถัดมาตัดสิน requirement กับ design แล้วแผนจึงบอกวิธีลงมือ Code กับ test เป็นทั้งผลงานและหลักฐาน ส่วน PR กับ incident record เก็บผลการตรวจ การอนุมัติ และสิ่งที่เกิดขึ้นหลัง deploy

**ได้อะไร:** session ใหม่เริ่มงานต่อได้โดยไม่ต้องอาศัยความจำของ agent ตัวก่อน และ Git history บอกได้ว่าใครสร้าง แก้ หรืออนุมัติอะไร

## ใช้ทั้งส่งต่องานและตรวจย้อนหลัง

ในฐานะ **handoff protocol** chain บอกผู้รับว่าต้องอ่านอะไรและส่งอะไรต่อ ในฐานะ **audit trail** ทีมใช้ย้อนจาก incident ไปหา diff, plan, spec และ intent ได้

Chain จะทำสองหน้าที่นี้ได้ก็ต่อเมื่อ artifact มี owner, status, timestamp และลิงก์ถึงกัน ถ้ามีเพียงไฟล์ที่ตั้งชื่อถูกแต่ไม่มีเกณฑ์รับช่วงต่อ ก็ยังใช้งานจริงไม่ได้

**ผลคือ:** เอกสารมีค่าเพราะเชื่อมการตัดสินใจกับงานจริง ไม่ใช่เพราะจำนวนไฟล์

## จุดพังที่พบบ่อย

- **Drift:** code เปลี่ยนแต่ `plan.md` ไม่เปลี่ยน หรือ spec เปลี่ยนแต่ intent ยังเล่าโจทย์เก่า
- **Dual source of truth:** Jira กับ repo ต่างฝ่ายต่างอ้างว่าเป็นข้อมูลจริง แล้วไม่มี record ID หรือ commit SHA เชื่อมกัน
- **False completeness:** แผนอ่านครบแต่ยังข้าม assumption สำคัญ ดู [[plan-mode-as-prompting]]
- **Review queue:** agent สร้าง artifact เร็วกว่าคนอนุมัติ จน gate กลายเป็นคอขวดใหม่
- **Ceremony tax:** งานเล็กต้องแก้ Markdown หลายชิ้นจนช้ากว่าการแก้และทดสอบตรง ๆ

Hooks ช่วยบังคับกฎเชิงกลได้ เช่นห้าม merge เมื่อ plan กับ diff ไม่ sync แต่ hook ตัดสินแทนคนไม่ได้ว่า requirement ยังตอบปัญหาจริงหรือไม่

## ไม่เท่ากับ chain of command

Artifact chain บอกลำดับของข้อมูล ไม่ได้บังคับว่า Plan, Design, Build และ Test ต้องเป็น waterfall ทีมย้อนแก้ชิ้นก่อนหน้าได้ และบางช่วงทำขนานกันได้ ตราบใดที่แก้ artifact อื่นที่พึ่งข้อมูลนั้นตามไปด้วย

แนวคิดนี้จึงเชื่อม [[spec-driven-development|SDD]] กับ [[facts-first]] เข้าด้วยกัน Prose เก็บเหตุผลและ decision ส่วน test, schema และ telemetry เก็บสิ่งที่เครื่องตรวจได้

**ผลคือ:** chain ที่ดีรักษาทั้งบริบทของคนและหลักฐานจากระบบ โดยไม่ยกไฟล์ชนิดเดียวเป็น source of truth ของทุกอย่าง

## วัดได้ว่า chain ยังมีชีวิตหรือกลายเป็นพิธีกรรม

เมื่อ artifact อยู่ใน git ทีมก็ดึงตัววัดจาก timestamp กับ PR metadata ได้โดยไม่ต้องให้ใครกรอกฟอร์ม [[ai-native-sdlc-playbook|Playbook ของ Anthropic]] เสนอตัววัดไว้สี่อย่าง

- **survival rate ของ intent:** สัดส่วน `intent.md` ที่ product owner รับเข้าช่วงถัดไป
- **เวลาระหว่าง commit ของ intent กับ spec:** บอกว่าช่วง Design ยังติดอะไรอยู่ไหม
- **จำนวน commit `spec.md` ที่เกิดหลัง `plan.md` แรกของงานเดียวกัน:** ใช้วัด requirement rework
- **ความถี่ที่ diff ที่ merge แล้วตรงกับ `plan.md`:** ใช้จับ drift ซึ่งเป็นจุดพังหลักของ chain

ตัววัดอาจกดดันให้คนทำตัวเลขให้สวย survival rate จะสูงขึ้นทันทีถ้า product owner รับทุกไฟล์ จึงควรใช้ดูแนวโน้ม ไม่ใช่ตั้งเป็น target ของทีม

**ได้อะไร:** ทีมตอบได้ด้วยหลักฐานว่า chain ช่วยงานจริง หรือแค่เพิ่มไฟล์ให้แก้

## See also

- [[ai-native-sdlc-playbook]]
- [[claude-codes-new-intent-md-rob-shocks]]
- [[intent-md]]
- [[ai-driven-sdlc]]
- [[spec-driven-development]]
- [[facts-first]]
- [[agentic-code-review]]
- [[evals-and-error-analysis]]
- [[intent-gap]]
