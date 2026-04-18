---
title: Engineering Role Shift
type: concept
tags: [ai, software-engineering, career, roles]
created: 2026-04-15
updated: 2026-04-18
sources: [software-engineer-role-ai-era.md, llm-era-computer-engineering-nattee.md]
---

# Engineering Role Shift / การเปลี่ยนขั้วของบทบาทวิศวกร

ข้อเสนอหลัก คือ AI ไม่ได้ "ลบ" งานวิศวกรรมซอฟต์แวร์ทิ้ง แต่ **กระจายงานออกจากตรงกลาง** ของ pipeline การพัฒนา ไปยังสองปลายแทน

## โครงสร้างทวิขั้ว (the bimodal shift)

งานวิศวกรรมซอฟต์แวร์แบ่งเป็นสามโซนที่แยกทิศทางกันภายใต้ AI:

- **ต้นน้ำ (upstream) — ขยาย:** งาน requirements gathering, architectural decisions, problem framing, domain analysis เวลาที่ใช้ในโซนนี้ *เพิ่มขึ้น* เพราะ AI จะทำงานได้ดีแค่ไหนขึ้นอยู่กับ spec ที่มันได้รับ
- **ตรงกลาง (middle) — หด:** งาน boilerplate, CRUD scaffolding, routine logic, การจำ syntax, refactor ซ้ำ ๆ AI ทำให้ได้หมด
- **ปลายน้ำ (downstream) — ขยาย:** งาน code review, evaluation, verification, security auditing, การควบคุม output ของ AI เวลาที่ใช้ในโซนนี้ *เพิ่มขึ้น* เพราะ output ของ AI "ดูมั่นใจแต่พังเงียบ ๆ"

ความสนใจของวิศวกรถูกดึงไปสองปลายพร้อมกัน

## ทำไมตรงกลางถึงหาย

ตรงกลางของงานซอฟต์แวร์คือส่วนที่:

1. **Volume สูงและซ้ำ ๆ** — LLM เก่งกับความถี่ของ pattern
2. **Spec ชัดเจน** — แค่ ticket หรือ function signature ก็มี context พอ
3. **Verify ง่าย** — tests, compilers, type checkers จับ error ส่วนใหญ่ได้

เงื่อนไขสามข้อนี้พอดีกับสภาวะที่ LLM ให้คำตอบถูกต้องได้เร็วกว่ามนุษย์

## ทำไมสองปลายถึงขยาย

สองปลายต้าน automation ได้เพราะ:

- **ต้นน้ำ** ต้องเจรจากับความกำกวม (ambiguity) กับคน เข้าใจ business context ที่ไม่ได้พูดออกมา และตัดสินใจ tradeoff ภายใต้ข้อมูลไม่ครบ
- **ปลายน้ำ** ต้องสังเกต *สิ่งที่ไม่ได้อยู่ตรงนั้น* — silent bug, architectural misfit, ช่องโหว่ security งานแบบนี้ยากกว่าการ generate เพราะต้องมี mental model ที่ AI อาจจะไม่มี

ดู [[llm-coding-pitfalls]] สำหรับ taxonomy ของ [[andrej-karpathy|Karpathy]] ว่าทำไม output ของ AI ถึงพังเงียบ ๆ — งาน Quality Gatekeeper ดำรงอยู่ได้ก็เพราะ failure mode พวกนี้

## การประเมินค่าทักษะใหม่

| ทักษะที่มูลค่าลดลง | ทักษะที่มูลค่าเพิ่มขึ้น |
|---|---|
| Writing boilerplate | System design |
| Memorizing syntax | Problem analysis |
| Basic CRUD | Domain knowledge |
| Repetitive refactoring | Architectural judgment |
| Routine test writing | Debugging complex issues |

เส้นเชื่อมร่วมกัน คือ **judgment** และ **taste** ทบต้น ส่วน **recall** และ **throughput** เฟ้อลงเรื่อย ๆ

## ทฤษฎีแกนยิ่งสำคัญมากขึ้น ไม่ใช่น้อยลง

ข้อสังเกตที่พลาดง่ายจาก [[nattee-niparnan|Nattee Niparnan]] (Ep. 2, 2026-04-17): วิชาแกนพื้นฐาน — **Data Structure, Algorithm, Discrete Math** — **มูลค่าเพิ่มขึ้น** ในยุค Agent ไม่ใช่ลดลง เหตุผลคือ วิชาพวกนี้จะเลิกเป็น "ทฤษฎีบนกระดาน" และกลายเป็น **substrate สำหรับ verify output ของ AI** คุณจะ "ต่อมเอ๊ะ" กับตัวเลือก algorithm ของ Agent ไม่ได้เลย ถ้าไม่เคยเรียนว่าทำไม Dijkstra ถึงใช้กับ negative weight ไม่ได้

> "ยิ่งมี Agent ยิ่งต้องแม่นเรื่องพวกนี้มากขึ้น ไม่ใช่น้อยลง" — Nattee

นี่คือภาพกระจกของตรงกลางที่หายไป — ทักษะ *throughput* เฟ้อ ทักษะ *verification* เพิ่มมูลค่า และสิ่งที่ปลดล็อก verification ได้คือทฤษฎี [[taste-paradox]] อธิบายต่อว่า *ทำไม* ต้องเรียนด้วยวิธีเดิมอยู่ดี ทั้งที่ Agent รับงานระดับผิวไปแล้ว

## Design choices ถูกดันลงสู่จูเนียร์

ข้อสังเกตที่สองจาก Nattee: การตัดสินใจแบบ *"เลือก framework ไหน ใช้ library ไหน ทำไมต้อง abstract แบบนี้"* เคยเป็นงานของ Senior Engineer แต่ Agent เข้ามายึด implementation layer ดังนั้น **บัณฑิตใหม่ถูกดันขึ้นไปตัดสินใจเรื่อง architecture ที่สมัยก่อนกว่าจะได้แตะต้องต้องผ่านงานหลายปี** ส่วนที่ขยายของต้นน้ำจึงไปตกที่วิศวกรที่มีประสบการณ์น้อยที่สุด ซึ่งทำให้ปัญหา [[taste-paradox]] ทบเข้าไปอีก — เด็กใหม่ต้องใช้ judgment ที่ยังสะสมไม่ทัน ดู [[ai-orchestrator]] สำหรับ framing ระดับระบบของแรงดันขึ้นนี้

## บทบาทใหม่ที่เกิดขึ้น

การเปลี่ยนขั้วนี้ก่อให้เกิดบทบาทใหม่หกแบบ (ตามต้นทาง):

- [[ai-orchestrator]] — คุม pipeline ของ AI agents (นิยาม senior developer ใหม่)
- Systems Architect — เจ้าของคำถาม *what* และ *why*
- Quality Gatekeeper — จับสิ่งที่ AI พลาด
- [[domain-to-ai-translator]] — เปลี่ยน requirement ฟุ้ง ๆ ให้กลายเป็น spec ที่ execute ได้
- AI Tool Builder — สร้าง RAG, agent framework, [[model-context-protocol|MCP]] server, evals
- Governance & Safety Owner — compliance และ risk สำหรับระบบ AI

## See also

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
