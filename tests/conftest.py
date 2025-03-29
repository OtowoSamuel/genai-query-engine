import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_token(client):
    response = client.post("/login?username=demo&password=demo123")
    return response.json()["access_token"]