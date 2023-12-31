import streamlit as st

from st_pages import show_pages_from_config, add_page_title

# Either this or add_indentation() MUST be called on each page in your
# app to add indentation in the sidebar
add_page_title()

show_pages_from_config()

# ---------------------------------------------------------------------- #

import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)

# authenticator.login("Login", "sidebar")

if st.session_state["authentication_status"]:
    with st.sidebar:
        st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout("Logout", "sidebar", key="logout_button")
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")

# ---------------------------------------------------------------------- #

st.info(
    "This page is intended to showcase the visualization of structured data, using AI methods, with CSV as an example.",
    icon="ℹ️",
)

# ---------------------------------------------------------------------- #

import pandas as pd
import plotly.express as px

uploaded_file = st.file_uploader(
    "uploaded", type=["csv"], label_visibility="hidden"
)

if uploaded_file is not None:
    st.toast("File uploaded successfully", icon="🎉")
    df = pd.read_csv(uploaded_file)

    st.divider()
    st.subheader("Uploaded CSV file content:")
    st.write(df)

    st.divider()
    st.subheader("Scatter Plot Matrix:")
    fig_scatter_matrix = px.scatter_matrix(df)
    st.plotly_chart(fig_scatter_matrix)

    st.divider()
    st.subheader("Bar Chart:")
    x_column = st.selectbox("Select X-axis Column Name", df.columns)
    y_column = st.selectbox("Select Y-axis Column Name", df.columns)
    fig_bar = px.bar(df, x=x_column, y=y_column)
    st.plotly_chart(fig_bar)
