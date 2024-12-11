# ------------------------------------------------ IMPORTS ------------------------------------------------------
import streamlit as st
from sidebar import context

# --- PAGE SETUP ---
home_page = st.Page(
    "pages/Home page.py",
    title="Home page",
    icon=":material/account_circle:",
    default=True,
)
create_account_page = st.Page(
    "pages/Create account.py",
    title="Create an account",
    icon=":material/person_add:",
)
nav = st.navigation(
    {
        "Info": [home_page],
        "Accounts": [create_account_page],
    }
)

# ------------------------------------------ STREAMLIT SETTINGS -------------------------------------------------
page_title = "QA's Automagical Tooling"
page_icon = ":japanese_secret_button:"  # ":card_file_box:"
layout = "centered" if True else "wide"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
# ---------------------------------------------------------------------------------------------------------------

# ------------------------------------------ HIDE STREAMLIT STYLE -----------------------------------------------
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
# ---------------------------------------------------------------------------------------------------------------

with st.sidebar:
    # TODO Get Arlo Logo
    # st.logo("assets/codingisfun_logo.png")

    context()
    st.markdown("Made with 👋 by [Ivan](https://www.linkedin.com/in/ivan-shiriaev/)\t   \t[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/IvanSoregashi)")

nav.run()
