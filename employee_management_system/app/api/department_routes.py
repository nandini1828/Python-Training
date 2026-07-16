"""FastAPI routes for department actions."""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

from app.repositories.employee_repository import EmployeeRepository

router = APIRouter()
repository = EmployeeRepository()


class DepartmentCreateRequest(BaseModel):
    """Payload for creating a department."""

    department_id: str
    name: str
    manager: str | None = None


@router.get("", status_code=status.HTTP_200_OK)
async def list_departments() -> list[dict[str, str | None]]:
    """List departments."""
    departments = repository.list_departments()
    return [department.to_dict() for department in departments]


@router.post("", status_code=status.HTTP_201_CREATED)
def create_department(request: DepartmentCreateRequest) -> dict[str, str]:
    """Create a department using JSON body."""
    departments = repository.list_departments()
    departments.append(request.model_dump())
    return {"message": "Department created successfully"}


@router.put("/{department_id}", status_code=status.HTTP_200_OK)
def update_department(department_id: str, request: DepartmentCreateRequest) -> dict[str, str]:
    """Update a department using JSON body."""
    departments = repository.list_departments()
    for department in departments:
        if department.department_id == department_id:
            department.name = request.name
            department.manager = request.manager
            return {"message": "Department updated successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")


@router.delete("/{department_id}", status_code=status.HTTP_200_OK)
def delete_department(department_id: str) -> dict[str, str]:
    """Delete a department by id."""
    departments = repository.list_departments()
    for index, department in enumerate(departments):
        if department.department_id == department_id:
            departments.pop(index)
            return {"message": "Department deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Department not found")
