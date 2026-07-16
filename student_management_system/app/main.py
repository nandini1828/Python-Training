from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.attendance_router import router as attendance_router
from app.routers.course_router import router as course_router
from app.routers.education_router import router as education_router
from app.routers.student_router import router as student_router
from app.services.attendance_service import AttendanceService
from app.services.course_service import CourseService
from app.services.student_service import StudentService

app = FastAPI(
    title="Student Management System",
    version="1.0.0",
    description="A complete FastAPI application for managing students, courses, and attendance.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(student_router, prefix="/students", tags=["Students"])
app.include_router(course_router, prefix="/courses", tags=["Courses"])
app.include_router(attendance_router, prefix="/attendance", tags=["Attendance"])
app.include_router(education_router)


@app.get("/", tags=["Health"])
def health_check():
    return {
        "success": True,
        "message": "Student Management System is running",
        "docs": "/docs",
    }


@app.on_event("startup")
def seed_demo_data():
    StudentService().seed_demo_data()
    CourseService().seed_demo_data()
    AttendanceService().seed_demo_data()
