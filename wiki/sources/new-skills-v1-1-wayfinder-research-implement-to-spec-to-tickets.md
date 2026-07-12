---
title: "New Skills! v1.1 brings /wayfinder, /research, /implement, /to-spec, /to-tickets"
type: source
tags: [ai, agents, skills, workflow, planning, implementation, code-review, tdd]
url: https://www.youtube.com/watch?v=A8mokin_YOs
date_ingested: 2026-07-12
created: 2026-07-12
updated: 2026-07-12
sources: ["https://www.youtube.com/watch?v=A8mokin_YOs"]
---

# New Skills! v1.1 / Wayfinder, Research, Implement, To-Spec, To-Tickets

วิดีโอ changelog ของ [[matt-pocock|Matt Pocock]] (ผู้สอน TypeScript และคนสร้าง workflow สำหรับ coding agent) อธิบาย Skills v1.1. รอบนี้ไม่ใช่แค่เพิ่ม skill หลายตัว แต่ประกอบของเดิมให้เป็น software development lifecycle เต็มเส้น ตั้งแต่เคลียร์ decision ไปจนถึง review และ commit.

ภาพรวมคือ `grill หรือ wayfind → to-spec → to-tickets → implement → code review → commit`. งานเล็กเริ่มด้วย grilling ได้. งานใหญ่ที่ยังมี fog ใช้ [[wayfinding|Wayfinding]] แยกการค้นหาคำตอบข้ามหลาย session ก่อนค่อยกลั่นเป็น spec.

## ใจความสำคัญ

- `/to-PRD` เปลี่ยนชื่อเป็น `/to-spec` เพราะ artifact กว้างกว่า Product Requirements Document และผสม technical/non-technical requirement ได้
- `/to-issues` เปลี่ยนชื่อเป็น `/to-tickets` เพื่อตัดอคติว่าต้องใช้ GitHub หรือ Linear
- grilling ถามทีละคำถาม, ห้าม implement ก่อนผู้ใช้ยืนยัน shared understanding และแยก facts ที่ agent หาเองออกจาก decisions ที่ต้องถามคน
- `/implement` เชื่อม ticket เข้ากับ TDD, type checking, test หลายระดับ, code review และ commit
- code review ตรวจสองแกนแบบขนาน: repo standards กับ fidelity ต่อ spec พร้อมเพิ่ม refactoring smells เป็น vocabulary ให้ model จับปัญหาโครงสร้าง
- Wayfinder ใช้ issue map, sub-issues และ blocking relationship พางานที่ใหญ่เกินหนึ่ง smart zone ไปสู่ spec
- `/research` ให้ background agent อ่าน primary sources แล้วเก็บผลเป็น markdown ตาม convention ของ repo
- TDD skill เปลี่ยนเป็น reference material: เน้น red ก่อน green ทีละ slice และย้าย refactoring ออกจาก implementation loop ไปไว้ใน review

## เปลี่ยนชื่อให้ artifact ตรงกับสิ่งที่เป็น

Pocock เปลี่ยน `/to-PRD` เป็น `/to-spec` เพราะสิ่งที่ skill สร้างไม่ใช่ PRD แคบ ๆ. มันเป็น specification ของสิ่งที่จะสร้าง ซึ่งอาจเป็น technical, non-technical หรือผสมกัน. คำว่า spec จึงครอบคลุมกว่าและไม่ทำให้ requirement ที่ไม่ใช่ product ดูเหมือน “หลุด” เอกสาร.

ส่วน `/to-issues` กลายเป็น `/to-tickets`. คำว่า issue ผูกภาพกับ GitHub และ Linear มากไป ขณะที่ workflow ต้องการหน่วยงานที่อยู่ใต้ spec ไม่ว่าจะใช้ tracker เจ้าไหน. Ticket แต่ละใบคือก้าวหนึ่งของการทำให้ spec เกิดขึ้นจริง.

การ migrate ไม่ใช่ rename อัตโนมัติ. Pocock แนะนำให้รัน `npx skills add mattpocock/skills` แล้วเลือก skill ใหม่อย่างตั้งใจ พร้อมตรวจ folder เดิมว่ามี `/to-PRD` หรือ `/to-issues` ค้างอยู่ไหม.

**ได้อะไร:** ubiquitous language ของ workflow ตรงกับ artifact จริง และย้ายข้าม tracker ได้ง่ายขึ้น.

## Grilling: facts ไม่ใช่ decisions

v1.1 แก้ failure mode ของ [[grill-me|grilling]] สามเรื่อง:

1. ย้ำให้ถามทีละคำถาม พร้อมอธิบายว่าหลายคำถามพร้อมกันทำให้ผู้ใช้สับสน
2. เพิ่ม confirmation gate: ห้ามลงมือทำ plan จนผู้ใช้ยืนยันว่า shared understanding ตรงกันแล้ว
3. แยก **facts** ออกจาก **decisions** — agent หา fact จาก codebase เองได้ แต่ decision ต้องให้ผู้ใช้ที่เป็นเจ้าของเจตนาตอบ

ข้อสามแก้ปัญหา agent “grill ตัวเอง”: มันสำรวจ repo แล้วตอบแทนผู้ใช้ ทั้งที่คำถามนั้นเป็น choice ไม่ใช่ข้อเท็จจริง. Pocock ระบุว่าอาการนี้เกิดกับ Fable บ่อยเป็นพิเศษ และหลังแก้ wording มี complaint ลดลง แต่ยังเป็น field report ของผู้สร้าง skill ไม่ใช่ benchmark.

**ผลคือ:** การสัมภาษณ์ไม่จบด้วย agent เดา intent แล้วรีบ implement เอง.

## Lifecycle เต็มเส้น

ก่อน v1.1 ชุด Skills เน้น planning มากกว่า execution. รอบนี้ Pocock เติมเส้นทางให้ชัด:

1. **Grill / Grill with Docs / Wayfinder** — เคลียร์ภาษา, architecture decision และ unknowns
2. **To-Spec** — กลั่นปลายทางเป็น spec
3. **To-Tickets** — แตกเส้นทาง implementation ให้แต่ละ ticket อยู่ในหนึ่ง agent session
4. **Implement** — ทำ ticket ด้วย TDD ตาม seam ที่ตกลง, รัน type check และ test ระหว่างทาง
5. **Code Review** — ตรวจมาตรฐาน repo กับ spec fidelity
6. **Commit** — บันทึกงานบน branch ปัจจุบัน

`/implement` ตั้งใจสั้น. มันพึ่ง priors ของ model และ harness ที่มีอยู่ แล้วทำหน้าที่บอกว่าหลัง ticket ต้องเดินไปจุดไหนต่อ. ระหว่างทำให้รัน single test file และ type check บ่อย ส่วน full test suite รันครั้งเดียวท้ายงานเพื่อลด feedback cost.

**ได้อะไร:** user ไม่ต้องเดาเองว่า skill หลายตัวต่อกันเป็น flow ไหน และ ticket หนึ่งใบมี exit path ไป review/commit ชัด.

## Code review: สองแกนและ refactoring smells

`/review` ที่เคยอยู่ระหว่างพัฒนาใน [[new-skills-handoff-prototype-review-writing|changelog ก่อนหน้า]] ถูกยกเป็นส่วนจริงของ lifecycle แล้ว. มันยังคง [[dual-axis-code-review|สองแกน]]:

- **Standards axis** — code ตรงกับมาตรฐานที่ repo เขียนไว้หรือไม่
- **Spec axis** — code ทำตาม issue, PR หรือ spec ต้นทางจริงหรือไม่

Pocock แนะนำให้เก็บ coding standards แยกจาก `AGENTS.md` แล้วอ่านในจังหวะ review. สองแกนรันเป็น subagent ขนานก่อนรวมผล.

ของใหม่คือเติมชื่อ code smells จากหนังสือ *Refactoring* ของ Martin Fowler เช่น mysterious name, duplicated code, feature envy, data clumps, primitive obsession, repeated switches, divergent change, speculative generality และ message chains. เหตุผลคือศัพท์พวกนี้อยู่ใน priors ของ model อยู่แล้ว แค่เรียกชื่อและให้ gloss สั้น ๆ ก็ช่วยดึง lens นั้นออกมาใช้. Pocock รายงานว่าทดลองสองสัปดาห์แล้วมีประโยชน์มาก แต่ผลนี้ยังเป็นประสบการณ์ส่วนตัว.

**ผลคือ:** review ไม่ได้ถามกว้าง ๆ ว่า “โค้ดดีไหม” แต่มีทั้ง evidence จาก repo/spec และ vocabulary สำหรับจับ design smell.

## Wayfinder อยู่ก่อน spec

Wayfinder เข้ามาแทน `Grill with Docs` ในบางงาน โดยเฉพาะงานที่วางแผนไม่จบในหนึ่ง agent session หรือเสี่ยงหลุด smart zone/context window. มันเก็บ map บน issue tracker แล้วทำ decision ticket ทีละใบ. Sub-issue มี blocking relationship และแต่ละใบถูก scope ให้จบใน session เดียว.

ในวิดีโอ Pocock โชว์ map จาก Sandcastle สำหรับ spike ว่าจะรับ AI SDK เป็น dependency หรือไม่. Ticket แยกเป็น research, grilling, prototype และ task. พอปิดครบ คำตอบถูกสรุปบน map โดย ticket เดิมยังเป็น primary source แล้วจึงส่ง map เข้า `/to-spec`.

Pocock บอกว่าใช้ Wayfinder กับงาน non-coding ด้วย เช่นวางแผน course. นี่สนับสนุน claim ใน [[wayfinder-skill]] ว่า map เป็น domain-agnostic แต่ยังเป็นรายงานจากผู้ใช้/ผู้สร้างคนเดียว.

**ได้อะไร:** planning state อยู่ใน tracker ที่แชร์กับทีมได้ ไม่ต้องพึ่ง handoff และการประคอง context ด้วยคนตลอดทาง.

## Research และ prototype ช่วยลดความไม่รู้

`/research` เป็น skill เล็กสำหรับให้ background agent ตรวจคำถามกับ primary sources แล้วเขียนผลลง markdown ตาม convention ของ repo. การรันเบื้องหลังทำให้ main session เดินต่อได้ แต่ asset ที่ได้ยังต้องถูก link กลับเข้า ticket/map เพื่อใช้เป็นหลักฐาน.

`/prototype` รองรับทั้ง logic prototype และ UI prototype. ใน Wayfinder มันใช้กับคำถาม “ควรหน้าตาอย่างไร” หรือ “ควรทำงานอย่างไร” โดยทำของหยาบราคาถูกให้คน react ก่อนเขียน spec. Pocock แนะนำเป็นพิเศษกับ frontend เพราะการเห็น interaction จริงให้ข้อมูลที่ข้อความล้วนไม่มี.

**ผลคือ:** research ลด unknown ที่ต้องอ่านจากโลกภายนอก ส่วน prototype ลด unknown ที่ต้องเห็นของจริงก่อนตัดสินใจ.

## TDD: red-green ก่อน แล้ว refactor ตอน review

TDD skill เดิมมีขั้นตอนโต้ตอบมากจนไม่เหมาะกับ AFK agent. v1.1 ลดมันเป็น reference material. กฎหลักคือเขียน red ก่อน green, ทำทีละ slice และไม่บังคับ conversation flow ยาว.

Pocock แยก refactoring ออกจาก red-green loop แล้วเลื่อนไป code review. เหตุผลคือไม่อยากให้ implementation แบกทั้ง behavior และ cleanup พร้อมกัน. ตรงนี้ต่างจากสูตร Red-Green-Refactor แบบคลาสสิก จึงควรเก็บเป็น preference ของ workflow นี้ ไม่ใช่นิยาม TDD สากล.

**ได้อะไร:** implementation agent ทำงาน AFK ได้ง่ายขึ้น แต่ทีมต้องมั่นใจว่า review/refactoring stage เกิดขึ้นจริง ไม่อย่างนั้น “Refactor” จะหายไปจากวงจร.

## ข้อจำกัดและ claim ที่ยังต้องระวัง

- complaint ลดลงหลังแก้ grilling, code smells “outrageously useful”, ยอดดาวราว 160K และดาวน์โหลด 7 ล้านครั้ง เป็นตัวเลข/ประสบการณ์ที่ Pocock กล่าวในวิดีโอ ยังไม่ได้ตรวจอิสระ
- lifecycle นี้เป็น opinionated workflow. การรัน full suite แค่ท้ายงานหรือย้าย refactor ไป review อาจไม่เหมาะกับ repo ที่ feedback ช้าหรือ architecture เสี่ยงสูง
- migration แบบลบแล้วติดตั้งใหม่เสี่ยงทับ customization ของผู้ใช้ จึงควรเทียบ release notes และ diff ก่อน
- AI Coding Crash Course ยังเป็นประกาศล่วงหน้า; ในวิดีโอยังไม่กำหนดราคาและคาดว่าจะพร้อมราวเดือนสิงหาคม

## ความเชื่อมโยงกับ wiki

- เติม implementation/review ให้ [[agentic-engineering]] ซึ่งเดิมเน้น spec, verification และ coordination ระดับกว้าง
- เปลี่ยนสถานะ [[dual-axis-code-review]] จากแนวคิดที่กำลังทำ มาเป็น skill ที่อยู่ใน lifecycle v1.1
- ทำให้ [[wayfinding]] มี downstream ชัด: map → spec → tickets → implementation
- เพิ่ม confirmation gate และ facts/decisions boundary ให้ [[grill-me]]
- วาง [[throwaway-prototyping]] ก่อน spec อย่างเป็นทางการ โดยเฉพาะงาน frontend
- สร้างแรงตึงกับ [[specs-to-code]]: v1.1 ใช้ spec เป็น handoff artifact แต่ยังคง TDD, review, tests และ human decision gates ไม่ได้เสนอให้ generate แล้วเชื่อทันที

## See also

- [[matt-pocock]]
- [[wayfinder-skill]]
- [[wayfinding]]
- [[grill-me]]
- [[dual-axis-code-review]]
- [[throwaway-prototyping]]
- [[agentic-engineering]]
- [[specs-to-code]]
- [[new-skills-handoff-prototype-review-writing]]
