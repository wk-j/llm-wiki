---
title: "Boris Cherny: We Cut 80% of Claude Code's Prompt"
type: source
author: Y Combinator
url: https://www.youtube.com/watch?v=qyPCVqFUyDo
date_ingested: 2026-09-10
tags: [ai, claude-code, opus-5, harness, prompts, evals, agents]
created: 2026-09-10
updated: 2026-09-10
sources: ["https://www.youtube.com/watch?v=qyPCVqFUyDo", "https://www.ycrootaccess.com/p/boris-cherny-building-claude-code"]
---

# Boris Cherny: We Cut 80% of Claude Code's Prompt / ทำไม Claude Code ตัด system prompt ออก 80%

[[boris-cherny|Boris Cherny]] (ผู้สร้าง [[claude-code|Claude Code]]) คุยกับ Diana Hu บนเวที [[y-combinator|Y Combinator]] Startup School 2026 หลังเปิดตัว [[claude-opus-5|Claude Opus 5]] ประเด็นหลักไม่ใช่เทคนิคเขียน prompt ให้คมกว่าเดิม แต่เป็นวิธีสร้าง AI product ตอน model เปลี่ยนเร็ว: ลบสิ่งที่เคยชดเชยข้ออ่อนของรุ่นเก่า ทดลองจากฐานที่เบาที่สุด แล้วเพิ่มกลับเฉพาะสิ่งที่ผลทดสอบบอกว่ายังจำเป็น

บทสรุปนี้อิง transcript ที่ผู้ใช้ส่งมา วันที่เผยแพร่วิดีโอยังไม่ได้ยืนยันจากหน้า YouTube และยังไม่ได้ตรวจ release note, system card หรือเอกสาร Claude Code ของ Opus 5 ดังนั้น claim เรื่องความสามารถ ความปลอดภัย คำสั่งทดลอง และจำนวน agent ทั้งหมดคงสถานะเป็นคำบอกเล่าของ Boris ในเวทีนี้

## Opus 5 เก่งขึ้นตรงไหน (0:21-3:19)

Boris ยกความเปลี่ยนแปลงสองเรื่อง เรื่องแรกคือ model รันงานได้นานขึ้นมาก โดยเฉพาะเมื่อใช้กับ auto mode เขาบอกว่างานอาจเดินต่อเป็นวัน สัปดาห์ หรือเดือนโดยไม่ต้องพึ่ง scaffolding เพิ่มเพื่อคอยสั่งให้ทำต่อ

เรื่องที่สองคือ prompt injection เขาอ้างว่าเมื่อนำสามชั้นมารวมกัน ทีมยังสาธิตการโจมตีให้สำเร็จไม่ได้:

1. model ที่ผ่าน alignment มาหลายปี
2. prompt-injection classifier ที่ดู activation ภายใน model จากงาน mechanistic interpretability
3. auto-mode classifier ที่คุม action ใน harness

คำว่า "cannot demonstrate prompt injection anymore" ไม่เท่ากับพิสูจน์ว่า prompt injection เป็นไปไม่ได้กับทุก input, tool และ deployment นี่เป็นผลที่ทีมรายงานจากระบบของตัวเอง ยังต้องอ่านคู่กับ [[agent-runtime-untrusted|หลักที่ถือ runtime เป็นส่วนที่เชื่อไม่ได้]] หลักนี้วาง sandbox, allowlist และ audit log ไว้นอก model ต่อให้ตัว model ดูต้านการโจมตีได้ดีขึ้นแล้วก็ตาม

**ได้อะไร:** model alignment ลดโอกาสพลาดได้ แต่ security boundary ที่ย้อนตรวจได้ยังควรอยู่ใน harness

## ทำไมตัด system prompt ออก 80% (3:19-6:37)

Claude Code ไม่ได้มี harness ชุดเดียวแล้วใช้กับ model ทุกรุ่น ทีมเปลี่ยน system prompt, tool set, tool prompt และ code รอบ model ทุกครั้งที่รุ่นใหม่ออก เพราะคำสั่งที่ช่วย model เมื่อสามเดือนก่อนอาจไม่ช่วยรุ่นปัจจุบัน หรืออาจกลายเป็นตัวขวางเสียเอง

สำหรับ Opus 5 คำสั่งจำนวนมากมีไว้แก้พฤติกรรมที่ model รุ่นก่อนควรทำได้แต่ยังทำไม่ได้ พอรุ่นใหม่ทำเองได้ ทีมจึงลบ system prompt ออกราว 80% Boris บอกว่าตอนทดสอบแบบ simple mode ทีมเอา prompt ทั้งของระบบและ tool ออก แล้ว model บางครั้งดูฉลาดขึ้นด้วย แต่ product จริงยังต้องเก็บคำสั่งบางส่วนไว้เพื่อกำหนด UX, permission และพฤติกรรมที่ผู้ใช้คาดหวัง

ทีมใช้ [[prompt-ablation|prompt ablation]]: ลบ prompt ทั้งก้อน แล้วนำกลับทีละบรรทัดพร้อมวัดผลว่าบรรทัดนั้นช่วยอะไรจริงหรือไม่ วิธีเดียวกันใช้กับ tool และ code ใน harness Boris บอกว่า code ที่เหลือใน Claude Code ตอนนี้หนักไปทาง safety, permission, static analysis และ UI ส่วน logic ที่พยายามคิดแทน model ถูกถอดออกไปมากแล้ว

Transcript ดูเหมือนพูดถึง flag สำหรับเปลี่ยน system prompt และ environment variable `CLAUDE_CODE_SIMPLE=1` แต่เสียงถอดคำสั่งเพี้ยน จึงไม่ควรใช้หน้านี้เป็นคู่มือ CLI จนกว่าจะตรวจเอกสารทางการ

**ผลคือ:** system prompt ไม่ใช่ทรัพย์สินที่ยิ่งสะสมยิ่งดี ทุกบรรทัดมีค่าใช้จ่ายทุกครั้งที่รัน และต้องพิสูจน์ประโยชน์ใหม่เมื่อ model เปลี่ยน

## สร้าง prompt ใหม่จาก failure ที่เกิดซ้ำ (6:37-9:16)

Boris แนะนำผู้สร้าง agent และผู้ใช้ Claude Code ให้ลองลบ `CLAUDE.md`, skills หรือ hooks เป็นระยะ แล้วดูว่ารุ่นใหม่ยังต้องพึ่งสิ่งเหล่านั้นไหม ขั้นต่อไปไม่ใช่นั่งเดาว่าควรเขียนกฎอะไร แต่คือใช้งานจริง ดูว่า model ทำอะไรได้ดี และจับจุดที่สะดุดกับ codebase หรือ architecture

เพิ่มคำสั่งกลับเมื่อเห็น model พลาดเรื่องเดิมซ้ำ ๆ เท่านั้น เพราะคำสั่งถาวรจะถูกอ่านทุก session วิธีนี้ทำให้การออกแบบ harness คล้ายการทดลองมากกว่าการออกแบบระบบครั้งเดียวแล้วคงไว้ยาว ๆ:

`delete → use → observe repeated failure → add one control → evaluate again`

คำแนะนำนี้ไม่ได้แปลว่าลบ guardrail ที่กันความเสียหายแบบ deterministic สิ่งที่ควรท้าทายก่อนคือคำสั่งและ scaffolding ที่คอยบอก model ว่า "ต้องคิดอย่างไร" ส่วน permission, sandbox, test และ audit trail มีหน้าที่คนละชั้น

**ได้อะไร:** กฎใหม่มาจาก failure ที่เห็นจริง ไม่ใช่ความกลัวล่วงหน้าหรือ habit จาก model รุ่นก่อน

## Eval อยู่ได้นานกว่า harness แต่ก็หมดอายุ (9:16-10:25)

ตอนถามว่าอะไรคงที่ข้าม model release Boris ตอบว่า eval มักอยู่ได้นานกว่า prompt และ harness แต่ไม่ได้ถาวร เขาประเมินคร่าว ๆ ว่า eval หนึ่งชุดอาจใช้ได้หนึ่งถึงสาม model generations ก่อน model ทำคะแนนเต็มหรือโจทย์ไม่สะท้อนจุดอ่อนใหม่ แล้วทีมต้องทิ้งหรือสร้างชุดยากขึ้น

แนวทางคือใช้ product กับ model จริง ดูว่า model พลาดตรงไหน แล้วสร้าง eval จาก failure เหล่านั้น จุดนี้ต่อกับ [[evals-and-error-analysis|evals และ error analysis]] โดยตรง: eval เป็นเครื่องมือค้นข้อจำกัดปัจจุบัน ไม่ใช่อนุสาวรีย์ของข้อจำกัดรุ่นเก่า

**ผลคือ:** ทั้ง prompt และ eval มี lifecycle เพียงแต่ eval มักเสื่อมช้ากว่า และควรเก็บไว้จนกว่าจะอิ่มตัวจริง

## Product overhang กับการเลิกขวาง model (10:25-19:45)

Boris ใช้คำว่า [[product-overhang|product overhang]] กับช่องว่างที่ model วันนี้ทำได้แล้ว แต่ยังไม่มี product เปิดทางให้ความสามารถนั้นออกมา ส่วน **hobbling** คือ product หรือ harness ใส่โครงบังคับมากจน model ทำสิ่งที่มันทำได้ไม่เต็มที่

Claude Code รุ่นแรกเกิดจากมุมนี้ ตอน Claude 3.5 Sonnet เก่งพอจะเขียนทั้ง function หรือทั้งไฟล์ แต่ผลิตภัณฑ์ส่วนใหญ่ยังให้ autocomplete ทีละบรรทัดหรือ chat แบบอ่านอย่างเดียว ทีมจึงให้ model เข้าถึง terminal และเขียนไฟล์ได้กว้างขึ้น แทนสร้าง IDE workflow ที่แบ่งขั้นไว้แน่น

วิธีหา overhang คือให้ [[model-elicitation|model elicitation]] เป็นงานทดลอง: มอบโจทย์ที่ยากกว่าที่คิดว่า model ทำได้เล็กน้อย ระบุ guardrail กับ exit criteria แล้วให้มันหาวิธีเอง Boris ยกทั้งงานที่มีเป้าธุรกิจ เช่น rewrite codebase และการเล่นที่ยังไม่มี use case ตรง เช่นให้ Opus 5 วาดภาพผ่าน OpenCV เพื่อดูว่าความสามารถอะไรซ่อนอยู่

**ได้อะไร:** โอกาสของ product ไม่ได้อยู่แค่รอ model รุ่นหน้า แต่อยู่ที่หา interface, tool และ verifier ที่เปิดความสามารถของ model รุ่นนี้

## Bun rewrite: prompt เดียวด้านบน แต่ข้างในมี workflow และ proof (15:35-18:25)

Boris เล่าเคส [[bun-in-rust|Bun rewrite จาก Zig เป็น Rust]] ว่า [[jarred-sumner|Jarred Sumner]] โยนโจทย์นี้ให้ model ใหม่ทุก generation จน Fable เริ่มทำได้ แล้วรัน dynamic workflow 11 วันจน codebase ใช้งานได้ใน production เขาเรียกว่า one prompt แต่ก็ชี้ว่ามี steering ระหว่างทาง และ test suite ของ Bun กับ Node.js ทำให้ model ตรวจผลได้

ต้นทางของทีม Bun ให้รายละเอียดมากกว่า: เตรียม `PORTING.md`, `LIFETIMES.tsv`, trial run, workflow ราว 50 ตัว, peak ประมาณ 64 Claudes, compiler queue, adversarial review, CI และ fuzzing สองคำอธิบายจึงไม่จำเป็นต้องขัดกันถ้าแยกระดับ: "one prompt" หมายถึงโจทย์ระดับบน ส่วน execution จริงมีโครงสร้างและ feedback จำนวนมาก

จุดที่ยังไม่ควรรวมคือ [[fable|Fable 5]] กับ [[claude-opus-5|Opus 5]] Boris บอกว่า Fable เริ่มทำ rewrite ได้ และ Opus 5 ก็น่าจะทำได้ ไม่ได้บอกว่าสองชื่อนี้คือ model เดียวกัน

**ผลคือ:** prompt สั้นทำงานใหญ่ได้เมื่อข้างใต้มี testable target ไม่ใช่เพราะรายละเอียดทั้งหมดหายไปจากระบบ

## งาน Swift ที่รันเกินสองสัปดาห์ (19:45-24:42)

Boris ทดลอง rewrite Claude Desktop จาก Electron เป็น Swift ผ่าน Claude ใน Slack เขาให้ access กับ macOS runner และ repo แล้วสั่งให้รัน app เดิมกับ app ใหม่ จับ screenshot เทียบ pixel ต่อ pixel และอย่าหยุดจนกว่าจะเสร็จ ตอนสัมภาษณ์งานยังรันอยู่หลัง 14-15 วัน และ agent สร้าง Slack channel เพื่อโพสต์ screenshot ความคืบหน้าเอง

เขาใช้เคสนี้ย้ำว่าคำสั่งที่ดีขึ้นในยุคนี้ไม่จำเป็นต้องยาวขึ้น สิ่งสำคัญคือให้โจทย์ยากพอและให้เครื่องมือที่ตรวจงานระหว่างทางได้ ถ้า model ขาด context ค่อยให้ MCP ถ้าพลาด pattern เดิมค่อยเพิ่ม prompt หรือ skill

คำว่า "ยังรันอยู่" เป็นหลักฐานเรื่อง duration ไม่ใช่หลักฐานว่า rewrite สำเร็จหรือพร้อม ship หน้านี้จึงไม่อัปเกรด demo ที่ยังไม่จบให้เป็นผลลัพธ์ production

## Dynamic workflows, loops และ routines (24:42-30:15)

[[dynamic-workflows|Dynamic workflows]] ให้ Claude แตกงานหนึ่งก้อนเป็นหลาย stage: fan-out ให้ agent ชุดแรกลงมือ แล้วให้ชุดถัดไปสรุป ตรวจ หรือ fan-out ซ้ำ Boris อธิบายว่าเป็น algebra สำหรับจัด agent แบบ sequence และ parallel ภายใน sandbox เพื่อเพิ่ม test-time compute อย่างมีโครงสร้าง

เมื่อถูกถามว่างาน Swift เปิดกี่ agent เขาไม่รู้ตัวเลขจริงและเดาว่าอาจเป็นหลักพันหรือหลักหมื่น จึงต้องเก็บเป็นการคาดเดา ไม่ใช่ telemetry

อีกแบบคือ loop กับ routine งานจะไม่แชร์ context ทุกครั้ง แต่อาจแชร์ memory และรันซ้ำตามเวลา เช่นทุกห้านาที ทุกชั่วโมง หรือทุกวัน ทีม Claude Code มี routine ราว 20-30 ตัวคอยหา dead code, ลบ experiment flag ที่ rollout ครบ, เติมหรือลบ test และรวม abstraction ที่ซ้ำกัน Boris บอกว่าระบบนี้ใช้ agent หลักร้อยถึงหลักพันต่อวัน และกำลังมุ่งไปสู่การดูแล app อัตโนมัติมากขึ้น

ตัวเลข scale ยังไม่ตอบว่า pull request เหล่านี้ถูก merge กี่ชิ้น ต้องใช้คนตรวจเท่าไร หรือ false positive มากแค่ไหน จึงต้องอ่านคู่กับ [[orchestration-tax|orchestration tax]] และ [[agentic-code-review|agentic code review]]

**ได้อะไร:** fan-out คุ้มเมื่อแต่ละ stage ลดข้อมูลให้เหลือ evidence ที่ตัดสินต่อได้ ไม่ใช่แค่สร้าง output เพิ่ม

## “Coding is solved” มีขอบเขต (30:15-34:47)

Boris จำกัดคำของตัวเองว่า coding ใกล้ถูกแก้สำหรับงานแบบที่เขาทำ ไม่ใช่ทุก codebase Model ยังติดกับ systems code ที่ลึก, distributed systems และ UI verification ที่คลาดแค่ไม่กี่ pixel คนที่ใช้ agent ได้ดีจึงต้องกล้าทิ้ง prior จากรุ่นเก่า ทดลองใหม่ และปรับจากผลจริง

สำหรับนักศึกษา เขาไม่ได้แนะนำให้ทิ้ง computer science แต่ให้เรียนผ่านปัญหาที่อยากแก้ แล้วเสริม design sense, business sense, data science และการคุยกับผู้ใช้ ความสามารถสร้าง code จะมีค่ามากเมื่อผูกกับการเลือกปัญหาและการตัดสินว่าอะไรควรสร้าง

## ข้อจำกัดและเรื่องที่ยังตอบไม่ได้

- วิดีโอเป็นบทสัมภาษณ์เปิดตัวจากผู้สร้างผลิตภัณฑ์เอง ไม่มี benchmark protocol, system card หรือ red-team report แนบใน transcript
- Claim ว่า prompt injection สาธิตไม่ได้แล้ว ยังไม่ใช่หลักฐานว่า attack surface ปิดครบ และไม่ควรใช้แทน sandbox, permission หรือ audit
- ตัวเลข 80% ไม่บอก token ก่อน-หลัง, ส่วนที่ถูกลบ หรือผล eval แยกตาม task จึงอ่านเป็นวิธีคิดมากกว่าตัวเลขที่นำไปเทียบผลิตภัณฑ์อื่นได้
- คำแนะนำให้ลบ `CLAUDE.md`, skills และ hooks เป็นการทดลอง ไม่ใช่คำสั่งให้ทิ้ง safety control พร้อมกัน ควรแยก behavioral prompt ออกจาก deterministic enforcement
- งาน Swift ยังไม่เสร็จตอนสัมภาษณ์ ส่วนจำนวน agent เป็นการเดาของ Boris เอง
- Routine ดูแล codebase อาจลดงานซ้ำ แต่ transcript ไม่บอก acceptance rate, defect rate, review load หรือ cost จึงยังสรุปไม่ได้ว่าแทนงานวิศวกรได้กี่คนจริง
- วันที่เผยแพร่วิดีโอและ syntax ของ simple mode ยังไม่ได้ยืนยันจากหน้า YouTube หรือเอกสารทางการ

## See also

- [[boris-cherny]]
- [[y-combinator]]
- [[anthropic]]
- [[claude-code]]
- [[claude-opus-5]]
- [[prompt-ablation]]
- [[model-elicitation]]
- [[product-overhang]]
- [[coding-harness]]
- [[evals-and-error-analysis]]
- [[dynamic-workflows]]
- [[long-running-agents]]
- [[agent-runtime-untrusted]]
- [[orchestration-tax]]
- [[bun-in-rust]]
- [[fable]]
