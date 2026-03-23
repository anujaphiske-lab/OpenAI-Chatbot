import streamlit as st
import openai
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


import os
from dotenv import load_dotenv
load_dotenv()

## Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGSMITH_PROJECT"] = "Simple Q&A ChatBot with OpenAI"
os.environ["LANGCHAIN_PROJECT"] = "Simple Q&A ChatBot with OpenAI 1.0"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to user queries."),
        ("user", "Question:{question}")
    ]
)

def genrate_response(question, api_key, llm, temperature, max_tokens):
    openai.api_key = api_key
    llm = ChatOpenAI(
        model=llm, 
        api_key=api_key,           # Forces use of the sidebar key
        temperature=temperature,   # Uses your slider value
        max_completion_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain= prompt|llm|output_parser
    answer= chain.invoke({'question':question})
    return answer

## Title of the app
st.title("Simple Q&A chatbot with OpenAI")

## Sidebar for settings
api_key=st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

## Drop down to select various LLM Models
llms = st.sidebar.selectbox("Select an Open AI Model", ["gpt-5.2-2025-12-11", "gpt-5-mini-2025-08-07", "gpt-5-nano-2025-08-07"])

## Slider from temperature
temperature = st.sidebar.slider("Temperature",min_value=0.0, max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)

## Main Interface for user Input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = genrate_response(user_input, api_key, llms, temperature, max_tokens)
    st.write(response)
else:
    st.write("Please provide the query")