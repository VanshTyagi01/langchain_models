from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
st.header("Research Tool")

paper_input = st.text_input("Enter title of the Research Paper")
# paper_input = st.selectbox("Select Research Paper Name", ["Attention is All You Need", "BERT: Pre-Training of Bidirectional Transformers",  "GPT-3: Language Models are Few Shots Learners", "Diffusio Models Beats GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Begineer-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation length", ["short(1-2 Paragraph)", "Medium (3-5 paragraph)", "Long (Detailed Explanation)"])

# template
# template = PromptTemplate(
#     template="""
# Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}
# 1. Mathematical Details:
# - Include relevant mathematical equations if present in the paper.
# - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
# 2. Analogies:
# - Use relatable analogies to simplify complex ideas.
# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=['paper_input', 'style_input', 'length_input']
# validate_template=True
# )

template = load_prompt('D:/langchain_models/LangChain_Prompts_WorkFlow/template.json')

# fill the placeholders
# making the prompt from json
# prompt = template.invoke({
#         'paper_input':paper_input,
#         'style_input':style_input,
#         'length_input':length_input
#     })

# user_input = st.text_input("Enter your prompt")
if st.button('Summarize'):
    # making chain to reducr invoke times
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    
    # result = model.invoke(prompt)
    st.write(result.content)