---
title: Bun in Rust
type: source
tags: [ai, software-engineering, rust, bun, agents]
created: 2026-07-09
updated: 2026-07-09
sources: [https://bun.com/blog/bun-in-rust]
---

# Bun in Rust / Bun เขียนใหม่ด้วย Rust

บทความนี้คือบันทึกของ [[jarred-sumner|Jarred Sumner]] (ผู้สร้าง [[bun|Bun]]) ว่าทีมย้าย Bun จาก [[zig|Zig]] ไปเป็น [[rust|Rust]] ได้อย่างไร โดยใช้ [[claude-code|Claude Code]] และ model pre-release ชื่อ [[fable|Claude Fable 5]] ช่วยเขียน แก้ และ review โค้ดในสเกลที่ปกติต้องใช้ทีมหลายคนเป็นปี

แก่นไม่ใช่แค่ "AI เขียนโค้ดเร็ว" แต่คือการออกแบบระบบรอบการ rewrite: porting guide, lifetime table, test suite เดิม, compiler errors เป็น queue, adversarial reviewers, worktree isolation, CI หลาย platform, fuzzing และ human judgement ที่คุมจังหวะ merge.

## เรื่องนี้สำคัญตรงไหน

[[bun|Bun]] เป็น runtime/toolchain ของ JavaScript ที่ scope ใหญ่มาก: transpiler, bundler, package manager, test runner, module resolution, HTTP/WebSocket client และ implementation ของ Node APIs หลายสิบตัว. โค้ดเดิมส่วนใหญ่เป็น Zig และมี C/C++ ปนอยู่ผ่าน [[javascriptcore|JavaScriptCore]], uWebSockets, BoringSSL, SQLite และ library อื่น ๆ.

ปัญหาที่ดันให้ต้อง rewrite คือ bug กลุ่ม memory safety: use-after-free, double-free, leak, race, out-of-bounds read/write. ทีมมี ASAN, fuzzing, leak tests อยู่แล้ว แต่ bug ยังโผล่ เพราะ Bun อยู่ตรงจุดยาก: JavaScript เป็น garbage-collected language แต่ runtime ต้องคุยกับ memory ที่จัดการเองใน Zig/C/C++.

**ได้อะไร:** การเลือกภาษาไม่ได้เป็นเรื่อง taste อย่างเดียว. สำหรับ runtime ที่ผสม GC กับ manual memory, type system และ cleanup semantics มีผลกับ stability โดยตรง.

## ทำไม Rust แทนที่จะเป็น style guide

Jarred บอกว่า Zig ทำให้ Bun เกิดขึ้นได้ และไม่ได้โทษ Zig แบบเหมารวม. แต่ในงานของ Bun คำถาม "memory นี้ใคร owns", "free ตอนไหน", "free ซ้ำไหม", "exception จาก JavaScript เกิดแล้ว cleanup ยังถูกไหม" ต้องตอบถูกทุกครั้ง.

ทางหนึ่งคือเขียน style guide หรือ smart pointer แบบ Rust ใน Zig. แต่ enforcement ยังพึ่ง code review กับ lint/static analyzer. Rust ให้สิ่งที่ต่างกว่า: use-after-free, double-free และ forgot-to-free ใน error path จำนวนมากกลายเป็น compiler error หรืออย่างน้อยถูกบังคับให้ encode ownership/lifetime ชัดขึ้น. `Drop` ก็ช่วยให้ cleanup ผูกกับ scope ของค่า ไม่ต้องจำใส่ `defer` ทุก call site.

**ผลคือ:** Rust ไม่ได้ทำให้ bug หายเองทั้งหมด แต่ย้าย failure mode หลายอย่างจาก "หลุดไปเจอใน fuzzing/production" มาเป็น "compiler หรือ review เห็นเร็วขึ้น".

## วิธี rewrite: เหมือน transpile ก่อน ค่อยทำให้ idiomatic ทีหลัง

Jarred เลือก **rewrite ทั้งก้อน** แทน incremental rewrite. เหตุผลคือ incremental rewrite จะสร้าง temporary bridge code เยอะ และเจ็บในระยะกลาง. แต่เขาไม่ได้สั่ง Claude แบบกว้าง ๆ ว่า "rewrite Bun in Rust". เขาเริ่มจาก prep work:

- คุยกับ Claude ราว 3 ชั่วโมงเพื่อทำ `PORTING.md` mapping pattern/type จาก Zig ไป Rust
- ให้ workflow วิเคราะห์ lifetime ของ field ใน struct ทุกไฟล์ แล้ว serialize เป็น `LIFETIMES.tsv`
- ให้ adversarial reviewers ตรวจ `PORTING.md` กับ `LIFETIMES.tsv`
- ทำ trial run แค่ 3 ไฟล์ก่อน โดยมี 1 implementer, 2 reviewers, 1 fixer

เป้าหมายรอบแรกคือ Rust ที่หน้าตาเหมือน mechanical port จาก Zig ให้มากที่สุด. Refactor เพื่อลด `unsafe` และทำให้ idiomatic ค่อยตามมาหลัง Bun v1.4.

**ได้อะไร:** สำหรับ rewrite ใหญ่ ความใกล้เคียงกับของเดิมเป็น feature. ยิ่งโค้ดใหม่คล้ายโค้ดเก่า คนที่รู้ระบบเดิมยิ่ง review behavior ได้.

## Dynamic workflows ที่รันจริง

Jarred ใช้ workflow แบบ dynamic ราว 50 ตัว รันต่อเนื่อง 11 วัน. ตัวอย่าง loop คือ:

- สร้าง porting guide
- port ทุก `.zig` เป็น `.rs`
- แก้ compiler errors ทีละ crate
- ทำให้ subcommand เช่น `bun test` และ `bun build` กลับมารันได้
- ไล่ test suite ทั้งหมดให้ผ่าน
- refactor และ cleanup หลายรอบ

ตอน peak มี 4 workflow แยก worktree แต่ละอันมี Claude 16 ตัว รวมประมาณ 64 ตัวพร้อมกัน. มี 6,502 commits ใน branch port, peak 58 commits/minute และ diff ที่ merge เข้าไปเพิ่มสุทธิราว 1,009,272 lines.

นี่เป็นหลักฐานภาคสนามที่หนักกว่า claim ตอนเปิดตัว [[dynamic-workflows|dynamic workflows]]: ไม่ใช่แค่ demo ว่า agent ทำ migration ได้ แต่เป็นการย้าย runtime ใหญ่จริงผ่าน compiler/test/CI จริง.

## Adversarial review loops

ส่วนที่น่าสนใจที่สุดคือ pattern `1 implementer + 2 adversarial reviewers + 1 fixer`. Reviewer อยู่ใน context แยกจาก implementer และถูกสั่งให้ assume ว่าโค้ดผิด. หน้าที่คือหาเหตุผลว่าทำไม diff นี้พัง ไม่ใช่ช่วยเขียน.

บทความยก bug ที่ reviewer จับได้ เช่น:

- libuv close เป็น async แต่ Rust `Box` drop ทันที ทำให้ use-after-free/double-free
- แปลงเวลา negative fractional ด้วย `trunc()` ทำให้ `nsec` ติดลบ ต้องใช้ `floor()`
- `unwrap_or` ใน Rust evaluate argument แบบ eager ทำให้ panic ทั้งที่ค่าหลักมีอยู่ ต้องใช้ `unwrap_or_else`

สามเคสนี้ compile ผ่านและดู plausible. ตรงนี้เป็นแก่นของ [[adversarial-review-loops|adversarial review loops]]: reviewer ไม่ได้ให้ verdict สวย ๆ แต่ต้องหา failure mode ที่ test หรือ compiler ยังไม่จับ.

**ได้อะไร:** AI reviewer มีค่าเมื่อบทบาทมันถูกแยกจาก writer และ objective คือ "หาทางที่มันผิด" ไม่ใช่ "ช่วยให้ PR ดู mergeable".

## Compiler errors เป็น work queue

หลัง port เสร็จ มี compiler errors ประมาณ 16,000 จุด. Workflow รัน `cargo check`, group error ตาม crate/file, แล้วแบ่งให้ Claude แก้เป็น batch. แต่มี false start: Claude เข้าใจ "ทำให้ compile" เป็น "stub function ที่มี error ทิ้งไว้". Jarred เลยเพิ่มกฎให้ reviewer reject workaround ที่ต้องใช้ comment ยาว ๆ อธิบายว่าทำไมโอเค.

อีกปัญหาคือ cyclic dependencies. โค้ด Zig เดิมเป็นเหมือน compilation unit เดียว แต่ Rust ใหม่ถูกแยกเป็นราว 100 crates เพื่อ compile เร็วขึ้น. การแยกนี้ทำให้เกิด cycle และ error จำนวนมาก ต้องมี workflow อีกตัว classify ว่าโค้ดควรอยู่ crate ไหน.

**ผลคือ:** compiler ไม่ใช่แค่เครื่องจับผิดหลังเขียนเสร็จ แต่เป็น queue generator สำหรับ agent fleet. แต่ queue ต้องมี guardrail ไม่งั้น agent optimize เพื่อให้ error หายเฉย ๆ.

## Test suite เป็น oracle

Bun มี test suite เขียนด้วย TypeScript จึงไม่ผูกกับ implementation language. นี่ทำให้ rewrite จาก Zig เป็น Rust ยังใช้ oracle เดิมได้. หลัง compile ผ่าน ทีมไล่ smoke test, local tests, แล้ว CI จนครบทุก platform.

ตัวเลขก่อน merge:

- 0 tests skipped หรือ deleted
- 6 platform green ใน Buildkite
- Debian 13 x64: 60,624 tests / 1,386,826 `expect()` calls
- macOS 14 arm64: 58,850 tests / 1,259,953 `expect()` calls
- Windows 2019 x64: 57,337 tests / 1,007,544 `expect()` calls

Jarred ยังบอกว่าตรวจด้วยตัวเองว่า tests รันจริง ไม่ใช่ถูก skip. นี่โยงตรงกับ [[behavioral-verifier|behavioral verifier]] และ [[facts-first|facts-first]]: งาน rewrite ข้ามภาษาเชื่อได้เพราะมีพฤติกรรมที่ตรวจได้ ไม่ใช่เพราะ diff ดูดี.

## ความล้มเหลวระหว่างทาง

บทความไม่ได้ทำให้ process ดูสะอาดเกินจริง. มีหลายจุดที่ workflow พัง:

- Claude บางตัว `git stash`, อีกตัว `git stash pop`, แล้วมี `git reset HEAD --hard` ทำให้ชนกัน
- worktree มากเกินทำให้ disk space ไม่พอ เพราะ repo Bun ใหญ่
- command ช้าอย่าง `grep` freeze disk I/O บน EC2 เพราะลืมเพิ่ม IOPS
- test บางกลุ่มใช้ resource หนักมาก เช่น spawn process ประมาณ 10k ตัว หรืออ่าน/เขียน disk เป็น GB
- ต้องใช้ `systemd-run`/cgroups จำกัด memory/CPU และ isolate pid namespace แต่เครื่องก็ยังล่มจาก disk หลายรอบ

**ได้อะไร:** scale agent ไม่ใช่แค่ scale token. ต้อง scale filesystem, disk I/O, worktree policy, command permissions, resource isolation และ observability ด้วย.

## Cost และผลลัพธ์

ก่อน merge ใช้ประมาณ 5.9B uncached input tokens, 690M output tokens และ 72B cached input token reads. Jarred ประเมินเป็นประมาณ $165,000 ตาม API pricing. เขาเทียบว่าถ้าทำมือ น่าจะใช้ engineer 3 คนที่รู้ codebase เต็มบริบราว 1 ปี และช่วงนั้นทีมคงทำ feature/security/compatibility ต่อไม่ได้.

หลัง rewrite:

- Bun v1.4.0 แก้ bug 128 ตัวที่ reproduce ได้ใน v1.3.14
- known regressions จาก rewrite 19 ตัว และแก้หมดแล้ว
- `Bun.build()` leak หลาย MB ต่อ build ใน v1.3.14 แต่ v1.4.0 memory level off หลังราว 600 MB ใน benchmark 2,000 builds
- binary size เล็กลงประมาณ 20% บน Linux/Windows เมื่อรวม Rust rewrite, ICU changes และ identical code folding
- stack usage ลดลงใน recursive descent parsers
- benchmark หลาย workload เร็วขึ้นราว 2%-5%

**ข้อควรระวัง:** ตัวเลขทั้งหมดมาจาก Bun team เองและอยู่ในบริบท canary/ก่อน release เต็ม. ควรอ่านเป็น source-attributed claim จนกว่าจะมี benchmark ภายนอก.

## Porting mistakes ที่น่าจำ

บทความย้ำว่า rewrite ใหญ่ไม่มีทาง zero regression. Bug หลายตัวมาจาก syntax คล้ายกันแต่ semantics ต่างกัน:

- Zig `assert` เป็น function ที่ argument รันทุก build; Rust `debug_assert!` เป็น macro ที่หายไปใน release build ทำให้ side effect หาย
- Zig helper cast slice ด้วย `@divTrunc` และ ignore trailing odd byte; Rust `bytemuck::cast_slice` panic
- Zig `ReleaseFast` เอา bounds checks ออกบน macOS/Linux; Rust release ยัง bounds-check ทำให้ off-by-one เดิมกลายเป็น panic
- Zig `comptime` format string rewrite marker ก่อน substitute argument; Rust function เห็น string หลัง format แล้ว parser กิน escape sequence ผิด ต้องเป็น macro

**ได้อะไร:** mechanical port ยังต้องมี semantic audit. ความเหมือนทาง syntax เป็นกับดัก เพราะคนกับ model เห็นว่า "เหมือนเดิม" ทั้งที่ runtime behavior ต่าง.

## Production และ shipping

[[prisma|Prisma]] เปิด public beta ของ Prisma Compute บน Bun Rust rewrite. [[claude-code|Claude Code]] v2.1.181 ขึ้นไปก็ใช้ Rust port ของ Bun แล้ว; source บอก startup บน Linux เร็วขึ้น 10% และ user แทบไม่สังเกต. Jarred สรุปว่า boring is good.

Bun v1.3.14 เป็น version สุดท้ายที่เขียนด้วย Zig. Bun v1.4.0 จะเป็น version แรกที่เขียนด้วย Rust และตอนบทความออกมี canary ให้ลอง.

## ความสัมพันธ์กับหน้าอื่น

- [[dynamic-workflows]] — เคส Bun คือหลักฐาน field-scale ของ workflow แบบนี้
- [[large-scale-changes]] — rewrite นี้เป็น LSC แบบข้ามภาษา แต่ใช้ test suite และ CI เป็นฐาน ไม่ใช่แค่ script rewrite
- [[adversarial-review-loops]] — source นี้ให้ pattern ชัดที่สุดของ maker/checker/fixer
- [[agentic-code-review]] — AI reviewer เป็น sensor ที่คุ้มเมื่อแยก objective จาก implementer
- [[git-worktrees]] — worktree แก้ collision แต่ยังมี disk/IO/bookkeeping cost
- [[orchestration-tax]] — 64 Claudes ลดเวลาทำงาน แต่เพิ่มภาระ monitoring, evidence reading และ merge judgement
- [[ai-token-economics]] — $165k token cost เป็นตัวอย่างว่า agentic rewrite ถูกเมื่อเทียบกับปีคน แต่ยังเป็นเงินจริงที่ต้องนับ

## See also

- [[bun]]
- [[jarred-sumner]]
- [[rust]]
- [[zig]]
- [[claude-code]]
- [[fable]]
- [[dynamic-workflows]]
- [[adversarial-review-loops]]
- [[large-scale-changes]]
- [[behavioral-verifier]]
- [[git-worktrees]]
- [[orchestration-tax]]
