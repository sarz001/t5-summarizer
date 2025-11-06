from fastapi import FastAPI
from pydantic import BaseModel
from app.summarizer import summarize
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="T5 Text Summarizer API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all origins (or specify domains)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Request(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(req: Request):
    summary = summarize(req.text)
    return {"summary": summary}

@app.get("/health")
def health():
    return {"status": "ok"}
