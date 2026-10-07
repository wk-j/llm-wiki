---
title: Codemode
type: concept
tags: [ai, agents, harness, codemode, tool-calling, mcp, sandboxing]
created: 2026-10-07
updated: 2026-10-07
sources: [what-is-codemode-armin-ronacher.md]
---

# Codemode / ให้ agent เรียก tool ผ่าน code

**Codemode** คือการให้ LLM เขียน code สั้น ๆ (เช่น JavaScript) ที่เรียก tool หลายตัวต่อกัน แทนการยิง tool call ทีละครั้งผ่าน context ชื่อนี้ [[cloudflare|Cloudflare]] ตั้งก่อน ส่วนหน้านี้อิงคำอธิบายของ [[armin-ronacher|Armin Ronacher]] ใน [[what-is-codemode-armin-ronacher|What is Codemode]] ซึ่งเล่าการใช้จริงใน [[pi-agent|Pi]] 1.0

## แก่นความคิด

ปกติ agent เรียก tool แล้วผลทั้งหมดก็ไหลกลับเข้า context ถ้างานต้องเรียก 100 ครั้ง context ก็ต้องรับผล 100 ก้อน Codemode เปลี่ยนตรงนี้ model เขียน script ครั้งเดียว ตัว script วน loop, รันขนาน, กรอง, เรียง แล้วคืนแค่ผลที่ย่อแล้วกลับมา

ตัวอย่าง: agent ดึง GitHub issue 100 ตัวผ่าน `tools.bash` ส่งทุกตัวให้ [[jev|Jev]] จำแนกพร้อมกัน แล้วคืนแค่ 12 ตัวที่ผู้ใช้หงุดหงิดที่สุด context เห็นแค่ 12 บรรทัด ไม่ใช่ issue ทั้ง 100 ตัว

**ได้อะไร:** งานซ้ำ ๆ ไปอยู่ใน code ส่วน context เก็บไว้ให้การตัดสินใจ

## ทำไมไม่ใช้ bash อย่างเดียว

bash ก็ต่อคำสั่งได้อยู่แล้ว และ model คุ้นกับมันจากตอน train แต่ bash ต่อได้แค่โปรแกรมที่รันได้ บางความสามารถอยู่ในตัว harness ไม่ใช่โปรแกรม:

- ดูรูป ต้องให้ harness ฉีด image payload เข้า protocol ของ LLM `cat` ทำแทนไม่ได้
- สั่ง subagent ต้องคุยกับ harness ข้างนอก ทำผ่าน CLI ได้แต่หยาบ
- เรียก API ภายในของ harness เช่น image model หรือ classifier model

อีกเรื่องคือ bash รันฝั่ง execution environment ส่วน Codemode รันฝั่ง harness สองฝั่งนี้ระบบไฟล์ต่างกันและความเชื่อถือต่างกัน ดู [[harness-vs-execution-environment|Harness vs Execution Environment]]

**ผลคือ:** bash ยังเป็นมือที่ทำงานกับไฟล์และโปรแกรม ส่วน Codemode เป็นช่องให้ model สั่งงานหลายขั้นข้าง harness

## หน้าตาใน Pi

Pi รัน Codemode บน QuickJS ใน WASM runtime ตั้งใจตัดสิทธิ์ทิ้งเกือบหมด ไม่มี network ไม่มี file system ไม่มี timer RAM จำกัด code ทำได้อย่างเดียวคือเรียก tool ที่ harness เปิดให้ เช่น:

| API | ใช้ทำอะไร |
| --- | --- |
| `tools.bash(...)` | รันคำสั่งฝั่ง execution environment แล้วได้ output แบบมีโครงสร้าง ไม่ถูกตัดเหลือ 2,000 บรรทัดท้ายแบบ tool call ปกติ |
| `tools.mcp__<server>__<tool>(...)` | เรียก MCP tool ที่ไม่ได้ฉีด schema เข้า context |
| `models.generateImages`, `models.classify` | เรียก model ชนิดอื่นผ่าน AI SDK ของ Pi |
| `image()`, `text()` | ส่ง content กลับให้ LLM (`image()` เขียนไฟล์ชั่วคราวให้ bash ใช้ต่อได้ด้วย) |
| `store()` | เก็บข้อมูลลง session transcript ให้ Codemode รอบหน้าโหลดกลับ |

Pi จำกัด tool ที่รันพร้อมกันไว้ 4 ตัว ที่เหลือเข้าคิว script จึงใช้ `Promise.all` กับรายการยาวได้โดยไม่ท่วมระบบ Codemode เปิดเองเมื่อเปิด MCP หรือตั้ง `"defaultTools": ["+codemode"]`

## Pattern ที่ agent ใช้จริง

- **probe แล้วค่อย scale** ลองกับ 5–10 รายการก่อนดูรูปทรงข้อมูล แล้วเขียน script จัดการรายการที่เหลือ
- **fan-out แล้วย่อ** ยิงขนานไปหลาย item หรือหลาย org แล้วคืนเฉพาะสรุป
- **ให้ model เล็กตัดสิน ให้ code ลงมือ** ในตัวอย่างเกมรถถัง Jev เลือก action จากสี่ตัว (`attack`, `approach`, `dodge`, `powerup`) ส่วนฟังก์ชันธรรมดาแปลง action เป็นคำสั่งเกม ตรงกับแนว [[system-one-models|System One Models]] ที่ให้ model ตอบคำถามแคบ แล้วให้ code ถือ logic
- **เก็บผลไว้ใช้ต่อ** `store()` ทำให้ไม่ต้องคำนวณซ้ำหรือดันผลกลางทางผ่าน context

## Codemode กับ MCP

Pi ไม่ได้ส่ง MCP tool definition ให้ LLM เลย agent ใช้ tool search ใน Codemode ค้นเองว่า server ทำอะไรได้ นี่คือ [[progressive-disclosure|progressive disclosure]] อีกแบบ ต่างจาก tool search ของ [[claude-code|Claude Code]] ตรงที่ Claude Code ยังดึง schema เข้า context ให้ model เรียกเป็น tool call ส่วน Pi ให้ model เรียกผ่าน code

ปัญหาตอนนี้คือ MCP server ส่วนใหญ่ยังออกแบบให้ LLM อ่าน output เอง Armin ขอสี่อย่างจากคนทำ server: คืน structured content (ใช้ `outputSchema`), รูปทรง output คงที่ไม่ว่ามีกี่รายการ, รองรับ binary ใหญ่ และ tool search ที่ประกอบข้ามหลาย server ได้

server ที่ทำ Codemode ไว้ข้างในเอง เช่นของ Cloudflare ทำให้เกิด Codemode ซ้อน Codemode: JSON escape สองชั้น model เล็กสับสน และ code ชั้นในเรียก tool ชั้นนอกไม่ได้

**ได้อะไร:** ถ้า client เป็น code คนทำ MCP server ต้องคิดแบบคนออกแบบ API ไม่ใช่แบบคนเขียนข้อความให้ LLM อ่าน

## เรื่องที่ยังตอบไม่ได้

- **durability** script ที่รันกลางทางแล้วพังจะ resume ยังไง Armin คิดถึงการ snapshot แบบ [[durable-execution|durable workflow engine]] หรือเปลี่ยนไปใช้ภาษาที่ deterministic อย่าง Starlark
- **รูปและ binary** ยังไม่เรียบร้อย ทั้งใน Codemode และใน MCP
- **model เล็ก** ยังเขียน Codemode ได้ไม่ดีพอ
- **ไม่มีตัวเลข** บทความไม่ได้วัดว่าประหยัด token หรือทำงานสำเร็จมากขึ้นเท่าไรเทียบกับ tool call ปกติ ตัวอย่างทั้งหมดคัดมาจาก session ของผู้เขียนเอง
- **sandbox ของ Codemode ไม่ได้กั้น tool ที่มันเรียก** code ไม่มี network ก็จริง แต่ถ้าเรียก `tools.bash` หรือ MCP tool สิทธิ์ก็เป็นไปตาม tool นั้น ขอบเขตความเสียหายยังต้องคุมที่ tool และ execution environment ตามหลัก [[agent-runtime-untrusted]]

## See also

- [[what-is-codemode-armin-ronacher]]
- [[harness-vs-execution-environment]]
- [[pi-agent]]
- [[armin-ronacher]]
- [[cloudflare]]
- [[model-context-protocol]]
- [[progressive-disclosure]]
- [[jev]]
- [[system-one-models]]
- [[coding-harness]]
- [[durable-execution]]
- [[agent-runtime-untrusted]]
