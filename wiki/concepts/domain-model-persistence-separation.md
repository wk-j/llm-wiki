---
title: Domain Model Persistence Separation
type: concept
tags: [ddd, domain-modeling, persistence, software-design]
created: 2026-07-02
updated: 2026-07-02
sources: [zoran-horvat-domain-model-persistence.md]
---

# Domain Model Persistence Separation / แยก Domain Model ออกจาก Persistence

**Domain Model Persistence Separation** คือหลักคิดว่า model ของระบบควรเริ่มจากภาษาธุรกิจและกฎของปัญหา ส่วนการเก็บข้อมูลเป็นอีกงานหนึ่ง. หน้านี้มาจากโพสต์ของ [[zoran-horvat|Zoran Horvat]] ที่บอกว่า domain model ไม่ควรงอเพื่อให้เข้ากับ database ก่อน.

## สองงานคนละเป้าหมาย

[[domain-modeling|Domain modeling]] ตอบว่า "ของในธุรกิจนี้คืออะไร และมันทำอะไรได้บ้าง." Persistence ตอบว่า "เราจะเก็บและดึงข้อมูลกลับมาอย่างไร." สองเรื่องนี้เกี่ยวกัน แต่ไม่ใช่เรื่องเดียวกัน.

ถ้า schema นำ model เสมอ เรามักได้ object ที่เป็นแค่ table row ในชุดเสื้อใหม่. ถ้า domain นำก่อน เรามีโอกาสได้ type ที่บอก intent เช่น `Money`, `OrderId`, `UtcTimestamp` และ enforce rule ได้เอง.

**ได้อะไร:** คนอ่าน code เห็นภาษาของปัญหา ไม่ใช่เห็นแค่ชนิดข้อมูลของ database.

## ทำไม ORM ทำให้ทีมยอมแพ้ง่าย

[[object-relational-mapping|ORM]] มักมีข้อจำกัดด้าน mapping, constructor, change tracking, และ query translation. พอเจอแรงต้าน ทีมเลย flatten model เป็น primitive เพื่อ save/load ง่าย.

Horvat แย้งว่า database ไม่ใช่อุปสรรคเสมอไป. หลายครั้งอุปสรรคคือ assumption ของทีมว่า ORM ทำแบบ domain-rich ไม่ได้. Tooling สมัยใหม่ เช่น [[entity-framework-core|EF Core]] อาจรองรับ complex properties และ value converters พอให้ model อยู่ใกล้ domain ได้มากขึ้น.

**ผลคือ:** ก่อนลดคุณภาพ model เพื่อ persistence ควรถามก่อนว่า tooling ทำอะไรได้จริง.

## Boundary ที่สำคัญ

จุดที่ข้อมูลข้ามจาก database กลับเข้า domain object เป็น boundary ที่ควร rebuild invariant. ถ้า database เก็บแค่ scalar ธรรมดา application ควรสร้าง wrapper/value object กลับมา ไม่ใช่ปล่อย raw value ไหลทั่วระบบ.

ตัวอย่างจาก source คือ `DateTime` ที่ database อาจทำ `Kind` หาย. Converter จึงบังคับ UTC อีกครั้งตอนอ่าน. นี่ไม่ใช่แค่ mapping trick แต่เป็นการรักษาความหมายของ domain หลังผ่าน persistence.

**ได้อะไร:** persistence layer เป็น adapter ไม่ใช่เจ้าของกฎของ domain.

## Open question

หลักการแยกสองงานนี้ค่อนข้างเสถียร แต่ระดับที่ทำได้จริงขึ้นกับ ORM, database provider, version, migration strategy, และ performance. Source นี้ยังเป็น claim จากโพสต์ X ไม่ใช่ผลทดสอบใน repo จริง.

## See also

- [[zoran-horvat-domain-model-persistence]]
- [[domain-modeling]]
- [[value-objects]]
- [[primitive-obsession]]
- [[object-relational-mapping]]
- [[entity-framework-core]]
- [[ubiquitous-language]]
