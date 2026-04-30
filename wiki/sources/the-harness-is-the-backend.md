---
title: "The Harness Is the Backend"
type: source
tags: [agent-infrastructure, backend-architecture, iii, worker-trigger-function]
created: 2026-04-29
updated: 2026-04-29
sources: [The Harness Is the Backend.md]
---

# The Harness Is the Backend / บังเหียนคือระบบหลังบ้าน

บทความโดย [[mf-piccolo]] (2026-04-28) ผู้นำเสนอแนวคิดว่าโครงสร้างพื้นฐานของ AI Agent (Harness) ไม่ควรถูกแยกออกจากระบบหลังบ้าน (Backend) แบบเดิม แต่ควรรวมเข้าเป็นเนื้อเดียวกันผ่านชุด Primitives ที่เรียบง่าย

## สาระสำคัญ (Key takeaways)

- **Harness as Infrastructure:** ปัจจุบัน Harness (orchestration, tools, memory, context management) ถูกมองว่าเป็นส่วนที่ครอบ Model ไว้ แต่อาจถูกแยกขาดจาก Backend ดั้งเดิม ทำให้เกิดปัญหาในการ debug และความซับซ้อนในการจัดการ state
- **The Problem of Stochastic Paths:** เมื่อ Agent (ซึ่งมีความไม่แน่นอน - stochastic) ทำงานร่วมกับ Backend หลายตัว (deterministic) ความเป็นไปได้ในการเกิด error จะทวีคูณ (Agents^2 * Services) ทำให้การไล่สาย (debugging) ทำได้ยากหากระบบแยกจากกัน
- **WTF Primitives (Worker-Trigger-Function):** แนวคิดการยุบหมวดหมู่ของ Backend ให้เหลือเพียง 3 องค์ประกอบหลัก:
    - **Function:** หน่วยของงาน (Unit of work)
    - **Trigger:** สิ่งที่กระตุ้นให้งานเริ่ม (HTTP, Cron, State change)
    - **Worker:** กระบวนการที่ลงทะเบียน Function และ Trigger (รวมถึง Agent ด้วย)
- **Agent as a Worker:** ในระบบ [[iii-triple-i]], Agent ไม่ได้เรียก Backend ผ่าน integration layer พิเศษ แต่ตัว Agent เองคือ "Worker" ที่ร่วมใช้ Primitives เดียวกับระบบอื่น ทำให้สามารถใช้ Queue, State, และ Pub/Sub ได้โดยตรง
- **Recursive Infrastructure:** Agent สามารถสร้าง Worker ใหม่ (เช่น Sandbox microVM) ขึ้นมาใช้งานเองได้ในขณะ runtime (Just-in-time infrastructure)
- **Harness Debate Reframed:** ข้อพิพาทเรื่อง "Thin vs Thick Harness" (Anthropic vs LangGraph) กลายเป็นเพียงเรื่องของจำนวน Function และการประกอบ (composition) ของมันในระบบเดียวกัน

## ผลลัพธ์ (The Payoff)

การเปลี่ยนจากการมอง Harness เป็น "Temporary Scaffolding" มาเป็น "Backend Primitive" ช่วยลดความซับซ้อนของสถาปัตยกรรม (Complexity Collapse) และทำให้ระบบ Agent สามารถขยายตัว (Live Extensibility) และตรวจสอบได้ (Live Observability) อย่างแท้จริง

## See also

- [[harness-engineering]]
- [[iii-triple-i]]
- [[wtf-primitives]]
- [[mf-piccolo]]
- [[agent-runtime-untrusted]]
