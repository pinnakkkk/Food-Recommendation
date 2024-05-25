import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome! 👋")

st.sidebar.success("Select a recommendation app.")

st.markdown(
    """
    Select a recommendation app from sidebar.
    """
)
