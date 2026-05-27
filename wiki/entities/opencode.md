---
title: OpenCode
type: entity
tags: [ai, tools, cli, coding, harness, open-source]
created: 2026-04-18
updated: 2026-05-27
sources: [alex-ker-harnesses-optimize.md, opencode-tauri-to-electron.md, opencode-desktop-electron-brendonovich.md, opencode-vs-claude-code-morph.md, improved-15-llms-harness-changed.md]
---

# OpenCode

Coding harness แบบ open-source — เป็นหนึ่งใน harness หลักๆ ในตลาด เทียบเคียงได้กับ [[claude-code|Claude Code]], [[openai-codex|Codex]], Cursor, Deep Agent CLI, และ Roo Code. Repo: `anomalyco/opencode` (ก่อนหน้านี้อยู่ภายใต้ SST ซึ่งรีแบรนด์เป็น **Anomaly**) License: MIT; ภาษาหลักคือ TypeScript. มี ~112K GitHub stars, 779 contributors, 80 releases ในช่วง ม.ค.+ก.พ. 2026, และมีผู้ใช้งานต่อเดือนที่อ้างว่ามี 2.5 ล้านคน (จาก Morph, ก.พ. 2026)

## ตำแหน่งในภูมิทัศน์ของ Harness (ตาม Alex Ker, 18 เม.ย. 2026)

### จุดที่เหมือนกับเจ้าอื่น

- **Skills progressive disclosure:** OpenCode, Claude Code, และ Codex ต่างก็ใช้รูปแบบเดียวกัน — คือจะโหลดแค่ชื่อและคำอธิบายของ skill ตอนเริ่มต้น; ส่วน `SKILL.md` ทั้งหมดจะถูกโหลดเมื่อต้องการใช้งาน

### การจัดการ MCP tool

OpenCode จะโหลด definition ของ MCP tool ที่ตั้งค่าไว้ทั้งหมดเข้ามาใน context ตอนเริ่ม session **เอกสารของ OpenCode เตือนผู้ใช้อย่างชัดเจนให้จำกัดจำนวน server ที่จะเปิดใช้งาน เพราะ context จะเต็มเร็วมาก** คำเตือนนี้เป็นสัญญาณในตัวเองว่า: ผู้ใช้ที่เชื่อมต่อ MCP server หลายตัวโดยไม่ควบคุม จะเจอปัญหา [[instruction-budget]] ตั้งแต่ช่วงต้นของ session

ซึ่งตรงข้ามกับ [[claude-code|Claude Code]] ที่มาพร้อม tool-search index และจะโหลด schema เมื่อต้องการใช้งาน (~85% context reduction ตามที่ Anthropic รายงาน)

## สถาปัตยกรรม

ใช้ TypeScript ทั้งระบบ (end-to-end), เป็นแบบ client-server Server (`opencode serve`) จะรัน agent loop, คุยกับ LLM, และเป็นเจ้าของ SQLite DB (ย้ายมาจาก flat files ใน v1.2.0) Client (TUI, Web UI) จะคุยกับ server ผ่าน HTTP ส่วน Desktop app มีไว้เพื่อรวม server + UI เข้าด้วยกันเป็นแอปที่ดาวน์โหลดได้ในครั้งเดียว มี **ACP** integration อย่างเป็นทางการกับ **Zed** และ **JetBrains**

### การโต้ตอบ (Interactivity - มุมมองใหม่จาก Morph, ก.พ. 2026)

เนื่องจาก server ทำงานต่อเนื่องยาวนาน และ client คุยกับมันผ่าน HTTP, OpenCode จึงให้ความสำคัญกับการควบคุม session แบบ interactive มากกว่า harness ส่วนใหญ่:

- **Tab** — สลับระหว่าง Build และ Plan agent ได้ทันที; ไม่ต้องใช้ slash command
- **@mention** — เรียก subagent ใดๆ ก็ได้แบบ inline (`@explore`, `@general`, หรือ agent อื่นๆ ที่อยู่ใน `.opencode/agents/`)
- **HTTP API** — client ใดๆ ก็ได้ (มือถือ, remote box, curl) สามารถควบคุม session ได้; เริ่มงานที่โต๊ะ, รีวิวจากมือถือ
- **Persistent sessions** — session ยังคงอยู่แม้จะปิด terminal ไปแล้ว

**ข้อแลกเปลี่ยน:** ไม่มีระบบ checkpoint/rewind เหมือน Esc×2 ของ [[claude-code|Claude Code]]; การกู้คืนต้องทำผ่าน git ด้วยตนเอง ไม่มีคำสั่งที่เทียบเท่า `/compact`; กลยุทธ์ด้าน context คือ "เริ่ม session ใหม่"

## มุม harness-as-bridge (Can Bölük, ก.พ. 2026)

[[can-boluk|Can Bölük]] ตีความการบล็อก OpenCode ว่าเป็นสัญญาณ **"อย่าสร้าง harness เอง มาใช้ของเรา"** — ทั้งที่ open harness ปรับ edit format แล้วดัน model ของ vendor เองได้ 5–14pp (ดู [[hashline]], [[improved-15-llms-harness-changed]]) Vendor ไม่ยอมปรับให้ model คู่แข่งอยู่แล้ว แต่ชุมชน open-source ทำให้ทุก model ได้ เพราะ contributor แต่ละคนใช้ model ต่างกัน

> "The model is the moat. The harness is the bridge."

## กรณี Anthropic บล็อก OAuth (9 ม.ค. 2026) และการตอบโต้ด้วย Black/Zen

Anthropic ได้บล็อก OpenCode ไม่ให้ใช้ Claude ผ่าน consumer **OAuth** token อย่างเงียบๆ OpenCode จึงถอดการรองรับ Claude Pro/Max ออกจาก codebase โดยอ้าง *"anthropic legal requests."* การเข้าถึงผ่าน API-key ยังคงใช้งานได้ มีการเปิดตัว gateway ของตัวเอง 2 ตัวเพื่อตอบโต้:

- **Black** — enterprise API gateway, มีราคา $20 / $100 / $200 ต่อเดือน
- **Zen** — gateway แบบ pay-as-you-go

OpenAI ได้แสดงท่าทีตรงกันข้ามอย่างเปิดเผย โดยยินดีต้อนรับเครื่องมือ third-party และเอ่ยชื่อ Anthropic เหตุการณ์นี้ทำให้ชุมชนแตกออกเป็นสองฝ่ายตามแนวคิดเรื่องอิสระจากผู้ให้บริการ (provider-freedom) กับการผสานรวมที่แน่นแฟ้น (integration-tightness) OpenCode ยังได้เพิ่มการรองรับ adaptive-thinking สำหรับ Sonnet 4.6 / Opus 4.6 สำหรับผู้ใช้ API-key ด้วย ที่มา: [[opencode-vs-claude-code-morph]]

## Desktop shell: Tauri → Electron (ประกาศ 25 มี.ค. 2026)

Desktop app ของ OpenCode ได้ย้ายจาก [[tauri|Tauri]] ไปยัง [[electron|Electron]] ตามที่ lead engineer **@brendonovich** บอก มีเหตุผล 3 ข้อรวมกัน:

1.  **JS server ไม่สามารถรันใน main process ของ Tauri ได้** ภายใต้ Tauri, `opencode serve` ต้องรันเป็น **sidecar** — ทำให้มีต้นทุนตอนเริ่มต้น, มี IPC latency, และปัญหาความเสถียร (โดยเฉพาะบน Windows) ในขณะที่ Node main process ของ Electron สามารถ host server ไว้ใน process เดียวกันได้
2.  **WebKit (ที่ Tauri ใช้บน macOS/Linux) มีประสิทธิภาพการเรนเดอร์และมีความไม่สอดคล้องของสไตล์ที่แย่กว่า Chromium**, ทำให้การสร้าง UI ที่สอดคล้องกันทุก platform เป็นเรื่องยาก
3.  **การย้ายจาก Bun → Node** กำลังดำเนินอยู่แล้วด้วยเหตุผลอื่น; เมื่อเสร็จสิ้น, server ก็สามารถย้ายไปอยู่ใน Node ที่มีมาให้ในตัวของ Electron ได้เลย

**ผลกระทบ:** **plugin ใดๆ ที่ใช้ Bun-specific API จะไม่ทำงานใน Desktop เวอร์ชันใหม่ๆ** — เรื่องราวทั้งหมดของ plugin จะถูกเลื่อนไปที่ OpenCode 2.0 มีการยอมรับอย่างชัดเจนว่าขนาดของ bundle จะใหญ่ขึ้น

เหตุการณ์นี้ถูกมองว่าเป็น "การเลือกเครื่องมือที่เหมาะสมกับงาน" ไม่ใช่ว่า Tauri ไม่ดี ที่มาหลัก: [[opencode-desktop-electron-brendonovich]] สรุปก่อนหน้า: [[opencode-tauri-to-electron]]

## ดูเพิ่ม

- [[claude-code]]
- [[openai-codex]]
- [[alex-ker-harnesses-optimize]]
- [[opencode-desktop-electron-brendonovich]]
- [[opencode-tauri-to-electron]]
- [[tauri]]
- [[electron]]
- [[coding-harness]]
- [[progressive-disclosure]]
- [[model-context-protocol]]
- [[opencode-vs-claude-code-morph]]
