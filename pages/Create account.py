import streamlit as st
from utils import ensure_email


def validate_email():
    email = st.session_state.email_input
    try:
        st.session_state.email_input = ensure_email(email)
        st.session_state.valid_email = True
    except RuntimeError as e:
        st.session_state.valid_email = False

# ---------------------------------------------- COMPONENTS -----------------------------------------------------


@st.fragment
def account_creation_container():
    if not st.session_state.env:
        st.warning("Environment must be selected before account can be created")
        st.stop()

    st.text_input("E-mail:", key="email_input", on_change=validate_email)

    if "valid_email" not in st.session_state:
        st.warning("Please Provide an email to continue")
        st.stop()

    if not st.session_state.valid_email:
        st.error(f"Could not construct email from data {st.session_state.email_input} only letters, numbers and _.+- symbols can be used")
        st.stop()

    arlo_tab, legacy_tab, calix_tab, verisure_tab = st.tabs(["Arlo", "Legacy", "Calix", "Verisure"])

    with arlo_tab:
        st.selectbox("Country Code", ["US"], key="arlo_country_code")
        st.selectbox("Language", ["en-us"], key="arlo_language")

        col_sel, col_opt = st.columns([1, 4])

        with col_sel:
            st.checkbox("Basic", key="basic_checkbox", help="Only first step of account creation is performed")
            st.checkbox("MFA", key="mfa_checkbox", value=True, disabled=(st.session_state.env == "production"), help="Self-explanatory. Disable MFA for the account. Not available in production.")

        with col_opt:
            st.slider("Locations", min_value=0, max_value=5, disabled=st.session_state.basic_checkbox)

    with legacy_tab:
        st.selectbox("Country Code", ["US"], key="legacy_country_code")
        st.selectbox("Language", ["en-us"], key="legacy_language")
        col_sel, col_opt = st.columns([1, 4])

    if st.button("Submit"):
        st.success("Account created! (not really)")
# ---------------------------------------------------------------------------------------------------------------


st.header("Create an account")
account_creation_container()
