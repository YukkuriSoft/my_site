import streamlit as st
from components.floating_button import floating_button


# Define the pages
main_page = st.Page("pages/main_page.py", title="main_page", icon="🎈")
sketch_page = st.Page("pages/sketch_page.py", title="sketch_page", icon="❄️")
work_page = st.Page("pages/work_page.py", title="work_page", icon="🎉")
test_page = st.Page("pages/test_page.py", title="test_page", icon="🎉")


pg = st.navigation([main_page, sketch_page, work_page, test_page])


pg.run()


if floating_button():
    st.write("floating button clicked")
