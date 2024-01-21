import os

from config import OPENAI_API_KEY
#openai.api_key=OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

from langchain_openai.llms import OpenAI

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")

query="Write five lines on Large Language Models"
answer=llm.invoke(query)

print(answer)