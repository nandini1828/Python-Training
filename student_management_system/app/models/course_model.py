from typing import Optional

from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=150)
    code: str = Field(..., min_length=2, max_length=20)
    instructor: str = Field(..., min_length=2, max_length=100)
    credits: int = Field(..., ge=1, le=10)
    max_students: int = Field(..., ge=1, le=500)
    is_active: bool = True


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=150)
    code: Optional[str] = Field(None, min_length=2, max_length=20)
    instructor: Optional[str] = Field(None, min_length=2, max_length=100)
    credits: Optional[int] = Field(None, ge=1, le=10)
    max_students: Optional[int] = Field(None, ge=1, le=500)
    is_active: Optional[bool] = None


class Course(CourseBase):
    id: int

    class Config:
        from_attributes = True
