import streamlit as st

st.title("はじめてのStreamlit")

st.write("こんにちは")

x = st.slider("数字を選んで",0,100,50)

st.write("値:",x)
