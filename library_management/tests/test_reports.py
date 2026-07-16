from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_reports_summary():
    response = client.get("/reports/summary")
    assert response.status_code == 200
    payload = response.json()
    assert "total_books" in payload
    assert "total_members" in payload
