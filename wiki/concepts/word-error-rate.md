---
title: Word Error Rate (WER)
type: concept
tags: [asr, evaluation, speech, metrics]
created: 2026-05-09
updated: 2026-05-09
sources: [granite-4-1-fastest-asr.md]
---

# Word Error Rate (WER) / อัตราคำผิดใน ASR

Word Error Rate หรือ **WER** คือ metric หลักของ [[automatic-speech-recognition|ASR]] ใช้วัดว่า transcript ที่ model สร้างต่างจาก transcript อ้างอิงกี่คำ

พูดง่ายๆ: WER ต่ำ แปลว่าคำผิดน้อย

## WER วัดอะไร

WER นับความผิด 3 แบบ:

- **Substitution** — model เขียนคำผิดแทนคำที่ควรเป็น
- **Deletion** — model ทำคำหาย
- **Insertion** — model เพิ่มคำที่ไม่ควรมี

จากนั้นเทียบกับจำนวนคำใน reference transcript

ได้อะไร: WER เป็นเลขที่ช่วยเทียบ ASR model ได้เร็ว แต่ยังต้องดูงานจริงประกอบ

## ทำไม average WER สำคัญ

ใน [[granite-4-1-fastest-asr|Granite 4.1 - The Fastest ASR?]], [[sam-witteveen|Sam Witteveen]] เน้นว่า score บน dataset ง่ายหรือคุ้นเคยอย่าง LibriSpeech อาจดูดี แต่ไม่แปลว่าจะใช้กับเสียงจริงได้ดีเสมอ

เขาเลยให้ความสำคัญกับ **average WER** บน Open ASR leaderboard มากกว่า เพราะรวมหลาย task/dataset และน่าจะสะท้อนงานจริงดีกว่า

ตัวเลขที่วิดีโอยกคือ Granite Speech 4.1 2B มี average WER **5.33** หรือพูดคร่าวๆ ว่าถูกประมาณ 95% ของคำในชุด benchmark นั้น

## WER ไม่ใช่ทุกอย่าง

ASR ที่ WER ต่ำอาจยังไม่พอ ถ้างานต้องการ:

- speaker label
- timestamp ต่อคำ
- keyword biasing
- translation
- throughput สูงมาก

เช่น Granite Speech 4.1 2B Plus อาจ WER สูงกว่ารุ่น base แต่มี [[speaker-attributed-asr|speaker attribution]] และ timestamp ที่จำเป็นกับ podcast/meeting ส่วนรุ่น NAR อาจตัด feature หลายอย่างเพื่อให้ throughput สูง

ผลคือเลือก ASR model ด้วย WER อย่างเดียวไม่ได้ ต้องดู workflow หลัง transcript ด้วย

## See also

- [[automatic-speech-recognition]]
- [[granite-speech]]
- [[speaker-attributed-asr]]
- [[non-autoregressive-asr]]
- [[granite-4-1-fastest-asr]]
