---
title: Model Elicitation
type: concept
tags: [ai, models, capabilities, product-design, experimentation]
created: 2026-09-10
updated: 2026-09-10
sources: [boris-cherny-cut-80-percent-claude-code-prompt.md]
---

# Model Elicitation / ดึงความสามารถของ model ออกมาใช้

**Model elicitation** คือการจัดโจทย์ tool context และ feedback ให้ model แสดงความสามารถที่มีอยู่แล้วออกมา ไม่ใช่การ train ความสามารถใหม่ คำถามหลักคือ “model วันนี้ทำอะไรได้ ถ้าเราเปิดทางให้ถูก” มากกว่า “ต้องเขียน prompt วิเศษว่าอะไร”

[[boris-cherny|Boris Cherny]] อธิบายแนวคิดนี้ใน [[boris-cherny-cut-80-percent-claude-code-prompt|บทสัมภาษณ์กับ Y Combinator]] เขาแนะนำให้มอบงานที่ยากกว่าขอบเขตที่เราคิดว่า model ทำได้เล็กน้อย ระบุ guardrail กับ exit criteria แล้วให้เครื่องมือตรวจงานระหว่างทาง จากนั้นค่อยดู failure จริงและเติม context, skill หรือ prompt เท่าที่จำเป็น

## ต่างจาก prompt engineering อย่างไร

Prompt engineering มักโฟกัสถ้อยคำที่ส่งเข้า model ส่วน elicitation มองทั้งระบบ:

- โจทย์กว้างพอให้ model เลือกวิธีเองหรือไม่
- มี tool ที่ทำ action จริงหรือยัง
- มี context ที่ต้องใช้ ณ จังหวะนั้นหรือไม่
- มี verifier ที่บอกได้ว่างานดีขึ้นหรือถอยลงหรือไม่
- harness กำลังช่วย หรือกำลัง [[product-overhang|hobble]] model ด้วยขั้นตอนจากรุ่นเก่า

Prompt ยังมีประโยชน์ แต่เป็นเพียง knob หนึ่งในระบบทดลอง

## ตัวอย่างจาก source

- Claude 3.5 Sonnet เขียนได้ทั้งไฟล์ แต่ product ยุคนั้นยังจำกัดไว้ที่ autocomplete/chat จน Claude Code เปิด terminal และ write access
- Bun rewrite จาก Zig เป็น Rust เกิดขึ้นได้เมื่อ model มี test suite, compiler, CI และ workflow ให้ตรวจตัวเอง
- งาน rewrite Electron เป็น Swift มี macOS runner กับ screenshot comparison เป็น feedback แม้ตอนสัมภาษณ์จะยังไม่เสร็จ
- การให้ Opus 5 วาดภาพด้วย OpenCV เป็น exploratory elicitation: ยังไม่ต้องมี business case ก็ใช้ค้น capability ที่ไม่มีใครนึกถึงได้

**ได้อะไร:** ความยากของงานไม่ต้องถูกซ่อนจาก model แต่ต้องมีทางให้มันรู้ว่ากำลังไปถูกหรือผิด

## ข้อควรระวัง

- งานรันได้นานไม่เท่ากับงานถูก ต้องแยก duration ออกจาก completion
- verifier ที่แคบอาจถูก optimize จนผ่านโดยไม่ตรงเจตนา ดู [[reward-hacking]]
- autonomy ที่สูงขึ้นต้องเพิ่ม permission boundary และ observability ตาม blast radius
- demo ที่น่าทึ่งหนึ่งครั้งยังไม่บอก reliability, cost หรือ acceptance rate ใน production

## See also

- [[product-overhang]]
- [[coding-harness]]
- [[prompt-ablation]]
- [[evals-and-error-analysis]]
- [[behavioral-verifier]]
- [[long-running-agents]]
- [[dynamic-workflows]]
- [[reward-hacking]]
