from fastapi import FastAPI
from pydantic import BaseModel
from app.summarizer import summarize

app = FastAPI(title="T5 Text Summarizer API")

class Request(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(req: Request):
    summary = summarize(req.text)
    return {"summary": summary}

@app.get("/health")
def health():
    return {"status": "ok"}
