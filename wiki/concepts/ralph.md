---
title: Ralph (the loop)
type: concept
tags: [ai, agents, loops, automation, history]
created: 2026-06-21
updated: 2026-06-21
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md"]
---

# Ralph / ลูปดั้งเดิมของ agent coding

**Ralph คือเทคนิคลูปดั้งเดิมของ [[jeffrey-huntley|Jeffrey Huntley]]: เขียน `while` loop ที่ส่ง prompt เดิมให้ [[claude-code|Claude Code]] ซ้ำ ๆ ไปเรื่อย ๆ จนกว่างานจะเสร็จ.** เป็นต้นตอของกระแส "agentic loop" ที่มาดังทีหลัง. บทความต้นฉบับลงวันที่ 14 ก.ค. ปีก่อน

## กลไก

ง่ายมาก: ลูปที่ pass prompt ก้อนเดิมให้ Claude Code แล้วรันใหม่ ครั้งแล้วครั้งเล่า

```
while not done:
    run claude-code with <same prompt>
```

agent ทำงานไปเรื่อย ๆ จนถึงเงื่อนไขจบ. ความเรียบง่ายนี่แหละทำให้มันดังและกลายเป็นต้นแบบของ pattern ลูปยุคหลัง

## Matt Pocock มองว่า "ไม่จำเป็นต้องเป็นลูป"

[[matt-pocock|Matt Pocock]] เคยพูดถึง Ralph ตั้งแต่ต้นปี. ข้อสรุปของเขาคือ พอลองใช้จริง **เขาไม่ได้ต้องการ "ลูป"** — สิ่งที่ต้องการมีแค่ AFK agent มารับงานที่ scope ชัดแล้วไปทำให้จบ (ดู [[afk-agents]])

> "I don't really need to run this as a loop... The only thing I need out of this is the AFK agent to take on a specific task and do that task."

เขาเลยเสนอให้มองเป็น **[[queues-over-loops|คิวมากกว่าลูป]]** — backlog ของงานที่หลาย node หยิบไปทำ แทนลูปเดียวที่วิ่งทำทุกอย่าง

## ที่ทางในประวัติศาสตร์

Ralph → กระแส loop engineering ปี 2026 ([[loop-engineering-osmani|Addy Osmani]], Peter Steinberger, Boris Cherny). Matt มองว่าครึ่งหนึ่งของ hype คือ lab อยากขาย token (รันลูปตลอด = จ่ายตลอด) แต่ก็ยอมรับว่า "ลูปมีประโยชน์ แค่ไม่ใช่ภาพทั้งหมด"

## ดูเพิ่ม

- [[jeffrey-huntley]]
- [[queues-over-loops]]
- [[afk-agents]]
- [[loop-engineering]]
- [[matt-pocock-agentic-workflow]]
- [[claude-code]]
