from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
# select the models
model = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
result = model.embed_query("Delhi is capital of india")
# result will show the numbers 
print(str(result))