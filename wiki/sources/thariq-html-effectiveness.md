---
title: "Using Claude Code: The Unreasonable Effectiveness of HTML"
type: source
tags: [claude-code, html, artifacts, communication, visualization, productivity]
url: https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html
author: "[[thariq-shihipar|Thariq Shihipar]]"
published: 2026-05-20
date_ingested: 2026-05-09
created: 2026-05-09
updated: 2026-05-25
sources: [Using Claude Code The Unreasonable Effectiveness of HTML.md]
---

# Using Claude Code: The Unreasonable Effectiveness of HTML / ทำไม HTML ถึงเวิร์กมากใน Claude Code

บทความนี้ของ [[thariq-shihipar|Thariq Shihipar]] (Member of Technical Staff ในทีม [[claude-code|Claude Code]]) อธิบายว่าทำไมเขาและบางคนในทีม Claude Code เริ่มใช้ HTML แทน Markdown สำหรับ output ที่ต้องให้มนุษย์อ่าน ตรวจ แชร์ หรือใช้เป็น reference ระหว่างทำงานกับ agent

แก่นคือ Markdown ยังดีสำหรับข้อความเรียบ ๆ แต่พอ agent ทำงานซับซ้อนขึ้น แผน, spec, report และ code review ยาวขึ้นจนคนไม่อ่านจริง HTML จึงกลายเป็นสื่อกลางที่ช่วยให้คนยังอยู่ใน loop ได้

## Key takeaways

### 1. Markdown เริ่มเป็นคอขวดเมื่อ agent ทำงานใหญ่ขึ้น

Thariq เริ่มจากข้อสังเกตง่าย ๆ: Markdown เป็น format หลักที่ agent ใช้สื่อสารกับมนุษย์ เพราะเรียบง่าย portable และแก้ได้ง่าย แต่เมื่อ Claude Code เริ่มเขียน spec และ plan ที่ยาวขึ้น เขาพบว่าตัวเองไม่ค่อยอ่าน Markdown เกินร้อยบรรทัด และยิ่งยากที่จะให้คนอื่นในองค์กรอ่าน

Markdown ยังมีข้อดีเรื่องแก้ข้อความตรง ๆ แต่ใน workflow ใหม่ มนุษย์มักไม่ได้แก้ไฟล์เองแล้ว เขาจะ prompt ให้ Claude แก้แทน ข้อดีหลักของ Markdown เลยลดความสำคัญลง

ได้อะไร: ถ้า output หลักมีไว้ให้คนอ่านและตัดสินใจ ไม่ใช่ให้คนแก้ด้วยมือ HTML อาจเหมาะกว่า Markdown

### 2. HTML ให้ information density สูงกว่า

HTML เก็บข้อมูลได้หลายมิติกว่า Markdown มาก เช่น table, CSS, SVG, code snippet, interaction ด้วย JavaScript, workflow diagram, canvas, absolute positioning และ image tag

ประเด็นไม่ใช่ความสวยอย่างเดียว แต่คือการทำให้ model ส่งข้อมูลที่ลึกและซับซ้อนมาให้มนุษย์ตรวจได้แบบอ่านรู้เรื่องกว่า ASCII diagram หรือข้อความยาว ๆ

นี่คือแกนของ [[html-artifacts|HTML Artifacts]]: ใช้ HTML เป็น medium ที่เพิ่ม information density และลดภาระการอ่านของมนุษย์

ได้อะไร: HTML ช่วยให้ agent ส่ง context ที่ซับซ้อนโดยไม่ทำให้คนหลุดจากงาน

### 3. HTML ช่วย visual clarity, sharing, และ responsive reading

Claude สามารถจัด HTML ให้มี tabs, links, illustrations, layout และ responsive design ได้ ทำให้ spec หรือ report ยาว ๆ อ่านง่ายกว่า Markdown ที่ไหลเป็น text ก้อนเดียว

อีกจุดคือ sharing Markdown มักต้องแนบไฟล์หรือเปิดใน tool ที่ render ได้ แต่ HTML เปิดใน browser ได้ตรง ๆ พอ upload แล้วแชร์ link ให้คนในองค์กรอ่านได้ง่ายกว่า โอกาสที่คนจะอ่าน PR writeup, report หรือ spec จึงสูงขึ้น

ได้อะไร: format ที่แชร์และอ่านง่ายขึ้นช่วยลด [[cognitive-debt|Cognitive Debt]] เพราะคนยังตาม mental model ของ agent ทัน

### 4. Two-way interaction ทำให้เอกสารกลายเป็นเครื่องมือ

HTML ไม่ได้เป็นแค่เอกสารอ่านอย่างเดียว มันใส่ sliders, knobs, drag-and-drop, live preview, validation และปุ่ม copy output กลับไปให้ Claude Code ได้

ตรงนี้นำไปสู่ [[custom-editing-interfaces|Custom Editing Interfaces]] หรือ throwaway editors: ให้ Claude Code สร้าง HTML file เฉพาะกิจสำหรับงานเดียว เช่นจัดลำดับ Linear tickets, แก้ feature flag config, tuning prompt template หรือ annotate diff แล้ว export กลับเป็น JSON, Markdown, prompt หรือ diff

ได้อะไร: มนุษย์ยังเป็นคนตัดสินใจ แต่ loop สั้นลงมาก เพราะไม่ต้องแปลงความต้องการทุกอย่างเป็นข้อความในช่อง prompt

### 5. Claude Code สำคัญเพราะ ingest context ได้กว้าง

Thariq แยกว่าเหตุผลที่ใช้ Claude Code สร้าง HTML ไม่ใช่แค่เพราะมันเขียน HTML ได้ แต่เพราะ Claude Code อ่าน filesystem, git history, MCP sources เช่น Slack/Linear และ browser context ได้

ตัวอย่างในบทความคือเขาให้ Claude Code อ่าน folder ที่เก็บ HTML files ที่เคยสร้างไว้ แล้วจัดหมวดหมู่เป็น HTML diagram ประกอบบทความเอง

ได้อะไร: HTML artifact มีค่ามากขึ้นเมื่อมันสกัดจาก context จริงของงาน ไม่ใช่เป็นหน้าเว็บสวย ๆ ที่ลอยจากระบบ

## Use cases

- **Specs, planning, exploration** — ใช้ HTML หลายไฟล์เป็น web ของการคิด: brainstorm ทางเลือก, ทำ mockup, ใส่ code snippet, แล้วค่อยสรุปเป็น implementation plan สำหรับ session ถัดไป
- **Code review and understanding** — render diff, annotation, severity color, flowchart, module map หรือ PR explainer ให้ reviewer อ่านง่ายกว่า diff ปกติ
- **Design and prototypes** — ทำ mockup หรือ interaction prototype ใน HTML ก่อนแปลงเป็น React, Swift หรือ surface จริง
- **Reports, research, learning** — อ่าน Slack, codebase, git history หรือ web แล้วทำเป็น explainer, incident report, weekly status หรือ slideshow/deck
- **Custom editing interfaces** — สร้าง editor เฉพาะกิจที่จบด้วย export/copy button เพื่อส่งผลกลับเข้า Claude Code

## ข้อควรระวัง

Thariq ไม่ได้บอกว่าต้องทำ `/html` skill ทันที เขาแนะนำให้เริ่มง่าย ๆ ด้วย prompt อย่าง "make an HTML file" หรือ "make an HTML artifact" ก่อน สิ่งสำคัญกว่าคือรู้ว่า artifact นั้นต้องช่วยให้คนทำอะไรต่อ

FAQ ในบทความยังยอมรับว่า HTML ใช้ token มากกว่า Markdown แต่สำหรับ workflow ที่มนุษย์มีแนวโน้มจะอ่านจริง ความคุ้มค่ามักอยู่ที่ความเข้าใจและการตัดสินใจ ไม่ใช่ token count อย่างเดียว

ผลคือ: อย่าทำ HTML เพื่อ decoration ให้ทำ HTML เมื่อมันช่วยให้คนอ่าน เห็น ทดลอง ตัดสินใจ หรือ export งานกลับเข้า loop ได้ดีขึ้น

## ความสัมพันธ์กับ source อื่น

หลัง ingest [[fundamental-productivity-ai-world|Fundamental of productivity in AI world]], บทความนี้อ่านได้ชัดขึ้นในฐานะตัวอย่างของ [[interaction-productivity|Interaction Productivity]]: HTML artifact เพิ่ม productivity เพราะทำให้คนเขียนกับคนอ่านส่งต่อความเข้าใจกันเร็วขึ้น ไม่ใช่เพราะมันเป็น format ที่อลังการกว่า Markdown เฉย ๆ

มันยังต่อกับ [[ai-era-standard-balance|AI-era Standard Balance]] ด้วย เพราะ standard ของเอกสารยุค AI ต้อง balance ภาระของ producer กับ consumer ใหม่ HTML เป็นหนึ่งใน candidate format ที่ลดภาระฝั่ง consumer ได้

## See also

- [[thariq-shihipar]]
- [[claude-code]]
- [[html-artifacts]]
- [[custom-editing-interfaces]]
- [[interaction-productivity]]
- [[ai-era-standard-balance]]
- [[cognitive-debt]]
