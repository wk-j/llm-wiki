---
title: Orchestration Tax
type: concept
tags: [ai, agents, productivity, attention, orchestration, concurrency, bottleneck]
created: 2026-05-29
updated: 2026-07-09
sources: [The Orchestration Tax.md, How to Keep Shipping When You Walk Away from Your Desk — Zack Proser, WorkOS.md, Agentic Code Review.md, "รู้จักกับ Loop Engineering — mikelopster transcript", techsauce-ai-brain-fry.md, l8-principals-agentic-engineering-workflow-kun-chen.md, aom-fable-elysia-2-audit.md, how-ai-became-more-expensive-than-workers-it-replaced.md, stop-building-ai-agents-old-way.md, code-isnt-free-mario-zechner-hard-truths-coding-ai.md, piyalitt-codex-keynote-attention-not-token.md, bun-in-rust.md]
---

# Orchestration Tax / ภาษีค่าควบคุมวง

**Orchestration Tax** คือต้นทุนที่เกิดตอนคนเปิด AI agent หลายตัวพร้อมกันแล้วลืมไปว่า การเปิด agent เพิ่มไม่ได้ทำให้มี "เรา" เพิ่ม นิยามของ [[addy-osmani|Addy Osmani]] (วิศวกร Google) คือ **ช่องว่างเชิงโครงสร้างระหว่างของที่ agent ผลิตได้ กับของที่เรา merge เข้าระบบได้จริง** — สิ่งที่เกิดขึ้นเมื่อเอา resource ที่ทำงานทีละเส้น (serial) ไปคุม resource ที่ทำงานขนาน (concurrent)

ชื่อนี้ Richard Seroter เป็นคนตั้งบน panel ที่ Google I/O แล้ว Addy เอามาแกะต่อในโพสต์ [[the-orchestration-tax]] (28 พ.ค. 2026) จุดสำคัญที่เขาย้ำ: **นี่ไม่ใช่ปัญหาวินัย แต่เป็นปัญหา architecture** — แก้ด้วยการขยันขึ้นไม่ได้ ต้องแก้ด้วยการออกแบบ

## ความไม่สมมาตรที่คนไม่คิดราคา

แก่นของปัญหาอยู่ที่ความไม่สมมาตร:

- **เปิด agent ถูกมาก** — กดปุ่มเดียว พิมพ์ประโยคเดียว
- **ปิดงาน agent (close the loop) แพงมาก** — ต้องเช็คว่าผลถูกไหม แล้วเอาไปปรับให้เข้ากับงานที่ agent ตัวอื่นแก้ไปด้วย

คนที่ทำ "ปิดงาน" ได้คือมนุษย์ และมีคนเดียว เปิดได้ไม่จำกัด ปิดได้ทีละนิด — ช่องว่างตรงนี้คือที่มาของภาษี

## เราคือ GIL — กลไกของภาษี

Addy ใช้สอง mental model จากวงการ performance engineering อธิบายว่าทำไมเพิ่ม agent ถึงไม่ช่วย:

**เราคือ GIL ของ agent** — Python มี Global Interpreter Lock (GIL) คือ lock ตัวเดียวที่ thread ต้องแย่งถือก่อนรัน เปิดกี่ thread ก็ได้แต่รันจริงทีละตัว agent ก็เหมือนกัน — รันพร้อมกันได้หมด แต่พองานไหนต้องใช้ **ความเข้าใจสถาปัตยกรรมจริง ๆ หรือต้องแก้ merge conflict** งานนั้นต้องมาถือ lock ที่มีตัวเดียว และเราถือมันอยู่

**Amdahl's Law** — speedup จากการขนานถูกจำกัดด้วยสัดส่วนงานที่ยังต้องทำเป็น serial เพิ่ม core เท่าไหร่ก็ตันที่เพดานนั้น ในงาน agent **ส่วน serial คือ judgement** เปิด agent 8 ตัวไม่ได้ทำให้เวลาตัดสินใจเร็วขึ้น มันแค่ทำให้คิวที่รอป้อนเข้าสมองเรายาวขึ้น

สรุปเป็นกฎเก่าของ performance ที่ยังทำคนแปลกใจ: **เร่งส่วนที่ไม่ใช่คอขวด ไม่เพิ่ม throughput** มีแต่จะกองงานค้างหน้าคอขวดให้สูงขึ้น คอขวดจริงคือขั้น review และ throughput ของทั้งระบบเท่ากับ throughput ของขั้นนั้นเป๊ะ

**ผลคือ:** จำนวน agent ที่เปิดไม่ใช่ตัวชี้วัด output — output ถูกจำกัดด้วยอัตราที่เรา review และ merge ได้

## อาการเมื่อภาษีไม่ถูกจ่าย

จะฝืนขยันแก้ข้อจำกัดเชิงโครงสร้างไม่ได้ ภาษีถูกเก็บอยู่ดี ถ้าฝืน มันโผล่มาในรูปพวกนี้:

- **เหนื่อยแบบเฉพาะตัว** — รัน serial processor ที่ 100% ไม่มี slack ทุกครั้งที่ไปเช็ค agent ที่ทิ้งไว้ จ่าย **context switch cost**: flush สมองแล้วโหลด context ใหม่จากศูนย์ CPU ทำในไมโครวินาที เราทำในนาทีและโหลดกลับไม่เคยครบ "5 agent = cold reload 5 ครั้ง + process เบื้องหลังที่คอยกังวลว่าควรเช็คตัวไหน"
- **review ตื้นเขิน** — อ่านผ่าน ๆ เพราะไม่มีเวลาพอ
- **[[cognitive-surrender]]** — ยอมรับโค้ดของ agent เพราะการตั้งความเห็นของตัวเองกินความสนใจที่ไม่เหลือแล้ว
- **หนี้สองชั้น** — [[cognitive-debt]] (mental model ต่อโค้ดเบสเก่าและไม่ตรงจริง) สะสมพร้อม technical debt โดยไม่โผล่บน dashboard จนกว่า production จะพัง

[[zack-proser|Zack Proser]] ให้หลักฐานจากหน้างานอีกแบบใน [[how-to-keep-shipping-away-from-desk|How to Keep Shipping When You Walk Away from Your Desk]]: [[simon-willison|Simon Willison]] เปิด agent ขนานสี่ตัวแล้วหมดแรงก่อน 11 โมง และ Zack เองพบว่าวันจันทร์กับอังคารดู productive มาก แต่พอปลายสัปดาห์งานกระจัดกระจายและคนหมดแรง. เขาสรุปตรงกับหน้านี้ว่า **agent ไม่ใช่คอขวดแล้ว คนต่างหาก**.

[[mikelopster]] ให้ตัวอย่างจากงาน content ใน [[mikelopster-loop-engineering|คลิป Loop Engineering]]: ตั้ง loop ให้ดึงข่าว/source แล้วเขียน draft ทุกครึ่งวัน. agent เลือก source ได้ดีและเขียน draft พอใช้ได้ แต่ output ยังมีความเชื่อมโยงแปลก ๆ ที่ต้องให้คนอ่านและแก้. พอปล่อยไปสองวัน draft กองเต็มระบบ. ตรงนี้แสดงภาษีแบบชัดมาก: **producer เร็วขึ้น แต่ consumer ยังเป็นคนเดิม**.

[[techsauce|Techsauce]] เพิ่มเลนส์ workplace ทั่วไปผ่าน [[techsauce-ai-brain-fry|โพสต์เรื่อง AI Brain Fry]]: คนไม่ได้เหนื่อยเพราะ AI ทำงานไม่ได้ แต่เหนื่อยเพราะต้องคุม ตรวจ เทียบ และสลับ AI หลาย tool พร้อมกัน. ตัวเลขที่โพสต์ยกมาบอกว่า AI oversight ใกล้ชิดทำให้ mental fatigue และ information overload เพิ่มขึ้น และ productivity เริ่มตกเมื่อใช้เกิน 3 tool พร้อมกัน. นี่คือ orchestration tax นอกโลก coding: output เร็วขึ้น แต่ judgement ของคนยังเป็นคอขวดเดิม.

[[kun-chen|Kun Chen]] เป็นกรณีฝั่งที่พยายามจ่ายภาษีนี้ด้วยระบบ ไม่ใช่ด้วยแรงใจ. ใน [[l8-principals-agentic-engineering-workflow-kun-chen|workflow walkthrough]] เขาใช้ [[lavish|Lavish]] ให้ requirement ชัดก่อนทำ, [[no-mistakes|No Mistakes]] ให้ agent self-review + E2E evidence ก่อนถึงคน, [[treehouse|Treehouse]] กัน worktree housekeeping ไม่ให้กินหัว, และ [[first-mate|First Mate]] ลดการสลับ context ระหว่าง agent sessions.

ข้อสำคัญ: เขาไม่ได้ทำให้ภาษีหายไป. เขาเลื่อนภาษีไปอยู่จุดที่ควรจ่าย คือ judgement ตอนต้นและตอนท้าย. งานตรงกลางที่พิสูจน์ได้ถูก offload ให้ pipeline.

[[aom-khunpanitchot|Aom Khunpanitchot]] ให้ภาพอีกด้านใน [[aom-fable-elysia-2-audit|Fable audit Elysia 2]]. [[fable|Fable]] สร้าง report 104 ข้อจาก audit ที่แตก agent เกือบ 100 ตัว. แบบนี้ลดภาษีบางส่วน เพราะ agent ทำงานอ่านละเอียดแทนคนได้มาก แต่ก็สร้างภาษีใหม่: คนต้องอ่าน report, คัด false positive, จัด severity, และตัดสินใจว่าอะไร block release จริง.

จุดเรียนรู้คือ deep audit ไม่ได้ลบคอขวดมนุษย์. มันเปลี่ยนงานมนุษย์จาก "หา bug เองทุกมุม" เป็น "judge report ที่มี evidence เยอะมาก". ถ้า report ดี ภาษีลด. ถ้า report ฟุ้ง ภาษีแค่ย้ายที่.

[[economy-media|Economy Media]] เพิ่มมุม CFO ใน [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]]: ถ้า agent ผลิตงานมากขึ้นแต่ต้องใช้ token มากขึ้นและคนยังต้องตรวจอยู่ ภาษีไม่ได้อยู่แค่ในสมองมนุษย์ แต่โผล่เป็นบิลจริงในงบองค์กรด้วย. นี่เชื่อม orchestration tax กับ [[enterprise-ai-roi|enterprise AI ROI]] โดยตรง

[[prompt-engineering|Prompt Engineering]] ใน [[stop-building-ai-agents-old-way]] เสนอ [[agent-observability|agent observability]] เป็นวิธีลดภาษีฝั่งการเฝ้า: แยก raw trace ออกจาก dashboard ที่เห็น task, cost, error, screenshot, และ key decision. แต่คลิปไม่ได้บอกว่าคนหายไปจาก loop. Observability แค่ช่วยให้คน step in ถูกจุด แทนที่จะอ่าน transcript ทั้งหมด.

**ข้อควรระวัง:** dashboard ที่ไม่คัด signal จะกลายเป็น orchestration tax อีกชั้น. Dashboard ที่ดีต้องช่วยตัดสินใจ ไม่ใช่แค่เพิ่มสิ่งที่ต้องคอยดู.

[[mario-zechner|Mario Zechner]] ให้ภาพจากคนดูแล [[pi-agent|pi]] ใน [[code-isnt-free-mario-zechner-hard-truths-coding-ai|Code Isn't Free]]: เขาเปิดหลาย session เพื่อ preprocess issue ได้ แต่ไม่ถือว่านี่คือ 10x output ตรง ๆ. หลัง agent วิเคราะห์ เขายังต้องอ่านข้อเสนอ เข้า code เอง และตัดสินใจว่า solution ไหนควรทำ. วันที่เขาไล่ได้ 30 issue เป็นวันที่มีประสิทธิภาพสูงมาก แต่ทำบ่อยไม่ได้ เพราะ context switching ทำให้สมองหมดแรง.

**ได้อะไร:** parallel agent ช่วยได้เมื่อใช้เป็น queue ของ analysis ที่มนุษย์ batch-review ได้. ถ้าใช้เป็นกองทัพ implementation ที่รอ merge พร้อมกัน ภาษีจะกลับมาที่สมองคนเหมือนเดิม.

[[bun-in-rust|Bun in Rust]] เป็นเคสที่จ่ายภาษีด้วยระบบจนคุ้ม. [[jarred-sumner|Jarred Sumner]] รันประมาณ 64 Claudes พร้อมกัน 11 วัน แต่ไม่ได้ปล่อยให้ output ไหลเข้าหัวคนดิบ ๆ. เขาแปลงงานเป็น workflow, ใช้ compiler/test/CI เป็น gate, แยก [[adversarial-review-loops|adversarial reviewers]], จำกัดคำสั่ง git/cargo ช่วงที่เสี่ยงชนกัน, แล้วอ่าน output เพื่อแก้ process. ภาษียังอยู่: ต้อง monitor, อ่าน evidence, แก้ workflow, ตรวจ test ไม่ถูก skip และตัดสินใจ merge. แต่ภาษีถูกจ่ายตรงจุดที่สร้าง leverage.

**ผลคือ:** agent fleet ใหญ่ไม่ขัดกับ orchestration tax ถ้าระบบลดงานที่ไม่ต้องใช้ judgement ออกจริง. ถ้าไม่มี proof pipeline แบบนี้ ตัวเลข agent/commit/lines จะกลายเป็นคิวรอคนอ่าน.

## Attention bottleneck — คอขวดที่ซื้อเพิ่มไม่ได้

[[peter-steinberger|Peter Steinberger]] บนเวที Codex keynote (สรุป [[piyalitt-codex-keynote-attention-not-token]]) ตั้งชื่อใหม่ให้ภาพเดียวกันในมุมทรัพยากร: พอแก้ token และ compute แล้ว ข้อจำกัดหลักกลายเป็น **attention** — ต่างจากสองอย่างแรกตรงที่เพิ่มไม่ได้. ดูหน้า [[attention-bottleneck]] เต็ม ๆ

อาการที่ชัด: นั่งจ้อง agent ระหว่าง code ไหลผ่านหน้าจอ — กับ model รุ่นก่อนจำเป็น แต่ model รุ่นล่าสุดเข้าใจเจตนาได้ดีขนาดที่การจ้องกลายเป็นการเผา attention เปล่า ๆ. ทางแก้คือ [[inner-loop-outer-loop|outer loop]]: มนุษย์ตัดสินเฉพาะจังหวะที่ judgement สร้างความต่าง (อนุมัติ PR, ทิ้งโน้ต) ไม่ polling ทุก tool call

**ผลคือ:** orchestration tax วัดเป็นคิวก่อน review; attention bottleneck วัดเป็นสมาธีที่เหลือ — สองเลนส์ของคอขวดเดียวกัน

## วิธีแก้ — architect your attention

ทางแก้คือปฏิบัติกับ attention เหมือน serial resource ที่หายาก แล้วออกแบบระบบรอบมัน เหมือนออกแบบ distributed system รอบคอขวด Addy ลิสต์ 5 ข้อ:

| วิธี | หลักการ concurrency | ทำอะไร |
|---|---|---|
| **Scale fleet to review rate** | backpressure | จำนวน agent ที่ถูกต้อง = จำนวนที่ review ได้ดีจริง (มักหลักเดียว) ไม่ใช่จำนวนที่ UI ยอมให้เปิด |
| **Sort the work** | แยก parallel ออกจาก serial | งาน isolated → ส่ง background agent; งานที่ judgement คือเนื้องาน → **ห้ามขนาน** เพราะแค่ทำให้แย่ลง |
| **Batch your reviews** | ลด context switch | รีวิวหลาย agent ในรอบเดียวถูกกว่าเช็คทีละตัวแบบ cold; ให้สายป่านยาว ปล่อยงานกองนิดแล้วประมวลทั้ง batch |
| **Only spend the lock on judgement** | offload งานที่ verify เองได้ | ให้ agent เขียน test ที่ผ่าน / generate screenshot พิสูจน์ 80% น่าเบื่อเอง เก็บ attention ไว้กับ 20% ที่ต้องการมนุษย์ |
| **Protect your serial time** | ให้คอขวดได้ทรัพยากรดีที่สุด | คอขวดต้องการชั่วโมงที่ดีที่สุด ไม่ใช่เศษนาทีระหว่างเช็ค agent; บางทีหยุด orchestrate แล้วคิดเรื่องเดียวให้หนักคือ leverage สูงสุด |

ข้อที่สี่ผูกกับ [[behavioral-verifier]] และ [[model-honesty]] โดยตรง — ถ้าโมเดลพิสูจน์งานตัวเองได้และ **ไม่เนียนว่าทำเสร็จทั้งที่ยังไม่ผ่าน** lock ของมนุษย์ก็ถูกใช้น้อยลง

**ได้อะไร:** ระบบที่เคารพ throughput จริงของมนุษย์ แทนที่จะอ้อมมันด้วยการแอบลดมาตรฐานเราลงเงียบ ๆ

## busy ≠ productive — กับดักที่มองไม่เห็นจากข้างใน

failure mode ที่อันตรายที่สุดคือมันมองไม่เห็นจากข้างใน agent 20 ตัวที่รันอยู่ให้ความรู้สึก productivity มหาศาล dashboard เต็ม ทุกอย่างขยับ แต่ความรู้สึกนั้นหลุดจากการ ship โค้ดดีขึ้น main จริง — "ยุ่งสุด ๆ แต่แทบไม่ได้ผลิตอะไร" รู้สึกเหมือน "productive จริง" เป๊ะจากมุมคนทำ

นี่คือเหตุผลที่ Addy สรุปว่า **"เปิด agent ไม่ใช่ทักษะ ใครก็เปิด 20 ตัวได้ ทักษะจริงคือออกแบบระบบรอบ resource เดียวที่ clone ไม่ได้ — ความสนใจของเรา"**

## ที่ทางในวิกินี้ — น้ำหนักถ่วงฝั่งบริโภค

หน้านี้เป็นด้านตรงข้ามของหน้าที่พูดเรื่อง "เปิด subagent เยอะ ๆ":

- [[subagent-patterns]] / [[agent-swarm]] / [[dynamic-workflows]] — ฝั่ง **production**: เปิด subagent ขนานเป็นร้อยได้ orchestration tax คือฝั่ง **consumption** ที่เตือนว่าคอขวดมนุษย์ปลายทางไม่ scale ตาม **ข้อแก้ต่าง:** ยิ่ง agent self-verify ได้มาก (dynamic workflows ผูก test suite เป็น oracle) ภาษีฝั่งมนุษย์ยิ่งลด — แต่การ "ตัดสินใจ architecture" และ "merge งานที่ขัดกัน" ยังเป็น serial เสมอ
- [[theory-of-constraints]] / [[local-optimization-trap]] — orchestration tax คือ ToC เล่าด้วยภาษา concurrency: review คือคอขวด เพิ่ม agent คือ optimize จุดที่ไม่ใช่คอขวด
- [[acceptance-bottleneck]] (ChrisZa) — คอขวดเดียวกันมองจากฝั่งคนรับงาน: ผลิตเร็วไม่พอ ต้องมีคน "ยอมรับและรับผิดชอบ" ก่อนเดินต่อ
- [[care-allocation]] — attention เป็น resource หายากที่ต้องจัดสรร orchestration tax คือกรณีเฉพาะตอนจัดสรรกับวง agent
- [[long-running-agents]] — งานของ Addy เอง; "Sort the work" + "give agents a long leash" คือเหตุผลเชิงปฏิบัติของ background/async agent + Mission Control inbox
- [[loop-engineering]] — งานของ Addy เองอีกชิ้น (ฝั่งระบบ/ผลิต): ออกแบบลูปที่ prompt agent แทนเรา. ลูปแก้การชน *เชิงกลไก* ด้วย [[git-worktrees|worktree]] และผลิตงานขนานเยอะขึ้น — แต่ Addy เตือนเองว่า "YOU are still the ceiling, your review bandwidth decides how many you can actually run" → ลูปที่ดีขึ้นยิ่งทำให้ orchestration tax คมขึ้น ไม่ใช่หายไป
- [[developer-balance]] — คำตอบระดับวันทำงาน: ใช้ signal layer, verification gate, remote steering, และ health constraint เพื่อไม่ให้ orchestration tax กลายเป็น burnout
- [[ai-brain-fry]] — อาการในหัวของคนเมื่อ oversight load จาก AI tools มากเกินไป; เป็น workplace cousin ของ orchestration tax
- [[agentic-code-review]] — คำตอบระดับ review architecture: ไม่ใช่พยายามอ่านทุกบรรทัดให้เร็วขึ้น แต่ tier review ตาม blast radius, require evidence ก่อนรับ review, ใช้ AI reviewer เป็น sensor หลาย character, และเก็บ human judgement ไว้กับ path ที่พังแล้วเจ็บ. นี่คือวิธีใช้ "Only spend the lock on judgement" แบบเป็นระบบ
- [[mikelopster-loop-engineering]] — หลัก feedback gate: loop ที่ไม่มี scorer ชัดจะเพิ่มงานค้างให้คนตรวจ ไม่ได้เพิ่ม throughput จริง

## See also

- [[agentic-code-review]]
- [[the-orchestration-tax]]
- [[agent-observability]]
- [[cognitive-surrender]]
- [[addy-osmani]]
- [[theory-of-constraints]]
- [[local-optimization-trap]]
- [[acceptance-bottleneck]]
- [[care-allocation]]
- [[cognitive-debt]]
- [[subagent-patterns]]
- [[agent-swarm]]
- [[dynamic-workflows]]
- [[long-running-agents]]
- [[behavioral-verifier]]
- [[model-honesty]]
- [[loop-engineering]]
- [[git-worktrees]]
- [[developer-balance]]
- [[how-to-keep-shipping-away-from-desk]]
- [[mikelopster-loop-engineering]]
- [[code-isnt-free-mario-zechner-hard-truths-coding-ai]]
- [[ai-brain-fry]]
- [[techsauce-ai-brain-fry]]
- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[no-mistakes]]
- [[first-mate]]
- [[treehouse]]
- [[deep-agent-audit]]
- [[aom-fable-elysia-2-audit]]
- [[bun-in-rust]]
- [[adversarial-review-loops]]

- [[enterprise-ai-roi]]
- [[ai-token-economics]]
- [[tokenmaxxing]]
- [[attention-bottleneck]]
- [[peter-steinberger]]
- [[piyalitt-codex-keynote-attention-not-token]]
