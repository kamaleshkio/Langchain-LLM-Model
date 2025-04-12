import os 
from constant import API_KEY
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain   
import streamlit as st

st.title("Langchain demo with Gemini 2.0 Flash")
input_txt = st.text("Search What you want")

llm = GoogleGenerativeAI(
    model = "google-flash-2.0",
    google_api_key = API_KEY
)

response = llm.invoke(input_txt)

prompt = PromptTemplate(
    input_variables=['topic'],
    template = "Explain {topic} in simple terms."
)

chains = LLMChain(
    llm = llm,
    prompt = prompt
)
output = chains.run("black Holes")
print(output)