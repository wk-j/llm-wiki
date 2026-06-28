---
title: "Matt Pocock's Agentic Engineering Workflow (just copy him) — David Ondrej × Matt Pocock"
type: source
tags: [ai-coding, harness, agentic-workflow, skills, loops, afk, podcast]
url: https://www.youtube.com/watch?v=nQwJVHCtDDY
date_ingested: 2026-06-21
created: 2026-06-21
updated: 2026-06-21
sources: ["Matt Pocock’s Agentic Engineering Workflow (just copy him).md"]
---

# Matt Pocock's Agentic Engineering Workflow / เวิร์กโฟลว์ของ Matt Pocock

พอดแคสต์ระหว่าง [[david-ondrej|David Ondrej]] (ครีเอเตอร์สาย AI coding) กับ [[matt-pocock|Matt Pocock]] (ผู้สอน TypeScript และคนทำ skill repo ดังบน GitHub) เผยแพร่ 2026-06-19. แก่นของทั้งคลิปคือประโยคเดียว: **เลิกหมกมุ่นกับ model แล้วไปลงแรงกับ harness แทน** — เพราะ harness คือส่วนที่เราคุมได้จริง ส่วน model เป็นของที่ lab ปล่อยมาให้

Matt ใช้ [[claude-code|Claude Code]] + [[claude-opus-4-8|Opus 4.8]] effort `medium` เป็นหลัก และทำงานส่วนใหญ่แบบ **AFK (away from keyboard)** ผ่านเครื่องมือที่เขาสร้างเองชื่อ [[sandcastle|Sandcastle]]

## หมกมุ่นผิดที่: model vs harness

Matt เปิดด้วยอุปมา Formula 1: ทุกคนจ้องแต่ "เครื่องยนต์" (model) ทั้งที่เครื่องยนต์เป็นแค่ส่วนหนึ่งของรถ — ยังมีตัวถัง การลู่ลม ฯลฯ

> "Everyone's obsessed with the engine of the Formula 1 car whereas in fact the engine is really only a part of the whole system."
> (ทุกคนหมกมุ่นกับเครื่องยนต์ของรถ F1 ทั้งที่จริงเครื่องยนต์เป็นแค่ส่วนหนึ่งของระบบทั้งหมด)

ประเด็นคือ **เราคุม harness ได้มากกว่าคุม model** — เลือก prompt, เลือก skill, ปรับ environment, ปรับ codebase เองได้หมด. Matt บอกให้คิดเป็น 50/50 ไม่ใช่ model 90% + harness 10% อย่างที่คนส่วนใหญ่เชื่อ ดูกรอบเต็มที่ [[coding-harness]] และ [[matt-pocock-4-ai-terms]] (Matt เคยนิยาม Model / Harness / Environment / Agent ไว้)

**ของจริงข้อหนึ่ง:** อยากประหยัด token ให้ทำ codebase ที่แก้ง่ายเข้าไว้

> "How do you optimize for token spend? Have a code base that's easier to make changes in."

พอ codebase ดี guardrail ชัด agent ก็ explore ง่าย ไม่ต้องเอาหัวโขกกำแพงเปลือง token — แล้วก็ใช้ **model ที่ถูกกว่า/โง่กว่า** ทำงานเดิมได้. ถ้า hamstring (มัดมือมัดเท้า) agent ตั้งแต่วันแรก ก็ต้องไปพึ่ง model แพง ๆ

### David แย้ง + the bitter lesson

David แย้งว่าทำไมไม่ทำทั้งสองอย่าง — เปลี่ยนเครื่องยนต์ที่ดีกว่าเข้าไป ทุกอย่างก็ดีขึ้นทันที. Matt ยอมรับว่าจริง แต่ยกเรื่อง [[bitter-lesson|the bitter lesson]] (บทเรียนคลาสสิกใน ML ว่า raw compute ชนะการ optimize ด้วยมือเสมอ) มาเตือนตัวเองว่าเขาอาจกำลัง "ตกหลุม" ด้านกลับของ bitter lesson คือเอาแต่ขัด harness แทนที่จะรอ model ดีขึ้นเอง

จุดยืนสุดท้ายของ Matt: **"I'm not a pundit"** ไม่ทำนายอนาคต. ถ้ายึด software fundamentals ที่เวิร์กมา 30-40 ปี และพยายามทำ harness ให้ **agent-agnostic** (ไม่ผูกกับ model ตัวใดตัวหนึ่ง) ของพวกนี้ก็น่าจะเวิร์กต่อไปไม่ว่า model จะเปลี่ยนไปแค่ไหน. ถ้า over-optimize รอบ ๆ model ตัวเดียว จะเสีย focus จาก fundamentals

> ได้อะไร: อย่ารอ AGI เฉย ๆ (David เห็นด้วยว่าโง่) แต่ก็อย่าทุ่มทุกอย่างไปที่ model — ลงแรงกับสิ่งที่อยู่ในมือเรา คือ harness และ codebase

## Strategic vs tactical programming

Matt ยืม John Ousterhout (*A Philosophy of Software Design*) มาแยก [[strategic-vs-tactical-programming|tactical กับ strategic programming]]:

- **Tactical** = งานหน้างานรายวัน เขียนโค้ด แก้ syntax ไล่ bug ทำ commit
- **Strategic** = "ชนะสงคราม ไม่ใช่ชนะการรบ" — คิดยาว codebase ควรเป็นยังไง จะเพิ่ม velocity ของทีมยังไง

> "AI has basically eaten tactical programming. It's gone."
> (AI กินงาน tactical ไปหมดแล้ว)

เพราะ AI ทำ tactical ได้ถูกกว่าและเก่งกว่าเรา เราเลยต้องเก่ง **strategic** เพื่อคุมกองทัพ tactical programmer ไม่จำกัดจำนวนที่เพิ่งได้มา. หลักการ delegation เดิมยังใช้ได้หมด: ออกแบบส่วนยากไว้ก่อน, scope งานให้ชัด, คิดเรื่อง interface ระหว่าง module, เขียน test ดี ๆ, ทำ doc แค่พอชี้ทาง

**ทักษะของเราคือเพดานของ AI** — AI ทำให้ senior dev เก่งขึ้น 10 เท่า แต่ junior ได้แค่นิดเดียว เพราะ AI มี context ให้ทำงานเท่ากับที่เราป้อนให้ ถ้าทักษะเราต่ำ AI ก็ไปไม่เกินนั้น. ฉะนั้น "getting good with AI is really about getting good at your domain"

## Skills: procedures vs abilities

Matt มี skill repo ดังบน GitHub (`github.com/mattpocockuk/skills`, ติดตั้งด้วย `npx skills latest add`). เขาแบ่ง skill เป็นสองแบบ ดู [[skill-procedures-vs-abilities]]:

- **Procedures** = skill ที่ **เราสั่งเอง** อยากให้ model ทำตามขั้นตอน เช่น [[grill-me|grill me]], 2prd. เราถือพวงมาลัย
- **Abilities** = skill ที่ **model หยิบไปใช้เอง** เช่นไฟล์ coding standards ("เขียน React ห้ามใช้ useEffect")

Matt ชอบ **procedures** มากกว่า เพราะอยากเป็นคนคุม ไม่อยากยกการคิดให้ model. เหตุผลเชิงเทคนิคอีกข้อ: ทุก skill จะ **leak description เข้า context window** — มี 100 skill ก็ leak 100 บรรทัด. เขาเลยซ่อนความรู้พวกนี้ไว้ในหัวคน (developer) ไม่ใช่ในหัว AI และตั้ง `disable model invocation: true` กับ skill ที่ไม่อยากให้ leak. (เทียบ: skill repo `superpowers` ของ [[superpowers|Obra]] เลือกทางตรงข้าม — ให้ model เป็นคนคุม)

> "I don't want to delegate my thinking to the model."

**Grill me** เป็น procedure ที่เขาภูมิใจ: สั้นแค่ ~5 ประโยค เปลี่ยน agent เป็น "ผู้สัมภาษณ์ฝ่ายตรงข้าม" คอยซักจนเข้าใจตรงกัน. เขาใช้แทน plan mode. David เสริมเวอร์ชันของตัวเอง: "list out the 10 most consol decisions... interview me until you understand 98%"

## Knowledge / skills / wisdom

Matt (เคยเป็นครู 10 ปี) แยกสามอย่างที่ต้องมีถึงจะเก่งอะไรสักอย่าง ดู [[knowledge-skills-wisdom]]:

1. **Knowledge** — เข้าใจว่ามันคืออะไร
2. **Skills** — ทำมาหลายครั้งจนเป็น muscle memory
3. **Wisdom** — รู้ว่าควรทำตอนไหน ใช้กับโลกจริงยังไง — อันนี้ **เกือบเป็นไปไม่ได้ที่จะได้มาโดยไม่ลงมือทำในบริบทจริง** (อยากได้ wisdom แบบคนที่ Anthropic ก็ต้องไปอยู่ Anthropic)

ของที่ตื่นเต้นในยุคนี้คือ เราเอา knowledge + skills (สองข้อแรก) มามัดเป็น skill ที่ reuse และแจกทีมได้ — เหมือนดึง function ที่ซ้ำสามรอบออกมาเป็น shared function. ทุกคนในทีม plan แบบเดียวกันและช่วยกันปรับ skill นั้นให้ดีขึ้น = **ยกพื้น (raise the floor) ของทั้งทีม**

### The teach skill

Matt โชว์ [[teach-skill|teach skill]] ของเขา — เป็น **stateful skill** (เก็บ state ไว้ใน workspace local เหมือนครูที่จำได้ว่าเราเรียนอะไรไปแล้ว). ขั้นตอน: สร้าง `mission.md` ก่อน (อยากสร้างอะไร ทำไมถึงสำคัญ success คืออะไร) → ค้น trusted resources → สร้าง reference cheat sheet + บทเรียนเป็น **HTML** (เปิดในเบราว์เซอร์อ่านง่ายกว่า terminal) → มี quiz (เพิ่ม storage strength) → เก็บ learning record. อิงหลักการสอนจริง เช่น zone of proximal development. David ใช้สอนตัวเองแก้ Rubik's cube ได้

## Queues, not loops

David ถามเรื่อง agentic loop ที่ไวรัลบน Twitter. Matt ตอบว่าครึ่งหนึ่งเป็น "lab อยากขาย  token" (รันลูปตลอด = จ่ายเงินตลอด) ดู [[queues-over-loops]]:

ที่มาของลูปคือ **[[ralph|Ralph]]** ของ [[jeffrey-huntley|Jeffrey Huntley]] (14 ก.ค. ปีที่แล้ว) — `while` loop ที่ส่ง prompt เดิมให้ Claude Code ซ้ำ ๆ จนเสร็จ. แต่ Matt สรุปว่า **เขาไม่ได้ต้องการ "ลูป" จริง ๆ** สิ่งที่ต้องการคือ AFK agent มารับงานที่ scope แล้วไปทำให้จบ

> "The way I mostly think about these things as queues, okay, queues, not loops."

มองเป็น **queue (backlog ของงาน)** ดีกว่า: PM เติมงานเข้า queue, มีหลาย node (agent/dev) คอยหยิบงานออกไปทำ, งานหลุด queue เมื่อ PR merge. นี่คือวิธีที่ทีม dev ทำงานกันมาตลอด — ไม่ใช่ลูปเดียวที่วิ่งทำทุกอย่าง. ตัวอย่างจริง: Matt ใช้ GitHub issue ของ Sandcastle เป็น queue, ติด label `agent` ให้ agent ไป explore/implement เอง

> Matt ไม่ได้ปฏิเสธ loop engineering ทั้งหมด — เขาบอกว่า "ลูปมีประโยชน์ แต่ไม่ใช่ภาพทั้งหมด" และมุม queue ที่หยิบงานทีละชิ้นตรงกับการทำงานจริงมากกว่า

### AFK vs human-in-the-loop

Matt แยกงานสองแบบ ดู [[afk-agents]]:

- **Human-in-the-loop** — เราอยู่กับ agent คุยกันไป เหมาะกับ planning, งานซับซ้อน, งานที่ยัง unscoped
- **AFK (away from keyboard)** — โยนงานที่ scope แล้วให้ agent ไปทำเอง ไม่ต้องนั่งกดอนุมัติ

> "The moment that I discovered AFK was the moment I really got into AI coding."

พอออกจากลูปได้ ก็เหมือนมี "เรา" หลายคนทำงานขนานกัน → ผลิตโค้ดได้เยอะขึ้นมากแล้วค่อยมา review

## ดันจุด human-in-the-loop ไปทางขวา

คำถามคือเมื่อไหร่ค่อยถอด checkpoint ที่ต้องมีคนตรวจออก. Matt บอกให้ดันมันไปทาง production เรื่อย ๆ แต่ต้องเข้าใจว่า review ให้อะไรเราสองอย่าง:

1. **gate ของอันตราย** — กันของแย่ (security, โค้ดลับรั่ว) เข้า prod
2. **insight/observability เข้าระบบตัวเอง** — ดูว่าระบบทำงานยังไง เพื่อเอาไป **ปรับ harness** ให้ดีขึ้น

> "We're not just reviewing the code. We're also reviewing the system that produces the code."

ถ้าจะให้ AI ตัดสินว่า PR ไหนไม่ต้อง review — **"who reviews the AI that's doing that?"** ก็ต้องสุ่มเช็คงานที่ AI บอกว่า "ผ่าน" อยู่ดี แล้วค่อย ๆ ปรับปรุงไป

## Self-improving systems: "buy a lock"

David เล่าว่า Fable (ใน Cursor) เจอ security bug ลึก ๆ ที่ model อื่นมองข้าม. Matt ตอบว่าอย่าตื่นเต้นกับ model — **บทเรียนจริงคือ codebase เรามี security issue และเราควรมีระบบที่คอยเช็ก**

> "It's like if someone keeps stealing your bike, maybe buy a lock."
> (เหมือนถ้ามีคนขโมยจักรยานเราเรื่อย ๆ ก็น่าจะซื้อกุญแจล็อกซะ)

แทนที่จะให้ model แพง ๆ มาเจอ bug ลึก ๆ ให้รัน **cron job** ทุกวันที่ทำ security review ทีละส่วนของ repo ด้วย model ถูก ๆ + prompt/harness ที่ดี ก็เจอได้เหมือนกัน. เรา "lagging behind in our practices and expecting the model to just pick up the slack" — นี่คือสิ่งที่แยก "10x AI builder" ออกจากคนทั่วไป: ไม่ใช่แค่ "Fable เจ๋ง แก้ bug ให้หน่อย" แต่ถามว่า bug นี้เกิดได้ยังไง แล้วสร้างระบบกันไว้

## DX vs AX (Agent Experience)

Matt แยก **DX (developer experience)** กับ **AX (agent experience)** ดู [[agent-experience]]:

> "Agent experience is the experience that the agent has working in the codebase."

อะไรก็ตามที่ทำให้ agent ทำงานในโค้ดได้ดี — skill ดี, harness ดี, **และโดยเฉพาะ codebase ที่ดี (คนมักลืมข้อนี้)** — คือ AX ที่ดี. มี overlap สูงระหว่าง DX ดีกับ AX ดี → senior ที่สร้าง codebase ให้คนทำงานได้ดี ก็มักทำให้ agent ทำงานได้ดีด้วย. นี่คือเหตุผลที่ senior มีค่าในยุค AI

**ทำให้ review ลื่นขึ้น:** มีคนให้ AI อัดวิดีโอเดินผ่านโค้ดที่เปลี่ยน + เสียง TTS พากย์ทับ แปะไว้บน PR — review ได้เร็วขึ้นมาก. GitHub สร้างมานานแล้ว ไม่ได้ออกแบบมาเพื่อยุค agentic อาจต้องมี HTML surface ที่รู้จักเรา รู้ pattern ของ bug เก่า ๆ

## สร้างธุรกิจในยุค AI

Matt: ไม่มีอะไรเปลี่ยนเรื่อง fundamentals — คุยกับลูกค้า, หาว่าเขาต้องการอะไร, สร้าง prototype ที่แก้ปัญหาจริง. **AI ไม่ได้ช่วยเรื่องหาไอเดียที่ถูกต้อง** เพราะต้องออกไปคุยกับคนจริง. AI ห่วยเรื่องไอเดีย original. เราต้องเป็นเจ้าของ vision เอง

> "You should be asking AI what thing you can remove from your app."
> (ควรถาม AI ว่ามีอะไรที่เอาออกจากแอปได้บ้าง)

ถาม AI ว่าจะทำให้เรียบง่ายขึ้นยังไง ไม่ใช่ถามว่าควรเพิ่ม feature อะไร — กันแอปแบบ VC funded ที่มีพันฟีเจอร์จนหาของที่ต้องการไม่เจอ

## Junior vs senior / การจ้าง

- **Enthusiasm beats experience** ในแง่ output ล้วน ๆ — junior ที่ตื่นเต้นกับงานทำได้ดีกว่าคนมีประสบการณ์ เพราะเรียนรู้เร็ว
- คนที่มี **experimental mindset** + ตื่นเต้นกับ AI + สนใจ harness/AX → thrive ไม่ว่าจะ junior หรือ senior
- senior มีค่าเพราะรู้วิธีสร้าง DX ดี ซึ่ง overlap กับ AX
- ใครที่ยัง "เป็นแค่ tactical programmer ก้มหน้าทำงาน" — หายไปแล้ว ("you can't be a code monkey anymore")

## คำแนะนำปิดท้าย (action steps)

> "First thing I would do is I would delete every single skill, every single plugin, every single MCP server... delete your claude.md, delete your agents.md, go back to absolutely nothing, and then observe the agent."

1. **ลบทุกอย่างกลับเป็น blank slate** — skill, plugin, MCP, `CLAUDE.md`, `AGENTS.md` ทิ้งหมด แล้วดูว่า agent ทำอะไร. คนส่วนใหญ่ทำ context window บวมด้วย instruction มากเกินไป
2. **ค่อย ๆ layer กลับ** — เพิ่มทีละอย่างที่ **เราเลือกเอง** และให้เป็น **procedures** ไม่ใช่ abilities. คิดถึงอะไรค่อยเอากลับมา (เช่น brainstorming จาก superpowers)
3. **delegate implementation ให้ AFK agent** ให้มากที่สุด

## ข้อสังเกต / caveats

- เป็นพอดแคสต์เชิง opinion ของคนขายคอร์ส dev — Matt เองบอก "take my advice with a pinch of salt"
- มุม "queues not loops" กับ "loop engineering" ของ [[addy-osmani|Addy Osmani]] ไม่ได้ขัดกันแรง — Addy เองก็พูดเรื่อง maker/checker, state file, verifiable stop condition; Matt แค่เน้นว่า "ลูปเดียววิ่งทำทุกอย่าง" เป็นภาพที่ผิด ควรมองเป็น queue ที่หลาย node หยิบงาน ดู [[loop-engineering]]
- เรื่อง "ทำ cron + model ถูก ๆ ก็เจอ bug ลึกได้เหมือน model แพง" เป็น claim ที่ยังไม่มีหลักฐานวัดผล — เป็นจุดยืน harness-first มากกว่าผลการทดลอง
- Matt รอ ~1 เดือนก่อนรับ model ใหม่ (ทำแบบนี้ตอน Opus 4.5) ยังไม่ตัดสินใจเรื่อง Fable — มองว่า hype รอบ launch เป็น noise

## ดูเพิ่ม

- [[matt-pocock]]
- [[david-ondrej]]
- [[queues-over-loops]]
- [[afk-agents]]
- [[agent-experience]]
- [[strategic-vs-tactical-programming]]
- [[skill-procedures-vs-abilities]]
- [[knowledge-skills-wisdom]]
- [[bitter-lesson]]
- [[ralph]]
- [[teach-skill]]
- [[sandcastle]]
- [[coding-harness]]
- [[loop-engineering]]
- [[grill-me]]
- [[matt-pocock-software-fundamentals]]
- [[matt-pocock-4-ai-terms]]
