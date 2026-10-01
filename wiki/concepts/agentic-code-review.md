---
title: Agentic Code Review
type: concept
tags: [ai, agents, code-review, verification, software-engineering]
created: 2026-06-16
updated: 2026-09-30
sources: [Agentic Code Review.md, aom-fable-elysia-2-audit.md, bun-in-rust.md, dhh-ai-programming-setup-lex-clips.md, claude-codes-new-intent-md-rob-shocks.md, dillon-mulroy-ships-production-code-he-didnt-write.md, ai-native-sdlc-playbook.md, engineering-the-harness-thoughtworks.md]
---

# Agentic Code Review / การ review โค้ดในยุค agent

**Agentic code review** คือวิธีออกแบบ code review ใหม่เมื่อ coding agent ผลิตโค้ดได้เร็วกว่า review capacity ของมนุษย์หลายเท่า. แก่นไม่ใช่ "ให้ AI review แทนคน" แต่คือ **จัดระบบความเชื่อมั่น**: ใช้ deterministic gate, AI reviewer, risk tier, และ human judgement ให้ถูกที่.

[[addy-osmani|Addy Osmani]] (วิศวกร Google ที่เขียนเรื่อง [[orchestration-tax|orchestration tax]] และ [[loop-engineering|loop engineering]]) สรุปใน [[agentic-code-review|Agentic Code Review]] ว่า writing cheap ลงแล้ว แต่ understanding ยังแพงเท่าเดิม. Review เลยกลายเป็น skill ที่ leverage สูงที่สุดใน software ตอนนี้.

## ปัญหาหลัก: output โตเร็วกว่า trust

สมัยก่อน senior engineer อ่านโค้ดได้เร็วกว่า junior เขียนโค้ด. Review เลยตาม production ทันโดยไม่ต้องออกแบบมาก. Agent ทำลายสมดุลนั้น. มันผลิต diff ใหญ่และดูเรียบร้อยได้เร็วมาก แต่ human reading speed ไม่ได้เร็วขึ้น.

นี่คือรูปเฉพาะของ [[orchestration-tax|orchestration tax]]: คอขวดไม่ใช่การเขียนแล้ว แต่คือการตัดสินว่า change นี้ถูกไหม, ควร merge ไหม, และใครเข้าใจพอจะรับผิดชอบมัน.

**ได้อะไร:** ถ้าเพิ่ม agent โดยไม่เพิ่ม review system ระบบจะไม่ ship ดีขึ้นเท่าที่ dashboard บอก. มันแค่สะสม unread code, shallow review, และ [[cognitive-surrender|cognitive surrender]].

## Review ต้อง tier ตาม blast radius

Agentic review เริ่มจากถามว่า "ถ้าพัง เสียหายแค่ไหน" ไม่ใช่ "ใครเขียน". ตัวแปรหลักมีสามตัว:

- **Blast radius** — bug กระทบอะไร: ไม่มีใคร, ผู้ใช้จริง, เงิน, privacy, security, on-call
- **อายุของโค้ด** — prototype ที่ทิ้งได้ หรือ subsystem ที่จะอยู่หลายปี
- **จำนวนคนที่ต้องเข้าใจ** — solo builder หรือทีมที่ต้อง share ownership

ดังนั้น review depth ต้องเป็น dial:

| บริบท | Review ที่สมเหตุสมผล |
|---|---|
| Solo / no users / throwaway | test จริง + automation + อ่านส่วนเสี่ยง |
| เริ่มมี users / team เล็ก | intake evidence + PR เล็ก + owner review ตรง path สำคัญ |
| Legacy / high-blast-radius | type/test/CI + AI reviewers ต่างชนิด + system owner + security/architecture pass |

**ผลคือ:** ไม่เสีย human attention กับ boilerplate แต่ก็ไม่เอา "tests pass" ไปแทน judgement ใน path ที่พังแล้วเจ็บ.

## Intent ต้องมากับ PR

Agent PR มักมีปัญหาแปลกกว่ามนุษย์เขียน: โค้ดอาจดูดี แต่ไม่มีใครรู้ว่า "ทำไม" มันออกมาแบบนั้น. Reasoning trace ของ agent เคยมีอยู่ตอนทำงาน แต่หายไปก่อนถึง PR. Reviewer เลยต้องย้อนสร้าง intent เองจาก diff.

Agentic review จึงควร require ก่อน review:

- purpose ของ change
- decision log สั้น ๆ: เลือกวิธีนี้เพราะอะไร, ตัดทางเลือกอะไรทิ้ง
- test output / proof ว่ารันแล้ว
- risk note: path ไหนเปลี่ยน, user impact คืออะไร
- PR ที่เล็กพอให้คนอ่านจริง

ตรงนี้ผูกกับ [[intent-gap|intent gap]] โดยตรง. Natural language plan อย่างเดียวไม่พอ แต่ไม่มี intent เลยก็ทำให้ reviewer กลายเป็นคนแรกที่ต้องเข้าใจโค้ดจากศูนย์.

**ได้อะไร:** ย้ายงานกู้ intent กลับไปที่คน/agent ที่ submit PR ซึ่งมี context ถูกกว่า แทนให้ reviewer จ่ายแพงทีหลัง.

## AI reviewer เป็น sensor ไม่ใช่ verdict

AI reviewer มีประโยชน์มากใน agentic review เพราะมันเป็น [[harness-guides-sensors|inferential sensor]] ที่จับสิ่งเชิงความหมายได้: bug pattern, missing edge case, architecture smell, security concern. แต่ output ของมันควรเป็น input ให้มนุษย์ ไม่ใช่คำตัดสินสุดท้าย.

หลักใช้ที่สำคัญ:

- ใช้ reviewer ที่ต่าง character กันในงานเสี่ยง เช่น ตัวหนึ่งเน้น correctness อีกตัวเน้น production failure severity
- อย่าวัดจาก benchmark กลางอย่างเดียว ให้วัดกับ codebase ของตัวเอง
- ให้ AI reviewer ช่วยจัดลำดับ attention: safe-looking, needs work, high-risk
- อย่า auto-merge เพราะ AI บอกว่า looks good

ความต่างของ reviewer สำคัญเพราะ blind spot ของ model มัก correlated. สี่สำเนาของ model เดียวกันไม่เท่ากับสี่มุมมอง.

**ผลคือ:** AI review ช่วยให้มนุษย์ใช้เวลาในจุดที่แพงที่สุด แต่ accountability ยังอยู่กับคนกด merge.

## Adversarial review loop: reviewer ต้องจับผิดจริง

[[bun-in-rust|Bun in Rust]] ให้ pattern ที่ concrete กว่า "ให้ AI review": [[jarred-sumner|Jarred Sumner]] ใช้ 1 implementer, 2 adversarial reviewers, และ 1 fixer ในหลาย workflow. Reviewer อยู่ใน context แยกจาก implementer และถูกสั่งให้ assume ว่าโค้ดผิด.

ผลที่จับได้เป็น bug ที่ compile ผ่านและดู plausible เช่น async close ที่ทำให้ `Box` drop เร็วเกินจน use-after-free/double-free, การแปลง timestamp ติดลบด้วย `trunc()` จน `nsec` ติดลบ, และ `unwrap_or` ที่ evaluate argument แบบ eager จน panic. ดู [[adversarial-review-loops]].

**ได้อะไร:** AI reviewer จะคุ้มกว่าเมื่อ objective เป็น adversarial และแยกจากคน/agent ที่เขียน. ถ้า reviewer แค่อยู่ในบท "ช่วยให้ PR ผ่าน" มันกลายเป็นอีกเสียงที่เพิ่ม borrowed confidence.

## Deep audit เป็น review tier สูง

[[aom-khunpanitchot|Aom Khunpanitchot]] ให้ตัวอย่างสุดโต่งใน [[aom-fable-elysia-2-audit|Fable audit Elysia 2]]. เขาให้ AI หลายตัว audit [[elysia-2|Elysia 2]] แล้วส่วนใหญ่บอกว่าพร้อม stable/RC. แต่ [[fable|Fable]] รันผ่าน ultracode auto mode, แตก agent เกือบ 100 ตัว, แล้วส่ง report 104 ข้อที่สรุปว่ายังไม่เหมาะขึ้น RC.

นี่คือ [[deep-agent-audit|deep agent audit]]: ไม่ใช่ review ทุก PR แต่เป็น review tier สูงสำหรับ release gate หรือ codebase สำคัญ. จุดที่ควรเชื่อไม่ใช่ "Fable บอกว่าไม่พร้อม" แต่คือ report มีปัญหาที่ trace ได้, severity ชัด, วิธีแก้ชัด, และมีการ verify.

**ได้อะไร:** AI reviewer มีหลายระดับ. งานประจำใช้ sensor เบา ๆ ได้ แต่งาน release ควรยอมจ่าย budget ให้ audit ลึกขึ้น แล้วให้มนุษย์ตัดสินจาก evidence ไม่ใช่จากความมั่นใจของ model.

## Deterministic gate ต้องแข็งกว่าเดิม

ยิ่ง agent เก่งในการทำให้ dashboard เขียว ยิ่งต้องรักษา gate ที่ไม่ถูกกล่อมด้วยภาษา. CI, type checker, linter, test, coverage threshold, mutation testing, security scan คือกำแพงที่ควรย้ายซ้ายและย้ายยาก.

จุดที่ต้องอ่านด้วยตาคน:

- test ถูกลบหรือ skip
- coverage threshold ถูกลด
- assertion ถูก rewrite ให้ตรงกับ behavior ใหม่
- helper ถูก copy ทั้งที่มีของเดิม
- user-controlled text ไหลเข้า LLM call แล้วกลายเป็น prompt injection surface
- lint/build gate ถูกลดความเข้มเพื่อให้ผ่าน

นี่คือ [[shift-left-testing|shift-left testing]] ในยุค agent: ของ deterministic และถูกควรล้มงานตั้งแต่ต้น. ของ inferential ใช้เสริมตรงที่ต้องตีความ.

**ได้อะไร:** ลดงาน review ที่ควรให้เครื่องจับอยู่แล้ว และกัน failure mode ที่ agent "ทำให้เขียว" โดยทำให้มาตรฐานต่ำลง.

## Human on the loop

ในระบบ agentic review คนไม่จำเป็นต้องอ่านทุกบรรทัดเสมอไป โดยเฉพาะในงาน low-risk. แต่คนยังต้องอยู่ **บนลูป** (human on the loop): sampling, spot-checking, audit, escalation, และตัดสินใจ merge ใน path สำคัญ.

งานที่ยังไม่ควรยกให้ model ทั้งหมด:

- ตัดสินว่า change นี้ควรทำตั้งแต่แรกไหม
- ตัดสิน trade-off ที่กระทบ product / user / org
- high-blast-radius gate
- requirement ที่ไม่มีใครเขียนไว้
- ownership หลัง merge

ตรงนี้คือขอบเขตของ [[loop-engineering|loop engineering]]. ลูปช่วยผลิตและตรวจได้มากขึ้น แต่ถ้าปิดลูปด้วย model ทั้งหมด เราอาจได้ [[cognitive-surrender|borrowed confidence]]: ระบบมั่นใจแทนเรา ทั้งที่ไม่มีคนเข้าใจจริง.

## วิธีจำสั้น ๆ

Agentic code review = **risk tier + evidence intake + deterministic gates + heterogeneous AI sensors + human ownership**.

ถ้าขาด risk tier จะ review หนักเกินในงานเล็กและเบาเกินในงานใหญ่. ถ้าขาด evidence intake reviewer ต้องกู้ intent เอง. ถ้าขาด deterministic gate agent จะ optimize เขียวแทน optimize ถูก. ถ้าขาด AI sensor คนจะจมใน volume. ถ้าขาด human ownership ไม่มีใครรับผิดชอบตอน production พัง.

## Review chain ใน playbook ของ Anthropic

ก่อนถึงกรณีของ DHH, playbook ที่ [[claude-codes-new-intent-md-rob-shocks|Rob Shocks สรุป]] เพิ่มโครงรอบ PR ไว้อีกชั้น Agent ฝั่ง implement เปิด PR พร้อม diff, test และ [[artifact-chain|artifact ก่อนหน้า]] จากนั้น reviewer อีก instance ตรวจเทียบ policy กับ security rule แล้วส่ง comment กลับไปให้ agent แก้

จุดที่ยังไม่ควรย่อรวมคือ AI review, deterministic CI และ human approval ทำหน้าที่คนละอย่าง Reviewer ช่วยหา concern, CI บังคับสิ่งที่เขียนเป็นกฎได้ ส่วนคนรับผิดชอบ gate ที่กระทบ production Hooks ควรปิดเส้นทาง deploy จนกว่าจะมี permission ที่กำหนดไว้

**ผลคือ:** ความเร็วไม่ได้มาจากตัด review ออก แต่มาจากให้ agent เตรียม evidence และแก้ feedback ก่อนถึง human gate

## Thoughtworks: REVIEW agent วนเอง คนอยู่ที่ด่าน scope

[[engineering-the-harness-thoughtworks|บทความของ Thoughtworks]] วาง automated review agent เป็นช่วงสุดท้ายของ pipeline หกช่วง (ANALYZE, BLUEPRINT, RED, GREEN, REFACTOR, REVIEW) หน้าที่ของมันคือเช็คว่า test ครอบ acceptance criteria ครบไหม ถ้าเจอข้อที่ยังไม่มี test มันไม่ดึงคนเข้ามา แต่ส่งงานกลับไป RED/GREEN ให้เขียน test กับโค้ดที่ขาด แล้วรัน REVIEW ใหม่เองก่อนเปิด pull request

คนถูกเรียกเร็วกว่านั้น คือตอน BLUEPRINT ที่ architecture agent เจอผลกระทบข้ามหลาย service ([[blast-radius-gates]]) บทความแยกไว้ชัดว่า human feedback loop มีไว้กับเรื่องที่ย้อนไม่ได้ ส่วน automated loop มีไว้กับ failure ที่แก้ด้วยกลไกได้

สิ่งที่บทความไม่ได้บอก: หลังเปิด PR แล้วมีคน review อีกชั้นไหม และ REVIEW agent เชื่อได้แค่ไหนเมื่อ test ที่มันตรวจก็มาจาก AI เหมือนกัน ประเด็นหลังนี้ต่อกับคำเตือนของ Böckeler ใน [[harness-guides-sensors]] เรื่อง behaviour harness

**ได้อะไร:** อีกทางหนึ่งในการ tier ตามความเสี่ยง คือย้ายด่านคนไปไว้ก่อนลงมือในเรื่องใหญ่ แล้วให้ review ตอนท้ายเป็นงานของเครื่อง

## DHH: ตรวจสิ่งที่ควรเปลี่ยนแต่นอก diff ด้วย

[[dhh|DHH]] ผู้สร้าง Ruby on Rails เล่าใน [[dhh-ai-programming-setup-lex-clips|บทสัมภาษณ์เรื่องชุดเครื่องมือ AI]] ว่าใช้ Neovim เป็นตัวเปิดดูโปรเจกต์ แม้เขียน code เองน้อยลง เขาชอบการแสดง diff ของ Hunk แต่ระหว่างตรวจงาน agent อยากเปิดไฟล์ที่ไม่ได้เปลี่ยนด้วย เพื่อถามว่ามีส่วนไหนควรแก้ตามแล้ว agent ลืมหรือไม่

ตัวอย่างนี้เสริมการแบ่งระดับ review ตามความเสี่ยง: เมื่อความถูกต้องของงานขึ้นกับไฟล์อื่น ผู้ตรวจต้องตามออกไปดูบริบทนั้นได้ การเห็นเฉพาะบรรทัดที่เปลี่ยนอาจทำให้ไม่เห็นงานที่ขาด ข้อสรุปนี้เป็นการเชื่อมแนวคิดของ wiki ไม่ใช่ผลทดสอบว่า Hunk ตรวจ bug ได้น้อยกว่าเครื่องมืออื่น

ผลคือ เครื่องมือ review ควรเปิดทางจาก diff ไปยัง code ที่เกี่ยวข้อง และคนยังต้องตัดสินว่าขอบเขตที่ agent แก้ครบตามโจทย์หรือยัง

## Dillon: local review ก่อนให้ PR ถึงทีม

[[dillon-mulroy|Dillon Mulroy]] ใช้ [[plannotator|Plannotator]] เปิด AI-generated diff ใน local web app แล้ว comment ทีละไฟล์ก่อน push Agent รับ comment กลับเข้า session และแก้ต่อได้ใน loop เดิม เขายังพยายามจำกัด PR ไว้ราว 300 ถึง 800 บรรทัดเพื่อให้อ่านครบและเข้าใจเป็น atomic unit

วิธีนี้เพิ่ม gate ก่อน team review ไม่ได้แทน CI หรือ reviewer คนอื่น จุดแข็งคือ feedback เกิดตอน context ของ implementer ยังอุ่น และงานที่เจ้าของยังไม่อ่านไม่ถูกโยนไปเป็นภาระของทีม ข้อจำกัดคือคำว่า "อ่านทุกบรรทัด" ไม่ได้พิสูจน์ว่าจับ architecture mismatch หรือ missing requirement ครบ

**ผลคือ:** local review ลด review debt ที่ผลักไปให้คนอื่น แต่ยังต้องใช้ risk tier, deterministic evidence และ human ownership ตามเดิม

## `REVIEW.md` เขียนนโยบาย review เป็นไฟล์

[[ai-native-sdlc-playbook|Playbook ของ Anthropic]] ไม่ได้ให้ agent review ตาม prompt ที่เขียนใหม่แต่ละครั้ง แต่วางนโยบายไว้ใน `REVIEW.md` ที่เก็บ version เหมือน code ไฟล์นี้มีสี่ส่วน

- **Passes:** แบ่งรอบตรวจเป็น bugs, security, compliance (ตรงกับ `spec.md` และ `plan.md` ไหม)
- **Important vs. nit:** นิยามชัดว่าอะไรคือของจริง (พฤติกรรมพัง ข้อมูลรั่ว ผิด policy) อะไรคือเรื่องรูปแบบ
- **Caps:** รายงาน nit ได้ไม่เกิน 5 ข้อต่อรอบ ที่เหลือสรุปเป็นจำนวน
- **Exclusions:** ตัด generated file และทุกอย่างที่ CI ตรวจอยู่แล้วออก

สามข้อหลังช่วยกันไม่ให้ comment เล็ก ๆ ท่วม review จนคนเลื่อนผ่าน finding ที่กระทบพฤติกรรมหรือความปลอดภัย

เมื่อต้องการให้แก้ตาม comment engineer จะ tag `@claude` ที่ comment นั้น แล้ว agent แก้และ push ให้ ถ้า finding เดิมโผล่เป็นรอบที่สอง ให้เขียนกฎกลับลง [[claude-md|`CLAUDE.md`]] เพื่อป้องกันก่อนถึงรอบ review ครั้งถัดไป

ยังต้องแยกหน้าที่เหมือนเดิม agent ที่เขียน code อนุมัติ code ตัวเองไม่ได้ กฎนี้บังคับที่ branch protection ไม่ใช่ instruction ดู [[policy-as-code-for-agents]]

**ผลคือ:** คนได้ใช้ความสนใจไปกับเรื่องที่ตัดสินใจยาก ส่วนเรื่องที่ตรวจซ้ำได้ก็ผลักไปให้เครื่องทำแทน

## See also

- [[agentic-code-review]]
- [[addy-osmani]]
- [[orchestration-tax]]
- [[loop-engineering]]
- [[harness-guides-sensors]]
- [[cognitive-surrender]]
- [[shift-left-testing]]
- [[facts-first]]
- [[intent-gap]]
- [[behavioral-verifier]]
- [[developer-balance]]
- [[deep-agent-audit]]
- [[aom-fable-elysia-2-audit]]
- [[adversarial-review-loops]]
- [[bun-in-rust]]
- [[dhh-ai-programming-setup-lex-clips]]
- [[dhh]]
- [[claude-codes-new-intent-md-rob-shocks]]
- [[artifact-chain]]
- [[plannotator]]
- [[dillon-mulroy-ships-production-code-he-didnt-write]]
- [[dillon-mulroy]]
- [[stacked-pull-requests]]
- [[ai-native-sdlc-playbook]]
- [[engineering-the-harness-thoughtworks]]
- [[blast-radius-gates]]
