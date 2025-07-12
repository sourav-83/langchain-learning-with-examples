from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(  
    model_id = "Qwen/Qwen2.5-7B-Instruct",  # updated model
    task = 'text-generation',
    pipeline_kwargs = dict(  
        temperature = 0.3,
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)

# Example: Generating a question in Bengali
result = model.invoke("বাংলাদেশের রাজধানীর নাম কী?")

print(result.content)
