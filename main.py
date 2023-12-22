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
