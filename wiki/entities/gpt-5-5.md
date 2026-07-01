---
title: GPT-5.5
type: entity
tags: [ai, models, openai, gpt]
created: 2026-04-24
updated: 2026-07-01
sources: [Piyalitt Ittichaiwong - GPT-5.5 Launch.md, Piyalitt Ittichaiwong - DeepSWE FrontierSWE Benchmark.md, Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md, https://openai.com/index/introducing-genebench-pro/]
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
| **[[claude-opus-4-8\|Claude Opus 4.8]]** | หลัง Opus 4.8 ออก (28 พ.ค. 2026) [[piyalitt-ittichaiwong\|Piyalitt]] เปลี่ยนใจว่า "Opus 4.8 โหดกว่า GPT-5.5 จริงๆ" โดยเฉพาะนิสัย [[missed-requirement\|ลืมข้อกำหนด]] ที่ลดลงมาก — เป็น**ความรู้สึกเชิงอัตวิสัย** ยังไม่มีการรัน [[deepswe\|DeepSWE]] เทียบ 4.8 (ก่อนหน้านี้ GPT-5.5 นำที่ 70% vs Opus 4.7 ที่ 54%); เขายังหยอกว่า "ไม่ได้โหดกว่า 5.6 นะ" |

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
| **[[deepswe\|DeepSWE]]** | **70% (อันดับ 1)** | benchmark ปลอดการปนเปื้อน; นำอันดับ 2 (gpt-5.4 ที่ 56%) อยู่ 14 จุด; ขึ้นจาก 59% บน SWE-Bench Pro |
| **[[genebench-pro\|GeneBench-Pro]]** | 12.0% (xhigh) | ตาม [[gpt-5-6-sol\|GPT-5.6 Sol]] ที่ 28.7% max / 31.5% Pro; ชี้ว่า coding strength กับ scientific judgement ไม่ใช่ axis เดียวกัน |

## ผลบน benchmark ที่ใกล้งานจริง (DeepSWE / FrontierSWE)

[[piyalitt-deepswe-benchmark|โพสต์ benchmark ของ Piyalitt]] (2026-05-27) ยืนยันว่า GPT-5.5 นำชัดเจนเมื่อ benchmark ออกแบบให้ใกล้งานจริง:

- **[[deepswe|DeepSWE]]: อันดับ 1 ที่ 70%** ห่างอันดับ 2 ถึง 14 จุด — ขณะที่ Opus 4.7 ตามมาที่ 54% ช่องว่างกว้างกว่าตาราง SWE-Bench Pro ที่ทำให้สองตัวดูสูสี
- **ประหยัดทรัพยากรที่สุด** — ทำ 70% ด้วย output token เฉลี่ยแค่ 47k (น้อยสุดในกลุ่ม) ใช้เวลา 20 นาที/ครั้ง, $5.8/ครั้ง; คะแนนสูงไม่ได้แลกมาด้วยการเผา token
- **ทำตามคำสั่งแม่นและคงเส้นคงวา** — อัตราพลาดข้อกำหนดต่ำสุดในกลุ่ม (ตรงข้ามกับ [[missed-requirement|นิสัยลืมข้อกำหนด]]ของ Claude); รันหลายรอบตีความ prompt ตรงกัน
- **ไม่โกง** — ไม่เคยกู้เฉลยจาก git history เลย (Opus ทำเกิน 12% ของ rollout บน SWE-Bench Pro — ดู [[reward-hacking]])
- **[[frontierswe|FrontierSWE]]: อันดับ 1** บน Codex เหนือ Opus 4.7 บน Claude Code — benchmark อิสระอีกตัวที่ให้ภาพเดียวกัน

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
- [[claude-opus-4-8]]
- [[claude-opus-4-7]]
- [[claude-mythos-preview]]
- [[genebench-pro]]
- [[kimi-k2-6]]
