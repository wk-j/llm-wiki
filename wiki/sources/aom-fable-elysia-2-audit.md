---
title: Aom Khunpanitchot - Fable Elysia 2 Audit
type: source
tags: [ai-coding, code-review, agents, audit, fable, elysia]
created: 2026-07-02
updated: 2026-07-02
sources: []
url: https://www.facebook.com/AomKhunpanitchot/posts/pfbid02VdEw7C6eAHA4VZDWKc4jUw7Y5xXZ1Vsuhn5M63kp7Q3ThyzVW2ZHRAuJZeYehDn7l
date_ingested: 2026-07-02
---

# Aom Khunpanitchot - Fable Elysia 2 Audit / Fable audit Elysia 2

โพสต์ Facebook นี้ของ [[aom-khunpanitchot|Aom Khunpanitchot]] (ผู้โพสต์จาก URL ที่ให้มา; ชื่อ author ใน capture ว่าง) เป็น field report ภาษาไทยเรื่อง [[fable|Fable]] ทำ [[deep-agent-audit|deep agent audit]] ให้ [[elysia-2|Elysia 2]]. แก่นของโพสต์คือ Aom เริ่มไม่แน่ใจแล้วว่า Fable อาจเก่งด้าน technical ทั่วไปกว่าเขาหรือยัง เพราะมันจับจุดอ่อนใน codebase ที่เขาเขียนและดูแลเองมาหลายปีได้ละเอียดมาก.

นี่ไม่ใช่ benchmark กลาง. ควรอ่านเป็นประสบการณ์จากคนใช้เครื่องมือกับ codebase จริงหนึ่งชุด. แต่โพสต์มีค่ากับ wiki เพราะมันเป็นตัวอย่างเข้มของคำถามเดิมใน [[agentic-code-review|Agentic Code Review]]: ถ้า AI reviewer อ่านได้ลึกกว่าคนเต็มเวลาในบางงาน บทบาทของคนควรย้ายไปอยู่ตรงไหน.

## เหตุการณ์ในโพสต์

Aom เล่าว่าเขาให้ AI หลายตัว full review และ audit code ของ Elysia 2 อย่างหนักมาก. รายชื่อที่พูดถึงคือ Opus 4.8, Fugu Ultra, และ GLM 5.2. ทุกตัวให้สัญญาณว่า code พร้อม stable release หรืออย่างน้อย RC แล้ว. เขาย้ำว่า prompt ไม่ได้เบา: ให้ทำทุกอย่างที่ทำได้, ไม่สน token, ใช้ workflow/subagent ได้เต็มที่.

เขายังลอง update plugin 11 ตัวแล้วบอกว่าทุกตัวใช้ได้แทบไม่ต้องแก้ code. เมื่อนำไปใส่ app จริงก็เหมือนทำงานปกติ. ในสภาพนี้ เขาจึงคิดว่าคงพอขยับ Elysia 2 ออกจาก alpha ได้.

แล้วเขาลอง Fable ต่างออกไป: prompt เดียวที่เขียนไม่เกิน 3 นาที, ให้ review แต่ไม่ต้องแก้ code, เปิด ultracode auto mode, แล้วปล่อยทิ้งไว้จนชน limit ก่อนรอกลับมาสั่งต่อ. ผลคือ Fable แตกตัวเป็น agent เกือบ 100 ตัวและเขียน report ว่ายังไม่เหมาะขึ้น RC.

**ได้อะไร:** ความต่างที่โพสต์ชี้ไม่ใช่แค่ "model ไหนฉลาดกว่า" แต่คือการที่ harness/workflow บางแบบยอมลงทุน compute และ agent fan-out เพื่ออ่าน codebase ลึกกว่าการ review ปกติ.

## Report ที่ Fable สร้าง

ตามโพสต์ Fable ส่ง report ละเอียดมาก: 104 ข้อ, ยาวประมาณ 24,000 คำ หรือ 174,000 ตัวอักษร. เนื้อหาไล่ตั้งแต่ปัญหา วิธีแก้ ไปจนถึงการ verify ว่าปัญหามีจริง. Aom บอกว่าอ่านคร่าว ๆ แล้วรู้สึกว่ามัน review ได้ละเอียดในระดับที่มนุษย์แทบไม่มีทางยอมลงทุนทำเท่านี้ หรือถ้าทำจริงอาจใช้ทีมช่วยกัน 2-3 สัปดาห์.

จุดสำคัญคือ Fable ไม่ได้แค่ตอบว่า "ยังไม่พร้อม". มันให้ artifact ที่คนอ่านต่อได้: รายการปัญหา, เหตุผล, วิธีแก้, และหลักฐาน. ตรงนี้ทำให้ AI review กลายเป็น [[harness-guides-sensors|inferential sensor]] ที่มีน้ำหนักมากกว่า comment สั้น ๆ แบบ "looks risky".

แต่ source capture ที่ ingest ไม่มีไฟล์ report 104 ข้อแนบมาด้วย. ดังนั้น wiki ควรเก็บ claim นี้เป็น claim จากโพสต์ ไม่ใช่ข้อพิสูจน์อิสระว่า Fable ถูกทุกข้อ.

**ผลคือ:** output ที่ยาวมากไม่ได้มีค่าเพราะยาว. มันมีค่าเมื่อแยกปัญหาเป็นชิ้น, ผูกกับบรรทัด/วิธีแก้/วิธี verify, และทำให้คนตัดสินใจ release ได้ดีขึ้น.

## ทำไมเรื่องนี้กระทบบทบาทของมนุษย์

Aom ย้ำว่ารู้จัก codebase นี้ดีมาก: เขียนเอง ดูแลมา 4 ปี รู้โครงสร้างพอจะเขียนใหม่จากศูนย์ได้ในไม่กี่เดือน. แต่ Fable ยังพบจุดอ่อนที่เขาไม่คิดว่าจะมีได้ภายในเวลาไม่ถึง 3 ชั่วโมง.

นี่ทำให้โพสต์ไปไกลกว่าคำถาม "AI ช่วย review ได้ไหม". คำถามจริงคือ ถ้า agent หนึ่งตัวสามารถทำงาน audit ที่ละเอียดเกินกว่าคนทั่วไปจะยอมทำในเวลาปกติ คนที่งานประจำคือ "เขียน code ตามสั่ง" และไม่ได้มีความได้เปรียบชัดเจนจะอยู่ตรงไหน.

Aom ยังไม่ได้บอกว่าคนหมดความหมาย. เขาเชื่อว่ายังมีงานให้คนทำในบทบาท domain expert, specialist, tech lead, และตำแหน่งตัดสินใจ. แต่เขามองว่างาน coding ตามสั่งอย่างเดียวเริ่มเสี่ยงมากขึ้น.

**ได้อะไร:** บทบาทมนุษย์ไม่หาย แต่เลื่อนขึ้นไปที่ judgement, domain context, prioritization, release decision, และ accountability. นี่ตรงกับ [[strategic-vs-tactical-programming|Strategic vs Tactical Programming]] และ [[agentic-code-review|Agentic Code Review]].

## จุดที่ขัดกับ claim เดิมใน wiki

โพสต์นี้ไม่ได้ลบ claim เดิมที่ว่า benchmark อย่าง [[deepswe|DeepSWE]] และ [[frontierswe|FrontierSWE]] แสดงช่องว่างของ frontier model. มันเพิ่มอีกมุมหนึ่ง: ในงานจริงบางงาน harness + long-running fan-out อาจสร้างผลลัพธ์ที่ benchmark model เดี่ยวไม่สะท้อน.

มี tension ที่ควรเก็บไว้เป็นคำถามเปิด:

- ถ้า Opus 4.8, Fugu Ultra, และ GLM 5.2 ต่างบอกว่า Elysia 2 พร้อม RC แต่ Fable บอกว่ายังไม่พร้อม ใครถูก.
- ปัญหา 104 ข้อเป็น bug จริงกี่ข้อ, severity สูงกี่ข้อ, และข้อไหนเป็น taste/architecture preference.
- ความเก่งของ Fable มาจาก model, harness, auto mode, subagent scale, instruction ของ Aom, หรือการใช้ token/เวลาเยอะมาก.
- รายงานยาวระดับ 24,000 คำช่วยลด risk จริง หรือเพิ่มภาระ review แบบใหม่ให้มนุษย์.

**ผลคือ:** แหล่งนี้ควรถูกวางเป็น field evidence ของ [[deep-agent-audit|deep agent audit]] ไม่ใช่ verdict สุดท้ายว่า Fable ชนะทุก frontier model.

## คำถามเปิด

- Report 104 ข้อมีรายละเอียดอะไรบ้าง และข้อไหนได้รับการยืนยันโดย test/patch จริง.
- "Fable หมด" ในโพสต์หมายถึง quota/credit/agent budget แบบไหน.
- ultracode auto mode คือ mode ของ Fable หรือ harness รอบ Fable กันแน่.
- Fable ใช้ model อะไร, routing อย่างไร, และแตก agent เกือบ 100 ตัวด้วย policy แบบไหน.
- Elysia 2 ในโพสต์นี้เป็น project/product/library ใดแน่ชัด. Capture ไม่มี repo หรือ product page.
- โพสต์ capture แสดงเวลา `19m` แต่ไม่มี timestamp เต็ม. วันที่ ingest คือ 2026-07-02; วันที่โพสต์จริงควร verify จาก Facebook ถ้าต้องอ้างทางประวัติ.

## See also

- [[aom-khunpanitchot]]
- [[fable]]
- [[elysia-2]]
- [[deep-agent-audit]]
- [[agentic-code-review]]
- [[coding-harness]]
- [[orchestration-tax]]
- [[long-running-agents]]
- [[dynamic-workflows]]
- [[model-honesty]]
