---
title: Replayable State Transformations
type: concept
tags: [architecture, composition, plugins, state-management]
created: 2026-09-22
updated: 2026-09-22
sources: [opencode-reloaded.md]
---

# Replayable State Transformations / ประกอบ State ใหม่จาก Contribution ที่ยังใช้

Replayable State Transformations คือ pattern ที่ให้แต่ละ component ประกาศ transformation ของตัวเอง แทนการเข้าไปแก้ shared state ตอนไหนก็ได้ Host เก็บ contribution เหล่านี้ตามลำดับ แล้วสร้าง state ใหม่จากฐานสะอาดทุกครั้งที่ input หรือ component เปลี่ยน

[[kit-langton|Kit Langton]] อธิบาย pattern นี้ผ่าน [[opencode-reloaded|OpenCode Reloaded]] ตัว [[opencode|OpenCode 2]] ใช้ abstraction ชื่อ `State` กับ model catalog, skill, command, agent, tool, MCP server และ formatter

## ปัญหาที่ pattern นี้แก้

Shared mutable state ทำให้ผลลัพธ์ขึ้นกับประวัติ:

- refresh ข้อมูลต้นทางอาจเขียนทับ policy ที่ plugin อีกตัวเพิ่งใส่
- record ที่ต้นทางลบแล้วอาจค้าง เพราะรอบใหม่เขียนเฉพาะของที่ยังมี
- operation ที่ไม่ idempotent อาจสะสมผลทุกครั้งที่ event ทำให้มันรันซ้ำ
- plugin ต้องรู้ว่าใครแก้อะไรมาก่อน จึงจะคืนหรือปรับค่าของตัวเองได้ถูก

ต่อให้เพิ่ม event เพื่อบอกว่า state เปลี่ยน ปัญหาก็ยังอยู่ เพราะ consumer ต้องประสานลำดับและกันไม่ให้ใครอ่านค่าระหว่างกลาง

**ได้อะไร:** pattern นี้ย้ายความรับผิดชอบเรื่องประวัติและลำดับออกจาก plugin แต่ละตัวมาไว้ที่ host จุดเดียว

## วิธีประกอบ State

ภาพย่อของรอบ rebuild คือ:

```text
empty state
  -> source contribution
  -> local additions
  -> policy filter
  -> limit adjustment
  -> published state
```

แต่ละ transformation รับ state ชนิดหนึ่งแล้วส่งต่อ state ชนิดเดิม Host จึงเก็บเป็นลำดับเดียวและ replay ทั้งชุดได้ พอ plugin หายไปก็ลบ transformation ของ plugin นั้น แล้วประกอบใหม่โดยไม่ต้องเขียน undo logic เฉพาะตัว

ตรงนี้ไม่ได้ทำให้ลำดับไม่มีความหมาย Policy filter ยังต้องอยู่หลัง source contribution ความต่างคือ host มองเห็นและควบคุมลำดับทั้งหมด แทนที่จะปล่อยให้ timer, event subscriber และ mutation กระจายกันตัดสิน

**ผลคือ:** state ปัจจุบันอธิบายได้จากฐานตั้งต้น ข้อมูลล่าสุด และรายการ contribution ที่ active ไม่ต้องรู้ mutation ทุกครั้งตั้งแต่โปรแกรมเริ่ม

## เปลี่ยน input ได้โดยไม่เปลี่ยน transformation

Transformation ไม่จำเป็นต้องเปลี่ยนทุกครั้งที่ข้อมูลเปลี่ยน ในตัวอย่าง OpenCode plugin ของ `models.dev` ลงทะเบียน function ครั้งเดียว Function อ่าน provider ชุดล่าสุดจาก closure พอ fetch รอบใหม่เสร็จ plugin แค่แทนข้อมูลใน closure แล้วสั่ง `reload`

จุดแยกนี้สำคัญ:

- contribution บอกกฎว่า component นี้เปลี่ยน state อย่างไร
- input บอกข้อมูลล่าสุดที่กฎนั้นจะใช้
- reload นำกฎทุกตัวมารันใหม่กับ input ปัจจุบัน

พอแยกสามอย่างนี้ออกจากกัน refresh จึงไม่ต้องสะสมผลบน state เก่า และ lifecycle ของ plugin ก็ไม่ต้องสร้าง event protocol เฉพาะคู่

## ใช้กับ hot reload อย่างไร

Host ต้องจำว่า transformation ใดมาจาก plugin ตัวไหน:

- เพิ่ม plugin: รัน plugin เก็บ contribution แล้ว rebuild state ที่แตะ
- แก้ plugin: ถอด contribution รุ่นเก่า รันรุ่นใหม่ แล้ว rebuild
- ลบ plugin: ถอด contribution ของไฟล์นั้น แล้ว rebuild โดยไม่มีมัน

ถ้า session ทุกตัวอ่าน published state ก้อนเดียวกัน การสลับก้อนใหม่ทำให้ environment เปลี่ยนพร้อมกัน Agent จึงเพิ่ม tool หรือ MCP server แล้วใช้ต่อได้โดยไม่เริ่ม session ใหม่

**ได้อะไร:** hot reload กลายเป็น lifecycle ของ contribution ไม่ใช่การไล่แก้ object ที่กำลังถูกใช้ทีละจุด

## เงื่อนไขที่ยังต้องออกแบบ

Pattern นี้ช่วยเรื่อง composition แต่ไม่ได้ตอบทุกเรื่องเอง:

- ต้องกำหนดลำดับ transformation ให้ชัด เพราะเรียงคนละแบบอาจได้ผลคนละก้อน
- ต้องตัดสินว่าจะทำอย่างไรเมื่อ transformation fail เพื่อไม่ให้ publish state ครึ่งสำเร็จ
- ต้องระวัง side effect ใน transformation เพราะ replay อาจทำให้ side effect เกิดซ้ำ
- ต้องวัดต้นทุน rebuild เมื่อ state ใหญ่หรือ contribution เยอะ
- ต้องมี trust boundary แยกต่างหาก เพราะ plugin ยังเป็น code ที่รันใน host
- ต้องคุม external input และ clock ถ้าต้องการ reproducibility จริง

แหล่งต้นทางอธิบายเฉพาะการประกอบ state กับ plugin lifecycle ของ OpenCode ยังไม่มี benchmark, rollback contract หรือ security model จึงควรอ่านรายการนี้เป็นคำถามออกแบบต่อ ไม่ใช่ capability ที่ยืนยันแล้ว

## See also

- [[opencode-reloaded]]
- [[opencode]]
- [[coding-harness]]
- [[plugin-manager]]
- [[harness-engineering]]
