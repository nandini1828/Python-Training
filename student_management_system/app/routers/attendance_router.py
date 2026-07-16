from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, status

from app.models.attendance_model import Attendance, AttendanceCreate, AttendanceUpdate
from app.services.attendance_service import AttendanceService
from app.utils.response import error_response, success_response

router = APIRouter()
service = AttendanceService()


@router.get("", response_model=List[Attendance])
def list_attendance(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    student_id: Optional[int] = None,
    course_id: Optional[int] = None,
):
    return service.list_attendance(skip=skip, limit=limit, student_id=student_id, course_id=course_id)


@router.get("/{attendance_id}", response_model=Attendance)
def get_attendance(attendance_id: int):
    record = service.get_attendance(attendance_id)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_response("Attendance record not found"))
    return record


@router.post("", response_model=Attendance, status_code=status.HTTP_201_CREATED)
def create_attendance(attendance_data: AttendanceCreate):
    return service.create_attendance(attendance_data)


@router.put("/{attendance_id}", response_model=Attendance)
def update_attendance(attendance_id: int, attendance_data: AttendanceUpdate):
    record = service.update_attendance(attendance_id, attendance_data)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_response("Attendance record not found"))
    return record


@router.delete("/{attendance_id}", status_code=status.HTTP_200_OK)
def delete_attendance(attendance_id: int):
    deleted = service.delete_attendance(attendance_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_response("Attendance record not found"))
    return success_response("Attendance record deleted successfully")


@router.get("/summary")
def attendance_summary():
    return success_response("Attendance summary fetched", data=service.get_summary())
