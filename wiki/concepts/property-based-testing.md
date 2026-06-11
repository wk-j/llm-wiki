---
title: Property-Based Testing (PBT)
type: concept
tags: [testing, verification, formal-methods, software-engineering]
created: 2026-06-11
updated: 2026-06-11
sources: ["Stop Writing Specs. Start Writing Facts. The Entire SDD Movement Is Already Obsolete..md"]
---

# Property-Based Testing (PBT) / ทดสอบด้วย "คุณสมบัติ" แทนตัวอย่าง

**Property-based testing** คือการเขียน test เป็น *คุณสมบัติที่ต้องจริงเสมอ* (universally quantified predicate) แล้วให้เครื่องสุ่ม input มายิงใส่เป็นร้อยเป็นพันเคส แทนที่จะเขียนตัวอย่าง input/output ทีละคู่แบบ example-based test เช่น แทนที่จะเขียน "sort([3,1,2]) ต้องได้ [1,2,3]" ก็เขียน "ทุก list ที่ sort แล้ว สมาชิกตัวซ้ายต้องไม่มากกว่าตัวขวา" แล้วให้ framework สุ่ม list มาลองเอง

เครื่องมือต้นตระกูลคือ **QuickCheck** (Haskell, 2000) ฝั่ง Python มี **Hypothesis** ฝั่ง Erlang มีของ Quviq

## เคส production ที่แรงที่สุด

งานของ **John Hughes** (ผู้ร่วมสร้าง QuickCheck, บริษัท Quviq) กับผู้ผลิตรถยนต์สวีเดน: โค้ด Erlang production 60,000 บรรทัด ใช้ PBT test แค่ **450 บรรทัด** เจอบั๊ก **25 ตัว** รวมถึง race condition ที่ example-based test เข้าไม่ถึง — อัตราส่วนโค้ดต่อ test ประมาณ 133:1

**ผลคือ:** test น้อยบรรทัดแต่ครอบคลุมพฤติกรรมกว้าง เพราะเราประกาศ "กฎ" แล้วให้เครื่องไปหาเคสที่ละเมิดกฎเอง

## ที่ทางในยุค AI coding

ใน [[facts-first]] property คือ fact ระดับกลาง (ระหว่าง single test กับ contract) — เป็น executable assertion ที่เครื่องตรวจได้โดยไม่ผ่านการตีความของ model ในแผนย้ายของ [[jaroslaw-wasowski|Wasowski]] invariant ที่เคยอยู่ใน prose spec จะถูกแปลงเป็น Hypothesis/QuickCheck test

มุมที่น่าสนใจสำหรับยุค agent: PBT เหมาะเป็นพิเศษกับโค้ดที่ AI เขียน เพราะมันตรวจ *พฤติกรรม* ไม่ผูกกับ *วิธีเขียน* — agent จะ implement แบบไหนก็ได้ ขอแค่ property ไม่พัง (หลักเดียวกับ [[behavioral-verifier]] ในโลก benchmark) และคนเขียน property ไม่กี่บรรทัดก็คุมงาน generate ได้กว้าง

## See also

- [[facts-first]]
- [[stop-writing-specs-start-writing-facts]]
- [[verifiability]]
- [[behavioral-verifier]]
- [[shift-left-testing]]
