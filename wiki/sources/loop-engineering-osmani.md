---
title: "Loop Engineering — Addy Osmani"
type: source
tags: [ai, agents, loops, harness, orchestration, automation, workflow]
created: 2026-06-09
updated: 2026-06-09
sources: ["Loop Engineering..md"]
---

# Loop Engineering — Addy Osmani

บทความ/โพสต์ X ของ [[addy-osmani|Addy Osmani]] (วิศวกร Google) เผยแพร่ 2026-06-09 ([x.com/addyosmani](https://x.com/addyosmani/status/2064127981161959567)). หัวใจของมันสรุปได้ประโยคเดียว:

> **Loop engineering is replacing yourself as the person who prompts the agent. You design the system that does it instead.**
> (loop engineering คือการ *ถอดตัวเองออก* จากตำแหน่งคนที่คอยพิมพ์ prompt ให้ agent แล้วไปออกแบบ "ระบบ" ที่ทำหน้าที่นั้นแทน)

> **A loop here can be thought of a recursive goal where you define a purpose and the AI iterates until complete.**
> (ลูปในที่นี้ = เป้าหมายแบบวนซ้ำ เรากำหนด "จุดประสงค์" ไว้ แล้ว AI วนทำจนกว่าจะเสร็จ)

Addy บอกเองว่ายัง early และเขายัง skeptical — ต้องระวัง **token cost** (คนที่ token เยอะกับ token น้อยจะเจอ pattern ต่างกันมาก) และเรื่อง **คุณภาพ/slop** ก็ยังเป็นข้อกังวลจริง แต่เขาเชื่อว่านี่อาจเป็น "อนาคตของวิธีที่เราทำงานกับ coding agent"

หน้านี้สรุปตามโครงของบทความ. แก่นความคิดที่ดึงออกมาเป็นหน้าแยกอยู่ที่ [[loop-engineering]] และ [[git-worktrees]]

## ใครพูดอะไร — ที่มาของไอเดีย

บทความเปิดด้วยคำพูดสองคนที่จุดประเด็นนี้:

- **[@steipete](https://x.com/steipete)** (Peter Steinberger): *"You shouldn't be prompting coding agents anymore. You should be designing loops that prompt your agents."*
- **[@bcherny](https://x.com/bcherny)** (Boris Cherny หัวหน้า Claude Code ที่ Anthropic): *"I don't prompt Claude anymore. I have loops running that prompt Claude and figuring out what to do. My job is to write loops."*

Addy วางตำแหน่งของ loop engineering ว่าอยู่ **ชั้นบน** ของสองเรื่องที่เขาเขียนไว้ก่อน:

- [[agent-harness-engineering]] — การออกแบบ *สภาพแวดล้อมที่ agent ตัวเดียวรันอยู่ข้างใน*
- factory model — *ระบบที่สร้างซอฟต์แวร์* (โรงงาน)

> Loop engineering sits one floor above the harness. The harness but it runs on a timer, it spawns little helpers, and it feeds itself.
> (loop engineering อยู่สูงกว่า harness หนึ่งชั้น — มันคือ harness ที่ *รันบน timer*, *แตก helper ตัวเล็ก ๆ ออกไป*, และ *ป้อนงานให้ตัวเอง*)

จุดที่ Addy แปลกใจ: นี่ไม่ใช่เรื่องของ tool แล้ว. เมื่อปีก่อนถ้าอยากได้ลูปต้องเขียน bash กองโตแล้วดูแลมันเอง. ตอนนี้ชิ้นส่วนมันมากับตัวผลิตภัณฑ์เลย — list ของ Steinberger map เกือบเป๊ะกับทั้ง Codex app และ Claude Code. **พอเห็นว่ารูปร่างมันเหมือนกัน ก็เลิกเถียงว่าใช้ tool ไหน แล้วออกแบบลูปที่ยังทำงานได้ไม่ว่าจะนั่งอยู่ใน tool ตัวไหน**

## ห้าชิ้น + memory

ลูปต้องการ 5 ชิ้น แล้วก็อีกหนึ่งที่ไว้จำของ:

1. **Automations** — รันตามตารางเวลา ทำ discovery + triage เอง
2. **Worktrees** — ให้ agent สองตัวทำงานขนานกันได้โดยไม่เหยียบไฟล์กัน
3. **Skills** — เขียนความรู้เกี่ยวกับโปรเจกต์ลงไป แทนที่จะให้ agent เดาเอง
4. **Plugins & Connectors** — เสียบ agent เข้ากับเครื่องมือที่เราใช้อยู่จริง
5. **Sub-agents** — ให้ตัวหนึ่งคิด อีกตัวตรวจ

ชิ้นที่หก คือ **memory**: ไฟล์ markdown, บอร์ด Linear, หรืออะไรก็ได้ที่อยู่ *นอก* บทสนทนาเดียว และเก็บว่า "อะไรเสร็จแล้ว / อะไรค้างอยู่"

> Sounds too dumb to matter. But it's the same trick every long running agent depends on... the model forgets everything between runs so the memory has to be on disk and not in the context. The agent forgets, the repo doesnt.
> (ฟังดูง่ายเกินจะสำคัญ แต่มันคือกลเดียวกับที่ [[long-running-agents|long-running agent]] ทุกตัวพึ่งพา — โมเดลลืมทุกอย่างระหว่างรอบ memory เลยต้องอยู่บนดิสก์ ไม่ใช่ใน context. **agent ลืม แต่ repo ไม่ลืม**)

Addy ย้ำว่าทั้ง Claude Code และ Codex มีครบทั้งห้าแล้ว ชื่อต่างกันบ้างแต่ความสามารถเหมือนกัน

## Automations — หัวใจที่เต้น (the heartbeat)

Automations คือสิ่งที่ทำให้ลูปเป็น "ลูป" จริง ไม่ใช่แค่รันครั้งเดียวจบ

- **Codex app**: สร้างใน Automations tab เลือก project, prompt, ความถี่, และรันบน local checkout หรือ background worktree. รอบที่เจออะไรไป Triage inbox, รอบที่ไม่เจอก็ archive ตัวเองทิ้ง. OpenAI ใช้ภายในกับงานน่าเบื่อ เช่น daily issue triage, สรุป CI failure, เขียน commit briefing, ตามล่า bug ที่เพิ่งใส่เข้าไปอาทิตย์ก่อน. **automation เรียก skill ได้** — ยิง`$skill-name`แทนการ paste กำแพงคำสั่งยาว ๆ ลงตารางที่ไม่มีใครกลับมาอัปเดต
- **Claude Code**: ไปถึงจุดเดียวกันผ่าน scheduling + hooks — `/loop` รัน prompt/command ตาม interval, cron task, hook ยิง shell command ตามจังหวะ lifecycle ของ agent, หรือดันทั้งอย่างขึ้น GitHub Actions ให้รันต่อหลังปิดเครื่อง

มี primitive ใน session อีกตัวที่ใกล้แก่นบทความที่สุด:

- **`/loop`** — รันซ้ำตาม cadence (จังหวะเวลา)
- **`/goal`** — วิ่งต่อจนกว่าเงื่อนไขที่เราเขียนจะเป็นจริง. **หลังทุก turn มี model เล็กแยกต่างหากมาเช็คว่าเสร็จหรือยัง — ตัวที่เขียนโค้ดไม่ใช่ตัวที่ให้เกรด.** เช่นบอกว่า "all tests in test/auth pass and lint is clean" แล้วเดินจากไปได้. Codex ก็มี `/goal` เหมือนกัน วิ่งข้าม turn จนกว่าเงื่อนไขหยุดแบบ verify ได้จะเป็นจริง มี pause/resume/clear

> So this is the part that surfaces the work. The rest of the loop is what acts on it.
> (Automations คือส่วนที่ *ทำให้งานโผล่ขึ้นมา* ส่วนที่เหลือของลูปคือส่วนที่ลงมือทำกับงานนั้น)

## Worktrees — กันขนานไม่ให้กลายเป็นความวุ่นวาย

พอรัน agent มากกว่าหนึ่งตัว ไฟล์เริ่มชนกัน — เหมือน engineer สองคน commit ทับบรรทัดเดียวกันโดยไม่คุยกันก่อน. [git worktree](https://git-scm.com/docs/git-worktree) แก้เรื่องนี้: working directory แยก บน branch ของตัวเอง แชร์ประวัติ repo เดียวกัน → edit ของ agent ตัวหนึ่งแตะ checkout ของอีกตัวไม่ได้เลย

- **Codex**: build worktree support มาในตัว
- **Claude Code**: `git worktree` + flag `--worktree` เปิด session ใน checkout ของตัวเอง + setting `isolation: worktree` ติดบน subagent ให้ helper แต่ละตัวได้ checkout สดที่ล้างตัวเองหลังเสร็จ

> the worktrees take away the mechanical collision but YOU are still the ceiling, your review bandwith decides how many you can actually run, not the tool.
> (worktree เอา *การชนกันเชิงกลไก* ออกไปก็จริง แต่ **เพดานยังคือตัวเรา** — review bandwidth ของเราเป็นตัวกำหนดว่ารันได้กี่ตัวจริง ไม่ใช่ tool)

ตรงนี้คือ [[orchestration-tax|orchestration tax]] ที่ Addy เขียนไว้ก่อน — แยกเป็นหน้า [[git-worktrees]]

## Skills — เลิกอธิบายโปรเจกต์ใหม่ทุกครั้ง

Skill คือวิธีหยุดอธิบาย context ของโปรเจกต์ซ้ำทุก session เหมือนปลาทอง. ทั้งสอง tool ใช้ format เดียวกัน: โฟลเดอร์ที่มี `SKILL.md` (instruction + metadata) แล้วมี script/reference/asset เสริมได้

- **Codex**: รัน skill ตอนเรียกด้วย`$`หรือ`/skills`หรือรันเองเมื่อ task ตรงกับ description ของ skill — เหตุผลที่ description ที่ "น่าเบื่อแต่ตรง" ชนะ description ที่ฉลาด
- **Claude Code**: ทำเหมือนกัน

Skill = จุดที่ **intent หยุดเสียเงินซ้ำ ๆ**. Addy อ้างแนวคิด intent debt ของตัวเอง: agent เริ่มทุก session แบบเย็นชืด และจะเติม "ช่องว่างของ intent" ด้วยการเดาอย่างมั่นใจ. skill คือ intent ที่เขียนไว้ข้างนอก — convention, ขั้นตอน build, "เราไม่ทำแบบนี้เพราะเหตุการณ์ครั้งนั้น" — เขียนครั้งเดียวที่ agent อ่านทุกรอบ. **ไม่มี skill ลูปจะ re-derive โปรเจกต์ทั้งหมดจากศูนย์ทุกรอบ มี skill มันค่อย ๆ compound**

ข้อต้องแยกให้ชัด: **skill คือ format สำหรับ "เขียน" ส่วน plugin คือวิธี "ส่ง"** — อยากแชร์ skill ข้าม repo หรือมัดหลายตัวเข้าด้วยกันก็แพ็กเป็น plugin จริงทั้งใน Codex และ Claude Code

## Plugins & Connectors — ลูปแตะเครื่องมือจริงของเรา

ลูปที่เห็นได้แค่ filesystem คือลูปจิ๋ว. **Connectors สร้างบน [[model-context-protocol|MCP]]** ให้ agent อ่าน issue tracker, query database, ยิง staging api, ส่งข้อความเข้า Slack. Codex และ Claude Code พูด MCP ทั้งคู่ → connector ที่เขียนให้ตัวหนึ่งมักใช้กับอีกตัวได้เลย. **plugin มัด connector + skill เข้าด้วยกัน** ให้เพื่อนร่วมทีมติดตั้ง setup ของเราในก้าวเดียว

> This is the difference between an agent that says "here is the fix" and a loop that opens the PR, links the Linear ticket and pings the channel once CI is green by itself.
> (นี่คือความต่างระหว่าง agent ที่บอกว่า "นี่ไงตัวแก้" กับลูปที่ *เปิด PR เอง, ลิงก์ Linear ticket, แล้ว ping channel เองพอ CI เขียว*)

## Sub-agents — แยกคนทำออกจากคนตรวจ

สิ่งที่มีประโยชน์เชิงโครงสร้างที่สุดในลูป คือการแยก **คนเขียน** ออกจาก **คนตรวจ**

> The model that wrote the code is way too nice grading its own homework. A second agent with different instructions and sometimes a different model catches the stuff the first one talked itself into.
> (โมเดลที่เขียนโค้ดมัน *ใจดีเกินไป* เวลาให้เกรดการบ้านตัวเอง. agent ตัวที่สองที่มี instruction ต่าง บางทีก็คนละ model จะจับสิ่งที่ตัวแรกพูดจนตัวเองเชื่อไปเอง)

- **Codex**: spawn subagent ตอนสั่งเท่านั้น รันพร้อมกันแล้วพับผลกลับเป็นคำตอบเดียว. นิยาม agent เป็นไฟล์ TOML ใน `.codex/agents/` (name, description, instructions, optional model + reasoning effort) → security reviewer เป็น model แรงบน effort สูง ขณะที่ explorer เป็นตัวเร็ว read-only
- **Claude Code**: subagent ใน `.claude/agents/` + agent teams ที่ส่งงานต่อกัน

split ที่ใช้บ่อยทั้งสอง tool: **ตัวหนึ่ง explore, ตัวหนึ่ง implement, ตัวหนึ่ง verify ตาม spec**. Addy เคยเขียนเรื่องนี้สองครั้งในชื่อ "code agent orchestra" และ "adversarial code review"

เหตุผลที่มันสำคัญ *ในลูป* โดยเฉพาะ: ลูปรันตอนเราไม่ได้ดู — verifier ที่เราเชื่อใจจริงคือเหตุผลเดียวที่เดินจากไปได้. subagent เผา token มากกว่า (แต่ละตัวรัน model + tool ของตัวเอง) → ใช้ตรงที่ความเห็นที่สองคุ้มค่าจ่าย. นี่คือสิ่งที่ `/goal` ของ Claude Code ทำใต้ฝากระโปรงอยู่แล้ว — model สดตัดสินว่าลูปเสร็จไหม ไม่ใช่ตัวที่ทำงาน = **maker/checker split ที่ใช้กับเงื่อนไขหยุดเอง**

## ลูปหนึ่งหน้าตาเป็นยังไง

Addy ยกตัวอย่างรูปที่เขาใช้บ่อย:

1. **automation** รันทุกเช้าบน repo → prompt เรียก triage skill ที่อ่าน CI failure เมื่อวาน + open issue + commit ล่าสุด แล้วเขียน finding ลง markdown / Linear
2. finding ที่ควรทำ → thread เปิด **worktree** แยก ส่ง **sub-agent** ตัวหนึ่งร่างตัวแก้
3. **sub-agent ตัวที่สอง** review ร่างนั้นเทียบกับ project skill + test เดิม
4. **connector** เปิด PR + อัปเดต ticket
5. อะไรที่ลูปจัดการไม่ได้ → ตกลง triage inbox ให้เรา
6. **state file** คือกระดูกสันหลัง — จำว่าลองอะไรไป อะไรผ่าน อะไรค้าง เพื่อพรุ่งนี้รันต่อจากจุดที่วันนี้หยุด

> And look at what you actually did there. You designed it one time. You did not prompt any of those steps.
> (ดูสิว่าจริง ๆ เราทำอะไรไป — เราออกแบบมันครั้งเดียว ไม่ได้ prompt สักขั้นเลย)

## สิ่งที่ลูปยังไม่ทำให้เรา

> **The loop changes the work, it does not delete you from it.**
> (ลูปเปลี่ยนงาน ไม่ได้ลบเราออกจากงาน)

และ 3 ปัญหานี้ **คมขึ้น** เมื่อลูปดีขึ้น ไม่ใช่ง่ายขึ้น:

- **Verification ยังเป็นของเรา** — ลูปที่รันไม่มีคนดู ก็คือลูปที่ *ทำพลาดโดยไม่มีคนดู* ด้วย. แยก verifier sub-agent ออกจาก maker ก็เพื่อให้คำว่า "เสร็จ" มีความหมาย แต่ถึงอย่างนั้น "done is a claim and not a proof" (เสร็จคือคำกล่าวอ้าง ไม่ใช่ข้อพิสูจน์). งานของเราคือ ship โค้ดที่เรา *ยืนยันแล้ว* ว่าทำงาน
- **ความเข้าใจของเราเน่าได้ถ้าปล่อย** — ยิ่งลูป ship โค้ดที่เราไม่ได้เขียนเร็วเท่าไหร่ ช่องว่างระหว่าง "สิ่งที่มีอยู่จริง" กับ "สิ่งที่เราเข้าใจ" ยิ่งโต. Addy เรียกว่า *comprehension debt* (ญาติของ [[cognitive-debt]]) — ลูปที่ลื่นยิ่งทำให้มันโตเร็วเว้นแต่เราจะอ่านสิ่งที่ลูปทำ
- **[[cognitive-surrender]]** — พอลูปรันเอง มันยั่วยวนให้เลิกมีความเห็นแล้วรับอะไรก็ตามที่มันคืนมา

> Designing the loop is the cure when you do it with judgement and the accelerant when you do it to avoid thinking, same action, opposite result.
> (ออกแบบลูปคือ *ยา* ถ้าทำด้วยวิจารณญาณ และเป็น *ตัวเร่ง* ถ้าทำเพื่อเลี่ยงการคิด — ทำเหมือนกันเป๊ะ ผลตรงข้ามกัน)

## สรุปของ Addy — Build the loop. Stay the engineer.

> Two people can build the exact same loop and get completely opposite results. One uses it to move faster on work they understand deeply. The other uses it to avoid understanding the work at all. The loop doesn't know the difference. You do.
> (สองคนสร้างลูปเดียวกันเป๊ะ ได้ผลตรงข้ามกันได้ — คนหนึ่งใช้มันทำงานที่เข้าใจลึกให้เร็วขึ้น อีกคนใช้มันเพื่อ *เลี่ยงการเข้าใจงาน* เลย. ลูปไม่รู้ความต่าง แต่เรารู้)

> That's what makes loop design harder than prompt engineering, not easier. Cherny's point isn't that the work got easier. It's that the leverage point moved.
> (นี่แหละที่ทำให้ออกแบบลูป *ยาก* กว่า prompt engineering ไม่ใช่ง่ายกว่า. ประเด็นของ Cherny ไม่ใช่ว่างานง่ายลง แต่ *จุดงัด* มันย้ายที่)

> **Build the loop. But build it like someone who intends to stay the engineer, not just the person who presses go.**

Addy เตือนปิดท้าย: ถ้าไม่ review โค้ดเอง หรือพึ่งลูปอัตโนมัติล้วน คุณภาพ product จะตก และจะติด downward spiral ขุดหลุมให้ตัวเองลึกลงเรื่อย ๆ. **ตั้งลูปไปเถอะ แต่อย่าลืมว่าการ prompt agent ตรง ๆ ก็ยังได้ผล — มันเรื่องของการหาสมดุล**

## ประเด็นหลักที่ดึงออกมา

- [[loop-engineering]] — แก่นความคิด: ออกแบบระบบที่ prompt agent แทนเรา; 5 ชิ้น + memory; ลูป = recursive goal
- [[git-worktrees]] — isolation เชิงกลไกสำหรับ agent ขนาน; กันชนไฟล์ แต่ไม่เพิ่ม review bandwidth
- เชื่อมกับ [[orchestration-tax]], [[cognitive-surrender]], [[long-running-agents]], [[subagent-patterns]], [[agent-harness-engineering]]

## See also

- [[loop-engineering]]
- [[git-worktrees]]
- [[addy-osmani]]
- [[agent-harness-engineering]]
- [[the-orchestration-tax]]
- [[orchestration-tax]]
- [[cognitive-surrender]]
- [[long-running-agents]]
- [[subagent-patterns]]
- [[model-context-protocol]]
- [[plugin-manager]]
