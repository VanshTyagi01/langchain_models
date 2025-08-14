from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
# load API key in environment
load_dotenv()
# select model 
model = ChatAnthropic(model='claude-3-5-sonnet-20241022')
# start conversation
result = model.invoke("What is the capital of india")
# result
print(result)