---
title: AI Search Economics
type: concept
tags: [ai, search, economics, business-model]
created: 2026-07-03
updated: 2026-07-03
sources: [how-perplexity-lost-ai-war.md]
---

# AI Search Economics / เศรษฐศาสตร์ของ AI Search

AI search economics คือคำถามว่า query หนึ่งครั้งต้องจ่ายอะไรบ้าง และหาเงินกลับมาได้อย่างไร. เรื่องนี้สำคัญเพราะ [[answer-engine|answer engine]] ไม่ได้มีต้นทุนเหมือน search engine แบบเดิม

## ต้นทุนต่อ query

ในกรอบของ [[how-perplexity-lost-ai-war|How Perplexity Lost the AI War]] query ของ [[perplexity|Perplexity]] ต้องทำหลายอย่างพร้อมกัน:

- live search เพื่อดึง source ปัจจุบัน
- เรียก large language model
- synthesize คำตอบ
- แสดง citation

ทุกขั้นมี compute cost. ยิ่งผู้ใช้ถามเยอะ ต้นทุนก็เพิ่มตาม usage

ฝั่ง [[google|Google]] มี search infrastructure ที่ optimize มานาน. Search แบบเดิมต้นทุนต่ำมากต่อครั้ง และ Google เลือกเปิด AI summary เฉพาะ query ที่คุ้มได้

ผลคือ: AI search ไม่ได้ชนะกันด้วย “คำตอบฉลาดกว่า” อย่างเดียว แต่ชนะกันด้วย gross margin ต่อ query ด้วย

## Monetization ไม่เหมือน search ads เดิม

Google search ads ทำเงินดีเพราะ high-intent query มีคนพร้อมซื้อ, attribution ชัด, และ advertiser วัด conversion ได้. แต่ answer-first UX อาจลดพื้นที่และจังหวะของ ad

Perplexity จึงเจอโจทย์ยากตามที่วิดีโอนี้เล่า:

- ถ้าใส่ ad มากไป trust ลด
- ถ้าใส่น้อยไป revenue ไม่พอ support compute
- ถ้า ad เป็น sponsored follow-up หรือ brand integration performance อาจไม่ชัดเท่า search ad เดิม

ได้อะไร: AI search startup ต้องแก้สองสมการพร้อมกัน คือคำตอบต้องดี และ query ต้องทำกำไรได้

## Open questions

- AI answer query แบบไหนคุ้มกว่า search page แบบเดิม
- ad model ที่ไม่ทำลาย trust ควรหน้าตาเป็นอย่างไร
- subscription พอจ่ายต้นทุนของ heavy users หรือไม่
- incumbent ที่มี ad engine อยู่แล้วได้เปรียบถาวรแค่ไหน

## See also

- [[perplexity]]
- [[google]]
- [[answer-engine]]
- [[distribution-moat]]
- [[value-migration-from-code]]
- [[ai-token-economics]]
