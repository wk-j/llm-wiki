---
title: mikelopster
type: entity
tags: [creator, software, ai, youtube, thai]
created: 2026-06-28
updated: 2026-06-28
sources: ["รู้จักกับ Loop Engineering — mikelopster transcript"]
---

# mikelopster

[[mikelopster]] เป็น creator ไทยสาย software engineering และ AI. ในวิกินี้อ้างถึงจากวิดีโอ [[mikelopster-loop-engineering|รู้จักกับ Loop Engineering]] ซึ่งเล่า [[loop-engineering|Loop Engineering]] แบบคนลองใช้จริงกับ [[claude-code|Claude Code]] และ [[openai-codex|Codex]].

## มุมที่สำคัญกับวิกินี้

mikelopster ไม่ได้ขายคำว่า loop แบบ hype ล้วน ๆ. เขาเล่าว่าคอนเซปต์ดูดี แต่พอลองจริงกลับเจอคำถามว่า "จะใช้กับอะไรดี" เพราะหลายงานที่เหมือนควรเป็น loop กลับซ้ำกับ workflow agent เดิม หรือสุดท้ายยังต้องให้คน review.

มุมที่เขาเติมให้หน้า [[loop-engineering]] คือ **feedback gate**. ลูปจะดีหรือไม่ดีอยู่ที่นิยามจุดผ่าน/ไม่ผ่าน. ถ้า gate ไม่ชัด agent จะวนจนเผา token. ถ้า gate หลวมไป งานดูเหมือนผ่านแต่คนต้องมาแก้ซ้ำ.

อีกมุมคือการแยกงานที่เหมาะกับ loop ออกจากงานที่ยังไม่เหมาะ. งาน test/lint/CI/coverage มี scorer ชัด. แต่งาน content, taste, UI "ให้สวยขึ้น", หรือ production/security ที่พลาดไม่ได้ ยังต้องระวัง เพราะคอขวดอยู่ที่ judgement ของคน ดู [[orchestration-tax]].

> ได้อะไร: mikelopster ทำให้ loop engineering ดูเป็นเรื่องปฏิบัติ ไม่ใช่แค่คำใหม่. ก่อนสร้าง loop ต้องถามว่า "วัดจบยังไง" และ "ใครต้องตรวจ output สุดท้าย".

## See also

- [[mikelopster-loop-engineering]]
- [[loop-engineering]]
- [[orchestration-tax]]
- [[claude-code]]
- [[openai-codex]]
