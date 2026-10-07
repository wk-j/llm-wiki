---
title: "Engineering the harness: A practical pattern for reliable coding agents"
type: source
tags: [ai, agents, harness, software-engineering, feedback-loop, thoughtworks, governance]
url: https://www.thoughtworks.com/insights/blog/architecture/engineering-the-harness-a-practical-pattern-for-reliable-coding-agents
author: Jaya Simha Reddy Nandyala, Prabina Pani
published: 2026-09-29
date_ingested: 2026-09-30
created: 2026-09-30
updated: 2026-10-01
sources: ["https://www.thoughtworks.com/insights/blog/architecture/engineering-the-harness-a-practical-pattern-for-reliable-coding-agents"]
---

# Engineering the Harness / ออกแบบ harness ให้ไว้ใจ coding agent ได้

บล็อกจาก [[thoughtworks|Thoughtworks]] (บริษัทที่ปรึกษาซอฟต์แวร์ที่ผลักเรื่อง CI/CD และ evolutionary architecture) เขียนโดย Jaya Simha Reddy Nandyala กับ Prabina Pani เผยแพร่ 2026-09-29 บทความใช้คำ guides กับ sensors ชุดเดียวกับกรอบ [[harness-guides-sensors|Harness Guides & Sensors]] ของ [[birgitta-bockeler|Birgitta Böckeler]] (engineer ของ Thoughtworks เหมือนกัน) แต่ไม่ได้อ้างชื่อเธอตรง ๆ สิ่งที่บทความเพิ่มคือ **ด่านให้คนตัดสินเฉพาะจุด (selective human gates)** กับตัวอย่าง pipeline หกช่วงที่เอาทั้งหมดมาต่อกัน

## ปัญหาตั้งต้น: โค้ดถูกเฉพาะจุด แต่พังทั้งระบบ

บทความเปิดด้วยอาการที่ทีมเจอบ่อย agent เขียนโค้ดสวย compile ผ่าน syntax ถูก แต่ผิดเมื่อมองทั้งระบบ เพราะมันเห็นแค่ context ตรงหน้า

ตัวอย่างคือ สั่ง agent refactor data model แล้วมัน rename field ใน service ที่กำลังแก้ โดยไม่รู้ว่ามี microservice อีกสองตัวใช้ field นั้นอยู่ ผู้เขียนสรุปว่า "The change is locally correct, but systemically destructive." (ถูกเฉพาะจุด แต่ทำลายทั้งระบบ)

ผู้เขียนมองว่าช่องว่างนี้ไม่ได้มาจาก model ไม่เก่งเป็นหลัก model ขาดสามอย่าง คือ มองไม่เห็นระดับระบบ ไม่มี guardrail เชิงสถาปัตยกรรม และไม่มี feedback อัตโนมัติ เลยใช้สูตรเดียวกับที่ wiki เจอมาหลายแหล่ง (ดู [[coding-harness]]):

> "Agent = Model + Harness"

Model ให้ความสามารถในการคิด ส่วน harness ให้สภาพแวดล้อม ขอบเขตของ tool ขอบเขตของ context และ feedback loop ที่เปลี่ยนความฉลาดของ model ให้กลายเป็นระบบส่งมอบงานที่ปลอดภัยและตรวจย้อนได้

**ได้อะไร:** ถ้า agent ทำผิดระดับระบบ อย่าเพิ่งโทษ model ให้ถามก่อนว่า harness ให้มันเห็นระบบพอหรือยัง

## สองชั้น กับด่านคนเฉพาะจุด

ส่วนนี้คือโครงของทั้ง pattern harness ระดับ production มีสองชั้นที่บังคับได้ คั่นด้วยด่านตัดสินใจ:

1. **Guides** — คุมทิศทางก่อน agent ลงมือ
2. **Sensors** — ตรวจผลหลัง agent ทำเสร็จ
3. **Selective human gates** — จุดที่ต้องให้คนตัดสิน หรือเซ็นรับความเสี่ยงของผลกระทบวงกว้าง วางไว้ระหว่าง guides กับ sensors

แยก "ก่อนลงมือ" ออกจาก "หลังลงมือ" ให้ชัด ทีมก็เลี่ยงหลุมได้สองแบบ แบบแรกคือปล่อย agent ทำเองโดยไม่มีขอบเขต แบบที่สองคือบังคับให้คนกดอนุมัติทุก tool call จนล้า

**ผลคือ:** คนไม่ต้องเฝ้าทุกก้าว แต่ยังได้ตัดสินในจุดที่พลาดแล้วแก้ยาก ดู [[blast-radius-gates]]

## Guides: คุมก่อน agent ลงมือ

Guides กำหนดกรอบว่า agent สำรวจ วางแผน และเขียนโค้ดได้แค่ไหน บทความให้สี่ pattern

### คำสั่งตามขอบเขต และ progressive disclosure

ถ้าโหลดไฟล์คำสั่งก้อนใหญ่เข้าทุก session context จะเต็มเร็ว ผู้เขียนเรียกอาการนี้ว่า "attention dilution" (attention เจือจาง) คู่กับ [[context-rot|context rot]] (อาการที่ model แย่ลงเมื่อ context ยาว)

ทางแก้คือผูกคำสั่งกับ path หรือ domain เช่น โหลดกฎ database เฉพาะตอนแตะไฟล์ schema แล้วให้ agent เดินลง documentation tree เท่าที่ต้องใช้ แทนการโหลดทุกอย่างไว้ก่อน ตรงนี้คือ [[progressive-disclosure]] ที่ใช้กับ instruction

### Tool แบบสิทธิ์น้อยที่สุด (least-privilege)

เขียนใน prompt ว่า "อย่า push code" หรือ "อย่าแก้ config" ยังเปราะเกินไป ให้เปลี่ยนคำขอเชิงพฤติกรรมเป็นข้อบังคับเชิงโครงสร้างแทน

ตัวอย่างในบทความคือ agent ที่ตอบคำถามหรือตรวจโค้ด ได้เฉพาะ tool อ่านอย่างเดียว มันไม่มีความสามารถเขียนไฟล์ตั้งแต่ต้น หลักเดียวกับ [[policy-as-code-for-agents]] ที่ให้ตัดความสามารถออก แทนการสั่งไม่ให้ทำ

### ค่า default ที่ประกาศชัด แทนการเดา

ตอนรับข้อมูลเข้าแบบมีโครงสร้าง (structured intake) ถ้าเจอ input ที่ไม่บังคับ เช่น technical spec ที่จะมีหรือไม่มีก็ได้ agent ไม่ควรสมมติเอาเอง harness บังคับให้ "ask before deciding" (ถามก่อนตัดสิน) ถ้า developer เลือกข้ามขั้นนั้น harness ก็บันทึกการตัดสินใจนั้นไว้ชัด ๆ

> "A default is visible and inspectable, a guess is hidden and risky."
> — default มองเห็นและตรวจได้ ส่วนการเดาซ่อนอยู่และเสี่ยง

### ถามยืนยันเฉพาะเรื่องที่ลามไกล

จะให้เร็วโดยไม่เสียความปลอดภัย ต้องสงวนด่านยืนยันไว้กับเรื่องที่ย้อนไม่ได้หรือกระทบวงกว้าง เช่น ขยาย scope ข้ามหลาย repository, schema migration และการแก้ public API เรื่องเสี่ยงต่ำให้เดินต่อด้วย default ที่สมเหตุสมผล

**ได้อะไร:** guides เปลี่ยนการควบคุมจาก "ขอให้ระวัง" เป็นโครงสร้างที่ agent ฝ่าไม่ได้ หรือไม่ต้องเดา

## Sensors: ตรวจหลัง agent ลงมือ

Guides ดีแค่ไหนก็จับ edge case ทาง logic หรือ runtime error ไม่หมด sensors เลยรันหลัง agent ทำ แล้วป้อนผลตรวจจากการคำนวณกลับมา

### ตรวจอัตโนมัติ

Sensors ห่อ check มาตรฐานอย่าง unit test, linter, static type checker และ architecture rule เข้าไปใน loop ของ agent พอ agent ทำ implementation เสร็จหนึ่งรอบ sensors ก็รันเอง ไม่ต้องเชื่อคำประเมินตัวเองของ agent

### ผ่านเงียบ พังละเอียด

Sensors ทำตามกฎ "silent success, verbose failure":

- **ผ่าน** — แทบไม่พูดอะไร ประหยัดทั้ง context token และ attention ของคน
- **ไม่ผ่าน** — ส่งรายละเอียดที่เอาไปแก้ได้ เช่น stack trace ตำแหน่ง lint error และ diff ของ test ที่พัง กลับเข้า loop ให้ agent แก้เองโดยไม่ต้องมีคนเข้ามา

หลักเดียวกันเคยปรากฏใน [[agent-harness-engineering]] ของ [[addy-osmani|Addy Osmani]] ดู [[silent-success-verbose-failure]]

### เลื่อนกฎจากข้อความไปเป็นตัวบังคับที่รันได้

ถ้าทีมต้องเติมกฎเป็นข้อความใน prompt file ซ้ำ ๆ เพราะ agent ไม่ทำตาม convention กฎนั้นควรถูกเลื่อนไปเป็น sensor เชิงกลไก เช่น custom lint rule, type check หรือ architecture test

> "Prose is the starting point; where a rule can be reliably encoded, mechanical enforcement is the stronger option."
> — ข้อความเป็นแค่จุดเริ่ม กฎไหนเข้ารหัสได้เชื่อถือได้ การบังคับด้วยกลไกแข็งกว่า

ตรงนี้คือ [[harness-ratchet]] แบบระบุทิศชัด: failure ที่เกิดซ้ำไม่ควรจบที่ prose

**ผลคือ:** agent แก้ตัวเองจากผลตรวจจริง คนเห็นเฉพาะปัญหาที่ loop แก้เองไม่ได้

## Pattern นี้ทำงานข้าม repo ยังไง

ผู้เขียนยกตัวอย่างสมมติสาม microservice:

- `billing-service` เป็นเจ้าของ field `discount_rate`
- `checkout-service` ใช้ `discount_rate`
- `invoicing-service` ใช้ `discount_rate`

บทความบอกเองว่าเป็นตัวอย่างแบบย่อ และใช้ได้เมื่อ dependency "known and accessible to the harness" (harness รู้และเข้าถึงได้)

### รันระดับ repo เดียว ไม่มีอะไรคุม

Agent รันใน `billing-service` แล้ว rename `discount_rate` เป็น `promotional_discount` ใน repo นั้น test ใน repo ผ่าน agent เลยรายงานว่าสำเร็จ แต่อีกสอง service หลุด sync ไปเงียบ ๆ จน workflow ใน production พัง

### รันผ่าน shared harness

พอส่งคำสั่งเดียวกันผ่าน harness ที่ครอบทั้งสาม repo:

1. **Impact analysis** — agent สแกน dependency graph ใน workspace ร่วม แล้วเจอว่าแก้ billing กระทบ checkout กับ invoicing ([[code-knowledge-graphs|code knowledge graph]] คือเครื่องมือแนวนี้)
2. **Multi-repo confirmation gate** — harness เห็นว่าผลกระทบข้ามหลาย repo เลยหยุดแล้วเปิดด่านยืนยันแบบ blocking ให้ developer
3. **Coordinated update** — พอคนอนุมัติ agent แก้ contract กับ implementation ทั้งสาม repo แล้วรัน test ข้าม service เพื่อตรวจว่าแก้ครบกันจริง

**ได้อะไร:** agent ไม่ได้ฉลาดขึ้น แต่ harness ทำให้มันเห็นผลกระทบ แล้วส่งการตัดสินใจเรื่อง scope ไปให้คน

## Delivery loop เต็มวง

ผู้เขียนเสนอ pipeline หกช่วงเป็นทางหนึ่งที่รวม guides, sensors และด่านคนเข้าด้วยกัน:

| ช่วง | ใครทำ | ทำอะไร |
|---|---|---|
| ANALYZE | structured intake | รวบรวม Jira ticket กับ technical context บังคับ explicit default เมื่อ input ขาด |
| BLUEPRINT | architecture agent | วาง file plan ข้าม repo ถ้าเจอผลกระทบหลาย service ก็หยุดรอคนเซ็นที่ multi-repo gate |
| RED | test agent | เขียน acceptance test ที่ยัง fail ตาม requirement |
| GREEN | implementer agent | เขียนโค้ดน้อยที่สุดจน test ของ RED ผ่านหมด |
| REFACTOR | (บทความไม่ระบุ agent) | เกลาโครงสร้างและ convention ของทีม โดย test ต้องยังผ่าน |
| REVIEW | automated review agent | ตรวจว่า test ครอบ acceptance criteria ครบไหม |

ใน pipeline นี้ feedback สองแบบมีหน้าที่ต่างกัน:

- **Human feedback loop** — เก็บไว้กับเรื่องที่มีผลตามมาและย้อนไม่ได้ เช่น อนุมัติ scope สถาปัตยกรรมข้าม repo ในช่วง BLUEPRINT
- **Automated feedback loop** — จัดการ failure ที่แก้ได้ด้วยกลไก เช่น REVIEW เจอ acceptance criterion ที่ยังไม่มี test ก็ไม่ดึงคนเข้ามา แต่ส่งงานกลับไป RED/GREEN ให้สร้าง test กับ implementation ที่ขาด แล้วรัน REVIEW ใหม่เองก่อนเปิด pull request

**ผลคือ:** คนถูกเรียกเฉพาะตอนต้องตัดสินเรื่องใหญ่ ส่วนเรื่องที่เครื่องตรวจได้ loop จัดการเอง

## ดูแล harness เหมือนเป็นซอฟต์แวร์

ผู้เขียนย้ำว่า harness ไม่ใช่กอง config หรือ prompt ที่เขียนครั้งเดียวแล้วลืม ต้องดูแลเข้มเท่า production software:

- **Version control และ peer review** — เก็บ agent definition, skill, rule และ workflow ไว้ใน version control แก้ harness ผ่าน pull request ที่มีคน review
- **Earn every rule (กฎต้องมีที่มา)** — อย่าเติมกฎเผื่อไว้ กฎแต่ละข้อต้องโยงกลับไปหาเหตุจริงได้ เช่น production failure ในอดีต จุดที่ developer เจ็บ requirement ด้าน security หรือข้อจำกัดทางวิศวกรรมที่ตั้งไว้แล้ว กฎที่ไม่มีที่มาเพิ่มเสียงรบกวน ทำให้ attention ของ model เจือจาง และคุณภาพ output ตก (ดู [[instruction-budget]])
- **Refactor ต่อเนื่อง** — พอ LLM เก่งขึ้น ให้กลับไปดูกฎเดิมแล้วตัดข้อที่หมดยุค ผู้เขียนเตือนด้วยว่า harness เองก็มีต้นทุนดูแล ทุก rule, sensor และ workflow กลายเป็นส่วนของระบบที่ทีมต้องตามแก้

**ได้อะไร:** harness ถูก review และย้อนดูได้เหมือนโค้ด ไม่ใช่ความรู้ที่กระจายอยู่ใน prompt ของแต่ละคน

## สรุป: อิสระแบบมีขอบเขต

บทความปิดว่า การพัฒนาซอฟต์แวร์ด้วย agent ให้เชื่อถือได้ ต้องไปไกลกว่า prompt engineering

> "Asking a model to be careful is fundamentally different from building an environment where violations are prevented or mechanically caught."
> — ขอให้ model ระวัง ไม่เหมือนสร้างสภาพแวดล้อมที่กันการฝ่าฝืนไว้ก่อน หรือจับได้ด้วยกลไก

จุดชี้ขาดไม่ได้อยู่ที่พูดว่า "ใช้ harness" แต่อยู่ที่รู้ว่าจะแบ่งความรับผิดชอบตลอด delivery lifecycle ยังไง และดูแล harness เป็นซอฟต์แวร์ที่มี version และตรวจย้อนได้

## หมายเหตุและเรื่องที่ยังเปิด

- **ตัวอย่างเป็นภาพสมมติ** บทความไม่มีตัวเลข ไม่มี case study จาก production และไม่ได้วัดว่า pattern นี้ลด failure ได้เท่าไร
- **ด่านคนถูกนับสองที่** "confirmation only for high-blast-radius decisions" อยู่ทั้งในรายการ guide pattern และเป็นชั้นที่สามแยกออกมา อ่านได้ว่าเป็นกลไกเดียวกันที่มองสองมุม คือเป็นกฎที่ออกแบบไว้ล่วงหน้า (guide) และเป็นจังหวะที่คนเข้ามาตอน run (gate)
- **ไม่ลงรอยกับทิศของ Cursor เรื่อง multi-repo** [[cursor|Cursor]] เล่าใน [[what-weve-learned-building-cloud-agents]] ว่าย้าย logic multi-repo ออกจาก harness ไปให้ agent ตัดสินเองผ่าน tool และเตือนว่า cloud agent ที่รอ permission อาจค้างเป็นชั่วโมง บทความนี้กลับวาง blocking gate ไว้ใน harness เมื่อผลกระทบข้าม repo สองแหล่งอาจถูกคนละบริบท ฝั่งหนึ่งห่วงต้นทุนของการหยุด อีกฝั่งห่วงต้นทุนของการพลาด wiki เก็บไว้ทั้งสองด้าน ดู [[blast-radius-gates]]
- **REVIEW loop ยังพึ่ง test ที่ AI เขียน** ช่วง REVIEW ส่งงานกลับ RED/GREEN เองจนกว่า test จะครอบ acceptance criteria แต่ Böckeler เตือนใน [[harness-guides-sensors]] ว่า behaviour harness ตอนนี้ฝากความหวังกับ test ที่ AI สร้างเองมากเกินไป และ [[teepagorn-claude-code-adoption-nobody-reading|เคส voxium]] ชี้ว่า test กับ code ที่มาจาก AI อาจเชื่อ assumption ผิดข้อเดียวกัน บทความแยก test agent กับ implementer agent ออกจากกัน แต่ไม่ได้แสดงว่าการแยกนี้กัน assumption ร่วมได้
- **ด่านเห็นแค่สิ่งที่อยู่ใน graph** ตัวอย่างทำงานได้เพราะ harness รู้ dependency ทั้งหมด ถ้า consumer อยู่นอก workspace หรืออ่าน field ผ่าน data pipeline ที่ไม่อยู่ใน graph ด่านก็ไม่ลั่น
- บทความลิงก์ไปงานอื่นของ Thoughtworks ที่ wiki ยังไม่ได้ ingest ได้แก่ "What is harness engineering", "Exploring AI coding sensors", "Supervisory engineering: orchestrating the software middle loop", "Code review is dead, long live code review" และ "Cybernetics: human on the loop"

**Provenance:** ผู้ใช้ส่งเนื้อบทความ ชื่อ URL และชื่อผู้เขียนมาให้ วันเผยแพร่ 2026-09-29 ดึงจากหน้าเว็บตอน ingest (2026-09-30) หน้าเว็บไม่ได้ระบุตำแหน่งงานของผู้เขียน ไม่ได้เก็บสำเนาลง `raw/`

## See also

- [[harness-guides-sensors]]
- [[harness-engineering-bockeler]]
- [[blast-radius-gates]]
- [[silent-success-verbose-failure]]
- [[harness-ratchet]]
- [[instruction-budget]]
- [[progressive-disclosure]]
- [[coding-harness]]
- [[code-knowledge-graphs]]
- [[agentic-code-review]]
- [[policy-as-code-for-agents]]
- [[agent-harness-engineering]]
- [[what-weve-learned-building-cloud-agents]]
- [[thoughtworks]]
- [[birgitta-bockeler]]
