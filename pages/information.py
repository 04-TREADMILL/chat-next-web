import streamlit as st

from st_pages import show_pages_from_config, add_page_title
from streamlit_extras.let_it_rain import rain

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

st.info(
    "This page is designed to showcase news related to AI, recommend popular repositories in the AI field, and display the timeline of AI development.",
    icon="ℹ️",
)

# ---------------------------------------------------------------------- #

from streamlit_timeline import timeline

import random
from http import HTTPStatus
import dashscope

dashscope.api_key = "sk-99f8b6523df14ad28e5178bd0bbf8401"


def fetch_ai_news():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Please list five pieces of AI news. Provide only the sequence number, content (highlighting key information using markdown syntax), and include emojis – no additional details needed!",
        },
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


st.subheader("AI Latest News")
with st.spinner("Wait for fetching..."):
    st.write(fetch_ai_news())

# ---------------------------------------------------------------------- #

import pandas as pd

st.divider()
st.subheader("Awesome AI Repositories")

COUNT = 10
# TODO: generate by LLM
df = pd.DataFrame(
    {
        "name": [
            "TensorFlow",
            "PyTorch",
            "Scikit-learn",
            "Keras",
            "OpenCV",
            "spaCy",
            "fastai",
            "AllenNLP",
            "Transformers",
            "MXNet",
        ],
        "url": [
            "https://github.com/tensorflow/tensorflow",
            "https://github.com/pytorch/pytorch",
            "https://github.com/scikit-learn/scikit-learn",
            "https://github.com/keras-team/keras",
            "https://github.com/opencv/opencv",
            "https://github.com/explosion/spaCy",
            "https://github.com/fastai/fastai",
            "https://github.com/allenai/allennlp",
            "https://github.com/huggingface/transformers",
            "https://github.com/apache/incubator-mxnet",
        ],
        "stars": [random.randint(1000, 10000) for _ in range(COUNT)],
        "views_history": [
            [random.randint(1000, 10000) for _ in range(30)]
            for _ in range(COUNT)
        ],
    }
)
st.dataframe(
    df,
    column_config={
        "name": "Name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
    use_container_width=True,
)

# ---------------------------------------------------------------------- #

st.divider()
st.subheader("AI Development Timeline")

with open("timeline.json", "r") as f:
    data = f.read()

timeline(data, height=800)
