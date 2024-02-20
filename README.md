
![sunflower-1627193_1920](https://github.com/frukcharkrit/frukcharkrit.github.io/assets/157786904/9a632902-721d-43b6-9526-01d2c1839731)

# สมุดบันทึก

สำหรับรายวิชา [OOP](https://frukcharkrit.github.io/)

# คำสั่ง git พื้นฐาน
` ` `
    
    git status 
    
    git add
    
    git commit
    
` ` `
# คำสั่ง python พื้นฐาน
` ` `
d = {'Anna': 3.99, 'Betty': 3.78}
for k,v in d.items():
    print(k,v)
` ` `

# สำหรับผู้ที่ยังไม่มี git

1. เปิด powershell 

2. ใช้คำสั่ง Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

3. ใช้คำสั่ง Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression

4. เปิด VSCode ซึ่งหลังจากเสร็จสิ้นกระบวนการตัวโปรแรมควรจะตรวจจับ git ให้อัตโนมัติ 

5. Ctrl + Shift + P แล้วเลือก Git Clone

6. ใส่ลิ้งเว็บไซต์ github.com/xxxxxx/xxxxxx.github.io.git
    *xxxxxx = ชื่อผู้ใช้ของตน

7. เลือก folder : OOP > streamlit

8. Open in New window

# วิธีการรัน streamlit

    streamlit run streamlit/app03.py

# Huggingface 

    https://github.com/huggingface/diffusers

# Diffusers

    pip install --upgrade diffusers[torch]
    pip install --upgrade transformers

# เริ่มต้นพัฒนา streamlit

1. clone จาก github

git clone https://github.com/frukcharkrit/frukcharkrit.github.io.git

2. deactivate

conda deactivate

3. สร้างสภาพแวดล้อมใหม่

python -m venv venv

4. activate สภาพแวดล้อมใหม่

venv/scripts/activate

5. ติดตั้ง streamlit

pip install streamlit

ลงชื่อ - ชาคริต พิมพ์สระเกษ