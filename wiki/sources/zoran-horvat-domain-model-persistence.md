---
title: "Zoran Horvat on Domain Model and Persistence"
type: source
tags: [ddd, domain-modeling, persistence, ef-core, orm, value-objects]
url: https://x.com/zoranh75/status/2072568453815279803
created: 2026-07-02
updated: 2026-07-02
sources: ["Zoran Horvat on X — domain model should never bend to fit the database.md"]
---

# Zoran Horvat on Domain Model and Persistence / Domain Model ไม่ควรงอเข้าหา Database

โพสต์ X ของ [[zoran-horvat|Zoran Horvat]] วางประเด็นแบบชัดมาก: domain model ควรสะท้อนภาษาธุรกิจ ไม่ใช่สะท้อนข้อจำกัดของ database หรือ ORM ก่อน. เขาใช้ตัวอย่าง [[entity-framework-core|EF Core]] เพื่อบอกว่า tooling สมัยใหม่พอจะ map model ที่ซับซ้อนลงตารางเดียวได้ โดยไม่ต้องทำให้ model กลายเป็น primitive ทั้งหมด.

ประโยคเปิดของเขาคือ "Your domain model should never bend to fit the database." แก่นของโพสต์นี้ถูกแยกเป็นหน้า [[domain-model-persistence-separation]].

## ปัญหาที่โพสต์ชี้

ปัญหาไม่ใช่ database อย่างเดียว. Horvat บอกว่าทีมมักยอมแพ้ตั้งแต่ตอน ORM ดันกลับ. พอ persistence ทำยาก ก็ flatten model เป็น `decimal`, `string`, หรือ raw GUID เพื่อให้เก็บข้อมูลง่าย.

ตรงนี้คืออาการของ [[primitive-obsession|Primitive Obsession]]: แนวคิดที่ควรมีชื่อและกฎของตัวเองกลับถูกแทนด้วย primitive. ผลคือ business rule หลุดออกจาก type แล้วไปกระจายตาม service, validator, หรือ convention ที่คนต้องจำเอง.

**ผลคือ:** code เขียนง่ายตอน save ลง database แต่ model อ่านยากขึ้น และ safety ลดลง.

## หลักคิด: แยก modeling ออกจาก persistence

Horvat แยกว่า [[domain-modeling|Domain Modeling]] กับ persistence เป็นงานคนละชิ้น. Domain model ตอบคำถามว่า "ระบบนี้มีแนวคิดอะไร และแต่ละแนวคิดมีกฎอะไร." Persistence ตอบคำถามว่า "จะเก็บและอ่านข้อมูลนั้นอย่างไร."

เขาไม่ได้บอกว่า schema ไม่สำคัญ. แต่บอกว่า schema ไม่ควรเป็นตัวเริ่ม shape ของ model เสมอไป. ถ้าเริ่มจากตารางก่อน เรามักได้ object ที่เป็นแค่ row wrapper. ถ้าเริ่มจาก domain ก่อน เรามีโอกาสได้ type ที่บอก intent และ enforce invariant ได้.

**ได้อะไร:** model เป็นภาษาของปัญหา ไม่ใช่ภาพสะท้อนของตาราง.

## Value objects first

Horvat ย้ำว่า concept ที่มีความหมายควรเป็น type ของตัวเอง เช่น currency, amount, timestamp, identifier. นี่คือ [[value-objects|Value Objects]]: object ที่นิยามด้วยค่าและกฎ ไม่ใช่ identity แบบ entity.

ตัวอย่างเช่น `Money` อาจรวม amount กับ currency. `OrderId` อาจ wrap GUID. `UtcTimestamp` อาจบังคับว่าเวลาต้องเป็น UTC. สิ่งเหล่านี้ทำให้ code ผิดยากขึ้น เพราะ caller ส่ง `string` ผิดช่องไม่ได้ง่าย ๆ.

**ผลคือ:** type system ช่วยกัน bug ตั้งแต่ compile/runtime boundary แทนที่จะปล่อยให้ business rule อยู่ในความจำคน.

## EF Core complex properties

โพสต์อ้างว่า EF Core 10 สามารถ map nested object graph ของ value objects ลงเป็น flat columns ใน single table ได้. Horvat เรียกจุดนี้ว่า complex properties: object ซ้อน object ได้ และ leaf scalar แต่ละตัวลง column ของตัวเอง.

ตัวอย่างภาพรวมคือ `Order` มี `Money`, `Money` มี `Amount` และ `Currency`; database ยังอาจเก็บเป็น `Amount_Value`, `Currency_Code` ในตารางเดียว. Model ด้านในยังเป็น object graph ส่วน table ด้านล่างยัง query ได้ตรง.

หมายเหตุของ wiki: claim เรื่อง EF Core 10 นี้มาจากโพสต์นี้ ยังไม่ได้ตรวจเอกสาร Microsoft โดยตรง. ถ้าจะใช้ในงาน production ควรเช็ค behavior ของ EF Core version ที่ใช้จริง.

**ได้อะไร:** ไม่ต้องเลือกระหว่าง "model สวยแต่ persist ยาก" กับ "schema ง่ายแต่ model แบน".

## Value conversions และ invariant boundary

สำหรับ wrapper type ที่ถือค่าเดียว Horvat เสนอ value converter: ตอนเขียนลง database ให้ unwrap เป็น scalar; ตอนอ่านกลับให้ rebuild type. จุดนี้ยังเป็น boundary ที่ re-establish invariant ได้ด้วย.

ตัวอย่างในโพสต์คือ `DateTime`: database อาจตัด `Kind` ออกไป พออ่านกลับมา converter จึงบังคับให้เป็น UTC อีกครั้ง. แนวคิดนี้สำคัญเพราะ persistence layer ไม่ได้รักษา semantic ทุกอย่างของ runtime object เสมอไป.

**ผลคือ:** database เก็บข้อมูลแบบที่มันถนัด แต่ application ได้ object ที่ยังมีกฎครบ.

## Private constructor และ query translation

Horvat บอกว่า EF Core สร้าง empty shell แล้ว populate properties ผ่าน reflection. ดังนั้น private parameterless constructor เปิดทางให้ ORM ทำงานได้ โดยไม่เปิดให้ application code สร้าง object ครึ่ง ๆ กลาง ๆ.

payoff ที่เขาเน้นจริง ๆ คือ query translation. ถ้า mapping ดี เรา filter บน nested properties, compare amount, หรือใช้ custom operator ได้ แล้ว EF Core แปล expression เป็น SQL. Intent ใน memory จึงกลายเป็น database query โดยไม่ต้องเขียน helper code แยก.

**ได้อะไร:** domain-rich model ยัง query ได้ ไม่ใช่แค่สวยตอนอยู่ใน memory.

## แหล่งเรียนรู้ที่โพสต์แนะนำ

ท้ายโพสต์ Horvat แนะนำทรัพยากร DDD และ persistence:

- *Domain Modeling Made Functional* โดย Scott Wlaschin
- *Domain-Driven Design* โดย Eric Evans
- *Database System Concepts* โดย Abraham Silberschatz และคณะ
- course เรื่อง C#/.NET Entity Framework Core ของ Horvat เอง

เขายัง disclose ว่าลิงก์บางส่วนเป็น affiliate links.

## ข้อสังเกตของ wiki

โพสต์นี้เติมมุม software fundamentals ให้ wiki ที่เดิมพูดถึง DDD ผ่าน [[ubiquitous-language|Ubiquitous Language]] ในบริบท AI coding เป็นหลัก. Horvat ดึง DDD กลับมาที่แกนดั้งเดิมกว่า: type, invariant, persistence boundary, และ query model.

จุดที่ควรเก็บเป็น open question คือ tool capability เปลี่ยนเร็ว. หลักแยก domain กับ persistence ค่อนข้างเสถียร แต่รายละเอียด EF Core 10 ต้องตรวจจากเอกสาร/ทดลองจริงก่อนใช้เป็น guideline เชิง implementation.

## See also

- [[domain-model-persistence-separation]]
- [[domain-modeling]]
- [[value-objects]]
- [[primitive-obsession]]
- [[object-relational-mapping]]
- [[entity-framework-core]]
- [[ubiquitous-language]]
