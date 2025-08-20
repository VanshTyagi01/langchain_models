from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
st.header("Research Tool")

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
user_input = st.text_input("Enter your prompt")

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)