import openai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Chat function
def chat_with_gpt(user_input):
    messages = [
        {"role": "system", "content": "You are a friendly assistant."},
        {"role": "user", "content": user_input}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=messages
    )
    return response['choices'][0]['message']['content']

# Simple loop
print("Chatbot is running! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    answer = chat_with_gpt(user_input)
    print("Bot:", answer)
