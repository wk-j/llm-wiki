---
title: Conversation-Code Provenance
type: concept
tags: [provenance, collaboration, agents, version-control, context]
created: 2026-08-15
updated: 2026-08-15
sources: [software-is-made-between-commits.md]
---

# Conversation-Code Provenance / ที่มาของ code จากบทสนทนา

**Conversation-code provenance** คือความสามารถในการย้อนความสัมพันธ์สองทางระหว่างบทสนทนากับ code ที่เปลี่ยนไป บทสนทนาบอกเหตุผลหรือคำสั่ง ส่วน history บอกว่า operation ใดเกิดตามมา เป้าหมายคือให้คนและ agent หาได้ทั้ง “ข้อความนี้สร้าง code ตรงไหน” และ “code ตรงนี้เกิดจากการคุยอะไร”

แนวคิดนี้มาจาก [[nathan-sobo|Nathan Sobo]] ใน [[software-is-made-between-commits|Software Is Made Between Commits]] เขาเสนอว่าในงานกับ agent บทสนทนากำลังกลายเป็นต้นทางของ software จึงไม่ควรแยก transcript ไว้อีกระบบแล้วค่อยพยายามผูกกลับกับ commit ภายหลัง

## ทำไม line number กับ commit ยังไม่พอ

Line number เปลี่ยนเมื่อแทรก ย้าย หรือลบ code ส่วน commit เก็บ snapshot เป็นช่วง ๆ จึงมองไม่เห็นทุก operation ระหว่างทาง PR comment ช่วยอธิบาย snapshot ได้ แต่บางครั้งเหตุผลสำคัญเกิดขึ้นก่อนเปิด PR ไปแล้ว

ในแบบที่ DeltaDB เสนอ ทุก edit เป็น `delta` ที่มี identity คงที่ การอ้างอิงจึงเกาะกับ operation ไม่ใช่ตำแหน่งชั่วคราว คนเปิดได้ทั้ง code ตอนที่ข้อความถูกพูดและ code เวอร์ชันล่าสุด แม้บรรทัดจะย้ายไปแล้ว

**ได้อะไร:** provenance อยู่รอดเมื่อ code เคลื่อน และไม่ต้องพึ่งความจำของคนว่า transcript ช่วงไหนตรงกับ diff ส่วนใด

## การไหลสองทาง

| เริ่มจาก | สิ่งที่ต้องหาได้ | ใช้ทำอะไร |
|---|---|---|
| บทสนทนา | code ตอนนั้นและ code ปัจจุบัน | ตรวจว่าคำสั่งหรือเหตุผลกลายเป็น implementation แบบไหน |
| code | บทสนทนาที่สร้างและบทสนทนาที่แก้ต่อ | ทำความเข้าใจ intent ก่อนแก้ของเดิม |
| agent ปัจจุบัน | context และผู้ทำงานก่อนหน้า | ถามเหตุผล ลดการเดาซ้ำ และสานงานต่อ |

**ผลคือ:** history กลายเป็น context ที่ใช้งานต่อได้ ไม่ใช่แค่บันทึกย้อนหลังให้คนอ่าน

## ต่างจาก Git history และ PR อย่างไร

Git เหมาะกับ snapshot, branch, integration และการเชื่อมกับ CI ส่วน PR เหมาะกับ review/approval รอบ change ที่นิยามแล้ว Conversation-code provenance ดูชั้นก่อนหน้านั้น: งานระหว่างกำลังก่อตัวและเหตุผลที่ไหลมากับ edit

สองชั้นนี้ไม่จำเป็นต้องแทนกัน [[deltadb|DeltaDB]] อาจเก็บ continuous history แล้วส่ง milestone เข้า Git/PR แต่ source ยังไม่บอกว่า provenance, permission และ approval จะเดินข้าม boundary นี้อย่างไร

**ได้อะไร:** แยก “พื้นที่ก่อรูปงาน” ออกจาก “ประตู integrate งาน” แล้วค่อยถามว่าหลักฐานใดต้องส่งผ่านระหว่างสองพื้นที่

## Provenance ไม่เท่ากับความจริง

มี transcript ครบไม่ได้แปลว่าเหตุผลในนั้นถูก agent อาจเข้าใจ requirement ผิด คนอาจเปลี่ยนใจ หรือการแก้ถัดมาอาจทำให้คำอธิบายเดิมล้าสมัย ระบบจึงยังต้องมี test, review และ [[facts-first|fact]] ที่ตรวจซ้ำได้

การเก็บทุกบทสนทนายังเพิ่มคำถามเรื่องข้อมูลลับ สิทธิ์เข้าถึง retention ปริมาณ noise และการสรุป context ให้ agent โดยไม่กลบ fact สำคัญ Source เปิดตัว DeltaDB ยังไม่ตอบเรื่องเหล่านี้

**ผลคือ:** provenance ช่วยให้ตรวจเหตุผลย้อนหลังได้ แต่ไม่ควรถูกใช้แทน verification หรือ governance

## See also

- [[deltadb]]
- [[collaborative-ai-engineering]]
- [[context-engineering]]
- [[facts-first]]
- [[stacked-pull-requests]]
- [[git-worktrees]]
- [[software-is-made-between-commits]]

