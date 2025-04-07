from transformers import pipeline
import streamlit as st

# Load a lightweight Hugging Face model (FLAN-T5 small)
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

st.title("🤖 Free AI Chatbot")

question = st.text_input("Enter Your Question:")

if st.button("Get Answer") and question:
    with st.spinner("Generating answer..."):
        response = qa_pipeline(question, max_length=100)
        st.subheader("Answer:")
        st.write(response[0]['generated_text'])