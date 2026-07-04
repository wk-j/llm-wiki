---
title: Stop Building AI Agents the Old Way
type: source
tags: [ai, agents, long-running, observability, harness, memory]
url: "https://www.youtube.com/watch?v=ju7R6jer6_M"
author: "Prompt Engineering"
created: 2026-07-04
updated: 2026-07-04
sources: [stop-building-ai-agents-old-way.md]
---

# Stop Building AI Agents the Old Way / เลิกสร้าง AI agent แบบเดิม

วิดีโอของ [[prompt-engineering|Prompt Engineering]] (ช่อง YouTube ที่อธิบายงาน AI engineering) เสนอวิธีออกแบบ [[long-running-agents|long-running agents]] ที่รันได้นานเป็นชั่วโมงหรือเป็นวันโดยไม่หลุดทาง. แกนของคลิปคือ agent ตัวหลักเป็นแค่ executor. ความน่าเชื่อถือเกิดจากระบบรอบตัวมัน: goal, evaluator, verifier, loop, orchestration, observability, และ memory.

คลิปนี้อยู่ใกล้ [[loop-engineering|loop engineering]] และ [[harness-guides-sensors|harness guides & sensors]] มาก แต่เล่าเป็นสูตรสำหรับคนสร้าง agent product. จุดที่เพิ่มเข้ามาชัดคือ [[agent-observability|agent observability]] ผ่าน dashboard/trace และ [[session-mining|session mining]] ที่เปลี่ยน failure จาก run เก่าให้เป็น rule ของ run ต่อไป.

## ใจความสำคัญ

- long-running agent ไม่ควรถูกปล่อยให้ "คิดยาว ๆ" ตามลำพัง แต่ควรถูกวางในระบบที่ให้มันลองสั้น ๆ, ตรวจ, แก้, และวนใหม่
- goal ต้องเป็น contract: มี end state, success criteria, constraint, และ budget ที่วัดได้
- evaluator / judge ต้องแยกจาก agent ที่ลงมือทำ เพื่อไม่ให้ตัวทำงานให้เกรดตัวเอง
- verifier คือหลักฐาน ไม่ใช่คำอธิบายของ agent: เริ่มจาก test/type/lint แล้วค่อยเสริม benchmark, screenshot comparison, held-out eval หรือ agent review
- outer loop กัน early stopping: ถ้ายังไม่ผ่าน goal ก็ส่ง failure กลับเข้า agent พร้อมให้วางแผนใหม่หรือส่งต่อให้คน
- orchestration ควรคิดเป็น roles มากกว่า model เดียวทำทุกอย่าง: model แข็งสำหรับ planning, model ถูก/เร็วสำหรับ execution, model ที่ตัดสินดีสำหรับ evaluation
- observability เป็นหน้าควบคุมระหว่าง run ไม่ใช่ report หลังจบ: ต้องเห็น task, cost, latency, error, screenshot, key decision และให้ feedback ได้
- memory แบบ session mining เอา run เก่ามาหา pattern ของ failure แล้วเขียนกลับเป็น rule / config / `AGENTS.md` / `prompt.md`

## 7 components ของ long-running agent

คลิปเสนอว่าสิ่งที่ทำให้ agent รันยาวได้ไม่ใช่ agent ตัวเดียว แต่เป็น 7 component รอบตัวมัน:

| Component | ทำอะไร | หน้าใน wiki |
|---|---|---|
| Goal | end state + success criteria + constraint + budget | [[delegation-mindset]] |
| Evaluator | judge ที่ดู spec กับ output โดยไม่ใช้ context เดียวกับ executor | [[subagent-patterns]] |
| Verifiers | test/type/lint + eval ที่แพงขึ้นตามความเสี่ยง | [[verifiability]] |
| Outer loop | เช็ค progress เทียบ goal แล้ววนกลับถ้ายังไม่ผ่าน | [[loop-engineering]] |
| Orchestration | แยก planning / execution / evaluation ตาม role และ cost | [[model-choice-by-expertise]] |
| Observability | trace, dashboard, issue view, พื้นที่รับ feedback | [[agent-observability]] |
| Memory | mine run เก่าเป็น rule และ procedural knowledge | [[session-mining]] |

**ผลคือ:** agent ที่ดู autonomous จริง ๆ คือระบบควบคุมที่ประกอบจากหลายชิ้น ไม่ใช่ model ที่ฉลาดขึ้นอย่างเดียว.

## Goal เป็น contract ไม่ใช่ prompt ยาว

คลิปย้ำว่า goal ที่ดีไม่ได้บอก step-by-step แต่บอกว่าจบแล้วควรเป็นอย่างไร. ตัวอย่างเช่น "เพิ่มหน้า settings" กว้างเกินไป เพราะ agent อาจสร้าง UI แล้วประกาศเสร็จทั้งที่ save ไม่ครบหรือ test พัง. ถ้า goal เปลี่ยนเป็น match design, save every setting, pass this test งานจะมีเกณฑ์วัด.

ตรงนี้ต่อกับ [[delegation-mindset|delegation mindset]]: เราไม่ micromanage agent ทุก step แต่ต้องให้ intent, constraint, และหลักฐานว่า done คืออะไรให้ครบตั้งแต่ต้น.

**ได้อะไร:** ถ้าคนยังนิยาม success criteria ไม่ชัด agent จะเติมช่องว่างเอง และส่วนที่เติมมักไม่ตรงกับเจตนา.

## Evaluator ต้องแยกจาก executor

คลิปวาง maker/checker split แบบตรงไปตรงมา: agent ที่เขียนงานไม่ควรเป็นคนให้เกรดงานนั้นเอง. evaluator ควรเห็น initial spec กับ final output แล้วตัดสิน ไม่แชร์ context เดียวกับ executor เพราะ context เดียวกันทำให้ bias ตามเหตุผลที่ executor สร้างไว้.

ถ้า outcome ชัด ใช้ deterministic check เช่น test, type, lint. ถ้า outcome fuzzy เช่นเขียนดีไหมหรือ UI ดูถูกไหม ค่อยใช้ agent judge ทับบน baseline ที่ตรวจได้.

จุดนี้เหมือน [[loop-engineering|loop engineering]] และ [[agentic-code-review|agentic code review]]: AI reviewer มีประโยชน์ในฐานะ inferential sensor แต่ไม่ควรเป็นด่านเดียวสำหรับงานที่มีผลเสียสูง.

## Verifier คือ proof ไม่ใช่คำกล่าวอ้าง

คลิปแยก verifier เป็นสองชั้น:

- ชั้นถูกและ deterministic: compile, test, type, lint
- ชั้นแพงกว่า: benchmark, screenshot comparison, held-out eval, agent review

แกนสำคัญคือ "เสร็จแล้ว" ต้องผ่าน check ไม่ใช่แค่ agent อธิบายว่าทำเสร็จแล้ว. นี่ต่อกับ [[facts-first|facts-first]] และ [[harness-guides-sensors]] ตรง ๆ: test/fact เป็น sensor แบบ computational ส่วน agent review เป็น sensor แบบ inferential ที่ช่วยเติมความหมายแต่ไม่แน่นอนเท่า.

**ได้อะไร:** long-running agent ที่ไม่มี verifier ชัดคือ agent ที่อาจทำงานยาวขึ้น แต่ไม่ได้น่าเชื่อถือขึ้น.

## Outer loop ไม่ใช่ให้คิดยาว แต่ให้ลองสั้นซ้ำ

คลิปอธิบาย outer loop เป็นกลไกควบคุมที่ปลุก agent ขึ้นมาเช็ค progress เทียบ goal. ถ้าผ่านก็ปิดงานว่าเสร็จ. ถ้าไม่ผ่านก็ส่ง failure กลับไปให้ทำใหม่. เวอร์ชันที่ดีกว่านั้นมี evaluator ใน loop ที่ช่วยวางแผนใหม่และส่งต่อให้คนเมื่อจำเป็น.

มุมนี้ใกล้ `/goal` ใน [[claude-code|Claude Code]] และ [[openai-codex|Codex]]: ไม่ใช่ให้ model คิดยาว ๆ รอบเดียว แต่ให้ทำ attempt สั้น ๆ ที่มี check คุม แล้วค่อย refine.

## Observability เป็นหน้าควบคุม

คลิปบอกว่าพอ agent รันเป็นชั่วโมง คนไม่ควรต้องนั่งอ่าน raw transcript ทั้งหมด. ระบบควรแยก raw logs/data ออกจาก presentation แล้วทำ dashboard ที่เห็น task, cost, error, screenshot, และ key decision ได้เร็ว.

ช่วง sponsor แนะนำ [[latitude|Latitude]] เป็น open-source agent observability tool ที่ trace cost, latency, span tree, search trace ด้วยภาษาธรรมชาติ, cluster conversation, รวม repeated failures เป็น issue, สร้าง eval จาก failure, save search เป็น monitor, และดึง failing trace กลับเข้า editor ผ่าน [[model-context-protocol|MCP server]] ได้. ข้อมูลนี้มาจากช่วง sponsor ในคลิป จึงควรอ่านเป็น product claim ของ source จนกว่าจะตรวจ repo/เอกสารโดยตรง.

**ผลคือ:** observability ไม่ใช่ของไว้ดูย้อนหลังอย่างเดียว แต่เป็นจุดที่คนตัดสินใจว่าจะ step in ตรงไหน.

## Memory ผ่าน session mining

คลิปเสนอว่า past agent runs คือ training data ฟรีที่คนมักทิ้ง. วิธีใช้คือกลับไปดู run ล่าสุด ๆ หา pattern เช่น failed checks ซ้ำ, wrong path ซ้ำ, หรือ shortcut ซ้ำ แล้วเขียนผลเรียนรู้กลับเป็น rule ใน project instruction, agent config, `AGENTS.md`, หรือ `prompt.md`.

นี่คือเวอร์ชันใช้ง่ายของ [[harness-ratchet|harness ratchet]]: failure เดิมไม่ควรถูกแก้ด้วยการบอก agent รอบเดียว แต่ควรถูกแปลงเป็น rule, check, หรือ memory ที่ run ถัดไปอ่านได้.

**ข้อควรระวัง:** rule ที่เพิ่มควรมาจาก failure จริงและควรถอดได้ ไม่อย่างนั้น memory จะกลายเป็น policy เก่าที่เพิ่ม context cost และอาจสร้าง [[memory-drift|memory drift]].

## เมื่อเทียบกับกรอบเดิมใน wiki

คลิปนี้ไม่ลบงานของ [[addy-osmani|Addy Osmani]], [[birgitta-bockeler|Birgitta Böckeler]], หรือ [[matt-pocock|Matt Pocock]]. มันสรุปภาพเดียวกันด้วยภาษาภาคปฏิบัติ:

- กับ [[long-running-agents]]: Google พูด pattern ระดับ platform เช่น checkpoint/resume, HITL, memory governance, fleet orchestration. คลิปนี้พูดชุด control ที่เริ่มใช้ได้กับ agent loop เล็กกว่า.
- กับ [[loop-engineering]]: Addy พูดการออกแบบ loop ที่ prompt agent แทนเรา. คลิปนี้แจก component ของ loop นั้น โดยเน้น goal/evaluator/verifier/observability/memory.
- กับ [[orchestration-tax]]: dashboard และ role orchestration ไม่ได้ทำให้ human judgement หายไป แต่ช่วยให้คนเห็นจุดที่ควรใช้ judgement แทนการอ่าน transcript ทั้งหมด.
- กับ [[harness-guides-sensors]]: goal เป็น guide, verifier/evaluator/observability เป็น sensor, session mining คือ steering loop ที่เอา failure กลับมาแก้ harness.

## Open questions

- Latitude ทำได้ครบตามที่ sponsor claim แค่ไหนใน repo open-source จริง และ feature ไหนอยู่ใน hosted product
- evaluator ที่ไม่แชร์ context กับ executor จะพอเข้าใจงานซับซ้อนได้ไหม หรือต้องมีสรุปกลางที่ออกแบบเฉพาะ
- agent review ที่เป็น judge ควรใช้ model เดียวกัน ต่าง model หรือหลาย reviewer เพื่อกัน bias
- session mining ควรเลือก rule แบบไหนให้คุ้มกับ instruction budget และไม่ทำให้ memory drift
- dashboard แบบไหนลด [[orchestration-tax|orchestration tax]] จริง แทนที่จะเพิ่มอีกหน้าที่คนต้องเฝ้า

## See also

- [[long-running-agents]]
- [[loop-engineering]]
- [[harness-guides-sensors]]
- [[agent-observability]]
- [[session-mining]]
- [[latitude]]
- [[prompt-engineering]]
- [[harness-ratchet]]
- [[orchestration-tax]]
- [[verifiability]]
- [[facts-first]]
- [[subagent-patterns]]
