---
title: Piyalitt Ittichaiwong — GPT-5.5 Launch Commentary
type: source
tags: [ai, models, openai, gpt, benchmarks, launch, thai]
created: 2026-04-24
updated: 2026-04-24
sources: [Piyalitt Ittichaiwong - GPT-5.5 Launch.md]
---

# Piyalitt Ittichaiwong — GPT-5.5 Launch Commentary

Facebook post (Thai) by [[piyalitt-ittichaiwong|Piyalitt Ittichaiwong]] on **2026-04-23 (~9 h before ingest 2026-04-24)**. Two layers: (1) his subjective reaction as a PhD researcher + 20-year programmer who had pre-release access, (2) a structured summary of OpenAI's official GPT-5.5 launch materials in Thai.

## Subjective reaction (layer 1)

- **เป็น Model แรกที่ทำให้ผู้เขียนรู้สึกว่า 20 ปีที่เรียน/เขียนโปรแกรมสู้มันไม่ได้** งาน PhD ด้านการแพทย์ของผู้เขียน "แทบจะจบใน 1 prompt" ถ้ารอได้ (ช้า)
- **เก่งใกล้ [[claude-mythos-preview|Claude Mythos Preview]] มากๆ** ยกเว้น **SWE-Bench Pro** ที่ใน model card ของ Anthropic ก็ flag ว่ามี sign ของ memorization — ผู้เขียนเชื่อว่าไม่ได้ตั้งใจ benchmaxx น่าจะพลาด
- แต่**เปิดให้ทุกคนเข้าถึงได้** (ต่างจาก Mythos Preview ที่จำกัดผ่าน [[project-glasswing|Project Glasswing]])
- **"Anthropic เหนื่อยแน่นอน"** — แม้แต่ frontend พอ GPT ใช้ gpt-image-2 ได้ ให้ design system GPT-5.5 ทำได้ดีกว่า
- **Pricing inversion**: GPT-5.5 **แพงกว่า Opus เล็กน้อย** ทั้งที่ปกติจะถูกกว่าประมาณครึ่งหนึ่ง → แปลว่าใช้ทรัพยากรมากจริง; Coder ต้องระวัง prompt management
- Event: Hackathon OpenAI × สมาคมปัญญาประดิษฐ์ประเทศไทย (เสาร์ที่กำลังจะถึง 2026-04-25; credit รวมเป็นล้าน)

## OpenAI launch summary (layer 2)

### Positioning
- OpenAI's smartest + easiest-to-use model; next step toward new way of working on computers
- Understands user intent faster; carries more of the load by itself
- Code + debug, internet research, data analysis, docs/spreadsheets, software use, cross-tool navigation until done

### Smarter without losing speed
- Same **per-token latency** as GPT-5.4 in real use, at much higher intelligence
- Uses **significantly fewer tokens** for the same Codex tasks

### Agentic coding
- **Terminal-Bench 2.0: 82.7%** (SOTA)
- **SWE-Bench Pro: 58.6%** — Anthropic card flags memorization signal; Piyalitt thinks unintentional mistake, not benchmaxx
- **Expert-SWE** (internal, ~20-hour-human tasks): beats GPT-5.4
- All three: score up, token use down vs GPT-5.4

### Structural understanding (testimonials)
- **Dan (CEO, Every)**: first coding model with serious *conceptual clarity*; time-travel debugged a post-launch issue GPT-5.4 couldn't
- **Pietro (CEO, MagicPath)**: merged a branch with hundreds of changes into a heavily-diverged main *in a single 20-minute run*
- **Senior engineer** testing: stronger than both GPT-5.4 and **Claude Opus 4.7** in reasoning + autonomy; anticipates test/review needs unprompted; re-architect-a-collaborative-markdown-comment-system request returned a stack of **12 near-complete diffs**

### Knowledge work benchmarks
- GDPval (44 occupations): **84.9%**
- OSWorld-Verified: **78.7%**
- Tau2-bench Telecom: **98.0%** (no prompt tuning)
- FinanceAgent: 60.0%; internal investment-banking modeling: 88.5%; OfficeQA Pro: 54.1%

### OpenAI internal deployment
- **85%+ of company** uses Codex weekly (eng, finance, comms, marketing, data science, PM)
- Finance: K-1 review — 24,771 forms / 71,637 pages, 2 weeks faster than prior year
- GTM: weekly business reports, 5–10 h/week saved

### Science research
- **GeneBench**: clearly above GPT-5.4
- **BixBench** (bioinformatics, real data analysis): **80.5%** — leads all published models
- Derya (Jackson Laboratory): gene expression 62 samples × ~28,000 genes → report his team would have needed *months* for
- Bartosz (Adam Mickiewicz University): algebraic-geometry app in 11 minutes from one prompt (visualize quadratic surface intersection, transform to Weierstrass model)
- Brandon (Axiom Bio): significant accuracy gains on hardest drug-discovery evals

### Math
- Internal GPT-5.5 + special harness → **new proof about off-diagonal Ramsey numbers** (combinatorics, long-standing asymptotic fact), subsequently verified in **Lean**

### Serving infrastructure
- Co-designed / trained / served on NVIDIA **GB200** and **GB300 NVL72**
- Codex + GPT-5.5 wrote custom heuristic splitter for production traffic patterns → **>20% token-generation speedup** (model improving the infra that serves it)

### Cybersecurity
- **Preparedness Framework: High** (not Critical) — step up from GPT-5.4
- **CyberGym: 81.8%** (vs GPT-5.4 79.0%, Claude Opus 4.7 73.1%)
- Largest safeguard suite OpenAI has shipped; ~200 early-access partners pre-launch

### Access & pricing
| Surface | Plans |
|---|---|
| ChatGPT GPT-5.5 | Plus / Pro / Business / Enterprise |
| ChatGPT GPT-5.5 Pro | Pro / Business / Enterprise |
| Codex | Plus / Pro / Business / Enterprise / Edu / Go; 400K context |
| Fast mode | +1.5× token speed at 2.5× price |
| API (coming soon) | `gpt-5.5` — **$5/M input, $30/M output**, 1M context |
| API Pro | `gpt-5.5-pro` — $30/M input, $180/M output |
| Batch/Flex | ½ standard API |
| Priority | 2.5× standard |

- **2× price of GPT-5.4**; slightly above [[claude-opus-4-7|Opus 4.7]] despite historically being ~½ — indicates real resource cost, not just margin
- Artificial Analysis Coding Agent Index: SOTA at ½ the price of rival frontier coding models

## Key takeaways for the wiki

1. **First model a PhD-level Thai engineer flags as "I can't compete"** — a useful primary-source datapoint on the subjective gradient from Opus 4.6 → 4.7 → Mythos-ish, not just benchmark deltas
2. **SWE-Bench Pro memorization sign** on GPT-5.5 — cross-referenced in Anthropic's own card. Adds evidence to treating SWE-Bench Pro skeptically as a ranking axis (already relevant to [[kimi-k2-6]] where the benchmark table was curated)
3. **Pricing inversion** (OpenAI > Anthropic on flagship, reversing historical pattern) — signals frontier-tier compute cost, not pricing power. Relevant when reasoning about [[model-choice-by-expertise]] and [[advisor-strategy]] cost math
4. **Opus 4.7 comparison**: senior-engineer testimonial places GPT-5.5 clearly above Opus 4.7 in reasoning/autonomy + CyberGym (81.8 vs 73.1). GPT-5.5 is *accessible* Mythos-class for most tasks
5. **Math-proof discovery** (Ramsey numbers, Lean-verified) — concrete new datapoint for AI-as-research-instrument beyond the Terence Tao-style anecdotes

## See also

- [[piyalitt-ittichaiwong]]
- [[openai]]
- [[gpt-5-5]]
- [[claude-opus-4-7]]
- [[claude-mythos-preview]]
- [[kimi-k2-6]] (the other 2026 "frontier coding model" launch; also flagged for curated benchmark handling)
