import streamlit as st
page_bg_img = '''<style>
.stApp {
    background-image: url('https://png.pngtree.com/background/20210712/original/pngtree-mysterious-cosmic-space-galaxy-nebula-background-picture-image_1179108.jpg');
    background-size: cover;
}
<style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("My Webpage")
st.sidebar.header('with')
st.sidebar.subheader("BG Image")

with st.expander("Videos"):
    c = st.container()
    video_file = open('star.mp4', 'rb')
    video_bytes = video_file.read()
    c.write('This is my darksky video.')
    c.video(video_bytes)
    c.write('This my image.')
    c.image('https://www.blognone.com/sites/default/files/externals/0ed73752b75fe76befe48dc307a6033d.jpg')