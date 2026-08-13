---
title: About Stacked Pull Requests — GitHub Docs
type: source
tags: [github, pull-requests, git, code-review, ci, agents]
created: 2026-08-04
updated: 2026-08-04
sources: [about-stacked-pull-requests-github-docs.md]
url: https://docs.github.com/en/pull-requests/get-started/about-stacked-prs
---

# About Stacked Pull Requests — GitHub Docs / รู้จัก Stacked Pull Requests บน GitHub

เอกสารทางการของ [[github|GitHub]] อธิบาย [[stacked-pull-requests|stacked pull requests]] (PR หลายชั้นที่ต่อกันเป็นสาย) ในฐานะวิธีแบ่ง change ใหญ่เป็น PR เล็กที่ review และ merge แยกกันได้ โดยไม่ต้องรอให้ PR ก่อนหน้ารวมเข้า trunk ก่อนค่อยเริ่มงานถัดไป

ณ วันที่อ่าน 4 ส.ค. 2026 ฟีเจอร์นี้ยังเป็น **public preview** และอาจเปลี่ยนได้ รายละเอียดเรื่องคำสั่ง API และ surface ที่รองรับจึงควรเช็กเอกสารล่าสุดก่อนเอาไปวาง workflow ระยะยาว

## Stack หนึ่งชุดหน้าตาอย่างไร

Stack ต้องมี PR อย่างน้อยสองตัวใน repository เดียวกัน PR ล่างสุดชี้ไปที่ trunk ซึ่งมักเป็น `main` ส่วน PR ชั้นถัดไปชี้ไปที่ branch ของ PR ที่อยู่ข้างล่าง

```text
main
└── feat/auth       → PR #1, base: main
    └── feat/api    → PR #2, base: feat/auth
        └── feat/ui → PR #3, base: feat/api
```

งานฐานอย่าง shared type หรือ database schema อยู่ชั้นล่าง งานที่ต้องใช้ฐานนั้น เช่น API และ UI อยู่ชั้นสูงขึ้น แต่ละ PR แสดงเฉพาะ diff ระหว่าง branch ของตัวเองกับ branch ข้างล่าง reviewer จึงไม่ต้องอ่าน change ทั้งก้อนซ้ำทุกครั้ง

หลักสำคัญคือ ถ้า code ชั้นหนึ่งพึ่งอีกชั้น dependency ต้องอยู่ branch เดียวกันหรืออยู่ต่ำกว่า พอเปลี่ยน concern เช่น backend ไป frontend, core logic ไป test หรือก้อนปัจจุบันใหญ่พอ review แล้ว จึงค่อยแตก branch ชั้นใหม่

**ได้อะไร:** dependency ใน code ตรงกับ dependency ใน PR ทำให้คนอ่านเห็นทีละชั้นโดยไม่เสียลำดับของงาน

## ทำไม GitHub ถึงทำ stack เป็น feature โดยตรง

ทีมทำ stacked PR แบบ manual ได้อยู่แล้ว แต่ต้องคอย rebase branch หลายชั้น ไล่ดูว่า CI รันครบหรือไม่ และเปิด PR ทีละตัวเพื่อปะติดปะต่อ context GitHub จึงเพิ่มมุมมองและ operation ที่จัดการทั้งสายเป็นหน่วยเดียว

### Cascading rebase

GitHub ทำ rebase ไล่ขึ้นทั้ง stack ได้จาก server หรือผ่าน extension `gh stack` ใน GitHub CLI พอ merge PR ล่างสุด branch ที่เหลือจะถูก rebase ต่อกัน และ PR ชั้นถัดไปจะเปลี่ยนไปชี้ default base branch โดยอัตโนมัติ

**ได้อะไร:** ลดงาน sync branch ที่ทำมือแล้วพลาดง่าย โดยเฉพาะเมื่อฐานชั้นล่างเปลี่ยนระหว่าง review

### Stack map และสถานะรวม

หน้า PR แสดงหมายเลขชั้นและ stack map ใน merge box แผนที่นี้บอกว่า PR ไหนอยู่ตรงไหน สถานะเป็นอย่างไร และกดข้ามไปแต่ละชั้นได้

**ได้อะไร:** reviewer เห็นทั้ง diff เล็กตรงหน้าและตำแหน่งของมันใน change ใหญ่พร้อมกัน

### Rules และ CI ครบทุกชั้น

ข้อกำหนดการ merge ของทุก PR อิง base branch ของ PR ล่างสุด ปกติคือ `main` ดังนั้น branch protection เช่น CODEOWNER approval และ CI ที่ปกติรันเมื่อเปิด PR เข้า default branch จะถูกบังคับกับ PR กลาง stack ด้วย

**ได้อะไร:** การแบ่งงานเป็นชั้นไม่ทำให้ PR ด้านบนหลุด quality gate เพียงเพราะมันชี้ไปที่ feature branch

### Automation มองเห็น stack

GitHub เปิดข้อมูล stack ผ่านหลายทาง:

- Webhook `pull_request` มี object `stack` เพื่อแจ้งตอน PR เข้า ย้ายตำแหน่ง หรือออกจาก stack
- REST API อ่าน membership และสั่ง list, create, extend หรือ dissolve stack ได้
- GraphQL เปิด field แบบ read-only เพื่อ query stack และตำแหน่งของ PR

**ได้อะไร:** dashboard, bot และ workflow ภายในองค์กรใช้ dependency เดียวกับที่คนเห็นในหน้า GitHub ได้

## Merge อย่างไร

PR ต้อง merge จากล่างขึ้นบน แต่ผู้ใช้สั่งรวมได้หลายขนาด:

- merge PR ล่างสุดเพื่อรวมทีละชั้น แล้วให้ GitHub rebase ชั้นที่เหลือ
- merge PR กลางเพื่อรวม PR ตัวนั้นพร้อมทุกชั้นที่อยู่ข้างล่าง ส่วนชั้นบนยังเปิดต่อและถูก retarget
- merge PR บนสุดเพื่อรวมทั้ง stack ในครั้งเดียว

Stack รองรับ merge commit, squash และ rebase merge รวมถึงทำงานร่วมกับ merge queue ประวัติ commit ที่ได้ควรเหมือน merge PR ทีละตัวจากล่างขึ้นบน

ถ้า automation merge ผ่าน API ต้องย้ายไปใช้ merge API สำหรับ stack ตามที่เอกสารลิงก์ไว้ ไม่ควรสมมติว่า endpoint เดิมให้ semantics เดียวกัน

**ผลคือ:** ทีมเลือกได้ว่าจะทยอยส่งของ หยุดครึ่งทาง หรือรวมทั้งสาย โดย dependency order ยังเหมือนเดิม

## ใช้ได้ที่ไหนและติดข้อจำกัดอะไร

เอกสารระบุว่ารองรับ GitHub CLI, เว็บไซต์, GitHub Mobile, Webhooks, REST API, GraphQL และ agent ผ่าน skill `gh-stack`

ข้อจำกัดที่ระบุชัดมีสองข้อ:

- branch ทุกชั้นต้องอยู่ repository เดียวกัน จึงทำ cross-fork stack ไม่ได้
- GitHub Desktop ยังไม่รองรับ

นอกจากนี้สถานะ public preview หมายความว่าองค์กรควรทดลองกับ stack สั้น ๆ ก่อน ดูเวลา CI, policy ของ branch, วิธี rollback และ automation ที่พึ่ง API ให้ครบ แล้วค่อยขยายใช้ทั้งทีม

## จุดที่ควรอ่านอย่างระวัง

- ประโยชน์เรื่อง review เร็วขึ้นและ conflict น้อยลงเป็นเหตุผลเชิง workflow จาก GitHub ไม่ใช่ benchmark ที่เปรียบเทียบทีมหลายแบบ
- stack ช่วยบันทึก dependency แบบเส้นตรง แต่ไม่ได้ทำให้ change ที่ผูกกันแน่นแยก review ได้เอง ถ้า interface ชั้นล่างยังแกว่ง ชั้นบนก็ยังต้อง rebase และ review ใหม่ตาม
- source พูดถึง AI agent ในฐานะงานปริมาณสูงที่เข้ากับ stack ได้ดี แต่หนึ่ง PR ต่อหนึ่ง task จะคุ้มก็ต่อเมื่อ task มีขอบเขตชัดและแต่ละชั้นตรวจได้จริง
- surface, API และคำสั่งอาจเปลี่ยนระหว่าง public preview ควรถือหน้านี้เป็น snapshot ณ วัน ingest

## See also

- [[stacked-pull-requests]]
- [[pr-dependency-dag]]
- [[github]]
- [[agentic-engineering]]
- [[orchestration-tax]]
- [[git-worktrees]]
