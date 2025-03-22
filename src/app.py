import streamlit as st
import requests

st.title("AI-Powered Text Summarizer")

text = st.text_area("Enter your text here to summarize:")

if st.button("Summarize"):
    if text:
        response = requests.post("http://localhost:8000/summarize", json={"text": text})
        summary = response.json()["summary"]
        st.subheader("Summary:")
        st.write(summary)




