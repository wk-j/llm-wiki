---
title: "Building pi in a World of Slop — Mario Zechner"
type: source
tags: [coding-agents, pi, open-source, slop, software-quality]
created: 2026-05-03
updated: 2026-07-03
sources: [Building pi in a World of Slop — Mario Zechner.md, eternal-sloptember.md]
---

# Building pi in a World of Slop / สร้าง pi ในโลกที่เต็มไปด้วย Slop

[[mario-zechner|Mario Zechner]] (ผู้สร้าง libGDX และ [[pi-agent|pi]]) ใช้ talk นี้เล่า 3 เรื่องที่ต่อกัน: ทำไมเขาสร้าง pi, ทำไม OSS เริ่มโดน agent-generated garbage กดทับ, และทำไมคนทำซอฟต์แวร์ควรช้าลงเมื่อใช้ agent

แก่นของ talk ไม่ใช่แค่ "pi ดีกว่า harness ตัวอื่น" แต่คือคำเตือนว่า agent เพิ่ม output ได้เร็วกว่าที่มนุษย์จะเข้าใจ ตรวจ และรับผิดชอบได้ ถ้าไม่มีวินัย ซอฟต์แวร์จะบวมขึ้นเร็วมาก

## Key Takeaways

- **Context ต้องเป็นของผู้ใช้**: Mario เลิกใช้ [[claude-code|Claude Code]] เพราะ harness เริ่มควบคุม context แทนผู้ใช้ ทั้ง system prompt, tool definitions, reminders, และ hidden injection เปลี่ยนได้ตาม release โดยที่ผู้ใช้มองไม่เห็นพอ
- **Minimal harness ยังแข่งได้**: [[terminalbench|TerminalBench]] แสดงให้เห็นว่า harness ที่เรียบมาก เช่น terminal/tmux interface ก็ทำคะแนนสูงได้ จึงไม่จำเป็นต้องยัด feature ทุกอย่างเข้า core
- **pi คือ self-modifying agent core**: [[pi-agent|pi]] ตั้งใจเป็น agent core ที่เล็ก แต่แก้ตัวเองได้ผ่าน documentation, examples, TypeScript extensions, custom tools, slash commands, events, providers, compaction, และ UI
- **Extension แทน marketplace silo**: Mario ไม่อยากสร้าง marketplace ใหม่ เขามองว่า package managers อย่าง npm และ GitHub ก็พอแล้ว ผู้ใช้ควร package/share extension ได้เหมือน software ปกติ
- **Clankers ทำให้ OSS เหนื่อยขึ้น**: หลัง [[pi-agent|pi]] ถูกใช้เป็น agentic core ใน OpenClaw โปรเจกต์ของ Mario โดน PR/issue garbage จาก agent มากขึ้น เขาเลยใช้ whitelist, human voice issue, vouching, labels, embeddings view, และ "OSS vacation"
- **Agent สร้าง complexity แบบ compound interest**: เมื่อปล่อยหลาย agent เขียน code โดยไม่มี bottleneck มนุษย์ error จะสะสมเร็วขึ้น และ codebase จะกลายเป็น enterprise-grade complexity ในเวลาไม่นาน
- **งาน critical ต้องอ่านทุกบรรทัด**: Mario ไม่ได้บอกว่าอย่าใช้ agent เขาเสนอให้ใช้กับงาน scope ชัด, งาน reproduce bug, งาน non-critical, งานที่มี evaluation function และยังต้องให้มนุษย์ตัดสินใจส่วนสำคัญเอง

## Act 1: ทำไมสร้าง pi

Mario เริ่มจากความไม่พอใจต่อ harness ที่โตเร็วเกินไป ฟีเจอร์เยอะขึ้นทำให้ bug เยอะขึ้น และสำคัญกว่านั้นคือ context เริ่มไม่โปร่งใส พอ harness ฉีด reminder หรือแก้ tool definition เอง model ก็เปลี่ยนพฤติกรรมโดยที่ workflow เดิมของผู้ใช้พังได้

เขาวิจารณ์ [[opencode|OpenCode]] ในมุมเดียวกัน เช่น การ prune tool output จน model เสียข้อมูลสำคัญ หรือการ inject LSP error ระหว่าง edit tool ทั้งที่มนุษย์มักเขียนให้จบก่อนค่อยเช็ค error ตรงนี้ทำให้ model สับสนเพราะ feedback เข้ามาผิดจังหวะ

ข้อสรุปของเขาคือ current coding agents ยังอยู่ในช่วงลองผิดลองถูก เราเลยควรมี [[malleable-tools|เครื่องมือที่ดัดแปลงได้]] มากกว่าเครื่องมือใหญ่ที่ตัดสินใจแทนผู้ใช้

## pi ในฐานะ agent core ที่แก้ตัวเองได้

[[pi-agent|pi]] แยกเป็น 4 package หลัก: provider abstraction, agent core, toy TUI framework, และ coding agent ตัวจริง core ของมันเล็กมาก มี tool ไม่กี่ตัว และ system prompt สั้น เพราะ Mario มองว่า model ถูก post-train มาให้รู้แล้วว่า coding agent คืออะไร ไม่ต้องอธิบายซ้ำด้วย prompt ยาว

จุดสำคัญคือ pi ship documentation และ extension examples เข้าไปให้ agent อ่าน เมื่อผู้ใช้ต้องการ subagent, plan mode, MCP, custom compaction, custom provider, หรือ UI ใหม่ ก็ให้ pi เขียน extension เองแล้ว hot reload ใน session ได้เลย

ผลคือ pi ไม่ได้แข่งด้วยจำนวน feature ใน core แต่แข่งด้วยความเร็วในการเปลี่ยน workflow ของผู้ใช้

## Act 2: OSS ในยุค clankers

หลัง pi ถูกเอาไปใช้เป็น core ของ OpenClaw โปรเจกต์ของ Mario เริ่มเจอ issue/PR จาก agent จำนวนมาก เจ้าของ repo กลายเป็นคนรับภาระ review output ที่ผู้ส่งเองอาจไม่ได้เข้าใจจริง

Mario ใช้วิธีกรองแบบมนุษย์ก่อน เช่น auto-close PR พร้อมขอให้ผู้ส่งเขียน issue แบบ human voice ถ้าเขาเห็นว่าเป็นมนุษย์จริง ก็เพิ่มชื่อเข้า whitelist รอบต่อไปค่อยส่ง PR ได้ วิธีนี้ตัด agent spam ได้ส่วนหนึ่ง เพราะ agent มักไม่กลับมาอ่าน comment แล้วทำตาม

เขายังใช้ labels เพื่อลด priority ของ issue ที่มาจาก OpenClaw, ทำ embedding view เพื่อดู cluster ของ issue/PR, และปิด tracker เป็นครั้งคราวเพื่อพักจาก maintenance load ตรงนี้ทำให้ [[clanker-slop|Clanker Slop]] ไม่ใช่แค่ปัญหาคุณภาพ code แต่เป็นปัญหา attention ของ maintainer ด้วย

## Act 3: ช้าลง

Mario เตือนว่าคำพูดแบบ "product นี้ agent สร้าง 100%" มักซ่อนปัญหาไว้ Agent ไม่ได้แค่เพิ่ม code output แต่มันเพิ่มความซับซ้อน, abstraction, duplication, compatibility layer, และ defense-in-depth ที่ไม่จำเป็นได้เร็วมาก

เขาเปรียบมนุษย์กับ agent ว่ามนุษย์เป็น bottleneck ที่มีข้อดี เพราะมนุษย์เจ็บจาก codebase ที่ซับซ้อนแล้วหยุดแก้ หรือ refactor แต่ agent จะเขียนต่อได้เรื่อยๆ แม้ codebase จะบวมจนทั้งมนุษย์และ agent อ่านไม่ไหว

หลักปฏิบัติที่เขาเสนอคือ scope งานให้เล็กพอที่ agent จะหา context ได้ครบ มี evaluation function ถ้าเป็นไปได้ ใช้ agent กับงาน boring/non-critical/reproduction/rubber duck แล้วให้มนุษย์ evaluate, take what's reasonable, finalize

## Implications

- สำหรับ [[coding-harness|coding harness]]: ความโปร่งใสของ context สำคัญเท่ากับ feature list
- สำหรับ [[vibecoded-slop|Vibecoded Slop]]: slop ไม่ได้มาจาก output แย่ทีละชิ้น แต่มาจาก output จำนวนมากที่ไม่มีคนอ่านจนสะสมเป็น system risk
- สำหรับ [[harness-engineering|Harness Engineering]]: harness ที่ดีควรช่วยให้มนุษย์เห็น, จำกัด, และตัดสินใจ ไม่ใช่แค่เพิ่ม throughput
- สำหรับ OSS: maintainer ต้องออกแบบ social protocol ใหม่ ไม่ใช่แค่ CI/test protocol
- เทียบกับ [[eternal-sloptember|The Eternal Sloptember]]: Mario ยังเชื่อว่าถ้า harness โปร่งใสและมนุษย์อ่านทัน agents มีพื้นที่ใช้ประโยชน์ได้ ส่วน Eternal Sloptember วางข้อสงสัยลึกกว่านั้นว่า process ของ LLM-style agent เองอาจไม่ใช่ programming ตั้งแต่ต้น

## See also

- [[mario-zechner]]
- [[pi-agent]]
- [[malleable-tools]]
- [[clanker-slop]]
- [[vibecoded-slop]]
- [[quality-proxy-collapse]]
- [[coding-harness]]
- [[terminalbench]]
