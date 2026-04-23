---
title: Kimi K2.6
type: entity
tags: [ai, llm, model, open-source, coding, agents, moonshot]
created: 2026-04-21
updated: 2026-04-23
sources: [Kimi K2.6 Tech Blog Advancing Open-Source Coding.md]
---

# Kimi K2.6

โมเดล flagship แบบ open-source จาก [[moonshot-ai|Moonshot AI]] (เปิดตัวเมษายน 2026) เป็นรุ่นต่อจาก Kimi K2.5 วางตำแหน่งตัวเองเป็น **โมเดล open-source ที่ล้ำสมัยที่สุดสำหรับงาน coding และ agent ที่ต้องทำงานระยะยาว (long-horizon)** — ไม่ได้แข่งขันที่ความสามารถในการให้เหตุผล (reasoning) หรือ vision โดยตรง

## ความสามารถเด่น

- **Long-horizon coding** — ทำงานต่อเนื่องได้นาน 12+ ชั่วโมง, เรียกใช้ tool ได้ 4000+ ครั้ง; แสดงให้เห็นในการทำ optimization ของ Qwen3.5-0.8B Zig-port และการยกเครื่อง matching-engine ของ exchange-core
- **Agent Swarm orchestration** — จัดการ sub-agent 300 ตัวที่ทำงานประสานกันกว่า 4000 ขั้นตอนต่อการรันหนึ่งครั้ง (เพิ่มขึ้น 3 เท่า / 2.6 เท่า เทียบกับ K2.5); ดูที่ [[agent-swarm]]
- **Coding-driven design** — เปลี่ยน prompt ให้กลายเป็น frontend ทั้งหมด + full-stack แบบเบา (auth, DB, session)
- **Proactive 24/7 agents** — เป็นขุมพลังให้ OpenClaw, Hermes; Moonshot เคยรัน K2.6 agent ต่อเนื่องนาน **5 วัน** โดยอัตโนมัติเพื่องาน RL infra ops
- **Document-to-Skill** — สกัด DNA เชิงโครงสร้างและสไตล์จากไฟล์ PDF, สไลด์, spreadsheets, Word docs ออกมาเป็น Skills ที่ใช้ซ้ำได้โดยอัตโนมัติ

## รายละเอียด API

- **Platform:** **platform.kimi.ai**
- **Default context:** **262,144 tokens**
- เปิดใช้งาน Thinking mode เป็นค่าเริ่มต้นใน benchmark ที่เผยแพร่
- **Test params:** temperature 1.0, top-p 1.0
- คะแนน benchmark ด้าน coding เป็นค่าเฉลี่ยจากการรันอิสระ 10 ครั้ง

## ไฮไลท์จาก Benchmark

อ้างว่ามีคะแนนนำหรือเทียบเท่า GPT-5.4 (xhigh), Claude Opus 4.6 (max), Gemini 3.1 Pro (thinking high):

- **SWE-Bench Pro: 58.6** (นำ) — Opus 4.6 53.4, GPT-5.4 57.7
- **HLE-Full w/ tools: 54.0** (นำ) — Opus 4.6 53.0
- **DeepSearchQA f1: 92.5** (นำ) — Opus 4.6 91.3
- **BrowseComp w/ agent swarm: 86.3** (เป็นแกนที่ไม่เหมือนใคร — เป็นคะแนนในโหมด swarm, ตัวอื่นไม่ได้วัด)
- **Terminal-Bench 2.0:** 66.7 — เทียบเท่า Opus 4.6 ที่ 65.4, แต่ต่ำกว่า Gemini 68.5
- ตามหลังใน AIME/GPQA (การให้เหตุผลล้วนๆ) และ benchmark ด้าน vision บางตัว

**ข้อควรระวัง:** ตาราง benchmark ไม่ได้รวม [[claude-opus-4-7|Claude Opus 4.7]] (ที่เปิดตัว 16 เม.ย. 2026) เข้ามาด้วย โดยใช้แค่ 4.6 เท่านั้น

## การกล่าวถึงใน Ecosystem

Testimonial จากองค์กรต่างๆ ในโพสต์เปิดตัว: **CodeBuddy** (codegen +12% / long-context +18% / tool-call success 96.6%), **Ollama**, **[[opencode|OpenCode]]**, **Qoder**, **Hermes Agent** (Nous Research), **KiloClaw**, **OpenClaw**, **AI Gateway / Next.js** (ประสิทธิภาพบน Next.js bench ดีขึ้น 50%+)

## ดูเพิ่ม

- [[moonshot-ai]]
- [[agent-swarm]]
- [[kimi-k2-6-tech-blog]]
- [[subagent-patterns]]
- [[claude-opus-4-7]]
