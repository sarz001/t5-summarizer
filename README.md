# T5-Based Text Summarization API

This project implements a **fine-tuned T5 abstractive summarization model** served through a production-ready **FastAPI** backend. The model is packaged using **Docker** and deployed easily on cloud platforms.

---

##  Features

- Fine-tuned **T5** model for domain-specific summarization
- Real-time inference via **FastAPI REST API**
- **Dockerized** for portable and reproducible deployment
- **Git LFS** used to manage large model files efficiently
- Ready for **cloud deployment** (Render / Railway / AWS / GCP)

---

##  Project Structure

<pre style="font-family: monospace;">
t5_Summarizer/
│   Dockerfile
│   requirements.txt
│
├── app/
│   ├── main.py         # FastAPI endpoints
│   └── summarizer.py   # Model loading + inference
│
└── t5_finetuned/       # Fine-tuned T5 model (tracked with Git LFS)
</pre>

## Run Locally

### 1) Activate Virtual Environment
$ source .venv/Scripts/activate
Windows users (PowerShell/CMD):
powershell.venv\Scripts\activate
### 2) Start API Server
bash$ python -m uvicorn app.main:app --reload --port 8000
### 3) Open Interactive API UI
texthttp://127.0.0.1:8000/doc

##  Run with Docker
### Build Image
docker build -t t5-summarizer .
### Run Container
docker run -p 8000:8000 t5-summarizer
### Access:
http://127.0.0.1:8000/docs
