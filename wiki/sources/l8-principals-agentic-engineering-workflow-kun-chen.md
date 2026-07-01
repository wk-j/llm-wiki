---
title: "L8 Principal's Agentic Engineering Workflow — Kun Chen"
type: source
tags: [ai-coding, agentic-workflow, harness, terminal, skills, validation, worktrees, orchestration]
url: https://www.youtube.com/watch?v=iQyg-KypKAA
date_ingested: 2026-07-01
created: 2026-07-01
updated: 2026-07-01
sources: ["user-provided transcript"]
---

# L8 Principal's Agentic Engineering Workflow / เวิร์กโฟลว์ Agentic Engineering ของ Kun Chen

วิดีโอนี้คือ walkthrough ของ [[kun-chen|Kun Chen]] (อดีต Meta L8/principal engineer และคนทำ coding-agent tooling หลายตัว) ว่าเขาจัดระบบทำงานกับ coding agents ยังไงให้ ship งาน production ได้เยอะโดยไม่หลุดคุณภาพ. ภาพเปรียบเทียบหลักคือ **captain + crew**: คนไม่ใช่ลูกเรือที่ลงไปพายเองทุกลำ แต่เป็นกัปตันที่จัดเรือ, ฝึก crew, ตั้งระบบตรวจ, แล้วเลือกทิศทาง.

แก่นของคลิปไม่ใช่ "ใช้ terminal เท่ ๆ" แต่คือการสร้าง operating system ส่วนตัวรอบ agent: terminal workflow, memory, skills, voice input, agent-friendly tools, interactive planning, validation pipeline, long-running loop, parallel worktrees, และ meta-agent ที่ช่วยคุมงานหลายสาย.

## เครื่องมือที่ประกอบเป็นเรือ

ช่วงแรก Kun อธิบายว่าทำไมเขาทำงานแทบทั้งหมดใน terminal. เหตุผลหลักมีสองข้อ: มือไม่ต้องออกจาก keyboard จึงไม่หลุด flow และ workflow เดิมใช้ได้ข้ามเครื่อง แม้กระทั่งจากโทรศัพท์.

Stack พื้นฐานคือ [[wezterm|WezTerm]] (terminal emulator ที่ config ด้วย Lua ได้), [[tmux]] (terminal multiplexer ที่แยก pane/window และ detach/reattach session ได้), และ [[neovim|Neovim]] (modal editor ที่ใช้ keyboard เป็นหลัก). สามตัวนี้ทำให้เขารัน editor, shell, และ agent หลายตัวพร้อมกันในพื้นที่เดียว.

**ได้อะไร:** terminal ไม่ใช่เป้าหมายเอง แต่เป็น surface ที่ทำให้ switching cost ต่ำพอจะคุม agent หลายตัวได้จริง.

## Harness ต้อง agent-agnostic

Kun ใช้หลาย agent harness: [[claude-code|Claude Code]], [[openai-codex|Codex CLI]], [[pi-agent|Pi]], และ [[opencode|OpenCode]]. เขาชมแต่ละตัวต่างกัน: Claude Code มี default ดี, Codex ลื่นและ open source, Pi minimal และ extensible, OpenCode model-agnostic และ TUI ดี.

แต่จุดสำคัญคือเขาพยายามทำ workflow ให้ **agent-agnostic**. เหตุผลง่ายมาก: model และ harness ที่ดีที่สุดเดือนหน้าอาจไม่ใช่ตัวเดิม. ถ้า workflow ผูกกับ tool เดียวมากเกินไป ทุกครั้งที่ landscape เปลี่ยน เราจะต้องย้ายระบบชีวิตใหม่.

ตรงนี้เสริมหน้า [[coding-harness|Coding Harness]] และ [[bitter-lesson|Bitter Lesson]]: ลงแรงกับสิ่งที่เราคุมได้ เช่น memory, skills, tests, worktrees, validation pipeline และ tool ergonomics แทนการฝากชีวิตไว้กับ model รุ่นเดียว.

## Memory files คือ onboarding ของ crew

Kun แบ่ง memory เป็นสองชั้น:

| ชั้น | เก็บอะไร | หลักคิด |
|---|---|---|
| Global memory | preference ส่วนตัวที่ใช้ทุก project | ต้องสั้น เพราะเข้า system prompt ทุก session |
| Project memory | repo layout, terminology, testing, conventions, failure lessons | เป็น collective learning ของ agent ใน project นั้น |

ตัวอย่าง global rule ที่เขาใส่คือ "อย่าให้น้ำหนัก development cost มากเกินไปตอนตัดสินใจทางเทคนิค." เขามองว่า model มักประเมิน cost แบบมนุษย์ เพราะ training data มาจากมนุษย์ เลยเลือก solution ที่ "ถูก" แต่คุณภาพต่ำ ทั้งที่ agent ทำ prototype ได้เร็วมาก.

อีก rule คือ bug fix ต้องเริ่มจาก reproduce แบบ end-to-end ใกล้ user experience จริงที่สุด ไม่ใช่กระโดดไปเขียน unit test ก่อน. นี่คือการแก้ bias ที่ model มักชอบ test เล็ก ๆ แต่ไม่พิสูจน์ behavior จริง.

**ได้อะไร:** memory file ไม่ใช่กอง handbook. มันคือ training record ที่เกิดจากการแก้ agent เมื่อทำผิดซ้ำ แล้วทำให้ agent รอบหน้าพลาดน้อยลง.

## Skills คือ progressive disclosure

Project memory มีโอกาสบวมขึ้นเรื่อย ๆ. Kun แก้ด้วยการย้ายความรู้ที่ใช้เฉพาะบางสถานการณ์ออกไปเป็น skill. ตัวอย่างเช่น E2E testing instructions ไม่ควรอยู่ใน memory ที่โหลดทุกครั้ง เพราะถ้าแค่ถามคำถาม มันเปลือง token เปล่า.

Skill ทำงานแบบ [[progressive-disclosure|progressive disclosure]]: ตอนเริ่ม session agent เห็นแค่ description สั้น ๆ ของ skill. ถ้าตัดสินใจว่าต้องใช้ จึงค่อยอ่านเนื้อเต็ม. นี่ทำให้เก็บ procedural knowledge ได้เยอะโดยไม่เป่า context window ทุกคำขอ.

Kun เตือนแรงว่าอย่าติดตั้ง skill มั่วจากอินเทอร์เน็ต. Skill สั่ง agent ให้รันอะไรก็ได้บนเครื่องได้ จึงเสี่ยงทั้ง secret leak และ performance regression. GitHub stars บอก popularity ไม่ได้บอก quality.

**ได้อะไร:** skill ที่ดีคือความรู้แบบ conditionally useful. Skill ที่แย่คือ prompt bloat หรือ security risk ที่ถูก package มาให้ดูน่าเชื่อถือ.

## Voice input และ agent ergonomics

Kun ย้าย prompt ส่วนใหญ่ไปใช้เสียงผ่าน [[open-superwhisper|OpenSuperWhisper]] (app ที่รัน Whisper local). เหตุผลคือการพูดเร็วกว่า typing มาก โดยเฉพาะ prompt ยาวที่อธิบาย intent. เขายัง tune transcription prompt ให้รู้จักชื่อ project/tool ที่ใช้บ่อย.

หลังจากนั้นเขาโยงไปที่ **agent ergonomics**: tool ที่ agent ใช้มีผลกับ token cost, latency, และ success rate. ตัวอย่าง GitHub access: เขาบอกว่า GitHub MCP ใช้ token และ latency มากกว่า CLI ใน benchmark ของเขา ส่วน [[axi|AXI]] คือชุด design standard/tooling ที่เขาทำเพื่อให้ output เป็นมิตรกับ agent มากกว่า เช่น token-efficient format แทน JSON.

**ได้อะไร:** ความเร็วของ agent ไม่ได้อยู่ที่ model อย่างเดียว. Interface ที่ agent ใช้กับโลกภายนอกเป็น bottleneck ได้เหมือนกัน.

## Planning ผ่าน artifact ไม่ใช่ wall of text

Kun ใช้ [[lavish|Lavish]] สำหรับงาน planning ซับซ้อน. แทนให้ agent พ่น plan เป็น text ยาว ๆ ใน terminal Lavish ให้ agent สร้าง HTML artifact ที่ใช้ design system ของ project จริง แสดง options, prototype, decision points, และรับ annotation ได้.

ตัวอย่างในคลิปคือการรวมปุ่ม "What I can do" กับ "My progress" ในแอปเด็กให้กลายเป็น achievement system. แบบ text อ่านยากและชี้ feedback ลำบาก. แบบ Lavish ทำให้เห็นภาพ UI, comment เฉพาะจุด, และเลือก decision ได้ทันที.

ตรงนี้เชื่อมกับ [[html-artifacts|HTML artifacts]] และ [[agent-experience|Agent Experience]]: medium ที่ดีลดงานตีความของคน และทำให้ feedback กลับไปหา agent ชัดขึ้น.

**ได้อะไร:** planning ที่ดีทำให้ requirement ชัดก่อน implementation. Agent กลางทางเลยทำงานยาวขึ้นโดยไม่ต้องเรียกคนบ่อย.

## Validation: อย่าให้ human review เป็นคอขวดเดียว

Kun บอกว่าตอน agent บอกว่า "done" คือจุดอันตราย. ถ้าทุก diff ต้องให้คนอ่านเอง velocity จะติดเพดานทันที. วิธีของเขาคือส่ง change เข้า [[no-mistakes|No Mistakes]] pipeline:

1. สร้าง branch/commit ถ้ายังไม่มี
2. รัน validation ใน worktree แยก
3. อ่าน session เพื่อเข้าใจ intent
4. rebase บน latest main และแก้ conflict ก่อน
5. ทำ adversarial review ใน context ใหม่
6. self-correct ปัญหาชัด ๆ และ escalate เรื่อง ambiguous ที่มีผล product
7. test แบบ end-to-end พร้อม evidence เช่น screenshot/video/log
8. update docs, lint, push branch, เปิด PR
9. babysit PR ต่อจน merge รวมถึง CI failure หรือ conflict ใหม่

คนยังต้องใช้ judgement ตอนท้าย แต่ไม่ได้อ่านทุกบรรทัดตั้งแต่แรก. เขาดู intent, evidence, risk assessment และเฉพาะ low-risk change บางประเภทอาจไม่อ่าน diff เลย.

**ได้อะไร:** นี่คือคำตอบเชิง process ต่อ [[orchestration-tax|Orchestration Tax]]: ใช้ automation เก็บ 80% ที่พิสูจน์ได้ แล้วเก็บ attention ของคนไว้กับการตัดสินใจจริง.

## Long-running loops: Good Night Have Fun

สำหรับงานที่ควรปล่อยยาว Kun ใช้ [[good-night-have-fun|Good Night Have Fun]]: ให้ objective + stop condition แล้ว agent จะวนทำจนจบหรือชน cap. ตัวอย่างคือให้ agent แกล้งเป็นเด็ก 7 ขวบ ใช้แอป High Bit end-to-end หา usability problem ตัวแรก, fix, แล้ววนซ้ำ.

งานที่เหมาะคือ objective ที่ verify ได้ หรืออย่างน้อย agent มี judgement พอ เช่น ลด page load time, เพิ่ม E2E test coverage, ทดลอง hypothesis เพื่อปรับ metric. เขาชอบ tool นี้มากกว่า `/goal` แบบทั่วไปเพราะตั้ง token cap, iteration cap, และ stop condition ได้ละเอียดกว่า.

**ได้อะไร:** human ใช้เวลาต้นทางกับปลายทาง. ตรงกลางปล่อย agent ทำงานยาว ถ้า objective และ gate ชัดพอ.

## Parallel worktrees: Treehouse

พอ agent ตัวหนึ่งรันอยู่ใน repo เดิม การเปิด agent อีกตัวใน directory เดียวกันจะเหยียบไฟล์กัน. Git worktree แก้ได้ แต่มี overhead: ต้องตั้งชื่อ, จำว่า worktree ไหนทำอะไร, cleanup เอง.

Kun ทำ [[treehouse|Treehouse]] เพื่อให้พิมพ์คำสั่งเดียวแล้วได้ fresh worktree. `treehouse status` ดูได้ว่าอันไหนใช้อยู่หรือ idle. ปิด tab แล้ว Treehouse รู้ว่า worktree ว่างและ reuse ได้.

ในคลิปเขาเปิดหลายงานพร้อมกัน: ปรับ voice input popover, เพิ่ม action แนบ screenshot, แก้ agent status bar. แต่ละงานอยู่คนละ worktree และควรตามด้วย No Mistakes ก่อนปิด.

**ได้อะไร:** worktree เอาการชนเชิงไฟล์ออก ส่วน Treehouse เอาหนี้ทางความจำของคนออก.

## First Mate: meta-agent ที่คุม crew

แม้มี tmux + Treehouse + No Mistakes แล้ว การคุยกับ agent ทีละตัวก็ยังเหนื่อย. Kun เลยทำ [[first-mate|First Mate]] เป็น meta-agent ที่รับคำสั่งระดับ captain แล้วไปจัดการ crew ให้เอง.

ตัวอย่างในคลิป: เขาบอก First Mate ให้เพิ่ม `update` command ใน CLI ของสาม project พร้อมกัน. First Mate แยกเป็นสาม task, เปิด tmux tabs, เรียก Treehouse สร้าง worktrees, รัน agent, แล้วใช้ No Mistakes gate จนพร้อม PR. ระหว่างรอ ยังดึง issue ล่าสุดของ Lavish AXI มาคุยและแตกงานใหม่ต่อได้.

ตรงนี้ใกล้ [[meta-harness|Meta-harness]] มาก แต่เป็นเวอร์ชัน personal workflow: common control layer เหนือ harness/worktree/validation pipeline.

**ได้อะไร:** คนเลิกเป็น dispatcher ที่ต้อง context-switch เอง แล้วกลับไปเป็นคนกำหนดทิศทาง.

## Captain's mindset

ตอนท้าย Kun บอกว่าเมื่อ First Mate จัดการ overhead ให้มากพอ bottleneck ใหม่จะกลายเป็น "เราคิดงานให้มันทำทันไหม". นี่คือสัญญาณว่าบทบาทเปลี่ยนแล้ว.

งานของ captain คือคุยกับ user, เข้าใจ competitive landscape, และสร้าง treasure map ที่บอก crew ว่าควรไปทางไหน. Agent ทำ tactical work ได้มากขึ้นเรื่อย ๆ แต่ vision, priority, product judgement, และ quality bar ยังเป็นงานของคน.

ตรงนี้เข้ากับ [[agentic-engineering|Agentic Engineering]] แบบเต็ม ๆ: professional leverage ไม่ได้มาจากการเปิด agent เยอะ แต่มาจากระบบที่ทำให้ agent ทำงานยาว ตรวจงานตัวเองได้ และเรียกคนเฉพาะตอนต้องใช้ judgement.

## ข้อสังเกต / Caveats

- วิดีโอนี้เป็น workflow ส่วนตัวของ solo builder/power user. การเอาไปใช้ในทีมใหญ่ต้องปรับ risk tier, compliance, ownership, และ review policy.
- Tool หลายตัวเป็นของ Kun เอง จึงควรอ่านเป็น field report + product philosophy ไม่ใช่ benchmark กลาง.
- แนวคิด "low-risk changes ไม่ต้องอ่าน diff" ใช้ได้ก็ต่อเมื่อ validation pipeline, evidence, และ historical calibration แข็งพอ. ใน codebase ที่ยังไม่มี harness ดี อันนี้เสี่ยง.
- Skill security เป็นจุดสำคัญ: skill ไม่ใช่แค่เอกสาร แต่เป็น instruction ที่อาจทำให้ agent รันคำสั่งบนเครื่อง.

## See also

- [[kun-chen]]
- [[agentic-engineering]]
- [[coding-harness]]
- [[agent-experience]]
- [[orchestration-tax]]
- [[agentic-code-review]]
- [[loop-engineering]]
- [[long-running-agents]]
- [[git-worktrees]]
- [[progressive-disclosure]]
- [[skill-procedures-vs-abilities]]
- [[html-artifacts]]
- [[meta-harness]]
- [[wezterm]]
- [[tmux]]
- [[open-superwhisper]]
- [[axi]]
- [[lavish]]
- [[no-mistakes]]
- [[good-night-have-fun]]
- [[treehouse]]
- [[first-mate]]
