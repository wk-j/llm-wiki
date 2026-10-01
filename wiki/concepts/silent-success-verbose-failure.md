---
title: Silent Success, Verbose Failure
type: concept
tags: [ai, agents, harness, feedback-loop, context-management]
created: 2026-09-30
updated: 2026-09-30
sources: [agent-harness-engineering.md, engineering-the-harness-thoughtworks.md, harness-engineering-bockeler.md]
---

# Silent Success, Verbose Failure / ผ่านเงียบ พังละเอียด

**Silent success, verbose failure** คือกฎออกแบบ output ของ sensor (ตัวตรวจที่รันหลัง agent ทำงาน เช่น test, linter, type checker) ถ้าผ่าน ให้พูดน้อยที่สุด ถ้าพัง ให้ส่งรายละเอียดที่เอาไปแก้ได้กลับเข้า loop ของ agent

หลักนี้โผล่ในสองแหล่งที่เขียนแยกกัน [[addy-osmani|Addy Osmani]] พูดไว้ใน [[agent-harness-engineering]] ว่า "success silent, failure verbose" ตอนอธิบาย hook ส่วน [[thoughtworks|Thoughtworks]] ใช้ชื่อ "silent success, verbose failure" ใน [[engineering-the-harness-thoughtworks]] ตอนอธิบาย sensors

## ทำไมผ่านแล้วต้องเงียบ

ส่วนนี้ว่าด้วยต้นทุนของข่าวดี output ของ tool ทุกบรรทัดกิน context ของ agent ถ้า test 400 ตัวพิมพ์ `PASS` ทีละบรรทัด agent ต้องแบก log นั้นไปทั้ง session โดยไม่ได้ข้อมูลอะไรเพิ่ม คนที่มาอ่านทีหลังก็ต้องไล่หาบรรทัดที่สำคัญ

- ประหยัด token และลดโอกาสเกิด [[context-rot]] (อาการที่ model แย่ลงเมื่อ context ยาว)
- ไม่แย่ง attention ไปจากเรื่องที่ต้องตัดสินจริง
- "ผ่าน" สรุปได้ในบรรทัดเดียว เช่น exit code 0 หรือ `typecheck ok`

## ทำไมพังแล้วต้องละเอียด

พอพัง agent ต้องรู้ว่าพังตรงไหน เพราะอะไร จะได้แก้เองโดยไม่ต้องมีคนมาอธิบาย Thoughtworks ยกตัวอย่างของที่ควรส่งกลับ ได้แก่ stack trace, ตำแหน่งของ lint error และ diff ของ test ที่พัง

ถ้าได้แค่ `Build failed` agent ต้องเดาเอา หรือต้องรันซ้ำแบบ verbose เองอีกรอบ เปลืองทั้งเวลาและ token

**ผลคือ:** loop แก้ตัวเองได้ คนไม่ต้องเป็นตัวกลางคัดลอก error มาแปะใน chat

## ละเอียดไม่ได้แปลว่าเทหมด

"verbose" ในที่นี้คือละเอียดพอจะแก้ได้ ไม่ใช่ log ดิบทั้งก้อน Addy เสนอไว้ใน [[progressive-disclosure]] ว่าให้เก็บ log ยาวไว้ใน filesystem แล้วส่งเข้า context เฉพาะ header/footer หรือ error ที่สำคัญ

สองหลักนี้ต้องใช้คู่กัน เลือกส่งเฉพาะส่วนที่ทำให้ agent ตัดสินใจต่อได้ แล้วชี้ไปที่ไฟล์เต็มเผื่อต้องขุดต่อ

## ความเงียบที่หลอกตา

ผ่านเงียบมีด้านที่ต้องระวัง ถ้า sensor พังเอง ถูกข้าม หรือไม่ได้รันจริง ผลก็เงียบเหมือนกัน [[birgitta-bockeler|Birgitta Böckeler]] ตั้งคำถามไว้ใน [[harness-guides-sensors]] ว่า sensor ที่ไม่เคยลั่นเลย แปลว่าคุณภาพดี หรือแปลว่ากลไกตรวจจับไม่พอ

วิธีกันที่พอทำได้ (wiki สังเคราะห์เอง แหล่งไม่ได้เสนอ):

- ให้ "ผ่าน" ยังบอกขอบเขตสั้น ๆ เช่น จำนวน test ที่รัน หรือ check ที่ถูกข้าม
- ตรวจความครอบคลุมของ harness เป็นระยะ ด้วย mutation testing หรือฉีด bug ทดสอบว่า sensor ลั่นจริง

**ได้อะไร:** เงียบแบบมีหลักฐานว่ารันแล้ว ต่างจากเงียบเพราะไม่มีใครตรวจ

## See also

- [[agent-harness-engineering]]
- [[engineering-the-harness-thoughtworks]]
- [[harness-guides-sensors]]
- [[progressive-disclosure]]
- [[context-rot]]
- [[harness-ratchet]]
- [[addy-osmani]]
- [[thoughtworks]]
