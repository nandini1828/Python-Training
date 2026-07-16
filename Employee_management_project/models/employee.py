"""Employee model."""

from dataclasses import dataclass

from pydantic import BaseModel, Field


@dataclass
class Employee:
    """Simple employee representation."""

    employee_id: int
    name: str
    department: str
    salary: float
    role: str = "Employee"


class EmployeeCreate(BaseModel):
    """Payload for creating an employee."""

    employee_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    department: str = Field(..., min_length=1)
    salary: float = Field(..., ge=0)
    role: str = Field(default="Employee", min_length=1)


class EmployeeUpdate(BaseModel):
    """Payload for updating an employee."""

    name: str | None = None
    department: str | None = None
    salary: float | None = Field(default=None, ge=0)
    role: str | None = None
