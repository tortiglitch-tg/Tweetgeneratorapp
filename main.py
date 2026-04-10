import streamlit as st
import google.generativeai as genai

# Load API key securely
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Missing GOOGLE_API_KEY in Streamlit secrets")
    st.stop()

# Initialize Gemini 2.5 Flash
model = genai.GenerativeModel("gemini-2.5-flash")

# UI
st.header("Tweet Generator - Kasyap 🚀")
st.subheader("Generate tweets using Gemini 2.5 Flash")

topic = st.text_input("Enter topic")
number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1)

# Generate tweets
if st.button("Generate"):
    if not topic:
        st.warning("Please enter a topic")
    else:
        try:
            prompt = f"Generate {number} engaging tweets about {topic}"

            response = model.generate_content(prompt)

            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {str(e)}"))
    
