---
title: What is Codemode
type: source
tags: [ai, agents, harness, mcp, codemode, tool-calling, sandboxing, pi]
url: https://lucumr.pocoo.org/2026/10/6/codemode/
author: Armin Ronacher
published: 2026-10-06
date_ingested: 2026-10-07
created: 2026-10-07
updated: 2026-10-07
sources: ["https://lucumr.pocoo.org/2026/10/6/codemode/"]
---

# What is Codemode / Codemode คืออะไร ถ้า bash ก็พอแล้ว

[[armin-ronacher|Armin Ronacher]] (developer open source ที่ทำ [[pi-agent|Pi]] ร่วมกับ [[mario-zechner|Mario Zechner]]) เขียนบล็อกนี้หลัง Pi 1.0 เพิ่ม MCP support ผ่าน [[codemode|Codemode]] เมื่อปีก่อนเขาเคยเขียนว่า "Code Is All You Need" และ "MCP needs code" คือให้ agent ใช้ script กับ CLI แทนการยัด custom tool หรือ MCP server เข้า context คนอ่านเลยอาจสงสัยว่า Pi กลับลำหรือเปล่า

คำตอบของ Armin คือไม่ได้กลับลำ bash ยังเป็นทางหลัก แต่มีงานบางแบบที่ bash ทำไม่ได้โดยธรรมชาติ Codemode ปิดช่องนั้น และ MCP ก็ได้ประโยชน์ไปด้วย

## Tool คืออะไร และ bash ติดตรงไหน

ส่วนนี้ปูว่าทำไม Pi ถึงเอนไปทาง bash มาตลอด และทำไม bash อย่างเดียวไม่พอ

harness อย่าง Pi ส่ง tool definition ให้ LLM แล้ว server ฝั่ง model แปลงเป็นโครงสร้าง token ส่วน model จะอยากเรียก tool แค่ไหนมาจาก reinforcement learning ตอน train (Armin เคยเขียนเรื่องนี้ใน "better models worse tools")

Pi เลือก CLI กับ bash เพราะสองเหตุผล:

- ต่อคำสั่งหลายตัวเข้าด้วยกันได้ง่าย
- model เรียนรู้ระบบไฟล์มาตอน train แล้ว พอรัน `echo foo > /tmp/test.txt` มันก็รู้เองว่าหลังจากนั้นมีไฟล์ `/tmp/test.txt`

แต่ bash มีข้อจำกัดพื้นฐาน:

> "bash has one fundamental limitation which is that it can only compose programs that run."

(bash ต่อได้แค่โปรแกรมที่รันได้)

บางอย่างไม่ใช่โปรแกรม มันต้องเป็น tool ที่ harness ถือเอง ตัวอย่างชัดสุดคือ `read` หรือ `view_image` ถ้า model แบบ multimodal จะดูรูป มันใช้ `cat` ไม่ได้ เพราะ harness ต้องฉีด payload ของรูปเข้า protocol ของ LLM เอง อีกตัวอย่างคือ subagent จะให้ agent สั่ง subagent ผ่าน CLI ที่คุยกับ harness ข้างนอกทาง environment variable กับ Unix socket ก็ทำได้ แต่หยาบ และยังติดคำถามว่า code นั้นรันที่ไหน

**ผลคือ:** bash เก่งเรื่องต่อโปรแกรม แต่ต่อความสามารถที่อยู่ในตัว harness ไม่ได้

## Brains vs Hands: harness กับที่ที่ tool รันแยกกัน

ส่วนนี้คือแกนของบทความ Armin ให้แยกระบบเป็นสองฝั่ง แล้วจะเห็นว่า Codemode ควรอยู่ฝั่งไหน

- **brain** คือตัว harness รันอยู่บนเครื่องหนึ่ง และเป็นฝั่งที่เชื่อถือได้
- **hands** คือที่ที่ tool รันจริง Pi เรียกตอนนี้ว่า **execution environment** หลายครั้งเป็นเครื่องเดียวกัน แต่ไม่จำเป็นต้องเป็น

สองฝั่งนี้มีระบบไฟล์คนละชุด และระดับความเชื่อถือต่างกัน ตัวอย่างคือ ถ้าใช้ sandbox อย่าง Gondolin (ลิงก์ในบทความชี้ไปที่ `earendil-works.github.io/gondolin`) คำสั่ง bash จะถูก sandbox ดี แต่ตัว harness ไม่ได้อยู่ใน sandbox นั้น ดูรายละเอียดที่ [[harness-vs-execution-environment|Harness vs Execution Environment]]

**ได้อะไร:** พอแยกสองฝั่งได้ ก็ตอบได้ว่างานไหนควรวิ่งใน sandbox ของ bash และงานไหนต้องวิ่งข้าง harness

## Codemode ทำอะไร

Codemode คือช่องให้ LLM เขียน code เพื่อสั่งงานหลายขั้นฝั่ง harness ไม่ใช่ฝั่ง execution environment

> "Codemode runs in the harness, in its own sandbox."

ใน Pi ตัว Codemode รันบน QuickJS ใน WASM runtime และตั้งใจจำกัดไว้ คือ ไม่มี network ไม่มี file system ไม่มี timer และ RAM จำกัด ทางเดียวที่ code ทำอะไรได้คือเรียก tool ต่อ Armin บอกว่าภาษาอาจเป็น Scheme หรืออย่างอื่นก็ได้ ส่วนชื่อ Codemode เขาให้เครดิต [[cloudflare|Cloudflare]] ที่ตั้งชื่อนี้ก่อน

สิ่งที่ได้จากการเรียก tool ผ่าน code:

- **output ใหญ่ไม่ต้องผ่าน context** ถ้าเรียก bash เป็น tool call ปกติ Pi จะใส่แค่ 2,000 บรรทัดท้ายเข้า context ที่เหลือ agent ต้องไปเปิด overflow file เอง แต่ถ้าเรียกผ่าน Codemode ฝั่ง code ได้ output ใหญ่กว่านั้นแบบมีโครงสร้าง
- **รันพร้อมกันและเขียน workflow ได้** pattern ที่ Armin เห็นบ่อยคือ agent ลองดึง 5–10 รายการก่อนเพื่อดูหน้าตา แล้วค่อยเขียน script จัดการรายการที่เหลือ
- **เก็บ state ข้ามรอบได้** เรียก `store()` แล้วข้อมูลจะถูกเก็บลง transcript ของ session ให้ Codemode รอบถัดไปโหลดกลับมาได้ state นี้อยู่ฝั่ง harness ไม่ใช่ใน sandbox
- **เปิด API ที่ไม่คุ้มทำเป็น tool** เช่น สร้างรูปด้วย image model หรือจำแนกข้อความด้วย classifier ถ้าทำเป็น tool ปกติก็เปลือง context เปล่า ๆ Pi เลยเปิดผ่าน Codemode อย่างเดียว

**ผลคือ:** model เขียน loop, fan-out และการกรองผลเองได้ โดย context เห็นแค่ผลสรุปท้ายสุด

## ตัวอย่างจาก session จริง

Armin ยกตัวอย่างจาก session ของ Pi ที่เขาใช้เอง เขาย้ำว่า code ทั้งหมดไม่มีคนเขียนเลย แค่จัดย่อหน้าใหม่ให้อ่านง่าย agent เลือกใช้ Codemode เองเมื่อเจองานที่เหมาะ หรือเมื่อผู้ใช้สั่ง

Codemode ใน Pi เปิดเป็นปกติเฉพาะตอนเปิด MCP ถ้าจะเปิดเองให้ตั้ง `"defaultTools": ["+codemode"]` ใน settings หรือสั่ง Pi ให้เปิดให้

### สร้างรูป

Pi รองรับ image generation อยู่แล้วใน AI SDK core แต่ไม่ได้เปิดเป็น tool ก่อนหน้านี้ถ้าจะใช้ต้องเขียน extension เฉพาะ หรือให้ agent รัน node เรียก API ภายในเอง ตอนนี้ agent เรียก `models.getAvailableOfType("image")` กับ `models.generateImages(...)` ใน Codemode ได้เลย

ฟังก์ชัน `image()` ส่งรูปกลับเข้า LLM เป็น image content และเขียนลงดิสก์เป็น artifact ชั่วคราวด้วย agent จะได้ส่งรูปนั้นต่อให้ bash ได้

### จำแนก issue ด้วย Jev

Armin ใช้ [[jev|Jev]] (classifier model ของ [[typesafe-ai|Typesafe AI]] ที่คืน typed answer แทนข้อความ) ทำ sentiment analysis กับ GitHub issue ทั้งก้อน:

1. ดึง model ด้วย `models.getModelOfType("classifier", "typesafe", "jev-latest")`
2. เรียก `tools.bash` รัน `gh issue list` ดึง issue ที่เปิดอยู่ 100 ตัว
3. ใช้ `Promise.all` ส่งทุก issue ให้ Jev ถามสามข้อ: `sentiment` (`choice`), `frustration` (`score` สี่ระดับ) และ `kind` (`choice`: bug, feature, question, other)
4. `store("sentiment_results", results)` เก็บผลไว้ให้รอบหน้า
5. คืนแค่ 12 issue ที่หงุดหงิดสุด เรียงตามคะแนน

`Promise.all` ตรงนี้ไม่ทำให้ระบบท่วม เพราะ Pi จำกัด tool ที่รันพร้อมกันไว้ 4 ตัว ที่เหลือเข้าคิว

ตัวอย่างนี้ยืนยันชื่อชนิดคำถาม `choice` กับ `score` ที่ [[jev-the-ultimate-classification-model|วิดีโอของ Sam Witteveen]] เล่าไว้ (ส่วน `noul` ไม่ปรากฏในบทความนี้)

### ขับเกมด้วย Jev เพื่อ debug

ตัวอย่างที่ผาดโผนกว่าคือ agent รู้จักคำสั่ง `tankctl` ของ Armin แล้วเขียน harness เล็ก ๆ ขับเกมรถถังเอง loop 30 รอบ แต่ละรอบ:

1. ขอ state เกมเป็น JSON แล้วสรุปกระสุนที่กำลังพุ่งเข้ามา
2. ส่งแผนที่แบบ text, ภัยคุกคาม และ HP ให้ Jev เลือกหนึ่งในสี่ action: `attack`, `approach`, `dodge`, `powerup`
3. ฟังก์ชัน `commandFor` แปลง action เป็นคำสั่งเกมแบบ deterministic เช่น หลบตั้งฉากกับกระสุนลูกที่ใกล้สุด
4. จด log ทุกรอบ แล้วคืน log ทั้งก้อน

ตรงนี้เห็นการแบ่งงานชัด: Jev ตัดสินว่า "ควรทำอะไร" ส่วน code ธรรมดาตัดสินว่า "ทำยังไง"

### เรียก MCP server

Pi ไม่ได้เปิด MCP tool ให้ LLM เห็นตรง ๆ agent ต้องเรียก API tool search ใน Codemode เพื่อค้นว่า server ที่ต่ออยู่ทำอะไรได้บ้าง Armin เรียกว่า progressive discovery และบอกว่าทำให้ MCP ใช้ได้ดีพอสำหรับหลายเคสแล้ว

ตัวอย่าง Sentry: agent เรียก `tools.mcp__sentry__find_organizations` ทันทีโดยไม่ค้นก่อน แล้วใช้ `Promise.allSettled` หา project ของทุก org Armin เดาว่า model น่าจะรู้หน้าตา Sentry MCP มาจากตอน RL แต่มันไม่ได้เดาลอย ๆ เพราะ system prompt บอกไว้ว่ามี Sentry server ต่ออยู่

**ได้อะไร:** ทุกตัวอย่างใช้ pattern เดียวกัน คือ code ทำงานซ้ำและงาน mechanical ส่วน context ของ LLM รับแค่ผลที่ย่อแล้ว

## Codemode ซ้อน Codemode

ส่วนนี้อธิบายว่าทำไม MCP กับ Codemode ตอนนี้ยังไม่เข้ากันเต็มที่

MCP server ส่วนใหญ่ยังออกแบบสำหรับ harness ที่ไม่มี Codemode ระหว่างนี้บาง server แก้ขัดด้วยการทำ Codemode ไว้ใน server เอง แบบที่ Cloudflare ทำ พอเอามาใช้ใน Pi ก็กลายเป็น Codemode ซ้อน Codemode

> "But now we have Codemode in Codemode which is pretty bad."

ปัญหาที่ตามมา:

- JSON ถูก escape สองชั้น
- model เล็กสับสนง่าย
- code ชั้นในเรียก tool ของชั้นนอกไม่ได้

ตัวอย่างคือ agent ต้องเขียน JavaScript ส่งเป็น string เข้า `tools.mcp__cloudflare__execute` เพื่อเรียก `cloudflare.request` อีกที แล้ว parse `content` ที่เป็น text กลับเป็น JSON เอง Armin บอกว่าไม่ดีเลย แต่ก็เข้าใจว่าทำไมถึงเป็นแบบนี้

## สิ่งที่ Armin อยากได้จาก MCP

Armin บอกตรง ๆ ว่าตอนนี้ Codemode ใช้กับ MCP ได้ "not amazingly well" เพราะ MCP server ยังไม่ได้ออกแบบมาสำหรับ harness ที่มี Codemode (เขาคิดว่าตอนนี้ harness ส่วนใหญ่รองรับแล้ว) เขาเสนอสี่ข้อ:

| ข้อ | ปัญหาวันนี้ | สิ่งที่อยากได้ |
| --- | --- | --- |
| Structured content | หลาย server คืน text ที่ code ต้อง parse เอง | คืน JSON ที่มีรูปทรงชัด; `outputSchema` ของ MCP ช่วยตรงนี้ |
| Consistent results | server บางตัวลด token ด้วยการเปลี่ยนรูป output ตามจำนวนรายการ เลยทำให้ script ที่ผ่านตอนลอง 5 รายการ พังตอนเจอ batch เต็ม | รูปทรง output เหมือนเดิมไม่ว่าผลจะมีกี่รายการ |
| Large binary data | MCP ยังส่ง binary ใหญ่ไม่ได้ ต้องอ้อมด้วย pre-signed URL ให้ upload นอก MCP | รองรับ binary ใหญ่ใน protocol |
| Composable tool search | server รู้ดีกว่า client ว่า tool ไหนเหมาะ แต่ไม่มีกลไกให้ harness กระจาย tool search ไปหลาย server พร้อมกัน ตอนนี้เป็นพฤติกรรมที่เกิดเอง และ scale ไม่ได้เมื่อมีหลาย server | กลไก tool search ที่ประกอบข้าม server ได้ |

**ผลคือ:** คนทำ MCP server ควรคิดว่า client อาจเป็น code ไม่ใช่ LLM ที่อ่าน text เอง

## อนาคตของ Codemode

Armin ปิดว่านี่ไม่ใช่การกลับลำจากที่เคยเชียร์ CLI

> "the MCP ecosystem from my perspective picked up on exactly what we pointed out a year ago works: code."

และ Codemode ไปไกลกว่า MCP ด้วย เพราะเป็นกลไกใน harness ที่ให้อิสระกับ agent มากขึ้น

เรื่องที่ยังต้องหาคำตอบ:

- **durability** ทำยากกว่าใน Codemode อาจต้องยืมไอเดียจาก durable workflow engine มา snapshot การเรียกแต่ละครั้ง หรือเปลี่ยนไปใช้ภาษาอย่าง Starlark ที่ deterministic กว่า JavaScript (ดู [[durable-execution]])
- **รูปภาพกับ binary data** ยังจัดการไม่เรียบร้อย
- **model เล็ก** ยังใช้ pattern นี้ได้ไม่ดี

## ข้อสังเกตตอน ingest

- บทความมาจากผู้สร้าง Pi เอง ตัวอย่างทั้งหมดคือ session ที่เขาเลือกมาโชว์ ไม่มีตัวเลขวัดว่า Codemode ประหยัด token หรือทำงานสำเร็จมากขึ้นเท่าไร
- หน้า [[pi-agent]] เดิมบันทึกว่า Pi ไม่มี MCP ในตัว ตามที่ Mario เล่า บทความนี้บอกว่า Pi 1.0 เพิ่ม MCP แล้ว แต่ไม่ได้ฉีด MCP tool เข้า context ตรง ๆ จึงยังเข้ากับเหตุผลเดิมเรื่องไม่อยากให้ context บวม บทความไม่ได้บอกว่า MCP อยู่ใน core หรือเป็น extension
- Codemode ใน Pi รันใน sandbox ฝั่ง harness แต่ "ไม่มี network/file system" หมายถึงตัว code ชั้นนี้ ถ้ามันเรียก `tools.bash` คำสั่งนั้นก็ไปรันฝั่ง execution environment ตามสิทธิ์ของ bash ตามปกติ

## See also

- [[codemode]]
- [[harness-vs-execution-environment]]
- [[armin-ronacher]]
- [[pi-agent]]
- [[earendil]]
- [[model-context-protocol]]
- [[progressive-disclosure]]
- [[jev]]
- [[system-one-models]]
- [[cloudflare]]
- [[coding-harness]]
- [[durable-execution]]
- [[agent-runtime-untrusted]]
