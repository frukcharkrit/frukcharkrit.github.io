from diffusers import DiffusionPipeline as dp
from PIL import Image
import torch
import streamlit as st


h = st.header('My Web Site on Diffusion')
s = st.subheader('เว็บไซต์ส่วนตัวของฉัน')
p = st.write('เว็บนี้ทำเพื่อเป็นพื้นฐานในการทำ streamlit เท่านั้น')
banner = st.image('https://cdn2.unrealengine.com/egs-starwarsbattlefrontiicelebrationedition-dice-g1a-01-1920x1080-87971829e831.jpg')
text = st.text_input('prompt: ')
if text:
    dp_model = dp.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    image_data = dp_model(text).images[0]
    image = Image.fromarray(image_data)
    st.image(image)
    b = st.button('จะไปต่อหรือ....')