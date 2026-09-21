from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_openapi_schema():
    r = client.get("/openapi.json")
    assert r.status_code == 200
    assert "paths" in r.json()

def test_docs_available():
    assert client.get("/docs").status_code == 200
