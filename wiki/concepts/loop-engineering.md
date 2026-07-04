---
title: Loop Engineering
type: concept
tags: [ai, agents, loops, harness, orchestration, automation, workflow]
created: 2026-06-09
updated: 2026-07-05
sources: ["Loop Engineering..md", "Introducing Omnigent A Meta-Harness to Combine, Control and Share Your Agents.md", Agentic Code Review.md, "Matt Pocock’s Agentic Engineering Workflow (just copy him).md", Self Learning for Agents Clearly Explained.md, "รู้จักกับ Loop Engineering — mikelopster transcript", l8-principals-agentic-engineering-workflow-kun-chen.md, stop-building-ai-agents-old-way.md, piyalitt-codex-keynote-attention-not-token.md]
---

# Loop Engineering / วิศวกรรมลูป

**Loop engineering คือการเลิกเป็น "คนพิมพ์ prompt" ให้ agent แล้วไปออกแบบ "ระบบ" ที่ทำหน้าที่พิมพ์ prompt นั้นแทนเรา.** [[addy-osmani|Addy Osmani]] (วิศวกร Google) สรุปไว้ในบทความ [[loop-engineering-osmani|Loop Engineering]] (2026-06-09): ลูป = *recursive goal* — เรากำหนด "จุดประสงค์" ไว้หนึ่งอย่าง แล้ว AI วนทำเองจนกว่าจะเสร็จ. เราไม่ได้คุยทีละ turn อีกต่อไป เราออกแบบลูปครั้งเดียวแล้วปล่อยให้ลูปไปจิ้ม agent แทน

ที่มาของคำมาจากสองคน: Peter Steinberger (*"You should be designing loops that prompt your agents"*) และ Boris Cherny หัวหน้า Claude Code (*"My job is to write loops"*)

## จาก "ถือเครื่องมือ" ไปเป็น "ออกแบบระบบ"

สองปีที่ผ่านมา วิธีรีดงานจาก coding agent คือ: เขียน prompt ดี ๆ ใส่ context พอ → อ่านที่มันตอบ → พิมพ์อันต่อไป. **agent เป็นเครื่องมือ และเราถือมันอยู่ตลอดเวลา** ทีละ turn

loop engineering เปลี่ยนภาพนั้น. เราสร้างระบบเล็ก ๆ ที่ *หางานเอง → แจกงาน → ตรวจงาน → จดว่าอะไรเสร็จ → ตัดสินใจขั้นต่อไป* แล้วปล่อยให้ระบบนั้นไปจิ้ม agent แทนเรา

**ที่ทางในกองความคิดของ Addy** — loop engineering อยู่ *ชั้นบน* ของ [[agent-harness-engineering|harness]] หนึ่งชั้น:

- [[coding-harness|harness]] = สภาพแวดล้อมที่ agent *ตัวเดียว* รันอยู่ข้างใน (prompt, tool, filesystem, memory, hook)
- loop = harness ที่ **รันบน timer, แตก helper ออกไป, และป้อนงานให้ตัวเอง**

> ได้อะไร: จุดงัด (leverage) ย้ายจาก "เขียน prompt เก่ง" ไปเป็น "ออกแบบลูปเก่ง" — งานไม่ได้ง่ายลง แต่จุดที่ใช้ทักษะมันย้ายที่

## ห้าชิ้น + memory

Addy บอกว่าลูปต้องการ 5 ชิ้น แล้วก็อีกหนึ่งที่ไว้จำของ. ที่น่าสนใจคือ **ตอนนี้ทั้ง Claude Code และ Codex มีครบทั้งหมดแล้ว** — เลิกเขียน bash กองโตเองได้. ชื่อต่างกันบ้าง แต่ความสามารถเหมือนกัน → ออกแบบลูปที่ทำงานได้ไม่ว่าจะนั่งอยู่ใน tool ตัวไหน

| ชิ้น | ทำอะไร | หน้าที่เกี่ยว |
|---|---|---|
| **Automations** | รันตามตารางเวลา ทำ discovery + triage เอง — *หัวใจที่เต้น* ของลูป | (ดูด้านล่าง) |
| **Worktrees** | ให้ agent ขนานกันได้โดยไม่เหยียบไฟล์กัน | [[git-worktrees]] |
| **Skills** | เขียนความรู้โปรเจกต์ลงดิสก์ แทนให้ agent เดา | [[claude-md\|skill/CLAUDE.md]] |
| **Plugins & Connectors** | เสียบ agent เข้าเครื่องมือจริง (issue tracker, DB, Slack) ผ่าน [[model-context-protocol\|MCP]] | [[plugin-manager]] |
| **Sub-agents** | ตัวหนึ่งคิด อีกตัวตรวจ | [[subagent-patterns]] |
| **Memory** (ชิ้นที่หก) | state file *นอก* บทสนทนา จำว่าอะไรเสร็จ/ค้าง | [[long-running-agents]] |

### Automations — หัวใจที่เต้น

Automations คือสิ่งที่ทำให้ลูปเป็น "ลูป" จริง ไม่ใช่แค่รันครั้งเดียว. เลือก project + prompt + ความถี่ + รันบน local หรือ background worktree. รอบที่เจออะไรไป triage inbox, รอบที่ไม่เจอก็ archive ตัวเองทิ้ง

มี primitive ใน session สองตัวที่อยู่ใกล้แก่นที่สุด — และนี่คือจุดที่ทั้งสอง tool ตรงกัน:

- **`/loop`** — รันซ้ำตาม cadence (ทุก ๆ กี่นาที/ชั่วโมง)
- **`/goal`** — วิ่งต่อ *ข้าม turn* จนกว่าเงื่อนไขที่ verify ได้จะเป็นจริง เช่น "all tests in test/auth pass and lint is clean". **หลังทุก turn มี model เล็กแยกต่างหากเช็คว่าเสร็จหรือยัง** — ตัวที่เขียนโค้ดไม่ใช่ตัวที่ให้เกรด. นี่คือ maker/checker split ที่ใช้กับ *เงื่อนไขหยุด* เอง

> Automations คือส่วนที่ทำให้งาน *โผล่ขึ้นมา* ส่วนที่เหลือของลูปคือส่วนที่ลงมือทำกับงานนั้น

### Skills — intent ที่เขียนไว้ข้างนอก

agent เริ่มทุก session แบบเย็นชืด และจะเติม "ช่องว่างของ intent" ด้วยการเดาอย่างมั่นใจ. skill คือ intent ที่เขียนไว้ข้างนอก (convention, ขั้นตอน build, "เราไม่ทำแบบนี้เพราะเหตุการณ์ครั้งนั้น") เขียนครั้งเดียว agent อ่านทุกรอบ

> ไม่มี skill ลูป re-derive โปรเจกต์จากศูนย์ทุกรอบ. มี skill มันค่อย ๆ compound

ข้อต้องแยก: **skill คือ format สำหรับ "เขียน" ส่วน [[plugin-manager\|plugin]] คือวิธี "ส่ง"** — อยากแชร์ข้าม repo ก็แพ็กเป็น plugin

### Memory — agent ลืม แต่ repo ไม่ลืม

ชิ้นที่หกฟังดูง่ายเกินจะสำคัญ: ไฟล์ markdown หรือบอร์ด Linear ที่อยู่ *นอก* บทสนทนาเดียว เก็บว่าอะไรเสร็จ/ค้าง. แต่มันคือกลเดียวกับที่ [[long-running-agents|long-running agent]] ทุกตัวพึ่งพา — **โมเดลลืมทุกอย่างระหว่างรอบ memory เลยต้องอยู่บนดิสก์ ไม่ใช่ใน context.** state file คือกระดูกสันหลังที่ทำให้พรุ่งนี้รันต่อจากจุดที่วันนี้หยุดได้

## ลูปหนึ่งหน้าตาเป็นยังไง

ตัวอย่างที่ Addy ใช้บ่อย ร้อยทั้งหมดเข้าด้วยกัน:

1. **automation** รันทุกเช้า → เรียก triage skill อ่าน CI failure เมื่อวาน + open issue + commit ล่าสุด → เขียน finding ลง state file
2. finding ที่ควรทำ → เปิด **worktree** แยก ส่ง **sub-agent** ร่างตัวแก้
3. **sub-agent ตัวที่สอง** review ร่างเทียบ project skill + test เดิม
4. **connector** เปิด PR + อัปเดต ticket เอง
5. อะไรที่ลูปจัดการไม่ได้ → ตกลง triage inbox ให้เรา
6. **state file** จำว่าลองอะไร อะไรผ่าน อะไรค้าง

จุดสำคัญ: **เราออกแบบมันครั้งเดียว ไม่ได้ prompt สักขั้นเลย** — นั่นคือ "การ write loop" ของ Cherny ที่เป็นจริง

## maker/checker — สิ่งที่สำคัญที่สุดในลูป

> โมเดลที่เขียนโค้ดมันใจดีเกินไปเวลาให้เกรดการบ้านตัวเอง

การแยก **คนเขียน** ออกจาก **คนตรวจ** คือโครงสร้างที่มีประโยชน์ที่สุดในลูป. agent ตัวที่สอง — instruction ต่าง บางทีคนละ model — จับสิ่งที่ตัวแรกพูดจนตัวเองเชื่อไปเอง. เหตุผลที่มันสำคัญ *ในลูป* โดยเฉพาะ: ลูปรันตอนเราไม่ได้ดู — **verifier ที่เราเชื่อใจจริงคือเหตุผลเดียวที่เดินจากไปได้**

นี่คือ [[subagent-patterns|pipeline pattern]] (explore → implement → verify) ที่ Addy เคยเขียนในชื่อ "code agent orchestra" / "adversarial code review" — และเป็นสิ่งที่ `/goal` ทำใต้ฝากระโปรงอยู่แล้ว

## สามอย่างที่ลูปยัง *ไม่* ทำให้ — และคมขึ้นเมื่อลูปดีขึ้น

> The loop changes the work, it does not delete you from it.
> (ลูปเปลี่ยนงาน ไม่ได้ลบเราออกจากงาน)

1. **Verification ยังเป็นของเรา** — ลูปที่รันไม่มีคนดู = ลูปที่ *พลาดโดยไม่มีคนดู* ด้วย. "done is a claim and not a proof" (เสร็จคือคำกล่าวอ้าง ไม่ใช่ข้อพิสูจน์). งานเราคือ ship โค้ดที่เรา *ยืนยันแล้ว*
2. **ความเข้าใจเน่าได้ถ้าปล่อย** — ยิ่งลูป ship เร็ว ช่องว่างระหว่าง "สิ่งที่มีจริง" กับ "สิ่งที่เราเข้าใจ" ยิ่งโต. Addy เรียก *comprehension debt* — ญาติของ [[cognitive-debt]]
3. **[[cognitive-surrender]]** — พอลูปรันเอง มันยั่วให้เลิกมีความเห็นแล้วรับอะไรก็ตามที่มันคืนมา

> Designing the loop is the cure when you do it with judgement and the accelerant when you do it to avoid thinking — same action, opposite result.
> (ออกแบบลูปคือ *ยา* ถ้าทำด้วยวิจารณญาณ และเป็น *ตัวเร่ง* ถ้าทำเพื่อเลี่ยงการคิด — ทำเหมือนกันเป๊ะ ผลตรงข้าม)

## มุมลองใช้จริง: feedback gate สำคัญกว่า trigger

[[mikelopster]] ในวิดีโอ [[mikelopster-loop-engineering|รู้จักกับ Loop Engineering]] เติมมุมที่เป็นประโยชน์มากจากการลองเล่นจริงกับ [[claude-code|Claude Code]] และ [[openai-codex|Codex]]: ลูปไม่ได้พังเพราะไม่มี trigger. มันพังเพราะ **feedback gate** ไม่ดี.

feedback gate คือเกณฑ์ที่บอกว่า "ผ่านหรือยัง". ถ้า gate คลุมเครือหรือเข้มผิดทาง agent จะวนแก้ไม่จบและเผา token. ถ้า gate หลวมไป agent จะประกาศว่าผ่าน ทั้งที่งานจริงยังไม่ผ่าน แล้วมนุษย์ต้องมา prompt ซ้ำ. เพราะฉะนั้นคำถามแรกไม่ใช่ "จะให้มันรันทุกกี่นาที" แต่คือ **"เราจะรู้ได้ยังไงว่าควรหยุด"**.

ตัวอย่างที่ mikelopster เห็นว่าไปได้ดีคือ test, lint, coverage, CI, PR status, metric, หรือ log anomaly ที่มีสัญญาณวัดได้. แต่พองานกลายเป็น content หรือ UI ที่ต้องใช้รสนิยม เช่น "อ่านแล้วแปลก" หรือ "ทำให้สวยขึ้น" gate จะนิยามยาก. agent อาจผลิต draft เยอะขึ้น แต่คอขวดย้ายไปอยู่ที่คนอ่านและตัดสิน.

> ได้อะไร: loop engineering ไม่ใช่แค่ automation + agent. มันคือ automation + agent + **scorer ที่ไว้ใจได้** + เพดานรอบ/token ที่กันไม่ให้การวนกลายเป็นการเผาเงิน.

## ตัวอย่างหน้างาน: manager/worker ของ Peter Steinberger

[[peter-steinberger|Peter Steinberger]] บนเวที Codex keynote (สรุป [[piyalitt-codex-keynote-attention-not-token]]) เป็นตัวอย่าง loop engineering ที่ลงมือจริง:

- เคยเปิด 10+ terminal แล้วรู้สึกว่า orchestrate — จริง ๆ แค่ **polling** (ตัวเขาเป็น scheduler/router/memory)
- วันนี้คุยกับ **manager agent ตัวเดียว** รันยาว → กระจายงาน worker; งานยากค่อย pair กับ worker โดยตรง
- สามชิ้นที่ทำให้ได้: server-side compaction, ระบบประสานงานหลาย project ใน thread เดียว, automation ปลุก manager เมื่อมีเหตุการณ์
- หลัก [[inner-loop-outer-loop|inner/outer loop]]: agent วิ่ง execution; Peter รีวิว PR เมื่อ judgement สร้างความต่าง

> "อนาคตไม่ใช่การเปิด terminal 20 หน้าต่าง แต่คือ loop ที่ดีกว่าเดิม"
> — Peter Steinberger

โจทย์ที่ยังเปิด: manager ที่ออกแบบ loop ให้เราเองทั้งหมดเมื่อบอกเป้าหมาย — ยังไม่มีใครแก้สำเร็จ (Peter บอกตรง ๆ บนเวที)

## มุมแย้ง: "คิว ไม่ใช่ลูป" (Matt Pocock)

[[matt-pocock|Matt Pocock]] ดันกลับกระแสลูปในพอดแคสต์กับ [[david-ondrej|David Ondrej]] (2026-06-19): เขาบอกว่าครึ่งหนึ่งของ hype คือ "lab อยากขาย token" (รันลูปตลอด = จ่ายตลอด) และที่จริงเราไม่ได้ต้องการ "ลูป" — ต้องการแค่ AFK agent มารับงานที่ scope แล้วไปทำให้จบ

> "The way I mostly think about these things as queues, okay, queues, not loops."

มุมของ Matt คือมองงานเป็น **[[queues-over-loops|คิว]]** ที่หลาย node (agent/dev) หยิบไปทำ — ตรงกับวิธีทีม dev ทำงานจริงมากกว่า "ลูปเดียววิ่งทำทุก task". ที่มาของลูปคือ [[ralph|Ralph]] ของ [[jeffrey-huntley|Jeffrey Huntley]]

จริง ๆ สองมุมนี้**เสริมกันมากกว่าขัดกัน**: Addy เน้นกลไก (maker/checker, state file, verifiable stop) ส่วน Matt เน้นว่าโครงควรเป็นคิวที่หยิบงานทีละชิ้น ไม่ใช่ลูปเดี่ยว. ทั้งคู่เห็นตรงกันว่า verification ยังเป็นของมนุษย์ และเพดานคือ review bandwidth

## มุมปฏิบัติ: Good Night Have Fun

[[kun-chen|Kun Chen]] โชว์ long-running loop ในรูปที่ใช้งานจริงผ่าน [[good-night-have-fun|Good Night Have Fun]]. Pattern คือให้ objective + stop condition + cap แล้วให้ agent วนทำเอง. ตัวอย่างในคลิปคือให้ agent แกล้งเป็นเด็ก 7 ขวบ ใช้แอป end-to-end, หา usability problem แรก, fix, แล้ว rinse and repeat.

จุดนี้เติมรายละเอียดให้หน้า loop engineering: loop ที่ดีไม่ได้ต้องเป็น daemon ใหญ่เสมอไป. บางครั้งมันคือ task-scoped loop ที่มี objective ชัด, evidence ชัด, และเพดาน token/iteration ชัด. Kun บอกว่าเหมาะกับงานที่ verify ได้ เช่น performance, E2E coverage, metric improvement หรือ hypothesis search.

**ได้อะไร:** `/goal` หรือ long-running loop จะมีประโยชน์เมื่อ stop condition ชัดพอให้เดินจากไปได้โดยไม่ตื่นมาเจอ quota หายหมด.

## Recipe แบบ 7 ชิ้นของ loop ที่รันยาว

[[prompt-engineering|Prompt Engineering]] ใน [[stop-building-ai-agents-old-way]] อธิบาย outer loop ในภาษาง่ายกว่า: ไม่ใช่ให้ agent คิดยาว ๆ รอบเดียว แต่ให้มันทำ attempt สั้น ๆ แล้วมี loop เช็ค progress เทียบ goal. ถ้ายังไม่ผ่านก็ส่ง failure กลับไปให้ทำใหม่ ถ้าผ่านจึง mark complete.

สิ่งที่คลิปเติมให้หน้านี้คือ checklist ของสิ่งรอบ loop: goal เป็น contract, evaluator แยกจาก executor, verifier เป็น proof, orchestration แยก planning/execution/evaluation ตาม model ที่เหมาะ, [[agent-observability|observability]] ทำให้คนเห็น run ระหว่างทาง, และ [[session-mining|session mining]] เอา failure ซ้ำกลับไปปรับ rule.

**ผลคือ:** loop ที่ดีไม่ได้มีแค่ trigger กับ retry. ต้องมีเกณฑ์หยุด, หลักฐาน, และทางให้ failure กลายเป็น control ในรอบถัดไป.

## loop engineering = ชั้น Harness ที่เรียนรู้เอง

[[ataiiam|@ataiiam]] ใน [[self-learning-for-agents-explained]] จัด loop engineering เป็นวิธีแรกของการทำให้ **ชั้น Harness เรียนรู้เอง** (ดู [[three-learning-layers]]). มุมที่เสริมหน้านี้: เขาเรียง loop เป็น 4 ระดับตาม "harness ทำเองมากแค่ไหน" — (1) verification loop (grader ตัวสองส่งกลับถ้าไม่ผ่าน, ใกล้ maker/checker ข้างบน), (2) ยิงตามตาราง (= Automations), (3) อ่าน trace แล้ว **เขียน harness ใหม่เอง** (LangChain Deep Agents / Self-Harness), (4) ติดตั้ง harness สำเร็จรูป ([[microsoft|Microsoft]] Agent Framework). Sydney Runkle ([[langchain|LangChain]]) บอกว่าคุณค่าอยู่ที่ loop ชั้นนอก.

ข้อจำกัดที่ thread ย้ำตรงกับหน้านี้เป๊ะ: **loop ช่วยได้ก็ต่อเมื่อให้คะแนน output ได้** (test, rule, หรือ LLM judge). ไม่มี scorer → loop ไม่มีอะไรให้วน. และ "harness จับได้ ≠ agent ฉลาดขึ้น" — verification loop หยุด error ซ้ำได้ แต่การเรียนรู้จริงต้องไปเก็บที่ชั้น context ([[agent-memory-types|procedural memory]]).

## เชื่อมกับเรื่องอื่นในวิกินี้

- **[[three-learning-layers]]** — loop engineering คือวิธีหนึ่งของ self-learning ชั้น Harness; verification loop / self-rewriting harness อยู่ในนั้น
- **[[orchestration-tax]]** — คู่ตรงข้ามที่สำคัญ. ลูปแก้การชน *เชิงกลไก* (ผ่าน worktree) และผลิตงานขนานได้เยอะ แต่ **เพดานยังคือ review bandwidth ของเรา** — เปิดลูปเยอะเกินที่ตรวจไหวก็เกิด orchestration tax. ทั้งสองเรื่องคือ Addy คนเดียวกัน เล่าคนละด้าน: ลูป = ฝั่งผลิต/ระบบ, orchestration tax = ฝั่งบริโภค/ความสนใจ
- **[[mikelopster-loop-engineering]]** — มุมลองใช้จริงภาษาไทย: loop จะคุ้มเมื่อ feedback gate วัดเองได้; งาน content/taste มักตันที่คน review
- **[[agentic-code-review]]** — ชั้นตรวจของลูป. พอลูปไม่ได้แค่เขียนโค้ด แต่เริ่ม review และ judge งานเอง คำถามจะกลายเป็น "ตรงไหนต้องมีคนอยู่บนลูป". คำตอบของ Addy คือใช้ AI triage + heterogeneous reviewers ได้ แต่ high-blast-radius path และ merge ownership ยังต้องมีมนุษย์
- **[[long-running-agents]]** — ลูปคือ long-running agent ที่ประกอบจาก primitive ของตัวผลิตภัณฑ์; state file = memory-on-disk เหมือน checkpoint-and-resume
- **[[stop-building-ai-agents-old-way]]** — สูตร 7 ชิ้นของ long-running loop: goal/evaluator/verifier/outer loop/orchestration/observability/memory
- **[[agent-harness-engineering]]** — ชั้นล่างของลูป (harness ของ agent ตัวเดียว)
- **[[subagent-patterns]]** — chunk "Sub-agents" ของลูปคือ pattern พวกนี้
- **[[git-worktrees]]** — chunk "Worktrees"
- **[[harness-ratchet]]** — finding ซ้ำ ๆ ที่ลูปเจอ ควรกลายเป็น skill/test/hook ถาวร
- **[[meta-harness]]** — พื้นกลางสำหรับลูปที่ต้องประกอบ agent ต่าง harness, ใช้ policy ร่วมกัน และให้ทีมเข้าดู live session. Loop เน้นระบบที่ทำงานวนเอง ส่วน meta-harness เน้น interoperability และ control ข้ามเครื่องมือ

## See also

- [[loop-engineering-osmani]]
- [[agentic-code-review]]
- [[addy-osmani]]
- [[git-worktrees]]
- [[orchestration-tax]]
- [[cognitive-surrender]]
- [[long-running-agents]]
- [[agent-harness-engineering]]
- [[subagent-patterns]]
- [[plugin-manager]]
- [[model-context-protocol]]
- [[harness-ratchet]]
- [[cognitive-debt]]
- [[meta-harness]]
- [[omnigent]]
- [[queues-over-loops]]
- [[afk-agents]]
- [[ralph]]
- [[matt-pocock]]
- [[matt-pocock-agentic-workflow]]
- [[three-learning-layers]]
- [[self-learning-for-agents-explained]]
- [[langchain]]
- [[mikelopster]]
- [[mikelopster-loop-engineering]]
- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[good-night-have-fun]]
- [[stop-building-ai-agents-old-way]]
- [[agent-observability]]
- [[session-mining]]
- [[peter-steinberger]]
- [[inner-loop-outer-loop]]
- [[piyalitt-codex-keynote-attention-not-token]]
