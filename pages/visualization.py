import streamlit as st

from st_pages import show_pages_from_config, add_page_title

# Either this or add_indentation() MUST be called on each page in your
# app to add indentation in the sidebar
add_page_title()

show_pages_from_config()

st.write("visualization.py")
