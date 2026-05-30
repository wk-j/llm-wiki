---
title: Effort Levels
type: concept
tags: [ai, claude, claude-code, performance, cost-optimization]
created: 2026-04-16
updated: 2026-05-29
sources: [Introducing Claude Opus 4.7.md, Whats new in Claude Opus 4.7 - Anthropic Docs.md, Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6.md, Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md]
---

# Effort Levels / ระดับความพยายาม

พารามิเตอร์ที่ [[anthropic|Anthropic]] สร้างขึ้นมาเพื่อให้ผู้ใช้สามารถแลกเปลี่ยนระหว่าง **คุณภาพการให้เหตุผล (reasoning quality) กับ latency และค่า token** บนโมเดล [[claude|Claude]] ผู้เรียกใช้จะเลือกระดับ (tier) และโมเดลจะจัดสรรเวลาในการคิดให้ตามนั้น

## ระดับต่างๆ (ณ Opus 4.7)

| ระดับ | ตำแหน่ง | ควรใช้เมื่อไหร่ |
|---|---|---|
| `medium` | ต่ำ | งานง่ายๆ, ต้องการคำตอบเร็ว |
| `high` | กลาง-สูง | จุดเริ่มต้นที่แนะนำสำหรับงาน coding / agentic |
| **`xhigh`** | ใหม่ใน Opus 4.7 | การให้เหตุผลเพิ่มเติมสำหรับปัญหายากๆ; เป็นค่าเริ่มต้นใน [[claude-code\|Claude Code]] |
| `max` | สูงสุด | ปัญหาที่ยากที่สุด; latency และค่า token สูงสุด |

`xhigh` ถูกเพิ่มเข้ามาพร้อมกับ [[claude-opus-4-7|Opus 4.7]] เพื่อให้สามารถควบคุมระหว่าง `high` และ `max` ได้ละเอียดขึ้น

## การเปลี่ยนแปลงใน Opus 4.8 (2026-05-28)

[[claude-opus-4-8|Opus 4.8]] ปรับวิธีใช้ effort สองอย่าง:

- **ค่าเริ่มต้นกลับมาเป็น `high`** (ไม่ใช่ `xhigh` แบบที่ [[claude-code\|Claude Code]] ตั้งให้ 4.7) — Anthropic ประเมินว่า `high` คือจุดสมดุลที่ดีที่สุดระหว่างคุณภาพกับประสบการณ์ใช้งาน สำหรับงาน coding ระดับนี้ใช้ token พอๆ กับค่าเริ่มต้นของ 4.7 แต่ให้ผลดีกว่า
- **ชื่อ tier ใหม่ `extra`** = ระดับเดียวกับ `xhigh` ใน Claude Code — แนะนำให้ใช้ `extra` กับงานที่ยากและงานแบบ asynchronous ที่รันยาว ส่วน `max` ไว้สำหรับงานหนักสุด
- Claude Code **เพิ่ม rate limit** ให้แล้วเพื่อรองรับการใช้ token ที่มากขึ้นในระดับ effort สูง

**effort control บน UI:** Opus 4.8 เพิ่มปุ่มควบคุม effort ข้าง model selector บน **claude.ai และ Cowork** (เดิม effort เป็นพารามิเตอร์ API อย่างเดียว) — ตั้งสูง = Claude คิดบ่อยและลึกขึ้น, ตั้งต่ำ = ตอบเร็วขึ้นและกิน rate limit ช้าลง เปิดให้ทุกแพ็กเกจ

**คำกล่าวอ้างจากบุคคลที่สาม:** [[claude-opus-4-7-migration-pachaar|คู่มือการย้ายระบบของ Pachaar]] อธิบายว่ามี 5 ระดับ (เพิ่ม `low` เข้ามาต่ำกว่า `medium`) สำหรับ "งานที่ latency-sensitive และมีขอบเขตจำกัด" แต่เอกสารทางการของ Anthropic ระบุเพียง 4 ระดับข้างต้น ให้ถือว่า `low` ยังไม่ได้รับการยืนยันจนกว่า Anthropic จะยืนยัน

## การสลับ effort ระหว่างทำงาน

Effort ไม่ใช่ปุ่มที่ตั้งค่าครั้งเดียวแล้วจบ รูปแบบของ Pachaar คือ: **เพิ่มและลด effort ในแต่ละช่วงของงานเดียวกัน** เพื่อควบคุมการใช้ token

- `xhigh` สำหรับช่วงออกแบบ/วางแผน (การให้เหตุผลที่ยากที่สุด, การเลือกสถาปัตยกรรม)
- `high` สำหรับการ implement ที่ตรงไปตรงมาเมื่อมีแผนแล้ว
- `max` ชั่วครู่สำหรับช่วง debugging ที่ติดปัญหาหนักๆ แล้วค่อยลดกลับลงมา

Opus 4.7 เคารพ effort อย่างเคร่งครัดกว่า 4.6 — หาก `low`/`medium` รู้สึกว่าคิดน้อยเกินไป ให้เพิ่ม effort แทนที่จะเติม prompt ด้วยคำว่า "คิดให้หนักขึ้น"

**คำแนะนำสำหรับ Opus 4.7** (จากเอกสาร): เริ่มต้นด้วย `xhigh` สำหรับ use case ที่เป็น coding และ agentic; ใช้ขั้นต่ำ `high` สำหรับ use case ส่วนใหญ่ที่ต้องการความฉลาดสูง Messages API เท่านั้น — Claude Managed Agents จะเลือก effort โดยอัตโนมัติ

## ความสัมพันธ์กับ adaptive thinking

Effort ≠ thinking. [[adaptive-thinking|Adaptive thinking]] เป็นการตั้งค่าเปิด/ปิดและการแสดงผลที่แยกต่างหาก ซึ่งควบคุมว่าโมเดลได้รับอนุญาตให้คิดก่อนตอบหรือไม่ ใน 4.7, thinking จะปิดเป็นค่าเริ่มต้น — `effort` อย่างเดียวไม่สามารถเปิดมันได้; ผู้เรียกใช้ต้องส่ง `thinking: {type: "adaptive"}` อย่างชัดเจน

## ผลกระทบต่อการใช้ token

Effort ที่สูงขึ้นหมายถึงการคิดที่มากขึ้น — โดยเฉพาะใน turn หลังๆ ของการตั้งค่าแบบ agentic เมื่อรวมกับ tokenizer ที่อัปเดตของ [[claude-opus-4-7|Opus 4.7]] (input เดียวกันใช้ token มากขึ้น 1.0–1.35 เท่า) การย้ายระบบจำเป็นต้องมีการวัดผลจากการใช้งานจริง การประเมินผล coding ภายในของ Anthropic แสดงให้เห็นว่า tokens-per-result โดยรวมดีขึ้นในทุกระดับ effort หลังจากการอัปเกรด

## การควบคุมค่าใช้จ่าย

- ลด effort สำหรับงานที่ง่ายกว่า
- **[[task-budgets|Task budgets]]** (API, public beta) — เพดานการใช้ token ต่อการรันหนึ่งครั้ง
- Prompt ให้โมเดลตอบให้กระชับขึ้น
- ใช้ [[advisor-strategy]] — ให้ executor ทำงานที่ effort ไม่สูงมาก และ escalate ไปหา Opus advisor เฉพาะเมื่อเจอการตัดสินใจที่ยาก

## ดูเพิ่ม

- [[claude-opus-4-8]]
- [[claude-opus-4-7]]
- [[claude-code]]
- [[adaptive-thinking]]
- [[task-budgets]]
- [[advisor-strategy]]
- [[claude-code-session-management]]
