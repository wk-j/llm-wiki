---
title: Reasoning Regression
type: concept
tags: [llm, reasoning, thinking-mode, failure-mode]
created: 2026-04-28
updated: 2026-07-03
sources: [peter-gostev-what-models-suck-at.md, llm-loops-instead-of-chain-of-thought.md]
---

# Reasoning Regression / สภาวะคิดเยอะจนหลงทาง

**Reasoning Regression** คือปรากฏการณ์ที่การเพิ่มขีดความสามารถในการ "คิด" (Reasoning steps/Thinking process) ของ LLM ไม่ได้ช่วยให้ผลลัพธ์ดีขึ้น แต่กลับทำให้โมเดลพยายามหาความหมายหรือเหตุผลในเรื่องที่ไร้สาระจนเกินขอบเขต

## กลไกของปัญหา

เมื่อโมเดลที่มี Thinking mode (เช่น GPT-O series) เจอกับคำถามที่ไม่มีคำตอบหรือเป็นเรื่องหลอกลวง:
1. โมเดลจะใช้ "งบประมาณการคิด" (Thinking budget) ทั้งหมดที่มี
2. พยายามวิเคราะห์ทุกความเป็นไปได้ (Over-analysis)
3. สุดท้ายอาจจะยอมรับสมมติฐานที่ผิดนั้นเพียงเพราะต้องการจะ "ทำภารกิจให้สำเร็จ" (Goal-driven to a fault)

## ตัวอย่างจาก [[peter-gostev]]

ในบททดสอบ [[bullshitbench]] โมเดลที่ไม่มี Reasoning อาจจะตอบสั้นๆ ว่า "ฉันไม่รู้" หรือ "นี่มันไร้สาระ" ซึ่งถือว่าสอบผ่าน แต่โมเดลที่มี High Reasoning อาจจะเขียนความยาว 20 ย่อหน้าเพื่อพยายามหาความเชื่อมโยงของเรื่องไร้สาระเหล่านั้น

## บทเรียน

การมี "ตรรกะ" (Reasoning) ที่ดีต้องมาพร้อมกับ "วิจารณญาณ" (Judgment) ในการหยุดคิดหรือปฏิเสธงานที่ผิดเพี้ยนตั้งแต่ต้นทาง

## เกี่ยวกับ Chain-of-Thought และ latent reasoning

[[llm-loops-instead-of-chain-of-thought|bycloud]] เสนออีกมุมหนึ่งว่า [[chain-of-thought|chain-of-thought]] คือวิธีเพิ่ม test-time compute ผ่านข้อความ: model เขียนขั้นคิด อ่านกลับ แล้วคิดต่อ. [[looped-transformers|Looped transformer]] พยายามย้ายการคิดนี้เข้า [[latent-reasoning|latent state]] แทน

ตรงนี้ไม่ได้ลบปัญหา reasoning regression. ถ้าเพิ่ม compute โดยไม่มี judgement หรือ stop condition ที่ดี ไม่ว่าจะเพิ่มผ่าน token หรือ hidden-state loop model ก็ยังอาจคิดเยอะจนหลงทางได้. ต่างกันแค่ว่า chain-of-thought ทำให้เราเห็น trace ส่วน latent reasoning ซ่อน failure ไว้ใน activation มากกว่า

## ดูเพิ่ม

- [[bullshitbench]]
- [[eh-gland]] — สัญชาตญาณ "เอ๊ะ" ที่มนุษย์ต้องมีเพื่อดักจับปัญหานี้
- [[chain-of-thought]]
- [[latent-reasoning]]
- [[looped-transformers]]
