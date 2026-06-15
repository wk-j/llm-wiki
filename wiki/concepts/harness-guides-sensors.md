---
title: Harness Guides & Sensors
type: concept
tags: [ai, agents, harness, software-engineering, feedback-loop, cybernetics]
created: 2026-06-08
updated: 2026-06-11
sources: [harness-engineering-bockeler.md, How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md]
---

# Harness Guides & Sensors / บังเหียนที่ทำจาก "ตัวนำทาง" กับ "ตัวเซ็นเซอร์"

หน้านี้เป็นกรอบคิด (mental model) จาก [[birgitta-bockeler|Birgitta Böckeler]] (engineer ที่ [[thoughtworks|Thoughtworks]] เขียนบน martinfowler.com) สำหรับคนที่ **ใช้** coding agent — ไม่ใช่คนสร้างตัว agent. ไอเดียหลักคือ: harness ที่ดีไม่ใช่กองของ skill กับ MCP ที่ตั้งมั่ว ๆ แต่เป็น **ระบบควบคุม** ที่ทำจากสองอย่าง — ตัวนำทางก่อนทำงาน (guides) กับตัวเซ็นเซอร์ที่คอยจับงานหลังทำ (sensors) — แล้วคนคอยปรับระบบนี้ไปเรื่อย ๆ ดูภาพรวมของคำว่า harness ที่ [[coding-harness]]

## harness ของผู้ใช้ vs ของผู้สร้าง (bounded contexts)

คำว่า "harness" แปลว่าทุกอย่างใน agent ที่ไม่ใช่ตัว model (สูตร **Agent = Model + Harness**) ซึ่งกว้างมาก Böckeler เลยขอจำกัดความให้แคบลงสำหรับคนใช้ coding agent โดยวาดเป็นวงกลมซ้อนกันสามชั้น:

- **ชั้นใน — model** ตัวที่ถูกครอบ (เช่น Opus, GPT)
- **ชั้นกลาง — builder harness** ส่วนที่เจ้าของเครื่องมือสร้างมาให้แล้ว เช่น system prompt, กลไกดึงโค้ด, orchestration ภายใน
- **ชั้นนอก — user harness** ส่วนที่ "เรา" ในฐานะผู้ใช้สร้างเองให้เข้ากับ use case และระบบของเรา

ประเด็นคือ coding agent เปิดช่องให้ผู้ใช้สร้าง **outer harness** ของตัวเองได้เยอะ และหน้านี้พูดถึงชั้นนอกนี้เป็นหลัก

เป้าหมายของ outer harness ที่ดีมีสองข้อ: (1) เพิ่มโอกาสที่ agent จะทำถูกตั้งแต่รอบแรก และ (2) มี feedback loop ที่ดักแก้ปัญหาให้ได้มากที่สุดก่อนงานจะไปถึงตามนุษย์ ผลคือ **ลดงาน review** + **คุณภาพระบบดีขึ้น** + เปลือง token น้อยลง

## สองทิศ: guides (feedforward) กับ sensors (feedback)

นี่คือแกนหลักของทั้งกรอบคิด harness ทำงานสองทิศ:

- **Guides = feedforward (ตัวนำทาง)** — สิ่งที่ป้อนให้ agent *ก่อน* และ *ระหว่าง* ทำงาน เพื่อให้มันทำถูกตั้งแต่แรก เช่น `AGENTS.md`, skill, ref docs, how-to, LSP/language server, CLI, script, codemod
- **Sensors = feedback (ตัวเซ็นเซอร์)** — สิ่งที่ *จับ* งานหลัง agent ทำเสร็จ แล้วบอกว่าผ่านหรือไม่ผ่าน เช่น test, linter, type checker, structural test, review agent, log, browser

จุดสำคัญที่ Böckeler เน้น: sensor ไม่ได้ป้อนกลับให้แค่มนุษย์ แต่ป้อนกลับเข้า **self-correcting loop ของ agent เอง** ด้วย — agent เห็น lint error ก็แก้เองก่อนจะถึงคน นี่คือหัวใจของการลด review toil

[[zack-proser|Zack Proser]] ให้ตัวอย่างใช้งานจริงใน [[how-to-keep-shipping-away-from-desk|How to Keep Shipping When You Walk Away from Your Desk]]: gate ชั้นแรกคือ lint/build/unit test ผ่าน hook, ชั้นสองคือให้ agent คลิก browser flow จริง, ชั้นสามคือ critic agent ตรวจตาม constitution. ลำดับนี้ไล่จาก computational sensor ที่เร็ว ไปหา sensor ที่ต้องตีความมากขึ้น.

## computational vs inferential

แต่ละ guide/sensor ยังแบ่งตาม *วิธีรัน* ได้สองแบบ:

- **Computational** — รันด้วย CPU, เป็น deterministic (ผลเดิมเสมอ), เร็วระดับมิลลิวินาทีถึงวินาที, เชื่อถือได้ เช่น test, linter, type checker, structural analysis
- **Inferential** — รันด้วย model (GPU/NPU), เป็นการตัดสินเชิงความหมาย (semantic), ช้ากว่า แพงกว่า และ non-deterministic เช่น AI code review, "LLM as judge"

หลักใช้งาน: computational ถูกและเร็วพอจะรันได้**ทุกการเปลี่ยนแปลง** ส่วน inferential แพงและไม่แน่นอน เลยใช้ตรงที่ต้องการ **วิจารณญาณเชิงความหมาย** จริง ๆ และไม่ต้องรันทุก commit ถึง inferential จะไม่ deterministic แต่ถ้าจับคู่กับ model ที่เหมาะกับงาน ก็เพิ่มความเชื่อมั่นได้จริง

ตัวอย่างการจัดหมวด (จากบทความ):

| สิ่งที่ทำ | ทิศ | ชนิด | ตัวอย่าง |
|---|---|---|---|
| coding convention | feedforward | inferential | `AGENTS.md`, Skills |
| วิธี bootstrap โปรเจกต์ใหม่ | feedforward | ทั้งคู่ | skill ที่มีทั้งคำอธิบาย + script |
| code mod | feedforward | computational | tool ที่เรียก OpenRewrite recipe |
| structural test | feedback | computational | hook รัน ArchUnit เช็คขอบเขต module |
| วิธี review | feedback | inferential | Skills |

## the steering loop (คนคือคนปรับบังเหียน)

งานของมนุษย์ในกรอบนี้คือ **steer** — คอยปรับ harness ทีละรอบ หลักง่าย ๆ: **พอปัญหาเดิมเกิดซ้ำหลายครั้ง ให้ปรับ guide/feedback ให้ปัญหานั้นเกิดยากขึ้นหรือไม่เกิดอีก** ตรงนี้ตรงกับ [[harness-ratchet]] (แปลง failure เป็น constraint ถาวร) เป๊ะ ๆ

และเดี๋ยวนี้ใช้ AI ช่วยปรับ harness ได้ด้วย — agent ช่วยเขียน structural test, ร่าง rule จาก pattern ที่สังเกตเห็น, สร้าง custom linter, หรือขุด codebase มาทำเป็น how-to ได้ การมี coding agent ทำให้ "สร้าง control เองแบบ custom" ถูกลงมาก

**ได้อะไร:** harness ไม่ใช่ของตั้งครั้งเดียวจบ แต่เป็นงานวิศวกรรมที่ทำต่อเนื่อง

## keep quality left (วางด่านให้ซ้ายสุดเท่าที่ทำได้)

มาจากวินัยสาย [[shift-left-testing|continuous integration / shift-left]]: เจอปัญหายิ่งเร็ว ยิ่งแก้ถูก เลยต้องกระจาย sensor ไปตาม lifecycle ตามต้นทุน/ความเร็ว/ความสำคัญ

- **ก่อน commit / ก่อน integrate** — ของที่เร็ว เช่น linter, test ชุดเร็ว, review agent แบบเบา ๆ
- **หลัง integrate (ใน pipeline)** — ของที่แพงกว่า เช่น mutation testing, review แบบมองภาพรวม — แล้วรันของเร็วซ้ำอีกที
- **drift/health sensor ที่รันตลอด นอก lifecycle** — เช่น จับ dead code, วัดคุณภาพ test coverage, สแกน dependency, ให้ agent คอยดู SLO ที่ค่อย ๆ แย่ลงแล้วเสนอวิธีแก้, หรือ AI judge สุ่มเช็คคุณภาพ response + จับ log ที่ผิดปกติ

**ได้อะไร:** ของที่ถูกและเร็วรันก่อน, ของที่แพงค่อยรันทีหลัง — ไม่เปลือง

## regulation categories: บังเหียนกำกับ "อะไร"

Böckeler มองว่า harness ทำตัวเหมือน **cybernetic governor** (ตัวกำกับสายไซเบอร์เนติกส์ — เอา feedforward + feedback มาคุมระบบให้เข้าสู่สภาพที่ต้องการ) แล้วชี้ว่าควรแยกว่าเรากำลังกำกับ *มิติไหน* เพราะแต่ละมิติ "harness ได้ง่าย-ยาก" ต่างกัน มีสามหมวด:

### 1. Maintainability harness — กำกับคุณภาพโค้ดภายใน
ง่ายสุดตอนนี้ เพราะมี tooling เดิมเยอะ computational sensor จับของเชิงโครงสร้างได้แน่นอน เช่น โค้ดซ้ำ, cyclomatic complexity, coverage ที่ขาด, architecture drift, style ผิด ส่วน LLM จับของที่ต้องตีความได้บ้าง (โค้ดซ้ำเชิงความหมาย, test ซ้ำซ้อน, fix แบบ brute-force, over-engineer) แต่แพงและไม่แน่นอน — ไม่รันทุก commit. **แต่** ของที่กระทบหนักที่สุดกลับจับไม่ค่อยได้ทั้งคู่: วินิจฉัยปัญหาผิด, ทำ feature เกินจำเป็น, เข้าใจคำสั่งผิด — โดยเฉพาะถ้าคนไม่ได้บอกแต่แรกว่าต้องการอะไร "ความถูกต้อง" ก็อยู่นอกขอบเขตที่ sensor ใด ๆ จะจับได้

### 2. Architecture fitness harness — กำกับคุณลักษณะเชิงสถาปัตยกรรม
คือ [[fitness-function|fitness function]] นั่นเอง เช่น skill ที่ป้อน performance requirement + performance test ที่ feedback กลับว่า agent ทำดีขึ้นหรือแย่ลง; หรือ skill ที่กำหนด logging standard + คำสั่งให้ agent สะท้อนว่า log ที่มีพอ debug ไหม

### 3. Behaviour harness — กำกับว่าแอปทำงาน "ถูกตามที่ต้องการ" ไหม
อันนี้คือช้างในห้องที่ยังไม่มีคำตอบดี ตอนนี้คนที่ปล่อยให้ agent autonomy สูงมักทำแบบนี้: feedforward = เขียน functional spec (สั้นบ้างยาวบ้าง); feedback = เช็คว่า test ที่ AI สร้างเขียวไหม + coverage พอไหม + บางคนใช้ mutation testing + ผสมกับ manual test แต่วิธีนี้ฝากความหวังไว้กับ **test ที่ AI สร้างเอง** มากเกินไป ซึ่งยังไม่ดีพอ บางทีมได้ผลดีกับ pattern **approved fixtures** แต่ใช้ได้เฉพาะบางงาน ไม่ใช่คำตอบเหมารวม — สรุปคือ harness สำหรับ "พฤติกรรมเชิงฟังก์ชัน" ยังต้องหาทางกันอีกเยอะ

## harnessability: บาง codebase ครอบง่ายกว่า

ไม่ใช่ทุก codebase จะ harness ได้เท่ากัน ภาษาที่ strongly typed ได้ type checker เป็น sensor ฟรี; ขอบเขต module ที่ชัดทำให้ตั้ง rule คุมสถาปัตยกรรมได้; framework อย่าง Spring ซ่อนรายละเอียดที่ agent ไม่ต้องสนใจ ก็เพิ่มโอกาสสำเร็จให้ agent โดยปริยาย ถ้าไม่มีคุณสมบัติพวกนี้ ก็สร้าง control พวกนั้นไม่ได้

ต่างกันชัดระหว่าง greenfield กับ legacy: ทีม greenfield ฝัง harnessability ได้ตั้งแต่วันแรก (เลือก tech/architecture ให้กำกับง่าย) ส่วน legacy ที่หนี้เทคนิคเยอะเจอปัญหาหนักกว่า — **harness จำเป็นที่สุดตรงที่มันสร้างยากที่สุด**

## harness templates (อนาคต)

องค์กรใหญ่ ๆ มักมี service topology ไม่กี่แบบที่ครอบ 80% ของงาน (เช่น business service ที่เปิด API, event processor, data dashboard) และหลายที่ทำเป็น service template ไว้แล้ว อนาคตพวกนี้อาจกลายเป็น **harness template** — ชุด guide + sensor สำเร็จที่ leash agent ให้อยู่ในโครงสร้าง/convention/tech stack ของ topology นั้น ทีมอาจเริ่มเลือก tech stack ส่วนหนึ่งเพราะ "มี harness ให้ใช้แล้ว" แต่ก็เจอปัญหาเดิมแบบ service template: พอ instantiate แล้วก็จะหลุด sync จาก upstream — และอาจหนักกว่าเดิมเพราะ guide/sensor แบบ inferential ทดสอบยาก

## โยงกับหน้าอื่น

- [[coding-harness]] — ภาพรวมคำว่า harness และความหมายหลายแบบ หน้านี้คือกรอบ "ผู้ใช้สร้าง outer harness เป็นระบบ control"
- [[harness-engineering]] (Panutat) — pipeline ของ review agent = ตัวอย่างหนึ่งของ inferential sensor ในกรอบนี้
- [[harness-ratchet]] — กลไกของ steering loop: แปลง failure เป็น constraint ถาวร
- [[shift-left-testing]] — รากของ "keep quality left"
- [[fitness-function]] — แกนของ architecture fitness harness
- [[verifiability]] / [[behavioral-verifier]] — ปัญหา behaviour harness คือเรื่องเดียวกัน: เราเชื่อ verifier ที่ AI สร้างได้แค่ไหน
- [[what-weve-learned-building-cloud-agents]] (Cursor) — เส้นแบ่ง deterministic (computational) vs ยกให้ agent (inferential) ขยับตลอด
- [[instruction-budget]] — guide ทุกบรรทัดมีต้นทุน ใส่เท่าที่จำเป็น
- [[facts-first]] / [[spec-driven-development]] — critique ของ Wasowski อ่านผ่านกรอบนี้ได้ตรง ๆ: prose spec คือ guide แบบ inferential (ต้องให้ model ตีความ, [[llm-nondeterminism|non-deterministic]]) ส่วน executable fact คือ sensor แบบ computational — facts-first คือการย้ายน้ำหนักจากฝั่งแรกไปฝั่งหลัง
- [[developer-balance]] — verification gate ทำให้ agent ปิด loop เองได้ คนจึงใช้ attention กับ judgement แทนการเฝ้ารายละเอียด

## ปัญหาที่ยังเปิดอยู่ (จากบทความ)

- harness โตแล้วจะรักษาความสอดคล้องยังไง ไม่ให้ guide กับ sensor ขัดกันเอง?
- เชื่อ agent ให้ trade-off เองได้แค่ไหน เมื่อ instruction กับ feedback ชี้คนละทาง?
- ถ้า sensor ไม่เคยลั่นเลย = คุณภาพดี หรือ = กลไกตรวจจับไม่พอ? เราต้องการอะไรสักอย่างแบบ code coverage / mutation testing แต่สำหรับวัด "ความครอบคลุมของ harness"
- guide/sensor ตอนนี้กระจายอยู่ทั่ว delivery มีช่องว่างให้ tooling ที่ช่วย config + sync + reason ทั้งระบบ

## See also

- [[birgitta-bockeler]]
- [[harness-engineering-bockeler]]
- [[thoughtworks]]
- [[coding-harness]]
- [[harness-engineering]]
- [[how-to-keep-shipping-away-from-desk]]
- [[developer-balance]]
- [[harness-ratchet]]
- [[shift-left-testing]]
- [[fitness-function]]
- [[verifiability]]
- [[what-weve-learned-building-cloud-agents]]
- [[instruction-budget]]
