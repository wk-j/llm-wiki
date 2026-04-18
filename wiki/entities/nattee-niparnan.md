---
title: Nattee Niparnan
type: entity
tags: [person, thai, education, ai, software-engineering]
created: 2026-04-18
updated: 2026-04-18
sources: [llm-era-computer-engineering-nattee.md]
---

# Nattee Niparnan

Faculty member at the Department of Computer Engineering (CEDT), Chulalongkorn University. Author of the ongoing Facebook series *"วิศวฯคอมจะอยู่อย่างไรในยุค LLM ครองเมือง"* ("How will Computer Engineering survive in the LLM era") — a working notebook on pedagogy and practice in the LLM/Agent era.

## Teaching focus

- Data Structure, Algorithm Design, and related core-CE courses — the "bitter pill" foundation classes at Chula CEDT.
- Self-described role as a "เป็ด" (generalist): teaching, research, procurement, software development, deployment, sysadmin, even running LAN cables. Breadth of exposure feeds the series.

## cafe-grader maintainership

Current maintainer of [`cafe-grader`](https://github.com/nattee/cafe-grader-web) — the department's automated judging system where students submit code and get test-case results. Originated by อ. มะนาว **Jittat Fakcharoenphol** and อ. โป้ง **Pramook Khungurn**; Nattee took over maintenance.

Most notable recent modification: embedded an LLM "ขอ hint" button into the grader with a Socratic-only prompt and a scoring cost (−10 points per click, 70 points max after 3 clicks in-exam). See [[llm-era-computer-engineering-nattee]] for details.

## The series

Two parts ingested to date:

| Ep. | Date | Theme |
|---|---|---|
| **Ep. 1** | 2026-04-10 | LLM in the classroom and exam room — grader integration, chat-log-as-submission, prompt-as-exam experiments |
| **Ep. 2** | ~2026-04-17 | Coding Agent on a real consulting PoC — $140 in tools, no RAs hired, authorization bug war story, introduction of the "taste paradox" |

Ep. 2 promises a future installment on *using Claude Code across the full SDLC*.

## Central contribution to the wiki

- **[[taste-paradox]]** — the recursive loop where Agent-skipped practice is the same practice that builds the judgment needed to control the Agent. Nattee's most-cited original framing.
- Empirical war stories: the authorization bug, $140 vs. 3–4 RAs, the −10/click economics of help-asking during exams.
- Explicit claim that **core theory (DS/Algo/Discrete Math) becomes more important, not less** in the Agent era.

## Stance

Consistent throughout both episodes: *"คิดมาเป็นปีแล้วก็ยังคิดไม่ตกครับ"* — the series is explicitly framed as working-out-in-public, not prescription. Invites responses from working engineers. Complementary counterpart to [[panutat-tejasen|Panutat Tejasen]]'s [[harness-engineering]] framing (see [[taste-paradox]] for the dialogue).

## Colleagues mentioned in the series

Faculty name-dropped in passing (no dedicated entity pages for these):

- Jittat Fakcharoenphol (อ. มะนาว) — cafe-grader co-originator
- Pramook Khungurn (อ. โป้ง) — cafe-grader co-originator
- Ekapol Chuangsuwanich (อ. เอก) — helps source tool funding for students; referenced อ. สมชาย's prompt-as-exam format
- Dittaya Wanvarie — co-coordinates tool-cost support for students
- Mock Suwannatat (อ. ม๊อค) — workshop lead on guided-learning LLM usage and NotebookLM
- Nuttapong Chentanez (อ. ชิน) — Claude Code skill author for lecture materials
- Piyalitt Ittichaiwong (อ. อ๋า) — referenced as a pace-of-AI-progress tracker
- *"อ. สมชาย"* — Intro to Com Prog instructor using prompt-as-exam format

## See also

- [[llm-era-computer-engineering-nattee]]
- [[taste-paradox]]
- [[panutat-tejasen]]
- [[harness-engineering]]
- [[engineering-role-shift]]
