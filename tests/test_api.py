from fastapi.testclient import TestClient

from api.main import app


def test_health_endpoint_returns_platform_status():
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "ai-platform-api",
    }


def test_model_info_exposes_demo_model_metadata():
    client = TestClient(app)

    response = client.get("/model-info")

    assert response.status_code == 200
    assert response.json()["model"] == "demo-ai-text-classifier"


def test_predict_returns_deterministic_demo_prediction():
    client = TestClient(app)

    response = client.post("/predict", json={"text": "platform"})

    assert response.status_code == 200
    body = response.json()
    assert body["input"] == "platform"
    assert body["prediction"] == "positive"
    assert body["confidence"] == 0.91
    assert "latency_ms" in body
