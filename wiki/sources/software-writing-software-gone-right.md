---
title: "Software Writing Software (gone right!)"
type: source
tags: [ai, neovim, lua, personal-software, developer-tools]
url: https://www.youtube.com/watch?v=HOO_yaidVWk
date_ingested: 2026-05-23
created: 2026-05-23
updated: 2026-05-23
sources: [Software Writing Software (gone right!).md]
---

# Software Writing Software (gone right!) / ซอฟต์แวร์เขียนซอฟต์แวร์แบบที่เวิร์ก

[[tj-devries|TJ DeVries]] (Neovim core maintainer และผู้ทำคอนเทนต์สาย editor) โชว์ thought experiment ชื่อ `luai.nvim`: เขียนชื่อ function หรือคำอธิบายสั้น ๆ แล้วให้ LLM สร้าง Lua function ให้ ถ้า function นั้นยังไม่มีใน runtime path ของ [[neovim|Neovim]] ก็ generate และ save ไว้ ครั้งต่อไปเรียกใช้ได้ทันทีเหมือน code ปกติ

แก่นของ talk ไม่ใช่ "ให้ AI เขียนทั้งโปรเจกต์" แต่เป็น [[just-in-time-software|just-in-time software]] ชิ้นเล็ก ๆ ที่อยู่ใน [[personalized-development-environment|personalized development environment]] ของคนเขียนเอง

## Key Takeaways

- **เป้าคือช่องว่างเล็ก ๆ ระหว่างคิดกับทำ** — TJ ไม่ได้ขาย agentic coding ขนาดใหญ่ แต่ถามว่า function เล็ก ๆ ที่เราไม่อยากเขียนเอง จะ materialize จากคำอธิบายได้ไหม
- **Generate once, reuse forever** — `luai.nvim` สร้าง Lua module เมื่อเรียก function ที่ยังไม่มี แล้วเก็บไฟล์นั้นไว้ใน runtime path. รอบต่อไปไม่ต้องรอ LLM
- **Personal software ไม่ต้อง generalize** — ตัวอย่างเช่น "search my Neovim config", "change Omarchy theme", "open floating terminal SSH to terminal.shop". สิ่งเหล่านี้อาจไม่ควร ship ให้คนอื่น แต่มีค่ามากถ้าเป็น friction ของเจ้าของเครื่อง
- **Prompt history อยู่กับ generated function** — ไฟล์ที่สร้างมี metadata/JSON เล็ก ๆ เก็บคำขอและคำแก้ เช่น `win highlight is deprecated`. เวลา improve function จึงไม่ต้องเล่าใหม่หมด
- **ระบบใช้ Lua metatables เป็น glue** — `__index` จับ function ที่ยังไม่มี, `require` หา implementation ที่ cached ไว้, และ `__call` ทำให้ table ที่มี metadata เรียกเหมือน function ได้
- **Dot prompts แทน dotfiles** — TJ เสนอเล่น ๆ ว่าแทนที่จะเก็บ config ทั้งหมดเป็น dotfiles อาจเก็บ "รายการสิ่งที่ไม่ชอบ" เป็น prompts แล้วให้ agent apply live กับเครื่องใหม่

## โครงเรื่องของเดโม

ช่วงแรก TJ วางภาพ [[personalized-development-environment|PDE]] ว่า editor เป็นแค่ส่วนหนึ่งของ environment ที่คนควรปรับได้เอง เป้าคือกำจัด papercut ที่เล็กแต่กวนใจ เช่น command ที่รู้ว่าทำได้ใน 30 วินาที แต่ผัดไปสามวันเพราะไม่อยากทำ

จากนั้นเขาเปิด `luai.nvim` แล้วเรียก function ผ่านชื่อธรรมดา เช่น `print all odd values in the table` หรือ `remove multiple white spaces from string anywhere in text`. ถ้าไม่มี implementation ระบบจะเรียก agent ให้เขียน Lua code แล้ว save ลง runtime path

พอเดโมไปถึง Neovim API ความน่าสนใจเพิ่มขึ้น เพราะ AI รู้ surface ของ editor และ plugin พอสมควร ตัวอย่าง `create floating window` พังเพราะใช้ key ที่ deprecated แล้ว TJ แก้ด้วย prompt สั้น ๆ ว่าอย่าใช้ `win highlight`. ระบบอ่าน metadata เก่า ส่งไปให้ LLM แล้วเขียน implementation ใหม่

ผลคือ workflow คล้ายการมี scratchpad ของ personal automation: ลองได้ ทิ้งได้ เก็บได้ และแก้เฉพาะจุดได้

## กลไกทางเทคนิค

`luai.nvim` ใช้ Lua module system เป็น cache layer. เมื่อเรียก field ที่ไม่มีใน module, metatable `__index` ทำงานก่อน มันลอง `require` implementation ที่มีอยู่แล้ว ถ้าเจอ ก็คืน function นั้นทันที ถ้าไม่เจอ ก็สร้าง wrapper function ที่ไปเรียก generator

ตัว generator ส่ง prompt ไปหา agent เช่น Cursor agent, Claude, Codex, หรือ local model ก็ได้ แล้วบังคับให้ตอบกลับเป็น Lua code เท่านั้น จากนั้นเก็บ code เป็น module ที่ Neovim โหลดได้

อีก trick คือ generated object ไม่ใช่แค่ function เปล่า มันเป็น table ที่มี `__call`. เลยเรียกเหมือน function ได้ แต่ยังฝัง metadata เช่น history, prompt, response, และ implementation เก่าไว้ได้

**ได้อะไร:** AI ไม่ได้อยู่ข้างนอก editor ในฐานะ chatbot แต่กลายเป็น lazy code generator ที่ผูกกับ module loading ของเครื่องมือโดยตรง

## ความหมายต่อ wiki นี้

แหล่งนี้ช่วยต่อภาพระหว่าง [[malleable-tools|malleable tools]] กับ [[coding-harness|coding harness]]. ฝั่ง Mario Zechner เน้น tool core ที่แก้ตัวเองได้ ส่วน TJ โชว์เวอร์ชัน micro: function เล็ก ๆ ใน editor ที่ generate, cache, แล้ว improve ได้

มันยังเป็นตัวอย่างที่ดีของ [[judgement-vs-automation|judgement vs automation]]: automate ส่วนที่ predictable และมี blast radius เล็ก แต่เจ้าของเครื่องยังเป็นคนตัดสินใจว่าจะเก็บ ทิ้ง หรือแก้ function ไหน

## See also

- [[tj-devries]]
- [[luaai-nvim]]
- [[neovim]]
- [[personalized-development-environment]]
- [[just-in-time-software]]
- [[malleable-tools]]
- [[coding-harness]]
