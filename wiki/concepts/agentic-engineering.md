---
title: Agentic Engineering
type: concept
tags: [ai, engineering, agents, automation]
created: 2026-04-30
updated: 2026-07-01
sources: [Andrej Karpathy From Vibe Coding to Agentic Engineering.md, l8-principals-agentic-engineering-workflow-kun-chen.md]
---

# Agentic Engineering / วิศวกรรมเชิงเอเจนท์

**Agentic Engineering** คือระเบียบวินัยทางวิศวกรรม (Engineering Discipline) ที่เน้นการใช้ AI Agents ในการทำงานที่ซับซ้อนโดยยังคงรักษามาตรฐานคุณภาพ (Quality Bar) และความปลอดภัยของซอฟต์แวร์ระดับมืออาชีพไว้ได้ ซึ่งเป็นขั้นที่พัฒนาต่อยอดมาจาก [[vibe-coding]]

## แก่นความคิด
ในขณะที่ [[vibe-coding]] เน้นการ "ยกระดับพื้นฐาน" (Raising the floor) ให้ทุกคนเข้าถึงการสร้างซอฟต์แวร์ได้ **Agentic Engineering** เน้นการ "ยกระดับเพดาน" (Raising the ceiling) ให้กับวิศวกรมืออาชีพ เพื่อให้สามารถทำงานได้เร็วขึ้น 10x-100x โดยไม่เสียการควบคุม

- **จาก Implementer สู่ Director**: มนุษย์ไม่ได้เลิกเขียนโค้ด แต่เปลี่ยนบทบาทไปควบคุม "ทิศทาง" (Taste & Judgment) และการออกแบบระดับสูง
- **การจัดการ Jagged Intelligence**: เข้าใจว่า AI มีความสามารถแบบฟันปลา ([[jagged-intelligence]]) คือเก่งงานยากแต่พลาดงานง่าย จึงต้องมีระบบตรวจสอบ (Verification) ที่รัดกุม

## องค์ประกอบสำคัญ
1. **Spec & Planning**: การเขียนรายละเอียดและแผนงานที่ชัดเจนเพื่อให้ Agent นำไปปฏิบัติ (Execution)
2. **Verification Loop**: การใช้ระบบ Automated Tests และการตรวจสอบด้วยมนุษย์เพื่อให้มั่นใจว่า Agent ไม่ได้สร้างช่องโหว่หรือ Bug
3. **Coordination**: การจัดการ Agent หลายตัว ([[agent-swarm]]) ให้ทำงานร่วมกันในโปรเจกต์ขนาดใหญ่
4. **Agent-Native Workflow**: การปรับเปลี่ยนกระบวนการทำงานให้เอื้อต่อการทำงานของ AI (เช่น การเตรียม docs และ infra ให้ AI อ่านง่าย)

## Payoff / ผลคือ
วิศวกรสามารถขยายขอบเขตการทำงาน (Scale) ได้มหาศาล โดยหนึ่งคนสามารถคุมงานที่เคยต้องใช้ทีมงานขนาดใหญ่ได้ ในขณะที่ยังคงรักษาความสมบูรณ์แบบ (Integrity) ของระบบไว้ได้

## Captain workflow: Kun Chen

[[kun-chen|Kun Chen]] ทำให้ภาพ "director/captain" เป็น workflow ที่จับต้องได้ใน [[l8-principals-agentic-engineering-workflow-kun-chen|L8 Principal's Agentic Engineering Workflow]]. เขาไม่ได้เริ่มจาก model choice แต่เริ่มจากเรือทั้งลำ:

- terminal cockpit: [[wezterm|WezTerm]] + [[tmux]] + [[neovim|Neovim]]
- onboarding: global/project memory + skills แบบ [[progressive-disclosure]]
- planning: [[lavish|Lavish]] สร้าง HTML artifact ให้คน feedback requirement ก่อนลงมือ
- execution: agent หลายตัวใน [[git-worktrees|worktree]] แยกผ่าน [[treehouse|Treehouse]]
- validation: [[no-mistakes|No Mistakes]] ทำ adversarial review, E2E evidence, docs/lint/PR babysitting
- delegation layer: [[first-mate|First Mate]] คุม crew แทนการสลับ tab เอง

ตรงนี้ทำให้ Agentic Engineering ชัดขึ้น: คนไม่ได้หายไปจากระบบ แต่ย้ายไปอยู่จุดที่ต้องใช้ judgement สูงสุด — เลือกทิศทาง, clear requirement, ดู evidence, และตัดสิน risk.

**ผลคือ:** leverage ไม่ได้มาจาก agent จำนวนมากอย่างเดียว แต่มาจาก harness ที่ทำให้ agent ทำงานยาว ตรวจตัวเองได้ และเรียกคนเฉพาะตอนที่ต้องใช้วิจารณญาณ.

## บทบาทที่เปลี่ยนไป: Tactical vs Strategic
[[matt-pocock]] เสริมมุมมองว่าใน Agentic Engineering:
- **AI คือ Tactical Sergeant**: รับหน้าที่ "จ่า" คอยคุมการรบหน้างาน จัดการรายละเอียดโค้ดและ implementation
- **มนุษย์คือ Strategist**: รับหน้าที่ "นักยุทธศาสตร์" ออกแบบโครงสร้าง (Interface), ควบคุมทิศทาง และจัดการความซับซ้อนภาพรวม

## ดูเพิ่ม
- [[vibe-coding]]
- [[software-3-0]]
- [[jagged-intelligence]]
- [[agent-swarm]]
- [[andrej-karpathy]]
- [[matt-pocock-software-fundamentals]]
- [[deep-modules]] — เครื่องมือสำคัญในการทำ Strategic design ร่วมกับ AI
- [[l8-principals-agentic-engineering-workflow-kun-chen]]
- [[kun-chen]]
- [[no-mistakes]]
- [[first-mate]]
