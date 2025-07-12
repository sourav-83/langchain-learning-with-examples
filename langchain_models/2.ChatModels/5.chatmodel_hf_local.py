from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(  
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = 'text-generation',
    pipeline_kwargs = dict(  
        temperature = .3,
        max_new_tokens = 100
    )
)
model = ChatHuggingFace(llm=llm)

result = model.invoke("create a question in Bengali about Dhaka city")

print(result.content)

# python 2.ChatModels/5.chatmodel_hf_local.py