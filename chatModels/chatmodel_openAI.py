from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model= ChatOpenAI(model='gpt-4',temperature=0.5,max_completion_tokens=40)
# can tell max words which are in outpu max_completion_tokens 
# temperature - creative response (randomness of lang model)
#0-0.3 deterministic and predictible 1.5 creative random diverse

result=model.invoke("What is the capital of India")
print(result)# it will give content as well as some keyword arguments also in result different to llm

print(result.content)#will only give this answer


