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
    with st.sidebar:
        st.error(
            "Username or password is incorrect, please check your username and password in *[home](/)* page."
        )
elif st.session_state["authentication_status"] is None:
    with st.sidebar:
        st.warning(
            "Please enter your username and password in *[home](/)* page."
        )

# ---------------------------------------------------------------------- #

st.info(
    "This page serves as the personal account center, offering a series of settings for both logged-in and logged-out users.",
    icon="ℹ️",
)

# ---------------------------------------------------------------------- #

if st.session_state["authentication_status"]:
    with st.expander("Settings for logged-in users"):
        # Reset password
        try:
            if authenticator.reset_password(
                st.session_state["username"], "Reset password"
            ):
                with open("config.yaml", "w") as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.toast("Password modified successfully", icon="🎉")
                st.balloons()
        except Exception as e:
            st.error(e)
        # Update user details
        try:
            if authenticator.update_user_details(
                st.session_state["username"], "Update user details"
            ):
                with open("config.yaml", "w") as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.toast("Entries updated successfully", icon="🎉")
                st.balloons()
        except Exception as e:
            st.error(e)

with st.expander("Settings for all users"):
    # Register user
    try:
        if authenticator.register_user("Register user", preauthorization=False):
            with open("config.yaml", "w") as file:
                yaml.dump(config, file, default_flow_style=False)
            st.toast("User registered successfully", icon="🎉")
            st.balloons()
    except Exception as e:
        st.error(e)
    # Forgot password
    try:
        (
            username_of_forgotten_password,
            email_of_forgotten_password,
            new_random_password,
        ) = authenticator.forgot_password("Forgot password")
        if username_of_forgotten_password:
            with open("config.yaml", "w") as file:
                yaml.dump(config, file, default_flow_style=False)
            st.toast("New password to be sent securely", icon="🎉")
            st.balloons()
            # Random password should be transferred to user securely
        else:
            st.error("Username not found")
    except Exception as e:
        st.error(e)
    # Forgot username
    try:
        (
            username_of_forgotten_username,
            email_of_forgotten_username,
        ) = authenticator.forgot_username("Forgot username")
        if username_of_forgotten_username:
            st.toast("Username to be sent securely", icon="🎉")
            st.balloons()
            # Username should be transferred to user securely
        else:
            st.error("Email not found")
    except Exception as e:
        st.error(e)
