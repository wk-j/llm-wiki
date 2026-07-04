---
title: "Piyalitt Ittichaiwong — Attention ไม่ใช่ Token: สรุป Codex Keynote AI Engineer World's Fair"
type: source
tags: [ai, codex, openai, agents, loop-engineering, attention, thai, keynote]
created: 2026-07-05
updated: 2026-07-05
url: https://www.facebook.com/piyalitt/posts/pfbid0gRZehexh9YbSoNbW4Gkca5wgHk1VGbPeK2zCdBmMgef8MtiUsGqX9V9fLUvHdJv1l
date_published: 2026-07-05
sources: []
---

# Piyalitt Ittichaiwong — Attention ไม่ใช่ Token / Codex Keynote

โพสต์ Facebook ของ [[piyalitt-ittichaiwong|Piyalitt Ittichaiwong]] สรุป keynote ของทีม [[openai-codex|Codex]] ในงาน [[ai-engineer-worlds-fair|AI Engineer World's Fair]] (รวมตัว AI engineer กว่า 7,000 คน) นำโดย [[romain-huet|Romain Huet]] (หัวหน้า Developer Experience ของ OpenAI) กับ [[alexander-embiricos|Alexander Embiricos]] (หัวหน้าฝ่ายผลิตภัณฑ์ Codex) ก่อนส่งไม้ต่อให้ [[peter-steinberger|Peter Steinberger]] (the Clawfather — ผู้สร้าง OpenClaw ที่ตอนนี้ร่วมงานกับ OpenAI)

โพสต์เปิดด้วยสรุปสั้น ๆ ของ [[thariq-shihipar|Thariq]] จากทีม Claude Code เรื่อง map vs territory และ [[unknowns-matrix|unknowns 4 ช่อง]] (มีหน้าเต็มใน [[field-guide-to-fable-finding-unknowns]]) แล้วลงลึก keynote หลัก

## แก่นความคิด

ยุคที่ model เก่งขึ้น **คอขวดย้ายจาก AI ไปอยู่ที่มนุษย์** — ไม่ใช่แค่เรื่อง prompt สวย แต่คือเราจัดการ unknowns และ [[attention-bottleneck|attention]] ได้ดีแค่ไหน. ฝั่ง OpenAI/Codex ยืนยันว่า engineering ไม่ตาย แต่ถูกนิยามใหม่: คนที่ได้เปรียบคือคนออกแบบ [[inner-loop-outer-loop|outer loop]] ให้ agent วิ่ง inner loop แทน

> "ตอนนี้สิ่งที่จำกัดผมมากที่สุดไม่ใช่ token หรือ compute อีกต่อไป แต่คือ attention และมันเพิ่มไม่ได้"
> — Peter Steinberger บนเวที (อ้างในโพสต์)

> "อนาคตไม่ใช่การเปิด terminal 20 หน้าต่าง แต่คือ loop ที่ดีกว่าเดิม มาสร้างมันกันเถอะ"
> — Peter Steinberger ปิดท้าย keynote

## ส่วนเปิด: Thariq กับ unknowns (สรุปย่อ)

Piyalitt เปิดโพสต์ด้วย frame จาก Thariq ที่สอดคล้องกับ wiki ที่มีอยู่แล้ว:

- **"The map is not the territory"** — prompt/context คือแผนที่; codebase/โลกจริงคือพื้นที่จริง; ช่องว่างคือ unknowns ที่ AI ต้องเดา
- ยิ่ง model เก่ง คอขวดยิ่งไม่ใช่ตัว AI แต่เป็นความสามารถของเราในการ clarify สิ่งที่ยังไม่รู้
- คนเก่ง agentic coding ไม่ใช่คนพิมพ์ prompt สวย แต่คือคน unknowns น้อยและรู้วิธีจัดการ
- เทคนิค 3 จังหวะ: ก่อนเขียน (blind spot pass, brainstorm/prototype, interview), ระหว่างเขียน (`implementation-notes`), หลังเสร็จ (quiz ก่อน merge)
- ตัวอย่าง color grading ในวิดีโอ launch Fable: ไม่สั่ง AI ทำมั่ว แต่ให้สอนก่อนเพื่อให้รู้ว่า "ดี" หน้าตาเป็นยังไง

**ผลคือ:** ทุก explainer/brainstorm/interview/prototype คือวิธีราคาถูกหา blind spot ก่อนมันแพงเกินแก้ — ตรงกับประโยคใน [[unknowns-matrix]]

## งาน World's Fair ของชาว AI engineer

[[romain-huet|Romain]] เปรียบงานกับ World's Fair ในอดีต — อนาคตถูกสร้างต่อหน้าสาธารณะ ไม่ได้ลอยมาจากที่ไหน. ท่ามกลางกระแสว่า engineer จะหายไปเมื่อ code กลายเป็นนามธรรม ทีม Codex ยืนยันตรงข้าม:

- Software เคยกินโลก → AI กิน software → **AI engineer กำลังกินโลก**
- แก่น engineering ไม่เคยเป็นการพิมพ์ code แต่คือแก้ปัญหาด้วยวิทยาศาสตร์ + การออกแบบ + รสนิยม + วิจารณญาณ + จินตนาการ
- ยุค AI = กลับสู่รากเหง้า ไม่ใช่จุดจบ

## จาก 15 เดือน เหลือ 6 สัปดาห์

ตัวเลขที่สะท้อนความเร็ววงการ: OpenAI ปล่อย model ใหม่จากเคยทุก ~15 เดือน ตอนนี้เหลือ ~ทุก 6 สัปดาห์ — สัปดาห์ก่อนงานเพิ่ง preview ตระกูล GPT-5.6

ประสบการณ์ coding วิวัฒน์เป็นขั้นบันได:

1. autocomplete ธรรมดา
2. inline prediction
3. Cmd+K (แก้ code ได้แต่ยังไม่ตรวจงานตัวเอง)
4. model รัน test ตรวจงานตัวเอง
5. วันนี้: model รับเป้าหมายยาวและทำต่อเนื่องจนจบ

**ตัวอย่างบนเวที:** DevDay 2024 Romain ใช้ o1-preview สร้างหน้าจอควบคุม drone แบบสด — โมเดลยังรัน/ตรวจงานตัวเองไม่ได้ เลยลุ้นไปกับมัน (โอกาส demo รอด ~3 ใน 4 → ฉายา "the demo god"). DevDay 2025 แค่ปีเดียวถัดมา ปล่อยให้ agent คุมกล้องและไฟทั้งงานได้

## Agent ก่อนและหลังการเขียน code

ปี 2026 ทีม Codex ปล่อยของต่อเนื่อง — Alexander ยกของโปรด: **Codex app**, **Goal Mode**, **Remote**. ทั้งหมดเกิดจากทีมใช้ Codex สร้าง Codex เอง

จุดเปลี่ยน: agent ทำได้แทบทุกอย่างบนคอมพิวเตอร์ — ไม่ได้ช่วยแค่ตอนเขียน code แต่ช่วยก่อนหน้า (ทำไมงานนี้ต้องเกิด) และหลัง (review, deploy). ยิ่งเชื่อม agent กับเหตุผลของงาน + ขั้น review/deploy มากเท่าไหร่ ยิ่งเริ่มงานเองและพาไปถึงเส้นชัยได้มาก

Alexander มุม product: สิ่งที่น่าตื่นเต้นไม่ใช่แค่ความเร็ว แต่คือ **ตัดสินใจได้ดีขึ้นว่าควรสร้างอะไร** — prototype หลายไอเดียได้มากขึ้น เหลือเวลาคลุกกับ user จริง

## เป้าหมายไม่ใช่แทนที่ engineer

ทีมยอมรับตรง ๆ: งานคอมพิวเตอร์ความยาวปานกลาง ถ้าให้คนกับ model เวลาเท่ากัน โดยเฉลี่ย model น่าจะทำได้ดีกว่า. คำตอบของทีม: **เสริมพลัง engineer ไม่ใช่ทำให้หายไป**

ภาพเปรียบเทียบ: ทำงานกับทีมคนจริง — ส่วนใหญ่คุยแล้วปล่อยให้ทีมลงมือ ไม่มีใครยืนมองข้ามไหล่ทุกชิ้น แต่บางจังหวะก็อยากลงลึก. หลักออกแบบ: **ผู้ใช้ต้องรู้สึกเชี่ยวชาญและเป็นเจ้าของงานเสมอ** — เข้าถึงรายละเอียดต้องไม่ยาก

### เบื้องหลัง Codex app ที่เคยโดนค้าน

ตอน pitch มี developer บอกว่าไม่มีวันออกจาก terminal/Vim/Emacs. วันนี้คนกลุ่มเดียวกันกลายเป็นผู้ใช้. เหตุผลทีม:

- **CLI** เป็นหน้าจอทำงานร่วมกันสำหรับงานทุกประเภทไม่ได้ — โดยธรรมชาติเป็น chat เป็นหลัก
- **IDE** เรียงลำดับผิดทาง — บังคับเริ่มจาก code ทั้งที่งานยุคนี้ควรเริ่มจากคุยแล้วค่อยลงลึก
- **Codex app** = chat เรียบง่าย ใช้ได้ทั้ง coding และงานอื่น — ชี้จุดแล้วสั่งแก้เฉพาะตรงนั้น หรือลงมือแก้เอง

Alexander (อ่านนิยายวิทยาศาสตร์เยอะ) บอก chat ถูกประเมินค่าต่ำเกินไป — โลกต้องการ chat เป็นตัวตนเดียวขอความช่วยเหลือได้ทุกเรื่อง คู่กับหน้าจอทำงานร่วมกันทรงพลังสำหรับตอนอยากตรวจ/ปรับทิศ/ปั้นด้วยมือ

## Stack ที่เปิดทุกชั้น

ชั้น harness ของ Codex **open source ทั้งหมด** — fork/ดัดแปลงได้. ใช้ชื่อกลาง `AGENTS.md` แทนประดิษฐ์รูปแบบใหม่ เพื่อให้ agent ค่ายอื่นใช้ร่วมกัน. model OpenAI เป็นค่าเริ่มต้น ไม่ล็อก — สลับ open model ใน agent loop เดิมได้. harness ถูกใช้ใน post-training ด้วย — model หัดเรียก tool ในสภาพแวดล้อมเดียวกับที่เปิดให้ developer

ตัวอย่าง: Thomas/Dimillian บน X ใช้ App Server สร้าง **Codex Monitor** ก่อน Codex app เปิดตัว — วันนี้เข้ามาร่วมทีมและสร้าง Codex สำหรับ iOS. ชั้นแอปขยายได้: browser ในตัว, plugin system, browser use / computer use เป็น plugin ด้วยจุดต่อเดียวกับที่เปิดให้ทุกคน. มี plugin สาย data science และ design เปิด open source. subscription เดิมใช้ได้ใน OpenCode, Pi, Droid, OpenClaw, Xcode, JetBrains

**สรุปชั้นนี้:** ไม่ได้สร้างระบบหนึ่งใช้เองแล้วสร้างอีกระบบลดทอนให้ developer — ทุกชั้นใช้ของชิ้นเดียวกับที่ส่งมอบ

## [[value-maxing|Value maxing]] — ฉลาดขึ้น ถูกลง เร็วขึ้นพร้อมกัน

ทีมเรียกแนวคิดนี้ว่า **value maxing** ไม่ใช่ token maxing — บทสนทนากับผู้บริหาร engineering วนอยู่รอบนี้

**แกนคุ้มค่า:**

- ทุกคนอยากได้ความฉลาดระดับ frontier + ปริมาณความฉลาดต่อเงินสูงสุด
- ตัวอย่าง: GPT-5.6 **Terra** — ความฉลาดระดับ GPT-5.5 ในราคาครึ่งเดียว
- **Luna** — ชนะ model ดังหลายตัว ราคา $1/1M input, $6/1M output
- รุ่นบนสุดตระกูล 5.6 ขึ้นนำ Terminal Bench (ตามกราฟบนเวที — ยัง source-attributed)

**แกนความเร็ว:**

- GPT-5.3 Codex Spark พิสูจน์แล้วว่าความเร็วปลดล็อกอะไรได้ แต่คนไม่อยากแลกความฉลาด
- รอบนี้: frontier ของตระกูล 5.6 รันบน Cerebras ที่ **750 token/วินาที** — เปิดใช้เดือนถัดไป
- ภาพเปรียบเทียบ: ได้ PR ขนาดใหญ่ใน ~10 วินาที
- ไม่ใช่แค่คำตอบเดียวเร็วขึ้น แต่เปิดทางให้ agent ลอง 5–6 แนวทางขนานแล้วคัดอันดี — ในเวลาน้อยกว่าที่เมื่อก่อนใช้สร้างคำตอบเดียว

## ปิดโน้ตบุ๊กแล้วปล่อย agent ทำงานต่อ

ยกมือในห้อง: ใครเคยเปิดโน้ตบุ๊กทิ้งไว้เต็มออฟฟิศให้ agent รันต่อ — มือยกทั่วห้อง. สิ่งที่ทุกคนต้องการ: ปิดเครื่องตัวเอง แล้วให้งานหลายชิ้นรันขนานบนเครื่องของมันแยกขาดกัน

การเปิดตัวใหญ่ครั้งแรกของ Codex คือ **Codex Cloud** — กำลังมีอัปเกรดสำคัญตามมา. ภาพอนาคต: **ไม่มีเส้นแบ่งแปลก ๆ ระหว่าง local กับ cloud** — มี agent เดียวคุยได้ทุกที่ มันคิดเองว่างานนี้ต้องใช้สภาพแวดล้อมแบบไหน

มีการอ้างทำนายของ Theo บนจอ — ผู้พูดฟันธงว่าภาพแบบนั้นจะมาถึงเร็วกว่า 6 เดือน

## บทเรียนจาก Peter: orchestrate หรือแค่ polling?

Peter เปิดด้วยภาพเดือนมกราคม: เปิด terminal พร้อมกันเกิน 10 หน้าต่าง คอยเฝ้าว่าอันไหนเสร็จเพื่อป้อนงานใหม่ — ตอนนั้นรู้สึกเป็น productivity ขั้นสุด วันนี้มองย้อนกลับแล้วออกจะดูตลก

ประโยคคม: **นึกว่ากำลัง orchestrate แต่จริง ๆ แค่ polling** — ตัวเขาเองเป็น scheduler, router, และ memory ของทั้งระบบ. จาก pair กับ agent ทีละตัว → 10 terminal = บริหารลูกทีม 10 คน

วิธีทำงานวันนี้: คุยกับ **manager agent ตัวเดียว** รันต่อเนื่องระยะยาว → กระจายงานไป worker. งานยากจริงค่อย pair กับ worker โดยตรง. สรุป: *"ผมบริหารผู้จัดการของบริษัทเล็ก ๆ ที่พนักงานเป็น agent"*

สามอย่างที่ทำให้ภาพนี้เป็นจริง:

1. **Server-side compaction** — งานรันยาวเสถียร ไม่ต้องเปิด session ใหม่เลี่ยงปัญหา
2. **ระบบประสานงาน** — thread เดียวสร้างและคุมหลาย project
3. **Automation** — ปลุก manager ตัวเดิมเมื่อมีเหตุการณ์

รวมกัน = context ที่คงอยู่ + การกระจายงาน + ตัวกระตุ้น → **นั่นคือ loop ของเรา**

## Bottleneck ย้ายที่ — จาก token → compute → attention

ปีที่แล้วข้อจำกัดหลักของ Peter คือ token — แก้ด้วยการเข้าไปทำงานที่ OpenAI (แซวตัวเองว่า scale ไม่ได้). จากนั้นย้ายไป compute — thread รันพร้อมกันจน MacBook ดังเหมือนเครื่องยนต์เจ็ต; แก้เกือบหมดด้วย **test box** (ให้ agent รัน test บนเครื่องอื่น). **ข้อจำกัดวันนี้คือ attention** — ต่างจาก token/compute ตรงที่เพิ่มไม่ได้

ทักษะสำคัญ: ตัดสินใจว่าจะใช้ attention ไปกับอะไร. คำถามบนเวที: เรายังนั่งจ้อง agent ระหว่าง code ไหลผ่านหน้าจออยู่ไหม? กับ model รุ่นก่อนพฤติกรรมนี้จำเป็น เพราะเห็น agent เลี้ยวผิดต้องกด escape. แต่ model รุ่นล่าสุดเข้าใจเจตนาได้ดีขนาดที่การนั่งดู code ถูกเขียนกลายเป็นการเผา attention เปล่า ๆ

## Inner loop / outer loop

Peter วาด loop ที่ใช้จริงกับ open source project:

1. มีคนเปิด issue เข้ามา
2. **Manager** ตื่น → เทียบ issue กับเป้าหมาย/วิสัยทัศน์ project → ตัดสินใจว่าน่าทำไหม
3. ถ้าใช่ → สร้าง **worker** หนึ่งตัว สืบหา แก้ รัน test
4. **Agent อีกตัว** รีวิวผลลัพธ์ซ้ำอีกชั้น
5. Peter ไม่ต้องดู agent ทำงานหรืออ่านทุกข้อความ — เมื่อ manager ต้องการเขาจริง ๆ จะส่ง PR พร้อม issue ต้นทาง + diff (บางครั้งแถมวิดีโอ/build ให้ VNC ดู)
6. Peter รีวิวรอบเดียว ทิ้งโน้ต หรืออนุมัติ → loop หมุนต่อจน merge เองหลังผ่านการตรวจครบ

หลักการ: **agent วิ่ง inner execution loop; มนุษย์กำหนดทิศทางและตัดสินใจใน outer loop**

## โจทย์ที่ยังไม่มีใครแก้ได้

เมื่อ manager มีอายุยืนขึ้น การผูกกับโน้ตบุ๊กเครื่องเดียวเริ่มผิดฝาผิดตัว. Codex ย้ายงานข้ามเครื่องได้แล้ว; OpenClaw มี gateway/node — แต่ Peter บอกยังไม่มีอันไหนเป็นรูปแบบสุดท้าย. อยากให้ agent เชื่อมทุกเครื่องของเขาเอง รู้เองว่างานไหนไป cloud ได้ งานไหนต้อง local

Manager ที่แท้จริงไม่ควรเป็นแค่ session ในแอปเดียว — ควรเป็น agent ที่ส่งข้อความหาได้ สั่งผ่าน Slack ได้ รายงานได้ไม่ว่าอยู่ที่ไหน. คำถามทิ้งท้าย: **ทำไมเรายังแค่คุยกับ agent แล้วให้มันออกแบบ loop ทั้งหมดให้เราเองไม่ได้?** — คำตอบวันนี้: ยังไม่มีใครแก้สำเร็จ

Peter ปิดว่า model พัฒนาเร็วกว่า harness และองค์กรที่ห่อหุ้ม — การออกแบบสิ่งเหล่านี้คือโจทย์ engineering ข้อถัดไป

## มุมมองส่งท้ายจากเพจ

- อาชีพ engineer ถูกนิยามใหม่ ไม่ใช่ถูกลบ — ขยับจากผู้พิมพ์ code ไปเป็นผู้ออกแบบระบบ กำหนดทิศทาง ตัดสินใจ outer loop
- ทรัพยากรแพงที่สุดคือ attention — token ซื้อเพิ่มได้ compute เช่าเพิ่มได้ แต่สมาธิมีเท่าเดิม
- ระบบดีต้องรบกวนเราเฉพาะจังหวะที่การตัดสินใจของมนุษย์สร้างความแตกต่างได้จริง
- stack ที่เปิดกว้างมีแนวโน้มชนะ — OpenAI ใช้ stack เดียวกับที่ส่งให้ developer ส่งสัญญาณว่าอนาคต agent ถูกสร้างร่วมกันทั้ง ecosystem

## Key takeaways

1. **คอขวดย้ายที่** — จาก model → unknowns/attention ของมนุษย์; token/compute แก้ได้ attention แก้ไม่ได้
2. **Engineering ไม่ตาย** — กลับสู่รากเหง้า: แก้ปัญหา + ออกแบบระบบ + outer loop
3. **Codex stack เปิดทุกชั้น** — harness, AGENTS.md, App Server, plugin; ใช้ของชิ้นเดียวกับที่ส่งให้ developer
4. **Value maxing** — ฉลาด + ถูก + เร็วพร้อมกัน (Terra, Luna, Cerebras 750 t/s) ไม่ใช่แค่ token maxing
5. **อนาคต = loop ไม่ใช่ 20 terminal** — manager agent + worker + compaction + automation; มนุษย์ไม่ polling แต่ตัดสินใจ
6. **โจทย์เปิด:** agent ที่ออกแบบ loop เองทั้งหมด + manager ที่ไม่ผูกกับเครื่อง/แอปเดียว — ยังไม่มีใครแก้สำเร็จ
7. **เชื่อมกับ Thariq:** ทักษะที่คุ้มลงทุนคือรู้จักสิ่งที่ยังไม่รู้ ไม่ใช่แค่สั่งให้ model เก่งขึ้น

## ข้อควรระวัง / คำถามเปิด

- ตัวเลข benchmark, ราคา Terra/Luna, Terminal Bench, Cerebras 750 t/s — มาจาก keynote ผ่านโพสต์ Piyalitt ยัง source-attributed จนกว่าจะตรวจจากเอกสาร OpenAI โดยตรง
- ทำนาย Theo เรื่อง unified local/cloud — อ้างบนเวทีว่าจะมาเร็วกว่า 6 เดือน แต่ไม่ได้ระบุ tweet/post ต้นฉบับในโพสต์
- Peter's workflow เป็นประสบการณ์ power user / creator OpenClaw — ไม่ได้แปลว่า transfer ตรงไป enterprise โดยไม่มี governance (เทียบ [[orchestration-tax]])

## See also

- [[field-guide-to-fable-finding-unknowns]]
- [[unknowns-matrix]]
- [[loop-engineering]]
- [[orchestration-tax]]
- [[attention-bottleneck]]
- [[inner-loop-outer-loop]]
- [[value-maxing]]
- [[cloud-agents]]
- [[openai-codex]]
- [[peter-steinberger]]
