---
title: Dillon Mulroy
type: entity
tags: [person, software-engineering, ai, cloudflare, coding-agents]
created: 2026-09-12
updated: 2026-09-12
sources: [dillon-mulroy-ships-production-code-he-didnt-write.md]
---

# Dillon Mulroy / ดิลลอน มัลรอย

**Dillon Mulroy** เป็น Principal Engineer ที่ [[cloudflare|Cloudflare]] ตามคำแนะนำตัวใน [[dillon-mulroy-ships-production-code-he-didnt-write|บทสัมภาษณ์กับ Jan-Niklas Wortmann]] เขาบอกว่าหลังใช้ Claude Opus 4.5 มาราวหกเดือนแทบไม่ได้เขียน code เอง แต่ยังอ่านทุกบรรทัดและรับผิดชอบสิ่งที่ ship

## วิธีทำงานกับ coding agent

Dillon ใช้ [[herdr|Herdr]] จัด workspace ใน terminal และใช้ [[pi-agent|pi]] เป็น harness หลัก เขาให้ความสำคัญกับ core ที่เล็ก system prompt สั้น tool น้อย และ behavior ที่ไม่เปลี่ยนถี่ เพราะ harness change อาจทำให้ model ตัวเดิมตอบต่างออกไป

ก่อน implement เขาค่อย ๆ สร้าง tech spec จาก TypeScript types, interfaces, boundary, call stack, input/output/error และ test หลังจากนั้นใช้ [[plannotator|Plannotator]] annotate plan หรือ review diff ในเครื่อง แล้วส่ง feedback กลับเข้า session PR มักอยู่ราว 300 ถึง 800 บรรทัดและต่อกันเป็น [[stacked-pull-requests|stacked PR]]

เขาไม่ใช้ subagent เป็นค่าเริ่มต้น แต่คุม `/tree` ของ pi เองเพื่อสำรวจ context ทีละกิ่งและเลือก summary กลับเข้าสายหลัก จุดนี้ทำให้มนุษย์เป็นคนตัดสินว่า model ควรเห็นอะไร แลกกับ workload ที่สูงและต้องมี intuition เรื่อง context มาก

**ผลคือ:** workflow ของ Dillon ไม่ใช่การปล่อย agent เขียน production code โดยไม่มีคนดู แต่เป็นการย้ายแรงคนจากการพิมพ์ implementation ไปอยู่ที่ context, design, review และ accountability

## Productivity กับความสุขไม่ไปทางเดียวกัน

Dillon รายงานว่า output สูงกว่าที่เคย แต่สนุกกับงานน้อยลง เขาอธิบายว่า implementation เคยให้ micro-problem และความรู้สึกสำเร็จที่พาเข้า flow พอ agent รับช่วงนี้ไป วันทำงานเหลือ macro design problem ต่อกันจนเหนื่อยกว่าเดิม

นี่เป็นประสบการณ์ส่วนตัว ไม่ใช่ข้อสรุปของ Cloudflare หรือผลวิจัยว่าผู้ใช้ agent ทุกคนจะรู้สึกเหมือนกัน ดูการเก็บมุมที่ขัดกันใน [[creative-ownership|Creative Ownership]] และกลไก workload ใน [[ai-work-intensification|AI Work Intensification]]

## ช่องทางที่ source ระบุ

- X: `@dillon_mulroy`
- GitHub: `@dmmulroy`
- Twitch: `@dillon`
- Website: [dillonis.online](https://dillonis.online)

## See also

- [[dillon-mulroy-ships-production-code-he-didnt-write]]
- [[cloudflare]]
- [[jan-niklas-wortmann]]
- [[pi-agent]]
- [[herdr]]
- [[plannotator]]
- [[creative-ownership]]
- [[developer-balance]]
