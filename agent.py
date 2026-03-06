import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

llm = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    api_version="2024-02-15-preview",
    temperature=0
)

prompt = PromptTemplate(
    input_variables=["code"],
    template="""
You are an expert Python developer specialized in testing.

Generate pytest unit tests for the following Python code.

Rules:
- First line must be: import pytest
- Use functions starting with test_
- Include success cases
- Include failure cases

Python code:
{code}
"""
)

def generate_tests(code):
    chain = prompt | llm
    response = chain.invoke({"code": code})
    return response.content
