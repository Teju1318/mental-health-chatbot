import streamlit as st
import openai
import os

# Use the latest client API
from openai import OpenAI

# Initialize the client with your secret
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def get_response(user_input):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a supportive mental health assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return chat_completion.choices[0].message.content

# Streamlit UI
st.set_page_config(page_title="Mental Health Chatbot")
st.title("🧠 Mental Health Chatbot")
st.markdown("I'm here for you. Please share how you're feeling today.")

user_input = st.text_input("You:")
if user_input:
    response = get_response(user_input)
    st.text_area("Chatbot:", value=response, height=200)
