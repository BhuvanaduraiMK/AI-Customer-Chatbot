import streamlit as st
from ai_chatbot import ask_ai

st.set_page_config(
    page_title="AI Customer Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Customer Assistant")

st.write(
    "Welcome! I can help with customer registration, "
    "renewals and product recommendations."
)

if st.button("🔄 Start New Conversation"):

    st.session_state.messages = []

    st.session_state.interaction_id = None

    st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []


if "interaction_id" not in st.session_state:
    st.session_state.interaction_id = None

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

user_message = st.chat_input(
    "Type your message..."
)


if user_message:
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):

        st.markdown(user_message)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response, interaction_id = ask_ai(
                user_message,
                st.session_state.interaction_id
            )

        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    st.session_state.interaction_id = interaction_id