import streamlit as st
from transformers import pipeline
@st.cache_resource
def load_model():
    return pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad"
        )
qa=load_model()
context="""
Python is high level language.
Python can be understood by everyone.
Python contains variables and functions.
Python can be used in automations,web
"""
st.title("Python chatbot")
question=st.text_input("Ask a question")
if st.button("get answer"):
    if question:
        result=qa(context=context,question=question,max_answer_len=10)
        st.success(result["answer"])
    else:
        st.warning("Please enter a valid question")