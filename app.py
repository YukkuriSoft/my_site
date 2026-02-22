import streamlit as st
import pandas as pd
import numpy as np
import time

# Define the pages
main_page = st.Page("pages/main_page.py", title="main_page", icon="🎈")
sketch_page = st.Page("pages/sketch_page.py", title="sketch_page", icon="❄️")
work_page = st.Page("pages/work_page.py", title="sketch_page", icon="🎉")


pg = st.navigation([main_page, sketch_page, work_page])


pg.run()
