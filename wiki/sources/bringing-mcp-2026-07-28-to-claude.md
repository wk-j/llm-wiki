---
title: Bringing MCP 2026-07-28 to Claude
type: source
tags: [mcp, anthropic, claude, protocols, extensions, oauth, enterprise]
created: 2026-07-29
updated: 2026-07-29
sources: [bringing-mcp-2026-07-28-to-claude.md]
url: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
---

# Bringing MCP 2026-07-28 to Claude / นำ MCP 2026-07-28 มาใช้กับ Claude

ประกาศจาก [[anthropic|Anthropic]] วันที่ 28 ก.ค. 2026 ว่า [[model-context-protocol|Model Context Protocol (MCP)]] รุ่น `2026-07-28` เปิดตัวแล้ว และ Claude จะทยอยรองรับในเร็วๆ นี้. MCP คือมาตรฐานเปิดที่ให้ AI agent ต่อกับเครื่องมือ ข้อมูล และบริการภายนอกได้ด้วย interface เดียว.

แก่นของรุ่นนี้ไม่ใช่การเพิ่ม tool ใหม่. มันแยก **core ที่ควรเบาและรองรับ request/response** ออกจากความสามารถที่ต้องมี state เช่น UI แบบโต้ตอบหรืองานที่รันนาน. ความสามารถพวกนั้นย้ายไปอยู่ใน extensions ที่ตกลงใช้และออกรุ่นแยกจาก core ได้.

## มีอะไรใหม่ใน MCP

### Stateless core

Anthropic อธิบายว่า MCP เปลี่ยนจาก protocol แบบ bidirectional ที่อิง session state ไปเป็นโมเดล request/response. MCP server จึงไม่ต้องผูก request ชุดหนึ่งไว้กับ process หรือ connection เดิมตลอดเวลา. ทำให้เอา server ไปวางบน serverless หรือ edge infrastructure และ scale ออกหลาย instance ได้ง่ายขึ้น.

ตัวอย่างตรงไปตรงมา: request ใหม่เข้ามาแล้ว worker ตัวไหนว่างก็รับไปทำได้. ระบบไม่ต้องตามหา process เดิมเพียงเพราะมันถือ session ก่อนหน้าอยู่.

**ได้อะไร:** งานธรรมดา deploy ง่ายขึ้น ส่วน state ที่จำเป็นจริงๆ ถูกย้ายไปใช้กลไกเฉพาะแทนการบังคับให้ทั้ง protocol แบก state.

### Standardized extensions

[[mcp-extensions|MCP Extensions]] ทำให้ความสามารถเสริมเดินคนละรอบ release กับ core:

- **MCP Apps** ให้ server ส่ง interactive UI เช่น form, chart หรือ dashboard มาแสดงในบทสนทนา
- **MCP Tasks** ให้ operation ที่ใช้เวลานานคืน durable task handle ก่อน แล้ว client ค่อยตามสถานะหรือส่งข้อมูลเพิ่มภายหลัง
- **Authorization extensions** เพิ่มวิธี auth สำหรับ machine-to-machine และการจัดสิทธิ์จากระบบ identity ขององค์กร

ทั้ง client และ server ต้องประกาศว่ารองรับ extension เดียวกัน. ถ้าอีกฝั่งไม่รองรับ ควร fallback เป็น core behavior หรือปฏิเสธอย่างชัดเจน.

**ผลคือ:** เพิ่มความสามารถใหม่ได้โดยไม่ทำให้ client ทุกตัวต้องรองรับพร้อมกัน และไม่ต้องแก้ core protocol ทุกครั้ง.

### Auth hardening

ประกาศบอกว่า authorization ของ MCP เข้าใกล้การ deploy แบบ production ของ **OAuth 2.0** และ **OpenID Connect (OIDC)** มากขึ้น. MCP server จึงต่อกับ identity provider ขององค์กร เช่น Microsoft Entra หรือ Okta ได้โดยไม่ต้องสร้างทางลัดเฉพาะระบบ.

ตรงนี้ต่างจากแค่ “ล็อกอินได้”. ฝ่าย IT ต้องกำหนดได้ว่าใครใช้ connector ไหน, กลุ่มผู้ใช้ใดรับสิทธิ์อัตโนมัติ และจะถอนสิทธิ์จากศูนย์กลางอย่างไร.

**ได้อะไร:** connector เข้าไปอยู่ใต้ access policy เดิมขององค์กรได้ง่ายขึ้น.

## เสียงจากผู้ใช้ช่วง beta

บทความยก Figma, Intuit, Netlify, PostHog, Xero และ Zoom มาอธิบายผลที่คาดจากรุ่นใหม่. ใจความร่วมคือ stateless core ลดภาระเรื่อง session และช่วย scale บน HTTP infrastructure มาตรฐาน ส่วน Apps, Tasks และ enterprise auth ช่วยต่อ workflow ที่ซับซ้อนขึ้น.

คำพูดเหล่านี้เป็น testimonial ในประกาศของ Anthropic. มันบอกทิศทางและ use case ได้ แต่ยังไม่ใช่ benchmark อิสระว่ารุ่นใหม่ลดต้นทุนหรือเพิ่ม reliability ได้เท่าไร.

## MCP ใน Claude ตอนนี้

Anthropic อ้างว่า Claude มี MCP server มากกว่า 950 ตัวใน connectors directory และมีคนใช้ทุกวันหลายล้านคน. ตัวเลขนี้มาจากเจ้าของผลิตภัณฑ์เองและบทความไม่ได้เปิดวิธีนับ จึงควรเก็บเป็น source-attributed claim.

บทความสรุปชั้นผลิตภัณฑ์ที่ Anthropic ทำเพิ่มรอบ MCP:

- **MCP Apps** แสดง UI ในบทสนทนา ผู้ใช้เห็นว่า connector กำลังทำอะไรและโต้ตอบได้โดยไม่เปลี่ยน tab
- **Enterprise-managed auth** ให้ admin authorize connector ครั้งเดียว แล้วกระจายสิทธิ์ตามกลุ่มใน identity provider
- **Connector observability** ให้ผู้เผยแพร่ connector ดู adoption, error, latency และ usage แยกตามผลิตภัณฑ์ Claude
- **MCP tunnels** (research preview) ต่อ Claude เข้ากับ MCP server ใน private network โดยไม่เปิด public endpoint หรือ inbound firewall rule

**ภาพรวม:** spec แก้ฐาน protocol ส่วน Claude product เติมของที่ต้องใช้ตอนเอา connector ขึ้น production เช่น identity, visibility และ private-network access.

## จุดที่ยังไม่ควรสรุปเกิน source

### Claude ยังไม่ได้รองรับพร้อมกันทุก surface

ประกาศใช้คำว่า support กำลัง “rolling out” และจะมา “soon”. จึงยังไม่ควรตีความว่า Claude ทุกผลิตภัณฑ์รองรับ `2026-07-28`, Apps, Tasks และ auth extensions ครบแล้ว. ต้องดู support matrix หรือเอกสารของ surface ที่ใช้งานจริงอีกครั้ง.

### สถานะของ Tasks ยังแสดงไม่ตรงกันทุกหน้า

[เอกสาร MCP Extensions](https://modelcontextprotocol.io/extensions/overview) ณ 29 ก.ค. 2026 วาง Tasks ไว้กับ official extensions. แต่ [หน้า Tasks](https://modelcontextprotocol.io/extensions/tasks/overview) ยังลิงก์ไป [repo `ext-tasks`](https://github.com/modelcontextprotocol/ext-tasks) ที่ README ระบุว่า **Experimental Extension** และบอกว่ายังพัฒนาอยู่. [support matrix](https://modelcontextprotocol.io/extensions/client-matrix) ในวันเดียวกันก็ยังไม่แสดง Tasks.

ตรงนี้อาจเป็นเอกสารที่กำลังเปลี่ยนผ่านหลัง release แต่ source ที่อ่านยังไม่พอจะตัดสินว่า Tasks “graduated แล้วสมบูรณ์” หรือ “ยังทดลองอยู่บางส่วน”. ควรเช็ก repo, SEP และ client support ใหม่ก่อนใช้ใน production.

## คำถามเปิด

- Stateless core ลดภาระ server ลงจริงเท่าไร เมื่อรวม durable storage, auth และ observability ที่ production ยังต้องมี?
- client แต่ละตัวจะ fallback อย่างไรเมื่อไม่รองรับ Apps หรือ Tasks?
- Tasks จะมีสถานะ official ตรงกันใน spec, docs, repo และ SDK เมื่อไร?
- ตัวเลข 400 ล้าน SDK downloads ต่อเดือนกับ 950 connectors วัด package download, installation หรือ active usage แบบใด?

## See also

- [[model-context-protocol]]
- [[mcp-extensions]]
- [[anthropic]]
- [[claude]]
- [[bring-your-own-agent]]
- [[enterprise-model-deployment]]
