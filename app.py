import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load the API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="OpenAI Chatbot", page_icon="💬")
st.title("💬 KSC OpenAI ")

# Session state to store messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display conversation history
for msg in st.session_state.messages[1:]:
    st.markdown(f"**{'👤 You' if msg['role']=='user' else '🤖 Bot'}:** {msg['content']}")

# Text input
user_input = st.chat_input("Say something...")

# When user sends a message
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
