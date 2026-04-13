from fastapi import FastAPI
from app.routers import translate

app = FastAPI(
    title='Translation API',
    description='Text translation using HF model',
    version='1.0.0'
)

app.include_router(translate.router, prefix="/translate", tags=["Translation"])

@app.get("/")
def root():
    return {
        "message": "Welcome to Translation API from VLT",
        "guidance": "Write your text, source language and target language you want to translate into!"
    }

@app.get("/health")
def health():
    return {
        "status": "oke hehe"
    }