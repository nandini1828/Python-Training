from fastapi import APIRouter, HTTPException

from app.models.address import Address
from app.models.student import Student, StudentInput, StudentUpdate
from app.services import student_service

router = APIRouter(prefix="/students", tags=["students"])


@router.get("/")
async def list_students() -> list[dict[str, object]]:
    """Topic: list data type, dictionaries, JSON response, async and await."""

    return await student_service.get_all_students()


@router.get("/{student_id}")
async def get_student(student_id: int) -> dict[str, object]:
    """Topic: int path parameter, type hints, None checking, and HTTP errors."""

    student = await student_service.get_student_by_id(student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.post("/")
async def create_student(student_data: StudentInput) -> dict[str, object]:
    """Topic: Pydantic validates JSON body data before creating an object."""

    address = Address(city=student_data.city)
    student = Student(
        name=student_data.name,
        age=student_data.age,
        address=address,
    )
    try:
        return await student_service.add_student(student)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@router.put("/{student_id}")
async def update_student(
    student_id: int,
    student_data: StudentUpdate,
) -> dict[str, object]:
    """Topic: Optional Pydantic fields allow safe partial updates."""

    try:
        student = await student_service.update_student(
            student_id=student_id,
            name=student_data.name,
            age=student_data.age,
            city=student_data.city,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error

    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@router.delete("/{student_id}")
async def delete_student(student_id: int) -> dict[str, str]:
    """Topic: boolean result checking and dictionary response."""

    deleted = await student_service.delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
