from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
#repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#repo_id="mistralai/Mistral-7B-Instruct-v0.3",
llm = HuggingFaceEndpoint(
    
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("create a question in bangla about dhaka city")

print(result.content)

# python 2.ChatModels/4.chatmodel