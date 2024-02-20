import streamlit as st

h = st.header('My Web Site on Diffusion')
s = st.subheader('เว็บไซต์ส่วนตัวของฉัน')
p = st.write('เว็บนี้ทำเพื่อเป็นพื้นฐานในการทำ streamlit เท่านั้น')
banner = st.image('https://cdn2.unrealengine.com/egs-starwarsbattlefrontiicelebrationedition-dice-g1a-01-1920x1080-87971829e831.jpg')
text = st.text_input('prompt: ')
if text:
    st.image('https://picsum.photos/400/200')
    b = st.button('จะไปต่อหรือ....')
