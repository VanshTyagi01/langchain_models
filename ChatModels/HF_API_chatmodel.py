from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os


load_dotenv()
hf_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
# print("API Key:", hf_api_key)

mo = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    model_kwargs={"api_key": hf_api_key}
)
model = ChatHuggingFace(llm=mo)
result = model.invoke("what is the capital of india")
print(result.content)