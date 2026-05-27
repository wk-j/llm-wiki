---
title: I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Changed.
type: source
tags: [ai, harness, coding, benchmarks, tools, open-source]
url: https://blog.can.ac/2026/02/12/the-harness-problem/
date_ingested: 2026-05-27
created: 2026-05-27
updated: 2026-05-27
sources: [I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Changed..md]
---

# I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Changed. / ปรับ harness ครั้งเดียว — 15 ตัว model เก่งขึ้น

บทความของ [[can-boluk|Can Bölük]] (ก.พ. 2026, cross-post จาก X @_can1357) เถียงกับกระแสที่ถกแค่ว่า "model ไหนเขียนโค้ดเก่งกว่า" — ของเขาคือ **bottleneck ตัวจริงอยู่ที่ harness** ต่างหาก ชั้นระหว่าง model กับ workspace ที่คุม tool schema, error message, state, และทุก input token ที่ป้อนเข้า model

Can ดูแล [[oh-my-pi|oh-my-pi]] (fork ของ [[pi-agent|pi]] จาก [[mario-zechner|Mario Zechner]]) เป็น hobby harness แบบ model-agnostic — ใช้เป็นสนามทดลอง โดยให้ model เป็นแค่พารามิเตอร์หนึ่ง บทความนี้เล่า experiment ที่เปลี่ยนแค่ **edit tool** แล้ววัด 16 model

## 0x0: คำถามผิด

การถกว่า GPT-5.3 vs Opus vs Gemini รุ่นใหม่ตัวไหนเก่งกว่า **มอง model เป็นตัวแปรเดียว** ทั้งที่ harness คุม first impression (scroll ลั่นหรือลื่น), เป็นแหล่งของทุก input token, และเป็น interface ระหว่าง output ของ model กับการเปลี่ยน workspace จริง

Can ยกตัวอย่างว่า [[claude-code|Claude Code]] ยัง leak raw JSONL จาก sub-agent output กลับเข้า context ทำให้เสีย token หลักแสน — ใน oh-my-pi เขาเปลี่ยนให้ subagent ส่ง structured data แทน จุดอย่าง tool schema, error message, state management นี่แหละที่ failure ส่วนใหญ่เกิดจริง — คือช่องว่างระหว่าง "model รู้ว่าจะแก้อะไร" กับ "issue ปิดจริง"

**ได้อะไร:** อยากได้ coding agent ที่ดีขึ้น อย่าเพิ่งจ้องแค่ model leaderboard — ดู tool boundary ก่อน

## 0x1: สถานะ edit tool ในอุตสาหกรรม

Can สรุป landscape ของ "จะแก้ไฟล์ยังไง" ก่อนเสนอ [[hashline|Hashline]]:

| แนวทาง | ใครใช้ | จุดแข็ง | จุดอ่อน |
|---|---|---|---|
| **`apply_patch`** (OpenAI-flavored diff string) | [[openai-codex|Codex]] | อาจถูก bias ที่ gateway สำหรับ Codex variants | model อื่นล้มเยอะ — Grok 4 patch failure ~50.7%, GLM-4.7 ~46.2% |
| **`str_replace`** (หา old text ตรงตัวอักษร แล้วแทน) | [[claude-code]], ส่วนใหญ่ | คิดง่าย | ต้อง reproduce whitespace เป๊ะ; หลาย match = reject; error "String to replace not found" เป็นประจำ |
| **Fine-tuned merge model (70B)** | Cursor | แยก model มา merge draft edit | ยังบอกใน blog ว่า rewrite ทั้งไฟล์ชนะ diff สำหรับไฟล์ <400 บรรทัด |
| **Unified diff (Aider)** | Aider | format เดียวกันช่วย GPT-4 Turbo 26%→59% | GPT-3.5 แค่ 19% — format ไม่พอถ้า model สร้าง diff ไม่ได้ |

Benchmark ภายนอกก็ยืนยันว่าไม่มี format ไหนชนะทุก model: **Diff-XYZ** (JetBrains), **EDIT-Bench** (มีแค่ model เดียวที่เกิน 60% pass@1)

ข้อสรุปของ Can: ทุกแนวต้องให้ model **จำ content ที่เคยอ่านแล้วพิมพ์กลับออกมา** — ไม่มี stable, verifiable identifier ที่บอกได้ว่าจะแก้บรรทัดไหนโดยไม่กิน context เพิ่ม พอพลาดผู้ใช้ก็โทษ model ทั้งที่เป็น mechanical failure

ดูรายละเอียดที่ [[edit-tool-formats]]

## 0x2: Hashline

พอ model อ่านไฟล์หรือ grep แต่ละบรรทัดจะติด tag แบบ `line:hash|content` มาด้วย:

```fallback
1:a3|function hello() {
2:f1|  return "world";
3:0e|}
```

ตอน edit ก็อ้าง tag — replace `2:f1`, replace range `1:a3`–`3:0e`, insert after `3:0e` ถ้าไฟล์เปลี่ยนหลัง read แฮชไม่ตรง harness reject ก่อนเขียน

**หลักคิด:** ถ้า model จำ pseudo-random tag ได้ ก็แปลว่ารู้จริงว่ากำลังแก้ตรงไหน — ไม่ต้องคัดลอก old content หรือ whitespace มาพิสูจน์

## 0x3: Benchmark (react-edit-benchmark)

**Fixtures:** สุ่มไฟล์จาก React codebase → ใส่ mutation แบบ bug (operator swap, boolean flip, off-by-one, ลบ optional chain, rename) → สร้างคำอธิบายภาษาอังกฤษ

**Protocol:** 3 runs/task, 180 tasks/run, session ใหม่ทุกครั้ง, 4 tools (read, edit, write), เทียบไฟล์หลัง format

**16 models × 3 formats:** Patch, Replace (`str_replace`), Hashline (+ Hashline v2)

ผลหลัก:

- **Patch แย่ที่สุด** เกือบทุก model
- **Hashline ชนะหรือเสมอ Replace** ส่วนใหญ่; **Hashline v2** ดีขึ้นอีก 12/16
- **Model อ่อนยิ่งได้เยอะ** — Grok Code Fast 1: 6.7% → 68.3%; MiniMax มากกว่า 2×; Grok 4 Fast ลด output token ~61% (เลิกวน retry)
- **Gemini 3 Flash:** +8pp success, −21% output tokens
- **DeepSeek V3.2:** Hashline แย่กว่า Replace เล็กน้อย (เป็นข้อยกเว้น)

> "Hashline outperforms Patch in 14/16 models."

โค้ดและรายงาน: [oh-my-pi react-edit-benchmark](https://github.com/can1357/oh-my-pi/tree/main/packages/react-edit-benchmark)

## 0x4: แล้วมันหมายความว่าอะไร

> "+8% improvement in the success rate of Gemini is bigger than most model upgrades deliver, and it cost zero training compute."

ส่วนใหญ่ไม่ใช่ว่า model ไม่เข้าใจงาน แต่ **แสดงออกมาไม่ได้** — เหมือนโทษ pilot ทั้งที่ landing gear พัง

**ได้อะไร:** ตอนนี้ปรับ harness ที่ tool boundary คุ้มที่สุด — Can ใช้แค่ ~$300 ก็รัน benchmark ได้

## 0x5: มุม vendor และ open harness

Can โยงกับเหตุการณ์ **Anthropic บล็อก [[opencode|OpenCode]]** จาก Claude Code subscription ว่าเป็นสัญญาณ "อย่าสร้าง harness เอง มาใช้ของเรา" และ Google ที่ **ปิดบัญชี Gemini ของเขาทั้งบัญชี** ขณะรัน benchmark (ไม่ใช่ rate limit) หลัง Gemini 3 Flash ได้ 78.3% ด้วยเทคนิคที่ดีกว่า harness ของ Google ~5pp

แต่ Can เถียงว่าการปรับ edit format ช่วย **model ของ vendor เอง** 5–14 points แถมลด token ~20% — น่าจะเป็น free R&D ให้ ไม่ใช่ภัย Vendor ไม่ปรับ harness ให้ model คู่แข่งหรอก แต่ **open-source harness ปรับให้ทุก model อยู่แล้ว** เพราะ contributor แต่ละคนใช้ model ต่างกัน

> "The model is the moat. The harness is the bridge. Burning bridges just means fewer people bother to cross."

เปรียบกับวงการ game security: ทีมป้องกันยังจ้าง cheater มาช่วยเลย — พอ third-party harness เริ่มมี traction ท่าที่ถูกคือ "เล่าให้ฟังหน่อย" ไม่ใช่ blanket ban

**ผลคือ:** ช่องว่างระหว่าง demo สวยกับ tool ใช้จริงได้ ไม่ใช่เรื่อง model magic แต่เป็น **empirical engineering น่าเบื่อ ๆ ที่ tool boundary** — จะแก้โดยบริษัทเดียวแบบ private ก็ได้ หรือให้ชุมชน open-source ช่วยกันแก้ให้ทุก model ก็ได้

## อ้างอิงหลัก

| อ้างอิง | เนื้อหา |
|---|---|
| Diff-XYZ | arXiv:2510.12487 — ไม่มี edit format ชนะทุก model/use case |
| EDIT-Bench | arXiv:2511.04486 — realistic editing; <60% pass@1 ส่วนใหญ่ |
| Aider benchmarks | format choice เปลี่ยน GPT-4 Turbo 26%→59% |
| Cursor Instant Apply | fine-tuned 70B; full rewrite ชนะ diff ไฟล์สั้น |

## See also

- [[can-boluk]]
- [[oh-my-pi]]
- [[hashline]]
- [[edit-tool-formats]]
- [[coding-harness]]
- [[agent-harness-engineering]]
- [[alex-ker-harnesses-optimize]]
- [[opencode]]
- [[pi-agent]]
- [[llm-coding-pitfalls]]
