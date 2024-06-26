import os
import boto3
import json
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConstitutionalChain


from dotenv import load_dotenv



load_dotenv()

def demo_chatbot(input_text):
    
    boto3.setup_default_session(
    aws_access_key_id = os.getenv("aws_access_key_id"),
    aws_secret_access_key= os.getenv("aws_secret_access_key"),
    region_name = os.getenv("region_name"),
    )
                            
    bedrock_runtime = boto3.client(service_name='bedrock-runtime')


    demo_llm = Bedrock(
    model_id='meta.llama2-70b-chat-v1',
    client=bedrock_runtime,
    model_kwargs={
        "temperature": 0.9,
        "top_p": 0.5,
        "max_gen_len": 512
    })

    return  demo_llm.predict(input_text)
response = demo_chatbot("Hi, what is yor name?")
print(response)