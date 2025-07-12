from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

chat_history = [SystemMessage(content='You are a helpful AI assistant')]
while True:
    msg = input('You: ')
    if msg.lower() != 'exit':
        chat_history.append(HumanMessage(content=msg))
        reply = model.invoke(chat_history).content
        print('Chatbot: ' + reply)
        chat_history.append(AIMessage(content=reply))
           
    else:
        print(chat_history)
        break

