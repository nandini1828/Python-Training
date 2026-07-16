from typing import List, Optional

from app.models.course_model import Course, CourseCreate, CourseUpdate
from app.utils.file_handler import FileStorage


class CourseService:
    def __init__(self):
        self.storage = FileStorage("courses.json")

    def list_courses(self, skip: int = 0, limit: int = 100, is_active: Optional[bool] = None) -> List[Course]:
        courses = self.storage.read()
        if is_active is not None:
            courses = [course for course in courses if course.get("is_active") == is_active]
        return [Course.model_validate(course) for course in courses[skip: skip + limit]]

    def get_course(self, course_id: int) -> Optional[Course]:
        for course in self.storage.read():
            if course.get("id") == course_id:
                return Course.model_validate(course)
        return None

    def create_course(self, course_data: CourseCreate) -> Course:
        courses = self.storage.read()
        course_id = max((course.get("id", 0) for course in courses), default=0) + 1
        payload = course_data.model_dump()
        payload["id"] = course_id
        courses.append(payload)
        self.storage.write(courses)
        return Course.model_validate(payload)

    def update_course(self, course_id: int, course_data: CourseUpdate) -> Optional[Course]:
        courses = self.storage.read()
        for index, course in enumerate(courses):
            if course.get("id") == course_id:
                updated = {**course, **course_data.model_dump(exclude_unset=True)}
                courses[index] = updated
                self.storage.write(courses)
                return Course.model_validate(updated)
        return None

    def delete_course(self, course_id: int) -> bool:
        courses = self.storage.read()
        remaining = [course for course in courses if course.get("id") != course_id]
        if len(remaining) == len(courses):
            return False
        self.storage.write(remaining)
        return True

    def seed_demo_data(self) -> None:
        if self.storage.read():
            return
        demo_courses = [
            {
                "id": 1,
                "title": "Mathematics",
                "code": "MATH101",
                "instructor": "Dr. Rivera",
                "credits": 3,
                "max_students": 30,
                "is_active": True,
            },
            {
                "id": 2,
                "title": "Science",
                "code": "SCI202",
                "instructor": "Prof. Khan",
                "credits": 4,
                "max_students": 25,
                "is_active": True,
            },
        ]
        self.storage.write(demo_courses)
