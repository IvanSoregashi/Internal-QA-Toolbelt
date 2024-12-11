import streamlit as st


if st.session_state.user_object.is_basic_user():
    st.stop()

account_list = st.session_state.user_object.get_the_account_list()

st.selectbox("Accounts", account_list)