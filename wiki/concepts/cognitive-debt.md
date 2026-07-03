---
title: Cognitive Debt
type: concept
tags: [psychology, developer-experience, ai]
created: 2026-05-05
updated: 2026-07-03
sources: [agentic-coding-trap.md, The Orchestration Tax.md, eternal-sloptember.md]
---

# Cognitive Debt / หนี้ทางความคิด

**Cognitive Debt** คือสภาวะที่นักพัฒนาสูญเสียความเข้าใจในโครงสร้างหรือพฤติกรรมของระบบ (mental model) เนื่องจากการพึ่งพาเครื่องมืออัตโนมัติหรือ AI Agent มากเกินไปจนไม่ได้สัมผัสและทำความเข้าใจกับโค้ดโดยตรง (เหมือนกับการสร้าง technical debt แต่เกิดขึ้นในสมองของคนเขียนแทน)

ปัญหาหลักคือเมื่อเราไม่ได้เขียนโค้ดเองหรือไม่ได้ใช้เวลากับมันมากพอ เราจะเสีย mental model ที่ชัดเจนของระบบไป [[simon-willison|Simon Willison]] อธิบายว่า เมื่อไม่มีภาพในหัวที่ชัดเจน ทุกๆ ฟีเจอร์ใหม่ที่เพิ่มเข้ามาจะยิ่งทำให้ระบบเข้าใจยากขึ้นเรื่อยๆ อาการนี้มักเกิดร่วมกับ [[skill-atrophy]]

ในยุคของ [[agentic-engineering]] การใช้ AI generate โค้ดปริมาณมากๆ นำไปสู่ Cognitive Debt ได้ง่าย เพราะความเร็วในการสร้างโค้ดนั้นสูงกว่าความสามารถในการทำความเข้าใจของมนุษย์ วิธีแก้ที่ [[lars-faye]] แนะนำคือ ไม่ควรให้ AI สร้างโค้ดมากเกินกว่าที่จะรีวิวและทำความเข้าใจได้หมดในคราวเดียว

[[eternal-sloptember|The Eternal Sloptember]] เพิ่มเหตุผลอีกชั้น: AI artifact ไม่ได้เกิดจาก process แบบมนุษย์เสมอไป แต่หน้าตาอาจเหมือนงานมนุษย์มากพอให้เราประเมินต่ำไปว่าต้องอ่านหนักแค่ไหน. นี่ทำให้ [[quality-proxy-collapse|quality proxy collapse]] กลายเป็นตัวเร่ง cognitive debt

## เชื่อมกับ Orchestration Tax

[[addy-osmani|Addy Osmani]] ใน [[orchestration-tax|Orchestration Tax]] ชี้ว่า "ภาษีค่าควบคุมวง" ที่ไม่จ่ายคือวิธีสะสม technical debt กับ cognitive debt **พร้อมกัน** — เปิด agent เกินที่ review ไหว เราเลย merge ของที่อ่านไม่ละเอียด แล้ว mental model ต่อโค้ดเบสก็ค่อย ๆ เก่าและไม่ตรงจริง อาการกลางทางคือ [[cognitive-surrender]] (ยอมรับโค้ด agent เพราะไม่เหลือ attention จะคิดเอง) เขาอ้างงานเรื่อง cognitive debt ของ Margaret-Anne Storey (นักวิจัย software engineering) ที่ Ciera Jaspan ยกขึ้นมาบน panel ด้วย จุดเดียวกับที่ [[simon-willison|Simon Willison]] เตือน — หนี้ก้อนนี้ไม่โผล่บน dashboard จนกว่า production จะพัง

## วิธีแก้และป้องกัน
1. **Human-in-the-loop**: อย่าปล่อยให้ Agent ทำงานคนเดียวโดยไม่ตรวจสอบ
2. **Surgical Updates**: ขอให้ Agent แก้ไขเฉพาะจุดที่จำเป็น ไม่ใช่เขียนใหม่หมด
3. **Review Discipline**: อ่านและทำความเข้าใจโค้ดที่ Agent เขียนเหมือนเป็นโค้ดของเพื่อนร่วมงาน
4. **[[html-artifacts|HTML Artifacts]]**: ใช้การสร้างเอกสาร HTML ที่มีภาพประกอบ (SVG/Charts) เพื่อให้มนุษย์เห็นภาพรวมของระบบและคง "Shared Mental Model" ไว้ได้ง่ายกว่าการอ่านโค้ดดิบๆ หรือ Markdown

## See also

- [[skill-atrophy]]
- [[eh-gland]]
- [[taste-paradox]]
- [[thariq-html-effectiveness]]
- [[orchestration-tax]]
- [[cognitive-surrender]]
- [[quality-proxy-collapse]]
