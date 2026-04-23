---
title: Advisor Strategy
type: concept
tags: [ai, agents, cost-optimization, architecture]
created: 2026-04-16
updated: 2026-04-23
sources: [advisor-strategy.md, Introducing Claude Opus 4.7.md, alex-ker-harnesses-optimize.md]
---

# Advisor Strategy

สถาปัตยกรรมของ agent ที่ให้ **โมเดลที่ถูกและเร็วกว่า** (the executor) ขับเคลื่อนงานตั้งแต่ต้นจนจบ และจะขอความช่วยเหลือจาก **โมเดลที่เก่งและแพงกว่า** (the advisor) เฉพาะเมื่อเจอจุดตัดสินใจที่ตัวเองแก้ไม่ได้เท่านั้น advisor จะให้แผน, การแก้ไข, หรือสัญญาณให้หยุด แต่จะไม่เรียก tool หรือสร้างผลลัพธ์ให้ผู้ใช้โดยตรง

## แตกต่างจาก orchestrator-worker อย่างไร

รูปแบบ [[ai-orchestrator|orchestrator-worker]] แบบดั้งเดิมจะใช้โมเดลขนาดใหญ่เพื่อแตกงานและมอบหมายงานย่อยให้ worker ที่เล็กกว่า แต่ advisor strategy จะกลับด้านกัน:

| | Orchestrator-worker | Advisor strategy |
|---|---|---|
| **ใครขับเคลื่อน** | โมเดลใหญ่ | โมเดลเล็ก |
| **ใครเรียก tool** | Workers (เล็ก) | Executor (เล็ก) |
| **บทบาทของโมเดลใหญ่** | แตกงาน, มอบหมาย, รวมผล | ให้คำแนะนำเมื่อถูกเรียก |
| **โมเดลใหญ่ทำงานเมื่อไหร่** | ทุกขั้นตอน | เฉพาะเมื่อมีการ escalate |
| **โปรไฟล์ค่าใช้จ่าย** | สูง (โมเดลใหญ่ทำงานตลอด) | ต่ำ (โมเดลใหญ่ทำงานเป็นครั้งคราว) |

executor จะหลีกเลี่ยง overhead ของการแตกงาน, การจัดการ worker pool, และ logic การควบคุม (orchestration) การใช้เหตุผลระดับ frontier จะเกิดขึ้นเมื่อจำเป็นเท่านั้น

## ทำไมถึงถูกกว่าการใช้ executor เพียงอย่างเดียวได้

อาจจะดูขัดกับสัญชาตญาณ แต่การเพิ่ม advisor ที่แพงกว่าเข้ามาอาจ*ลด*ค่าใช้จ่ายโดยรวมได้ คำแนะนำสั้นๆ (400–700 tokens) ของ advisor สามารถชี้นำ executor ให้ออกจาก tool loop ที่ไม่มีทางออกซึ่งอาจจะเผาผลาญ turn ของ executor ไปหลายรอบได้

## ควรใช้เมื่อไหร่

- Agentic workload ที่มีปริมาณสูง ซึ่งค่าใช้จ่ายเป็นเรื่องสำคัญแต่คุณภาพต้องไม่ต่ำกว่าเกณฑ์
- งานที่ executor สามารถตัดสินใจเองได้ 80%+ อย่างมีประสิทธิภาพ — advisor จะเข้ามาช่วยใน 20% ที่ยาก
- สถานการณ์ที่ latency ของการรัน Opus แบบเต็มๆ เป็นสิ่งที่ยอมรับไม่ได้ แต่การปรึกษา Opus เป็นครั้งคราวยังพอรับได้

## การรองรับใน API

[[anthropic|Anthropic]] ได้เพิ่ม `advisor_20260301` tool type เข้ามาใน Messages API โมเดล executor จะตัดสินใจเองว่าจะเรียกใช้เมื่อไหร่; การส่งมอบงานจะเกิดขึ้นภายในการเรียก API เพียงครั้งเดียว

ด้วย [[claude-opus-4-7|Opus 4.7]] (เปิดตัว 16 เม.ย. 2026), advisor model โดยธรรมชาติได้อัปเกรดจาก `claude-opus-4-6` เป็น `claude-opus-4-7` — โดยมี API shape และราคาเท่าเดิม ในฝั่ง executor, Sonnet 4.6 และ Haiku 4.5 ยังคงเป็นตัวเลือกที่นิยมใช้

## Advisor ในฐานะผู้พิพากษาของ pipeline

จุดที่เหมาะสมในการนำ advisor เข้ามาใน [[subagent-patterns|subagent pipeline]] คือในขั้นตอนการรวบรวมสุดท้าย: subagent สามหรือสี่ตัวใน parallel fan-out จะส่ง summary กลับมา; advisor ระดับ frontier จะรวบรวม summary เหล่านั้นเป็นคำตอบสุดท้าย [[alex-ker|Alex Ker]] (18 เม.ย. 2026) ได้กล่าวถึงรูปแบบนี้อย่างชัดเจน — "คุณสามารถใช้ frontier model เป็นผู้พิพากษาเพื่อรวบรวมคำตอบและรับประกันว่าจะได้พฤติกรรมที่ต้องการด้วยความมั่นใจที่สูงขึ้น" โครงสร้างที่ executor ขับเคลื่อน / advisor ช่วยในขั้นตอนที่ยากยังคงเดิม; แค่ advisor ถูกเรียกใช้ตอนสังเคราะห์ผลลัพธ์แทนที่จะเป็นระหว่างทำงาน

## ดูเพิ่ม

- [[ai-orchestrator]]
- [[harness-engineering]]
- [[coding-harness]]
- [[subagent-patterns]]
- [[llm-coding-pitfalls]]
- [[model-context-protocol]]
- [[claude-opus-4-7]]
- [[effort-levels]]
