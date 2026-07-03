---
title: Map vs Territory
type: concept
tags: [ai, agents, prompting, mental-model, epistemology]
created: 2026-07-04
updated: 2026-07-04
sources: [a-field-guide-to-fable-finding-your-unknowns.md]
---

# Map vs Territory / แผนที่ไม่ใช่พื้นที่จริง

"The map is not the territory" เป็นประโยคคลาสสิกของ Alfred Korzybski (นักคิดด้านภาษาและการรับรู้): ตัวแทนของสิ่งหนึ่ง ไม่ใช่ตัวสิ่งนั้นจริง ๆ [[thariq-shihipar|Thariq Shihipar]] (ทีม [[claude-code|Claude Code]]) หยิบมาใช้เป็น mental model หลักของการทำงานกับ coding agent ใน [[field-guide-to-fable-finding-unknowns|A Field Guide to Fable]]

## ใน agentic coding

- **แผนที่ (map)** = ตัวแทนของงานที่เราส่งให้ agent: prompt, skills, context ทั้งหมด
- **พื้นที่จริง (territory)** = ที่ที่งานต้องเกิดจริง: codebase, โลกจริง, ข้อจำกัดจริงของระบบ

ช่องว่างระหว่างสองอย่างนี้คือ **unknowns** (ดู [[unknowns-matrix]]) พอ agent เจอจุดที่แผนที่ไม่ครอบคลุม มันต้องเดาจาก best guess ว่าเราต้องการอะไร ยิ่งมอบงานก้อนใหญ่ ยิ่งเจอ unknowns บ่อย โอกาสเดาผิดสะสมก็ยิ่งสูง

จุดที่ทำให้ frame นี้สำคัญขึ้นในยุค model แรง ๆ: Thariq อ้างว่ากับ **Claude [[fable|Fable]] 5** คุณภาพงานไม่ได้ติดที่ความสามารถ model แล้ว แต่ติดที่ความเร็วของ *ผู้ใช้* ในการเคลียร์ unknowns ของตัวเอง — แผนที่ห่วยจำกัดผลงานมากกว่าเครื่องยนต์

## ทำไมวางแผนล่วงหน้าอย่างเดียวไม่พอ

แผนที่จะไม่มีวันตรงพื้นที่จริง 100%:

- unknowns บางตัวโผล่ลึกกลางทาง implementation (เช่น edge case ใน code เดิม)
- unknowns บางตัวชี้ว่าโจทย์ที่ตั้งมาผิดตั้งแต่ต้น ควรแก้ปัญหาคนละทางไปเลย

ทางแก้จึงไม่ใช่ "เขียน spec ให้สมบูรณ์ก่อนค่อยเริ่ม" แต่เป็น loop หา unknowns **ก่อน / ระหว่าง / หลัง** ลงมือ — ดูรายการเทคนิคใน [[unknowns-matrix]]

## โยงกับหน้าอื่น

- [[intent-gap]] — ปัญหาเดียวกันจากฝั่ง verification: โค้ด AI "plausible by construction but not correct by construction"; map/territory อธิบายว่า gap นั้นเกิดจากตัวแทนของงานที่ไม่ตรงพื้นที่จริง
- [[grill-me]] และ [[throwaway-prototyping]] — เครื่องมือย่อระยะห่างระหว่างแผนที่กับพื้นที่จริงก่อนลงมือ
- [[plan-mode-as-prompting]] — เตือนว่า plan ที่ agent เขียนก็เป็นแผนที่อีกชั้นหนึ่ง ไม่ใช่พื้นที่จริง; ยังต้องการ engineering judgment จากคน
- [[eternal-sloptember]] — ฝั่งวิจารณ์มองว่า gap เกิดจาก agent ไม่มี [[world-models|world model]] ของงานจริง; ฝั่ง Thariq มองว่า gap ส่วนใหญ่เคลียร์ได้ด้วยการจัดการ unknowns ของผู้ใช้ — เก็บเป็นคำถามเปิดว่าเส้นแบ่งอยู่ตรงไหน

## See also

- [[field-guide-to-fable-finding-unknowns]]
- [[unknowns-matrix]]
- [[intent-gap]]
- [[fable]]
- [[thariq-shihipar]]
