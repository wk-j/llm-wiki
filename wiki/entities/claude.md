---
title: Claude
type: entity
tags: [ai, models, anthropic, llm]
created: 2026-04-16
updated: 2026-07-02
sources: [Introducing Claude Opus 4.7.md, The advisor strategy Give Sonnet an intelligence boost with Opus.md, Claude Mythos Preview.md, Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md, zoran-horvat-claude-no-planning-engine.md]
---

# Claude

ตระกูลโมเดล AI จาก [[anthropic|Anthropic]] โดยมี 3 ระดับ (tier) มาตรฐาน คือ **Opus** (เก่งที่สุด), **Sonnet** (สมดุล), และ **Haiku** (เร็วที่สุด/ถูกที่สุด) — นอกจากนี้ยังมี **Mythos** ซึ่งเป็นรุ่นพรีวิวสำหรับเทคโนโลยีล่าสุด (frontier)

## รุ่นปัจจุบัน (พฤษภาคม 2026)

| โมเดล | ระดับ (Tier) | หมายเหตุ |
|---|---|---|
| **[[claude-opus-4-8]]** | Flagship | เปิดตัว 28 พ.ค. 2026; รุ่นต่อจาก Opus 4.7; จุดขายคือ [[model-honesty\|ความซื่อสัตย์]] (ไม่เนียนว่าทำเสร็จ) + alignment ใกล้ Mythos |
| [[claude-opus-4-7]] | Flagship (รุ่นก่อน) | เปิดตัว 16 เม.ย. 2026; เป็นรุ่นต่อจาก Opus 4.6 |
| Claude Opus 4.6 | Flagship (รุ่นเก่า) | ยังคงมีการอ้างอิงใน API และ benchmark บางตัว |
| Claude Sonnet 4.6 | Balanced | เป็น executor model ที่นิยมใช้ใน [[advisor-strategy\|รูปแบบ advisor]] |
| Claude Sonnet 4.5 | Balanced (รุ่นก่อน) | ยังคงใช้กันอย่างแพร่หลายในฐานะ "baseline ที่ดีพอ" สำหรับงานพัฒนาโดยผู้เชี่ยวชาญในโดเมน — ดูที่ [[model-choice-by-expertise]] |
| Claude Haiku 4.5 | Fast | ID `claude-haiku-4-5-20251001` |
| Claude Mythos Preview | Frontier preview | มีความสามารถโดยรวมสูงสุด; สามารถค้นหาและโจมตีช่องโหว่ zero-days ใน OS และเบราว์เซอร์หลักๆ ได้เอง; เปิดให้ใช้ในวงจำกัดผ่าน [[project-glasswing\|Project Glasswing]] |

## ความสามารถทั่วไป

- Multimodal (รองรับ text + images; Opus 4.7 รองรับรูปภาพด้านยาวสุด 2,576 px)
- Tool use / function calling
- Prompt caching (Opus 4.8 ใส่ `system` กลางคันใน messages array ได้โดยไม่พัง cache — ดู [[system-in-messages]])
- Effort levels — `medium` / `high` / `xhigh`(`extra`) / `max`; ดูที่ [[effort-levels]] (Opus 4.8 ค่าเริ่มต้น = `high`, มี effort control บน UI)
- [[model-context-protocol|MCP]] — โปรโตคอลสำหรับเชื่อมต่อกับ tool/data
- [[advisor-strategy]] — การใช้ Sonnet/Haiku ที่ถูกกว่าเป็น executor โดยมี Opus เป็น advisor
- File-system-based memory (ปรับปรุงให้ดีขึ้นใน Opus 4.7)
- [[dynamic-workflows|Dynamic workflows]] ใน [[claude-code|Claude Code]] (research preview, มากับ Opus 4.8) — วางแผนเอง + สั่ง subagent คู่ขนานเป็นร้อย

## ข้อควรระวังเรื่อง Plan mode

[[zoran-horvat|Zoran Horvat]] เสนอ counterpoint ใน [[zoran-horvat-claude-no-planning-engine]] ว่า plan ที่ Claude เขียนออกมาไม่ควรถูกนับเป็น proof ว่ามี planning engine จริง. ในมุมของเขา Plan mode คือ [[plan-mode-as-prompting|prompt scaffold]] ของ harness: จำกัดไม่ให้แก้ไฟล์ แล้วสั่ง model ให้ enumerate steps ก่อน implement.

นี่ไม่ลบ claim เรื่อง [[dynamic-workflows]] แต่ทำให้ต้องอ่านคำว่า "Claude self-plans" อย่างระวัง. Utility อาจจริงในงานที่มี verification gate เช่น test suite แต่ engineering judgment ยังต้องมาจากคน โดยเฉพาะ decision ที่กระทบ data, architecture, security, หรือ semantics ของ product.

## ช่องทางการใช้งาน (Surfaces)

- [[claude-code|Claude Code]] (CLI)
- Claude.ai (web + desktop apps)
- IDE extensions (VS Code, JetBrains)
- Claude API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry

## ดูเพิ่ม

- [[anthropic]]
- [[claude-opus-4-8]]
- [[claude-opus-4-7]]
- [[claude-mythos-preview]]
- [[claude-code]]
- [[effort-levels]]
- [[advisor-strategy]]
- [[plan-mode-as-prompting]]
