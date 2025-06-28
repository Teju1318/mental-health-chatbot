import streamlit as st

st.title("🧠 Mental Health Chatbot")
st.write("I'm here for you. Please share how you're feeling.")

user_input = st.text_input("You:")

if user_input:
    st.success("Bot: I hear you. You're not alone. Everything will be okay.")
