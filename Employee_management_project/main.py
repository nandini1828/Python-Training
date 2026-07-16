"""Entry point for the employee management project."""

from fastapi import FastAPI

from api.department_api import router as department_router
from api.employee_api import router as employee_router
from api.report_api import router as report_router
from services.employee_service import EmployeeService

app = FastAPI(
    title="Employee Management API",
    description="A FastAPI app for managing employees, departments, and reports.",
    version="1.0.0",
)

app.include_router(employee_router, prefix="/employees", tags=["employees"])
app.include_router(department_router, prefix="/departments", tags=["departments"])
app.include_router(report_router, prefix="/reports", tags=["reports"])


@app.get("/", tags=["root"])
def root() -> dict[str, str]:
    """Return basic API information."""
    return {"message": "Employee Management API"}


@app.get("/health", tags=["health"])
def health_check() -> dict[str, str]:
    """Health endpoint used by deployment and tests."""
    return {"status": "ok"}


def main() -> None:
    """Run a simple startup example."""
    service = EmployeeService()
    print("Employee Management Project is ready.")
    print(f"Loaded employees: {len(service.list_employees())}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
