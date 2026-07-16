"""Tests for FastAPI endpoints."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint_returns_ok() -> None:
    """Health route should return a status message."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_employees_returns_data() -> None:
    """Employees route should return records."""
    response = client.get("/employees")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_search_employees_route_returns_matches() -> None:
    """The search route should return employees matching the keyword."""
    response = client.get("/employees/search?keyword=Alice")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_employees_route_returns_filtered_results() -> None:
    """The filter route should accept department and salary query parameters."""
    response = client.get("/employees/filter?department_id=D001&minimum_salary=50000")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_form_endpoint_creates_employee() -> None:
    """The form endpoint should accept form data and create an employee."""
    response = client.post(
        "/employees/form",
        data={
            "employee_id": "E900",
            "first_name": "Test",
            "last_name": "User",
            "age": 30,
            "email": "test.user@example.com",
            "department_id": "D001",
            "salary": 55000,
            "city": "Boston",
            "state": "MA",
            "country": "USA",
            "postal_code": "02101",
        },
    )
    assert response.status_code == 201
    assert response.json()["message"] == "Employee created from form"
