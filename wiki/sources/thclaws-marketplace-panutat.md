---
title: thClaws Marketplace / มาร์เก็ตเพลสสำหรับ thClaws
type: source
tags: [thclaws, marketplace, skill, mcp, plugin, enterprise, security]
created: 2026-04-30
updated: 2026-04-30
sources: [thclaws-marketplace-panutat.md]
---

# thClaws Marketplace / มาร์เก็ตเพลสสำหรับ thClaws

Source: Facebook Post by [[panutat-tejasen|Panutat Tejasen]] (2026-04-30)

## สรุปสาระสำคัญ

- **การเปิดตัว thClaws Marketplace:** ในเวอร์ชัน 0.7.0 ของ [[thclaws]] ได้มีการเพิ่มระบบ Marketplace เพื่อให้ผู้ใช้สามารถติดตั้ง [[skill]], [[model-context-protocol|MCP]], และ Plugin ได้สะดวกขึ้น
- **ความจำเป็นสำหรับ Enterprise:** การทำ AI Solution ระดับองค์กรต้องมีการควบคุม (Control) การใช้งานส่วนขยายเหล่านี้ เพราะเป็นจุดเสี่ยงต่อข้อมูลรั่วไหลและโค้ดที่ไม่ประสงค์ดี
- **Private Marketplace:** ลูกค้า Enterprise สามารถมี marketplace ส่วนตัวเพื่อให้ Admin จัดการสิทธิ์และเลือกเฉพาะส่วนขยายที่ผ่านการตรวจสอบแล้วมาใช้งาน
- **แนวคิด Host Bridge:** แรงบันดาลใจจาก Claude Cowork โดยการใช้ HTML File System รัน webapp ใน browser เพื่อทำ Dashboard ที่สามารถอ่าน/เขียนข้อมูลใน working directory ที่ Agent ทำงานอยู่ได้ ทำให้ Agent มีหน้าจอใช้งานและสามารถสร้าง Dashboard เองได้
- **ปรากฏการณ์ [[rabbit-hole]]:** ผู้เขียนยกตัวอย่างการทำ Marketplace ที่ตอนแรกคิดว่าง่าย แต่กลับมีความซับซ้อนเพิ่มขึ้นเรื่อยๆ จนโค้ดบวมจากไม่กี่บรรทัดเป็น 3,000 บรรทัด

## ประเด็นที่น่าสนใจ

1. **Governance & Security:** เน้นย้ำว่า Marketplace ไม่ได้มีไว้แค่เพื่อความสะดวก แต่เป็นกลไกสำคัญในการทำ Governance สำหรับองค์กร
2. **Agent-Generated UI:** แนวคิดที่ Agent สามารถสร้าง Dashboard ของตัวเองผ่าน Host Bridge เป็นก้าวสำคัญของการมี [[diegetic-ui]] หรือเครื่องมือที่ Agent ใช้สื่อสารกับคนได้ดีขึ้น
3. **Complexity in "Simple" Tasks:** ย้ำเตือนเรื่องการประเมินความซับซ้อนของซอฟต์แวร์ที่มักจะบานปลายเมื่อลงรายละเอียด (Rabbit Hole)

## ดูเพิ่ม

- [[thclaws]]
- [[panutat-tejasen]]
- [[rabbit-hole]]
- [[host-bridge]]
