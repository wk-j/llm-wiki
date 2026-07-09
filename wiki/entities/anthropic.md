---
title: Anthropic
type: entity
tags: [company, ai, ai-safety, claude]
created: 2026-04-16
updated: 2026-07-09
sources: [Introducing Claude Opus 4.7.md, The advisor strategy Give Sonnet an intelligence boost with Opus.md, Using Claude Code Session Management & 1M Context.md, opencode-vs-claude-code-morph.md, Claude Mythos Preview.md, improved-15-llms-harness-changed.md, Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md, how-ai-became-more-expensive-than-workers-it-replaced.md, claude-in-microsoft-foundry.md, bun-in-rust.md]
---

# Anthropic

บริษัทวิจัยด้านความปลอดภัย AI และผู้สร้างตระกูลโมเดล **[[claude|Claude]]** และ **[[claude-code|Claude Code]]** นิยามภารกิจของตัวเองว่าคือการสร้างระบบ AI ที่เชื่อถือได้ (reliable), ตีความได้ (interpretable), และควบคุมได้ (steerable)

## ผลิตภัณฑ์ที่อ้างอิงใน Wiki นี้

- **[[claude|Claude]]** — ตระกูลโมเดล AI (Opus, Sonnet, Haiku)
- **[[claude-opus-4-8]]** — โมเดล flagship ปัจจุบัน (เปิดตัว 28 พ.ค. 2026); จุดขายคือ [[model-honesty|ความซื่อสัตย์]] + alignment ใกล้ Mythos; มากับ [[dynamic-workflows|dynamic workflows]] และ [[effort-levels|effort control]] บน UI
- **[[claude-opus-4-7]]** — flagship รุ่นก่อน (เปิดตัว 16 เม.ย. 2026)
- **[[claude-mythos-preview|Claude Mythos Preview]]** — โมเดลที่เก่งที่สุดของ Anthropic; สามารถค้นหาและโจมตีช่องโหว่ zero-days ใน OS และเบราว์เซอร์หลักๆ ได้เอง; ยังจำกัดการเข้าถึงอย่างจงใจระหว่างที่รอให้ระบบป้องกันด้าน cyber พัฒนาขึ้น
- **[[claude-code|Claude Code]]** — coding agent ที่ทำงานผ่าน terminal (มีเวอร์ชัน desktop, web, และ IDE extensions ด้วย)
- **[[claude-managed-agents|Claude Managed Agents API]]** — แพลตฟอร์มรัน agent ให้ลูกค้า; มี [[agent-memory-filesystem|Memory]] (public beta) และ [[dreaming|Dreaming]] (research preview, 2026-05-09)
- **Claude API** (`platform.claude.com`) — API สำหรับนักพัฒนา; รองรับ effort levels, task budgets, advisor tool, MCP
- **[[project-glasswing|Project Glasswing]]** — โครงการที่ใช้ Mythos Preview เพื่อเสริมความปลอดภัยให้ซอฟต์แวร์ที่สำคัญ ก่อนที่โมเดลระดับ Mythos-class จะเปิดให้ใช้ในวงกว้าง

## ช่องทางการให้บริการ (ณ 16 เม.ย. 2026)

- ผลิตภัณฑ์ของ Anthropic เอง (Claude.ai, [[claude-code|Claude Code]])
- Claude API
- Amazon Bedrock
- Google Cloud Vertex AI
- [[microsoft-foundry|Microsoft Foundry]] — Claude เป็น generally available บน Foundry ตั้งแต่ 2026-06-29 (ดู [[claude-in-microsoft-foundry]])

## รูปแบบและแนวคิดเด่นๆ ที่ริเริ่มหรือพัฒนาต่อ

- **[[advisor-strategy]]** — การกลับด้านของรูปแบบ orchestrator-worker (จากบล็อกของ Anthropic, 9 เม.ย. 2026)
- **[[compaction|/compact]]** และ **/rewind** ใน [[claude-code|Claude Code]]
- **[[model-context-protocol|MCP]]** — โปรโตคอลเปิดสำหรับการเชื่อมต่อ AI กับ tool
- **[[effort-levels|Effort levels]]** — พารามิเตอร์สำหรับแลกเปลี่ยนระหว่าง reasoning กับ latency อย่างชัดเจน

## ตัวชี้วัดทางธุรกิจ (ก.พ. 2026, อ้างอิงจาก SemiAnalysis ผ่าน Morph)

มูลค่าบริษัทประมาณ ~$380B, รายได้ต่อปี (ARR) ~$14B. เส้นกราฟรายได้พุ่งขึ้นอย่างรวดเร็วในช่วงที่ SemiAnalysis เรียกว่า "Claude Code Moment" — มีรายงานว่า [[claude-code|Claude Code]] เป็นผู้สร้าง commit ราว ~4% ของ public commit ทั้งหมดบน GitHub

## Enterprise cost pressure

ใน [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]] Economy Media วาง Anthropic เป็นหนึ่งในผู้ได้ประโยชน์จาก enterprise AI agents และ Claude Code adoption แต่ก็เป็นตัวอย่างของแรงตึงใหม่: ถ้าองค์กรใช้ token จำนวนมหาศาล บิล Anthropic อาจโตจนลูกค้าต้องถามว่า AI ยังถูกกว่าแรงงานหรือไม่

คลิปอ้างว่า Anthropic ตั้งเป้า annualized revenue ปี 2026 โตจากราว $3B เป็นเกือบ $9.6B และยกกรณี Microsoft ลด/ยกเลิก Claude Code usage เพราะต้นทุนสูง ตัวเลขเหล่านี้ยังเป็น source-attributed ผ่านคลิป ไม่ใช่ wiki ตรวจจาก Reuters/filing โดยตรง

## Claude GA บน Microsoft Foundry (2026-06-29)

Anthropic ประกาศว่า [[claude|Claude]] เป็น **generally available** บน [[microsoft-foundry|Microsoft Foundry]] แล้ว (ดู [[claude-in-microsoft-foundry]]). เป็นก้าว distribution ระดับองค์กร: ลูกค้ารัน [[claude-opus-4-8|Opus 4.8]] และ Claude Haiku 4.5 ในสภาพแวดล้อม [[azure|Azure]] ของตัวเอง โดย Anthropic เป็นผู้รัน inference และเป็น data processor, เลือก [[data-residency|data zone]] ได้. เป็นรูปแบบเดียวกับที่ Anthropic ทำผ่าน Bedrock/Vertex — เอา model ไปวางในคลาวด์ของลูกค้า (ดู [[enterprise-model-deployment]]).

## Bun rewrite ด้วย Fable/Claude Code (2026-07)

ใน [[bun-in-rust|Bun in Rust]], [[jarred-sumner|Jarred Sumner]] เปิดเผยว่าเขาใช้ pre-release [[fable|Claude Fable 5]] และ [[claude-code|Claude Code]] ทำ rewrite [[bun|Bun]] จาก [[zig|Zig]] เป็น [[rust|Rust]]. Disclosure ในบทความบอกว่า Bun ถูก Anthropic ซื้อในเดือนธันวาคม 2025 และทีม Bun ทำงานที่ Anthropic.

เคสนี้ทำให้ claim เรื่อง [[dynamic-workflows|dynamic workflows]] มีหลักฐานภาคสนาม: workflow ราว 50 ตัว, peak ประมาณ 64 Claudes, 11 วันจน test suite ผ่านทุก platform, พร้อม [[adversarial-review-loops|adversarial review loops]] และ CI/fuzzing เป็น guardrail.

## มุม third-party harness (Can Bölük, ก.พ. 2026)

[[can-boluk|Can Bölük]] มองการที่ Anthropic บล็อก [[opencode|OpenCode]] จาก Claude Code subscription ว่าเป็นสัญญาณ **anti–third-party harness** ทั้งที่จริงแล้วการที่ open harness ปรับ edit tool ช่วยดันให้ model ของ vendor เองได้อีกหลาย point โดยไม่ต้องเทรนใหม่ (ดู [[improved-15-llms-harness-changed]], [[edit-tool-formats]]) ของเขาคือพอเจอ third-party harness ก็ควร "เล่ามาให้ฟัง" ไม่ใช่ blanket ban — เหมือนทีม security ที่ยอมจ้าง cheater มาช่วยป้องกัน

## กรณีบล็อก OpenCode OAuth (9 ม.ค. 2026)

Anthropic ได้บล็อก [[opencode|OpenCode]] ไม่ให้ใช้ Claude ผ่าน consumer OAuth token (Claude Pro/Max) อย่างเงียบๆ ทาง OpenCode ได้ถอด integration ออกโดยอ้าง *"anthropic legal requests"* และตอบโต้ด้วยการเปิดตัว gateway ของตัวเอง (**Black**, **Zen**) เหตุการณ์นี้ถือเป็นจุดเปลี่ยนที่แสดงถึงความขัดแย้งอย่างเปิดเผยระหว่าง Anthropic กับ third-party harness แบบ open-source รายใหญ่ (การเข้าถึงผ่าน API key ยังคงใช้งานได้) บริบทและการตอบรับดูได้ที่ [[opencode-vs-claude-code-morph]]

## บริบทเกี่ยวกับกลยุทธ์ด้าน Cyber

สำหรับ Opus 4.7, Anthropic ได้จงใจลดทอนความสามารถด้าน cyber ระหว่างการฝึกและเพิ่มชั้นของระบบป้องกันอัตโนมัติเข้าไป กลยุทธ์ที่ประกาศคือการเรียนรู้จากการใช้งาน 4.7 ในโลกจริง ก่อนที่จะปล่อยโมเดลระดับ **Mythos-class** ในวงกว้าง สำหรับผู้เชี่ยวชาญด้านความปลอดภัยที่ต้องการใช้ความสามารถด้าน cyber เต็มรูปแบบ สามารถสมัครเข้าร่วม **Cyber Verification Program** ได้

**อัปเดต timeline (28 พ.ค. 2026, จากบทความเปิดตัว [[claude-opus-4-8|Opus 4.8]]):** Anthropic บอกว่ากำลังทำสองทางต่อ — (1) โมเดลความสามารถใกล้ Opus แต่ราคาถูกลง, และ (2) โมเดลที่ **ฉลาดกว่า Opus** (ระดับ Mythos) ตอนนี้องค์กรจำนวนหนึ่งใช้ [[claude-mythos-preview|Mythos Preview]] สำหรับงาน cybersecurity อยู่แล้วภายใต้ [[project-glasswing|Project Glasswing]] และการพัฒนามาตรการป้องกัน cyber ที่จำเป็น "คืบหน้าอย่างรวดเร็ว" คาดว่าจะ **นำโมเดลระดับ Mythos มาให้ลูกค้าทุกคนได้ภายในไม่กี่สัปดาห์ข้างหน้า** (เดิมบอกแค่ว่าจะปล่อยมาตรการป้องกันใหม่ "พร้อม Opus model ที่กำลังจะมาถึง" ซึ่งก็คือ Opus 4.8 นี่เอง)

[[project-glasswing|Project Glasswing]] (ที่เปิดตัวพร้อม [[claude-mythos-preview|Mythos Preview]]) คือหน่วยปฏิบัติการของกลยุทธ์นี้: Mythos Preview จะค้นหาช่องโหว่ในซอฟต์แวร์ที่สำคัญในสเกลใหญ่, ประสานงานการเปิดเผยข้อมูลอย่างรับผิดชอบ (responsible disclosure), และแบ่งปันการเข้าถึงให้กับพาร์ทเนอร์ที่ผ่านการตรวจสอบแล้ว ในบล็อกระบุว่าความพยายามนี้เป็น "ช่วงเวลาแห่งการเปลี่ยนแปลง" — ความสามารถด้าน cyber เกิดขึ้นมาเองโดยไม่ได้ตั้งใจฝึก แต่เป็นผลพลอยได้จากการพัฒาความสามารถโดยรวมของโมเดล สามารถค้นพบช่องโหว่ความรุนแรงสูง/วิกฤตหลายพันรายการ; มีความเห็นตรงกับผู้ตรวจสอบที่เป็นมนุษย์ถึง 89% ในเรื่องระดับความรุนแรง; และไม่เคยมี false positive เลยในการตรวจจับ memory corruption (ใช้ ASan เป็น oracle)

## ดูเพิ่ม

- [[claude]]
- [[claude-opus-4-8]]
- [[claude-opus-4-7]]
- [[claude-mythos-preview]]
- [[project-glasswing]]
- [[claude-code]]
- [[advisor-strategy]]
- [[model-context-protocol]]
- [[ai-token-economics]]
- [[enterprise-ai-roi]]
- [[microsoft-foundry]]
- [[claude-in-microsoft-foundry]]
- [[enterprise-model-deployment]]
- [[bun-in-rust]]
- [[bun]]
