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

st.info(
    "This page is designed to showcase the prompt engineering guide with recommended prompt template, and allows users to create their own prompt templates.",
    icon="ℹ️",
)

# ---------------------------------------------------------------------- #

from streamlit_ace import st_ace

from global_data import PROMPT_GUIDE, PROMPT_TEMPLATE

guide_tab, template_tab, creation_tab = st.tabs(
    [
        "🚀 Prompt Engineering Guide",
        "🎈 Recommended Prompt Template",
        "🎉 Create Your Own Prompt Template",
    ]
)

if "custom_prompt" not in st.session_state:
    st.session_state.custom_prompt = ""

with guide_tab:
    st.markdown(PROMPT_GUIDE["init"])

    st.header("📚 Introduction")
    with st.expander("🔑 LLM Settings", expanded=False):
        st.markdown(PROMPT_GUIDE["settings"])
    with st.expander("🔑 Basics of Prompting", expanded=False):
        st.markdown(PROMPT_GUIDE["basics"])
    with st.expander("🔑 Prompt Elements", expanded=False):
        st.markdown(PROMPT_GUIDE["elements"])
    with st.expander("🔑 General Tips for Designing Prompts", expanded=False):
        st.markdown(PROMPT_GUIDE["tips"])
    with st.expander("🔑 Examples of Prompts", expanded=False):
        st.markdown(PROMPT_GUIDE["examples"])

    st.header("💎 Techniques")
    with st.expander("✏️ Zero-shot Prompting", expanded=False):
        st.markdown(PROMPT_GUIDE["zero-shot"])
    with st.expander("✏️ Few-shot Prompting", expanded=False):
        st.markdown(PROMPT_GUIDE["few-shot"])
    with st.expander("✏️ Chain-of-Thought Prompting", expanded=False):
        st.markdown(PROMPT_GUIDE["CoT"])
    with st.expander("✏️ Self-Consistency", expanded=False):
        st.markdown(PROMPT_GUIDE["SC"])
    with st.expander("✏️ Generate Knowledge Prompting", expanded=False):
        st.markdown(PROMPT_GUIDE["GK"])
    with st.expander("✏️ More Techniques", expanded=False):
        st.markdown(PROMPT_GUIDE["more"])

with template_tab:
    (
        creative_tab,
        scientific_tab,
        journalistic_tab,
        dramatic_tab,
        artistic_tab,
    ) = st.tabs(
        [
            "✏️ Creative",
            "🔬 Scientific",
            "🗞️ Journalistic",
            "🎭 Dramatic",
            "🎨 Artistic",
        ]
    )

with creative_tab:
    st.markdown(PROMPT_TEMPLATE["creative"])

with scientific_tab:
    st.markdown(PROMPT_TEMPLATE["scientific"])

with journalistic_tab:
    st.markdown(PROMPT_TEMPLATE["journalistic"])

with dramatic_tab:
    st.markdown(PROMPT_TEMPLATE["dramatic"])

with artistic_tab:
    st.markdown(PROMPT_TEMPLATE["artistic"])

with creation_tab:
    st.markdown("🖋️ Write Down Your Ideas and 🍎 Save to Your Account!")
    content = st_ace()
    if (
        content is not None
        and len(content) > 0
        and st.session_state.custom_prompt != content
    ):
        st.session_state.custom_prompt = content
        st.toast("Save successfully", icon="🎉")
