from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Dhaka is the capital of Bangladesh",
    "Chattogram is the financial capital of Bangladesh"
]
result = embedding.embed_documents(documents)

print(str(result))