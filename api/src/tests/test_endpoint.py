"""
A test script to check connection to the app.
"""

from src.article_retriever.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    """
    Tests the endpoints of our fastapi app
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
