from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(input: TextInput):
    summary = summarizer(input.text, max_length=750, min_length=30, do_sample=False)
    return {"summary": summary[0]["summary_text"]}





