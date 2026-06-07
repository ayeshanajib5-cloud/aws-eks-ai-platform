from fastapi import FastAPI
from pydantic import BaseModel
import time

app = FastAPI(
    title="Enterprise AI Platform API",
    description="Production-grade FastAPI service deployed on AWS EKS",
    version="1.0.0"
)

class PredictionRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {"message": "Enterprise AI Platform running on AWS EKS"}

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ai-platform-api"
    }

@app.get("/model-info")
def model_info():
    return {
        "model": "demo-ai-text-classifier",
        "version": "1.0.0",
        "environment": "production"
    }

@app.post("/predict")
def predict(request: PredictionRequest):
    start_time = time.time()

    return {
        "input": request.text,
        "prediction": "positive" if len(request.text) % 2 == 0 else "negative",
        "confidence": 0.91,
        "latency_ms": round((time.time() - start_time) * 1000, 2)
    }