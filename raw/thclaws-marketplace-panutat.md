Panutat Tejasen
21h ·
เวลาเขียนโปรแกรมที่เราแพลนว่ามันจะง่าย แล้วพบว่ามันซับซ้อนขึ้นเรื่อยๆ ภาษาของ coder จะเรียกว่าเจอ "Rabbit Hole" หรือรูกระต่าย
คำนี้มาจากนิยาย Alice in Wonderland ของ Lewis Carroll ความหมายคือเข้าไปติดกับเขาวงกตที่มันซับซ้อนขึ้นเรื่อยๆ
วันนี้ติดเขาวงกตที่ว่านี่อย่างจัง วันนี้ทำ marketplace สำหรับ thClaws เพื่อใช้สำหรับให้ผู้ใช้ติดตั้ง Skills, MCP และ Plugins ได้สะดวกขึ้น จริงๆก็ติดตั้งได้อยู่แล้ว แต่การที่ต้องมี marketplace เพราะการจะทำ AI Solution สำหรับ Enterprise Level เราจำเป็นต้องมีการควบคุมการใช้ Skills, MCP และ Plugins ครับ เพราะเป็นจุดที่เปราะบางทั้งในด้านข้อมูลรั่วไหล และเป็นทางเข้าของ code ที่ไม่ประสงค์ดี ดังนั้น Enterprise Editon ของลูกค้าแต่ละรายจะมี private marketplace ของตัวเองที่ admin ของลูกค้าจัดการได้เองทั้งการกำหนดสิทธิ์และการเลือก skill, mcp และ plugins ที่จะใช้
ทำ marketplace ใช้เวลาไม่นาน แต่ดันคิดว่าจะใช้ productivity plugins ของ Claude Cowork มาเป็นตัวอย่างสำหรับ marketplace เพราะชอบ concept ของการทำ host bridge คือใช้ HTML file system ให้วิ่ง webapp ใน browser เพื่อทำ dashboard อ่านเขียนข้อมูลใน working directory ที่ thClaws เกาะอยู่ ทำให้ Agent มี dashboard ใช้ และ agent สามารถสร้าง dashboard ได้เอง 
code บวมขึ้นเรื่อยๆ จากที่คิดว่าน่าจะไม่กี่บรรทัดกลายเป็น 3,000 บรรทัด แก้แล้วแก้อีกกว่าจะจบ
ตอนนี้ thClaws มี marketplace แล้วนะครับใน version 0.7.0 host ได้ทั้ง Skills, MCP และ Plugins 
Repo อยู่ที่นี่ https://github.com/thClaws/marketplace
ใครต้องการ distribute skills, mcp กับ plugins สำหรับผู้ใช้ thClaws ทำ PR เข้ามาที่นี่ได้เลยครับ ขอสงวนสิทธิ์ในการรีวิว code ทั้งหมด และอาจไม่สามารถ host ได้ทุกอย่างนะครับ ขอสงวนสิทธิ์ในการคัดเลือกครับ