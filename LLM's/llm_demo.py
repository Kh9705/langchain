#I dont have key right now just seeing how code works
import langchain
from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (make sure your .env has OPENAI_API_KEY)
load_dotenv()

# Initialize the model
llm = OpenAI(model="gpt-3.5-turbo-instruct")

# Ask a question
result = llm.invoke("What is the capital of India?")

print(result)
