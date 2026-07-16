from fastapi import FastAPI

from app.api import course_api, student_api

app = FastAPI(
    title="Student Management Learning API",
    description="A fresher-level FastAPI project for Python data types and OOP basics.",
    version="1.0.0",
)


app.include_router(student_api.router)
app.include_router(course_api.router)


@app.get("/")
async def home() -> dict[str, str]:
    return {
        "message": "Welcome to the Student Management Learning API",
        "docs": "Open /docs to try the endpoints",
    }
