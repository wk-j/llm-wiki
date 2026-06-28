---
title: Agentic Code Review
type: source
tags: [ai, agents, code-review, software-engineering, verification]
created: 2026-06-16
updated: 2026-06-16
sources: [Agentic Code Review.md]
---

# Agentic Code Review / การ review โค้ดในยุค agent

หน้านี้สรุปโพสต์ [[addy-osmani|Addy Osmani]] (วิศวกร Google ที่เขียนเรื่อง agent architecture) เรื่อง **Agentic Code Review** เผยแพร่ 2026-06-16. แก่นของบทความคือ coding agent ทำให้การเขียนโค้ดถูกและเร็วขึ้นมาก แต่การเข้าใจและรับผิดชอบโค้ดยังแพงเท่าเดิม. งานสำคัญเลยย้ายจาก "เขียนได้ไหม" ไปเป็น "เชื่อได้ไหม".

> "the hard part of engineering moved from writing code to deciding whether to trust it"

ภาษาไทยสั้น ๆ: จุดยากของ software engineering ย้ายจากการผลิตโค้ด ไปอยู่ที่การตัดสินว่าเรากล้าเชื่อโค้ดนั้นหรือเปล่า.

## ข้อมูลปี 2026 บอกอะไร

Addy รวบรวมตัวเลขหลายชุดเพื่อชี้ว่า AI เพิ่ม output จริง แต่ทำให้ review หนักขึ้นด้วย. ตัวเลขพวกนี้ไม่ควรอ่านแบบ panic แต่ควรอ่านแบบ capacity planning: ถ้า output โตเร็วกว่า review capacity ระบบจะลดมาตรฐานเองเงียบ ๆ.

- [[faros-ai|Faros AI]] วัด 22,000 developers / 4,000 teams พบว่า adoption สูงขึ้นแล้ว throughput เพิ่ม แต่ code churn เพิ่ม 861%, incident-to-PR ratio เพิ่ม 242.7%, defect rate ต่อ developer เพิ่มจาก 9% เป็น 54%, median review duration เพิ่ม 441.5%, และ PR ที่ merge โดยไม่มี review เพิ่ม 31.3%
- [[coderabbit|CodeRabbit]] ศึกษา open-source PR 470 รายการ พบว่า AI-coauthored PR มี issue ราว 1.7 เท่าของ human-only PR. ปัญหาที่เพิ่มคือ logic/correctness, security, และ readability
- [[gitclear|GitClear]] พบว่า daily AI users ผลิต raw output ประมาณ 4 เท่าของ non-users แต่ productivity gain เทียบกับตัวเองปีก่อนอยู่ราว 12%. ช่องว่างระหว่าง 4x code กับ 12% delivered value คือภาระ review
- [[github|GitHub]] รายงานว่า Copilot review ทำ review ไปแล้วมากกว่า 60 ล้านครั้ง และมากกว่า 1 ใน 5 review บน platform เกี่ยวข้องกับ agent

Addy เตือน caveat สำคัญ: Faros กับ CodeRabbit ขายของในตลาดนี้ จึงมี incentive ทางการตลาด. แต่ effect size ใหญ่ และ pattern ไปทิศเดียวกันจากหลายแหล่ง เลยไม่ควรทิ้งตัวเลขทั้งหมด.

**ผลคือ:** เราเอา output ระดับ machine-speed ไปเทใส่ระบบที่ยังต้องตัดสินใจด้วย human-speed. คอขวดไม่ได้หายไป มันย้ายไปอยู่ที่ verification และ code review.

## ทุกคนไม่ได้แก้โจทย์เดียวกัน

Addy แบ่งวิธีคิด code review ตาม **blast radius** (ความเสียหายถ้าพัง), อายุของโค้ด, และจำนวนคนที่ต้องเข้าใจโค้ดนั้น. ประเด็นนี้สำคัญเพราะคำแนะนำส่วนใหญ่ในวง AI coding มักมาจากคนที่อยู่คนละบริบท.

- Solo / greenfield / ไม่มีผู้ใช้: ใช้ test และ automation หนัก ๆ, review เฉพาะส่วนที่เสี่ยง, ยอมเลื่อนบางงานได้. แต่ต้องมี safety net จริง. ไม่มีผู้ใช้แปลว่าเลื่อน review ได้ ไม่ได้แปลว่าข้าม verification ได้
- โปรเจกต์เริ่มมีผู้ใช้: เป็นช่วงอันตราย เพราะ habit แบบ solo ยังติดอยู่ แต่ bug เริ่มกระทบคนจริง และ knowledge-sharing เริ่มสำคัญ
- ระบบใหญ่ / legacy / ผู้ใช้เยอะ: ตัวเลข Faros ลงเต็มแรง. Review ต้องจับ bug, กระจายความเข้าใจ, และกัน [[comprehension-debt|comprehension debt]] พร้อมกัน

**ได้อะไร:** ระดับ review ต้องตั้งตาม cost of being wrong ไม่ใช่ตามความรู้สึกผิดหรือความเชื่อว่า AI ดี/แย่แบบเหมารวม.

## Review เปลี่ยนหน้าที่อย่างไร

สมัยมนุษย์เขียนโค้ด intent อยู่ในหัวคนเขียน. Reviewer ไม่ได้อ่านแค่ diff แต่ตรวจเหตุผลของ author ไปด้วย. พอ agent เขียนโค้ด เหตุผลนั้นมักถูกทิ้งหลังได้ diff. Reviewer เลยต้องย้อนสร้าง intent เองจากโค้ดที่ไม่มีใคร human อ่านมาก่อน.

Addy ยก paper **AI Slop and the Software Commons** ที่พบประโยคแรงจาก developer คนหนึ่งว่า reviewer เป็น "the first human being to ever lay eyes on this code". ปัญหานี้ไม่ใช่แค่ว่า AI เขียนผิด แต่คือ review pipeline ไม่ได้ถูกออกแบบมาให้กู้ intent ที่หายไป.

วิธีแก้ที่ Addy เสนอคือให้ agent แนบ decision log มากับ PR: ทำอะไร, ทำไม, ตัดทางเลือกอะไรทิ้ง, มี evidence อะไร. ตรงนี้โยงกับ [[intent-gap|intent gap]] และ [[facts-first|facts-first]]: prose ที่ไม่ตรวจไม่ได้ไม่พอ ต้องมี evidence ที่รันได้ด้วย.

**ผลคือ:** review ไม่ควรเริ่มจาก "อ่าน diff เปล่า ๆ" แต่ควรเริ่มจาก intent + evidence + risk class.

## AI reviewer ดีขึ้น แต่ต้องใช้แบบ sensor

Addy มองว่า AI review tools ดีพอจะใช้จริง แต่คุณค่าของมันไม่ได้อยู่ที่การแทนมนุษย์แบบสมบูรณ์. คุณค่าคือมันเป็น **inferential sensor** ที่ไม่เหนื่อย และ tool ต่างชนิดจับ bug ต่างชนิด.

ตัวอย่างในบทความ:

- [[coderabbit|CodeRabbit]] ทำได้ดีใน benchmark ของ Martian และมี workflow one-click fix
- [[greptile|Greptile]] เน้น recall / correctness / architecture แต่ trade-off กับ false positive ตาม benchmark บางชุด
- Anthropic Code Review รายงานว่า finding ที่ engineer mark ว่าผิดต่ำกว่า 1% และทำให้ PR ที่ได้ substantive review เพิ่มจาก 16% เป็น 54%
- การทดลองรัน CodeRabbit, Sentry Seer, Greptile, และ Cursor BugBot พร้อมกันบน 146 PR พบว่า flagged location 93.4% ถูกจับโดย tool เดียวเท่านั้น. แทบไม่มี overlap

บทเรียนคืออย่าหา "reviewer ที่ดีที่สุด" ตัวเดียว. สำหรับงานเสี่ยง ให้ใช้ reviewer สองตัวที่มี character ต่างกัน. ความต่างของ prior สำคัญกว่าเพิ่มสำเนาของ model เดิม.

**ได้อะไร:** AI reviewer คือ data point ไม่ใช่ verdict. มันช่วยจัด attention ของมนุษย์ ไม่ได้ย้าย accountability ออกจากมนุษย์.

## Human in the loop กลายเป็น human on the loop

Addy บอกตรง ๆ ว่าความคิด "มนุษย์อ่านทุกบรรทัด" กำลังจบในหลายบริบท. แต่คำตอบก็ไม่ใช่ปล่อย loop ตรวจตัวเองแล้วเดินหนี. ถ้า agent เขียน, agent อีกตัว review, agent ที่สาม judge โดยไม่มีมนุษย์เลย ระบบอาจมั่นใจพร้อมกันใน blind spot เดียวกัน.

รูปแบบที่เขาใช้เองคือให้ Claude Code หรือ Codex triage PR เป็น batch: อะไรดูปลอดภัย, อะไรต้องแก้, อะไรเสี่ยงสูง. เขาไม่ auto-merge ตามผลนั้น. AI ช่วยเรียงคิว attention ส่วน merge decision ยังเป็นของมนุษย์.

ตัวอย่างสุดขั้วคือ [[kun-chen|Kun Chen]] อดีต Meta L8 ที่ ship ประมาณ 40 PR/day ด้วย agent 20-30 ตัว และแทบไม่ review line-by-line แล้ว. แต่เขาย้ายงานมนุษย์ไปอยู่ก่อนโค้ดเกิด: เขียน plan ละเอียด, ให้ agent รันนาน, มี automated gate ชื่อ No Mistakes, และตัวเขายังรับ escalation. Addy เตือนว่านี่ rational ในบริบท solo builder แต่ copy ไปใส่ทีมใหญ่โดยตรงจะทำให้ dashboard กลายเป็น Faros numbers.

**ผลคือ:** มนุษย์ไม่ได้หายไปจาก loop แต่งานมนุษย์ย้ายขึ้นไปอยู่ระดับ sampling, spot-checking, auditing, risk gate, และ ownership.

## วิธีทำจริง

Addy เสนอ playbook ที่ค่อนข้าง pragmatic:

- **Tier by risk, not by author** — จัด review ตามความเสี่ยงของ diff ไม่ใช่เพราะเขียนโดยคนหรือ agent. Config เล็ก ๆ ได้ lint + glance. Core business logic ได้ types, tests, AI reviewers สองตัว, owner review, security pass
- **Fast-fail the expensive tail** — ใช้ cheap signals เช่น patch size / file type ทำนาย PR ที่จะกินแรง review สูง แล้วตัดสินใจตั้งแต่ก่อนคนลงเวลา
- **Raise the bar for review intake** — ไม่รับ review ถ้าไม่มี purpose, diff เล็กพอ, test output, และ proof ว่ารันแล้ว
- **Keep PRs small** — agent PR มักใหญ่ขึ้น. PR ที่คนอ่านได้เป็น design constraint แล้ว ไม่ใช่มารยาท
- **Read test changes first** — failure mode สำคัญคือ agent เปลี่ยน behavior แล้วแก้ assertion ให้ตรงกับ behavior ผิด. Test diff ใหญ่คือ flag
- **CI is the wall that does not move** — อย่าให้ agent ลด threshold, skip lint, remove test, หรือหลบ gate เพื่อให้เขียว
- **A human owns the merge** — model โดน page ไม่ได้. คนกด merge คือคนรับผิดชอบ

ตรงนี้เชื่อมกับ [[harness-guides-sensors|harness guides & sensors]] ชัดมาก: deterministic gate อยู่ซ้ายสุด, AI reviewer เป็น inferential sensor, และ human judgement อยู่ตรงที่ sensor ยังแทนไม่ได้.

## ความหมายสำหรับทีม

ถ้าทีมคิดว่า AI ทำให้ generation ถูกลงแล้วลดคน review ได้ทันที จะเปลี่ยน saving วันนี้เป็น incident วันหน้า. คอขวดใหม่คือ trusted human confidence: เร็วแค่ไหนที่คนที่รับผิดชอบระบบจะมั่นใจได้ว่าการเปลี่ยนแปลงนี้ถูกและควร merge.

Open source maintainer เจอกำแพงนี้ก่อน เพราะ contribution ที่ดู plausibly useful แต่กลวง กิน triage time จริง. บริษัทจะเจอถัดมา. ทีมที่ทำได้ดีจะไม่วัดแค่ merged PR แต่จะวัด review capacity และใช้มันเหมือน resource จำกัด.

## แก่นสุดท้าย

บทความนี้เติมอีกครึ่งให้ [[orchestration-tax|orchestration tax]]: ไม่ใช่แค่ว่าเปิด agent เยอะแล้วเราตรวจไม่ทัน แต่การตรวจเองต้องถูกออกแบบใหม่เป็นระบบ risk-tiered + evidence-required + heterogeneous sensors.

Writing got cheap. Understanding did not. งาน durable ของ engineer เลยไม่ใช่ผลิตโค้ดให้เยอะที่สุด แต่สร้างระบบ review ที่น่าเชื่อ และยังรู้พอจะยืนข้างหลังโค้ดที่ merge.

## See also

- [[agentic-code-review]]
- [[addy-osmani]]
- [[orchestration-tax]]
- [[loop-engineering]]
- [[harness-guides-sensors]]
- [[cognitive-surrender]]
- [[comprehension-debt]]
- [[intent-gap]]
- [[facts-first]]
- [[shift-left-testing]]
- [[coderabbit]]
- [[greptile]]
- [[faros-ai]]
- [[gitclear]]
- [[kun-chen]]
