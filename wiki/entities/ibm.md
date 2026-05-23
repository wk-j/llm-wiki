---
title: IBM
type: entity
tags: [company, ai, open-models, enterprise, speech]
created: 2026-05-09
updated: 2026-05-09
sources: [granite-4-1-fastest-asr.md]
---

# IBM

IBM เป็นบริษัทเทคโนโลยี enterprise รายใหญ่ที่ทำทั้ง infrastructure, research, cloud, และ AI model family ของตัวเองในชื่อ **Granite**

ใน source [[granite-4-1-fastest-asr|Granite 4.1 - The Fastest ASR?]] ของ [[sam-witteveen|Sam Witteveen]] จุดที่น่าสนใจคือ IBM ไม่ได้พยายามชนะด้วย chatbot model ใหญ่เพียงอย่างเดียว แต่ทำ model หลายสายที่ใช้ในงานจริงได้ เช่น language, vision, speech, embedding, และ guardian/safety

## Granite 4.1

Granite 4.1 คือ release ที่รวมหลาย modality โดยฝั่ง speech มี [[granite-speech|Granite Speech]] 4.1 สำหรับ [[automatic-speech-recognition|ASR]] หรือการแปลงเสียงเป็นข้อความ

Sam มองว่า IBM กำลังเติมช่องที่เคยมีคนคาดหวังจาก Microsoft Phi: model เล็กกว่า ใช้งานจริงง่ายกว่า และเหมาะกับ edge/local deployment มากกว่า frontier model ขนาดใหญ่

## ทำไมสำคัญ

สำหรับ enterprise การมี small open model ที่รันเองได้มีค่ามากกว่าคะแนน chatbot อย่างเดียว เพราะข้อมูลอย่างเสียงประชุม call transcript หรือเอกสารภายในมักไม่อยากส่งออก cloud

Granite Speech 4.1 เลยสำคัญในมุม “local AI ที่ทำงานเฉพาะทางได้เร็ว” มากกว่ามุม “model คุยเก่งที่สุด”

## See also

- [[granite-speech]]
- [[automatic-speech-recognition]]
- [[granite-4-1-fastest-asr]]
