"""Department model."""

from dataclasses import dataclass

from pydantic import BaseModel, Field


@dataclass
class Department:
    """Basic department representation."""

    department_id: int
    name: str
    location: str = "HQ"


class DepartmentCreate(BaseModel):
    """Payload for creating a department."""

    department_id: int = Field(..., gt=0)
    name: str = Field(..., min_length=1)
    location: str = Field(default="HQ")
