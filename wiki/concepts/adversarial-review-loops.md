---
title: Adversarial Review Loops
type: concept
tags: [ai, agents, code-review, verification, software-engineering]
created: 2026-07-09
updated: 2026-07-09
sources: [bun-in-rust.md]
---

# Adversarial Review Loops / ลูปรีวิวแบบจับผิด

**Adversarial review loop** คือ pattern ที่แยก agent เขียนโค้ดออกจาก agent รีวิว แล้วตั้ง objective ของ reviewer ให้เป็น "หาทางที่โค้ดนี้ผิด" ไม่ใช่ "ช่วยให้โค้ดนี้ผ่าน". ใน [[bun-in-rust|Bun in Rust]] [[jarred-sumner|Jarred Sumner]] ใช้ pattern นี้ตลอด rewrite [[bun|Bun]] จาก [[zig|Zig]] เป็น [[rust|Rust]].

รูปแบบที่ source ใช้บ่อยคือ:

- 1 implementer เขียนหรือแก้ code
- 2 adversarial reviewers อ่าน diff ใน context แยก
- 1 fixer เอา feedback ที่ใช้ได้มาแก้

Reviewer ไม่ได้ถือ reasoning ของ implementer. มันเห็น diff แล้วถูกสั่งให้ assume ว่าโค้ดผิด. ตรงนี้สำคัญ เพราะ model ที่เขียนโค้ดมักอยากให้โค้ดถูกยอมรับ ส่วน model ที่ถูกตั้งบทเป็น reviewer ต้องหาหลักฐานว่าอย่าเพิ่งยอมรับ.

## ต่างจาก AI review ทั่วไปยังไง

AI review ทั่วไปมักออกแนว "looks good / consider edge cases". มันช่วยได้ แต่เป้าหมายยังนุ่มไป. Adversarial reviewer ต้องจับ failure mode ที่ compile ผ่านและดู plausible:

- async close ที่ raw pointer ยังถูก libuv ถือไว้ แต่ Rust `Box` drop ไปแล้ว
- negative timestamp ที่ `trunc()` ทำให้ nanoseconds ติดลบ
- `unwrap_or` ที่ evaluate argument แบบ eager จน panic ทั้งที่ branch หลักมีค่า

สามตัวอย่างนี้เป็น bug ที่ test/compile ไม่ได้จับทันที. Reviewer ต้องใช้ความเข้าใจ runtime semantics ไม่ใช่แค่ตรวจ style.

**ได้อะไร:** reviewer ที่ดีไม่ใช่คนพูดว่า "ผ่าน". reviewer ที่ดีเพิ่มแรงต้านให้ระบบก่อน code ที่ดูดีจะถูก merge.

## ทำไมต้องแยก context

ถ้า reviewer อยู่ใน context เดียวกับ implementer มันเห็นเหตุผลที่ implementer ใช้โน้มน้าวตัวเองว่าโค้ดน่าจะถูก. เหตุผลนั้นอาจช่วยเข้าใจ แต่ก็ bias ให้ reviewer อยาก accept. การแยก context ทำให้ reviewer อ่าน artifact เหมือนคน review PR จริง: ไม่ได้อยู่ในหัวคนเขียน ต้องพิสูจน์จาก diff และ behavior.

ตรงนี้เชื่อมกับ [[agentic-code-review|agentic code review]] โดยตรง. AI reviewer เป็น [[harness-guides-sensors|inferential sensor]] แต่ sensor จะคุ้มเมื่อ objective ชัดและไม่กลายเป็นตรายาง.

## ใช้กับงานใหญ่ยังไง

ใน Bun rewrite, adversarial review ไม่ได้เป็น step สวย ๆ ตอนท้าย. มันฝังอยู่ใน workflow หลายชั้น:

- ตรวจ `PORTING.md` และ `LIFETIMES.tsv`
- ตรวจ port ทีละไฟล์ว่า behavior ตรงกับ Zig เดิมไหม
- ตรวจ fix ของ compiler errors
- ตรวจ fix จาก test failure
- reject workaround ที่แค่ทำให้ compile ผ่าน

สิ่งนี้ทำให้ review เป็นส่วนหนึ่งของ [[dynamic-workflows|dynamic workflow]] ไม่ใช่งานคนอ่านกอง diff ตอนจบ. Human ยังต้อง monitor output และตัดสินใจ merge แต่ agent ทำงานจับผิดรอบแรกซ้ำ ๆ ให้ก่อน.

**ผลคือ:** ย้าย human attention จาก "หา bug ทุกบรรทัดเอง" ไปเป็น "ตรวจว่าระบบจับผิดกำลังจับถูกเรื่องไหม".

## ข้อจำกัด

Adversarial review loop ไม่ได้แทน [[behavioral-verifier|behavioral verifier]] หรือ test suite. Reviewer ยังเป็น model เดาเชิงความหมายได้ผิด และ blind spot ของ model อาจซ้ำกัน. ในงานเสี่ยงสูงต้องจับคู่กับ deterministic gates: compiler, tests, fuzzing, sanitizer, CI และคนอ่าน path สำคัญ.

อีกข้อคือ reviewer อาจสร้าง noise. ถ้าไม่มี fixer หรือ human ที่คัด signal, loop จะกลายเป็น report ยาว ๆ ที่เพิ่ม [[orchestration-tax|orchestration tax]].

## วิธีจำสั้น ๆ

Adversarial review loop = **writer แยกจาก skeptic, skeptic เห็น diff ไม่เห็นข้อแก้ตัว, fixer แก้จาก evidence, verifier ตัดสิน behavior**.

## See also

- [[bun-in-rust]]
- [[agentic-code-review]]
- [[dynamic-workflows]]
- [[behavioral-verifier]]
- [[orchestration-tax]]
- [[harness-guides-sensors]]
