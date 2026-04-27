---
title: "สรุปโพสต์ thClaws: จาก LLM Wrapper สู่ AI Harness"
author: Panutat Tejasen
date: 2026-04-26
type: source
tags: [thclaws, rust, harness-engineering, agentic-ai, claude-code]
---

# thClaws Announcement: From LLM Wrapper to AI Harness

Author: [[panutat-tejasen|Panutat Tejasen]]
Date: April 26, 2026
Original: Facebook Post

## ประเด็นสำคัญ

### 1. การเปลี่ยนผ่านสู่ Harness Engineering
*   **LLM Wrapper vs. Harness:** ในยุคแรก คนมักมองว่า App AI เป็นแค่ "LLM Wrapper" (โปรแกรมครอบ API) แต่ตอนนี้หัวใจย้ายมาอยู่ที่ **Harness Engineering** — คือการสร้าง "บังเหียน" (harness) เพื่อควบคุม "ม้าป่า" (LLM)
*   **Agentic Application:** เป็น Wrapper รุ่นใหม่ที่คุม logic ซับซ้อนรอบตัว LLM ซึ่ง logic เหล่านี้ (เช่น agentic loops, sandboxing, context compaction) คิดเป็น 99% ของ code ทั้งหมด

### 2. โปรเจกต์ thClaws
*   **ลักษณะ:** เป็นการทำ "Clean Room Port" (แกะ logic มาเขียนใหม่โดยไม่ก๊อป code) ของหัวใจ [[claude-code]] มาเป็นภาษา Rust
*   **ขนาด:** ใช้ code Rust ประมาณ 36,000 บรรทัด (เทียบกับตัวต้นฉบับที่มี 500,000+ บรรทัด)
*   **เป้าหมาย:** เพื่อศึกษาและดึงส่วน "Harness" ที่ทำให้ Claude Code เก่ง โดยเน้นที่:
    *   Agentic Loops (วงจรการคิดและทำซ้ำ)
    *   Tool routing & Sub-agent dispatch (การส่งงานต่อให้เครื่องมือหรือ sub-agent)
    *   Sandboxing (สภาพแวดล้อมปลอดภัยรัน code)
    *   [[context-compaction|Context Compaction]] (การบีบอัด context)
    *   [[model-context-protocol|MCP]] & Plugins
    *   Agent Teams (การทำงานเป็นทีมของ agent - ฟีเจอร์ที่ Panutat ชอบที่สุด)
*   **License:** Apache + MIT Dual license (Open Source)

### 3. Product Overhang
*   Panutat พูดถึงแนวคิด **[[product-overhang|Product Overhang]]**: คือการที่ model มีความสามารถอยู่แล้ว แต่ซ่อนอยู่เพราะไม่มี interface หรือเครื่องมือ (เช่น filesystem access) ให้มันใช้
*   ตัวอย่างเช่น Claude 3.5 เขียน code เก่งมา 6 เดือนแล้ว แต่คนเพิ่งรู้ตอนมี [[claude-code]] ออกมาเป็น harness ให้

### 4. ความปลอดภัยและการทำงานอัตโนมัติ
*   AI Agent คือ **LLM + Tools + Knowledge**
*   ข้อควรระวัง: แม้จะมี harness ที่ดี แต่ agent ก็ยังอาจ "หลอน" ทำนอกสั่งได้ (เช่น ลบไฟล์โดยไม่ได้สั่ง)

## อ้างอิง
*   [[thclaws]]
*   [[harness-engineering]]
*   [[product-overhang]]
*   [[claude-code]]
