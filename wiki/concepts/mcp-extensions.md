---
title: MCP Extensions
type: concept
tags: [mcp, protocols, extensions, developer-tools, oauth]
created: 2026-07-29
updated: 2026-07-29
sources: [bringing-mcp-2026-07-28-to-claude.md]
---

# MCP Extensions / ส่วนขยายของ MCP

[[model-context-protocol|Model Context Protocol (MCP)]] มี core สำหรับงานพื้นฐาน เช่นค้นหาและเรียก tool. แต่ความสามารถบางอย่างต้องมี state, UI, งาน async หรือกฎ auth เฉพาะ. MCP Extensions แยกของพวกนี้ออกจาก core เพื่อให้แต่ละ extension พัฒนาและออกรุ่นได้เอง.

นึกภาพว่า core เป็นปลั๊กมาตรฐาน. Extension คืออุปกรณ์เสริมที่เสียบเพิ่มเมื่อทั้งสองฝั่งรู้จักมัน. client ที่ไม่รองรับ extension ยังใช้ MCP พื้นฐานต่อได้.

## ทำไมไม่ใส่ทุกอย่างไว้ใน core

ถ้า Apps, long-running Tasks และ enterprise auth กลายเป็นข้อบังคับของ core ทุก MCP client ต้อง implement ทั้งหมด แม้ไม่ได้ใช้. protocol จะใหญ่ขึ้น เปลี่ยนยาก และ compatibility แตกง่าย.

MCP รุ่น `2026-07-28` จึงให้ client กับ server ประกาศ extension support ผ่าน capability negotiation. Extension เป็น opt-in. ถ้าอีกฝั่งไม่รองรับ ระบบต้อง fallback เป็นผลลัพธ์แบบ core หรือแจ้ง error ให้ชัด.

**ได้อะไร:** core ยังเล็ก ขณะที่ทีมเฉพาะทางเพิ่มความสามารถใหม่ได้โดยไม่รอ core release.

## Extension สำคัญที่ประกาศพร้อมรุ่น 2026-07-28

### MCP Apps

[MCP Apps](https://modelcontextprotocol.io/extensions/apps/overview) ให้ tool ชี้ไปที่ interactive HTML resource. host อย่าง Claude เอา UI นั้นมา render ใน sandboxed iframe ภายในบทสนทนา. ผู้ใช้จึงกด form, สำรวจ chart หรือดู dashboard ได้โดยไม่ต้องออกไป web app อีกหน้า.

app คุยกับ host ผ่าน `postMessage` และ JSON-RPC. host ยังเป็นคนคุมว่า app เรียก tool ไหน เปิด link ได้ไหม หรือขอ permission เพิ่มอย่างกล้องและไมโครโฟนได้หรือไม่.

**เหมาะกับ:** data exploration, configuration ที่มีตัวเลือกเยอะ, rich media, monitoring และ multi-step workflow.

**ได้อะไร:** UI อยู่ข้างบทสนทนาและ context เดิม แต่ยังแยกจาก host ด้วย sandbox.

### MCP Tasks

[MCP Tasks](https://modelcontextprotocol.io/extensions/tasks/overview) ออกแบบมาสำหรับงานที่ตอบทันทีไม่ได้ เช่น CI, batch processing, deployment หรือ approval จากคน. server คืน `taskId` กับสถานะก่อน แทนการเปิด connection ค้างไว้. client ค่อย poll, รับ notification, ส่ง input เพิ่ม หรือกลับมาตามผลหลัง reconnect.

สถานะหลักคือ `working`, `input_required`, `completed`, `failed` และ `cancelled`. ตัว task handle ต้อง durable เพราะประโยชน์สำคัญคือกลับมาทำต่อได้หลัง client restart หรือ network หลุด.

**ได้อะไร:** request/response core ยัง stateless ได้ แต่ state ของงานยาวมีที่อยู่ชัดและตรวจตามได้.

### Authorization extensions

กลุ่ม auth extensions เติม flow ที่ core ไม่ควรบังคับทุกระบบ เช่น:

- OAuth Client Credentials สำหรับ machine-to-machine
- Enterprise-Managed Authorization สำหรับให้ admin คุมสิทธิ์ผ่าน identity provider ขององค์กร

**ได้อะไร:** MCP ใช้ access-control เดิมขององค์กรได้โดยไม่ต้องสร้าง login และ policy ชุดใหม่แยกสำหรับ connector.

## ข้อควรระวังตอน implement

1. **อย่าดูแค่ว่า extension มี spec.** ต้องเช็ก client, server และ SDK ที่ใช้ว่ารองรับจริง.
2. **เตรียม fallback.** UI-enhanced tool ควรยังคืน text ที่มีความหมายให้ client ที่ไม่มี Apps.
3. **อย่าฝาก state ไว้ใน process โดยไม่จำเป็น.** Tasks จะทน disconnect ได้ก็ต่อเมื่อ `taskId` และสถานะถูกเก็บแบบ durable.
4. **ถือ UI เป็น untrusted content.** sandbox, CSP, permission และ tool-call policy ยังจำเป็น.
5. **ตรวจ maturity จากหลายจุด.** ณ 29 ก.ค. 2026 [extension overview](https://modelcontextprotocol.io/extensions/overview) เรียก Tasks ว่า official แต่ [repo](https://github.com/modelcontextprotocol/ext-tasks) ยังติดป้าย experimental.

## คำถามเปิด

- เส้นแบ่งไหนควรอยู่ใน core และเส้นแบ่งไหนควรเป็น extension?
- ถ้า client หลายตัวรองรับ extension ไม่เท่ากัน server ควรออกแบบผลลัพธ์ขั้นต่ำอย่างไร?
- versioning ภายใน extension จะรักษา compatibility ได้ดีกว่าการตั้ง extension identifier ใหม่แค่ไหน?
- ใครรับผิดชอบ policy เมื่อ MCP App ขอใช้ tool ของ host ที่ app ไม่ได้เป็นเจ้าของ?

## See also

- [[bringing-mcp-2026-07-28-to-claude]]
- [[model-context-protocol]]
- [[anthropic]]
- [[bring-your-own-agent]]
- [[long-running-agents]]
- [[durable-execution]]
