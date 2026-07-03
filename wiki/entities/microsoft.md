---
title: Microsoft
type: entity
tags: [ai, cloud, infrastructure, organizations]
created: 2026-04-28
updated: 2026-07-03
sources: [microsoft-openai-partnership-2026.md, how-perplexity-lost-ai-war.md, how-ai-became-more-expensive-than-workers-it-replaced.md]
---

# Microsoft / ไมโครซอฟท์

ยักษ์ใหญ่ด้าน technology ที่เป็นหัวหอกในการผลักดัน AI เข้าสู่กระแสหลักผ่าน Azure และ Copilot โดยมีจุดเปลี่ยนสำคัญในช่วงต้นปี 2026 คือการปรับทิศทางสู่การเป็นอิสระมากขึ้น (AI independence)

## ทิศทางเชิงกลยุทธ์ (2026)

ในช่วงปี 2026 Microsoft เริ่มขยับตัวออกจากบทบาทผู้สนับสนุน [[openai]] เพียงอย่างเดียว ไปสู่การสร้างขีดความสามารถของตัวเองที่เทียบเท่ากัน:

- **Microsoft AI Division**: หน่วยงานใหม่ที่ตั้งขึ้นมาเพื่อดูแล consumer AI และโมเดลของตัวเองโดยเฉพาะ นำทีมโดย Mustafa Suleyman (อดีตหัวหน้า Copilot และ DeepMind co-founder)
- **Home-grown Models**: การพัฒนาโมเดลตระกูล MAI (Microsoft AI) เพื่อลดการพึ่งพา GPT เพียงอย่างเดียว และเพื่อใช้ในงานที่ต้องการการปรับแต่งเชิงลึกหรือ cost-efficiency
- **Project Stargate**: โครงการ AI supercomputer มูลค่า $500 billion ที่เดิมทีเป็นวิสัยทัศน์ร่วมกับ OpenAI แต่ภายหลัง Microsoft เริ่มเข้ามาคุมโครงสร้างพื้นฐาน (physical infrastructure) เองทั้งหมด

## ความสัมพันธ์กับ OpenAI (The "Open Relationship")

จากประกาศเมื่อ 2026-04-27 (ดู [[microsoft-openai-partnership-2026]]) ความสัมพันธ์ได้เปลี่ยนจาก "Exclusive" เป็น "Non-exclusive":

- **สิทธิในการใช้ IP**: Microsoft ยังถือสิทธิใช้งาน model ของ OpenAI (รวมถึง [[gpt-5-5]] และรุ่นอนาคต) ไปจนถึงปี 2032 แต่ไม่ใช่ผู้เล่นคนเดียวในตลาดอีกต่อไป
- **Azure as Primary Cloud**: แม้ OpenAI จะไปใช้ cloud อื่นได้ (เช่น Google, Amazon) แต่ Azure ยังเป็น "Primary Cloud Partner" และจะได้สิทธิในการรัน product ใหม่ก่อน (first-look) ถ้า infrastructure พร้อม
- **Financial Pivot**: ยกเลิกการจ่าย revenue share ให้ OpenAI และมีการตั้งเพดาน (cap) สำหรับเงินที่ OpenAI ต้องจ่ายคืนให้ Microsoft

## ผลกระทบต่อ Ecosystem

การที่ Microsoft เริ่มสร้างโมเดลเองและเปิดให้ OpenAI ไปหา cloud อื่นได้ ทำให้ตลาด AI ปี 2026 เริ่มเข้าสู่ยุค **Multi-cloud / Multi-model** อย่างเต็มตัว ผู้ใช้ Azure จะเห็นทางเลือกที่หลากหลายขึ้นระหว่างโมเดลของ Microsoft เอง กับโมเดลจาก OpenAI และ [[anthropic]] (ผ่าน integration ต่างๆ)

## Bing และบทเรียนเรื่อง distribution

ใน [[how-perplexity-lost-ai-war|How Perplexity Lost the AI War]] Microsoft ถูกยกเป็น counterexample สำคัญ: แม้ Bing จะได้ integration กับ ChatGPT ตั้งแต่ต้นปี 2023, มี Windows เป็น distribution surface, สิทธิ์เข้าถึง GPT-4, และงบ marketing ใหญ่ แต่แหล่งนี้บอกว่า market share ก็ยังขยับไม่มาก

บทเรียนของแหล่งนี้คือ search/browser habit เปลี่ยนยากมาก. ถ้า Microsoft ยังเปลี่ยนพฤติกรรมผู้ใช้ได้จำกัด [[perplexity|Perplexity]] ก็ยิ่งเจอโจทย์หนักเมื่อพยายามใช้ [[comet-browser|Comet]] แก้ [[distribution-moat|distribution moat]]

## Claude Code cost pullback

ใน [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]] Microsoft ถูกใช้เป็นตัวอย่างองค์กรที่เริ่มคุมค่าใช้จ่าย AI ภายใน คลิปอ้างว่า Microsoft สั่งให้วิศวกรหยุดใช้เครื่องมือ coding ของ Anthropic / Claude Code โดยเหตุผลที่ถูกเล่าภายหลังคือค่าใช้จ่ายสูง ไม่ใช่แค่การผลักให้ใช้เครื่องมือใน ecosystem ของตัวเอง

wiki เก็บเรื่องนี้เป็น source-attributed เพราะต้องตรวจ memo / reporting ต้นทางก่อนสรุปว่า policy จริงมีขอบเขตแค่ไหน

## ดูเพิ่ม

- [[openai]]
- [[gpt-5-5]]
- [[claude-code]] — คู่แข่งของ Copilot ในฝั่ง Anthropic
- [[distribution-moat]]
- [[enterprise-ai-roi]]
- [[ai-token-economics]]
