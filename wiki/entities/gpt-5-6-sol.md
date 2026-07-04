---
title: GPT-5.6 Sol
type: entity
tags: [ai, models, openai, gpt, science]
created: 2026-07-01
updated: 2026-07-05
sources: [https://openai.com/index/introducing-genebench-pro/, piyalitt-codex-keynote-attention-not-token.md]
---

# GPT-5.6 Sol / ตระกูล GPT-5.6

[[openai|OpenAI]] model ในตระกูล **GPT-5.6** — หน้านี้รวมข้อมูลจาก [[introducing-genebench-pro|GeneBench-Pro]] และ keynote Codex ที่ [[ai-engineer-worlds-fair|AI Engineer World's Fair]] (สรุป [[piyalitt-codex-keynote-attention-not-token]]). ตัวเลขจาก keynote ยัง source-attributed จนกว่าจะตรวจจาก OpenAI โดยตรง

## ผลบน GeneBench-Pro

บน [[genebench-pro|GeneBench-Pro]] ซึ่งวัด scientific judgement ใน computational biology:

| Mode | Pass rate |
|---|---:|
| highest/max reasoning | 28.7% |
| Pro mode | 31.5% |

OpenAI บอกว่า highest reasoning ของ GPT-5.6 Sol แก้โจทย์ได้เกือบ 6 เท่าของ GPT-5.2 และใช้ token ประมาณสองในสามของ GPT-5.2 ในระดับ reasoning สูงสุด

## Pattern ที่ OpenAI ยก

ในโจทย์ pharmacogenomic time-to-event response, GPT-5.6 Sol เลือก new-user marginal structural Cox model พร้อม stabilized inverse-probability weights และ 90-day efficacy lag เพื่อจัดการ treatment-confounder feedback

ความหมายคือ model ไม่ได้แค่รัน method ที่รู้จัก แต่ปรับ causal inference strategy ตาม data structure ซึ่งเป็นตัวอย่างของ [[research-taste|research taste]]

## ตระกูล 5.6 บนเวที Codex (source-attributed)

จาก [[piyalitt-codex-keynote-attention-not-token]] ทีม Codex ยกตัวอย่างในกรอบ [[value-maxing|value maxing]]:

| Variant | Claim บนเวที |
|---|---|
| **Terra** | ความฉลาดระดับ [[gpt-5-5\|GPT-5.5]] ในราคาครึ่งเดียว |
| **Luna** | ชนะ model ดังหลายตัว ราคา $1/1M input, $6/1M output |
| Frontier บน Cerebras | 750 token/วินาที — เปิดใช้เดือนถัดไป |
| รุ่นบนสุดตระกูล 5.6 | ขึ้นนำ Terminal Bench (ตามกราฟบนเวที) |

OpenAI preview ตระกูล 5.6 สัปดาห์ก่อนงาน World's Fair — สอดคล้องกับจังหวะปล่อย model ใหม่ทุก ~6 สัปดาห์ (เคยทุก ~15 เดือน)

## ข้อควรระวัง

หน้านี้รวมข้อมูลจาก GeneBench-Pro (OpenAI blog) และ keynote summary ผ่าน Piyalitt — ยังไม่ควรสรุป capability กว้าง ๆ นอกเหนือจากแหล่งเหล่านี้. ชื่อ variant (Terra, Luna) และตัวเลขราคา/ความเร็วจาก keynote ควรตรวจกับเอกสาร OpenAI ก่อนอ้างเป็นข้อเท็จจริง

## See also

- [[openai]]
- [[genebench-pro]]
- [[introducing-genebench-pro]]
- [[research-taste]]
- [[gpt-5-5]]
- [[value-maxing]]
- [[piyalitt-codex-keynote-attention-not-token]]
