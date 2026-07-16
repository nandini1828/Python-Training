from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class AttendanceBase(BaseModel):
    student_id: int
    course_id: int
    attendance_date: date
    status: str = Field(..., pattern="^(present|absent|late|excused)$")
    notes: Optional[str] = None


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseModel):
    student_id: Optional[int] = None
    course_id: Optional[int] = None
    attendance_date: Optional[date] = None
    status: Optional[str] = Field(None, pattern="^(present|absent|late|excused)$")
    notes: Optional[str] = None


class Attendance(AttendanceBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
