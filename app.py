import streamlit as st
import openai

# Securely access your OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

st.set_page_config(page_title="Mental Health Chatbot")

st.title("🧠 Mental Health Chatbot")
st.write("I'm here for you. Please share how you're feeling today.")

# User input
user_input = st.text_input("You:")

# Generate GPT-based response
def get_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful mental health assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content
# If user types something, generate reply
if user_input:
    with st.spinner("Thinking..."):
        reply = get_response(user_input)
        st.write("Bot:", reply)

