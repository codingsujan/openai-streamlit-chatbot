import openai
import os
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 150)

# Function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to the mic
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Speak now...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You:", text)
            return text
        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
            return None
        except sr.RequestError as e:
            print("❌ Speech service error:", e)
            return None

# Function to get GPT response
def get_response(prompt):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']

# Main loop
print("🎉 Voice Chatbot is ready! Say 'exit' to quit.")
while True:
    user_input = listen()
    if user_input is None:
        continue
    if user_input.lower() in ['exit', 'quit']:
        speak("Goodbye!")
        break

    reply = get_response(user_input)
    print("Bot:", reply)
    speak(reply)
