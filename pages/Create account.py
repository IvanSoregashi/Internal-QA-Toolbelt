import streamlit as st


# ---------------------------------------------- COMPONENTS -----------------------------------------------------
@st.fragment
def account_creation_container():
    if not st.session_state.env:
        st.warning("Environment must be selected before account can be created")
        st.stop()

    st.text_input("E-mail:", key="email")
    col1, col2 = st.columns([1, 4])

    with col2:
        result_banner = st.empty()

    with col1:
        if st.button("Check", use_container_width=True):
            result_banner.success("email is available")

    arlo_tab, legacy_tab, calix_tab, verisure_tab = st.tabs(["Arlo", "Legacy", "Calix", "Verisure"])

    with arlo_tab:
        st.selectbox("Country Code", ["US"], key="arlo_country_code")
        st.selectbox("Language", ["en-us"], key="arlo_language")
        col_sel, col_opt = st.columns([1, 4])

    with legacy_tab:
        st.selectbox("Country Code", ["US"], key="legacy_country_code")
        st.selectbox("Language", ["en-us"], key="legacy_language")
        col_sel, col_opt = st.columns([1, 4])

    with calix_tab:
        st.selectbox("Country Code", ["US"], key="calix_country_code")
        if "calix_partner_id" not in st.session_state:
            st.session_state.calix_partner_id = 'calix'
        partner_id = st.segmented_control("PartnerId",
                                          ['calix', 'calix-stg'],
                                          key="calix_partner_id")

    with verisure_tab:
        st.selectbox("Country Code", ["FR"], key="verisure_country_code")
        if "verisure_partner_id" not in st.session_state:
            st.session_state.verisure_partner_id = 'verisure-t'
        partner_id = st.segmented_control("PartnerId",
                                          ['verisure', 'verisure-d', 'verisure-s', 'verisure-t'],
                                          key="verisure_partner_id")

    if st.button("Submit"):
        st.success("Account created! (not really)")
# ---------------------------------------------------------------------------------------------------------------


st.header("Create an account")
account_creation_container()
