---
title: "Wayfinder Skill"
type: source
tags: [ai, agents, skills, planning, issue-tracking, workflow]
url: https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md
date_ingested: 2026-07-12
created: 2026-07-12
updated: 2026-07-12
sources: ["https://github.com/mattpocock/skills/blob/main/skills/engineering/wayfinder/SKILL.md"]
---

# Wayfinder Skill / สกิลหาเส้นทางผ่านงานก้อนใหญ่

`wayfinder` คือ skill ของ [[matt-pocock|Matt Pocock]] (ผู้สอน TypeScript และคนสร้าง workflow สำหรับ coding agent) สำหรับงานที่ใหญ่เกินหนึ่ง agent session และยังคลุมเครือเกินกว่าจะเขียนแผนเต็มได้ตั้งแต่ต้น. มันเปลี่ยน issue tracker ให้เป็นแผนที่ร่วม แล้วค่อยปิดคำถามทีละใบจนเส้นทางไปยังปลายทางชัด.

แก่นของต้นฉบับไม่ใช่ “แบ่งงานใหญ่เป็น task เล็ก ๆ ให้ครบ” แต่คือ **อย่าแกล้งทำเป็นว่าเห็นเส้นทางทั้งหมดทั้งที่ยังไม่เห็น**. ให้สร้าง ticket เฉพาะคำถามที่ตั้งได้คมแล้ว ส่วนเรื่องที่รู้ว่าจะต้องกลับมาดูแต่ยังถามไม่ถูก ให้เก็บไว้ใน fog ก่อน.

## Plan, don't do

Wayfinder เป็น planning workflow ก่อน. แต่ละ ticket มีหน้าที่ปิด decision หรือ investigation หนึ่งเรื่อง. แผนที่เสร็จเมื่อไม่มีอะไรต้องตัดสินใจก่อนเริ่ม implementation ไม่ใช่เมื่อ deliverable ถูกสร้างเสร็จ.

มีข้อยกเว้นได้ถ้า `Notes` ของ map บอกชัดว่าจะพา execution เข้าไปด้วย. แต่ถ้าไม่ได้เขียนไว้ ให้ถือว่าแรงอยาก “ลงมือทำเลย” คือสัญญาณว่ามาถึงขอบแผนที่และควร hand off.

**ได้อะไร:** planning กับ implementation ไม่ไหลปนกันจน ticket กลายเป็น mini-project ที่ไม่มีวันปิด.

## Map เป็น index ไม่ใช่คลังรายละเอียด

แผนที่หลักคือ issue หนึ่งใบ ติด label `wayfinder:map`. มันเก็บภาพรวมระดับต่ำพอให้เปิดครั้งเดียวต่อ session:

- `Destination` — ตอนจบของ effort นี้ต้องได้อะไร เช่น spec, decision หรือ change
- `Notes` — domain, skill ที่ต้องใช้ และ preference ประจำ effort
- `Decisions so far` — ลิงก์ไป ticket ที่ปิดแล้ว พร้อม gist หนึ่งบรรทัด
- `Not yet specified` — เรื่องใน scope ที่ยังตั้งเป็นคำถามคม ๆ ไม่ได้
- `Out of scope` — เรื่องที่จงใจตัดออกเพราะอยู่เลย destination

รายละเอียดของ decision อยู่ที่ ticket เพียงแห่งเดียว. Map แค่ชี้และย่อ ไม่คัดลอกคำตอบมาซ้ำ. เวลาพูดกับคน ให้เรียก map และ ticket ด้วยชื่อที่อ่านรู้เรื่อง ไม่ใช้เลข issue เปล่า ๆ.

**ผลคือ:** คนเห็นภาพรวมเร็ว แต่ยัง zoom เข้า evidence และเหตุผลของแต่ละ decision ได้โดยไม่เกิดข้อมูลสองสำเนา.

## Ticket, fog และ out of scope ไม่ใช่อย่างเดียวกัน

เกณฑ์แยกสามสถานะนี้คือหัวใจของ skill:

| สถานะ | ใช้เมื่อ | จะเกิดอะไรต่อ |
|---|---|---|
| Ticket | ตั้งคำถามได้ชัดแล้ว แม้ยังตอบไม่ได้หรือยังติด blocker | รออยู่ใน dependency graph จนขึ้น frontier |
| Not yet specified / fog | รู้คร่าว ๆ ว่ามีเรื่องต้องกลับมาดู แต่ยังตั้งคำถามให้แม่นไม่ได้ | พอ decision ข้างหน้าทำให้เห็นชัด ค่อยแตกเป็น ticket |
| Out of scope | เรื่องนั้นอยู่เลย destination | ปิดไว้ ไม่เลื่อนกลับเข้ามาเอง เว้นแต่ตั้ง effort ใหม่ |

ต้นฉบับให้ test ง่าย ๆ ว่า **ถ้าพูดคำถามให้ precise ได้ตอนนี้ ให้ทำ ticket**. การยังตอบไม่ได้ไม่ใช่เหตุผลให้โยนเข้า fog. ตรงกันข้าม ถ้ายังไม่รู้ด้วยซ้ำว่าควรถามอะไร อย่าฝืน pre-slice เป็น task ปลอม ๆ.

**ได้อะไร:** แผนยอมรับ [[unknowns-matrix|unknowns]] ตามจริง และค่อยเพิ่มความละเอียดเมื่อ evidence ข้างหน้ามาถึง.

## Frontier ทำให้หลาย session ทำงานร่วมกันได้

Ticket ทุกใบเป็น child issue และมี dependency ตามระบบ native ของ tracker. Ticket ที่เปิดอยู่, ไม่มี blocker และยังไม่มี assignee คือ **frontier** — ขอบของสิ่งที่รู้พอจะหยิบไปทำได้ตอนนี้.

ก่อนเริ่ม session ต้อง claim ticket ด้วยการ assign ให้ developer ผู้ขับ map. Session อื่นจึงข้ามใบนี้ไปหยิบ frontier ใบถัดไปได้. Skill ย้ำว่า session หนึ่งห้ามปิดเกินหนึ่ง ticket เพื่อให้ decision, context และผลลัพธ์ยังมีขอบเขตชัด.

**ผลคือ:** concurrency มาจากคิวของคำถามที่ไม่ติดกัน ไม่ใช่การยัดทุกอย่างลง context เดียวหรือให้หลาย agent เดางานซ้ำกัน.

## Ticket สี่ชนิด

Wayfinder แบ่ง ticket ตามวิธีลดความไม่รู้ ไม่ได้แบ่งตามทีมงาน:

- **Research (AFK)** — อ่านข้อมูลนอก working directory แล้วสร้าง markdown summary เป็น asset
- **Prototype (HITL)** — ทำของหยาบราคาถูกให้มนุษย์ react เมื่อคำถามคือ “ควรหน้าตา/ทำงานอย่างไร”
- **Grilling (HITL)** — ใช้ [[grill-me|grilling]] และ [[domain-modeling|domain modeling]] ถามทีละข้อ; เป็นชนิดปกติ
- **Task (HITL หรือ AFK)** — ลงมือทำสิ่งจำเป็นเพื่อปลด blocker ของ decision เช่น provision access หรือย้ายข้อมูลให้เห็น shape; ไม่ใช่ทำ destination ให้เสร็จ

HITL (human in the loop) ต้องคุยกับมนุษย์จริง. Agent ห้ามสวมบทเป็นคนแล้วตอบคำถามแทน โดยเฉพาะ grilling ticket.

**ได้อะไร:** ticket บอกชัดว่าคำตอบต้องมาจากการอ่าน, การเห็น prototype, การตัดสินใจร่วม หรือการปลด blocker.

## สองโหมดการใช้

### Chart the map

เริ่มจาก loose idea แล้วใช้ grilling + domain modeling ตั้ง `Destination` ก่อน. จากนั้นถามแบบ breadth-first เพื่อเห็น decision รอบพื้นที่ทั้งหมด. ถ้าไม่มี fog และงานเล็กพอจบใน session เดียว ก็ไม่ต้องสร้าง Wayfinder map.

ถ้าจำเป็นต้องมี map ให้สร้าง map ก่อน แล้วสร้าง ticket เฉพาะคำถามที่ชัด. ค่อย wire dependency ใน pass ที่สองเพราะ issue ต้องมี id ก่อนจึงอ้างกันได้. จบ session ตรงนี้ ไม่เริ่มปิด ticket ต่อ.

### Work through the map

เปิด map ระดับภาพรวม เลือก frontier ticket แรกถ้าผู้ใช้ไม่ได้ระบุ แล้ว claim ก่อนทำงาน. หลังได้คำตอบ ให้เขียน resolution comment, ปิด ticket และเพิ่ม pointer หนึ่งบรรทัดใน `Decisions so far`.

จากนั้นค่อยดูว่าคำตอบทำให้ fog ส่วนไหนตั้งเป็นคำถามได้แล้ว, ทำให้เกิด ticket ใหม่, ทำให้ ticket เดิมหมดความหมาย หรือเผยว่าเรื่องใดอยู่นอก scope. Map จึงเติบโตตามสิ่งที่เพิ่งรู้ ไม่ได้ถูกวาดละเอียดครบตั้งแต่วันแรก.

## ข้อจำกัดและจุดที่ต้องระวัง

- Skill สมมติว่า issue tracker รองรับ child issue, assignee และ dependency. ถ้าไม่มี ต้องใช้ convention ทดแทน และภาพ frontier จะอ่อนลง
- กฎหนึ่ง ticket ต่อ session ช่วยคุม context แต่เพิ่มค่า ceremony กับงานที่เล็กหรือ decision เกี่ยวกันแน่น
- Map อาจกลายเป็น backlog ธรรมดา ถ้า ticket เขียนเป็น deliverable แทนคำถาม หรือถ้า `Not yet specified` ถูกใช้เป็นที่กอง task ที่ไม่อยากจัดลำดับ
- ต้นฉบับเป็น workflow specification จากผู้สร้างเอง ยังไม่มีข้อมูลเปรียบเทียบว่าให้ผลดีกว่า planning pattern อื่นในทีมจริงแค่ไหน

## ความเชื่อมโยงกับ wiki

- ต่อจาก [[map-vs-territory]]: Wayfinder เป็นแผนที่ที่ประกาศตรง ๆ ว่ายังไม่ครอบคลุม territory ทั้งหมด
- ทำให้ [[unknowns-matrix]] เป็น workflow บน tracker: known question ไป ticket, unknown question อยู่ fog
- เป็น implementation ที่ชัดขึ้นของ [[queues-over-loops]]: frontier คือคิวงานที่หลาย session หยิบได้
- ใช้ [[grill-me]] และ [[domain-modeling]] เป็นกลไกสร้าง destination และปิด decision
- ต่างจาก [[agent-handoff-documents]] ตรงที่ handoff ส่ง context ระหว่างสอง session ส่วน Wayfinder เก็บ state ของ effort ทั้งก้อนไว้ใน issue graph

## See also

- [[wayfinding]]
- [[matt-pocock]]
- [[map-vs-territory]]
- [[unknowns-matrix]]
- [[queues-over-loops]]
- [[grill-me]]
- [[domain-modeling]]
- [[agent-handoff-documents]]
