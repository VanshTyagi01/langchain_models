#any open ai model will not work as i didn't buy enough credits

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
#load the API key
load_dotenv()
# select the model
model = ChatOpenAI(model='gpt-4', temperature=1.2, max_completion_tokens=20)
#start the conversation
result = model.invoke("What is the capital of india")
print(result.content)