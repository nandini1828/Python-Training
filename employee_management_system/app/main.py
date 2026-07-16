"""FastAPI entrypoint for the employee management system."""

from fastapi import FastAPI

from app.api.department_routes import router as department_router
from app.api.employee_routes import router as employee_router
from app.api.health import router as health_router

app = FastAPI(title="Employee Management System", version="1.0.0")

app.include_router(health_router, prefix="", tags=["health"])
app.include_router(employee_router, prefix="/employees", tags=["employees"])
app.include_router(department_router, prefix="/departments", tags=["departments"])


@app.get("/")
def read_root() -> dict[str, str]:
    """Return a simple welcome message."""
    return {"message": "Employee Management System is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)