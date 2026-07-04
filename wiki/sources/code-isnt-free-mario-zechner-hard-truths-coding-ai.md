---
title: Code Isn't Free - Mario Zechner on the Hard Truths of Coding With AI
type: source
tags: [ai, coding-agents, software-engineering, open-source]
created: 2026-07-04
updated: 2026-07-04
sources: [https://www.youtube.com/watch?v=GhjU-KvXtT0]
---

# Code Isn't Free - Mario Zechner on the Hard Truths of Coding With AI / โค้ดไม่ได้ฟรี

Source นี้คือบทสัมภาษณ์ [[mario-zechner|Mario Zechner]] (ผู้สร้าง [[pi-agent|pi]]) โดย [[jan-niklas-wortmann|Jan-Niklas Wortmann]]. แกนของคลิปคือ AI coding agent ทำให้ลองทางเลือกได้เร็วขึ้นจริง แต่ไม่ได้ทำให้ความรับผิดชอบต่อโค้ดหายไป. ถ้าเราใช้ความเร็วไปผลิตโค้ดที่ไม่มีใครเข้าใจ บิลจะกลับมาในรูป maintenance, review, security, และสมองของคนที่ต้องรับผิดชอบระบบ.

## แก่นของบทสนทนา

Mario ไม่ได้ปฏิเสธ coding agent. เขาใช้มันหนักมาก และสร้าง [[pi-agent|pi]] เอง. แต่เขาแยก "agent ช่วยคิดและสำรวจ" ออกจาก "agent ผลิตโค้ดกองโตแล้วคนยอมรับโดยไม่เข้าใจ".

ประโยคตั้งต้นของคลิปคือ "Code is never free" เพราะผลของการตัดสินใจจะตามมาทีหลัง. ตรงนี้ไม่ได้ลบแนวคิด [[code-is-free|Code is Free]] ในวิกิ แต่เพิ่มขอบเขตใหม่: implementation อาจถูกลงมาก แต่ ownership ของโค้ดยังแพงเหมือนเดิม.

**ผลคือ:** productivity ที่ดีไม่ใช่จำนวนบรรทัดหรือจำนวน agent. มันคือความเร็วในการหา solution ที่ดีโดยยังไม่เสียความเข้าใจของคน.

## ทำไม Mario สร้าง pi

Mario เริ่มจากใช้ [[claude-code|Claude Code]] แล้วพอใจ แต่หลังจากนั้น tool ไม่เข้ากับ workflow เขา. ปัญหาหลักไม่ใช่ model อย่างเดียว แต่คือ harness เปลี่ยนบ่อย: system prompt, tool definitions, reminder ที่ถูก inject ข้างหลัง, และ release cadence วันละหลายครั้ง. พอ harness เปลี่ยน workflow ที่ผู้ใช้เขียนไว้ก็พังได้ แม้ชื่อ model จะยังเหมือนเดิม.

[[pi-agent|pi]] จึงยืนบนปรัชญา [[malleable-tools|malleable tool]]: core เล็ก, extension ทำเองได้, ไม่มี hidden context, และผู้ใช้ควบคุม workflow เอง. Mario มองว่า coding agent ไม่ได้จำกัดอยู่แค่งานเขียนโค้ด เพราะ loop แบบเดียวกันใช้กับ research, finance, server administration, และ knowledge work อื่นได้.

**ได้อะไร:** pi เป็นการโต้กลับ harness ที่ฉลาดแต่เปลี่ยนใต้เท้าเรา. จุดขายไม่ใช่ feature เยอะ แต่คือความนิ่งและการดัดแปลงได้.

## Workflow จริง: caveman, แต่มีวินัย

Mario เรียกตัวเองว่า "absolute caveman" เพราะ workflow ของเขาไม่ได้เป็นกองทัพ agent อัตโนมัติ. งาน issue/bug เขาใช้ agent ทำ analysis ก่อน: อ่าน issue, reference code, PR ที่เกี่ยวข้อง, แล้วเสนอทางแก้หลายแบบ. เขาเปิดหลาย session เพื่อ preprocess issue ได้ แต่หลังจากนั้นเขาอ่านข้อเสนอ เข้า code เอง ทดลอง reproduce เอง และคุยกับ agent เหมือน rubber duck.

พอแผนเริ่มชัด context จะมี guardrail: interface ไหน, module ไหน, test แบบไหน, edge case ไหน. หลังจากนั้นค่อยให้ agent implement. เมื่อ agent เสร็จ เขา review diff, annotate line ที่มีปัญหา, ส่ง feedback กลับเข้า agent แล้ววนซ้ำ.

งาน critical เขายังอ่านเหมือน review คนจริง. งานทดลองหรือของเล่น เขาอาจ vibe code แล้ว manual test. แต่ถ้า prototype เริ่มมีคุณค่า เขาจะกลับมา refactor: แยก module, นิยาม boundary, ลอง API ด้วยมือ, แล้วให้ agent ทำงานที่มีกรอบชัด.

**ผลคือ:** agent เพิ่มความเร็วช่วง exploration และ implementation แต่ judgement ยังอยู่ที่คน. Workflow นี้เข้ากับ [[orchestration-tax|orchestration tax]] มากกว่า fantasy ว่าเปิด agent เยอะแล้ว output จะคูณตรง ๆ.

## Spec-driven development เป็น hyper-waterfall

บทสนทนาวิจารณ์ [[spec-driven-development|Spec-Driven Development]] แบบแรง. Mario มองว่าเราเหมือนลืมบทเรียน 30 ปีของ waterfall. ถ้า spec เป็น prose แล้วไม่ลงถึงระดับ code เอง agent ต้องเติมช่องว่าง. ช่องว่างนั้นมักถูกเติมด้วย pattern เฉลี่ยจาก internet ไม่ใช่ architecture ที่เหมาะกับระบบตรงหน้า.

เขายอมรับ counterargument ว่า AI ทำให้ turnaround ของ spec เร็วกว่ายุค waterfall มาก. จากเดือนอาจเหลือวันหรือชั่วโมง. แต่เขายังไม่เห็นหลักฐานชัดว่าวิธีนี้ใช้กับ production software ได้ดีโดยไม่ทิ้งหนี้ไว้.

**เปิดคำถาม:** SDD อาจมีที่ทางเมื่อ artifact ต้องให้คนข้ามทีม/กฎหมาย/ลูกค้าอ่าน. แต่ถ้าใช้แทนการคิด architecture และ verification มันเสี่ยงกลายเป็น vibe coding ที่ใส่สูทองค์กร.

## Code is never free

Mario ปฏิเสธการอ่านคำว่า "code is free" แบบสุดโต่ง. การ generate โค้ด 500,000 บรรทัดในหนึ่งสัปดาห์ไม่ได้แปลว่าได้ value. ถ้าไม่มีใครอ่านและ maintain ได้ มันคือการเลื่อนโทษไปข้างหน้า.

เขาแยกส่วนที่ agent มีค่าจริง: ตอนสำรวจ solution space. เมื่อการเขียนต้นแบบถูกลง เราสามารถลองหลาย architecture, หลาย API, หลาย path แล้วดูว่าทางไหนรู้สึกถูกต้องกว่า. แต่ผลจากการสำรวจไม่จำเป็นต้องเอาไปใช้ตรง ๆ. บางที value คือความเข้าใจที่ได้จากการลอง.

**ได้อะไร:** โค้ดราคาถูกมีประโยชน์เมื่อใช้เป็น probe เพื่อเรียนรู้. มันอันตรายเมื่อถูกนับเป็น asset ที่พร้อม merge.

## Async agent กับภาษีของสมอง

Mario เห็นข้อดีของ async agent สำหรับงานบางแบบ เช่น review, research, หรือ preprocessing issue. แต่ถ้าเปิดมากเกินไป context switching จะทำให้สมองพัง. เขาบอกว่าวันที่ดีมากอาจไล่แก้ issue ได้ 30 เรื่อง แต่ทำได้แค่เดือนละหนึ่งหรือสองครั้ง เพราะหลังจากนั้นสมองเละ.

เขาชอบ agent มากกว่าในฐานะ pair programmer: มีคนให้พูดปัญหาด้วย, ถาม Socratic question, และช่วยสำรวจ problem space. เหตุผลที่เขาไม่ชอบ "army of agents" คือมันดึงเขาออกจากการคิดเรื่องปัญหา.

**ผลคือ:** async เป็น feature ที่ดี แต่ต้องมี backpressure. ถ้าไม่มี มันกลายเป็น [[developer-balance|developer balance]] problem และ [[ai-brain-fry|AI Brain Fry]] แบบนักพัฒนา.

## Local AI เริ่มจริงขึ้น

Mario มองว่า local AI ยังไม่ consumer-ready เต็มที่ โดยเฉพาะ setup และ cost. แต่สำหรับงานบางชนิด model เล็กพอแล้ว. ตัวอย่างของเขาคือ toy robot สำหรับเด็กที่ใช้ speech-to-text, text-to-speech, และ LLM เล็กบน MacBook M1 ธรรมดา. เขาอ้างว่าชุดหนึ่งกิน unified memory ราว 14GB และใช้งานได้ดีพอสำหรับ chatbot ที่มีกล้องกับมอเตอร์.

เขาหวังว่า frontier model ขนาดใหญ่จะถูก distill ลงมาเหลือ model เล็กที่ยังเก็บ capability ส่วนใหญ่ไว้. เขายกตัวอย่าง open-weight/local direction เช่น Qwen, Gemma, DeepSeek V4 Flash, และ inference engine เฉพาะทาง.

**ได้อะไร:** local AI ไม่ได้ต้องแทน frontier model ทุกงาน. จุดแข็งคือ task ที่ latency/privacy/cost สำคัญ และ quality threshold ไม่ต้องถึง frontier.

## การเรียนรู้: friction ไม่ใช่ของเสียเสมอ

Mario เห็นด้วยว่าคนเรียนโปรแกรมต้องเจอ friction และ pain. ถ้า AI ตัดความเจ็บที่สร้าง mental model ออกไปหมด คนใหม่อาจเสียพื้นฐาน. แต่เขาแยก friction ที่สอนเราออกจาก friction ที่เป็นแค่งานประกอบ. ตอนเรียน electronics เขาให้ agent เขียน code MCU ที่เขาไม่อยากเรียนซ้ำ เพื่อเอาแรงไปเรียนวงจรจริง.

สำหรับ junior เขาไม่มีคำตอบง่าย. แรงกดดันในองค์กรทำให้ใช้ agent น่าสนใจมาก เพราะ junior ไม่อยากพลาด. แต่ถ้าใช้ก่อนมีพื้นฐาน ก็อาจคุม agent ไม่ได้.

**ผลคือ:** [[skill-atrophy|skill atrophy]] ไม่ได้แปลว่าห้ามใช้ AI. แปลว่าต้องถามว่า friction ตรงนี้กำลังสอนอะไร หรือแค่ขวางไม่ให้เรียนสิ่งที่อยากเรียน.

## Clanker load ใน Open Source

Mario เล่าว่าโปรเจกต์ open source ยุคก่อน agent อาจได้ PR หนึ่งถึงสองอันต่อสัปดาห์. ตอนนี้ [[pi-agent|pi]] เจอ PR จาก clanker วันละ 50-60 อัน แต่ละ PR มีคำอธิบายยาวมากและเปลี่ยนไฟล์ตั้งแต่ 10 ถึง 1,000 ไฟล์. หลายอันไม่เข้าใจปัญหาจริง หรือเป็น user error.

วิธีของเขาคือ auto-close PR โดยปริยาย แล้วให้คนเปิด issue สั้น ๆ ด้วยเสียงของมนุษย์ก่อน. ถ้า issue แสดงว่าเข้าใจปัญหาและทางแก้ เขาจะอนุญาตให้ส่ง PR และ workflow จะ whitelist account นั้น. Issues เองก็ถูก auto-close ก่อน แล้วเขาหรือ Armin ไล่อ่านย้อนหลังจาก marker เพื่อเปิดเฉพาะอันที่มีค่า.

**ได้อะไร:** open source maintainer ต้องมี intake protocol ไม่ใช่แค่ code review protocol. ประตูแรกคือพิสูจน์ว่าผู้ส่งเข้าใจปัญหา ไม่ใช่พิสูจน์ว่า agent สร้าง diff ได้.

## Security, trust, และ YOLO

pi ถูกวิจารณ์ว่าไม่มี permission prompt แบบละเอียด. Mario ตั้งใจให้คนเห็นว่า YOLO mode อันตราย แล้วไปออกแบบ sandbox/container ให้เหมาะกับ environment ของตัวเอง. เขามองว่า permission prompt บางแบบใน coding agent เป็น security theater เพราะ tool ไม่รู้ infrastructure ของผู้ใช้จริง และการให้ LLM ตัดสินว่า command ปลอดภัยอาจไม่พอ.

**เปิดคำถาม:** pi เลือกความซื่อตรงแบบ "นี่คือเครื่องมืออันตราย ต้อง sandbox เอง" ส่วน agent อื่นเลือก guardrail ในตัว. ทางไหนดีกว่าขึ้นกับ environment, threat model, และความสามารถของทีมในการทำ sandbox จริง.

## Token budget และราคา

ช่วงท้ายคุยเรื่อง token cost. Jan-Niklas ตั้งข้อสังเกตว่าบริษัทอาจเริ่มให้ budget AI ต่างกันตาม seniority. Mario คิดว่าราคา frontier model ไม่น่าลดลงง่าย โดยเฉพาะ subscription ที่ถูก subsidize. เขายังสงสัยว่าบาง vendor อาจเปลี่ยน tokenizer ทำให้ input เดิมนับ token มากขึ้น แม้ราคา per token ดูเท่าเดิม.

**ผลคือ:** workflow ที่ดีต้องมี cost discipline. "ใช้ Opus เพื่อ center div" อาจยังเกิดเพราะคนขี้เกียจสลับ model แต่ระยะยาวองค์กรจะถาม ROI มากขึ้น.

## ความเชื่อมโยงในวิกิ

- [[code-is-free]] — source นี้เพิ่ม caveat ว่า code generation ถูกลง แต่ code ownership ไม่ฟรี
- [[orchestration-tax]] — สนับสนุนฝั่ง review/context-switch เป็นคอขวดจริง
- [[spec-driven-development]] — เพิ่มคำวิจารณ์ SDD ว่าอาจเป็น hyper-waterfall
- [[clanker-slop]] — ให้ตัวเลขและ intake protocol จาก Pi
- [[developer-balance]] — ให้เรื่องเล่าหน้างานเรื่อง mental fatigue จาก agent หลายตัว
- [[open-weight-models]] — เพิ่มมุม local inference ที่พอใช้ได้กับงานขอบเขตชัด
- [[skill-atrophy]] — แยก friction ที่ช่วยเรียนกับ friction ที่ควร offload

## See also

- [[mario-zechner]]
- [[jan-niklas-wortmann]]
- [[earendil]]
- [[pi-agent]]
- [[claude-code]]
- [[code-is-free]]
- [[orchestration-tax]]
- [[spec-driven-development]]
- [[clanker-slop]]
- [[skill-atrophy]]
- [[open-weight-models]]
