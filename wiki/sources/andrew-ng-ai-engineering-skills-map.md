---
title: The AI Engineering Skills Map — Andrew Ng
type: source
tags: [ai, careers, skills, software-engineering, coding-agents, evals]
created: 2026-08-15
updated: 2026-08-15
sources: [andrew-ng-ai-engineering-skills-map.md]
url: https://x.com/AndrewYNg/status/2088302050706686198
---

# The AI Engineering Skills Map — Andrew Ng / แผนที่ทักษะ AI Engineering

โพสต์บน [[x-twitter|X]] ของ [[andrew-ng|Andrew Ng]] (ผู้ก่อตั้ง [[deeplearning-ai|DeepLearning.AI]] คนที่สอนคอร์ส machine learning ให้คนทั้งโลกมาตั้งแต่ยุค Coursera) ประกาศสิ่งที่เขาเรียกว่า **The AI Engineering Skills Map** — แผนที่ที่พยายามตอบคำถามเดียวว่า ในกองข่าว AI ที่เสียงดังและ hype เยอะขนาดนี้ ทักษะไหนคุ้มค่าที่จะไปฝึกจริง ๆ

Ng บอกว่าแผนที่นี้มีคนใช้สองกลุ่ม: developer ที่ต้องเลือกว่าจะเรียนอะไรก่อน กับ employer ที่ต้องรู้ว่าจะจ้างคนแบบไหน

## เขาได้คำตอบมาจากไหน

Ng เล่าวิธีทำงานของทีมไว้สี่ทาง:

- วิเคราะห์ job posting กว่า 10,000 ประกาศ
- สัมภาษณ์แบบมีโครง (structured interview) หลายสิบครั้งกับผู้เชี่ยวชาญ AI, hiring manager และ recruiter
- เก็บข้อมูลผ่าน survey
- สังเคราะห์ข้อมูลออนไลน์อื่น ๆ เพิ่ม

> "You can informally think of our process as akin to running clustering on a massive dataset of jobs and expert interviews to identify the most important skills, not just today but also in the near future."

เขาเปรียบกระบวนการนี้แบบไม่เป็นทางการว่าเหมือนเอา dataset ก้อนใหญ่ของงานกับบทสัมภาษณ์มา run clustering เพื่อหาว่าทักษะไหนสำคัญที่สุด — ทั้งวันนี้และในอนาคตอันใกล้

**ได้อะไร:** คำตอบไม่ได้มาจากความเห็นคนเดียว แต่มาจากการรวมสัญญาณจากตลาดงานจริงกับคนที่จ้างจริง (ข้อควรระวังเรื่องความน่าเชื่อถือของตัวเลขอยู่ท้ายหน้า)

## หมายเหตุเรื่องคำ: "ทักษะ" ไม่ใช่ "ตำแหน่ง"

Ng ตั้งใจพูดว่า **AI Engineering skills** ไม่ใช่ **AI Engineer role** เพราะคำแรกกว้างกว่ามาก

เขาใช้ cloud เป็นตัวเทียบ: ทุกวันนี้ developer ทุกคนต้องรู้จักทำงานกับ cloud แต่คนที่มีคำว่า "Cloud engineer" อยู่ในตำแหน่งจริง ๆ มีน้อยกว่านั้นเยอะ AI ก็เหมือนกัน — full-stack engineer, data engineer, DevOps engineer, machine learning engineer และ AI engineer ทุกคนจะต้องมีทักษะชุดนี้

**ผลคือ:** อย่าอ่านแผนที่นี้เป็นคำอธิบายตำแหน่งงานเฉพาะทาง ให้อ่านเป็นพื้นฐานที่กำลังจะกลายเป็นเรื่องปกติของ developer ทุกสาย

## ทักษะที่ 1 — Building and deploying AI applications

ประเด็นเปิดของ Ng คือความต่างที่แท้จริงระหว่างแอป AI กับแอปธรรมดา: **output ของ AI เดาไม่ได้**

> "When you prompt an LLM, you don't know what you'll get back. When you train a deep learning algorithm, you don't know what prediction it will make on new examples. In contrast, traditional software behaves more predictably."

พอ prompt ตัว LLM เราไม่รู้ว่าจะได้อะไรกลับมา พอ train deep learning เราก็ไม่รู้ว่ามันจะทำนายอะไรกับตัวอย่างใหม่ ต่างจาก software แบบเดิมที่พฤติกรรมคาดเดาได้มากกว่า

คนที่เก่งด้านนี้ต้องรู้สองชั้น:

1. **ชิ้นส่วนพื้นฐานของ AI** — LLM, [[context-engineering|context engineering]] (การจัดสิ่งที่ model ต้องเห็นเพื่อทำงานให้ถูก), RAG (retrieval-augmented generation คือดึงเอกสารจริงมาแปะให้ model อ่านก่อนตอบ), agentic workflow, machine learning และ deep learning
2. **สถิติสำหรับวัด บังคับทิศ และกำกับระบบ AI** ให้พฤติกรรมนิ่งขึ้น

แล้ว Ng ก็ชี้เจาะจงลงไปว่าทักษะแกนกลางของข้อนี้คืออะไร:

> "A core skill in doing so is knowing how to drive disciplined evals and error analysis loops."

คือรู้วิธีขับ **[[evals-and-error-analysis|eval ที่มีวินัยกับ loop วิเคราะห์ error]]** ไม่ใช่แค่ลองไปเรื่อย ๆ แล้วรู้สึกว่ามันดีขึ้น

**ได้อะไร:** ของที่เดาผลไม่ได้ไม่ได้แปลว่าคุมไม่ได้ แต่ต้องคุมด้วยการวัดเป็นระบบ ไม่ใช่ด้วยความรู้สึก

## ทักษะที่ 2 — Software engineering fundamentals

ข้อนี้ Ng ยืนยันว่าพื้นฐานวิศวกรรมซอฟต์แวร์ไม่ได้หมดค่า มันสำคัญขึ้น

การทำ software ต้องแลกกันเสมอระหว่าง cost, scalability, reliability, speed แล้วยังมี security กับ privacy มาเพิ่มความยุ่งอีก ประเด็นของ Ng คือ **พื้นฐานทำให้เรามองเห็นว่ามี tradeoff อะไรอยู่บ้างตั้งแต่แรก** ซึ่งนำไปสู่การเลือก stack, ออกแบบ architecture, ออกแบบ data store และวางแผน test ที่ดีขึ้น

จุดที่คมที่สุดคือตอนเทียบกับคนที่ไม่มีพื้นฐาน:

> "It also leads to much better outcomes than those for an inexperienced developer who vibe codes a solution without knowing the tradeoffs their coding agent is making — which will often be poor ones, because they don't know what context to give their coding agent."

developer ที่ไม่มีประสบการณ์แล้ว [[vibe-coding|vibe code]] ออกมา มักได้ผลแย่กว่า เพราะไม่รู้ว่า coding agent กำลังตัดสินใจแลกอะไรกับอะไรอยู่ และไม่รู้ว่าต้องป้อน context อะไรให้มัน ตรงกันข้าม คนที่แม่นพื้นฐานจะ steer agent ได้ด้วย "ภาษาที่แม่นยำของ software engineering"

**ผลคือ:** พื้นฐานไม่ใช่ของเก่าที่ agent มาแทน แต่เป็นคำศัพท์ที่ใช้สั่ง agent ให้ตรงจุด

## ทักษะที่ 3 — Using coding agents

Ng บอกตรง ๆ ว่าการใช้ agentic coding ให้เป็นตอนนี้เป็นทักษะจำเป็นของ developer ทุกคนแล้ว

คนที่มีทักษะนี้จะมี mental model ว่า agent ทำงานยังไง รู้ข้อจำกัดและวิธีเลี่ยง และ steer ได้เร็ว — ที่สำคัญคือ **รู้ว่าควรเข้าไปแทรกแค่ไหน และควรปล่อยให้มันทำเองแค่ไหน** เพื่อให้ได้ software ที่แข็งแรงโดยไม่เผาเวลาและ token ทิ้ง

รายการย่อยที่ Ng ระบุไว้:

- จัดการ context ของ coding agent
- ชั่งน้ำหนักระหว่าง planning กับ execution
- ช่วยให้ agent ปิด loop ได้เอง ด้วยการให้ verifier หรือ eval
- ทำงานกับ spec ที่ชัด **และรู้ว่าเมื่อไหร่ไม่ต้องเสียเวลาเขียน spec**
- orchestrate agent หลายตัวให้ทำงานร่วมกัน
- เลี่ยงหลุมพราง เช่นความเสี่ยงที่ agent จะไปทำ production database พัง

ข้อสุดท้ายเป็นเรื่องจังหวะเวลา: agentic coding เปลี่ยนเร็วมาก การเก่งเรื่องนี้จึงไม่ใช่แค่รู้ท่าล่าสุด แต่ต้องมี **routine** ที่คอยลองเครื่องมือใหม่และปรับ workflow ตาม best practice ที่ขยับตลอด

**ได้อะไร:** ทักษะนี้วัดที่การควบคุม ไม่ใช่ที่จำนวน agent ที่เปิดได้

## ทักษะที่ 4 — Shaping the build

ข้อนี้เป็นข้อที่ท้าทายนิยามงานวิศวกรมากที่สุด

> "Given a clear spec, coding agents are rapidly improving at delivering to it. Thus, our work as engineers is shifting toward deciding what should be in the spec."

ถ้า spec ชัด agent ก็ทำตามได้ดีขึ้นเรื่อย ๆ งานของวิศวกรเลยขยับไปอยู่ที่ **การตัดสินว่าอะไรควรอยู่ใน spec** Ng พูดชัดว่าวิศวกรไม่ควรคาดหวังอีกต่อไปว่าจะมีคนส่ง design ที่เป๊ะทุก pixel มาให้แล้วเราแค่ implement การทำงานแบบนี้ต้องมี product sense เข้าใจ business context และเข้าใจเป้าหมายของลูกค้า เพื่อจะได้เข้าไปร่วม[[shaping-the-build|กำหนดรูปร่างของงาน]]

อีกครึ่งของข้อนี้คือ **ownership และ agency** AI เปิดโอกาสให้เรารับผิดชอบได้มากกว่าเดิม — มองหาปัญหาและโอกาสที่น่าสนใจเอง แล้วลงมือทำอย่างรับผิดชอบ ซึ่งต้องรู้วิธีดันโปรเจกต์ให้เดิน ตัวอย่างที่ Ng ยกคือรู้ว่าเมื่อไหร่ควรรีบทำ MVP ไปให้ user ลอง และเมื่อไหร่ควรช้าลงเพื่อสร้างให้รอบคอบกว่านั้น

**ผลคือ:** เมื่อการ implement ถูกลง สิ่งที่แพงขึ้นคือการตัดสินใจว่าจะสร้างอะไร

## สิ่งที่รองรับทั้งสี่ข้อ: continuous learning

Ng ปิดด้วยว่าใต้ทักษะทั้งสี่ข้อมี mindset เดียวรองรับอยู่ คือ **การเรียนรู้ต่อเนื่อง** เพราะ AI ยังเปลี่ยนเร็ว ทุกคนจึงต้องเรียนและปรับทักษะตาม best practice ที่โผล่ขึ้นมาใหม่

เขาบอกด้วยว่า DeepLearning.AI มีเป้าหมายหลักคือช่วยให้ developer ได้ทักษะชุดนี้ และจะทยอยเขียนโพสต์ลงรายละเอียดแต่ละข้อ พร้อมปล่อยแผนที่ฉบับละเอียดตามมา

## จุดที่ควรอ่านอย่างระวัง

- **ยังไม่มีรายงานฉบับเต็มให้ตรวจ** ณ วันที่ ingest โพสต์นี้เป็นการประกาศ ยังไม่ใช่เอกสารวิธีวิจัย ตัวเลข "over 10,000 job postings" และ "dozens of structured interviews" จึงเป็น first-party claim ที่ยังตรวจไม่ได้ ไม่รู้ว่าเก็บจากประเทศไหน ช่วงเวลาใด หรือคัดกรองอย่างไร
- **คำว่า clustering เป็นการเปรียบเทียบ** Ng เขียนเองว่า "informally think of our process as akin to running clustering" ดังนั้นอย่าอ่านว่ามีการรัน algorithm จริงแล้วได้ 4 cluster ออกมา
- **มีส่วนได้ส่วนเสีย** ผู้เขียนเป็นผู้ก่อตั้ง DeepLearning.AI และบอกในโพสต์เองว่าองค์กรโฟกัสที่การสอนทักษะชุดนี้ แผนที่จึงเป็นทั้งงานวิเคราะห์และการวางตำแหน่งสินค้าไปพร้อมกัน
- **ข้อสมมติเรื่อง spec** ประโยค "given a clear spec, coding agents are rapidly improving at delivering to it" ชนกับสายวิจารณ์ใน wiki นี้โดยตรง — [[llm-nondeterminism]] และ [[stop-writing-specs-start-writing-facts]] เถียงว่า spec เป็นคำทำนายพฤติกรรม model ไม่ใช่สัญญา ส่วน [[mario-zechner|Mario Zechner]] เตือนเรื่อง hyper-waterfall ดู [[spec-driven-development]] สำหรับข้อโต้แย้งทั้งสองฝั่ง wiki ยังไม่ตัดสินให้ฝ่ายใดฝ่ายหนึ่ง
- **มุมมองต่อโอกาส** โพสต์นี้เล่าฝั่ง "มีทักษะแล้วจะมีโอกาสเยอะ" ซึ่งไม่ขัดแต่ก็ไม่ครอบคลุมฝั่งที่ [[ai-work-intensification]] และ [[ai-brain-fry]] บันทึกไว้ ว่าองค์กรอาจเพิ่มความคาดหวังและปริมาณงานตามความเร็วที่ได้มา

## See also

- [[ai-engineering-skills-map]]
- [[evals-and-error-analysis]]
- [[shaping-the-build]]
- [[andrew-ng]]
- [[deeplearning-ai]]
- [[engineering-role-shift]]
- [[agentic-engineering]]
- [[context-engineering]]
- [[spec-driven-development]]
- [[matt-pocock-software-fundamentals]]
