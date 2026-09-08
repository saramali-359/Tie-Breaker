import streamlit as st
import google.generativeai as genai

# 1. Configure the API key securely
genai.configure(api_key=st.secrets["API_KEY"])

# 2. Set up the app interface
st.title("My Google AI App")
st.write("Running directly in the browser!")

# 3. Create a text input for the user
user_prompt = st.text_input("Ask me anything:")

# 4. Generate the response
if st.button("Generate"):
    if user_prompt:
        model = genai.GenerativeModel('gemini-1.5-flash')
        with st.spinner("Thinking..."):
            response = model.generate_content(user_prompt)
            st.write(response.text)
    else:
        st.warning("Please enter a prompt.")
