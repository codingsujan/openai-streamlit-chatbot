
from PIL import Image
import streamlit as st

image = Image.open("openai.png",)
st.image(image, width=130)
# Page setup
st.set_page_config(
    page_title="KSC OpenAI (free)",)
# Hide Streamlit UI elements
st.markdown("""
    <style>
    [data-testid="stToolbar"], footer, header { visibility: hidden !important; }
    .block-container { padding-top: 1rem; max-width: 800px; margin: auto; }
    body { background-color: #f0f2f6; }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 style='text-align: center; font-weight: bold;'> KSC OpenAI (Free)</h1>", unsafe_allow_html=True)

# Puter.js Chat Interface Styled like ChatGPT
st.components.v1.html("""
  <script src="https://js.puter.com/v2/"></script>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
    }
    #chat-box {
      background-color: white;
      border-radius: 10px;
      padding: 20px;
      height: 400px;
      overflow-y: auto;
      box-shadow: 0 0 10px rgba(0,0,0,0.05);
    }
    .user-msg, .bot-msg {
      margin: 10px 0;
      padding: 10px 15px;
      border-radius: 10px;
      max-width: 80%;
      white-space: pre-wrap;
    }
    .user-msg {
      background-color: #daf0ff;
      align-self: flex-end;
      text-align: right;
      margin-left: auto;
    }
    .bot-msg {
      background-color: #f1f1f1;
      align-self: flex-start;
      text-align: left;
      margin-right: auto;
    }
    #input-area {
      display: flex;
      margin-top: 20px;
    }
    #input {
      flex: 1;
      padding: 10px;
      font-size: 1rem;
      border-radius: 8px;
      border: 1px solid #ccc;
    }
    #send-btn {
      padding: 10px 16px;
      margin-left: 10px;
      background-color: #10a37f;
      color: white;
      border: none;
      border-radius: 8px;
      font-weight: bold;
      cursor: pointer;
    }
  </style>

  <div style="display: flex; flex-direction: column;">
    <div id="chat-box"></div>
    <div id="input-area">
      <textarea id="input" rows="2" placeholder="Send a message..."></textarea>
      <button id="send-btn" onclick="sendMsg()">Send</button>
    </div>
  </div>

  <script>
    const chatBox = document.getElementById("chat-box");

    function appendMessage(content, className) {
      const msg = document.createElement("div");
      msg.className = className;
      msg.innerText = content;
      chatBox.appendChild(msg);
      chatBox.scrollTop = chatBox.scrollHeight;
    }

    async function sendMsg() {
      const inputElem = document.getElementById("input");
      const text = inputElem.value.trim();
      if (!text) return;
      appendMessage(text, "user-msg");
      inputElem.value = "";
      appendMessage("Thinking...", "bot-msg");

      const allMsgs = document.getElementsByClassName("bot-msg");
      const lastBot = allMsgs[allMsgs.length - 1];

      let output = "";
      for await (const part of await puter.ai.chat(text, {stream: true})) {
        output += part.text;
        lastBot.innerText = output;
      }
    }
  </script>
""", height=600)
