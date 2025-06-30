import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Local LLM Chatbot", page_icon="💬", layout="centered")

# App title and description
st.title("💬 Local LLM Chatbot")
st.markdown("Chat with your locally running LLM via Ollama. Powered by Streamlit frontend.")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
with st.chat_message("user"):
    user_input = st.text_input("You:", placeholder="Type your message here...")

# Process user input
if user_input:
    with st.spinner("Thinking..."):
        try:
            res = requests.post("http://localhost:8000/chat", json={"message": user_input})
            if res.status_code == 200:
                reply = res.json().get("reply", "No reply received.")
                
                # Add to chat history
                st.session_state.chat_history.append(("user", user_input))
                st.session_state.chat_history.append(("bot", reply))
            else:
                st.error(f"Server error: {res.status_code}")
        except Exception as e:
            st.error(f"Error: {e}")

# Display chat history
for sender, msg in st.session_state.chat_history:
    with st.chat_message("user" if sender == "user" else "assistant"):
        st.markdown(msg)
