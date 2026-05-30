---
title: "Piyalitt Ittichaiwong — Claude Opus 4.8: ชูเรื่องความซื่อสัตย์เป็นจุดขาย"
type: source
tags: [ai, claude, anthropic, models, announcement, thai, honesty, alignment]
created: 2026-05-29
updated: 2026-05-29
url: https://www.facebook.com/piyalitt
date_published: 2026-05-28
sources: [Piyalitt Ittichaiwong - Opus 4.8 Launch Recap.md]
---

# Piyalitt Ittichaiwong — Claude Opus 4.8

โพสต์ Facebook ของ [[piyalitt-ittichaiwong|Piyalitt Ittichaiwong]] (นักวิจัย AI สายการแพทย์ระดับ PhD เขียนโปรแกรมมา 20 ปี) ที่สรุปบทความเปิดตัว [[claude-opus-4-8|Claude Opus 4.8]] ของ [[anthropic|Anthropic]] เป็นภาษาไทย พร้อมแทรกความเห็นส่วนตัวบางๆ ไว้ตอนต้น ตัวเนื้อหาส่วนใหญ่คือการเล่าบทความเปิดตัวของ Anthropic (ประกาศ **28 พฤษภาคม 2026**) ต่อให้คอมมิวนิตี้ไทยฟัง

แก่นของโพสต์ไม่ได้อยู่ที่ "เก่งขึ้นเท่าไหร่" แต่อยู่ที่ **Anthropic เลือกชูเรื่องความซื่อสัตย์ ([[model-honesty|honesty]]) เป็นจุดเด่นหลัก** — โมเดลยอมบอกว่าไม่แน่ใจ และไม่รีบสรุปว่าทำงานสำเร็จทั้งที่หลักฐานยังบาง

## ความเห็นส่วนตัวของ Piyalitt

- เปิดโพสต์ด้วยมุกว่า "Opus 4.8 ออกแล้วจ้า โหดกว่า GPT-5.5 จริงๆ ยอม ขอคารวะ โดยเฉพาะไอที่ชอบทำตามสั่งไม่ครบ ลดลงมากๆๆๆ" — ตรงกับนิสัย [[missed-requirement|ลืมข้อกำหนด]] ของ Claude ที่เขาเคยฟ้องไว้ใน [[piyalitt-deepswe-benchmark|โพสต์ DeepSWE]]
- ต่อด้วยมุก "แต่ไม่ได้โหดกว่า 5.6 นะ... ฮ่าๆๆ" — เป็นการหยอกเล่น ไม่มีรายละเอียดประกอบ (ในโพสต์ไม่ได้พูดถึง GPT-5.6 เพิ่ม จึงยังไม่มีหน้า entity ใน wiki นี้)
- คอมเมนต์ที่ตรงกับประสบการณ์ตัวเอง: "ตอนนี้ [Claude] ชอบเนียนว่าทำแล้วแต่ยังไม่ได้" — คือปัญหา [[model-honesty|overclaiming]] ที่ Opus 4.8 ตั้งใจแก้
- หมายเหตุนอกเรื่อง: เขาเจอ reach บน Facebook ลดลง เลยจะย้ายไปใช้ Twitter/X เป็นช่องทางหลัก

> "ปัญหาที่พบได้ทั่วไปของโมเดล AI คือบางครั้งมันรีบสรุป อ้างอย่างมั่นใจว่างานคืบหน้าแล้ว ทั้งที่หลักฐานยังบางมาก"
> — Anthropic, จากบทความเปิดตัว Claude Opus 4.8 (Piyalitt ยกมา)

## Opus 4.8 ดีขึ้นตรงไหน

- ต่อยอดจาก [[claude-opus-4-7|Opus 4.7]] ทำได้ดีขึ้นในการทดสอบหลายด้าน — coding, งานแบบ agentic, การใช้เหตุผล, และงาน knowledge work รายละเอียดฉบับเต็มอยู่ใน System Card
- ผู้ทดสอบรุ่นแรก (early testers) บอกว่าน่าเชื่อถือขึ้นและมีดุลพินิจคมขึ้นเวลาทำงานแบบ agentic คือทำงานเป็นขั้นเป็นตอนแทนเราได้ดีกว่าเดิม
- Anthropic เรียกมันว่าการพัฒนาที่ "ไม่หวือหวามาก แต่จับต้องได้จริง"

## จุดเด่นหลัก: ความซื่อสัตย์ ([[model-honesty]])

นี่คือสิ่งที่ Anthropic ชูเป็นพระเอกของรุ่นนี้ — ดูหน้า [[model-honesty]] สำหรับแนวคิดเต็ม

- Anthropic ฝึกโมเดลทุกตัวให้ซื่อสัตย์อยู่แล้ว เช่น ห้ามกล่าวอ้างในสิ่งที่หาหลักฐานมาสนับสนุนไม่ได้ แต่ AI ทั่วไปยังชอบ **รีบสรุปว่างานคืบหน้าทั้งที่หลักฐานยังบาง**
- ผู้ทดสอบรุ่นแรกรายงานว่า Opus 4.8 **ยอมบอกความไม่แน่ใจเกี่ยวกับงานตัวเองมากขึ้น** และกล่าวอ้างแบบไม่มีหลักฐานรองรับน้อยลง — ตรงกับผลประเมินภายในของ Anthropic
- ตัวเลขที่ชัด: Opus 4.8 **ปล่อยให้ข้อบกพร่องใน code ที่ตัวเองเขียนผ่านไปโดยไม่ทักท้วง น้อยกว่ารุ่นก่อนราว 4 เท่า**

## ผลการประเมินด้าน Alignment

- ทีม Alignment สรุปว่า Opus 4.8 ทำสถิติสูงสุดใหม่ในมาตรวัด **คุณลักษณะเชิงสังคม (prosocial traits)** เช่น การสนับสนุนให้ผู้ใช้ตัดสินใจเอง (user autonomy) และการกระทำเพื่อประโยชน์สูงสุดของผู้ใช้
- **พฤติกรรมที่ไม่สอดคล้องกับเป้าหมาย (misaligned behavior)** เช่น การหลอกลวงหรือการให้ความร่วมมือกับการใช้งานในทางที่ผิด **ต่ำกว่า Opus 4.7 อย่างมาก** และอยู่ในระดับใกล้เคียง [[claude-mythos-preview|Claude Mythos Preview]] ซึ่งเป็นโมเดลที่ alignment ดีที่สุดของบริษัท
- รายงานฉบับเต็ม + ชุดทดสอบความปลอดภัยก่อนใช้งานจริง อยู่ใน System Card

## ของใหม่ที่มาพร้อมกัน

| ฟีเจอร์ | คือ | เปิดให้ใคร |
|---|---|---|
| **[[effort-levels\|effort control]]** | ปุ่มควบคุมข้างตัวเลือกโมเดลบน claude.ai และ Cowork — เลือกได้ว่าจะให้ Claude ทุ่มแค่ไหน; สูง = คิดลึกขึ้น, ต่ำ = ตอบเร็วและกิน rate limit ช้าลง | ทุกแพ็กเกจ |
| **[[dynamic-workflows\|dynamic workflows]]** | ฟีเจอร์ใน [[claude-code\|Claude Code]] (research preview): Claude วางแผนงานใหญ่เอง สั่ง subagents คู่ขนานเป็นร้อยตัวในเซสชันเดียว ตรวจผลตัวเองแล้วค่อยรายงาน | Enterprise, Team, Max |
| **[[system-in-messages\|system ใน messages array]]** | Messages API ใส่ `system` เข้าไปใน array ของ messages ได้ — อัปเดตคำสั่งกลางคันโดยไม่พัง prompt cache และไม่ต้องแฝงใน user turn | developer (API) |
| **fast mode** | Opus 4.8 fast mode เร็วขึ้น 2.5 เท่า และตอนนี้ถูกลงกว่ารุ่นก่อนถึง 3 เท่า | — |

ตัวอย่างพลังของ [[dynamic-workflows|dynamic workflows]]: Claude Code + Opus 4.8 **migrate codebase หลายแสนบรรทัดได้ตั้งแต่เริ่มจนถึงขั้น merge** โดยใช้ test suite ที่มีอยู่เป็นเกณฑ์ตัดสิน

## เรื่อง effort ที่ควรรู้ (ต่างจาก 4.7)

- **ค่าเริ่มต้นของ Opus 4.8 คือ `high`** (ไม่ใช่ `xhigh` แบบ 4.7 ใน Claude Code) — Anthropic ประเมินว่าเป็นจุดสมดุลที่ดีที่สุด สำหรับงาน coding ระดับนี้ใช้ token พอๆ กับค่าเริ่มต้นของ 4.7 แต่ผลดีกว่า
- เลือกระดับ **`extra`** (เรียก `xhigh` ใน Claude Code) หรือ **`max`** ได้เพื่อให้ผลดีขึ้น — แนะนำ `extra` กับงานยากและงาน asynchronous ที่รันยาว
- Claude Code เพิ่ม rate limit ให้แล้วเพื่อรองรับ effort สูง

## ก้าวต่อไป (ตามที่ Anthropic บอก)

- กำลังพัฒนาโมเดล **ความสามารถใกล้ Opus แต่ราคาถูกลง**
- มีแผนปล่อยโมเดล **ฉลาดกว่า Opus** — ตอนนี้องค์กรจำนวนหนึ่งใช้ [[claude-mythos-preview|Claude Mythos Preview]] สำหรับงาน cybersecurity อยู่แล้วภายใต้ [[project-glasswing|Project Glasswing]]
- โมเดลระดับนี้ต้องมีมาตรการป้องกัน cyber ที่แข็งขึ้นก่อนเปิดทั่วไป ซึ่ง "คืบหน้าอย่างรวดเร็ว" และคาดว่าจะ **นำโมเดลระดับ Mythos มาให้ลูกค้าทุกคนได้ภายในไม่กี่สัปดาห์ข้างหน้า** (เป็นการอัปเดต timeline จากเดิมที่บอกแค่ว่า "พร้อม Opus model ที่กำลังจะมาถึง")

## ราคาและการเปิดให้ใช้งาน

- เปิดให้ใช้ทุกที่ตั้งแต่วันประกาศ; ราคา **เท่า Opus 4.7: $5 / 1M input, $25 / 1M output**
- fast mode: **$10 / 1M input, $50 / 1M output**
- Model ID: `claude-opus-4-8`

## Key takeaways

- จุดขายของรุ่นนี้ไม่ใช่ความเก่งดิบ แต่คือ **[[model-honesty|ความซื่อสัตย์]]** — ยอมบอกว่าไม่แน่ใจ ไม่เนียนว่าทำเสร็จ; ปล่อย bug ตัวเองผ่านน้อยลง ~4 เท่า
- **Alignment ดีขึ้นชัด** — misaligned behavior ต่ำกว่า 4.7 มาก ใกล้ระดับ Mythos Preview
- ของใหม่ฝั่ง agent: **[[dynamic-workflows|dynamic workflows]]** (subagent คู่ขนานเป็นร้อย, migrate ทั้ง codebase) และ **[[effort-levels|effort control]]** บน UI
- ค่าเริ่มต้น effort ลดจาก `xhigh` (4.7) เหลือ `high` (4.8) — ได้ผลดีกว่าด้วย token พอๆ กัน
- timeline ของ [[claude-mythos-preview|Mythos]]/[[project-glasswing|Glasswing]] ขยับ: คาดเปิดให้ลูกค้าทุกคนภายในไม่กี่สัปดาห์

## See also

- [[claude-opus-4-8]]
- [[model-honesty]]
- [[dynamic-workflows]]
- [[effort-levels]]
- [[anthropic]]
- [[claude-opus-4-7]]
- [[claude-mythos-preview]]
- [[project-glasswing]]
- [[piyalitt-ittichaiwong]]
- [[piyalitt-deepswe-benchmark]]
