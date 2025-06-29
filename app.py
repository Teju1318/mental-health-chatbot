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
def get_response(prompt):
   client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

reply = response.choices[0].message.content

    return response.choices[0].message.content

# If user types something, generate reply
if user_input:
    with st.spinner("Thinking..."):
        reply = get_response(user_input)
        st.write("Bot:", reply)

