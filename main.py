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

import os

# 获取当前脚本所在目录
current_directory = os.path.dirname(os.path.abspath(__file__))

# 构建 README.md 的完整路径
readme_path = os.path.join(current_directory, "README.md")

# 读取 README.md 文件内容
with open(readme_path, "r", encoding="utf-8") as file:
    readme_content = file.read()

st.markdown(readme_content)

# ---------------------------------------------------------------------- #

from streamlit_extras.badges import badge

st.divider()
badge(type="github", name="04-TREADMILL/chat-next-web")
badge(type="buymeacoffee", name="VGalaxies")

# ---------------------------------------------------------------------- #

st.divider()
import pandas as pd
from datetime import datetime

# 原始数据
raw_data = """
2023-12-23: 2 个 li 元素
2023-12-22: 2 个 li 元素
2023-12-21: 1 个 li 元素
2023-12-20: 1 个 li 元素
2023-12-19: 4 个 li 元素
2023-12-18: 4 个 li 元素
2023-12-17: 2 个 li 元素
2023-12-15: 1 个 li 元素
2023-12-14: 1 个 li 元素
2023-12-12: 1 个 li 元素
2023-12-11: 4 个 li 元素
2023-12-10: 10 个 li 元素
2023-12-9: 1 个 li 元素
2023-12-8: 1 个 li 元素
2023-12-7: 17 个 li 元素
2023-12-6: 2 个 li 元素
2023-12-5: 2 个 li 元素
2023-12-3: 4 个 li 元素
2023-12-1: 2 个 li 元素
2023-11-29: 2 个 li 元素
2023-11-28: 2 个 li 元素
2023-11-27: 1 个 li 元素
2023-11-26: 1 个 li 元素
2023-11-25: 1 个 li 元素
2023-11-24: 9 个 li 元素
2023-11-21: 1 个 li 元素
2023-11-19: 4 个 li 元素
2023-11-18: 1 个 li 元素
2023-11-13: 1 个 li 元素
2023-11-12: 8 个 li 元素
2023-11-11: 7 个 li 元素
2023-11-10: 3 个 li 元素
2023-11-7: 1 个 li 元素
2023-11-6: 1 个 li 元素
2023-11-5: 1 个 li 元素
2023-11-4: 3 个 li 元素
2023-11-2: 1 个 li 元素
2023-10-29: 5 个 li 元素
2023-10-28: 5 个 li 元素
2023-10-27: 3 个 li 元素
2023-10-26: 1 个 li 元素
2023-10-24: 5 个 li 元素
2023-10-23: 1 个 li 元素
2023-10-19: 3 个 li 元素
2023-10-18: 4 个 li 元素
2023-10-14: 2 个 li 元素
2023-10-11: 1 个 li 元素
2023-10-9: 4 个 li 元素
2023-10-8: 4 个 li 元素
2023-10-7: 3 个 li 元素
2023-10-6: 53 个 li 元素
2023-10-5: 21 个 li 元素
"""

# 解析原始数据并构建字典
data_dict = {}
for line in raw_data.split("\n"):
    if line:
        date_str, count_str = line.split(":")
        date = datetime.strptime(date_str.strip(), "%Y-%m-%d")
        count = int(count_str.split(" ")[1])
        data_dict[date] = count

# 构建 DataFrame
chart_data = pd.DataFrame(list(data_dict.items()), columns=["Date", "Count"])

# 在 Streamlit 中创建条形图
st.title("Bangumi Timeline Overview")

st.bar_chart(chart_data.set_index("Date"))
