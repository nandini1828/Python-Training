"""Department FastAPI router."""

import asyncio
import json
from pathlib import Path

from fastapi import APIRouter

from config.settings import DATA_DIR
from models.department import Department, DepartmentCreate

router = APIRouter()


@router.get("", response_model=list[Department])
def list_departments() -> list[Department]:
    """List all departments."""
    data_file = Path(DATA_DIR) / "departments.json"
    if not data_file.exists():
        return []
    payload = json.loads(data_file.read_text(encoding="utf-8"))
    return [Department(**item) for item in payload]


@router.get("/async", response_model=list[Department], include_in_schema=False)
async def list_departments_async() -> list[Department]:
    """List all departments asynchronously."""
    await asyncio.sleep(0.01)
    data_file = Path(DATA_DIR) / "departments.json"
    if not data_file.exists():
        return []
    payload = json.loads(data_file.read_text(encoding="utf-8"))
    return [Department(**item) for item in payload]


@router.post("", response_model=Department)
def create_department(department: DepartmentCreate) -> Department:
    """Create a department."""
    return Department(department.department_id, department.name, department.location)
