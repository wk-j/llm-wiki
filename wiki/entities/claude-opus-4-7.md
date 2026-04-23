---
title: Claude Opus 4.7
type: entity
tags: [ai, models, anthropic, claude, opus]
created: 2026-04-16
updated: 2026-04-23
sources: [Introducing Claude Opus 4.7.md, Whats new in Claude Opus 4.7 - Anthropic Docs.md, Claude Opus 4.7 Isn't a Drop-in Replacement for 4.6.md, Claude Mythos Preview.md]
---

# Claude Opus 4.7

เป็นโมเดล flagship ของ [[anthropic|Anthropic]] ที่เปิดให้ใช้ทั่วไป ณ วันที่ **16 เมษายน 2026** เป็นรุ่นต่อโดยตรงจาก Opus 4.6

**Model ID:** `claude-opus-4-7`
**ราคา:** $5 / 1 ล้าน input tokens, $25 / 1 ล้าน output tokens (ไม่เปลี่ยนแปลงจาก 4.6)

## ตำแหน่งเมื่อเทียบกับรุ่นอื่นๆ

- **ดีกว่า Opus 4.6** ในทุก benchmarks (SWE-bench, Terminal-Bench 2.0, CyberGym, MCP-Atlas, Finance Agent, GDPval-AA)
- **ความสามารถโดยรวมยังไม่เท่า [[claude-mythos-preview|Claude Mythos Preview]]** (ซึ่งเป็นโมเดล frontier ของ [[anthropic|Anthropic]] ที่จำกัดการเข้าถึง; ความสามารถด้าน cyber เกิดขึ้นเองโดยไม่ได้ตั้งใจฝึก — ในทางกลับกันความสามารถด้านนี้ของ Opus 4.7 ถูก*ลดทอน*ลงระหว่างการฝึก)
- มี API shape เหมือนกับ Sonnet 4.6 และ Haiku 4.5 — [[effort-levels|effort levels]], prompt caching, tools

## สิ่งที่ปรับปรุงขึ้นจาก Opus 4.6

| ด้าน | การเปลี่ยนแปลง |
|---|---|
| **วิศวกรรมซอฟต์แวร์** | เก่งขึ้นอย่างเห็นได้ชัดในงานที่ยากมากๆ; ทำงานด้าน coding ที่ต้องรันนานๆ ได้อย่างน่าเชื่อถือ |
| **การตรวจสอบตัวเอง (Self-verification)** | โมเดลสามารถสร้างวิธีตรวจสอบงานของตัวเองก่อนจะรายงานผลกลับมา |
| **การทำตามคำสั่ง** | ทำตามคำสั่งแบบตรงไปตรงมามากขึ้นอย่างมาก — prompt เก่าๆ อาจจะต้องปรับแก้ |
| **Vision** | รองรับรูปภาพด้านยาวสุดถึง 2,576 px (ประมาณ 3 เท่าของ Claude รุ่นก่อนๆ) |
| **File-system memory** | จดจำข้อมูลข้าม session งานที่ทำต่อเนื่องหลายครั้งได้ดีขึ้น |
| **การป้องกัน Prompt injection** | ดีขึ้น |
| **ความซื่อสัตย์ (Honesty)** | ดีขึ้น |
| **ผลลัพธ์ที่มีรสนิยม (Tasteful outputs)** | สร้าง UI, สไลด์, เอกสาร ที่มีคุณภาพสูงขึ้น |

## ข้อด้อย / สิ่งที่ต้องแลกมา

- ให้คำแนะนำเพื่อลดอันตรายจากสารควบคุม (harm-reduction advice for controlled substances) ได้แย่ลงเล็กน้อย
- **ใช้ token มากขึ้น**: tokenizer ที่อัปเดตใหม่ (ใช้ token มากขึ้น +0–35% สำหรับ input ที่เหมือนกัน) และมีการ "คิด" มากขึ้นเมื่อใช้ effort level สูงๆ ใน turn หลังๆ ของ agent — แต่ผลกระทบสุทธิต่อค่า token ในการประเมินผลด้าน coding ภายในยังถือว่าดีขึ้น

## ฟีเจอร์ใหม่ที่เปิดตัวพร้อมกัน

- **`xhigh` effort level** — ดูที่ [[effort-levels]]
- **[[task-budgets|Task budgets]]** (API, public beta; beta header `task-budgets-2026-03-13`) — เป็นเป้าหมายจำนวน token ที่แนะนำสำหรับ agent loop ทั้งหมด; แตกต่างจาก `max_tokens`
- **`/ultrareview`** slash command ใน [[claude-code|Claude Code]]
- **[[auto-mode|Auto mode]]** ขยายให้ผู้ใช้ Claude Code Max สามารถใช้งานได้ (ตัว permission mode นี้เปิดตัวมาก่อนแล้วเมื่อวันที่ 24 มีนาคม 2026 สำหรับ Team plan — ดูที่ [[claude-code-auto-mode]])

## API Breaking Changes (กระทบ Messages API; ไม่กระทบ Managed Agents)

- **ยกเลิก Extended thinking budgets** — `thinking.budget_tokens` → 400. [[adaptive-thinking|Adaptive thinking]] กลายเป็นโหมดเดียวสำหรับการเปิด thinking ซึ่งจะปิดเป็นค่าเริ่มต้นใน 4.7 — ต้องเปิดใช้งานเอง
- **ยกเลิก Sampling parameters** — การส่ง `temperature` / `top_p` / `top_k` ที่ไม่ใช่ค่าเริ่มต้น → 400 error. ให้ใช้ prompt เพื่อชี้นำพฤติกรรมแทน
- **ไม่ส่งเนื้อหา thinking มาเป็นค่าเริ่มต้น** — การเปลี่ยนแปลงนี้เกิดขึ้นเงียบๆ; field `thinking` จะว่างเปล่า ยกเว้นจะตั้งค่า `display: "summarized"` หาก product ของคุณ stream reasoning ให้ผู้ใช้ จะเห็นว่ามีช่วงที่หยุดนิ่งนาน
- **Tokenizer ใหม่** — ข้อความเดียวกันจะใช้ token มากขึ้น ~1.0–1.35 เท่า; ควรเพิ่ม headroom ของ `max_tokens` และทบทวน trigger สำหรับการทำ [[compaction|compaction]] ใหม่ รองรับ 1M context ในราคาปกติ (ไม่มีค่า premium สำหรับ long-context)
- **Prefilled assistant responses ถูก deprecated** (เริ่มตั้งแต่ Claude 4.6) และจะ trả về **400 error บน Mythos Preview** ต้องออกแบบ prompt ที่เคยใช้ assistant prefill เพื่อบังคับ output shape ใหม่ (ที่มา: [[claude-opus-4-7-migration-pachaar|คู่มือย้ายระบบของ Pachaar]])

## พฤติกรรมที่เปลี่ยนไป (ระดับ Prompt)

- ทำตามคำสั่งแบบตรงไปตรงมามากขึ้น (โดยเฉพาะที่ effort level ต่ำๆ)
- ความยาวของคำตอบจะปรับตามความซับซ้อนของงาน
- เรียกใช้ tool และ subagent น้อยลงเป็นค่าเริ่มต้น (ต้องเพิ่ม effort / prompt เพื่อให้เรียกมากขึ้น)
- ใช้โทนเสียงที่ตรงไปตรงมาและแสดงความคิดเห็นมากขึ้น; ใช้อีโมจิน้อยกว่า 4.6
- อัปเดตความคืบหน้าบ่อยขึ้นระหว่างที่ agent ทำงานนานๆ — สามารถเอา scaffolding ที่เคยใส่ไว้เพื่อบังคับให้รายงานสถานะออกได้
- **ทุก turn ของผู้ใช้จะกระตุ้นให้เกิดการคิด (reasoning)** — การ prompt แบบถามตอบหลายๆ turn จะทำให้เปลือง token มากใน 4.7 ในขณะที่ 4.6 นั้นไม่เป็น ควรอัด context ที่จำเป็นทั้งหมดไว้ใน turn แรก; ดูที่ [[delegation-mindset]]
- **การทำตามคำสั่งตรงๆ อาจลด recall ของ code-review** เมื่อ harness สั่งว่า "conservative" หรือ "only high-severity" — โมเดลจะหา bug เจอ แต่กรองมันออกไปเอง วิธีแก้: [[find-vs-filter]] — แยกขั้นตอนการค้นหา (discovery) ออกจากการคัดกรอง (triage)

## นโยบายด้าน Cyber

- ความสามารถด้าน Cyber **ถูกลดทอนลงอย่างจงใจระหว่างการฝึก**
- มีระบบป้องกันอัตโนมัติเพื่อบล็อก request ที่ผิดกฎหมาย / มีความเสี่ยงสูงด้าน cyber
- มี **Cyber Verification Program** สำหรับนักวิจัยด้านความปลอดภัยที่ถูกต้อง
- เป็นส่วนหนึ่งของ **[[project-glasswing|Project Glasswing]]** ของ [[anthropic|Anthropic]] — เป็นการนำร่องระบบป้องกันบน 4.7 ก่อนที่จะปล่อยโมเดลระดับ Mythos-class ในวงกว้าง

## ช่องทางการใช้งาน

- ผลิตภัณฑ์ของ Claude (Claude.ai, [[claude-code|Claude Code]])
- Claude API (`claude-opus-4-7`)
- Amazon Bedrock
- Google Cloud Vertex AI
- Microsoft Foundry

## บทบาทใน Wiki Patterns ที่มีอยู่

- **[[advisor-strategy|Advisor strategy]]**: เป็น advisor model ที่มาแทน Opus 4.6 อย่างเป็นธรรมชาติ
- **[[llm-knowledge-bases|LLM wikis]]**: file-system memory ที่ดีขึ้นช่วยลดต้นทุนในการโหลด session ใหม่
- **[[claude-code-session-management|Session management]]**: effort level เริ่มต้นของ [[claude-code|Claude Code]] ถูกปรับเป็น `xhigh`; auto mode เป็นทางเลือกใหม่สำหรับการทำงานระยะยาว

## ดูเพิ่ม

- [[claude]]
- [[anthropic]]
- [[claude-mythos-preview]]
- [[claude-code]]
- [[effort-levels]]
- [[advisor-strategy]]
