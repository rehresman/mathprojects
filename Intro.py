import streamlit as st
from os.path import join, dirname

BASE_DIR = dirname(__file__)

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Hi! 👋 I'm Ryan")
st.write("## These are my math projects.")
st.sidebar.success("Select a demo above.")
st.write("**👈 Select a demo from the sidebar** to see some examples!")

col1, col2 = st.columns(2)


st.image(join(BASE_DIR, "images", "matrix_code.png"))


st.markdown(
    """
    My inspiration for these comes from my experience training AI models to do math and my interests in 
    ML/data science and music.  All the code for these projects is on [my GitHub](https://github.com/rehresman).
"""
)