---
title: Orchestration Tax
type: concept
tags: [ai, agents, productivity, attention, orchestration, concurrency, bottleneck]
created: 2026-05-29
updated: 2026-05-29
sources: [The Orchestration Tax.md]
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

## See also

- [[the-orchestration-tax]]
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
