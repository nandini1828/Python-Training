from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class StudentBase(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=100)
    last_name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(..., min_length=7, max_length=20)
    date_of_birth: date
    grade_level: str = Field(..., min_length=1, max_length=20)
    is_active: bool = True

    @field_validator("first_name", "last_name")
    @classmethod
    def validate_name(cls, value: str) -> str:
        return value.strip().title()


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=2, max_length=100)
    last_name: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = Field(None, min_length=7, max_length=20)
    date_of_birth: Optional[date] = None
    grade_level: Optional[str] = Field(None, min_length=1, max_length=20)
    is_active: Optional[bool] = None


class Student(StudentBase):
    id: int

    class Config:
        from_attributes = True
