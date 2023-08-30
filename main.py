import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/myphoto.png",width=300)

with col2:
    st.title("Nan Wu")
    content = "Hi, I am Nan! I am a fast learner and a enthusiastic programmer who is always curious"\
              " and enjoys solving interesting problems.I graduated in 2023 with a Master of Science"\
              " in Visual Computing from Saarland University in Germany with a focus on Machine Learning, AI, and Neuroscience areas."
    st.info(content)

content2="""
        Below you can find some of the apps I have built in python. Feel free to contact me!
        "
st.write(content2)