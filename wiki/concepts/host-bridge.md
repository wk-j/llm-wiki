---
title: Host Bridge / การเชื่อมต่อระบบโฮสต์ผ่านเบราว์เซอร์
type: concept
tags: [architecture, agent-ui, interface, thclaws, browser-api]
created: 2026-04-30
updated: 2026-04-30
sources: [thclaws-marketplace-panutat.md]
---

# Host Bridge / การเชื่อมต่อระบบโฮสต์ผ่านเบราว์เซอร์

**Host Bridge** คือแนวคิดทางสถาปัตยกรรมซอฟต์แวร์ที่อนุญาตให้ Web Application (ที่รันอยู่บน Browser) สามารถสื่อสารและจัดการข้อมูลในระบบ File System ของเครื่อง Host (ที่ Agent ทำงานอยู่) ได้โดยตรง

แนวคิดนี้ถูกนำมาใช้อย่างโดดเด่นในโปรเจกต์อย่าง Claude Cowork และต่อมาใน [[thclaws]] เพื่อแก้ปัญหาเรื่องการแสดงผล (Visualisation) และการโต้ตอบระหว่าง Agent กับผู้ใช้

## กลไกการทำงาน

1. **Local Server/Bridge:** มีกระบวนการรันอยู่เบื้องหลัง (เช่น thClaws) ทำหน้าที่เป็นตัวกลาง
2. **Web Standard APIs:** ใช้เทคโนโลยีอย่าง HTML5 File System Access API หรือ WebSocket ในการส่งข้อมูล
3. **Bi-directional Access:**
   - **Agent to Browser:** Agent เขียนไฟล์ข้อมูล (JSON/HTML) ลงใน working directory
   - **Browser to Host:** หน้าจอ Dashboard ใน Browser อ่านไฟล์นั้นมาแสดงผล และเมื่อผู้ใช้กดปุ่ม Dashboard สามารถส่งคำสั่งกลับไปให้ Agent ทำงานต่อได้

## Payoff (ผลลัพธ์ที่ได้)

- **Agent Dashboard:** Agent ไม่จำเป็นต้องคุยผ่าน text ใน terminal อย่างเดียว แต่สามารถมี "หน้าจอ" (GUI) ของตัวเองได้
- **Agent-Generated UI:** Agent สามารถเขียน code เพื่อสร้างหน้า Dashboard ใหม่ๆ ขึ้นมาเองตามสถานการณ์ (เช่น สร้างกราฟสรุปงานหลังจากรันวิเคราะห์ข้อมูลเสร็จ)
- **Shared Context:** ทั้งคนและ AI มองเห็นสถานะของงานผ่านหน้าจอเดียวกัน ทำให้การทำงานร่วมกัน (Collaboration) ง่ายขึ้น
- **Rich Interaction:** รองรับการลากวาง (Drag & Drop), การดูภาพ, และการโต้ตอบที่ซับซ้อนกว่า CLI

## กรณีตัวอย่างใน thClaws

ใน [[thclaws]] เวอร์ชัน 0.7.0 มีการใช้ Host Bridge เพื่อทำ Marketplace และ Dashboard ทำให้ผู้ใช้สามารถจัดการส่วนขยาย (Extensions) และดูสถานะของ Agent ได้สะดวกขึ้นผ่านเบราว์เซอร์ โดยที่ตัว Dashboard ยังสามารถอ่านเขียนไฟล์ในโฟลเดอร์โครงการได้

## ดูเพิ่ม

- [[thclaws]]
- [[diegetic-ui]]
- [[claude-code-remote-surfaces]]
- [[malleable-tools]]
