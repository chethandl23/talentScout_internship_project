import streamlit as st


def initialize_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "stage" not in st.session_state:
        st.session_state.stage = "greeting"
    if "candidate_info" not in st.session_state:
        st.session_state.candidate_info = {}
    if "tech_stack" not in st.session_state:
        st.session_state.tech_stack = []
    if "current_stack_index" not in st.session_state:
        st.session_state.current_stack_index = 0
    if "answers" not in st.session_state:
        st.session_state.answers = {}


def add_message(role, content):
    st.session_state.messages.append({
        "role": role,
        "content": content
    })


def get_messages():
    return st.session_state.messages