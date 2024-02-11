import streamlit as st
from vertexai import init, preview
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, GenerationConfig

# Initialize Vertex AI with your project ID
init(project="gemini-explorer-413721")

# Continue with your code
config = GenerationConfig(temperature=0.4)

# Load model with config
model = GenerativeModel("gemini-pro", generation_config=config)

# Start the chat session
chat = model.start_chat()

# Streamlit UI
st.title("Gemini Explorer Chat")

# Function to display chat messages
def display_chat_messages(chat_session, latest_user_input):
    # Display the latest user input
    if latest_user_input:
        st.text("You: " + latest_user_input)

    # Display chat history
    for msg in reversed(chat_session.history):
        if isinstance(msg, tuple) and len(msg) == 2:
            user_input, ai_response = msg
            st.text("You: " + user_input)
            st.text("Gemini Explorer: " + ai_response)

# Main Chat Loop
st.subheader("")  # Add space between title and input

user_input = st.text_input("Type your message here:", key="user_input")

if st.button("Send"):
    if user_input:
        try:
            # Try `add_message` first (if available)
            if hasattr(chat, "add_message"):
                chat.add_message("User", user_input)
            else:
                # Fallback to using `send_message` if `add_message` isn't available
                chat.send_message(user_input)
        except Exception as e:
            # Handle any unexpected errors gracefully
            st.error(f"Error adding message: {e}")

# Display messages regardless of method used
display_chat_messages(chat, user_input)



