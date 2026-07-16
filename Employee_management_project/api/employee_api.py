"""Employee FastAPI router."""

import asyncio

from fastapi import APIRouter, HTTPException, Query

from models.employee import Employee, EmployeeCreate, EmployeeUpdate
from services.employee_service import get_employee_service

router = APIRouter()


class EmployeeAPI:
    """Backward-compatible wrapper around the employee service."""

    def __init__(self) -> None:
        self.service = get_employee_service()

    def add_employee(self, employee: Employee) -> Employee:
        return self.service.add_employee(employee)

    def list_employees(self) -> list[Employee]:
        return self.service.list_employees()


@router.get("", response_model=list[Employee])
def list_employees() -> list[Employee]:
    """List all employees."""
    return get_employee_service().list_employees()


@router.get("/async", response_model=list[Employee], include_in_schema=False)
async def list_employees_async() -> list[Employee]:
    """List all employees asynchronously."""
    await asyncio.sleep(0.01)
    return get_employee_service().list_employees()


@router.post("", response_model=Employee)
def create_employee(employee: EmployeeCreate) -> Employee:
    """Create a new employee."""
    created = get_employee_service().add_employee(
        Employee(employee.employee_id, employee.name, employee.department, employee.salary, employee.role)
    )
    return created


@router.get("/role", response_model=list[Employee])
def get_employees_by_role(role: str = Query(default="", description="Employee role to filter by")) -> list[Employee]:
    """Get employees by role using a query parameter."""
    if not role:
        return get_employee_service().list_employees()
    return get_employee_service().get_employees_by_role(role)


@router.post("/role", response_model=Employee)
def assign_employee_role(
    employee_id: int = Query(..., description="Employee id to update"),
    role: str = Query(..., description="Role to assign"),
) -> Employee:
    """Assign a role to an employee using query parameters."""
    updated = get_employee_service().assign_role(employee_id, role)
    if updated is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated


@router.get("/{employee_id}", response_model=Employee)
def get_employee(employee_id: int) -> Employee:
    """Fetch one employee by id."""
    employee = get_employee_service().get_employee(employee_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.put("/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeUpdate) -> Employee:
    """Update an existing employee."""
    updated = get_employee_service().update_employee(employee_id, **employee.model_dump(exclude_none=True))
    if updated is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated


@router.delete("/{employee_id}")
def delete_employee(employee_id: int) -> dict[str, str]:
    """Delete an employee."""
    deleted = get_employee_service().delete_employee(employee_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted"}


@router.get("/search")
def search_employees(name: str | None = Query(default=None), department: str | None = None) -> list[Employee]:
    """Search employees by name and department."""
    employees = get_employee_service().list_employees()
    if name:
        employees = [employee for employee in employees if name.lower() in employee.name.lower()]
    if department:
        employees = [employee for employee in employees if employee.department.lower() == department.lower()]
    return employees

