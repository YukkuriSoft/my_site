import streamlit as st


def card(title, text, button_label, key):
    st.subheader(title)
    st.write(text)
    if st.button(button_label, key=key + "1"):
        st.write("clicked:", title)
    st.radio("aaaa", ["1", "2", "3"], key=key + "2")


card("User Info1", "This is custom card", "Open", key="card1_btn")
card("User Info2", "This is custom card", "Open", key="card2_btn")
