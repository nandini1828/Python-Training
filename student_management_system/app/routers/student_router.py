from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, status

from app.models.student_model import Student, StudentCreate, StudentUpdate
from app.services.student_service import StudentService
from app.utils.response import error_response, success_response

router = APIRouter()
service = StudentService()


@router.get("", response_model=List[Student])
def list_students(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    is_active: Optional[bool] = None,
):
    return service.list_students(skip=skip, limit=limit, is_active=is_active)


@router.get("/{student_id}", response_model=Student)
def get_student(student_id: int):
    student = service.get_student(student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_response("Student not found"))
    return student


@router.post("", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student_data: StudentCreate):
    return service.create_student(student_data)


@router.put("/{student_id}", response_model=Student)
def update_student(student_id: int, student_data: StudentUpdate):
    student = service.update_student(student_id, student_data)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_response("Student not found"))
    return student


@router.delete("/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int):
    deleted = service.delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_response("Student not found"))
    return success_response("Student deleted successfully")
