#any open ai model will not work as i didn't buy enough credits

from langchain_openai import OpenAI
from dotenv import load_dotenv
# load api key from environment
load_dotenv()
# choose the model
llm = OpenAI(model='gpt-3.5-turbo-instruct')
# start conversation and store the result
result = llm.invoke("What is capital of india")
# print result
print(result)