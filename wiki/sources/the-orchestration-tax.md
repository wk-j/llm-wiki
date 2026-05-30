---
title: "The Orchestration Tax"
type: source
tags: [ai, agents, productivity, attention, orchestration, concurrency, cognitive-debt]
created: 2026-05-29
updated: 2026-05-29
sources: [The Orchestration Tax.md]
---

# The Orchestration Tax / ภาษีค่าควบคุมวง

โพสต์บน X ของ [[addy-osmani|Addy Osmani]] (วิศวกร Google เขียนเรื่อง web performance + agent architecture) เมื่อ 28 พฤษภาคม 2026 ว่าด้วยปัญหาหนึ่งที่มากับยุค "เปิด AI agent กี่ตัวก็ได้" — พอเปิด agent ง่ายมาก คนเลยลืมไปว่า **เปิด agent เพิ่มไม่ได้แปลว่ามี "เรา" เพิ่ม**

แก่นของโพสต์: agentic workflow คือระบบ concurrent (ทำงานพร้อมกันหลายเส้น) อย่างหนึ่ง และในระบบนั้น **มนุษย์คือ component ที่ช้าที่สุดและทำงานทีละอย่าง (serial)** การ "ภาษีค่าควบคุมวง" (orchestration tax) คือราคาที่เราจ่ายเวลาลืมข้อนี้ ทางแก้จริงมีอย่างเดียว — **ออกแบบความสนใจ (attention) ของตัวเองให้เหมือนที่เราออกแบบระบบ concurrent**

แนวคิดหลักของโพสต์แยกออกมาเป็นหน้า concept: [[orchestration-tax]]

## ที่มา — panel ที่ Google I/O

Addy เล่าว่าเขาไปนั่ง panel ที่ Google I/O ร่วมกับ Richard Seroter, Aja Hammerly และ Ciera Jaspan คุยกันว่างาน software engineering ตอนนี้หน้าตาเป็นยังไงและจะวิวัฒน์ไปทางไหน ตอนใกล้จบ Richard ถามว่า "สิ่งหนึ่งที่อยากให้ developer กลับไปทำต่างจากเดิมคืออะไร" Addy ตอบสิ่งที่เขาคิดวนอยู่ในหัวมาหลายเดือน:

> **feeling busy is definitely not the same as being productive**
> (รู้สึกยุ่งไม่เท่ากับมี productivity จริง)

เขาขยายว่า "เปิด agent 20 ตัวแล้วรู้สึกยุ่งสุด ๆ ได้เลย แต่นั่นไม่ใช่งานที่ ship จริงเท่ากับ 20 agent"

ระหว่างคุย Richard เป็นคนตั้งชื่อปัญหานี้ว่า **"the orchestration tax"** และพูดประโยคที่ Addy ย้ำว่าโดนมาก:

> "You can't manage twenty agents successfully in your own brain."
> (คุณคุม agent ยี่สิบตัวให้สำเร็จในหัวตัวเองไม่ได้)

Addy เน้นว่านี่ **ไม่ใช่ปัญหาวินัย (discipline) แต่เป็นปัญหาเชิงสถาปัตยกรรม (architecture)** — และนั่นคือเหตุผลที่เขาอยากแกะให้ละเอียด

## the asymmetry people don't price in — ความไม่สมมาตรที่คนไม่คิดราคา

มีความไม่สมมาตรซ่อนอยู่ใน agentic workflow:

- **เปิด agent ถูกมาก** — แค่กดปุ่มหรือพิมพ์ประโยคเดียว
- **ปิดงาน agent (close the loop) แพงมาก** — ต้องมีคนเช็คว่าผลที่กลับมาถูกไหม แล้วเอาไปปรับให้เข้ากับงานที่ agent ตัวอื่นแก้ไปด้วย คนนั้นคือ "เรา" และมีเราอยู่คนเดียว

Addy เคยเขียนเรื่องนี้ส่วนหนึ่งไว้ในบล็อก ["Your parallel Agent limit"](https://addyosmani.com/blog/cognitive-parallel-agents/) เดือนก่อน เป็นเรื่องความกังวลคลุมเครือว่า "thread ไหนกำลังเงียบ ๆ พังอยู่" โพสต์นี้พูดเรื่อง **รูปร่างของต้นทุน** ที่อยู่ใต้ความกังวลนั้น พอมอง agent development เป็น concurrent system จะเห็นว่ามนุษย์เป็นแค่ component หนึ่งในระบบ — **เป็น component ที่ช้าและทำงานทีละอย่าง**

## you are the single thread resource — เราคือ resource ที่รันได้ทีละเส้น

ใครเคยเขียน concurrent code จะมี intuition ที่ถูกอยู่แล้ว แค่ชี้ผิดที่

**Python GIL** — Python มี Global Interpreter Lock (GIL) คือ lock ตัวเดียวที่ thread ต้องแย่งกันถือก่อนรัน bytecode จะเปิดกี่ thread ก็ได้ แต่รัน Python ได้ทีละ thread เพราะต้องถือ lock Addy บอกว่า **"เราคือ GIL ของ AI agent ของเรา"** — agent รันพร้อมกันได้หมด แต่พองานไหนต้องใช้ความเข้าใจสถาปัตยกรรมจริง ๆ หรือต้องแก้ merge conflict งานนั้นต้องมา "ถือ lock" และ lock มีตัวเดียว เราถือมันอยู่

**Amdahl's Law** — กฎที่บอกว่า speedup จากการขนานถูกจำกัดด้วย "สัดส่วนงานที่ยังต้องทำเป็น serial" ต่อให้เพิ่ม core เท่าไหร่ ถ้าส่วนหนึ่งขนานไม่ได้ ก็ตันที่เพดานนั้น ในงาน agent **สัดส่วน serial นั้นคือ judgement (การตัดสินใจ)** เปิด agent 8 ตัวไม่ได้ทำให้เวลาตัดสินใจเร็วขึ้น มันแค่ทำให้คิวของสิ่งที่รอป้อนเข้าสมองเรายาวขึ้น

> optimizing the non bottleneck part doesn't increase throughput
> (เร่งส่วนที่ไม่ใช่คอขวด ไม่ได้เพิ่ม throughput)

เพิ่ม agent คือการเร่งส่วนที่ไม่เคยเป็นข้อจำกัด ข้อจำกัดจริงคือขั้น review และ throughput ของทั้งระบบเท่ากับ throughput ของขั้นนั้นเป๊ะ ๆ **orchestration tax คือช่องว่างเชิงโครงสร้างระหว่าง "ของที่ agent ผลิตได้" กับ "ของที่เรา merge ได้จริง"** เกิดจากการเอา resource ที่รันทีละเส้นไปคุม resource ที่รันขนาน

(เชื่อมกับ [[theory-of-constraints]] และ [[local-optimization-trap]] ในวิกินี้โดยตรง)

## grinding won't fix structural limits — ขยันแค่ไหนก็ไม่ชนะข้อจำกัดเชิงโครงสร้าง

ที่ panel Addy พูดว่า "ไม่เคยรู้สึกว่า tool ทำให้ productive ขนาดนี้มาก่อน แต่ก็เหนื่อยกว่าที่เคยเหนื่อย" — ทั้งสองอย่างจริงและมีต้นเหตุเดียวกัน

ความเหนื่อยมาจากการรัน serial processor ที่ 100% ไม่มี slack เลย **ทุกครั้งที่ไปเช็ค agent ที่ทิ้งไว้ เราจ่าย context switch cost** — ต้อง flush สมองแล้วโหลด context อีกอันขึ้นมาจากศูนย์ CPU ทำสิ่งนี้ในไมโครวินาที (และ architect ยังพยายามเลี่ยง) แต่เราทำในหน่วยนาทีและโหลดกลับมาไม่เคยครบ "5 agent ไม่ใช่งาน 1 เท่าทำซ้ำห้ารอบ แต่คือ cold reload 5 ครั้ง บวกกับ process เบื้องหลังในสมองที่คอยกังวลว่าควรไปเช็คตัวไหน"

จะขยันฝืนแก้ข้อจำกัดเชิงโครงสร้างไม่ได้ ภาษีถูกเก็บอยู่ดี ถ้าฝืนกัดฟันทำ ข้อจำกัดจะโผล่มาในรูป **code review ที่ตื้นเขิน** หรือ **[[cognitive-surrender]]** — ภาวะที่เรายอมรับโค้ดของ agent เพราะการจะตั้งความเห็นของตัวเองมันกินความสนใจที่เราไม่เหลือแล้ว

> You either pay the tax deliberately or you let it quietly destroy your understanding of your own system.
> (จ่ายภาษีอย่างตั้งใจ หรือปล่อยให้มันค่อย ๆ ทำลายความเข้าใจที่เรามีต่อระบบของตัวเอง)

## architect your attention — ออกแบบความสนใจของตัวเอง

ต้องปฏิบัติกับ attention เหมือนเป็น serial resource ที่หายากอย่างที่มันเป็นจริง ๆ "เราไม่ออกแบบ distributed system โดยไม่คิดเรื่องคอขวด — ก็ให้เกียรติสมองตัวเองแบบเดียวกัน" Addy ลิสต์สิ่งที่ใช้ได้จริงกับเขา 5 ข้อ:

1. **Scale fleet to review rate, not the UI** — ระบบ concurrent ที่ดีใช้ backpressure ให้ producer ช้าลงมาเท่า consumer จำนวน agent คือ producer, review rate ของเราคือ consumer **จำนวน agent ที่ขนานได้ถูกต้องคือจำนวนที่เรา code review ได้ดีจริง ๆ** ซึ่งสำหรับคนส่วนใหญ่คือเลขหลักเดียว tool จะยอมให้เปิด 20 ตัว แต่นั่นเป็นแค่ฟีเจอร์ของ UI ไม่ใช่ capacity ของเรา

2. **Sort the work** — แยกงานเป็นสองกอง กองแรกคือ **งานแยกอิสระ (isolated)** ที่ส่งให้ background agent บน cloud รัน async ได้ ต้องการเราแค่ตอน gate สุดท้าย อีกกองคือ **งานที่ judgement คือเนื้องาน** เช่น bug แปลก ๆ หรือ architecture design ความผิดพลาดใหญ่คือพยายามขนานกองที่สอง — ทำงานยากหลายอันพร้อมกันไม่ได้เพิ่ม output แค่ทำให้ lock โดนแย่งจนทุกอย่างออกมาแย่ลง

3. **Batch your reviews** — context switch แพงทุกครั้ง รีวิว agent 4 ตัวในรอบเดียวถูกกว่าเช็คทีละตัวแล้วเดินไปทำอย่างอื่นแล้วกลับมาแบบ cold "ให้สายป่านยาวหน่อย ปล่อยงานกองได้นิด แล้วค่อยประมวลทั้ง batch"

4. **Only spend the lock on judgement** — อย่าเปลือง lock กับสิ่งที่เครื่องตรวจเองได้ ให้ agent เขียน test ที่ผ่านหรือ generate screenshot มาเอง มันพิสูจน์ส่วนน่าเบื่อ 80% ได้เอง เราจะได้เก็บความสนใจที่หายากไว้ใช้กับ 20% ที่ต้องการมนุษย์จริง ๆ (เชื่อมกับ [[behavioral-verifier]] และ [[model-honesty]])

5. **Protect your serial time** — คอขวดต้องการชั่วโมงที่ดีที่สุดของเรา ไม่ใช่เศษนาทีระหว่างเช็ค agent บางทีงานที่ leverage สูงสุดคือ **หยุด orchestrate ทั้งหมด ปิดเครื่องที่เต็มไปด้วย agent แล้วคิดเรื่องเดียวให้หนักโดยถือ lock ไว้ทั้งช่วง** — "orchestrating ไม่ใช่งานจริง มันคือ overhead รอบ ๆ งาน"

Aja ชี้ว่า **architecture คือทักษะเร่งด่วนตอนนี้** — รู้ว่าอะไรควรอยู่ใน agent ตัวเดียว อะไรใหญ่เกินไปสำหรับมัน Addy เสริมว่า "เราเป็น component หนึ่งในระบบนั้น attention ของเรามี serial throughput ที่รู้ค่าและต่ำ ระบบจะเคารพตัวเลขนั้น หรือไม่ก็จะอ้อมมันด้วยการแอบลดมาตรฐานของเราลงเงียบ ๆ"

## busy vs productive — ยุ่งกับ productive

จุดนี้สำคัญเพราะ **failure mode นี้มองไม่เห็นจากข้างใน** agent 20 ตัวที่กำลังรันให้ความรู้สึกว่า productivity มหาศาล dashboard เต็ม ทุกอย่างขยับ แต่ความรู้สึกนั้นหลุดจากการ ship โค้ดดี ๆ ขึ้น main เรายุ่งสุด ๆ และแทบไม่ได้ผลิตอะไรได้พร้อมกัน — จากข้างในมันรู้สึกเหมือนกันเป๊ะ

Ciera ชี้ไปที่ [งานเรื่อง cognitive debt ของ Margaret-Anne Storey](https://margaretstorey.com/blog/2026/02/09/cognitive-debt/) ในวงคุยกันถึง **technical debt** กับ **cognitive debt** orchestration tax ที่ไม่จ่ายคือวิธีสะสมหนี้ทั้งสองอย่างพร้อมกัน — เรา merge ของที่อ่านไม่ละเอียด, mental model ที่มีต่อโค้ดเบสค่อย ๆ เก่าและไม่ตรงจริง ทั้งหมดนี้ไม่โผล่บน dashboard วันนี้ มันโผล่ตอน production พังแล้วเรามองระบบแล้วพบว่า **ไม่รู้แล้วว่ามันทำงานยังไง** (เชื่อมกับ [[cognitive-debt]])

## บทสรุปจริงของโพสต์

> Spawning agents is not the skill. Anyone can run 20.
> (เปิด agent ไม่ใช่ทักษะ ใครก็เปิด 20 ตัวได้)

> **The real skill is designing the system around the one serial resource that cannot be cloned or parallelized. That resource is your attention.**
> (ทักษะจริงคือออกแบบระบบรอบ resource เดียวที่ clone หรือขนานไม่ได้ — resource นั้นคือความสนใจของเรา)

"Architect it the way you architect anything else you depend on in production." — ออกแบบมันเหมือนที่เราออกแบบทุกอย่างที่เราพึ่งพาใน production

## ทำไมเรื่องนี้สำคัญในวิกินี้

หน้านี้เป็น **น้ำหนักถ่วงฝั่งบริโภค (consumption side)** ของหลายหน้าที่พูดฝั่งผลิต (production side):

- [[subagent-patterns]], [[agent-swarm]], [[dynamic-workflows]] — เชียร์การเปิด subagent เป็นร้อย; orchestration tax เตือนว่าคอขวดมนุษย์ปลายทางไม่ scale ตาม
- [[long-running-agents]] (งานของ Addy เอง) — "Sort the work" + "give agents a long leash" คือเหตุผลเชิงปฏิบัติของ background/async agent กับ Mission Control inbox
- [[acceptance-bottleneck]] ของ ChrisZa และ [[theory-of-constraints]] — orchestration tax คือเรื่องเดียวกันเล่าด้วยภาษา concurrency

## See also

- [[orchestration-tax]]
- [[cognitive-surrender]]
- [[addy-osmani]]
- [[theory-of-constraints]]
- [[local-optimization-trap]]
- [[acceptance-bottleneck]]
- [[care-allocation]]
- [[cognitive-debt]]
- [[subagent-patterns]]
- [[long-running-agents]]
