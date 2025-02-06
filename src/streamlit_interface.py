import streamlit as st
from chatbot import send_prompt, establish_api

# Establish sessions state variable to save conversation history
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

message_history = st.session_state['message_history']

# Titles
st.title("Hello, I am Caregiver!")
st.write("Tell me what is on your mind.")

# Insert API key to get started
with st.sidebar:
    if "api_key" not in st.session_state:
        st.title("Insert API Key!")
        api_key = st.text_input("")
        if api_key:
            st.session_state["api_key"] = api_key
            st.write(establish_api(api_key))
        st.write("**To get started, you'll need a Gemini API key:**")

        instructions = """
        1. **Go to Google AI Studio:** Login and access the platform.
        2. **Click "Get API Key":** Locate the option to obtain an API key.
        3. **Choose Project:** Select a new or existing project for the API key.
        4. **Copy the Key:** Once generated, copy the API key here and have fun!
        """

        st.markdown(instructions)
    else:
        st.write("API Key already entered. Enjoy :D")
    
    
mood = st.radio(
    "How are you feeling?",
    ["Happy","Sad", "Angry", "Frustrated", "Exhausted"],
    
)

# Send, recieve and preserve conversation history
prompt = st.chat_input("Enter a prompt here")

messages = st.container()
if prompt:
    message_history.append({"user":prompt})
    response = send_prompt("You are an AI emotional support. Offer recommendation on how the user can improve their mood. The user is currently feeling {mood}. Here the user had said;" + prompt)
    message_history.append({"assistant":response})

for message in message_history:
    key, value = next(iter(message.items())) 
    messages.chat_message(key).write(value)

    
