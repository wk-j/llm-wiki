---
title: Product Overhang
type: concept
tags: [ai, economics, product-design, capabilities]
created: 2026-04-27
updated: 2026-09-10
sources: [thclaws-announcement-panutat.md, boris-cherny-cut-80-percent-claude-code-prompt.md]
---

# Product Overhang / ความสามารถส่วนเกินของโมเดล

**Product Overhang** คือปรากฎการณ์ที่ตัว AI model มีความสามารถแฝง (latent capabilities) อยู่ในตัวตั้งนานแล้ว แต่ความเก่งนั้นยังไม่ถูกดึงออกมาใช้ในโปรแกรมจริง เพราะขาด interface หรือเครื่องมือที่เหมาะสม

## ทำไมเรื่องนี้ถึงสำคัญ
เปรียบเหมือนเรามีเครื่องยนต์ Ferrari (ตัว LLM) แต่เอาไปวางไว้ในรถอีแต๋น เราก็จะไม่รู้เลยว่าเครื่องนี้มันวิ่งได้เร็วแค่ไหน จนกว่าจะมีคนสร้างโครงรถที่รับความเร็วได้ (ตัว Harness) มาครอบมันไว้

[[panutat-tejasen|Panutat Tejasen]] (วิศวกรที่ทำ thClaws) ยกตัวอย่างเรื่องนี้ผ่าน [[claude-code]]:
- **ความเก่งที่ซ่อนอยู่:** Claude 3.5 Sonnet ออกมาให้ใช้ตั้ง 6 เดือนแล้ว แต่คนส่วนใหญ่ก็แค่เอาไปแชทหรือเขียน code สั้นๆ
- **จุดที่ปลดล็อก:** พอ Anthropic ปล่อย Claude Code ที่ยอมให้ model เข้าถึงไฟล์ในเครื่องได้ (filesystem access) และมีระบบช่วยจัดการ context คนถึงได้รู้ว่า "อ้าว มันเขียนโปรแกรมทั้งโปรเจกต์ได้เลยนี่นา"
- **ได้อะไร:** ตรงนี้พิสูจน์ว่า บางทีเราไม่ต้องรอ model ใหม่ (เช่น GPT-5 หรือ Claude 4) แค่เราสร้าง [[harness-engineering|Harness]] ที่ดีกว่าเดิม เราก็อาจจะเจอความเก่งระดับโลกที่ซ่อนอยู่ใน model เดิมได้แล้ว

## นัยต่อการพัฒนาซอฟต์แวร์
- **ไม่ใช่แค่ Wrapper:** การแค่ต่อ API แล้วส่ง prompt ไปเฉยๆ (LLM Wrapper) ไม่เพียงพอที่จะปลดล็อก Product Overhang ได้
- **Logic รอบข้างคือหัวใจ:** งานสร้าง AI Agent ยุคใหม่ หัวใจอยู่ที่การสร้าง infrastructure (เช่น loop การคิด, sandbox, หรือการบีบอัด context) เพื่อเป็นสะพานเชื่อมให้ model ปล่อยของออกมาได้เต็มที่

## Boris Cherny: overhang กับ hobbling เป็นสองด้านของเรื่องเดียวกัน

ใน [[boris-cherny-cut-80-percent-claude-code-prompt|บทสัมภาษณ์กับ Y Combinator]] [[boris-cherny|Boris Cherny]] ให้นิยามจากฝั่งผู้สร้าง Claude Code: **product overhang** คือ model วันนี้ทำได้แล้วแต่ product ยังไม่มีทางให้มันแสดงออก ส่วน **hobbling** คือ product หรือ harness ใส่ขั้นตอนมากจนขวางความสามารถนั้น

ตัวอย่างแรกของ Claude Code คือเลิกจำกัด Claude 3.5 Sonnet ไว้ที่ autocomplete หรือ read-only chat แล้วให้ terminal กับ write access ตัวอย่างรุ่นใหม่คือใช้ [[prompt-ablation|prompt ablation]] ลบคำสั่งที่เคยชดเชย model เก่า และใช้ [[model-elicitation|model elicitation]] โยนโจทย์ยากขึ้นพร้อม verifier เพื่อค้นว่ารุ่นใหม่ไปได้ไกลแค่ไหน

มุมนี้เติม caveat ให้ข้อความเดิมที่ว่า “logic รอบข้างคือหัวใจ”: harness มีค่าเมื่อเปิด tool, context, feedback และ safety boundary แต่ logic ที่คิดแทน model มากเกินอาจกลายเป็น hobbling จึงไม่ใช่ยิ่งมี harness code มากยิ่งดี

**ได้อะไร:** งาน product คือหา boundary ที่พอดี เปิดความสามารถให้ model แต่ยังล็อกความเสียหายที่ยอมรับไม่ได้

## ดูเพิ่ม
- [[harness-engineering]]
- [[claude-code]]
- [[thclaws]]
- [[panutat-tejasen]]
- [[boris-cherny]]
- [[boris-cherny-cut-80-percent-claude-code-prompt]]
- [[prompt-ablation]]
- [[model-elicitation]]
