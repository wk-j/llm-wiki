---
title: "Software After Software"
type: source
tags: [ai, software-engineering, manifesto, agents, business-model, organization]
created: 2026-05-27
updated: 2026-05-27
sources: []
---

# Software After Software / ซอฟต์แวร์หลังยุคซอฟต์แวร์

แถลงการณ์ 12 ข้อจาก [[thorsten-ball|Thorsten Ball]] (วิศวกรของ [[amp|Amp]] ที่ [[sourcegraph|Sourcegraph]]) โพสต์บน X เมื่อ 2026-05-26 เพื่อประกาศจุดยืนของ [[amp-labs|Amp Labs]] ซึ่งเป็นหน่วยทดลองแนวหน้าของ Amp

โทนของบทความเป็นแบบ manifesto สั้น คม และตั้งใจให้แรง: Ball ไม่ได้บอกว่า AI จะมาช่วยให้เร็วขึ้น แต่บอกว่า **สมมติฐานของวงการซอฟต์แวร์ 40 ปีที่ผ่านมาตายแล้ว** และคนที่ยังคิดตามแบบเดิมจะตกขบวน

- Source: [thread บน X](https://x.com/thorstenball/status/2059304318055150066) (2026-05-26)
- ผู้เขียน: [[thorsten-ball|Thorsten Ball]]
- ปิดท้ายด้วยการประกาศ [[amp-labs|Amp Labs]] เป็นโครงสร้างองค์กรที่ Ball มองว่าเป็นคำตอบ

## 12 ข้อในแถลงการณ์

Ball จัดโครงสร้างเป็น 12 หัวข้อย่อย แต่ละข้อมี sub-point เล็ก ๆ ด้านล่าง สรุปย่อพร้อมประเด็นสำคัญ:

### 1. ทุกอย่างกำลังเปลี่ยน

Ball เปิดมาด้วยภาพใหญ่: เราอยู่ใน transformation ที่ทำให้สมมติฐานเกี่ยวกับซอฟต์แวร์และธุรกิจ "เกือบทุกข้อ" ต้องคิดใหม่ จะใช้เวลาหลายปี endgame ยังไม่ชัด แต่ "ดีกว่าตามให้ทัน อย่านั่งดูเฉย ๆ"

### 2. ยังประเมิน model ต่ำกว่าความจริง

> "Even if you think you're factoring in exponential improvements, you're likely still underestimating."

ประเด็นย่อยที่แรง:
- Model ไม่ต้อง perfect ก็พอจะทำลายเศรษฐศาสตร์เก่าของซอฟต์แวร์ได้ — แค่ดีกว่าค่าเฉลี่ยก็พอ
- การให้ "training wheels" (เช่น check code, spellchecker) จะหายไป เพราะ "Why put training wheels on someone who never wobbles?"
- "Quality of output will solely depend on input, not capability of the model" — คุณภาพจะขึ้นอยู่กับ input ของเรา ไม่ใช่ capability ของ model อีกแล้ว
- **"Every eight weeks you should give more leash to these models"** — ทุก 8 สัปดาห์ให้ปล่อย leash ยาวขึ้น ไม่งั้นจะติดอยู่จุดต่ำของกราฟ

### 3. อนาคต code ส่วนใหญ่จะถูกเขียนโดย agent

> "The assistant sidebar is dead. Agents will no longer be mere assistants."

- Agent จะไม่ใช่ assistant ข้างจอ แต่จะ run แม้ไม่มีใครนั่งหน้าเครื่อง
- จะ run ยาวกว่าและคุมน้อยกว่าที่คนส่วนใหญ่คิด
- **"An agent forced to work like a human is a wasted agent"** — บังคับให้ agent ทำงานแบบมนุษย์ คือเปลือง agent
- **"The unit of work becomes the delegated task, not the code to be written"** — หน่วยของงานคือ task ที่ delegate ไป ไม่ใช่ code ที่ต้องเขียน

### 4. คอขวดของการพัฒนาซอฟต์แวร์ย้ายแล้ว

- การเขียน valid code = trivial
- ที่ยังเหลือคือ "errors of engineering" — priorities, sequencing, tradeoffs
- **"Review will shift from code to decisions"** — review จะย้ายจาก code ไปอยู่ที่ decisions

### 5. Software development แบบที่เรารู้จัก 40 ปีตายแล้ว

- วิชาชีพ software dev ตั้งบนสมมติฐานว่า "การเขียน code ยากและพลาดง่าย"
- อุตสาหกรรม software ตั้งบนสมมติฐานว่า "code หายาก"
- ทั้งสองสมมติฐานไม่จริงอีกแล้ว

### 6. Process และพิธีกรรมเก่าไม่เหมาะอีกแล้ว

ส่วนนี้คือหัวใจของแนวคิด [[process-drag|Process Drag]]:

> "AI is not only an accelerator for X. It changes whether X should exist at all."

Ball ยกตัวอย่าง 4 ข้อ:
- "Why spend an hour prioritizing what can be done in thirty minutes?"
- "Why consider building a prototype when you can talk one into existence?"
- "Why wait for a review when you can spin up five agents to review in parallel?"
- "Why pick a single idea to try when you can try them all in parallel and dismiss four out of five without hurting a single ego?"

### 7. ซอฟต์แวร์เปลี่ยนรูปร่าง

- ซอฟต์แวร์ที่ผ่านมาออกแบบเพื่อมนุษย์ใช้ ในอนาคตจะออกแบบเพื่อ agent ใช้ ([[agent-native-infrastructure]])
- ซอฟต์แวร์จะถูกสร้าง **just-in-time** มากกว่า ahead-of-time ([[just-in-time-software]])
- เส้นแบ่งระหว่าง "ใช้ซอฟต์แวร์" กับ "สร้างซอฟต์แวร์" จะเบลอ อาจหายไปเลย

### 8. มูลค่าย้ายออกจาก code

หัวข้อย่อยของ [[value-migration-from-code|Value Migration from Code]]:

- ซอฟต์แวร์ที่ทำ X ไม่มีค่า ถ้า agent ทำ X ได้
- ซอฟต์แวร์ที่เป็น "code ที่คนอื่นเขียนให้เราใช้" มูลค่าลดลง
- ซอฟต์แวร์ที่ encode workflow มูลค่าลดลง
- สิ่งที่มูลค่าเพิ่มขึ้น: **data, permissions, distribution, trust, compliance, regulatory position, physical assets**
- vendor ที่ moat คือ "ลูกค้าสร้างเองไม่คุ้ม" จะโดนบีบ
- คนสุดท้ายที่ยอมรับเรื่องนี้คือ software companies เอง เพราะ business model สร้างบน scarcity เก่า

### 9. ผู้ชนะจะ reorganize around models

หัวข้อย่อยของ [[reorganize-around-models|Reorganize Around Models]]:

- การยัด model ลงในระบบ/org chart/process เดิมไม่พอ
- "Agents are wasted when made to work like people"
- **ผู้ชนะคือคนที่ organize ทีมรอบ model** — ไม่ใช่ใส่ model เข้าทีมเก่า
- **"A small team with strong judgment and many agents will outrun a large team trying to fit AI into processes from before the transformation"**
- "Ability to keep up matters more than headcount"

### 10. ทุก institution ที่จริงจังต้องมี "camp at the frontier"

หัวข้อย่อยของ [[frontier-camp|Frontier Camp]]:

- บริษัทใหญ่ sit-out ไม่ได้
- เรียนรู้อนาคตผ่าน committee ไม่ได้
- ต้องมี **ทีมเล็ก autonomous ที่ frontier** สร้างรอบ model
- ทีมนี้ไม่ใช่เพื่อ "เอา AI มาใส่กับวิธีทำงานเดิม" แต่เพื่อ **ค้นหาวิธีทำงานใหม่ แล้วดึงบริษัทตามไป**
- ต้องใกล้ระบบจริง ข้อมูลจริง ข้อจำกัดจริง ผลกระทบจริง
- ผลผลิตของมันไม่ใช่แค่ซอฟต์แวร์ แต่คือ "คนและ practice"

### 11. วิศวกรเปลี่ยน

- วิศวกรไม่หาย แต่เปลี่ยน
- ย้ายจาก code ไปสู่: product thinking, shaping systems, judging tradeoffs, business outcomes
- "Most valuable engineers will be system thinkers and operators that can increase business value"

อันนี้ไปทาง [[engineering-role-shift|Engineering Role Shift]] ที่หน้านี้มีอยู่แล้ว

### 12. Therefore — สรุปจุดยืน

> "We build for a world in which intelligence is abundant, continuous, and cheap."

- optimize เพื่อเรียนรู้ว่าโลกนั้นหน้าตาเป็นยังไง
- ไม่เก็บ process เก่าไว้เพราะความเคยชิน
- ไม่รอ end state ให้ชัดก่อน
- **"The best move is to play the game"**
- ไปที่ frontier ก่อน เพราะนั่นคือที่ที่อนาคตถูกเรียนรู้

ปิดด้วย: "That's what we believe in at Amp and why we created Amp Labs."

## ประเด็นสำคัญสำหรับคนอ่าน

ถ้าจะเอาแค่ 5 ประเด็นที่สำคัญที่สุด:

1. **Code abundance เปลี่ยน economics ของซอฟต์แวร์** — โยงกับ [[code-is-free]] ของ Lopopolo. Ball เพิ่มมุมว่ามันไม่ใช่แค่เรื่อง engineer cost แต่เป็นเรื่อง business model ทั้งอุตสาหกรรม
2. **Process drag** — พิธีกรรมการทำงานที่เคยช่วย (planning, prioritization, review) อาจกลายเป็น drag ในโลกที่ implementation ราคาถูก
3. **Value migration** — ถ้า agent ทำ X ได้ ซอฟต์แวร์ที่ขาย X ก็ไม่มีค่า ค่ามูลค่าย้ายไป data, distribution, trust, compliance
4. **Reorganize around models** — ผู้ชนะคือคนที่จัดทีมรอบ model ตั้งแต่ต้น ไม่ใช่ใส่ model เข้าทีมเดิม
5. **Frontier camp** — corporate response ที่ Ball แนะนำ: สร้างทีมเล็ก autonomous ที่ frontier เพื่อค้นหา new way of working

## ความขัดแย้งและจุดที่ควรระวัง

Ball เขียนในมุมของคนที่ขาย Amp/Amp Labs — มี incentive ทำให้ message แรง อยากให้คนกล้าเปลี่ยน คุณภาพของ argument ส่วนใหญ่จึงเป็นเชิง assertion มากกว่า evidence

ข้อ 2.4 ที่บอกว่า "The need to review code written by agents will fade" และ "Errors of expression will be gone" คือ claim ที่แรงและคนหลายกลุ่มไม่เห็นด้วย:

- [[lars-faye]] และ [[andrej-karpathy|Karpathy]] เตือนเรื่อง [[llm-coding-pitfalls|LLM coding pitfalls]] ที่ทำให้ code review ยังจำเป็น
- [[matt-pocock]] บอกใน [[matt-pocock-software-fundamentals]] ว่า "ไม่ดูโค้ดเลยคือกับดัก [[specs-to-code|Specs-to-Code]]"
- [[ryan-lopopolo|Lopopolo]]'s "code is free" framing ยังคงให้ verification อยู่กับมนุษย์ ([[token-billionaire]])

ในข้อ 4 Ball เลี่ยงปัญหานี้บางส่วนโดยบอกว่า "review will shift from code to decisions" — เลื่อนงาน review ไปอีกระดับ ไม่ใช่ลบทิ้ง ซึ่งเข้ากับ [[acceptance-bottleneck|Acceptance Bottleneck]] มากกว่า

## ทำไม manifesto นี้น่าสนใจ

ที่น่าสนใจไม่ใช่เพราะ Ball เป็นคนแรกที่พูดเรื่องนี้ — แต่ละข้อแยกกันมีคนพูดมาแล้ว ([[andrej-karpathy|Karpathy]] เรื่อง [[software-3-0]], [[ryan-lopopolo|Lopopolo]] เรื่อง [[code-is-free]], [[panutat-tejasen]] เรื่อง [[harness-engineering]], [[chrisza-stuff|ChrisZa]] เรื่อง [[interaction-productivity]])

ที่น่าสนใจคือ:

1. **Ball พยายามรวมทุกข้อเป็น manifesto ที่ทีม corporate ใช้ได้** — ไม่ใช่แค่แนวคิด standalone
2. **เป็นการ position ของ Amp Labs ที่ขาย "frontier camp as a service"** — ถ้าจะเปลี่ยน เริ่มจากตรงไหน
3. **โทนหนักแน่นกว่าคนอื่น** — Ball พูดเรื่อง "death of software development as we know it" ตรง ๆ ไม่ hedge

ผลคือ document นี้น่าจะถูกอ้างเป็น "manifesto" ของฝั่งที่เชื่อ end-to-end ในการเปลี่ยนผ่านสู่ agent-first

## See also

- [[thorsten-ball]]
- [[amp]]
- [[amp-labs]]
- [[sourcegraph]]
- [[code-is-free]]
- [[process-drag]]
- [[value-migration-from-code]]
- [[reorganize-around-models]]
- [[frontier-camp]]
- [[engineering-role-shift]]
- [[agent-native-infrastructure]]
- [[just-in-time-software]]
- [[delegation-mindset]]
- [[acceptance-bottleneck]]
- [[software-3-0]]
- [[harness-engineering]]
