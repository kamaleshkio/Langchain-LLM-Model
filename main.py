import os 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain   
from langchain_community.llms import Ollama
import streamlit as st


st.title("Langchain Demo with LLaMA 3 (Local Via Ollama)")
input_txt = st.text_input("Enter a topic you want explained")

llm = Ollama(model="llama3")

#response = llm.invoke(input_txt)


prompt_template = PromptTemplate(
    input_variables=['topic'],
    template = "Explain {topic} in simple terms."
)

chains = LLMChain(
    llm = llm,
    prompt = prompt_template
)

output = chains.run(input_txt)

st.subheader("Response: ")
st.write(output)