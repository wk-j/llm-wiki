---
title: vim.pack
type: concept
tags: [neovim, plugin-manager, lua, tooling]
created: 2026-04-17
updated: 2026-04-23
sources: [vim-pack-guide.md]
---

# vim.pack

`vim.pack` คือ [[plugin-manager]] ที่มาพร้อมกับ [[neovim|Neovim]] 0.12 ซึ่ง implement เป็น Lua module มันรวมการ install, load, และ update ไว้ใน API เดียวที่จงใจให้เล็กกว่า manager ของ third-party อย่าง `lazy.nvim` หรือ `packer.nvim`

## Public API

มีสามฟังก์ชันที่ครอบคลุมทุกอย่าง:

| ฟังก์ชัน | จุดประสงค์ |
|---|---|
| `vim.pack.add(specs)` | ติดตั้ง plugin ที่ยังไม่มีและ `packadd` มัน Idempotent — เรียกซ้ำสำหรับ plugin เดิมได้อย่างปลอดภัย |
| `vim.pack.update(names?, opts?)` | Fetch และใช้ updates. Opts: `force`, `offline`, `target = 'lockfile'` |
| `vim.pack.del(names)` | ลบ plugin ที่ติดตั้งแล้ว (หลังจากลบออกจาก config) |

spec คือ string ของ Git URL หรือ table: `{ src = '...', version = 'stable' \| 'v2.0' \| vim.version.range('2.x'), name = '...' }`

## สถาปัตยกรรม

- **plugin ทั้งหมดถูกติดตั้งเป็น "opt"** ภายใต้ directory ของ package `core` เพียงตัวเดียว ซึ่งหมายความว่าการ comment out การเรียก `vim.pack.add()` จะเป็นการปิดการใช้งาน plugin นั้นอย่างหมดจด — ไม่มีอะไรโหลดอัตโนมัติจาก `pack/start/`
- **Lockfile** (`nvim-pack-lock.json`) ในไดเรกทอรี config จะบันทึกเวอร์ชันที่แน่นอน ควร commit มัน; และห้ามแก้ไขด้วยมือเด็ดขาด
- **Hooks** จะทำงานผ่าน `PackChangedPre` / `PackChanged` autocmds ซึ่งมี `spec.name`, `active`, `kind` ∈ {`install`, `update`, `delete`}
- **Health check** ผ่าน `:checkhealth vim.pack` จะแจ้งเตือนเมื่อ lockfile ไม่ตรงและ plugin ที่ไม่ได้ใช้งาน

## ข้อแลกเปลี่ยนในการออกแบบ

สิ่งที่ `vim.pack` จงใจละเว้นเมื่อเทียบกับ `lazy.nvim`:

| ฟีเจอร์ที่ไม่มี | เหตุผล / วิธีแก้ |
|---|---|
| Declarative lazy-loading (`cmd`/`event`/`ft`/`keys`) | เขียน autocmds ด้วยมือพร้อม `once = true` ทำให้พฤติกรรมโปร่งใส |
| `opts` field สำหรับการตั้งค่า | เรียก `require('plugin').setup({...})` เองหลังจาก `vim.pack.add()` |
| `dependencies` graph | ใส่ dependency ไว้ก่อนใน `vim.pack.add()` call เดียวกัน |
| Non-Git sources | รองรับ Git เท่านั้น; source อื่นๆ ต้องติดตั้งด้วยตนเองใน `pack/*/opt/` |
| Plugin-declared hooks | วางแผนไว้เป็น `packspec`; ยังไม่ถูกปล่อยออกมา |

ข้อแลกเปลี่ยนคือ **ความโปร่งใสเชิงกลไก เหนือความสะดวกสบายแบบ declarative** — ไฟล์ config จะแสดงให้เห็นอย่างชัดเจนว่าอะไรทำงานและเมื่อไหร่

## รูปแบบการทำ Lazy-loading

เนื่องจากไม่มี DSL การทำ lazy loading จึงเป็นแค่ Lua:

```lua
-- เลื่อนการทำงานออกไปหลัง startup
vim.schedule(function()
  vim.pack.add({ 'https://github.com/nvim-mini/mini.cmdline' })
end)

-- ทำงานเมื่อมี event (ครั้งเดียว)
vim.api.nvim_create_autocmd('CmdlineEnter', {
  once = true,
  callback = function()
    vim.pack.add({ 'https://github.com/nvim-mini/mini.cmdline' })
    require('mini.cmdline').setup()
  end,
})
```

คำแนะนำของผู้เขียน [[evgeni-chasnovski|Chasnovski]]: lazy-load *อย่างพอประมาณ* ประโยชน์ด้าน startup time ที่ได้มามักไม่คุ้มกับความซับซ้อนของ config ที่เพิ่มขึ้น; `vim.loader.enable()` เพียงอย่างเดียวก็ช่วยได้ 20-30% แล้ว

## ข้อควรระวังเรื่องลำดับของ Hook

Install hook จะทำงานก็ต่อเมื่อ `PackChanged` autocmd มีอยู่ **ก่อน** ที่ `vim.pack.add()` จะรัน รูปแบบ config แบบ single-call (กำหนด autocmd ทั้งหมด → เรียก `vim.pack.add()` ครั้งเดียว) ทำให้เรื่องนี้ง่าย; แต่ถ้าไฟล์ `plugin/*.lua` กระจายกันอยู่ต้องระวังมากขึ้น

## ความสัมพันธ์กับ manager อื่นๆ

- **mini.deps** — รุ่นก่อนหน้าโดยผู้เขียนคนเดียวกัน `vim.pack` เป็นเหมือนผู้สืบทอดทางความคิดที่ถูกสร้างขึ้นมาใน core การย้ายส่วนใหญ่เป็นการเปลี่ยนชื่อ (`source`→`src`, `checkout`→`version`) และแปลง hook function เป็น autocmds
- **lazy.nvim** — manager ของ third-party ที่โดดเด่น Startup เร็วกว่าผ่าน declarative lazy loading ที่จริงจัง; มี spec DSL ที่สมบูรณ์กว่า `vim.pack` สามารถทำ performance ได้เท่ากันหากตั้งค่าอย่างระมัดระวัง แต่ไม่มีทางเทียบเท่าพลังของ declarative ได้
- **packer.nvim** — archived; `vim.pack` เข้ามาเติมเต็มช่องว่างสำหรับผู้ใช้ที่ต้องการตัวเลือกง่ายๆ ที่มาพร้อมกับโปรแกรม

## การวางตำแหน่ง

`vim.pack` เหมาะสำหรับผู้ใช้ที่มองว่าการจัดการ plugin เป็นเรื่องของระบบ (plumbing), ต้องการการรับประกันความเสถียรแบบ native, และชอบ Lua ที่ชัดเจนมากกว่า spec แบบ declarative ไม่ได้พยายามจะมาแทนที่ `lazy.nvim` สำหรับผู้ใช้ที่ต้องการความสะดวกสบายของมัน

## ดูเพิ่ม

- [[vim-pack-guide]]
- [[neovim]]
- [[evgeni-chasnovski]]
- [[plugin-manager]]
