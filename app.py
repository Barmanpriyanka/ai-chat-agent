import streamlit as st
from agent import ask_ai

st.set_page_config(page_title="AI Agent", page_icon="🤖")

st.title("🤖 My AI Agent")

# Chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input box
user_input = st.chat_input("Ask something...")

if user_input:
    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            response = ask_ai(user_input)
            st.write(response)

    # Store response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })