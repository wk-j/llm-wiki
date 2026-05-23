---
title: Writing Fragments
type: concept
tags: [ai, writing, creativity, workflow, skills]
created: 2026-05-12
updated: 2026-05-12
sources: ["New Skills! handoff, prototype, review and writing-*  Skills Changelog.md"]
---

# Writing Fragments / เศษความคิดสำหรับงานเขียน

**Writing fragments** คือวิธีเริ่มงานเขียนจากเศษประโยค ไอเดีย หรือ observation ที่ยังไม่เป็นบทความเต็ม. [[matt-pocock|Matt Pocock]] เสนอเป็นช่วงแรกของชุด skill `writing-*` ที่ยังอยู่ระหว่างพัฒนา

## แก่นความคิด

นักเขียนจำนวนมากไม่ได้เริ่มจาก outline ที่สมบูรณ์. เขาเก็บ journal, ประโยคที่สะดุดใจ, ความทรงจำ, หรือ observation เล็ก ๆ ไว้นาน ๆ แล้ว fragment เหล่านี้ค่อยไหลเข้า story หรือ article ในภายหลัง

Pocock อยากใช้ AI ช่วยตรงนี้ ไม่ใช่ให้ AI เขียนแทนทันที แต่ให้ AI ถามต่อเพื่อทำให้ fragment ดีขึ้น

**ได้อะไร:** งานเขียนเริ่มจากวัตถุดิบของคน ไม่ใช่จาก prose กลาง ๆ ของ model

## Workflow สามช่วง

ชุด writing skill ที่ Pocock เล่าวางไว้เป็นสามช่วง

| ช่วง | ทำอะไร | เป้าหมาย |
|---|---|---|
| Fragments | เก็บและขยายเศษความคิด | ได้วัตถุดิบที่มีเสียงของผู้เขียน |
| Beats | หา path ผ่าน fragment หลายชิ้น | ได้จังหวะของเรื่องหรือ article |
| Shape | Review งานสุดท้าย | ลดกลิ่น AI และจัด structure ให้เหมาะ |

คำว่า beats ในที่นี้คือจังหวะของเรื่อง. เช่น article หนึ่งควรไปทางไหนต่อ มีได้หลาย path. AI ช่วยเสนอ option 2-3 ทาง แล้วมนุษย์เลือกทิศที่ตรงกับเจตนา

## ต่างจากให้ AI เขียน article ตรง ๆ

ถ้าเริ่มจาก prompt สั้น ๆ ว่า "เขียนบทความเรื่อง X" model มักคืน prose เฉลี่ย. มันอาจถูก grammar แต่ขาดเสียงของคนและ observation เฉพาะตัว

Fragment-first workflow บังคับให้ AI ทำงานบนวัตถุดิบที่ผู้เขียนให้มา. มันเหมาะกับงานที่ต้องการ voice, taste, และความทรงจำเฉพาะ มากกว่างาน content farm

ตรงนี้เชื่อมกับ [[stop-slop-concept]] และ [[ai-language-crisis-phenomenon]] เพราะเป้าหมายคือหนีภาษา AI ที่เรียบเกินและซ้ำสูตร

## จุดที่ยังเป็นงานทดลอง

Pocock ระบุว่ายังต้องพัฒนา skill ชุดนี้อีกมาก. ความยากคือการทำให้ AI ช่วยถามและจัด shape โดยไม่กลืนเสียงของผู้เขียน

หลักที่น่าจะใช้ได้คือให้ AI ทำหน้าที่ editor หรือ interviewer มากกว่า ghostwriter. มันช่วยชี้ทาง ถามต่อ และจัด rhythm แต่เนื้อดิบต้องมาจากคน

## See also

- [[new-skills-handoff-prototype-review-writing]]
- [[stop-slop-concept]]
- [[ai-language-crisis-phenomenon]]
- [[ai-slop]]
- [[matt-pocock]]
