---
title: Anthropic
type: entity
tags: [company, ai, ai-safety, claude]
created: 2026-04-16
updated: 2026-04-23
sources: [Introducing Claude Opus 4.7.md, The advisor strategy Give Sonnet an intelligence boost with Opus.md, Using Claude Code Session Management & 1M Context.md, opencode-vs-claude-code-morph.md, Claude Mythos Preview.md]
---

# Anthropic

บริษัทวิจัยด้านความปลอดภัย AI และผู้สร้างตระกูลโมเดล **[[claude|Claude]]** และ **[[claude-code|Claude Code]]** นิยามภารกิจของตัวเองว่าคือการสร้างระบบ AI ที่เชื่อถือได้ (reliable), ตีความได้ (interpretable), และควบคุมได้ (steerable)

## ผลิตภัณฑ์ที่อ้างอิงใน Wiki นี้

- **[[claude|Claude]]** — ตระกูลโมเดล AI (Opus, Sonnet, Haiku)
- **[[claude-opus-4-7]]** — โมเดล flagship ปัจจุบัน (เปิดตัว 16 เม.ย. 2026)
- **[[claude-mythos-preview|Claude Mythos Preview]]** — โมเดลที่เก่งที่สุดของ Anthropic; สามารถค้นหาและโจมตีช่องโหว่ zero-days ใน OS และเบราว์เซอร์หลักๆ ได้เอง; ยังจำกัดการเข้าถึงอย่างจงใจระหว่างที่รอให้ระบบป้องกันด้าน cyber พัฒนาขึ้น
- **[[claude-code|Claude Code]]** — coding agent ที่ทำงานผ่าน terminal (มีเวอร์ชัน desktop, web, และ IDE extensions ด้วย)
- **Claude API** (`platform.claude.com`) — API สำหรับนักพัฒนา; รองรับ effort levels, task budgets, advisor tool, MCP
- **[[project-glasswing|Project Glasswing]]** — โครงการที่ใช้ Mythos Preview เพื่อเสริมความปลอดภัยให้ซอฟต์แวร์ที่สำคัญ ก่อนที่โมเดลระดับ Mythos-class จะเปิดให้ใช้ในวงกว้าง

## ช่องทางการให้บริการ (ณ 16 เม.ย. 2026)

- ผลิตภัณฑ์ของ Anthropic เอง (Claude.ai, [[claude-code|Claude Code]])
- Claude API
- Amazon Bedrock
- Google Cloud Vertex AI
- Microsoft Foundry

## รูปแบบและแนวคิดเด่นๆ ที่ริเริ่มหรือพัฒนาต่อ

- **[[advisor-strategy]]** — การกลับด้านของรูปแบบ orchestrator-worker (จากบล็อกของ Anthropic, 9 เม.ย. 2026)
- **[[compaction|/compact]]** และ **/rewind** ใน [[claude-code|Claude Code]]
- **[[model-context-protocol|MCP]]** — โปรโตคอลเปิดสำหรับการเชื่อมต่อ AI กับ tool
- **[[effort-levels|Effort levels]]** — พารามิเตอร์สำหรับแลกเปลี่ยนระหว่าง reasoning กับ latency อย่างชัดเจน

## ตัวชี้วัดทางธุรกิจ (ก.พ. 2026, อ้างอิงจาก SemiAnalysis ผ่าน Morph)

มูลค่าบริษัทประมาณ ~$380B, รายได้ต่อปี (ARR) ~$14B. เส้นกราฟรายได้พุ่งขึ้นอย่างรวดเร็วในช่วงที่ SemiAnalysis เรียกว่า "Claude Code Moment" — มีรายงานว่า [[claude-code|Claude Code]] เป็นผู้สร้าง commit ราว ~4% ของ public commit ทั้งหมดบน GitHub

## กรณีบล็อก OpenCode OAuth (9 ม.ค. 2026)

Anthropic ได้บล็อก [[opencode|OpenCode]] ไม่ให้ใช้ Claude ผ่าน consumer OAuth token (Claude Pro/Max) อย่างเงียบๆ ทาง OpenCode ได้ถอด integration ออกโดยอ้าง *"anthropic legal requests"* และตอบโต้ด้วยการเปิดตัว gateway ของตัวเอง (**Black**, **Zen**) เหตุการณ์นี้ถือเป็นจุดเปลี่ยนที่แสดงถึงความขัดแย้งอย่างเปิดเผยระหว่าง Anthropic กับ third-party harness แบบ open-source รายใหญ่ (การเข้าถึงผ่าน API key ยังคงใช้งานได้) บริบทและการตอบรับดูได้ที่ [[opencode-vs-claude-code-morph]]

## บริบทเกี่ยวกับกลยุทธ์ด้าน Cyber

สำหรับ Opus 4.7, Anthropic ได้จงใจลดทอนความสามารถด้าน cyber ระหว่างการฝึกและเพิ่มชั้นของระบบป้องกันอัตโนมัติเข้าไป กลยุทธ์ที่ประกาศคือการเรียนรู้จากการใช้งาน 4.7 ในโลกจริง ก่อนที่จะปล่อยโมเดลระดับ **Mythos-class** ในวงกว้าง สำหรับผู้เชี่ยวชาญด้านความปลอดภัยที่ต้องการใช้ความสามารถด้าน cyber เต็มรูปแบบ สามารถสมัครเข้าร่วม **Cyber Verification Program** ได้

[[project-glasswing|Project Glasswing]] (ที่เปิดตัวพร้อม [[claude-mythos-preview|Mythos Preview]]) คือหน่วยปฏิบัติการของกลยุทธ์นี้: Mythos Preview จะค้นหาช่องโหว่ในซอฟต์แวร์ที่สำคัญในสเกลใหญ่, ประสานงานการเปิดเผยข้อมูลอย่างรับผิดชอบ (responsible disclosure), และแบ่งปันการเข้าถึงให้กับพาร์ทเนอร์ที่ผ่านการตรวจสอบแล้ว ในบล็อกระบุว่าความพยายามนี้เป็น "ช่วงเวลาแห่งการเปลี่ยนแปลง" — ความสามารถด้าน cyber เกิดขึ้นมาเองโดยไม่ได้ตั้งใจฝึก แต่เป็นผลพลอยได้จากการพัฒาความสามารถโดยรวมของโมเดล สามารถค้นพบช่องโหว่ความรุนแรงสูง/วิกฤตหลายพันรายการ; มีความเห็นตรงกับผู้ตรวจสอบที่เป็นมนุษย์ถึง 89% ในเรื่องระดับความรุนแรง; และไม่เคยมี false positive เลยในการตรวจจับ memory corruption (ใช้ ASan เป็น oracle)

## ดูเพิ่ม

- [[claude]]
- [[claude-opus-4-7]]
- [[claude-mythos-preview]]
- [[project-glasswing]]
- [[claude-code]]
- [[advisor-strategy]]
- [[model-context-protocol]]
