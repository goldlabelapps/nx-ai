import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_queue():
    response = client.get("/queue")
    assert response.status_code == 200
    data = response.json()
    assert "meta" in data
    assert "data" in data
    queue_data = data["data"]
    assert "filters" in queue_data
    assert "filtered" in queue_data
    assert "total" in queue_data
    assert "next" in queue_data
    assert "collections" in queue_data["filters"]
    assert "groups" in queue_data["filters"]
    assert "collectionFilter" in queue_data["filters"]
    assert "groupFilter" in queue_data["filters"]
    meta = data["meta"]
    assert meta["severity"] == "success"
    assert meta["title"] == "Queue table info"
