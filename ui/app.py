import sys
from pathlib import Path

# Add project root directory to sys.path so 'chatbot' package is found
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

from chatbot.chatbot_agent import ChatbotAgent


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Intelligent Chatbot",
    page_icon="💬",
    layout="centered"
)


# --------------------------------------------------
# Initialize Chatbot Agent
# --------------------------------------------------

if "chatbot_agent" not in st.session_state:
    st.session_state.chatbot_agent = ChatbotAgent()


# --------------------------------------------------
# Initialize Conversation History
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# Page Header
# --------------------------------------------------

st.title("💬 Intelligent Support Chatbot")

st.write(
    "Ask questions about accounts, services, support, "
    "working hours, and contact information."
)


# --------------------------------------------------
# Display Conversation History
# --------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# --------------------------------------------------
# User Input
# --------------------------------------------------

user_input = st.chat_input("Type your message here...")


if user_input:
    # Add user message to conversation history
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    # Process message through chatbot agent
    result = st.session_state.chatbot_agent.process_message(
        user_input
    )

    chatbot_response = result["response"]

    # Add chatbot response to conversation history
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": chatbot_response
        }
    )

    # Rerun to display the updated conversation
    st.rerun()


# --------------------------------------------------
# Clear Conversation
# --------------------------------------------------

if st.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()
