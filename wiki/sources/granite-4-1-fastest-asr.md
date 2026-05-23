---
title: "Granite 4.1 - The Fastest ASR?"
type: source
tags: [asr, speech, ibm, granite, local-ai, open-models]
created: 2026-05-09
updated: 2026-05-09
sources: [Granite 4.1 - The Fastest ASR?.md]
---

# Granite 4.1 - The Fastest ASR? / Granite Speech 4.1 เร็วแค่ไหน

วิดีโอของ [[sam-witteveen|Sam Witteveen]] อธิบาย release ของ [[granite-speech|Granite Speech]] 4.1 จาก [[ibm|IBM]] โดยโฟกัสที่ฝั่ง [[automatic-speech-recognition|Automatic Speech Recognition]] หรือ ASR — งานแปลงเสียงพูดเป็นข้อความ

แก่นของวิดีโอคือ IBM ไม่ได้ปล่อย ASR model ตัวเดียว แต่ปล่อย **3 variant ขนาดประมาณ 2B parameters** ให้เลือกตาม bottleneck ของงาน:

| Model | เหมาะกับอะไร | Trade-off |
|---|---|---|
| Granite Speech 4.1 2B | งาน transcript ทั่วไปที่อยากได้ WER ต่ำ | ไม่มี speaker attribution ลึกเท่า Plus |
| Granite Speech 4.1 2B Plus | podcast, meeting, transcript ที่ต้องรู้ว่าใครพูดและ timing ของคำ | ภาษาน้อยลง, ไม่มี translation, WER สูงขึ้น |
| Granite Speech 4.1 2B NAR | bulk transcription ปริมาณมากที่ต้องการ throughput สูงมาก | ไม่มี keyword biasing, speaker attribution, timestamp, translation |

## IBM Granite Collection

Sam วาง Granite 4.1 ไว้ในภาพใหญ่ของ open model family ของ IBM: language, vision, speech, embedding และ model ด้าน safety/guardian เขามองว่า IBM ทำของน่าสนใจ แต่คนพูดถึงน้อยกว่าที่ควร

เขายก [[granite-speech|Granite Speech]] ต่อจากงาน document understanding อย่าง Granite Vision / Docling เพราะสองสายนี้ตอบโจทย์งาน enterprise ที่ต้องดึงข้อมูลจากของจริง เช่น PDF, document, เสียงประชุม, podcast, call recording

ผลคือ Granite ไม่ได้แข่งแค่ chatbot ใหญ่ๆ แต่แข่งในงานแคบที่ต้อง deploy ได้จริงในระบบขององค์กร

## Granite Speech 4.1 2B: workhorse ASR

รุ่น base คือ model ที่ Sam บอกว่าอยู่บนสุดของ Hugging Face Open ASR leaderboard ตอนวิดีโอออก โดยมี **average Word Error Rate (WER) 5.33** เขาเน้นว่า average WER แบบนี้มีประโยชน์กว่า score บน LibriSpeech อย่างเดียว เพราะน่าจะสะท้อนโลกจริงมากกว่า

ตัวเลข speed ที่ถูกยกมาคือ **RTFX ประมาณ 231** หรือประมวลผลเสียงได้เกือบ 4 นาทีต่อ compute 1 วินาที ถ้าเทียบหยาบๆ คือ transcribe เสียง 1 ชั่วโมงได้ในราว 16 วินาที

จุดเด่นของรุ่น base:

- วิดีโอระบุว่า transcription รองรับ 7 ภาษา และยกตัวอย่าง English, French, German, Spanish, Portuguese, Japanese
- มี bidirectional speech translation ระหว่าง English กับหลายภาษา
- ทำ punctuation และ true casing ได้
- มี [[keyword-biasing|keyword biasing]] — ส่งรายชื่อชื่อคน acronym หรือศัพท์เฉพาะเข้า prompt เพื่อช่วยให้ model จดจำคำเหล่านั้นถูกขึ้น

ได้อะไร: ถ้างานคือ transcript ทั่วไป แต่มีศัพท์เฉพาะเยอะ รุ่น base เป็นตัวที่ balance ดีระหว่าง accuracy, speed, และ control ผ่าน prompt

## Granite Speech 4.1 2B Plus: transcript ที่มีโครงสร้าง

รุ่น Plus เพิ่มของที่คนทำ transcript ใช้งานจริงมักต้องการ:

- [[speaker-attributed-asr|speaker-attributed ASR]] หรือ diarization — label ว่า speaker 1, speaker 2 พูดช่วงไหน
- word-level timestamps — แต่ละคำมี end time
- incremental decoding — ส่ง transcript ก่อนหน้าเป็น prefix เพื่อให้ model ต่อจาก chunk เดิม

Sam ยกตัวอย่างว่า podcast หรือ meeting recorder ต้องรู้ว่าใครพูดอะไร ไม่ใช่แค่ข้อความดิบ ถ้า model ให้ speaker 1 / speaker 2 มาแล้ว เราค่อย map เป็นชื่อคนจริงทีหลังได้

แต่รุ่น Plus มี trade-off ชัด:

- จำนวนภาษาลดเหลือ 5 ภาษา
- ตัด Japanese ออก
- ตัด translation ออก
- WER สูงกว่ารุ่น base

ได้อะไร: ถ้า transcript ต้องใช้ต่อโดยมนุษย์ เช่น subtitle, meeting note, podcast edit รุ่น Plus น่าสนใจกว่ารุ่น base เพราะให้ structure ที่ช่วยงานหลังบ้าน

## Granite Speech 4.1 2B NAR: เร่ง throughput ด้วย transcript editing

รุ่น NAR ย่อมาจาก **non-autoregressive** เป็นจุดที่ Sam มองว่าน่าตื่นเต้นที่สุด เพราะ model ไม่ได้ generate transcript ทีละ token แบบ Whisper, Parakeet, Canary และ ASR transformer ส่วนใหญ่

ปัญหาของ autoregressive ASR คือ decoding เป็นลำดับต่อกัน GPU ต้องทำ forward pass เล็กๆ ทีละ token แล้วรอ token ถัดไป วิธีที่เร็วกว่าในอุดมคติคือ predict ทั้ง sequence พร้อมกัน แต่ที่ผ่านมามักเสีย accuracy เพราะ transcript จากเสียงดิบในช็อตเดียวทำยาก

IBM ใช้แนวทาง [[non-autoregressive-asr|NLE: Non-autoregressive LLM-based ASR by Transcript Editing]]:

1. frozen CTC encoder ฟังเสียงแล้วสร้าง draft transcript เร็วๆ
2. LLM-based editor ใช้ bidirectional attention เพื่อ copy, insert, delete, replace จาก draft
3. model ไม่ได้เขียนจากศูนย์ แต่แก้ transcript ที่เกือบถูกอยู่แล้ว

Sam อ้างตัวเลขจาก model card ว่าเมื่อ batch บน H100 รุ่น NAR ทำได้ **RTFX 1,820** หรือเทียบหยาบๆ คือ transcribe เสียง 1 ชั่วโมงได้ในราว 2 วินาที บน hardware นั้น

trade-off ของ NAR:

- ไม่มี translation
- ไม่มี keyword biasing
- ไม่มี speaker attribution
- ไม่มี timestamp

ได้อะไร: ถ้างานคือ “มีเสียงหลายร้อยชั่วโมง ขอข้อความดิบให้เร็วที่สุด” รุ่น NAR คือทางเลือกหลัก

## Code Time และ local deployment

Sam demo บนเครื่อง Dell Pro Max Tower ที่มี RTX Pro 6000 Blackwell GPU แต่เขาย้ำว่า model ขนาด 2B ทำให้รันบน GPU หลายระดับได้ ไม่จำเป็นต้องเป็นเครื่องใหญ่เสมอ

ข้อควรระวังคือ environment:

- ต้องจัด PyTorch, CUDA, Flash Attention ให้เข้ากัน
- GPU เก่าอย่าง T4 อาจเจอปัญหาเวลาติดตั้ง Flash Attention
- NAR จะได้ speed สูงจริงเมื่อ batching/chunking ถูกออกแบบดี และ hardware รองรับ

ตัวอย่าง code ใช้ Hugging Face Transformers, `AutoProcessor`, และ prompt ที่ต่างกันสำหรับ diarization, keyword biasing, incremental decoding

## Long-form audio ยังเป็นโจทย์ workflow

ช่วงท้าย Sam บอกว่ายังทดลองเรื่อง long-form audio อยู่ โดยเฉพาะ:

- chunk size ที่เหมาะกับ podcast หรือ audio 4 ชั่วโมง
- การส่ง keyword biasing เข้าแต่ละ chunk
- pretext filling strategy เพื่อ stitch transcript ยาวให้ต่อเนื่อง
- การรักษา speaker numbering ให้คงที่ข้าม chunk

ตรงนี้สำคัญ เพราะ model เร็วอย่างเดียวไม่พอ งานจริงต้องมี pipeline ที่คุม chunking, overlap, speaker label, timestamp, และศัพท์เฉพาะได้

## Quotes

> "IBM is kind of framing this as pick the variant based on what your bottleneck actually is."

> "If you just needed the raw transcripts of hundreds of hours of audio, this is gonna allow you to process all of that in a really insane amount of time."

> "The speech stuff is really super interesting."

## See also

- [[granite-speech]]
- [[ibm]]
- [[sam-witteveen]]
- [[automatic-speech-recognition]]
- [[non-autoregressive-asr]]
- [[speaker-attributed-asr]]
- [[keyword-biasing]]
- [[word-error-rate]]
- [[speculative-decoding]]
