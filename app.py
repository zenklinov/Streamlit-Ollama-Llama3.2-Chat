from langchain_community.llms import Ollama
import streamlit as st
import torch

# Check if CUDA is available
device = "cuda" if torch.cuda.is_available() else "cpu"

llm = Ollama (model = "llama3.2") #Adjust the model based on the model you want

st.title("Chatbot using llama3.2")

prompt = st.text_area("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner ("Generating response..."):
            st.write(llm.invoke(prompt,stop=['<|eot_id|>']))
