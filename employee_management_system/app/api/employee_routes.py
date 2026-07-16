"""FastAPI routes for employee actions."""

from fastapi import APIRouter, Form, HTTPException, Query, status
from pydantic import BaseModel

from app.services.employee_service import EmployeeService

router = APIRouter()
service = EmployeeService()


class EmployeeCreateRequest(BaseModel):
    """Request payload for creating an employee."""

    employee_id: str
    first_name: str
    last_name: str
    age: int
    email: str
    department_id: str
    salary: float
    city: str
    state: str
    country: str
    postal_code: str


class EmployeeUpdateRequest(BaseModel):
    """Request payload for updating an employee."""

    first_name: str
    last_name: str
    age: int
    email: str
    department_id: str
    salary: float
    city: str
    state: str
    country: str
    postal_code: str


@router.get("", status_code=status.HTTP_200_OK)
async def list_employees() -> list[dict[str, object]]:
    """Return all employees."""
    employees = service.list_employees()
    return [employee.to_dict() for employee in employees]


@router.get("/search", status_code=status.HTTP_200_OK)
async def search_employees(keyword: str = Query(..., min_length=1)) -> list[dict[str, object]]:
    """Search employees using a query parameter."""
    employees = service.search_employees(keyword)
    return [employee.to_dict() for employee in employees]


@router.get("/filter", status_code=status.HTTP_200_OK)
async def filter_employees(
    department_id: str | None = Query(default=None),
    minimum_salary: float | None = Query(default=None),
) -> list[dict[str, object]]:
    """Filter employees by department or salary query parameters."""
    employees = service.filter_employees(department_id=department_id, minimum_salary=minimum_salary)
    return [employee.to_dict() for employee in employees]


@router.get("/{employee_id}", status_code=status.HTTP_200_OK)
def get_employee_by_id(employee_id: str) -> dict[str, object]:
    """Return a single employee by id."""
    employee = service.get_employee_by_id(employee_id)
    if employee is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return employee.to_dict()


@router.post("", status_code=status.HTTP_201_CREATED)
def create_employee(request: EmployeeCreateRequest) -> dict[str, str]:
    """Create a new employee from JSON body."""
    service.add_employee(
        employee_id=request.employee_id,
        first_name=request.first_name,
        last_name=request.last_name,
        age=request.age,
        email=request.email,
        department_id=request.department_id,
        salary=request.salary,
        city=request.city,
        state=request.state,
        country=request.country,
        postal_code=request.postal_code,
    )
    return {"message": "Employee created successfully"}


@router.put("/{employee_id}", status_code=status.HTTP_200_OK)
def update_employee(employee_id: str, request: EmployeeUpdateRequest) -> dict[str, str]:
    """Update an employee from JSON body."""
    existing = service.get_employee_by_id(employee_id)
    if existing is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")

    updated = existing
    updated.first_name = request.first_name
    updated.last_name = request.last_name
    updated.age = request.age
    updated.email = request.email
    updated.department_id = request.department_id
    updated.salary = request.salary
    updated.address.city = request.city
    updated.address.state = request.state
    updated.address.country = request.country
    updated.address.postal_code = request.postal_code

    service.update_employee(updated)
    return {"message": "Employee updated successfully"}


@router.delete("/{employee_id}", status_code=status.HTTP_200_OK)
def delete_employee(employee_id: str) -> dict[str, str]:
    """Delete an employee by id."""
    deleted = service.delete_employee(employee_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found")
    return {"message": "Employee deleted successfully"}


@router.post("/form", status_code=status.HTTP_201_CREATED)
def create_employee_from_form(
    employee_id: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    age: int = Form(...),
    email: str = Form(...),
    department_id: str = Form(...),
    salary: float = Form(...),
    city: str = Form(...),
    state: str = Form(...),
    country: str = Form(...),
    postal_code: str = Form(...),
) -> dict[str, str]:
    """Create an employee from HTML form data."""
    service.add_employee(
        employee_id=employee_id,
        first_name=first_name,
        last_name=last_name,
        age=age,
        email=email,
        department_id=department_id,
        salary=salary,
        city=city,
        state=state,
        country=country,
        postal_code=postal_code,
    )
    return {"message": "Employee created from form"}
