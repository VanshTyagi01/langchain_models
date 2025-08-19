from langchain_openai import OpenAIEmbeddings
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)
# embedding = GoogleGenerativeAIEmbeddings(model='gemini-embedding-001', dimensions=300)
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
    "Washington DC is the capital of USA",
    "Tokyo is the capital of Japan",
    "Virat Kohli is an indian cricketer ",
    "Ms Dohnio is former indian captan",
    "Rohit Sharma is known as Hit Machine",
    "Sachin Tendulkar is knowns as God of Cricket"
]

query = 'tell me about Rohit sharma'

#embeding of socuments 2D
doc_embeddings = embedding.embed_documents(documents)

# embedding of query 1D
query_embeddings = embedding.embed_query(query)

# cosine_similarity takes both as 2d and show the similaraties if query over documents
scores = cosine_similarity([query_embeddings], doc_embeddings)[0]

# make sure to attach positioning using enumerate function
# then sort and store last value index
index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("similarity score is : ", score)