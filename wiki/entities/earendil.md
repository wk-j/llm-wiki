---
title: Earendil
type: entity
tags: [company, ai, agents, software-engineering]
created: 2026-07-04
updated: 2026-10-07
sources: [code-isnt-free-mario-zechner-hard-truths-coding-ai.md, what-is-codemode-armin-ronacher.md]
---

# Earendil

**Earendil** คือบริษัท/ทีมที่ [[mario-zechner|Mario Zechner]] เข้าร่วมและทำ [[pi-agent|pi]] ต่อร่วมกับ [[armin-ronacher|Armin Ronacher]] ตามที่เล่าใน [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]]. Source นี้บอกว่า pi จะยังเป็น open source แต่ Mario มองหามูลค่าเพิ่มเติมที่ทำให้ทีมเล็กอยู่ได้.

ในบทสัมภาษณ์ Earendil ยังเป็นบริบทของเป้าหมายระยะยาว: ไม่ใช่แค่ coding agent บน terminal แต่รวม application layer, local inference, remoteability, observability, durability, และ SDK ที่ deploy agent ได้หลาย environment.

ใน [[what-is-codemode-armin-ronacher|What is Codemode]] [[armin-ronacher|Armin]] ลิงก์ไปที่ sandbox ชื่อ Gondolin ซึ่งอยู่ใต้ `earendil-works.github.io` เขายกมาเป็นตัวอย่างว่า sandbox แบบนี้กั้นคำสั่ง bash ได้ แต่ไม่ได้กั้นตัว harness (ดู [[harness-vs-execution-environment]]) การที่ Gondolin เป็นของ Earendil อนุมานจากโดเมนของลิงก์เท่านั้น บทความไม่ได้บอกตรง ๆ

## Open questions

- โมเดลธุรกิจและ product line ของ Earendil ยังไม่ได้ ingest จากแหล่งตรง รวมถึง Gondolin
- รายละเอียดบทบาทของ [[armin-ronacher|Armin Ronacher]] ใน Earendil ยังอิงจากคำบอกเล่าของ Mario

## See also

- [[mario-zechner]]
- [[pi-agent]]
- [[armin-ronacher]]
- [[what-is-codemode-armin-ronacher]]
- [[harness-vs-execution-environment]]
