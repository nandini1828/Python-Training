from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_member():
    response = client.post(
        "/members/",
        json={"name": "Ada", "email": "ada@example.com"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["name"] == "Ada"
