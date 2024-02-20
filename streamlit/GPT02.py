import streamlit as st
import requests

h = st.header('My Web Site on Diffusion')
s = st.subheader('เว็บไซต์ส่วนตัวของฉัน')
p = st.write('เว็บนี้ทำเพื่อเป็นพื้นฐานในการทำ streamlit เท่านั้น')
banner = st.image('https://cdn2.unrealengine.com/egs-starwarsbattlefrontiicelebrationedition-dice-g1a-01-1920x1080-87971829e831.jpg')
text = st.text_input('prompt: ')
if text:
    st.write(f'กำลังสร้างภาพ.... "{text}"')
    b = st.button('จะไปต่อหรือ....')

    if b:
        # API endpoint for generating image
        url = "https://api.deepai.org/api/text2img"
        payload = {'text': text}
        headers = {'api-key': 'YOUR_API_KEY_HERE'}

        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            image_url = response.json()['output_url']
            st.image(image_url)
        else:
            st.write("เกิดข้อผิดพลาดในการสร้างภาพ")
