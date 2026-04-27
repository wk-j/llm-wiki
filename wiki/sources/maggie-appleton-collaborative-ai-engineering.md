---
title: "Collaborative AI Engineering: One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub"
type: source
tags: [ai-engineering, agents, collaboration, github-next, ace]
created: 2026-04-28
updated: 2026-04-28
sources: [Collaborative AI Engineering One Dev, Two Dozen Agents, Zero Alignment — Maggie Appleton, GitHub.md]
---

# Collaborative AI Engineering / วิศวกรรม AI แบบร่วมมือกัน

Maggie Appleton (Staff Research Engineer จาก [[github-next|GitHub Next]]) นำเสนอวิสัยทัศน์ว่าในยุคที่การเขียน code กลายเป็นเรื่องที่ "ถูกและเร็ว" ปัญหาไม่ได้อยู่ที่ "จะสร้างอย่างไร" (How to build) แต่อยู่ที่ "ควรสร้างอะไร" (Should we build) และ "ความสอดประสานของทีม" (Alignment) กลายเป็นคอขวดใหม่ที่สำคัญที่สุด

## Key Takeaways

- **The One-Man, Two-Dozen Claudes Fallacy**: การที่คนหนึ่งคนมี agent เป็นฝูงไม่ได้ช่วยแก้ปัญหาเรื่องการสื่อสารและการทำงานร่วมกัน (Coordination) ในทีม การเพิ่ม output ของรายบุคคลอาจทำให้ปัญหาการประสานงานแย่ลง (เช่น code ทับซ้อนกัน, สร้าง feature ที่ไม่มีใครต้องการ)
- **Alignment is the New Bottleneck**: เมื่อการ implement ราคาถูกลง สิ่งที่แพงขึ้นคือ "Opportunity Cost" (ค่าเสียโอกาส) การเลือกทำสิ่งที่ผิดจะมีราคาแพงมาก เพราะเราสามารถสร้าง "Slop" (ขยะ) ได้ในปริมาณมหาศาลอย่างรวดเร็ว
- **Collapse of the Implementation Window**: ในอดีต กระบวนการ Build มีช่วงเวลาให้คนได้คุยกัน (Planning -> Building -> Review) แต่ปัจจุบัน Agent ยุบรวมช่วงเวลานี้จนเหลือไม่กี่นาที ทำให้จุดที่ทีมจะได้ sync กันหายไปหมด
- **ACE (Agent Collaboration Environment)**: Prototype จาก GitHub Next ที่ออกแบบมาเพื่อการทำงานร่วมกันโดยเฉพาะ
    - **Multiplayer Sessions**: เหมือน Slack ที่มี Agent อยู่ในห้องด้วย และทุกคนมี context เดียวกัน
    - **MicroVMs**: ทุก session รันบน VM แยกกันใน cloud ทำให้สลับงานได้ทันทีโดยไม่ต้อง stash หรือ pull code
    - **Proactive Agents**: Agent ช่วยสรุปงานของเพื่อนร่วมทีม (Team Pulse) เพื่อให้ทุกคนรู้ว่าใครทำอะไรอยู่โดยไม่ต้องอ่าน PR ยาวๆ
- **Craftsmanship vs. Vibecoded Slop**: ในโลกที่ software หาง่าย "คุณภาพ" (Quality) และ "งานฝีมือ" (Craft) จะเป็นตัวตัดเชือก การจะทำงานที่มีคุณภาพได้ต้องอาฆัยการคิดเชิงวิพากษ์ (Critical Thinking) และความสอดประสานในทีมที่เข้มข้นขึ้น

## Key Entities

- [[maggie-appleton]]: ผู้บรรยายและนักวิจัยจาก GitHub Next
- [[github-next]]: ทีมทดลองของ GitHub ผู้อยู่เบื้องหลัง [[ace]]
- [[ace]]: เครื่องมือช่วยให้ทีมทำงานร่วมกับ Agent ได้ในที่เดียว

## Key Concepts

- [[collaborative-ai-engineering]]: การขยับจากการใช้ Agent รายบุคคลไปสู่การใช้ในระดับทีม
- [[alignment-bottleneck]]: ปัญหาการไม่เข้าใจตรงกันที่รุนแรงขึ้นเมื่อความเร็วในการสร้างเพิ่มขึ้น
- [[vibecoded-slop]]: การสร้าง software ปริมาณมากที่ดูเหมือนจะใช้งานได้แต่ขาดคุณภาพและการออกแบบที่ดี
- [[team-pulse]]: การที่ Agent ช่วยดึง context ของงานที่กำลังเกิดขึ้นมาสรุปให้ทีมฟัง

## See also

- [[harness-engineering]] — แนวคิดเรื่องการใช้ Agent ตรวจสอบกันเอง (Ryan Lopopolo)
- [[engineering-role-shift]] — การเปลี่ยนแปลงบทบาทของ Engineer ในยุค AI
