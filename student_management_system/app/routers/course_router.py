from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, status

from app.models.course_model import Course, CourseCreate, CourseUpdate
from app.services.course_service import CourseService
from app.utils.response import error_response, success_response

router = APIRouter()
service = CourseService()


@router.get("", response_model=List[Course])
def list_courses(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=200),
    is_active: Optional[bool] = None,
):
    return service.list_courses(skip=skip, limit=limit, is_active=is_active)


@router.get("/{course_id}", response_model=Course)
def get_course(course_id: int):
    course = service.get_course(course_id)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_response("Course not found"))
    return course


@router.post("", response_model=Course, status_code=status.HTTP_201_CREATED)
def create_course(course_data: CourseCreate):
    return service.create_course(course_data)


@router.put("/{course_id}", response_model=Course)
def update_course(course_id: int, course_data: CourseUpdate):
    course = service.update_course(course_id, course_data)
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_response("Course not found"))
    return course


@router.delete("/{course_id}", status_code=status.HTTP_200_OK)
def delete_course(course_id: int):
    deleted = service.delete_course(course_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=error_response("Course not found"))
    return success_response("Course deleted successfully")
