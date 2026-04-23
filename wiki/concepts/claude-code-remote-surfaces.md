---
title: Claude Code Remote Surfaces / ช่องทางสั่ง Claude Code จากที่อื่น
type: concept
tags: [claude-code, remote-control, mobile, architecture]
created: 2026-04-21
updated: 2026-04-21
sources: [Remote Control - Claude Code Docs.md]
---

# Claude Code Remote Surfaces / ช่องทางสั่ง Claude Code จากที่อื่น

[[claude-code|Claude Code]] (CC) เดิมเป็น CLI ที่รันบนเครื่องตัวเอง แต่ตอนนี้ Anthropic ค่อย ๆ เปิดช่องทางให้ "สั่งงาน CC จากที่อื่น" หลายทาง ทั้งจากมือถือ, เบราว์เซอร์, Slack, cron, หรือ Telegram/Discord. ช่องทางพวกนี้ไม่ใช่ของชิ้นเดียวกัน — ต่างกันที่ **Claude รันที่ไหน** และ **อะไรเป็นตัวเริ่มงาน**. เข้าใจแกนนี้แล้วจะเลือกใช้ถูก.

## สองแกนที่ต้องแยก

**แกนที่ 1 — Claude รันที่ไหน (execution location)**
- *Local* = รันบนเครื่องเรา (CLI / Desktop / VS Code). เข้าถึง filesystem, MCP, project config ได้ทุกอย่าง
- *Cloud* = รันบน infrastructure ของ Anthropic. ไม่เห็น local files; ต้อง clone repo ใน cloud sandbox

**แกนที่ 2 — อะไรเป็น trigger**
- *Human-driven* = คนพิมพ์ข้อความเอง (interactive)
- *Event-driven* = event จากข้างนอก (CI fail, chat message, cron) มาปลุก

เอาสองแกนนี้มาแตกช่อง เห็นภาพรวมชัด.

## ตารางช่องทาง (จาก docs หน้า Remote Control)

| ช่องทาง | Trigger | Claude รันที่ | เหมาะกับ |
|---|---|---|---|
| **[[claude-code-remote-surfaces\|Dispatch]]** | ส่งงานจาก Claude mobile app | เครื่องเรา (Desktop) | ส่งงานตอนไม่อยู่โต๊ะ; setup น้อย |
| **Remote Control** | คุม session ที่รันอยู่แล้วผ่าน claude.ai/code หรือมือถือ | เครื่องเรา (CLI / VS Code) | งานที่ทำค้างไว้แล้วอยากคุมจากอีกเครื่อง |
| **Channels** | event จาก Telegram / Discord / server ของตัวเอง | เครื่องเรา (CLI) | ตอบ event ข้างนอก เช่น CI fail / chat |
| **Slack** | `@Claude` ใน channel | Anthropic cloud | PR review ใน team chat |
| **Scheduled tasks** | cron | CLI / Desktop / cloud | งานซ้ำ ๆ ตามเวลา เช่น daily review |
| **[[claude-code-on-the-web\|Claude Code on the web]]** | คนพิมพ์บน claude.ai/code | Anthropic cloud | เริ่มงานใหม่โดยไม่ต้อง setup เครื่อง; รันหลายงานขนาน |
| **[[ultraplan\|Ultraplan]]** | คนสั่งจาก terminal | Anthropic cloud (planning) + review บน browser | วางแผนงานใหญ่; review ที่หน้าจอใหญ่ |

Dispatch / Remote Control / Channels / Scheduled(CLI/Desktop) → Claude รัน *local*. Slack / web / Ultraplan → Claude รัน *cloud*.

**ได้อะไร:** รู้ว่าเลือกช่องไหน = ตัดสินใจสองเรื่องทีเดียว — "อยากเข้าถึง local files/MCP ไหม" กับ "ใครเป็นคนปลุก".

## Remote Control เจาะลึก — โมเดล "local + relay"

Remote Control คือช่องที่มีกลไกน่าสนใจที่สุดในกลุ่มนี้ เพราะมัน**ไม่ย้ายอะไรขึ้น cloud** แต่ยังคุมจากมือถือได้

- CC บนเครื่องเรายิง **outbound HTTPS only** — ไม่เปิด port ขาเข้า
- มัน register กับ Anthropic API แล้ว poll งาน
- พอเปิด claude.ai/code หรือ Claude app บนมือถือ → Anthropic ทำ relay ส่งข้อความไป-กลับระหว่าง client กับ session บนเครื่องเรา
- Traffic ทั้งหมดผ่าน TLS; credential สั้น ๆ แยก scope แยกวันหมดอายุ

หมายถึง **session ยังอยู่ local ทั้งดุ้น** — filesystem, [[model-context-protocol|MCP]] servers, project config, `@` file autocomplete — ใช้ได้หมดจากมือถือ. มือถือ/เบราว์เซอร์เป็นแค่ "หน้าต่าง" มองเข้าไป.

นี่ต่างจาก [[claude-code-on-the-web|CC on the web]] ที่ย้าย execution ขึ้น cloud ไปเลย — ไม่เห็น local files.

**ได้อะไร:** ไม่ต้อง trade-off ระหว่าง "คุมจากมือถือ" กับ "เข้าถึง local environment". แต่ trade-off ย้ายไปอยู่ที่ "ต้องเปิดเครื่องทิ้งไว้" แทน.

## สามวิธีเปิด Remote Control

1. **Server mode** — `claude remote-control`. Terminal ค้างเป็น listener. รองรับหลาย session (default 32). ใช้ flag `--spawn worktree` เพื่อให้แต่ละ session ได้ git worktree ของตัวเอง (ไม่ชนกันเวลา edit file เดียวกัน).
2. **Interactive** — `claude --remote-control` (`--rc`). เป็น CC ปกติที่พิมพ์ local ได้พร้อมคุมจาก remote ได้
3. **จาก session ที่มีอยู่แล้ว** — `/remote-control` (`/rc`) ต่อบทสนทนาเดิมไปเลย
4. **VS Code** — `/remote-control` ใน prompt box (ต้อง v2.1.79+)

เปิดอัตโนมัติทุก session: `/config` → `Enable Remote Control for all sessions` = true.

## ข้อจำกัดที่ต้องระวัง

- เครื่อง process ต้องรันค้าง — ปิด terminal = session จบ
- เน็ตหลุด >~10 นาที → session timeout, process ออก
- **[[ultraplan|Ultraplan]] เตะ Remote Control ออก** — ทั้งคู่ใช้ interface claude.ai/code ร่วมกัน ได้อย่างละอัน
- คำสั่งที่มี interactive picker (เช่น `/mcp`, `/plugin`, `/resume`) ทำได้จาก CLI อย่างเดียว. พวกที่ output เป็น text (`/compact`, `/clear`, `/context`, `/cost`, `/recap`, …) ใช้จากมือถือ/web ได้
- Auth ต้องเป็น **claude.ai OAuth session**. API key / `setup-token` / `CLAUDE_CODE_OAUTH_TOKEN` / Bedrock / Vertex / Foundry ใช้ไม่ได้

## ทำไมเรื่องนี้น่าสนใจสำหรับ wiki นี้

- ต่อกับ [[agent-runtime-untrusted|agent-runtime-untrusted]]: การที่ execution ยัง local, sandbox/permission ยังอยู่ที่ harness เครื่องเรา = boundary ของ trust ไม่เปลี่ยน. Remote แค่ดู ไม่ได้รัน. ตรงกับสต๊าประที่ OWASP APTS ตั้งไว้
- ต่อกับ [[auto-mode]]: RC เปิดจากมือถือ → เราอาจไม่ได้นั่งดู permission prompt ทันที. คู่กับ auto mode จะเหมาะ (classifier auto-approve งานปลอดภัย) แต่ถ้าเปิด `--dangerously-skip-permissions` จากมือถือ ต้องคิดหนัก
- ต่อกับ [[subagent-patterns]]: `--spawn worktree` ใน server mode = pattern fan-out ที่ระดับ session (ไม่ใช่ subagent). เหมาะสำหรับคนเดียวเปิดหลาย task ขนาน หรือหลายคนในทีมใช้เครื่อง dev cloud เดียวกัน
- Anthropic กำลังสร้าง **family of surfaces** บน claude.ai/code — Dispatch, RC, Channels, Slack, Scheduled, web, Ultraplan. ทุกอันมี job-to-be-done ต่างกันชัดเจน, ไม่ทับซ้อน

## See also

- [[claude-code]]
- [[claude-code-session-management]]
- [[auto-mode]]
- [[agent-runtime-untrusted]]
- [[subagent-patterns]]
- [[graduated-autonomy]]
