---
title: How Perplexity Lost the AI War
type: source
tags: [ai, search, startups, strategy, distribution]
created: 2026-07-03
updated: 2026-07-03
sources: []
---

# How Perplexity Lost the AI War / Perplexity แพ้สงคราม AI Search อย่างไร

สรุปวิดีโอของ [[mondo-startups|Mondo Startups]] เกี่ยวกับ [[perplexity|Perplexity]] และการแข่งขันในตลาด [[ai-search-economics|AI search economics]]. เนื้อหาเป็นบทวิเคราะห์เชิงธุรกิจ ไม่ใช่ข้อมูลบริษัทโดยตรง จึงควรอ่านตัวเลขและข้อกล่าวหาเป็น **source-attributed claim** ก่อน

- URL: https://www.youtube.com/watch?v=a5OW2c2xvdw
- ผู้เขียน/ช่อง: [[mondo-startups|Mondo Startups]]
- รูปแบบ: YouTube transcript
- แกนเรื่อง: Perplexity ไม่ได้พัง แต่แพ้ narrative ว่าจะมาแทน [[google|Google]] เพราะ differentiation ถูก copy, unit economics แพงกว่า, distribution อ่อนกว่า, monetization ยังไม่ชัด, และ publisher trust สั่นคลอน

## Thesis หลัก

Mondo Startups เปิดด้วยภาพว่า Perplexity เคยดูเหมือน startup ที่จะเปลี่ยน search เพราะให้คำตอบเร็ว มี citation สะอาด และไม่มี ad มาขวาง. แต่สุดท้ายข้อได้เปรียบนี้กลายเป็น feature ที่ incumbent copy ได้

ประโยคสำคัญคือ Perplexity ไม่ได้แพ้เพราะ product แย่. มันแพ้เพราะ **timing, economics, distribution, and what happens when giants wake up**. แปลแบบตรงใจคือ ต่อให้ product ดีกว่า ก็ไม่พอ ถ้าคู่แข่งถือ default behavior, ad machine, และ ecosystem ไว้หมดแล้ว

ได้อะไร: เคส Perplexity ชี้ว่า AI product ที่ดู “obviously better” อาจยังแพ้ได้ ถ้าต้นทุนต่อ usage และช่องทางถึงผู้ใช้ไม่เข้าข้าง

## Chapter 1: จุดต่างที่ถูก copy เร็ว

Mondo Startups เล่าว่า Perplexity ก่อตั้งในปี 2022 โดย [[aravind-srinivas|Aravind Srinivas]] และทีม. Pitch คือ Google ไม่ได้ตอบคำถาม แต่ให้ link. Perplexity จะตอบตรง ๆ แล้วให้ source เพื่อให้ตรวจเองได้

ตรงนี้ทำให้ Perplexity ดูใหม่มากในช่วงต้นปี 2023:

- ไม่มี SEO games แบบหน้าเว็บที่เขียนเพื่อ algorithm
- ไม่มี sponsored placement แบบ search ad ดั้งเดิม
- มีคำตอบพร้อม citation
- ลดภาระการขุดผ่าน “10 blue links”

แต่ Mondo Startups มองว่าปัญหาอยู่ที่ Perplexity ไม่ได้ train foundational model ขนาดใหญ่เอง. มันใช้ model จาก [[openai|OpenAI]], [[anthropic|Anthropic]], [[meta|Meta]], Google และค่ายอื่น แล้ววางระบบ search/answering ทับลงไป

ในมุมผู้ใช้ เรื่องนี้อาจไม่สำคัญ. แต่ในมุมอุตสาหกรรม มันทำให้คำถาม “นี่คือ AI company หรือ AI wrapper” ติดตัว Perplexity. พอ [[chatgpt|ChatGPT]], Google AI Overviews, [[claude|Claude]], และ Gemini เพิ่ม citation/answering เข้ามาเอง ความต่างหลักของ Perplexity ก็ลดลง

ผลคือ: “answers with sources” จาก product กลายเป็น feature ที่ทุกเจ้าต้องมี

## Chapter 2: เศรษฐศาสตร์ของ query ไม่เท่ากัน

บทนี้ชี้ว่า search ไม่ได้แข่งกันที่ intelligence อย่างเดียว แต่แข่งกันที่ cost ต่อ query ด้วย. ทุก query ของ Perplexity ต้องทำ live search, เรียก large language model, แล้ว synthesize คำตอบแบบ real time

ฝั่ง Google มีข้อได้เปรียบต่างกัน:

- search แบบเดิมมีต้นทุนต่ำมากต่อครั้ง
- infrastructure ถูกปรับมานานหลายสิบปี
- AI summary เปิดเฉพาะบาง query ที่คุ้มทางเศรษฐศาสตร์
- ad engine ชดเชยต้นทุน search ได้อยู่แล้ว

Mondo Startups ใช้คำแรงว่า นี่ไม่ใช่ product problem แต่เป็น “physics problem”. Perplexity อาจโตมาก แต่โตบน cost structure ที่หนักกว่า incumbent

ในกลางปี 2025 Srinivas อ้างตามวิดีโอว่า Perplexity ทำ query หลายร้อยล้านครั้งต่อเดือน. ตัวเลขนี้น่าประทับใจ แต่ Google อยู่ที่ระดับหลายหมื่นล้าน search ต่อวัน. ดังนั้นในกรอบการเทียบของ Mondo Startups Perplexity ยังต่ำกว่า 1% ของ global search volume มาก

ได้อะไร: ถ้า product ต้องจ่าย compute หนักทุก interaction แต่คู่แข่งจ่ายน้อยกว่าและ monetize ได้ดีกว่า การโตอาจยิ่งทำให้ burn หนักขึ้น

## Monetization: สะอาดกับทำเงินยังดึงกันเอง

Perplexity พยายามไม่ทำ search ads แบบเดิม แต่ทดลอง format ที่รักษาความไว้ใจ เช่น sponsored follow-up questions และ brand integrations เบา ๆ

ข้อกล่าวอ้างสำคัญในบทนี้:

- ปลายปี 2025 Perplexity หยุด onboarding advertiser ใหม่เพื่อคิด strategy ใหม่
- มีรายงานว่า ad revenue อยู่ราว $20,000 จาก total revenue $34 million
- advertiser ต้องการ performance แต่ Perplexity optimize เพื่อ answer ไม่ใช่ buying behavior

จุดนี้ทำให้ Perplexity เจอ choice ที่ Google ไม่ต้องเจอเท่ากัน: เพิ่ม ad แล้วเสี่ยงทำลาย trust หรือรักษา experience แล้ว monetization อ่อน

ควรเก็บเป็น open question: ตัวเลข ad revenue และสถานะ ad strategy มาจากรายงานที่ Mondo Startups อ้าง แต่ใน ingest นี้ยังไม่ได้ตรวจ primary source

## Publisher trust และคดีความ

Mondo Startups เล่าว่า publisher หลายรายกล่าวหา Perplexity เรื่อง scrape proprietary content, reproduce article ใกล้เกินไป, และ hallucinated quotes ที่ไปโยงกับ outlet จริง. ตัวอย่างที่กล่าวถึงคือ The New York Times ส่ง cease and desist, BBC ขู่ดำเนินคดี, และ Reddit ฟ้อง

Perplexity ตอบตามที่ช่องเล่าว่า สิ่งที่ทำคือ aggregate ไม่ใช่ plagiarize และเสนอ revenue sharing agreement

แก่นไม่ใช่แค่ถูกหรือผิดทางกฎหมาย. ประเด็นคือ perception สำคัญ. Startup ที่ตั้งตัวเป็น ethical alternative ต่อ Google ถ้าดูเหมือนสร้างบนงานของ publisher โดยไม่ชัดเรื่องผลตอบแทน ก็เสีย trust กับ publisher, regulator, และ enterprise customer ได้

เปิดคำถามไว้: ข้อกล่าวหาและการตอบโต้แต่ละเคสควรตรวจจากเอกสารคดี/จดหมาย/แถลงการณ์โดยตรงก่อนใช้เป็นข้อเท็จจริงแข็ง

## Chapter 3: Comet และปัญหา distribution

Perplexity พยายามออกจากการเป็น search box ด้วย [[comet-browser|Comet]] ซึ่งเป็น AI browser. logic คือ ถ้า own interface ก็ own user และ control distribution ได้มากขึ้น

Mondo Startups เทียบกับ Microsoft Bing. Microsoft มี Windows default placement, การ integrate ChatGPT ตั้งแต่ต้นปี 2023, สิทธิ์เข้าถึง GPT-4, และงบ marketing ใหญ่. แต่ market share ของ Bing ก็แทบไม่ขยับตามที่ช่องเล่า

บทเรียนคือ browser และ search เป็น habit ที่เหนียวมาก. คนไม่เปลี่ยนเพราะ “ดีกว่านิดหน่อย”. ต้องดีกว่าจนชีวิตเปลี่ยน

ตรงนี้เชื่อมกับ [[distribution-moat|distribution moat]]: Google ไม่ได้ชนะเพราะ AI ดีกว่าเสมอไป แต่เพราะ search ผูกกับ Android, Chrome, YouTube, Gmail, Google Drive และ default behavior ของผู้ใช้

## บทสรุป

Mondo Startups ไม่ได้บอกว่า Perplexity ตาย. แต่บอกว่า Perplexity กลายเป็น research tool ที่ดีสำหรับ power users และไม่ชนะสงครามที่จะ replace Google

สรุปเป็น bullet สั้น ๆ:

- core feature ถูก incumbents copy
- query cost แพงกว่า search แบบเดิม
- ads ไม่ fit กับ answer-first UX ง่าย ๆ
- publisher trust เป็นจุดเสี่ยง
- browser/search distribution เปลี่ยนยาก
- “better product” ไม่พอ ถ้าไม่ได้ถือ economics และ distribution

## Open questions

- ตัวเลข ad revenue $20,000 / total revenue $34 million มาจากรายงานใด และช่วงเวลาคือเมื่อไร
- การ pause onboarding advertisers ปลายปี 2025 เป็น pause กว้างแค่ไหน และเปลี่ยน strategy อย่างไรต่อ
- คดีหรือข้อพิพาทกับ The New York Times, BBC, Reddit อยู่ในสถานะใด
- “hundreds of millions of queries per month” ของ Perplexity วัด query แบบเดียวกับ search volume ของ Google หรือไม่
- Comet ทำให้ retention หรือ paid conversion ดีขึ้นแค่ไหนเมื่อเทียบกับ search product เดิม
- Perplexity ตั้งใจ “replace Google” จริงแค่ไหน หรือเป็น narrative จาก investor/media มากกว่ากลยุทธ์บริษัท

## See also

- [[perplexity]]
- [[google]]
- [[aravind-srinivas]]
- [[comet-browser]]
- [[ai-search-economics]]
- [[answer-engine]]
- [[distribution-moat]]
- [[value-migration-from-code]]
