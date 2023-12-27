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

authenticator.login("Login", "sidebar")

if st.session_state["authentication_status"]:
    with st.sidebar:
        st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout("Logout", "sidebar", key="logout_button")
elif st.session_state["authentication_status"] is False:
    st.error("Username/password is incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Please enter your username and password")

# ---------------------------------------------------------------------- #
import pandas as pd
import plotly.express as px

# 通过 st.file_uploader 允许用户上传 CSV 文件
uploaded_file = st.file_uploader("上传 CSV 文件", type=["csv"])

# 如果用户上传了文件
if uploaded_file is not None:
    # 读取 CSV 文件为 DataFrame
    df = pd.read_csv(uploaded_file)

    # 显示 DataFrame
    st.write("上传的 CSV 文件内容：")
    st.write(df)

    # 自动生成散点图矩阵
    st.write("散点图矩阵：")
    fig_scatter_matrix = px.scatter_matrix(df)
    st.plotly_chart(fig_scatter_matrix)

    # 自动生成条形图
    st.write("条形图：")

    # 利用选择的列名生成图表
    x_column = st.selectbox("选择 X 轴列名", df.columns)
    y_column = st.selectbox("选择 Y 轴列名", df.columns)

    fig_bar = px.bar(df, x=x_column, y=y_column, title="条形图")
    st.plotly_chart(fig_bar)
