---
title: Claude Code Remote Surfaces / ช่องทางสั่ง Claude Code จากที่อื่น
type: concept
tags: [claude-code, remote-control, mobile, architecture]
created: 2026-04-21
updated: 2026-04-23
sources: [Remote Control - Claude Code Docs.md]
---

# Claude Code Remote Surfaces / ช่องทางสั่ง Claude Code จากที่อื่น

[[claude-code|Claude Code]] (CC) แต่เดิมเป็นเครื่องมือบรรทัดคำสั่ง (CLI) ที่ทำงานบนเครื่องคอมพิวเตอร์ของผู้ใช้ แต่ปัจจุบัน Anthropic ได้เพิ่มช่องทางต่างๆ เพื่อให้สามารถ "สั่งงาน CC จากที่อื่น" ได้หลายวิธี ไม่ว่าจะเป็นผ่านมือถือ, เว็บเบราว์เซอร์, Slack, cron, หรือแม้แต่ Telegram/Discord ช่องทางเหล่านี้มีความแตกต่างกันในสองแกนหลัก: **Claude ทำงานที่ไหน** และ **อะไรเป็นตัวกระตุ้นให้เริ่มงาน** การเข้าใจสองแกนนี้จะช่วยให้เลือกใช้เครื่องมือได้เหมาะสมกับงาน

## สองแกนที่ต้องพิจารณา

**แกนที่ 1 — Claude ทำงานที่ไหน (Execution Location)**
- *Local* = ทำงานบนเครื่องของผู้ใช้ (ผ่าน CLI / Desktop / VS Code) ซึ่งสามารถเข้าถึงไฟล์ในเครื่อง, MCP, และการตั้งค่าโปรเจกต์ได้ทั้งหมด
- *Cloud* = ทำงานบนโครงสร้างพื้นฐานของ Anthropic ซึ่งจะไม่สามารถมองเห็นไฟล์ในเครื่องได้ และต้องทำการ clone repository ใน sandbox บนคลาวด์

**แกนที่ 2 — อะไรเป็นตัวกระตุ้น (Trigger)**
- *Human-driven* = ผู้ใช้เป็นคนพิมพ์คำสั่งเอง (interactive)
- *Event-driven* = เกิดจากเหตุการณ์ภายนอก (เช่น CI fail, ข้อความในแชท, cron)

เมื่อนำสองแกนนี้มาพิจารณาร่วมกัน จะทำให้เห็นภาพรวมของแต่ละช่องทางได้ชัดเจนขึ้น

## ตารางเปรียบเทียบช่องทางต่างๆ (จากเอกสาร Remote Control)

| ช่องทาง | Trigger | Claude ทำงานที่ | เหมาะสำหรับ |
|---|---|---|---|
| **[[claude-code-remote-surfaces\|Dispatch]]** | ส่งงานจากแอป Claude บนมือถือ | เครื่องของผู้ใช้ (Desktop) | การส่งงานเมื่อไม่ได้อยู่หน้าคอมพิวเตอร์; ตั้งค่าน้อย |
| **Remote Control** | ควบคุม session ที่ทำงานอยู่แล้วผ่าน claude.ai/code หรือมือถือ | เครื่องของผู้ใช้ (CLI / VS Code) | การควบคุมงานที่ทำค้างไว้จากเครื่องอื่น |
| **Channels** | event จาก Telegram / Discord / server ของตัวเอง | เครื่องของผู้ใช้ (CLI) | การตอบสนองต่อ event ภายนอก เช่น CI fail / chat |
| **Slack** | พิมพ์ `@Claude` ใน channel | Anthropic cloud | การรีวิว PR ใน team chat |
| **Scheduled tasks** | cron | CLI / Desktop / cloud | งานที่ทำซ้ำๆ ตามเวลา เช่น daily review |
| **[[claude-code-on-the-web\|Claude Code on the web]]** | ผู้ใช้พิมพ์บน claude.ai/code | Anthropic cloud | การเริ่มงานใหม่โดยไม่ต้องตั้งค่าบนเครื่อง; สามารถรันหลายงานขนานกันได้ |
| **[[ultraplan\|Ultraplan]]** | ผู้ใช้สั่งจาก terminal | Anthropic cloud (planning) + รีวิวบนเบราว์เซอร์ | การวางแผนงานขนาดใหญ่; รีวิวบนหน้าจอใหญ่ |

Dispatch / Remote Control / Channels / Scheduled(CLI/Desktop) → Claude ทำงานแบบ *local*
Slack / web / Ultraplan → Claude ทำงานบน *cloud*

**ข้อดี:** การทราบว่าควรเลือกช่องทางไหนช่วยให้ตัดสินใจได้สองเรื่องพร้อมกัน คือ "ต้องการเข้าถึงไฟล์/MCP ในเครื่องหรือไม่" และ "ใครเป็นคนสั่งงาน"

## Remote Control เจาะลึก — โมเดล "Local + Relay"

Remote Control เป็นช่องทางที่น่าสนใจที่สุดในกลุ่มนี้ เนื่องจาก **ไม่ได้ย้ายการทำงานไปที่คลาวด์** แต่ยังสามารถควบคุมจากมือถือได้

- CC บนเครื่องของผู้ใช้จะทำการเชื่อมต่อแบบ **outbound HTTPS เท่านั้น** — ไม่มีการเปิด port ขาเข้า
- CC จะลงทะเบียนกับ Anthropic API และคอยดึงงาน (poll)
- เมื่อผู้ใช้เปิด claude.ai/code หรือแอป Claude บนมือถือ, Anthropic จะทำหน้าที่เป็นตัวกลาง (relay) ในการส่งข้อความระหว่าง client กับ session ที่ทำงานอยู่บนเครื่องของผู้ใช้
- การสื่อสารทั้งหมดถูกเข้ารหัสผ่าน TLS และใช้ credential ที่มีอายุสั้นและขอบเขตการใช้งานจำกัด

ซึ่งหมายความว่า **session ทั้งหมด ยังคงทำงานอยู่บนเครื่องของผู้ใช้** — ทำให้สามารถเข้าถึง filesystem, [[model-context-protocol|MCP]] servers, project config, และ `@` file autocomplete ได้ทั้งหมดจากมือถือ โดยที่มือถือหรือเบราว์เซอร์เป็นเพียง "หน้าต่าง" ที่ใช้มองเข้าไปเท่านั้น

ซึ่งแตกต่างจาก [[claude-code-on-the-web|CC on the web]] ที่ย้ายการทำงานทั้งหมดไปไว้บนคลาวด์ ทำให้ไม่สามารถเข้าถึงไฟล์ในเครื่องได้

**ข้อดี:** ไม่ต้องเลือกระหว่าง "การควบคุมจากมือถือ" กับ "การเข้าถึงสภาพแวดล้อมในเครื่อง" แต่ต้องแลกมาด้วยการ "ต้องเปิดเครื่องทิ้งไว้" แทน

## สามวิธีในการเปิดใช้งาน Remote Control

1.  **Server mode** — `claude remote-control` Terminal จะทำงานเป็น listener และรองรับหลาย session (ค่าเริ่มต้น 32) สามารถใช้ flag `--spawn worktree` เพื่อให้แต่ละ session มี git worktree ของตัวเอง (เพื่อไม่ให้เกิดข้อขัดแย้งเมื่อแก้ไขไฟล์เดียวกัน)
2.  **Interactive** — `claude --remote-control` (`--rc`) เป็นโหมด CC ปกติที่สามารถพิมพ์คำสั่งในเครื่องและควบคุมจาก remote ได้พร้อมกัน
3.  **จาก session ที่มีอยู่แล้ว** — `/remote-control` (`/rc`) เพื่อเชื่อมต่อกับบทสนทนาเดิม
4.  **VS Code** — `/remote-control` ใน prompt box (ต้องใช้เวอร์ชัน 2.1.79+)

หากต้องการเปิดใช้งานอัตโนมัติทุก session: `/config` → `Enable Remote Control for all sessions` = true.

## ข้อจำกัดที่ควรทราบ

-   ต้องเปิดเครื่องที่ประมวลผลทิ้งไว้ — หากปิด terminal session จะจบลง
-   หากอินเทอร์เน็ตหลุดเกิน ~10 นาที, session จะหมดเวลาและ process จะหยุดทำงาน
-   **[[ultraplan|Ultraplan]] จะยกเลิก Remote Control** — เนื่องจากทั้งสองใช้ interface ของ claude.ai/code ร่วมกัน จึงสามารถใช้ได้ทีละอย่าง
-   คำสั่งที่ต้องมีการเลือกแบบ interactive (เช่น `/mcp`, `/plugin`, `/resume`) สามารถทำได้จาก CLI เท่านั้น ส่วนคำสั่งที่ให้ผลลัพธ์เป็นข้อความ (เช่น `/compact`, `/clear`, `/context`, `/cost`, `/recap`, …) สามารถใช้จากมือถือ/เว็บได้
-   การยืนยันตัวตนต้องเป็น **claude.ai OAuth session** เท่านั้น ไม่สามารถใช้ API key / `setup-token` / `CLAUDE_CODE_OAUTH_TOKEN` / Bedrock / Vertex / Foundry ได้

## ความน่าสนใจในบริบทของ Wiki นี้

-   **เชื่อมโยงกับ [[agent-runtime-untrusted|agent-runtime-untrusted]]**: การที่ execution ยังคงอยู่บนเครื่องของผู้ใช้ และ sandbox/permission ยังถูกจัดการโดย harness ในเครื่อง หมายความว่าขอบเขตของ trust ไม่เปลี่ยนแปลง Remote เป็นเพียงการมอง แต่ไม่ได้รัน ซึ่งตรงกับหลักการที่ OWASP APTS ตั้งไว้
-   **เชื่อมโยงกับ [[auto-mode]]**: การใช้ RC จากมือถืออาจทำให้ไม่สามารถตอบสนองต่อ permission prompt ได้ทันที การใช้ร่วมกับ auto mode จึงเหมาะสม (classifier จะอนุมัติงานที่ปลอดภัยโดยอัตโนมัติ) แต่ควรระมัดระวังหากเปิดใช้ `--dangerously-skip-permissions` จากมือถือ
-   **เชื่อมโยงกับ [[subagent-patterns]]**: `--spawn worktree` ใน server mode เปรียบเสมือน pattern แบบ fan-out ในระดับ session (ไม่ใช่ subagent) เหมาะสำหรับคนเดียวที่ต้องการเปิดหลาย task พร้อมกัน หรือทีมที่ใช้เครื่อง dev cloud ร่วมกัน
-   Anthropic กำลังสร้าง **family of surfaces** บน claude.ai/code — Dispatch, RC, Channels, Slack, Scheduled, web, Ultraplan ซึ่งแต่ละอันมี job-to-be-done ที่แตกต่างกันอย่างชัดเจนและไม่ทับซ้อนกัน

## ดูเพิ่มเติม

- [[claude-code]]
- [[claude-code-session-management]]
- [[auto-mode]]
- [[agent-runtime-untrusted]]
- [[subagent-patterns]]
- [[graduated-autonomy]]
