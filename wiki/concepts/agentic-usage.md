---
title: Agentic Usage
type: concept
tags: [ai-agents, workflows, compute-cost]
created: 2026-04-27
updated: 2026-07-03
sources: [github-copilot-billing-update.md, aaron-levie-agent-automation-jobs.md, how-ai-became-more-expensive-than-workers-it-replaced.md]
---

# Agentic Usage / การใช้งานแบบเอเจนท์

นิยามของพฤติกรรมการใช้ AI ที่ไม่ได้เป็นแค่การ "ถาม-ตอบ" ทีละครั้ง (one-off request) แต่เป็นการปล่อยให้ AI รันงานเป็น "Session" ยาวๆ มีหลายขั้นตอน และมีการตัดสินใจวนซ้ำ (loop) เพื่อให้บรรลุเป้าหมายใหญ่

## ลักษณะสำคัญ (Characteristics)
- **Multi-step**: มีการวางแผนและรันหลายคำสั่งต่อเนื่องกัน
- **Repository-wide**: ไม่ได้จำกัดแค่ไฟล์ที่เปิดอยู่ แต่สามารถ "เดิน" (traverse) ไปดูโค้ดทั้ง project ได้
- **Iterative**: มีการลองผิดลองถูก หรือการวนลูปแก้โค้ดจนกว่าจะผ่าน test
- **High Resource Demand**: ใช้ token มหาศาล ทั้งในส่วนของ context (input) และการลองสร้างคำตอบหลายๆ แบบ (output)

## ทำไมถึงต้องแยกนิยาม?
ในโลกของการพัฒนา software การขยับจาก "Autocomplete" ไปเป็น "Agentic" ทำให้ต้นทุนการประมวลผล (Inference cost) พุ่งสูงขึ้นมาก จนโมเดลการคิดเงินแบบ Buffet (จ่ายเหมา) เริ่มอยู่ไม่ได้ และต้องเปลี่ยนไปเป็น [[usage-based-billing\|Usage-based billing]]

วิดีโอ [[how-ai-became-more-expensive-than-workers-it-replaced|How AI Became More Expensive Than The Workers It Replaced]] เพิ่มมุม enterprise finance: agentic usage ไม่ได้แค่แพงกว่า autocomplete ต่อ request แต่พอทุกคนในองค์กรใช้พร้อมกัน บิล token จะคูณกับจำนวนพนักงานและจำนวนรอบลองผิดลองถูก จนกลายเป็นคำถามระดับงบประมาณ ไม่ใช่แค่ developer tooling

## ความเกี่ยวข้องในระบบต่างๆ
- **[[github-copilot]]**: ระบุว่าการเปลี่ยนไปใช้เครดิตมีสาเหตุหลักมาจากพฤติกรรมนี้
- **[[claude-code]]**: ถูกออกแบบมาเป็น Agent ตั้งแต่ต้น (Native Agentic Usage)
- **[[long-running-agents]]**: คือรูปแบบของระบบที่รองรับการใช้งานประเภทนี้

## See also
- [[subagent-patterns]]
- [[github-ai-credits]]
- [[token-optimization]]
- [[ai-token-economics]]
- [[enterprise-ai-roi]]
- [[tokenmaxxing]]
