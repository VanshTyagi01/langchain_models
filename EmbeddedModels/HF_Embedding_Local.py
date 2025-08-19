from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
# for multiple documents

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
vector = embeddings.embed_documents(documents)
# for single query
# text ='Delhi is the capital of India'
# vector = embeddings.embed_query(text)
print(vector)