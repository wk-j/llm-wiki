---
title: Throwaway Prototyping
type: concept
tags: [ai, prototyping, workflow, ui, software-engineering]
created: 2026-05-12
updated: 2026-07-21
sources: ["New Skills! handoff, prototype, review and writing-*  Skills Changelog.md", a-field-guide-to-fable-finding-your-unknowns.md, new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets.md, teepagorn-ten-lessons-building-with-ai.md]
---

# Throwaway Prototyping / Prototype แบบทิ้งได้

**Throwaway prototyping** คือการให้ agent สร้างของทดลองเร็ว ๆ เพื่อใช้เรียนรู้ ไม่ใช่เพื่อ merge เข้า production. ใน changelog ของ [[matt-pocock|Matt Pocock]] แนวคิดนี้ถูกแพ็กเป็น skill `/prototype`

## ทำไม prototype ถึงสำคัญใน AI engineering

AI coding ทำให้ implementation เร็วขึ้นมาก แต่ความเร็วนี้ไม่ได้ช่วยถ้าเรายังไม่รู้ว่าของที่ควรสร้างคืออะไร. บางคำถามตอบจาก spec ไม่พอ ต้องเห็น behavior จริงก่อน

Prototype จึงเป็น research tool. มันช่วย flush out design decisions ก่อน commit กับ implementation จริง

**ได้อะไร:** ลดการให้ agent สร้างของจริงจากสมมติฐานที่ยังไม่ผ่านการดูของจริง

## UI prototype

UI prototype ใช้ตอบคำถามที่ต้องใช้ taste และ product context เช่น หน้านี้ควรรู้สึกอย่างไร, layout แบบไหน scan ง่าย, interaction แบบไหนไม่ขัดมือ

Pocock เสนอให้ agent สร้างหลาย variation ที่ต่างกันชัดเจน แล้วให้มนุษย์เลือก

- เลือก variation ที่ถูกทางที่สุด
- บอกว่าอยากเก็บอะไรจาก A และ B
- แตก variation ใหม่จาก decision นั้น
- ทิ้งของที่ไม่ใช่

ตรงนี้เชื่อมกับ [[alignment-bottleneck]] เพราะทำให้คนกับ agent เห็น artifact เดียวกัน แทนที่จะคุยกันบนคำอธิบายลอย ๆ

[[thariq-shihipar|Thariq Shihipar]] (ทีม Claude Code) ให้เหตุผลเดียวกันใน [[field-guide-to-fable-finding-unknowns|A Field Guide to Fable]] ผ่านภาษา [[unknowns-matrix|unknowns]]: prototype เหมาะกับ **unknown knowns** — เกณฑ์ที่เรา "รู้ต่อเมื่อเห็น" เช่น visual design ที่เขาบรรยายไม่ถูกแต่เห็นแล้วรู้ทันที เขาจึงขอ HTML หน้าเดียวที่มี "4 wildly different design directions" ให้ react และย้ำว่าต้องหาให้เจอตอน prototype เพราะเจอตอน implementation แพงกว่ามาก — spec ขยับนิดเดียว code เปลี่ยนโครงได้เยอะ และให้ agent revert ของเก่าก็ยาก

## Logic prototype

Prototype ไม่จำเป็นต้องเป็น UI. งาน business logic ที่มี state เปลี่ยนตามเวลา ก็เหมาะกับ prototype มาก

ตัวอย่าง: entity ใน database เปลี่ยนสถานะตาม action ของผู้ใช้. แทนที่จะถก state machine ใน abstract, ให้ agent สร้าง terminal app เล็ก ๆ เพื่อกด case ต่าง ๆ แล้วดูว่า state ไหลไปทางไหน

**ผลคือ:** edge case โผล่เร็วขึ้น เพราะมนุษย์ได้ลองขยับระบบ ไม่ใช่แค่อ่าน spec

## Prototype เป็น handoff artifact

Prototype ที่ดีควรถูกส่งต่อให้ implementation agent ผ่าน [[agent-handoff-documents|handoff document]]. Agent ตัวถัดไปไม่ต้องเดา preference ใหม่ เพราะมี artifact และบทเรียนจากรอบทดลองอยู่แล้ว

ลำดับงานที่ Pocock ใช้บ่อยคือ

1. [[grill-me|Grill]] เพื่อเคลียร์ intent
2. Prototype เพื่อดู option จริง
3. Handoff ผล prototype ไปให้ implementation agent
4. Review ผลจริงตาม spec และ repo standards

ใน [[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets|Skills v1.1]], prototype ยังเป็น ticket type ของ [[wayfinding]]. มันอยู่ก่อน spec และใช้เมื่อ decision ต้องตอบจากของจริงว่า “ควรหน้าตาอย่างไร” หรือ “ควรทำงานอย่างไร”. Pocock แนะนำ Wayfinder + prototype เป็นพิเศษกับ frontend เพราะข้อความล้วนถ่ายทอด interaction และ taste ได้ไม่ครบ.

**ผลคือ:** prototype ไม่ได้เป็นแค่ handoff ชั่วคราว แต่กลายเป็น primary evidence ของ decision บน issue map ก่อนกลั่นเป็น spec.

## สร้างให้ตัวเองใช้ แล้วลองหลายทางเร็ว ๆ

[[teepagorn-ten-lessons-building-with-ai|Teepagorn]] เติมวิธีใช้ prototype ในงานส่วนตัวสามข้อ: ทำชิ้นเล็กที่สุดที่ใช้ได้, เป็นผู้ใช้คนแรกของตัวเอง และลดต้นทุนให้ลองสามแบบในหนึ่งชั่วโมงได้ พอได้จับของจริง friction จะโผล่เร็วกว่าการคิดระบบทั้งก้อนอยู่ในหัว

แนวนี้ต่างจาก throwaway prototype แบบเคร่งนิดหนึ่ง เพราะชิ้นทดลองที่ดีอาจถูกเก็บเป็นตัวต่อของระบบใหญ่ภายหลัง แต่ก่อน reuse ต้องแยกให้ชัดว่าส่วนไหนเป็นบทเรียน ส่วนไหนเป็น code ที่ผ่านมาตรฐาน production แล้ว การ “เสียดายน้อยลง” ช่วยให้ลบทางตันได้ ไม่ได้แปลว่าทุก draft พร้อมประกอบเข้าของจริง

**ได้อะไร:** ใช้ความเร็วของ AI ซื้อ feedback และ option มากขึ้น โดยไม่เปลี่ยน code ทดลองให้เป็นหนี้ถาวร.

## ข้อควรระวัง

คำว่า throwaway ต้องจริง. ถ้า prototype ถูกยกเข้า production แบบไม่ตรวจ จะกลายเป็น [[vibecoded-slop|vibecoded slop]] อีกแบบหนึ่ง

Prototype มีไว้หาคำตอบ ไม่ใช่เลี่ยง design. พอได้คำตอบแล้ว ต้องกลั่นกลับเป็น spec, issue, หรือ implementation plan ที่ชัดก่อนให้ agent สร้างของจริง

## See also

- [[new-skills-handoff-prototype-review-writing]]
- [[field-guide-to-fable-finding-unknowns]]
- [[unknowns-matrix]]
- [[agent-handoff-documents]]
- [[grill-me]]
- [[alignment-bottleneck]]
- [[ai-orchestrator]]
- [[custom-editing-interfaces]]
- [[html-artifacts]]
- [[wayfinding]]
- [[new-skills-v1-1-wayfinder-research-implement-to-spec-to-tickets]]
- [[teepagorn-ten-lessons-building-with-ai]]
