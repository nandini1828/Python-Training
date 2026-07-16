"""Report FastAPI router."""

import asyncio

from fastapi import APIRouter

from models.report import ReportCreate
from services.employee_service import get_employee_service
from services.report_service import ReportService

router = APIRouter()


@router.get("")
def list_reports() -> dict[str, object]:
    """Return a summary of current employee data."""
    employees = get_employee_service().list_employees()
    return ReportService.summary_report(employees)


@router.post("")
def create_report(payload: ReportCreate) -> dict[str, object]:
    """Create a simple report response from the provided payload."""
    employees = get_employee_service().list_employees()
    summary = ReportService.summary_report(employees)
    return {
        "title": payload.title,
        "notes": payload.notes,
        "employee_count": summary.get("employee_count", 0),
        "department_count": summary.get("department_count", 0),
        "average_salary": summary.get("average_salary"),
    }


@router.get("/async", include_in_schema=False)
async def list_reports_async() -> dict[str, object]:
    """Return a summary of current employee data asynchronously."""
    await asyncio.sleep(0.01)
    employees = get_employee_service().list_employees()
    return ReportService.summary_report(employees)
