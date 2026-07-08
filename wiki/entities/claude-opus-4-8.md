---
title: Claude Opus 4.8
type: entity
tags: [ai, models, anthropic, claude, opus, honesty, alignment]
created: 2026-05-29
updated: 2026-07-08
sources: [Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md, claude-in-microsoft-foundry.md]
---

# Claude Opus 4.8

โมเดล flagship ตัวใหม่ของ [[anthropic|Anthropic]] เปิดให้ใช้ทั่วไป **28 พฤษภาคม 2026** เป็นรุ่นต่อโดยตรงจาก [[claude-opus-4-7|Opus 4.7]] จุดที่ Anthropic ชูเป็นพระเอกไม่ใช่ความเก่งดิบ แต่เป็น **[[model-honesty|ความซื่อสัตย์]]** — โมเดลยอมบอกว่าไม่แน่ใจ และไม่รีบสรุปว่าทำสำเร็จทั้งที่หลักฐานยังบาง

**Model ID:** `claude-opus-4-8`
**ราคา:** $5 / 1M input tokens, $25 / 1M output tokens (เท่า Opus 4.7)
**ราคา fast mode:** $10 / 1M input, $50 / 1M output (fast mode เร็วขึ้น 2.5 เท่า และถูกลงกว่า fast mode รุ่นก่อน 3 เท่า)

> ที่มาในไฟล์นี้คือโพสต์สรุปภาษาไทยของ [[piyalitt-ittichaiwong|Piyalitt]] ([[piyalitt-opus-4-8-recap]]) ที่เล่าบทความเปิดตัวของ Anthropic ต่อ ตัวเลขเชิงลึกและการเทียบ benchmark ฉบับเต็มอยู่ใน System Card ของรุ่นนี้ ซึ่งยังไม่ได้ ingest เข้ามา

## ตำแหน่งเมื่อเทียบกับรุ่นอื่น

- **ดีกว่า [[claude-opus-4-7|Opus 4.7]]** ในการทดสอบหลายด้าน — coding, งานแบบ agentic, การใช้เหตุผล, และ knowledge work จริง Anthropic เรียกว่าการพัฒนาที่ "ไม่หวือหวา แต่จับต้องได้จริง"
- **Alignment ใกล้ [[claude-mythos-preview|Mythos Preview]]** — พฤติกรรม misaligned (หลอกลวง, ร่วมมือกับการใช้งานในทางที่ผิด) ต่ำกว่า 4.7 มาก จนเข้าใกล้ระดับ Mythos ที่เป็นโมเดล alignment ดีที่สุดของบริษัท
- ยังอยู่ใน tier เดียวกับ Opus — [[anthropic|Anthropic]] บอกว่ากำลังทำโมเดล "ฉลาดกว่า Opus" (ระดับ Mythos) ที่จะเปิดให้ลูกค้าทุกคนในไม่กี่สัปดาห์ข้างหน้า

## จุดเด่นหลัก: ความซื่อสัตย์ (Honesty)

ดูแนวคิดเต็มที่ [[model-honesty]]

- ปัญหา AI ทั่วไป: รีบสรุปและกล่าวอ้างอย่างมั่นใจว่างานคืบหน้า **ทั้งที่หลักฐานยังบาง** ([[model-honesty|overclaiming progress]])
- Opus 4.8 **ยอมบอกความไม่แน่ใจเกี่ยวกับงานตัวเองมากขึ้น** และกล่าวอ้างแบบไม่มีหลักฐานรองรับน้อยลง (รายงานจาก early testers + ผลประเมินภายใน)
- ตัวเลขเด่น: **ปล่อยให้ bug ใน code ที่ตัวเองเขียนผ่านไปโดยไม่ทักท้วง น้อยกว่ารุ่นก่อนราว 4 เท่า** — แก้จุดอ่อน "weak success criteria" ใน [[llm-coding-pitfalls]] โดยตรง และต่อยอด self-verification ที่เริ่มใน [[claude-opus-4-7|4.7]]

## สิ่งที่ปรับปรุงขึ้นจาก Opus 4.7

| ด้าน | การเปลี่ยนแปลง |
|---|---|
| **ความซื่อสัตย์ (Honesty)** | จุดขายหลัก — บอกความไม่แน่ใจมากขึ้น, overclaim น้อยลง, ปล่อย bug ตัวเองผ่านน้อยลง ~4 เท่า |
| **Alignment** | สถิติสูงสุดใหม่ด้าน prosocial traits (สนับสนุน user autonomy, ทำเพื่อประโยชน์ผู้ใช้); misaligned behavior ต่ำกว่า 4.7 มาก |
| **งาน agentic** | น่าเชื่อถือขึ้น, ดุลพินิจคมขึ้น, ทำงานเป็นขั้นเป็นตอนแทนเราได้ดีกว่าเดิม |
| **Coding / reasoning / knowledge work** | ดีขึ้นในหลาย benchmark (รายละเอียดใน System Card) |
| **Effort เริ่มต้น** | ลดจาก `xhigh` (4.7 ใน Claude Code) เหลือ `high` — ใช้ token พอๆ กับค่าเริ่มต้น 4.7 แต่ผลดีกว่า |

## ฟีเจอร์ใหม่ที่เปิดตัวพร้อมกัน

- **[[effort-levels|effort control]]** — ปุ่มควบคุมข้าง model selector บน claude.ai และ Cowork; เลือกได้ว่าจะให้ Claude ทุ่มแค่ไหน (สูง = คิดลึกขึ้น, ต่ำ = ตอบเร็ว + กิน rate limit ช้าลง) เปิดทุกแพ็กเกจ
- **[[dynamic-workflows|dynamic workflows]]** — ฟีเจอร์ใน [[claude-code|Claude Code]] (research preview): Claude วางแผนงานใหญ่เอง สั่ง subagents คู่ขนานเป็นร้อยตัวในเซสชันเดียว ตรวจผลตัวเองก่อนรายงาน; ตัวอย่างคือ migrate codebase หลายแสนบรรทัดตั้งแต่เริ่มจนถึง merge โดยใช้ test suite เป็นเกณฑ์ เปิดให้ Enterprise / Team / Max
- **[[system-in-messages|system ใน messages array]]** — Messages API ใส่ `system` ใน array ของ messages ได้ อัปเดตคำสั่ง / สิทธิ์ / งบ token / ข้อมูล environment กลางคันได้โดยไม่พัง prompt cache
- **fast mode** — เร็วขึ้น 2.5 เท่า, ราคาถูกลงกว่ารุ่นก่อน 3 เท่า

## effort levels (ณ Opus 4.8)

- ค่าเริ่มต้น = **`high`** (Anthropic ว่าเป็นจุดสมดุลที่ดีสุด)
- **`extra`** (= `xhigh` ใน Claude Code) และ **`max`** ให้ผลดีขึ้นแลกกับ token มากขึ้น — แนะนำ `extra` กับงานยากและงาน asynchronous ที่รันยาว
- Claude Code เพิ่ม rate limit แล้วเพื่อรองรับ effort สูง
- ดูรายละเอียดและความต่างจาก 4.7 ที่ [[effort-levels]]

## ความสัมพันธ์กับ Mythos / Project Glasswing

- [[anthropic|Anthropic]] บอกว่ากำลังทำสองทาง: (1) โมเดลความสามารถใกล้ Opus แต่ราคาถูกลง, (2) โมเดล **ฉลาดกว่า Opus** (ระดับ [[claude-mythos-preview|Mythos]])
- ภายใต้ [[project-glasswing|Project Glasswing]] ตอนนี้มีองค์กรจำนวนหนึ่งใช้ Mythos Preview สำหรับงาน cybersecurity อยู่แล้ว
- timeline ขยับ: คาดว่าจะ **นำโมเดลระดับ Mythos มาให้ลูกค้าทุกคนได้ภายในไม่กี่สัปดาห์ข้างหน้า** — ก่อนหน้านี้บอกแค่ว่าจะปล่อยมาตรการป้องกันใหม่ "พร้อม Opus model ที่กำลังจะมาถึง" (ซึ่งตอนนี้ก็คือ Opus 4.8 นี่เอง)

## ช่องทางการใช้งาน

- ผลิตภัณฑ์ Claude (claude.ai, Cowork, [[claude-code|Claude Code]])
- Claude API (`claude-opus-4-8`)
- เปิดให้ใช้ "ทุกที่" ตั้งแต่วันประกาศ
- **[[microsoft-foundry|Microsoft Foundry]]** — generally available บน [[azure|Azure]] ตั้งแต่ 2026-06-29 (คู่กับ Claude Haiku 4.5) ผ่าน Messages API รองรับ prompt caching + extended thinking; ดู [[claude-in-microsoft-foundry]]

## ดูเพิ่ม

- [[claude]]
- [[anthropic]]
- [[claude-opus-4-7]]
- [[claude-mythos-preview]]
- [[model-honesty]]
- [[dynamic-workflows]]
- [[effort-levels]]
- [[piyalitt-opus-4-8-recap]]
