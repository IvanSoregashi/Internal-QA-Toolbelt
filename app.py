import streamlit as st

st.set_page_config(layout="wide")


def update_environment(element):
    env = st.session_state[element]
    st.write(f"update_environment with {env}")
    st.query_params["env"] = env
    st.session_state.env_selectbox = env
    st.session_state.env_segmented = env
    st.session_state.env_radio = env

@st.fragment()
def context():
    """Context forms, sepecified in query, and sidebar"""
    # Collect specified query parameters
    user = st.query_params.get("user")
    env = st.query_params.get("env")
    account = st.query_params.get("account")
    device = st.query_params.get("device")

    # Verify specified query paramenters
    if env and env not in ["goldendev", "goldenqa", "production"]:
        del st.query_params["env"]
        env = None

    # Update session
    if "login_text_input" not in st.session_state:
        st.session_state.login_text_input = user
    if env and "env_selectbox" not in st.session_state:
        st.session_state.env_selectbox = env
        st.session_state.env_segmented = env
        st.session_state.env_radio = env

    # Login Form
    name = st.text_input("User", key="login_text_input", disabled=bool(user))

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Login", disabled=bool(user)) and name:
            st.query_params["user"] = name
            st.rerun()
    with col2:
        if st.button("Logout", disabled=(not bool(user))):
            del st.query_params["user"]
            del st.session_state["login_text_input"]
            st.rerun()

    # Environment Form

    st.selectbox("Choose the environment", ["goldendev", "goldenqa", "production"], key="env_selectbox", on_change=update_environment, args=("env_selectbox", ))

    st.radio("Environmenent", ["goldendev", "goldenqa", "production"], key="env_radio", horizontal=True, on_change=update_environment, args=("env_radio", ))
    st.segmented_control("Environmenent", ["goldendev", "goldenqa", "production"], key="env_segmented", selection_mode="single", on_change=update_environment, args=("env_segmented", ))

    # Account and Device Forms
    if account:
        account_field = st.text_input("Account", value=account, key="account_text_input")
    if device:
        device_field = st.text_input("Device", value=device, key="device_text_input")


with st.sidebar:
    st.title("Current Context")
    context()


st.title("Ivan's tooling site")
st.header(f"Hello {st.query_params.get("user", "")}")
with st.popover("state"):
    if st.button("update"):
        st.write(st.session_state)
