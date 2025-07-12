from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#text = "Dhaka is the capital of Bangladesh"

#vector = embedding.embed_query(text)

#print(str(vector))

documents = [
    "Dhaka is the capital of Bangladesh",
    "Chattogram is the financial capital of Bangladesh"
]

vector = embedding.embed_documents(documents)

print(str(vector))

