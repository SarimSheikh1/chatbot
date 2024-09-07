import google.generativeai as genai
import streamlit as st

# Retrieve API key from environment variable
GOOGLE_API_KEY = ('AIzaSyB8FdS5kWksD6aNsSx8RN_UkRXBZ-llvSM')

if GOOGLE_API_KEY is None:
    st.error("⚠️ API key not found. Please set the GOOGLE_API_KEY environment variable.")
else:
    # Configure API key
    genai.configure(api_key=GOOGLE_API_KEY)

    # Initialize the Generative Model
    model = genai.GenerativeModel('gemini-1.5-flash-001')

    def getResponsefromModel(user_input):
        try:
            response = model.generate_content(user_input)
            return response.text
        except Exception as e:
            return f"⚠️ Error occurred: {e}"

    st.title("🧐 Sarim Sheikh's Chatbot 🧐")
    st.write("✨✨ Powered by GEMINI API ✨✨")

    if "history" not in st.session_state:
        st.session_state["history"] = []

    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("💬 Type your message here:", max_chars=2000)
        submit_button = st.form_submit_button("🚀 Send")

        if submit_button:
            if user_input:
                response = getResponsefromModel(user_input)
                st.session_state.history.append((user_input, response))
                st.success("Message sent successfully! 👍")
            else:
                st.warning("😡🤬😭 Please enter a prompt! 😭😡🤬")

    # Display chat history
    if st.session_state["history"]:
        for i, (user_msg, bot_response) in enumerate(st.session_state["history"]):
            st.write(f"**You:** {user_msg}")
            st.write(f"**Bot:** {bot_response}")
