import streamlit as st
from PIL import Image, ImageDraw, ImageFont

h = st.header('My Web Site on Diffusion')
s = st.subheader('เว็บไซต์ส่วนตัวของฉัน')
p = st.write('เว็บนี้ทำเพื่อเป็นพื้นฐานในการทำ streamlit เท่านั้น')
banner = st.image('https://cdn2.unrealengine.com/egs-starwarsbattlefrontiicelebrationedition-dice-g1a-01-1920x1080-87971829e831.jpg')
text = st.text_input('prompt: ')
if text:
    st.write(f'กำลังสร้างภาพ.... "{text}"')
    b = st.button('จะไปต่อหรือ....')

    if b:
        # Create a blank image with white background
        width, height = 300, 100
        image = Image.new("RGB", (width, height), "white")

        # Initialize drawing context
        draw = ImageDraw.Draw(image)

        # Specify font and size
        font = ImageFont.truetype("arial.ttf", 20)

        # Draw text on image
        draw.text((10, 10), text, fill="black", font=font)

        # Display the image
        st.image(image)
