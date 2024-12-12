import streamlit as st

from utils import is_username
from logic.user import User


def parse_query():
    # Collect specified query parameters
    user = st.query_params.get("user") or st.session_state.get("user") or ""
    env = st.query_params.get("env") or st.session_state.get("env") or None
    # account = st.query_params.get("account")
    # device = st.query_params.get("device")

    # Verify specified query paramenters
    if user and not is_username(user):
        if "user" in st.query_params: del st.query_params["user"]
        if "user" in st.session_state: del st.session_state["user"]
        user = ""

    if env and env not in ["goldendev", "goldenqa", "production"]:
        if "env" in st.query_params: del st.query_params["env"]
        if "env" in st.session_state: del st.session_state["env"]
        env = None

    state = {}
    if user: state["user"] = user
    if env: state["env"] = env

    st.query_params.update(state)
    st.session_state.update(state)

    # Update session
    # if user and "login_text_input" not in st.session_state:        st.session_state.login_text_input = user
    # if env and "env_segmented" not in st.session_state:        st.session_state.env_segmented = env


def user_object_validation():
    # Getting username or None
    username = st.session_state.get("user")

    if "user_object" not in st.session_state:
        # Initialize User with username and save into session object. Login operation
        st.session_state.user_object = User(username, "autologin")
    else:
        # User object is already initialized, verify that name is correct
        if st.session_state.user_object.name != username:
            # TODO log error
            st.session_state.user_object = User(username, "autologin")


def context():
    """Context forms, sepecified in query, and sidebar"""
    parse_query()
    user_object_validation()

    user = st.session_state.get("user")

    # Login Form
    name = st.text_input("User", key="user", disabled=bool(user))

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("Login", disabled=bool(user)) and name:
            st.query_params["user"] = name

            st.rerun()
    with col2:
        if st.button("Logout", disabled=(not bool(user))):
            del st.query_params["user"]
            del st.session_state["user"]
            st.session_state["user_object"] = User(None)
            st.rerun()

    # Environment Form

    st.segmented_control(
        "Environmenent",
        ["goldendev", "goldenqa", "production"],
        key="env",
        selection_mode="single",
        on_change=lambda: (st.query_params.update(env=st.session_state.env))
    )

    # Account and Device Forms
    # if account:        account_field = st.text_input("Account", value=account, key="account_text_input")
    # if device:        device_field = st.text_input("Device", value=device, key="device_text_input")

