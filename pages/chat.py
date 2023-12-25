import time

import streamlit as st
from openai import OpenAI

from st_pages import show_pages_from_config, add_page_title

from global_data import MODEL_OPTIONS, SYSTEM_PROMPT

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

def model_changed():
    st.toast("Model changed", icon="🎉")
    if "messages" in st.session_state and len(st.session_state["messages"]) > 2:
        st.session_state.pop("messages")
        load_main()


if st.session_state["authentication_status"]:
    with st.sidebar:
        model = st.radio(
            label="Model For Chat",
            options=("GPT-3.5", "GPT-4"),
            help="Choose a Model and Chat ~",
            horizontal=True,
            on_change=model_changed,
        )
        st.session_state["model"] = model

        openai_api_key = st.text_input(
            label="API Key",
            key="chatbot_api_key",
            type="password",
            placeholder="Enter your API key here...",
            label_visibility="collapsed",
        )

        with st.expander("ADVANCED SETTINGS", expanded=False):
            temperature = st.slider(
                label="temperature",
                min_value=0.0,
                max_value=2.0,
                value=1.0,
                step=0.01,
            )
            st.session_state["temperature"] = temperature
            model_name = st.selectbox(
                label="model name",
                options=MODEL_OPTIONS[model],
                placeholder="Select Model...",
                on_change=model_changed,
            )
            st.session_state["model_name"] = model_name
            max_tokens = st.slider(
                label="max tokens",
                min_value=4,
                max_value=4096,
                value=512,
                step=1,
            )
            st.session_state["max_tokens"] = max_tokens


# ---------------------------------------------------------------------- #

def role_changed():
    st.toast("Role changed", icon="🎉")
    load_main()


role = st.selectbox(
    label="Who do you want to talk to?",
    options=[
        "AI Assistant", "Research Assistant",
        "Soul Accompany", "Business Assistant",
        "Travel Assistant", "Translator",
        "Calculator",
    ],
    on_change=role_changed,
)
st.session_state["role"] = role


def load_main():
    with st.spinner("Loading..."):
        if st.session_state["authentication_status"]:
            if "messages" not in st.session_state:
                st.session_state["messages"] = [
                    {"role": "system", "content": SYSTEM_PROMPT[st.session_state["role"]]},
                    {"role": "assistant", "content": "How can I help you?"}
                ]
            else:
                st.session_state["messages"][0]["content"] = SYSTEM_PROMPT[st.session_state["role"]]

            for msg in st.session_state.messages:
                if msg["role"] != "system":
                    st.chat_message(msg["role"]).write(msg["content"])


load_main()

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add OpenAI API key to your account.")
        st.stop()

    # client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner("Waiting for response..."):
        time.sleep(3)
        # response = client.chat.completions.create(
        #     model=model,
        #     messages=st.session_state.messages,
        #     temperature=temperature,
        # )
        # msg = response.choices[0].message.content
        msg = (f"Response from {st.session_state['role']} {st.session_state['model_name']}"
               f" with temperature {st.session_state['temperature']}"
               f" and max tokens {st.session_state['max_tokens']}.\n"
               f" The system prompt is {st.session_state.messages[0]['content']}.")
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
