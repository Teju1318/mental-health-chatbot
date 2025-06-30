import streamlit as st

# Simple rule-based chatbot function
def get_response(user_input):
    user_input = user_input.lower()

    if "sad" in user_input or "depressed" in user_input:
        return "I'm really sorry you're feeling that way. You're not alone, and I'm here to listen. ❤️"
    elif "happy" in user_input or "excited" in user_input:
        return "That's wonderful to hear! 😊 Keep spreading the positivity!"
    elif "angry" in user_input or "frustrated" in user_input:
        return "I understand. Try taking a few deep breaths. Want to talk about what happened?"
    elif "anxious" in user_input or "scared" in user_input:
        return "It’s okay to feel anxious sometimes. Would you like some calming tips?"
    elif "bye" in user_input or "thank you" in user_input:
        return "You're always welcome. Take care of yourself! 💚"
    else:
        return "I'm here for you. Please tell me more about how you're feeling."

# Streamlit UI
st.set_page_config(page_title="Mental Health Chatbot")
st.title("🧠 Mental Health Chatbot")
st.markdown("I'm here for you. Please share how you're feeling today.")

user_input = st.text_input("You:")
if user_input:
    reply = get_response(user_input)
    st.text_area("Chatbot:", value=reply, height=200)
