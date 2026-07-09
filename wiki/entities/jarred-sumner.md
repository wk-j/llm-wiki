---
title: Jarred Sumner
type: entity
tags: [person, software-engineering, bun, ai]
created: 2026-07-09
updated: 2026-07-09
sources: [bun-in-rust.md]
---

# Jarred Sumner

**Jarred Sumner** คือผู้สร้าง [[bun|Bun]] และผู้เขียน [[bun-in-rust|Bun in Rust]]. เขาเล่าว่า Bun เวอร์ชันแรกถูกเขียนใน [[zig|Zig]] ภายในประมาณ 1 ปี ก่อนยุค LLM และ Zig เป็นเหตุผลสำคัญที่ project ขนาดใหญ่แบบนี้เกิดขึ้นได้.

ในบทความปี 2026 เขาบันทึกการ rewrite Bun จาก Zig เป็น [[rust|Rust]] ด้วย [[claude-code|Claude Code]] และ [[fable|Claude Fable 5]]. เขาไม่ได้ framing ว่า "กดปุ่มให้ AI rewrite". จุดเด่นคือเขาออกแบบ workflow เอง: porting guide, lifetime table, trial run, worktree sharding, adversarial reviewers, compiler-error queue, test/CI loop และ manual verification ก่อน merge.

## บทเรียนจากบทความ

Jarred เป็นตัวอย่างของบทบาทใหม่ใน [[agentic-engineering|agentic engineering]]: คนไม่ได้เขียนทุกบรรทัดเอง แต่ยังออกแบบระบบผลิตงาน, ตรวจงาน, แก้ process เมื่อ agent พลาด, อ่าน evidence และตัดสินใจ merge.

ใน source นี้ เขาแก้ workflow หลายครั้งเมื่อ agent ทำสิ่งผิด เช่น `git stash`/`git reset`, stub function เพื่อให้ compile ผ่าน, หรือ comment ยาวเพื่อ justify workaround. สิ่งนี้ทำให้บทความเป็นเคสของ [[harness-ratchet|harness ratchet]] ด้วย: failure ของ agent ถูกเปลี่ยนเป็น rule/process ที่ดีขึ้น.

## See also

- [[bun]]
- [[bun-in-rust]]
- [[dynamic-workflows]]
- [[adversarial-review-loops]]
- [[large-scale-changes]]
