import streamlit as st
from form_page import form_page
from detailpage import detail_page

# Logika navigasi
if "page" not in st.session_state:
    st.session_state["page"] = "form"  # Default ke halaman form

# Navigasi berdasarkan state
if st.session_state["page"] == "form":
    form_page()
elif st.session_state["page"] == "detail":
    detail_page()
