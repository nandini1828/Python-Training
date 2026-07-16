from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_book():
    response = client.post(
        "/books/",
        json={"title": "Dune", "author": "Frank Herbert", "isbn": "9780441172719"},
    )
    assert response.status_code == 200
    payload = response.json()
    assert payload["title"] == "Dune"
