---
title: Simon Willison
type: entity
tags: [people, engineering]
created: 2026-05-05
updated: 2026-09-24
sources: [agentic-coding-trap.md, How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md, fables-judgement-simon-willison.md, teepagorn-claude-code-adoption-nobody-reading.md]
---

# Simon Willison

**Simon Willison** เป็นนักพัฒนาซอฟต์แวร์ระดับซีเนียร์ (ประสบการณ์เกือบ 30 ปี) และเป็นผู้สร้าง Datasette รวมถึงเป็นผู้บุกเบิกเทคโนโลยี web หลายตัว

เขาเป็นหนึ่งในคนที่ออกมาพูดถึงปัญหา [[cognitive-debt]] อย่างชัดเจน โดยแชร์ประสบการณ์ว่าแม้แต่คนที่มีประสบการณ์สูง เมื่อใช้งาน AI ช่วยเขียนโค้ดมากๆ ก็ยังทำให้ภาพจำหรือ mental model ของแอปพลิเคชันในหัวเริ่มเลือนลาง ทำให้การเพิ่มฟีเจอร์ใหม่ๆ ยากขึ้น เพราะไม่ได้ลงไปลุยเขียนด้วยตัวเองเหมือนแต่ก่อน

[[zack-proser|Zack Proser]] ยก Simon ใน [[how-to-keep-shipping-away-from-desk|talk เรื่องการทำงานกับ agent โดยไม่หมดแรง]] ว่า Simon เปิด agent ขนานสี่ตัวแล้วหมดแรงก่อน 11 โมง. ตัวอย่างนี้ชี้อีกด้านของปัญหาเดียวกัน: ต่อให้ agent เพิ่ม throughput ได้ แต่ attention และ judgement ของคนยังเป็นคอขวด ดู [[orchestration-tax]] และ [[developer-balance]].

## Fable's judgement (2026-07)

Simon เป็นพิธีกร Fireside Chat กับ [[cat-wu|Cat Wu]] และ [[thariq-shihipar|Thariq Shihipar]] จากทีม [[claude-code|Claude Code]] ที่ [[ai-engineer-worlds-fair|AI Engineer World's Fair]]. โพสต์ [[fables-judgement-simon-willison|Fable's judgement]] ของเขาสรุปเคล็ดที่ได้: ปล่อยให้ [[fable|Fable]] ใช้ดุลพินิจเองแทนสั่งกฎตายตัว (ดู [[judgement-based-prompting]]). เขาต่อยอดด้วยเคล็ดของ [[jesse-vincent|Jesse Vincent]] แล้วสั่ง Claude Code ให้เลือก model ที่ถูกลงรันใน subagent เองสำหรับงาน coding — บอกว่าได้งานเยอะขึ้นและโควตา Fable ลดช้าลง.

## เคส voxium (2026-09)

[[teepagorn-claude-code-adoption-nobody-reading|โพสต์ของ @teepagorn]] เล่าว่า Simon หยิบโพสต์ของ developer ชื่อ voxium มาแปะ voxium เข้าบริษัทใหญ่ที่ทุก level ทำทุกอย่างผ่าน [[claude-code|Claude Code]] คนทำงาน 12-13 ชั่วโมง "just to press enter" และสรุปว่า "Nobody is reading anything." wiki ยังไม่เห็นโพสต์ต้นทางของ Simon เคสนี้ต่อกับเรื่อง [[cognitive-debt]] ที่ Simon เตือนไว้ และ [[ai-work-intensification]]

## See also

- [[cognitive-debt]]
- [[orchestration-tax]]
- [[developer-balance]]
- [[how-to-keep-shipping-away-from-desk]]
- [[fables-judgement-simon-willison]]
- [[judgement-based-prompting]]
- [[teepagorn-claude-code-adoption-nobody-reading]]
- [[ai-work-intensification]]
