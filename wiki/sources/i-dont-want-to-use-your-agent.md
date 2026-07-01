---
title: "i don't want to use your agent — Rhys Sullivan"
type: source
tags: [ai, agents, harness, mcp, skills, product, developer-tools]
created: 2026-06-29
updated: 2026-06-29
sources: ["i don't want to use your agent — @RhysSullivan.md"]
---

# i don't want to use your agent — Rhys Sullivan / ฉันไม่อยากใช้ agent ของคุณ

โพสต์ X ของ [[rhys-sullivan|Rhys Sullivan]] ([@RhysSullivan](https://x.com/RhysSullivan/status/2070989582850793947)) เผยแพร่ 2026-06-27 UTC / 2026-06-28 เวลาไทย. แกนของโพสต์คือ **ไม่ได้ปฏิเสธ in-app agent**. เขาบอกตรง ๆ ว่าการคุยกับเว็บผ่าน agent นั้น magical. แต่เขาไม่อยากใช้ *agent ของแต่ละบริษัท* เป็นตัวหลัก.

เขาอยากใช้ agent ประจำวันของตัวเอง แล้วให้ agent ตัวนั้นเข้าถึงความรู้, skill, API, และ product surface ของบริษัทต่าง ๆ ได้. แก่นนี้ถูกดึงเป็นหน้า [[bring-your-own-agent]].

## ปัญหาที่เขาเห็น

โพสต์เปิดจากภาพรวมว่าแทบทุกบริษัทเริ่มมี agent ของตัวเองแล้ว. มี agent ใน dashboard ของ [[cloudflare|Cloudflare]] (แพลตฟอร์ม edge/cloud), agent ของ [[posthog|PostHog]] (product analytics), agent ของ Mercury, agent ของ [[linear|Linear]] (issue tracker), และอื่น ๆ. หน้า homepage ของหลายบริษัทค่อย ๆ กลายเป็น chat interface.

ตรงนี้ไม่ใช่เรื่องแย่. ปัญหาคือ power user ไม่ได้อยากย้ายเข้า chat ของทุก product.

## Incentives / แรงจูงใจเรื่องต้นทุน

เหตุผลแรกคือ incentive. ผู้ใช้สายหนักอาจจ่ายเงินเองเพื่อใช้ frontier model เช่น Opus หรือ GPT รุ่นแรง. แต่บริษัท SaaS ที่ให้ agent ฟรีหรือรวมมากับ subscription อาจแบกราคา model ระดับนั้นให้ user ทุกคนตลอดเวลาไม่ได้.

ผลคือ in-app agent หลายตัวอาจใช้ model ที่ถูกกว่า, quantized, หรือ route ผ่าน model ที่พอทำงานได้แต่ไม่ใช่ตัวที่ผู้ใช้เลือกเอง. ประโยคสำคัญของโพสต์คือ:

> "i'm paying for the best models, i want to use the best models for my work"

ความหมายคือ ถ้าผู้ใช้จ่ายเงินเพื่อ model ที่ดีที่สุดอยู่แล้ว เขาไม่อยากถูกลดเพดานลงเพราะ product chat เลือก model ประหยัดกว่า.

## Context / agent ในเว็บเห็นโลกไม่พอ

เหตุผลที่สองคือ context. ตอนอยู่ใน Linear agent บน web UI ตัว agent ไม่ได้เห็น local files, random git repositories, terminal setup, scripts, หรือ memory ส่วนตัวของผู้ใช้.

บริษัทอาจสร้าง integration เพิ่มได้ แต่ยากที่จะชนะ setup local ที่ power user ปรับเองมานาน. ตรงนี้เชื่อมกับ [[agent-experience|AX]] โดยตรง: agent ที่ดีไม่ได้มีแค่ model แรง แต่ต้องอยู่ใน environment ที่เห็นของจริงและแตะเครื่องมือจริงได้.

## สิ่งที่เขาต้องการ

เขาไม่ได้ขอให้บริษัทเลิกทำ agent. เขาขอให้บริษัททำให้ **agent ของผู้ใช้กลายเป็น expert ใน product และ problem area ของบริษัทนั้น**.

ตัวอย่างที่เขาให้:

- [[linear|Linear]]: skill สำหรับแตกปัญหาใหญ่ให้เป็น ticket ที่ทำได้จริง
- [[cloudflare|Cloudflare]]: docs ละเอียด, product surface ที่ agent เข้าใจ, และ CLI commands ที่รันได้
- [[posthog|PostHog]]: data ที่ query ได้, deeplink ไป UI component เพื่อดูภาพ, และ skill ที่ช่วยโต product

ประโยคที่สรุป thesis ได้ดี:

> "the same knowledge and expertise that you embed into your ui and documentation needs to become accessible to my daily driver agent"

ความหมายคือ ความรู้ของ product ไม่ควรถูกขังอยู่ใน UI, docs, support bot, หรือ in-app agent. มันควรถูก package เป็นสิ่งที่ agent ภายนอกหยิบใช้ได้.

## วิธีเปิดให้ power user โดยไม่ทิ้ง user ปกติ

โพสต์เสนอทางออกแบบสองชั้น:

1. user ทั่วไปยังใช้ in-app agent / Slackbot / dashboard chat ได้
2. power user ติดตั้ง MCP, CLI, API, และ skills เข้า agent ของตัวเอง

วิธีทำคือบริษัทควรสร้าง internal agent ของตัวเองบน primitive เดียวกับที่เปิดให้ power user:

- harness บางแบบ เช่น pi, OpenCode, harness SDK หรือของเบา ๆ ที่ทีมคุมได้
- skills ที่บอก workflow และ expertise ของ product
- [[model-context-protocol|MCP]] / API / CLI สำหรับเข้าถึงข้อมูลและ action จริง

พอ user เปิด chat ใน product ก็มี prompt เบา ๆ เช่น "อยากทำต่อใน agent ของคุณไหม? ติดตั้ง MCP/CLI และ skills ได้ที่นี่." คนทั่วไป dismiss ได้. Power user เอา product เข้า agent ประจำวันได้.

## ข้อสังเกตของ wiki

โพสต์นี้เป็นเวอร์ชัน product-side ของกรอบ [[three-learning-layers]]: model เป็นของ lab, แต่ harness/context เป็นของผู้ใช้. บริษัทจึงไม่ควรแข่งกับ daily-driver agent ด้วยการทำ chat อีกตัวอย่างเดียว. ควรขายหรือแจก **product context**: docs, skills, tools, schemas, prompt workflows, และ action surface.

มันยังต่อกับ [[coding-harness]] แบบตรงมาก. ถ้า agent = model + harness + environment แล้วบริษัท SaaS ควรยอมรับว่า power user มี harness/environment ของตัวเองอยู่แล้ว. งานของบริษัทคือทำ product ให้ harness นั้นเข้าถึงได้ดี.

## See also

- [[bring-your-own-agent]]
- [[coding-harness]]
- [[model-context-protocol]]
- [[skill-procedures-vs-abilities]]
- [[agent-experience]]
- [[three-learning-layers]]
- [[linear]]
- [[cloudflare]]
- [[posthog]]
