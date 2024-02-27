#streamlit run xtra01.py
import streamlit as st
page_bg_img = '''<style>
.stApp {
    background-image: url("้https://picsum.photo/1080/768");
    background-size: cover;       
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("My Webpage")
st.sidebar.header ("with")
st.sidebar.subheader("Beautiful Background Image")
# with st.expander ('see my video?'):
   # c = st.container()
   # video_file = open('star.mp4', 'rb')
   # video_vytes = video_file.read()
   # c.write('This is my home.')
   # c.video(video_bytes)