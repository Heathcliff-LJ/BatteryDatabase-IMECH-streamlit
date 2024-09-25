import streamlit as st

st.header('Preparing...')

col1, col2, col3 = st.columns(3)
with col1:
    # st.write("Cycling")
    st.image('pics/Disruptive.png')
with col2:
    # st.write("Characterization")
    st.image('pics/Disruptive2.jpg')
with col3:
    # st.write("Disruptive")
    st.image('pics/Disruptive3.jpg')
