---
title: GPT-5.5
type: entity
tags: [ai, models, openai, gpt]
created: 2026-04-24
updated: 2026-04-24
sources: [Piyalitt Ittichaiwong - GPT-5.5 Launch.md]
---

# GPT-5.5

Flagship model ของ [[openai|OpenAI]] เปิดตัว **2026-04-23** — OpenAI บอกเองว่าเป็น agentic coding model ที่แข็งแกร่งที่สุดของพวกเขาจนถึงปัจจุบัน

**Model ID (API, เร็วๆ นี้):** `gpt-5.5` / `gpt-5.5-pro`
**Context window:** 400K ใน Codex / 1M ใน API
**ราคา API:** $5 / 1M input, $30 / 1M output (Pro: $30 / $180)

## ตำแหน่งเมื่อเทียบกับรุ่นอื่นๆ

| vs | ผลที่ได้ |
|---|---|
| **GPT-5.4** | ฉลาดกว่ามาก, latency ต่อ token เท่าเดิม, ใช้ token น้อยลง — แต่**ราคา 2 เท่า** |
| **[[claude-opus-4-7\|Claude Opus 4.7]]** | senior engineer บอกว่า "แข็งแกร่งกว่าอย่างชัดเจน" ในด้าน reasoning + autonomy; CyberGym 81.8 vs 73.1; แพงกว่า Opus เล็กน้อย (ปกติ GPT ถูกกว่าครึ่ง — pricing inversion) |
| **[[claude-mythos-preview\|Claude Mythos Preview]]** | [[piyalitt-ittichaiwong\|Piyalitt]] บอกว่า "เก่งใกล้มากๆ" ยกเว้น SWE-Bench Pro ที่มี memorization sign — แต่ GPT-5.5 *เปิดให้ทุกคนเข้าถึง* ต่างจาก Mythos ที่ gate ผ่าน [[project-glasswing\|Project Glasswing]] |
| **[[kimi-k2-6]]** | K2.6 เน้น scale-out (300 sub-agent swarm, open source); GPT-5.5 เน้น single-agent capability + knowledge work + enterprise deployment |

## Benchmarks เด่น

| งาน | คะแนน | หมายเหตุ |
|---|---|---|
| **Terminal-Bench 2.0** | 82.7% | SOTA (agentic workflow ผ่าน command-line) |
| **SWE-Bench Pro** | 58.6% | ⚠️ Anthropic ฟ้องว่ามี memorization sign; [[piyalitt-ittichaiwong\|Piyalitt]] ตีความว่าพลาด ไม่ได้ benchmaxx ตั้งใจ |
| **Expert-SWE** (internal) | > GPT-5.4 | งานที่มนุษย์ใช้เวลา ~20 ชม. |
| **GDPval** | 84.9% | knowledge work, 44 อาชีพ |
| **OSWorld-Verified** | 78.7% | computer use |
| **Tau2-bench Telecom** | 98.0% | ไม่ต้องปรับ prompt |
| **BixBench** (bioinformatics) | 80.5% | นำ published model ทุกตัว |
| **CyberGym** | 81.8% | GPT-5.4 = 79.0%, Opus 4.7 = 73.1% |
| **FinanceAgent** | 60.0% | — |
| **Internal investment-banking modeling** | 88.5% | — |
| **OfficeQA Pro** | 54.1% | — |

## พฤติกรรมที่โดดเด่น (จาก testimonials ใน launch)

- **Conceptual clarity ในการเขียนโค้ด** — Dan (Every CEO) บอกว่าเป็นโมเดลแรกที่มี conceptual clarity จริงจัง; debug bug ที่ GPT-5.4 แก้ไม่ได้
- **Large-scale merge** — Pietro (MagicPath CEO) merge branch ที่มีการเปลี่ยนแปลงหลักร้อยครั้งเข้ากับ main ในครั้งเดียว ~20 นาที
- **Anticipatory reasoning** — จับปัญหาได้ล่วงหน้า คาดการณ์ความต้องการ test/review โดยไม่ต้องสั่ง
- **Multi-diff delivery** — ตัวอย่าง: ขอ re-architect comment ใน markdown editor แบบ collaborative = กลับมาพบ stack ที่มี 12 diff เกือบสมบูรณ์
- **Math discovery** — GPT-5.5 + harness พิเศษ ค้นพบบทพิสูจน์ใหม่เกี่ยวกับ off-diagonal Ramsey numbers (combinatorics) ซึ่ง verify ใน Lean แล้ว

## Access surfaces

- **ChatGPT**: Plus / Pro / Business / Enterprise
- **[[openai-codex|Codex]]**: Plus / Pro / Business / Enterprise / Edu / Go (400K ctx)
- **API** (เร็วๆ นี้): Responses + Chat Completions (1M ctx)
- **Fast mode**: token speed 1.5×, ราคา 2.5× — trade-off tier ที่ชัดเจนสำหรับงานที่ต้องรอ output

## ข้อควรระวัง

- **ราคาแพงขึ้น 2 เท่า** จาก GPT-5.4 — [[piyalitt-ittichaiwong|Piyalitt]] เตือนว่า prompt management / cost discipline จะสำคัญกว่าเดิมสำหรับ Coder
- **Pricing inversion vs Opus** — ปกติ GPT ถูกกว่า Opus ครึ่งหนึ่ง; ตอนนี้แพงกว่า → signal ว่า OpenAI ใช้ compute มากจริงเพื่อให้ทัน [[claude-mythos-preview|Mythos-class]] capability ในตลาด mass
- **ทำงานช้า** (Piyalitt's note) — capability มาพร้อมกับเวลารอ; งาน PhD ด้านการแพทย์ของเขาเกือบจบใน 1 prompt "ถ้ารอได้"
- **Cybersecurity: High** ตาม OpenAI Preparedness Framework — ไม่ถึง Critical แต่เป็น step up จาก GPT-5.4

## ดูเพิ่ม

- [[openai]]
- [[openai-codex]]
- [[piyalitt-gpt-5-5-launch]]
- [[claude-opus-4-7]]
- [[claude-mythos-preview]]
- [[kimi-k2-6]]
