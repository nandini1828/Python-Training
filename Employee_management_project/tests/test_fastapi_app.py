from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "Employee Management API"


def test_list_employees():
    response = client.get("/employees")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_create_employee():
    payload = {
        "employee_id": 100,
        "name": "Test Employee",
        "department": "Operations",
        "salary": 5000,
    }
    response = client.post("/employees", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == "Test Employee"


def test_assign_and_list_employee_role():
    payload = {
        "employee_id": 200,
        "name": "Role Test Employee",
        "department": "Operations",
        "salary": 5500,
        "role": "Manager",
    }
    created_response = client.post("/employees", json=payload)
    assert created_response.status_code == 200
    employee_id = created_response.json()["employee_id"]

    assign_response = client.post(
        "/employees/role",
        params={"employee_id": employee_id, "role": "Manager"},
    )
    assert assign_response.status_code == 200
    assert assign_response.json()["role"] == "Manager"

    list_response = client.get("/employees/role", params={"role": "Manager"})
    assert list_response.status_code == 200
    data = list_response.json()
    assert any(item["employee_id"] == employee_id for item in data)


def test_create_report():
    payload = {
        "title": "Quarterly Report",
        "notes": "Generated from the FastAPI app",
    }
    response = client.post("/reports", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["title"] == "Quarterly Report"
    assert body["employee_count"] >= 1
