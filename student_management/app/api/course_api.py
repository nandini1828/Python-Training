from fastapi import APIRouter, HTTPException

from app.models.course import Course, CourseEnrollment, CourseUpdate
from app.services import course_service

router = APIRouter(prefix="/courses", tags=["courses"])


@router.get("/")
async def list_courses() -> list[dict[str, object]]:
    """Topic: list data type, dictionaries, JSON response, async and await."""

    return await course_service.get_all_courses()


@router.get("/{course_id}")
async def get_course(course_id: int) -> dict[str, object]:
    """Topic: int path parameter, type hints, None checking, and HTTP errors."""

    course = await course_service.get_course_by_id(course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.post("/")
async def create_course(course_data: Course) -> dict[str, object]:
    """Topic: Pydantic validates course name and duration from JSON."""

    course = Course(
        name=course_data.name,
        duration_weeks=course_data.duration_weeks,
    )
    try:
        return await course_service.add_course(course)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@router.put("/{course_id}")
async def update_course(
    course_id: int,
    course_data: CourseUpdate,
) -> dict[str, object]:
    """Topic: Optional Pydantic fields allow safe partial course updates."""

    try:
        course = await course_service.update_course(
            course_id=course_id,
            name=course_data.name,
            duration_weeks=course_data.duration_weeks,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.delete("/{course_id}")
async def delete_course(course_id: int) -> dict[str, str]:
    """Topic: boolean result checking and dictionary response."""

    deleted = await course_service.delete_course(course_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}


@router.post("/enroll")
async def enroll_course(enroll_data: CourseEnrollment) -> dict[str, object]:
    """Topic: Pydantic checks integer IDs before course enrollment."""

    result = await course_service.enroll_course(
        enroll_data.course_id,
        enroll_data.student_id,
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Student or course not found")
    return result
