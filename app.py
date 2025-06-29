import streamlit as st

st.set_page_config(page_title="Mental Health Chatbot")

st.title("🧠 Mental Health Chatbot")
st.write("I'm here for you. Please share how you're feeling.")

user_input = st.text_input("You:")

def get_response(text):
    text = text.lower()
    if "happy" in text:
        return "😊 That's wonderful! I'm so glad to hear you're feeling happy."
    elif "sad" in text:
        return "😔 I'm sorry you're feeling sad. Want to talk about it?"
    elif "angry" in text or "mad" in text:
        return "😠 It's okay to feel angry. Take a deep breath. Want to share more?"
    elif "stressed" in text or "anxious" in text:
        return "😟 I'm here for you. Try to take things one step at a time."
    else:
        return "Thank you for sharing. I'm here to listen. ❤️"

if user_input:
    bot_response = get_response(user_input)
    st.write("Bot:", bot_response)

