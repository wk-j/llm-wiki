---
title: Google
type: entity
tags: [technology, search, ai, advertising, organizations]
created: 2026-07-03
updated: 2026-08-16
sources: [how-perplexity-lost-ai-war.md, the-new-software-lifecycle.md]
---

# Google

Google คือบริษัทเทคโนโลยีที่ครอง search, advertising, Android, Chrome, YouTube, Gmail, Google Drive, Google Cloud, และ AI ผ่าน Gemini/DeepMind. ใน wiki นี้ก่อนหน้านี้มีหน้าเฉพาะอย่าง [[google-cloud|Google Cloud]], [[google-deepmind|Google DeepMind]], และ [[google-for-developers|Google for Developers]] อยู่แล้ว. หน้านี้ทำหน้าที่เป็น entity กลางของบริษัท

## บทบาทใน Perplexity source

ใน [[how-perplexity-lost-ai-war|How Perplexity Lost the AI War]] Google เป็น incumbent ที่ [[perplexity|Perplexity]] พยายาม challenge. วิดีโอนี้บอกว่า Google ไม่จำเป็นต้องมี AI search ที่ดีที่สุดเสมอไป เพราะ Google ถือของสำคัญกว่า:

- search habit ของผู้ใช้
- Chrome/Android/default placement
- ad engine ที่ทำเงินจาก high-intent query
- infrastructure ที่ optimize search economics มานาน
- product ecosystem อย่าง YouTube, Drive, Gmail

ผลคือ Google สามารถเพิ่ม AI Overviews เข้า search แบบ selective ได้. ไม่ต้องจ่าย LLM compute ให้ทุก query ถ้าไม่คุ้ม

## Distribution สำคัญกว่า feature

วิดีโอนี้ใช้ Google เป็นตัวอย่างของ [[distribution-moat|distribution moat]]. ถ้า startup มี feature ดีกว่า แต่ incumbent copy feature นั้นแล้ววางไว้ใน default surface ที่คนใช้อยู่ทุกวัน startup จะเสียความต่างเร็วมาก

นี่ไม่ได้แปลว่า Google “ชนะเพราะ product ดีกว่า”. Mondo Startups ตีความว่าชนะเพราะ search เป็น infrastructure และ ecosystem ไม่ใช่แค่หน้าเว็บตอบคำถาม

## Whitepaper เรื่องวงจรพัฒนาซอฟต์แวร์

Google เผยแพร่ whitepaper *The New SDLC With Vibe Coding*. [[addy-osmani|Addy Osmani]] นำมาเล่าแบบย่อใน [[the-new-software-lifecycle|The New Software Lifecycle]]. กรอบหลักคือ AI เร่ง implementation มากกว่า phase ที่ใช้ judgement จึงทำให้ specification, architecture และ verification กลายเป็นคอขวดของ [[ai-driven-sdlc|AI-driven SDLC]]

Whitepaper กับบทความเป็นงานจากผู้สร้าง ecosystem เอง จึงเหมาะกับการอ่านทิศทาง แต่ตัวเลข benchmark, productivity, adoption และต้นทุนควรเก็บสถานะเป็น first-party claim หรือภาพประกอบตามที่บทความระบุ

**ได้อะไร:** Google ไม่ได้วาง AI coding เป็น autocomplete อย่างเดียว แต่กำลังเสนอกรอบกระบวนการที่ครอบตั้งแต่ requirement, harness/context ไปถึง eval และ deploy

## See also

- [[perplexity]]
- [[google-cloud]]
- [[google-deepmind]]
- [[google-for-developers]]
- [[ai-search-economics]]
- [[distribution-moat]]
- [[the-new-software-lifecycle]]
- [[ai-driven-sdlc]]
