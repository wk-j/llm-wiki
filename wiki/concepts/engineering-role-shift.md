---
title: Engineering Role Shift
type: concept
tags: [ai, software-engineering, career, roles]
created: 2026-04-15
updated: 2026-04-28
sources: [software-engineer-role-ai-era.md, llm-era-computer-engineering-nattee.md, aaron-levie-agent-automation-jobs.md, llm-era-computer-engineering-ep3-nattee.md]
---

# Engineering Role Shift / การเปลี่ยนขั้วของบทบาทวิศวกร

ข้อเสนอหลักคือ AI ไม่ได้ "ลบ" งานวิศวกรรมซอฟต์แวร์ทิ้ง แต่เป็นการ **กระจายงานออกจากส่วนกลาง** ของ pipeline การพัฒนาไปยังสองปลายทางแทน

## โครงสร้างทวิขั้ว (The Bimodal Shift)

งานวิศวกรรมซอฟต์แวร์แบ่งออกเป็นสามโซนที่เปลี่ยนแปลงไปในทิศทางที่ต่างกันภายใต้อิทธิพลของ AI:

-   **ต้นน้ำ (Upstream) — ขยายตัว:** งานที่เกี่ยวข้องกับการรวบรวม requirements, การตัดสินใจทางสถาปัตยกรรม, การกำหนดขอบเขตของปัญหา, และการวิเคราะห์โดเมน เวลาที่ใช้ในโซนนี้ *เพิ่มขึ้น* เนื่องจากประสิทธิภาพของ AI ขึ้นอยู่กับ spec ที่ได้รับ
-   **ตรงกลาง (Middle) — หดตัว:** งาน boilerplate, CRUD scaffolding, logic ทั่วไป, การจำ syntax, และการ refactor ที่ซ้ำซาก AI สามารถทำทั้งหมดนี้ได้
-   **ปลายน้ำ (Downstream) — ขยายตัว:** งาน code review, การประเมินผล, การตรวจสอบ, security auditing, และการควบคุมผลลัพธ์ของ AI เวลาที่ใช้ในโซนนี้ *เพิ่มขึ้น* เพราะผลลัพธ์ของ AI "ดูน่าเชื่อถือแต่อาจมีข้อผิดพลาดซ่อนอยู่"

ความสนใจของวิศวกรจึงถูกดึงไปยังสองปลายทางนี้พร้อมกัน

## กำแพงของ "เป็ด" ที่พังทลาย (The Shrinking Generalist Moat)

ข้อสังเกตจาก [[nattee-niparnan|Nattee Niparnan]] (Ep. 3, 2026-04-28): เดิมทีการเป็น **เป็ด (Generalist)** ที่รู้กว้างๆ ทำได้หลายอย่าง (Dev, Network, Infra, Ops) เคยเป็นจุดแข็งที่เป็น "Moat" (คูเมือง) ป้องกันตัวเองได้ แต่ในยุค AI คูเมืองนี้กำลังหายไปเพราะ:

- **AI ทำงานกว้างได้ดีกว่าคน**: งานที่เคยต้องใช้เวลาศึกษา (เช่น config Cisco/Huawei switch, เขียน Grafana dashboard, เซ็ต VM ใน Proxmox) ตอนนี้ AI สามารถทำแทนได้ทันทีด้วยคำสั่งเดียว
- **จุดแข็งกลายเป็นจุดอ่อน**: ความรู้ระดับผิวเผิน (พอทำได้) ไม่มีค่าตัวอีกต่อไป เพราะใครที่มี AI ก็ "พอทำได้" เหมือนกัน
- **ทางรอด**: ต้องเลือก "ลึก" ในบางด้านเพื่อสร้าง [[eh-gland|ต่อมเอ๊ะ]] ที่แข็งแรงพอจะคุม AI ในด้านนั้นๆ ได้ การรู้กว้างยังจำเป็นแต่ต้องใช้เพื่อ "ปิดจุดอ่อน" โดยมี AI เป็นตัวช่วย ไม่ใช่ใช้เป็นจุดขายหลักอีกต่อไป

## ทำไมส่วนกลางถึงหายไป

ส่วนกลางของงานซอฟต์แวร์คือส่วนที่:

1.  **มีปริมาณงานสูงและซ้ำซาก** — LLM เก่งในการจัดการกับ pattern ที่เกิดซ้ำๆ
2.  **มี spec ที่ชัดเจน** — เพียงแค่ ticket หรือ function signature ก็มี context เพียงพอ
3.  **ตรวจสอบได้ง่าย** — tests, compilers, type checkers สามารถจับข้อผิดพลาดส่วนใหญ่ได้

เงื่อนไขสามข้อนี้เหมาะสมกับสภาวะที่ LLM สามารถให้คำตอบที่ถูกต้องได้เร็วกว่ามนุษย์

## ทำไมสองปลายทางถึงขยายตัว

สองปลายทางนี้ต้านทาน automation ได้เพราะ:

-   **ต้นน้ำ** ต้องจัดการกับความกำกวม (ambiguity) และสื่อสารกับคน, เข้าใจ business context ที่ไม่ได้ระบุไว้, และทำการตัดสินใจ tradeoff ภายใต้ข้อมูลที่ไม่ครบถ้วน
-   **ปลายน้ำ** ต้องสังเกต *สิ่งที่ไม่ได้ปรากฏอยู่* — silent bug, architectural misfit, ช่องโหว่ด้านความปลอดภัย งานประเภทนี้ยากกว่าการ generate เพราะต้องใช้ mental model ที่ AI อาจไม่มี

ดู [[llm-coding-pitfalls]] สำหรับ taxonomy ของ [[andrej-karpathy|Karpathy]] เกี่ยวกับสาเหตุที่ผลลัพธ์ของ AI อาจมีข้อผิดพลาดซ่อนอยู่ — งาน Quality Gatekeeper ยังคงมีความสำคัญเพราะ failure mode เหล่านี้

## การประเมินค่าทักษะใหม่

| ทักษะที่มูลค่าลดลง | ทักษะที่มูลค่าเพิ่มขึ้น |
|---|---|
| การเขียน boilerplate | System design |
| การจำ syntax | การวิเคราะห์ปัญหา |
| Basic CRUD | ความรู้ในโดเมน |
| การ refactor ที่ซ้ำซาก | วิจารณญาณทางสถาปัตยกรรม |
| การเขียน routine test | การดีบักปัญที่ซับซ้อน |

เส้นเชื่อมร่วมกันคือ **judgment** และ **taste** ซึ่งมีมูลค่าเพิ่มขึ้น ในขณะที่ **recall** และ **throughput** มีมูลค่าลดลง

## ทฤษฎีหลักยิ่งมีความสำคัญมากขึ้น

ข้อสังเกตจาก [[nattee-niparnan|Nattee Niparnan]] (Ep. 2, 2026-04-17): วิชาพื้นฐาน — **Data Structure, Algorithm, Discrete Math** — **มีมูลค่าเพิ่มขึ้น** ในยุคของ Agent ไม่ใช่ลดลง เหตุผลคือวิชาเหล่านี้จะไม่ได้เป็นเพียง "ทฤษฎีบนกระดาน" แต่จะกลายเป็น **พื้นฐานในการตรวจสอบผลลัพธ์ของ AI** คุณจะไม่สามารถ "ตั้งคำถาม" กับ algorithm ที่ Agent เลือกได้เลยหากไม่เคยเรียนว่าทำไม Dijkstra ถึงใช้กับ negative weight ไม่ได้

> "ยิ่งมี Agent ยิ่งต้องแม่นเรื่องพวกนี้มากขึ้น ไม่ใช่น้อยลง" — Nattee

นี่คือภาพสะท้อนของส่วนกลางที่หายไป — ทักษะ *throughput* มีมูลค่าลดลง ในขณะที่ทักษะ *verification* มีมูลค่าเพิ่มขึ้น และสิ่งที่ปลดล็อกการ verification ได้คือความรู้ทางทฤษฎี [[taste-paradox]] อธิบายเพิ่มเติมว่า *ทำไม* ยังต้องเรียนด้วยวิธีเดิม แม้ว่า Agent จะเข้ามาทำงานในระดับผิวเผินแล้วก็ตาม

## Design choices ถูกผลักดันไปยัง junior

ข้อสังเกตที่สองจาก Nattee: การตัดสินใจเช่น *"เลือก framework ไหน ใช้ library อะไร ทำไมต้อง abstract แบบนี้"* เคยเป็นงานของ Senior Engineer แต่เมื่อ Agent เข้ามาจัดการ implementation layer **บัณฑิตใหม่จึงถูกผลักดันให้ต้องตัดสินใจเรื่อง architecture ที่ในอดีตต้องใช้เวลาหลายปีกว่าจะได้ทำ** ส่วนที่ขยายของต้นน้ำจึงตกเป็นภาระของวิศวกรที่มีประสบการณ์น้อยที่สุด ซึ่งทำให้ปัญหา [[taste-paradox]] รุนแรงขึ้น — เด็กใหม่ต้องใช้วิจารณญาณที่ยังสะสมไม่เพียงพอ ดู [[ai-orchestrator]] สำหรับกรอบความคิดเกี่ยวกับแรงกดดันนี้ในระดับระบบ

## บทบาทใหม่ที่เกิดขึ้น

การเปลี่ยนแปลงนี้ก่อให้เกิดบทบาทใหม่หกแบบ (ตามแหล่งข้อมูล):

-   [[ai-orchestrator]] — ผู้ควบคุม pipeline ของ AI agents (นิยามใหม่ของ senior developer)
-   Systems Architect — ผู้รับผิดชอบคำถาม *what* และ *why*
-   Quality Gatekeeper — ผู้ค้นหาสิ่งที่ AI พลาด
-   [[domain-to-ai-translator]] — ผู้เปลี่ยน requirement ที่คลุมเครือให้เป็น spec ที่สามารถ execute ได้
-   AI Tool Builder — ผู้สร้าง RAG, agent framework, [[model-context-protocol|MCP]] server, evals
-   Governance & Safety Owner — ผู้รับผิดชอบ compliance และ risk สำหรับระบบ AI
-   [[agent-enablement-role]] — เจ้าของการเอา agent ไปใช้กับ workflow จริงในองค์กร ([[aaron-levie|Levie]] บอกว่าจะเป็นการเติบโตที่ใหญ่ที่สุดในบริษัท non-tech)

## ดูเพิ่มเติม

- [[software-engineer-role-ai-era]]
- [[ai-orchestrator]]
- [[domain-to-ai-translator]]
- [[judgement-vs-automation]]
- [[ai-3d-workflow]]
- [[harness-engineering]]
- [[panutat-tejasen]]
- [[taste-paradox]]
- [[nattee-niparnan]]
- [[llm-era-computer-engineering-nattee]]
- [[llm-coding-pitfalls]]
- [[llm-knowledge-bases]]
