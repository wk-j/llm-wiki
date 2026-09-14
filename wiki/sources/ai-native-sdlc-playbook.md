---
title: The AI-Native SDLC Playbook
type: source
author: Louis Claxton
url: https://claude.com/blog/the-ai-native-sdlc-playbook
date_ingested: 2026-09-14
tags: [ai, software-engineering, sdlc, agents, governance, enterprise, security]
created: 2026-09-14
updated: 2026-09-14
sources: ["https://claude.com/blog/the-ai-native-sdlc-playbook"]
---

# The AI-Native SDLC Playbook / คู่มือออกแบบ SDLC รอบการทำงานของ agent

[[anthropic|Anthropic]] เผยแพร่ playbook นี้เมื่อ 21 สิงหาคม 2026 เขียนโดย [[louis-claxton|Louis Claxton]] และเป็นต้นทางของเรื่องที่ [[claude-codes-new-intent-md-rob-shocks|Rob Shocks เอาไปเล่าต่อในคลิป]] หน้านี้สรุปจากเอกสารโดยตรง จึงมีรายละเอียดเรื่อง governance, managed settings, control band และตัววัดผลที่คลิปไม่ได้ลงลึก

Playbook ตั้งต้นจากสมมติฐานง่าย ๆ ว่า process ของทีมซอฟต์แวร์เกิดขึ้นในยุคที่การเขียน code แพงและช้าที่สุด พอ agent เขียน code ได้ในไม่กี่ชั่วโมง งานรอบข้างกลับเป็นตัวถ่วง เอกสารจึงไล่ SDLC ทีละช่วงว่าต้องเปลี่ยนอะไร ต้อง commit artifact ชิ้นไหนลง repo และใครเป็นคนอนุมัติ

> "Humans remain accountable for every decision that requires judgment."
>
> คนยังรับผิดชอบทุกการตัดสินใจที่ต้องใช้วิจารณญาณ

## ทำไม SDLC แบบเดิมถึงเริ่มไม่พอ

Process เดิมไม่ได้ผิด เพราะออกแบบมาให้ตามความรับผิดชอบและควบคุมงานได้ ทุกขั้นจึงมีคนเซ็น คนตรวจ หรือคณะกรรมการพิจารณาข้อยกเว้น แต่ทั้งหมดตั้งอยู่บนสมมติฐานว่า **ทุกขั้นทำโดยคน** ความเร็วของระบบจึงติดอยู่ที่ความเร็วของคน

พอ agent เข้ามาเร่งเฉพาะช่วง Build งานที่ผลิตออกมาต่อวันมากขึ้นหลายเท่า แต่ทีม security ที่ตั้งขนาดไว้สำหรับ manual review ยังตรวจได้เท่าเดิม approval gate ยังเป็นคิวเดิม คณะกรรมการยังประชุมเดือนละครั้ง ผลคืองานไปกองหน้า gate แทนที่จะออกเร็วขึ้น

เอกสารสรุปว่าคอขวดย้ายไปอยู่ "ซ้ายและขวาของ build phase" ซ้ายคือการบอกให้ชัดว่าจะสร้างอะไร ขวาคือการพิสูจน์ว่าของที่ได้ใช้ได้จริงและปล่อยได้ ตรงกับที่ [[the-new-software-lifecycle|Addy Osmani]] มองไว้ใน [[ai-driven-sdlc|AI-driven SDLC]]

**ได้อะไร:** ถ้าซื้อ coding agent มาแล้วไม่แตะ process รอบข้าง สิ่งที่ได้คือคิวที่ยาวขึ้น ไม่ใช่ lead time ที่สั้นลง

## Stage 1 Plan: เก็บไอเดียเป็น `intent.md`

ปัญหาเดิมคือไอเดียเดินทางไกลเกินไป จากคนที่เจอปัญหา ไปลง backlog เป็น user story เข้า refinement meeting แล้วค่อยถึงมือ engineer แต่ละมือที่ส่งต่อทำให้เจตนาเดิมจางลง

วิธีใหม่ให้คนต้นเรื่องคุยกับ Claude เป็นภาษาปกติ คนนี้อาจเป็นลูกค้า product manager หรือ developer ก็ได้ จากนั้น Claude สรุปเป็น Markdown ตาม template ขององค์กร กลายเป็น [[intent-md|`intent.md`]] ที่บันทึกปัญหา ผลลัพธ์ที่อยากได้ ผู้ใช้และระบบที่กระทบ constraint และคำถามที่ยังค้าง

คนต้นเรื่องต้องอ่านและแก้ไฟล์เอง ไม่ใช่เซ็นผ่านงานของ agent จากนั้น product owner จึงรับเข้า Stage 2 ไฟล์ต้องอยู่ในระบบที่เก็บ version พร้อมชื่อคนและ timestamp ถ้าไม่ได้ใช้ git เอกสารเสนอให้ใช้ connector commit ผ่าน claude.ai

- **เข้า:** มีไอเดียแล้ว จะมาจาก request ของผู้ใช้ ticket หรือ alert จาก incident ก็ได้
- **ออก:** product owner รับ `intent.md` ที่ merge แล้ว

**ได้อะไร:** จากไอเดียถึงเอกสารที่ทีมอ่านต่อได้ วัดเป็นชั่วโมง แทนที่จะเป็นหลายสัปดาห์ผ่าน backlog

## Stage 2 Design: รวม requirement กับ design ให้จบใน session เดียว

เดิมทีสองอย่างนี้เป็นคนละ phase คนละทีม ระหว่างทางมีทั้งเวลารอและข้อมูลหาย playbook เสนอให้ยุบเป็นรอบเดียว

product owner เปิด session โดยโหลด skills ขององค์กรไว้ เช่น brand guideline, security policy, compliance และ UX Claude อ่าน `intent.md` ที่รับแล้ว แล้วเขียน `spec.md` ที่มีทั้ง requirement และ design โดยเอา policy ไปใส่ตั้งแต่ตอนเขียน ไม่ใช่รอไปเจอตอน review

ถ้ามีข้อไหนชนกับ policy Claude จะ flag ไว้ให้ product owner ไปคุยกับเจ้าของ policy งานที่เสี่ยงสูงให้ tech lead ร่วมอนุมัติด้วย

**ผลคือ:** ทีมเจอข้อขัดกับ policy ตอนที่ยังแก้ง่าย ไม่ใช่ตอนเปิด PR แล้วมีคนรอ merge

## Stage 3 Build: เริ่มจาก plan mode เสมอ

ปัญหาเดิมคือ engineer ลงมือเขียนเลย กลยุทธ์อยู่ในหัวหรือกระจายอยู่ใน comment reviewer เห็นแต่ diff ที่เสร็จแล้ว ไม่เห็นว่าทำไมถึงเลือกทางนี้

playbook ให้เริ่ม [[claude-code|Claude Code]] ใน [[plan-mode-as-prompting|plan mode]] ก่อน เป็น mode ที่ agent อ่าน codebase ได้แต่แก้อะไรไม่ได้ ป้อน `intent.md` กับ `spec.md` เข้าไป แล้วขอแผน จากนั้น engineer ซักแผน: เสี่ยงตรงไหน มีทางอื่นไหม จะทดสอบยังไง เกณฑ์รับคือ **คนที่ไม่เคยเห็นบทสนทนานี้ต้องอ่านแล้วทำตามได้** แล้วค่อย commit เป็น `plan.md`

พอ Claude ลงมือ ถ้างานจริงเบนจากแผน ให้แก้ `plan.md` ใน commit เดียวกัน แผนกับ diff จะได้ไม่หลุดจากกัน

### `CLAUDE.md` เก็บความรู้ของทีมให้ version ได้

[[claude-md|`CLAUDE.md`]] เก็บ convention ของ repo คำสั่ง build โครงสถาปัตยกรรม และความผิดพลาดที่เจอบ่อย กฎง่าย ๆ ที่เอกสารให้คือ **ถ้า Claude พลาดเรื่องเดิมสองครั้ง ให้เขียนลงไฟล์** และให้ยาวไม่เกินหนึ่งหน้า เพราะทุก session ที่เปิดใหม่ต้องอ่านไฟล์นี้ทั้งไฟล์ เรื่องเดียวกับ [[instruction-budget|instruction budget]]

### Skills เอา policy ไปวางเป็น code

Skills คือความรู้เชิงนโยบายที่ต้องใช้เหมือนกันทุกครั้ง เก็บเป็นโฟลเดอร์ใน `.claude/skills/` เอกสารยกตัวอย่าง skill ชื่อ `secure-api-review` ที่บังคับว่า endpoint ทุกตัวต้องผ่าน gateway JWT ห้ามมี anonymous route ต้อง validate input ต้องมี audit log และต้องจัดการ PII ให้ถูก skill จะทำงานเองเมื่อมีคนสร้างหรือแก้ endpoint และเจ้าของ policy เป็นคนเซ็นเวลาจะแก้ skill

### Hooks บังคับกฎที่ต่อรองไม่ได้

Hooks เป็น script ที่รันก่อนหรือหลัง action ของ Claude ในช่วง Build ใช้ห้ามแก้ path ที่ล็อกไว้ เช่น generated code หรือ package ที่ freeze รัน formatter/linter อัตโนมัติหลังแก้ไฟล์ และกัน credential ไม่ให้หลุดเข้า diff ส่วน hook ที่ต้องถามคนก่อนทำจะไปอยู่กับ approval gate ใน Stage 5

### งานขนาน: worktree กับ subagent

engineer เปิด Claude Code หลายตัวพร้อมกัน โดยให้แต่ละตัวอยู่คนละ [[git-worktrees|git worktree]] จะได้ไม่ชนไฟล์กัน ส่วน [[subagent-patterns|subagent]] ใช้กับงานที่ทำซ้ำ ๆ ในแต่ละ session เช่น verifier ที่รันแอปแล้วเช็คพฤติกรรมจริงก่อนรายงานว่าเสร็จ แต่ละตัวมี context window และ tool ของตัวเอง

เพดานจริงไม่ได้อยู่ที่เครื่อง แต่อยู่ที่ **จำนวน session ที่คนหนึ่งคนตรวจได้จริง** ตรงนี้คือ [[orchestration-tax|orchestration tax]] ที่ต้องนับ

## Stage 4 Test: ให้ Claude ตรวจงานตัวเองก่อนถึงมือคน

ปัญหาเดิมคือ feedback มาไม่พร้อมกัน CI ใช้เวลาไม่กี่นาที tester อาจตอบในอีกหลายวัน ส่วนปัญหาใน production อาจโผล่หลังผ่านไปหลายสัปดาห์ ระหว่างนั้นคนต้องคอยตรวจงาน agent ทุกชิ้นด้วยมือ

วิธีแก้ตรงไปตรงมา: มัดคำสั่ง test กับ build ให้เหลือเป้าเดียว (เช่น `make test`) เขียนไว้ใน `CLAUDE.md` ว่า output ที่ปกติหน้าตาเป็นยังไง แล้วตั้งเป้าที่วัดได้ให้ agent เช่น "test ผ่านหมด" หรือ "screenshot ตรงกับ mock" จากนั้นปล่อยให้วนรันเองจนถึงเป้า

- **งานแก้บั๊ก:** engineer เขียน failing test ก่อน แล้วให้ Claude ทำบั๊กให้เกิดซ้ำ แล้วแก้ที่ code โดยห้ามแตะไฟล์ test ใช้ hook บังคับตรงนี้ กัน [[reward-hacking|การแก้ test ให้ผ่านแทนการแก้บั๊ก]]
- **งาน UI:** ให้ agent implement แล้วถ่าย screenshot มาเทียบกับแบบ จากนั้นค่อยปรับ เอกสารบอกว่าปกติใช้ 2-3 รอบ

### Continuous evals ใน CI

ส่วนนี้ต่างจาก test ธรรมดา เพราะไม่ได้ทดสอบ code แต่ทดสอบ **configuration ที่กำกับ agent** เก็บงานจริงล่าสุดสัก 20-50 เคสพร้อมผลที่ควรได้ แล้วรันชุดนี้ทุกครั้งที่มีคนแก้ `CLAUDE.md`, skill หรือ hook ถ้า pass rate ตก ต้องมีคนดูก่อน merge

ทุก incident ที่หลุดไป production จะกลายเป็น eval ถาวรหนึ่งเคส ชุดวัดจึงโตตามความผิดพลาดที่เคยเจอจริง ตรงกับวิธีทำงานใน [[evals-and-error-analysis]]

**ได้อะไร:** agent แก้ความผิดพลาดที่ตรวจซ้ำได้ให้จบใน session ก่อนส่งให้ engineer คนจึงได้อ่านงานที่ผ่านเกณฑ์เบื้องต้นแล้ว

## Stage 5 Deploy: review กับ gate

### Claude อ่าน PR ก่อน คนอ่านทีหลัง

Claude review ทุก PR เทียบกับ policy ขององค์กร โดยนโยบายการ review เขียนไว้ใน `REVIEW.md` ที่ versioned เหมือนกัน เอกสารให้ตัวอย่างโครงประมาณนี้

- **Passes:** แยกรอบตรวจเป็น bugs (logic, edge case, regression), security (injection, ช่องโหว่ auth, PII หลุดลง log) และ compliance (ตรงกับ `spec.md`, `plan.md` และหลักการออกแบบไหม)
- **Important vs. nit:** important คือพฤติกรรมพัง ข้อมูลรั่ว หรือผิด policy ส่วน nit คือเรื่องสไตล์กับการตั้งชื่อ
- **Caps:** รายงาน nit ได้ไม่เกิน 5 ข้อต่อรอบ ที่เหลือสรุปเป็นจำนวน
- **Exclusions:** ตัด generated file และทุกอย่างที่ CI ตรวจอยู่แล้วออก

สามข้อหลังช่วยกันไม่ให้ comment เล็ก ๆ ท่วม review จนคนเลื่อนผ่าน finding ที่กระทบพฤติกรรมหรือความปลอดภัย ดู [[agentic-code-review]] และ [[dual-axis-code-review]]

เวลาจะแก้ตาม comment engineer tag `@claude` ที่ comment นั้น Claude แก้แล้ว push ให้ และ finding ที่เจอซ้ำรอบสองให้เขียนกลับลง `CLAUDE.md`

### Hooks เป็น approval gate

เอกสารให้ผู้บริหารกับฝ่าย compliance ระบุก่อนว่า gate ไหนต้องมีคนอนุมัติ แล้วให้ platform engineer แปลงแต่ละข้อเป็น hook ผลมีสามแบบ: **allow** (ผ่าน), **ask** (หยุดรอคนอนุมัติ) และ **block** (ไม่ให้ทำ) ข้อความตอนบล็อกต้องบอกทั้งเหตุผลและทางขออนุมัติ ส่วนกฎที่ต่อรองไม่ได้ให้ย้ายไปอยู่ใน managed settings ที่ engineer แก้เองไม่ได้

### CI/CD และ non-interactive mode

รัน Claude ใน pipeline ด้วย `claude -p "prompt"` เอกสารแนะนำให้ไล่ตามลำดับความเสี่ยง: เริ่มจากงานที่อ่านอย่างเดียวก่อน (วิเคราะห์ว่า build พังเพราะอะไร ร่าง changelog) แล้วค่อยขยับไปงานที่เขียน โดยยังวางไว้หลัง gate เดิม (แก้ lint ตอบ review comment)

ฝั่ง runtime ให้รันใน container ใช้ network policy และ token ที่อายุสั้นและมี scope แคบ ปกติ agent **ไม่ควรมี production credential** ส่วนคำสั่ง deploy ดูสถานะ และ rollback เปิดเป็น tool ผ่าน [[model-context-protocol|MCP]] โดยแยก scope ตาม environment

ระดับ autonomy ไล่ตาม environment: dev ปล่อยได้กว้าง staging จำกัดลงมา ส่วน production ต้องผ่าน gate Agent เดินไปถึงหน้าประตู production ได้ แต่ผ่านเองไม่ได้ เอกสารยังเน้นว่า **rollback คือเส้นทางที่ต้องซ้อมบ่อยที่สุด** จึงให้ซ้อมจริงใน staging เป็นประจำ

## Stage 6 Maintain: ปิดวงกลับไปที่ `intent.md`

ปัญหาเดิมคือ maintenance เป็นงานตั้งรับ ทุก incident รอคนเริ่ม ticket ค้างใน backlog และ action จาก post-mortem มักไปไม่ถึง code

playbook วางวิธีไว้เป็นสองชั้น ชั้นตรวจจับกับชั้นตอบสนอง แล้วแยกกันชัด

**ชั้นตรวจจับไม่ใช้ model เลย** เป็น script ธรรมดาที่เฝ้า metric เช่น อัตรา test พังใน CI, 5xx หลัง deploy, PR cycle time เทียบกับ baseline แบบ rolling แล้วใช้กฎสถิติ (Western Electric rules) จับ drift เหตุผลที่ต้อง deterministic คือการตัดสินว่า "ผิดปกติหรือยัง" ต้องให้ผลเหมือนเดิมทุกครั้งและอธิบายได้

**ชั้นตอบสนองไล่ตามระดับ** เขียนไว้ใน `bands.yaml` ที่ versioned ดูรายละเอียดที่ [[control-bands]]

```yaml
metric: ci_test_failure_rate
baseline: rolling_30d
rules: western_electric
tiers:
  1sigma: { action: log }
  2sigma: { action: diagnose, tools: "Read,Grep,Bash(gh run view *)" }
  3sigma: { action: propose, routes: [pull_request, runbook:rollback-deploy] }
```

อ่านง่าย ๆ คือ 1σ แค่บันทึกไว้ 2σ เรียก Claude มาวินิจฉัยแบบอ่านอย่างเดียว 3σ ถึงจะลงมือได้ และลงมือได้เฉพาะทางที่เปิดไว้ คือเปิด PR หรือเรียก runbook ที่อนุมัติแล้วเท่านั้น

ผลการวินิจฉัยจะเขียนเป็น `intent.md` โดยมีปัญหา หลักฐาน ผลที่อยากได้ และระบบที่กระทบ แล้วส่งกลับเข้า Stage 1 ตามปกติ on-call เป็นคน triage คิวนี้ ถ้า dismiss เคสไหนก็นำผลไปปรับ band แต่ถ้าแก้จริงให้เพิ่ม incident class นั้นลงชุด eval

### Claude Security สแกน repo ตามรอบ

สแกนทั้ง repo ที่ต่อไว้ตามตาราง (เช่นรายสัปดาห์) ใช้ model ตัวเก่งสุด (Mythos) และ **validate finding ก่อนรายงาน** พร้อมให้ค่าความมั่นใจติดมากับแต่ละข้อ finding เล็กที่ขอบเขตชัดจะกลายเป็น patch ที่เสนอผ่าน PR review ส่วน finding ใหญ่กลายเป็น `intent.md` เข้า pipeline ปกติ พอ fix ออกก็เพิ่ม vulnerability class นั้นเข้าชุด eval

### Claude Tag รับ on-call ใน Slack/Teams

Claude Tag (public beta) ให้ Claude เป็นสมาชิกใน channel ในชื่อของตัวเอง เมื่อ incident เข้ามาเป็น Slack message Claude จะทำหน้าที่ first responder ทีมกำกับทิศทางได้สด ๆ ใน channel และให้ Claude อ่าน metric ผ่าน MCP เพื่อยืนยันสิ่งที่พบ

ของแถมคือ history ใน channel กลายเป็นทั้ง audit trail และความจำสำหรับ incident ครั้งหน้า ส่วน post-mortem เขียนลงไฟล์ lessons ที่ versioned

## Governance: คนคุม loop โดยไม่ต้องลงมือทุกขั้น

Playbook นี้ไม่ได้เสนอให้ AI ทำทุกอย่าง หลักที่ใช้คือ **ควบคุมด้วย code แต่วิจารณญาณเป็นของคน**

การแยกหน้าที่ (separation of duties) ยังอยู่ครบ:

- agent ที่เขียน code อนุมัติ code ตัวเองไม่ได้ บังคับผ่าน branch protection
- ตัว reviewer อ่าน `CLAUDE.md`, skills และ hooks เพื่อใช้ policy ชุดเดียวกับทุก PR
- hook ที่ประตู production บล็อกจนกว่า release manager ที่ระบุชื่อจะอนุมัติ
- ทุก non-interactive run แยก log ว่าเป็น identity ของ agent หรือของ engineer

ชั้นควบคุมมีสามระดับ ไล่จากหลวมไปแข็ง: **skills** เป็นคำแนะนำที่ model ทำตาม, **hooks** เป็นกฎเชิงกลที่ตรวจได้แน่นอน, **managed settings** เป็นสิ่งที่ปลายทางแก้ไม่ได้ ดู [[policy-as-code-for-agents]]

### Managed settings สำหรับองค์กรที่มี regulator

สำหรับองค์กรที่กำกับเข้ม เอกสารให้ตัวอย่าง managed settings ที่ push ผ่าน MDM ประเด็นหลักของแต่ละบรรทัด:

| บรรทัด | บังคับอะไร |
| --- | --- |
| `permissions.deny` / `allow` | ปิดทางอ่าน `.env*` และ `secrets/**` ปิด `curl`/`wget`/`WebFetch` แล้วเปิด inner loop ที่ปลอดภัยไว้ล่วงหน้า (`git`, `make build/test/lint`) |
| `disableBypassPermissionsMode` + `allowManagedPermissionRulesOnly` | engineer ขยายสิทธิ์เองไม่ได้ |
| `sandbox.enabled` + `failIfUnavailable` | บังคับ isolation ระดับ OS และถ้า sandbox ใช้ไม่ได้ก็ไม่ให้รันเลย |
| `sandbox.network.allowedDomains` | ออกเน็ตได้เฉพาะ domain ที่ระบุ |
| `sandbox.credentials` | OS ปฏิเสธการอ่าน `~/.ssh`, `~/.aws/credentials` และถอด `GITHUB_TOKEN` ออกจาก env |
| `allowManagedHooksOnly` | รันได้เฉพาะ approval gate ของกลาง ของ local ไม่มีสิทธิ์ override |
| `disableSideloadFlags` + `strictKnownMarketplaces` | skill, hook และ MCP server ต้องมาจาก marketplace ขององค์กรเท่านั้น |
| `requiredMinimumVersion` | ไม่ให้สตาร์ทบน build เก่าที่ยังไม่ได้ประเมิน |

ชุดนี้ไม่ฝากความปลอดภัยไว้กับการเชื่อฟังของ agent แต่ตัดความสามารถที่ไม่ควรมีออกตั้งแต่ระดับ OS กับ network วิธีนี้ตรงกับ [[agent-runtime-untrusted|การถือว่า runtime ของ agent เป็นของที่ไว้ใจไม่ได้]]

### Audit trail

ทุก artifact ที่ commit ไม่ว่าจะเป็น intent, spec, plan, diff หรือ review finding มี timestamp กับชื่อคนจาก git ประวัติ PR เก็บว่าใครอนุมัติหรือปฏิเสธ Hook บันทึกทุกครั้งที่ allow หรือ block ส่วน session transcript ส่งเข้า observability ขององค์กรผ่าน OpenTelemetry ถ้ามีใคร dismiss finding จากการสแกนก็ต้องบันทึกเหตุผลไว้

**ผลคือ:** เวลา regulator ถามว่าใครอนุมัติอะไรเมื่อไหร่ คำตอบอยู่ใน git กับ log ไม่ต้องไปขุดจาก chat

## วัดผลยังไง

playbook แยก **leading indicator** (สัญญาณล่วงหน้า ขยับเร็ว) ออกจาก **lagging indicator** (ผลจริง ขยับช้า) ให้ทุก stage จุดที่ดีคือหลายตัวดึงจาก git กับ PR metadata ได้เลย ไม่ต้องให้คนกรอก

| Stage | Leading | Lagging |
| --- | --- | --- |
| Plan | เวลาจากคุยจนได้ `intent.md` ที่ commit (ควรเป็นชั่วโมง) | survival rate คือสัดส่วน `intent.md` ที่ product owner รับ และ rework หลังเริ่ม design |
| Design | เวลาระหว่าง commit ของ intent กับ spec | นับ commit `spec.md` ที่เกิดหลัง `plan.md` แรกของงานเดียวกัน |
| Build | สัดส่วนงานที่ merge ได้จาก implementation รอบแรก, เวลาจากอนุมัติแผนถึง merge | จำนวนรอบ rework, ความถี่ที่ diff ตรงกับ `plan.md` |
| Test | first-pass CI success rate ของงานที่ agent เขียน | เวลา review ต่อ PR (ควรลด), change failure rate |
| Deploy | เวลาถึง review ครั้งแรก (ควรเป็นนาที), สัดส่วน comment ที่ปิดได้โดยคนไม่ต้องแตะ branch | ข้อบกพร่องที่จับได้ก่อน merge เทียบกับที่หลุดไป production, ชุด [[dora\|DORA]] |
| Maintain | เวลาจาก band ทะลุถึง `intent.md` เข้าคิว triage | สัดส่วน finding ที่กลายเป็น fix ที่ merge, incident ซ้ำ class เดิม (ควรลดเมื่อ eval สะสมมากขึ้น) |

ตัววัดใน Build กับ Maintain ตอบคำถามคนละข้อ "diff ตรงกับแผนไหม" บอกว่า artifact chain ยังตามงานจริงอยู่หรือกลายเป็นพิธีกรรม ส่วน "incident ซ้ำ class เดิม" บอกว่าชุด eval ช่วยกันปัญหาเดิมได้จริงหรือแค่มีจำนวนเคสมากขึ้น

## เริ่มตรงไหนก่อน

เอกสารบอกว่าไม่ต้องเปลี่ยนทั้งหกช่วงพร้อมกัน ให้เริ่มจากของที่ทำได้โดยไม่ต้องรอส่วนอื่นก่อน สามอย่างแรกคือ

1. **`CLAUDE.md`** (Stage 3) ไม่ต้องพึ่งอะไรเลย เอาความรู้ทีมลง repo ได้ทันที
2. **`intent.md`** (Stage 1) เอาไอเดียเข้า version control
3. **Feedback loop** (Stage 4) ให้ agent ตรวจงานตัวเองก่อนถึงคน

ถ้าเป็นองค์กรใหญ่ที่ต้องเตรียมทั้งระบบ เอกสารเสนอลำดับดังนี้: กำหนดที่เก็บ intent → ใส่ `CLAUDE.md` กับ skills ใน repo → เปิด plan mode → เติม feedback loop → เปิด PR review → ตั้ง approval hook → ลง managed settings (sandbox + ปิด credential) → เพิ่ม eval ใน CI → ทำ control band กับ incident response

## ข้อจำกัดและเรื่องที่ยังตอบไม่ได้

- เอกสารนี้เป็น **vendor playbook** Anthropic เขียนถึง process ที่ประกอบขึ้นจากผลิตภัณฑ์ของตัวเองเกือบทุกชิ้น ทั้ง Claude Code, skills, hooks, managed settings, Code Review, Claude Security, Claude Tag และ MCP อ่านเป็นข้อเสนอเชิงสถาปัตยกรรมได้ แต่ไม่ใช่มาตรฐานที่เป็นกลาง
- **ไม่มีตัวเลขผลลัพธ์เลย** ไม่มีลูกค้าที่อ้างชื่อ ไม่มี before/after ไม่มีขนาดทีม เอกสารบอกว่าควรวัดอะไร แต่ไม่ได้แสดงว่าวัดแล้วได้เท่าไหร่
- ตัวเลข 20-50 เคสสำหรับ eval และ "2-3 รอบ" สำหรับ visual loop เป็นตัวอย่างในเอกสาร ไม่ใช่ผลจากการวัด
- ceremony ของ artifact สามชิ้นอาจแพงกว่าประโยชน์สำหรับงานเล็ก เอกสารไม่ได้บอกว่าเส้นแบ่งอยู่ตรงไหน เป็นปัญหาเดียวกับที่เขียนไว้ใน [[artifact-chain]]
- **เพดานที่คนตรวจไหว** เอกสารยอมรับเองว่ามีอยู่จริง แต่ไม่ได้เสนอวิธีขยาย นอกจากให้ agent กรองงานมาให้ดีขึ้น ถ้า throughput ฝั่ง build โตเร็วกว่าที่คนตรวจไหว คอขวดก็แค่ย้ายที่ ดู [[acceptance-bottleneck]]
- Continuous eval แก้ปัญหา regression ของ configuration ได้ แต่ตัวชุด eval เองก็ต้องมีคนดูแล ถ้า 20-50 เคสไม่แทนงานจริง pass rate ที่สวยก็ไม่ได้แปลว่าอะไร
- Western Electric rules ออกแบบมาสำหรับ process ในโรงงานที่ค่อนข้างนิ่ง metric ของ software delivery มี seasonality และ regime change เยอะ band ที่ไม่ปรับอาจได้ทั้ง false alarm และของที่หลุด
- ประโยคว่า agent "อาจทำถึงประตู production แต่ผ่านเองไม่ได้" จะจริงก็ต่อเมื่อ hook กับ managed settings ทำงานถูก เพราะชั้นควบคุมเหล่านี้ก็เป็น code ที่พังได้

## See also

- [[louis-claxton]]
- [[anthropic]]
- [[claude-code]]
- [[claude-codes-new-intent-md-rob-shocks]]
- [[ai-driven-sdlc]]
- [[intent-md]]
- [[artifact-chain]]
- [[control-bands]]
- [[policy-as-code-for-agents]]
- [[claude-md]]
- [[plan-mode-as-prompting]]
- [[agentic-code-review]]
- [[evals-and-error-analysis]]
- [[subagent-patterns]]
- [[git-worktrees]]
- [[orchestration-tax]]
- [[acceptance-bottleneck]]
- [[agent-runtime-untrusted]]
- [[graduated-autonomy]]
- [[spec-driven-development]]
- [[the-new-software-lifecycle]]
