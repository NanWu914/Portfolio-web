import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/myphoto.png",width=300)

with col2:
    st.title("Nan Wu")
    content = """
    Hi, I am Nan! I am a fast learner and a enthusiastic programmer who is always curious 
    and enjoys solving interesting problems.I graduated in 2023 with a Master of Science 
    in Visual Computing from Saarland University in Germany with a focus on Machine Learning, 
    AI, and Neuroscience areas."""
    st.info(content)

content2="""
        Below you can find some of the apps I have built in python. Feel free to contact me!
        """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:8].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[8:].iterrows():
        st.header(row['title'])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")