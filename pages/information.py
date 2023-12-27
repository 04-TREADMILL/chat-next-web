import streamlit as st
import openai

from st_pages import show_pages_from_config, add_page_title
from streamlit_extras.annotated_text import annotated_text

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

from streamlit_timeline import timeline

# import streamlit_wordcloud as wordcloud
#
# words = [
#     dict(text="达特茅斯大会的召开", value=1956, color="#b5de2b"),
#     dict(text="全球首家AI实验室的成立", value=1957, color="#b5de2b"),
#     dict(text="首款智能聊天机器人 ElIZA", value=1965, color="#b5de2b"),
#     dict(text="推理机规格语言（Knowledge Description Language, KRL）的提出", value=1979, color="#b5de2b"),
#     dict(text="专家系统的发展", value=1981, color="#b5de2b"),
#     dict(text="深蓝战胜加里·卡斯帕罗夫", value=1997, color="#b5de2b"),
#     dict(text="谷歌发布了一项以统计学习为基础的语音识别技术", value=2006, color="#b5de2b"),
#     dict(text="沃森在危险边缘节目中的胜利", value=2011, color="#b5de2b"),
#     dict(text="阿尔法狗战胜了围棋李世石", value=2016, color="#b5de2b"),
#     dict(text="阿尔法零的发布", value=2018, color="#b5de2b"),
# ]
# return_obj = wordcloud.visualize(words, tooltip_data_fields={
#     'text':'Event', 'value':'Year'
# }, per_word_coloring=False)

import random
from http import HTTPStatus
import dashscope


def call_with_messages():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "请列出最新的五条AI资讯, 只需要列出序号，内容，不需要其他内容"},
    ]
    response = dashscope.Generation.call(
        dashscope.Generation.Models.qwen_turbo,
        messages=messages,
        # set the random seed, optional, default to 1234 if not set
        seed=random.randint(1, 10000),
        result_format="message",  # set the result to be "message" format.
    )
    if response.status_code == HTTPStatus.OK:
        return response.output.choices[0]["message"]["content"]


# Streamlit 应用
st.title("最新资讯")
ai_news = call_with_messages()

# 展示生成的 AI 资讯
st.subheader("TOP FIVE")
st.write(ai_news)

# timeline
with open("timeline.json", "r") as f:
    data = f.read()
st.subheader("This is timeline of AI")
# render timeline
timeline(data, height=800)
