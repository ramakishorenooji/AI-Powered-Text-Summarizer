import streamlit as st
import requests

API_URL = "http://localhost:8000/summarize/"

st.title("AI-Powered Text Summarizer")
text = st.text_area("Enter text to summarize:")

if st.button("Summarize"):
    response = requests.post(API_URL, json={"text": text})
    summary = response.json().get("summary", "Error fetching summary")
    st.subheader("Summary:")
    st.write(summary)
