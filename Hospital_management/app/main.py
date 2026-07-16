"""
main.py

Entry point of the Hospital Management System.
"""

from fastapi import FastAPI

from app.routers import appointment_router, doctor_router, patient_router

# Create FastAPI application
app = FastAPI(
    title="Hospital Management System",
    version="1.0.0",
)

# Register routers
app.include_router(patient_router.router)
app.include_router(doctor_router.router)
app.include_router(appointment_router.router)


@app.get("/")
def home():
    """Home endpoint."""
    return {
        "message": "Welcome to Hospital Management System",
        "framework": "FastAPI",
    }
