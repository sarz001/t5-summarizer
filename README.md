# T5-Based Text Summarization API

This project implements a **fine-tuned T5 abstractive summarization model** served through a production-ready **FastAPI** backend. The model is packaged using **Docker** and deployed easily on cloud platforms.

---

## 🚀 Features

- Fine-tuned **T5** model for domain-specific summarization
- Real-time inference via **FastAPI REST API**
- **Dockerized** for portable and reproducible deployment
- **Git LFS** used to manage large model files efficiently
- Ready for **cloud deployment** (Render / Railway / AWS / GCP)

---

## 📂 Project Structure

t5_Summarizer/
├── Dockerfile
├── requirements.txt
├── app/
│   ├── main.py        # FastAPI endpoints
│   └── summarizer.py  # Model loading + inference
└── t5_finetuned/      # Fine-tuned T5 model (tracked with Git LFS)
