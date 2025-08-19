from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
# embed multiple documents 
result = model.embed_documents(documents)
# result will be in 2D matrix 
print(str(result))