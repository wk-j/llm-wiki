---
title: Claude
type: entity
tags: [ai, models, anthropic, llm]
created: 2026-04-16
updated: 2026-04-23
sources: [Introducing Claude Opus 4.7.md, The advisor strategy Give Sonnet an intelligence boost with Opus.md, Claude Mythos Preview.md]
---

# Claude

ตระกูลโมเดล AI จาก [[anthropic|Anthropic]] โดยมี 3 ระดับ (tier) มาตรฐาน คือ **Opus** (เก่งที่สุด), **Sonnet** (สมดุล), และ **Haiku** (เร็วที่สุด/ถูกที่สุด) — นอกจากนี้ยังมี **Mythos** ซึ่งเป็นรุ่นพรีวิวสำหรับเทคโนโลยีล่าสุด (frontier)

## รุ่นปัจจุบัน (เมษายน 2026)

| โมเดล | ระดับ (Tier) | หมายเหตุ |
|---|---|---|
| **[[claude-opus-4-7]]** | Flagship | เปิดตัว 16 เม.ย. 2026; เป็นรุ่นต่อจาก Opus 4.6 |
| Claude Opus 4.6 | Flagship (รุ่นก่อน) | ยังคงมีการอ้างอิงใน API และ benchmark บางตัว |
| Claude Sonnet 4.6 | Balanced | เป็น executor model ที่นิยมใช้ใน [[advisor-strategy\|รูปแบบ advisor]] |
| Claude Sonnet 4.5 | Balanced (รุ่นก่อน) | ยังคงใช้กันอย่างแพร่หลายในฐานะ "baseline ที่ดีพอ" สำหรับงานพัฒนาโดยผู้เชี่ยวชาญในโดเมน — ดูที่ [[model-choice-by-expertise]] |
| Claude Haiku 4.5 | Fast | ID `claude-haiku-4-5-20251001` |
| Claude Mythos Preview | Frontier preview | มีความสามารถโดยรวมสูงสุด; สามารถค้นหาและโจมตีช่องโหว่ zero-days ใน OS และเบราว์เซอร์หลักๆ ได้เอง; เปิดให้ใช้ในวงจำกัดผ่าน [[project-glasswing\|Project Glasswing]] |

## ความสามารถทั่วไป

- Multimodal (รองรับ text + images; Opus 4.7 รองรับรูปภาพด้านยาวสุด 2,576 px)
- Tool use / function calling
- Prompt caching
- Effort levels — `medium` / `high` / `xhigh` / `max`; ดูที่ [[effort-levels]]
- [[model-context-protocol|MCP]] — โปรโตคอลสำหรับเชื่อมต่อกับ tool/data
- [[advisor-strategy]] — การใช้ Sonnet/Haiku ที่ถูกกว่าเป็น executor โดยมี Opus เป็น advisor
- File-system-based memory (ปรับปรุงให้ดีขึ้นใน Opus 4.7)

## ช่องทางการใช้งาน (Surfaces)

- [[claude-code|Claude Code]] (CLI)
- Claude.ai (web + desktop apps)
- IDE extensions (VS Code, JetBrains)
- Claude API, Amazon Bedrock, Google Cloud Vertex AI, Microsoft Foundry

## ดูเพิ่ม

- [[anthropic]]
- [[claude-opus-4-7]]
- [[claude-mythos-preview]]
- [[claude-code]]
- [[effort-levels]]
- [[advisor-strategy]]
