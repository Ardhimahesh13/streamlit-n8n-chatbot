import streamlit as st
import requests
import uuid  # <--- 1. Import this library

# --- CONFIGURATION ---
N8N_WEBHOOK_URL = "https://ardi96.app.n8n.cloud/webhook/chat"

st.title("🤖 My n8n Powered Chatbot")

# --- SESSION STATE SETUP ---
# 2. Create a unique Session ID for this specific user/browser tab
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- DISPLAY CHAT HISTORY ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- HANDLE USER INPUT ---
if prompt := st.chat_input("What's on your mind?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Send to n8n
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # 3. Send BOTH the message AND the sessionId
                payload = {
                    "message": prompt,
                    "sessionId": st.session_state.session_id 
                }
                
                response = requests.post(N8N_WEBHOOK_URL, json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    ai_reply = data.get("response", "Error: No response key found.")
                    st.markdown(ai_reply)
                    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            
            except Exception as e:
                st.error(f"Connection Failed: {e}")