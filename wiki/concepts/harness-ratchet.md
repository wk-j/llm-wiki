---
title: Harness Ratchet
type: concept
tags: [ai, agents, harness, feedback-loop, software-engineering]
created: 2026-05-10
updated: 2026-05-10
sources: [Agent Harness Engineering.md, ryan-lopopolo-harness-engineering.md]
---

# Harness Ratchet / กลไกล็อกความผิดพลาดไม่ให้เกิดซ้ำ

**Harness Ratchet** คือวิธีคิดว่า agent failure ทุกครั้งควรถูกแปลงเป็น constraint ถาวรใน [[coding-harness|coding harness]] ไม่ใช่แก้เฉพาะหน้าแล้วปล่อยให้เกิดซ้ำ

คำว่า ratchet หมายถึงกลไกที่หมุนย้อนกลับยาก พอทีมเจอความผิดพลาดหนึ่งครั้ง harness ต้องขยับไปข้างหน้า เช่น เพิ่ม rule, hook, test, lint, reviewer agent, หรือ permission gate เพื่อกัน failure class เดิม

## ตัวอย่างง่าย

สมมติ agent ส่ง PR ที่ comment out test แล้วหลุด merge:

1. เพิ่มกฎใน `AGENTS.md`: ห้าม comment out test เพื่อให้ผ่านงาน
2. เพิ่ม hook หรือ lint ดัก `.skip(`, `.only(`, หรือ test ที่ถูกปิด
3. ให้ reviewer subagent เช็คเรื่องนี้ก่อนส่ง PR
4. ถ้าพบ failure ให้ inject error กลับเข้า loop พร้อมวิธีแก้

จุดสำคัญคือไม่ใช่แค่ "เตือน agent" แต่ทำให้ระบบมีฟันบังคับจริง

**ได้อะไร:** ความผิดพลาดหนึ่งครั้งกลายเป็นการลดโอกาสผิดทั้งคลาสในอนาคต

## ต่างจากการยัด rule ตั้งแต่ต้นอย่างไร

Harness Ratchet ไม่ได้บอกให้เขียน `AGENTS.md` ยาว ๆ ตั้งแต่วันแรก ตรงข้ามเลย กฎควรมีที่มา:

- เคยเกิด failure จริง
- มีผลเสียพอที่จะคุ้มกับ token / latency / maintenance cost
- บอกได้ว่า rule นี้กัน behavior อะไร
- ถ้า model รุ่นใหม่ไม่ต้องใช้แล้ว ควรถอดออกได้

ตรงนี้เชื่อมกับ [[instruction-budget]] โดยตรง ถ้าใส่กฎเผื่อทุกอย่างตั้งแต่ต้น model จะเข้า dumb zone และทำตามกฎจริง ๆ แย่ลง

**ผลคือ:** prompt ที่ดีไม่ใช่ prompt ที่ยาวที่สุด แต่เป็น prompt ที่แต่ละบรรทัดมีประวัติรองรับ

## รูปแบบของ constraint

Constraint ที่ดีไม่จำเป็นต้องเป็นข้อความใน prompt เท่านั้น เลือกชั้นที่เหมาะกับ failure:

| Failure | ชั้นที่ควรแก้ |
|---|---|
| ลืม convention ของ repo | `AGENTS.md`, `CLAUDE.md`, skill |
| ใช้ API ผิดซ้ำ | doc snippet แบบ [[progressive-disclosure]] หรือ lint rule |
| รันคำสั่งเสี่ยง | pre-tool hook, permission gate, sandbox |
| ship code ที่ typecheck พัง | post-edit hook, CI gate, test loop |
| review ไม่รอบด้าน | [[subagent-patterns]] เช่น pipeline subagent แบบ security/reliability reviewer |
| context ยาวจนหลง | [[compaction]], tool-output offloading, new session |

**ได้อะไร:** failure แต่ละแบบถูกแก้ใน layer ที่บังคับได้จริง ไม่ใช่เอาทุกอย่างไปกองใน system prompt

## เชื่อมกับ Durable Feedback Loops

[[ryan-lopopolo|Ryan Lopopolo]] ใช้คำว่า **durable feedback loops** ในความหมายใกล้กัน: feedback จากคนควรถูกแปลงเป็น lint, tests, docs, หรือ reviewer personas เพื่อให้ agent แก้ตัวเองในรอบต่อไป

Addy Osmani เพิ่มมุมว่า harness ทั้งชุดคือ living artifact. ทุกครั้งที่ agent พลาด ทีมควรถามว่า "เราจะทำให้ exact mistake นี้เกิดซ้ำยากขึ้นตรงไหน"

**สรุป:** Harness Ratchet คือ durable feedback loop ที่มองจากมุมสถาปัตยกรรมของ harness

## ข้อควรระวัง

Ratchet ที่ดีควรขยับจาก failure จริง ไม่ใช่ความกลัวล่วงหน้า ถ้าเพิ่ม hook/gate มากเกินไป agent จะช้าลงและเสีย autonomy โดยไม่จำเป็น

อีกจุดคือกฎต้องถอดได้ เมื่อ model หรือ tool ดีขึ้น กฎบางอย่างจะกลายเป็น scaffolding เก่า ถ้าไม่ prune harness จะกลายเป็นกอง legacy policy ที่ทำให้ context หนักและ debug ยาก

## See also

- [[agent-harness-engineering]]
- [[coding-harness]]
- [[harness-engineering]]
- [[just-in-time-context]]
- [[instruction-budget]]
- [[progressive-disclosure]]
- [[subagent-patterns]]
