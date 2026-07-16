from datetime import date
from typing import Dict, List, Optional

from app.models.student_model import Student, StudentCreate, StudentUpdate
from app.utils.file_handler import FileStorage


class StudentService:
    def __init__(self):
        self.storage = FileStorage("students.json")

    def list_students(self, skip: int = 0, limit: int = 100, is_active: Optional[bool] = None) -> List[Student]:
        students = self.storage.read()
        if is_active is not None:
            students = [student for student in students if student.get("is_active") == is_active]
        return [Student.model_validate(student) for student in students[skip: skip + limit]]

    def get_student(self, student_id: int) -> Optional[Student]:
        for student in self.storage.read():
            if student.get("id") == student_id:
                return Student.model_validate(student)
        return None

    def create_student(self, student_data: StudentCreate) -> Student:
        students = self.storage.read()
        student_id = max((student.get("id", 0) for student in students), default=0) + 1
        payload = student_data.model_dump()
        payload["id"] = student_id
        students.append(payload)
        self.storage.write(students)
        return Student.model_validate(payload)

    def update_student(self, student_id: int, student_data: StudentUpdate) -> Optional[Student]:
        students = self.storage.read()
        for index, student in enumerate(students):
            if student.get("id") == student_id:
                updated = {**student, **student_data.model_dump(exclude_unset=True)}
                students[index] = updated
                self.storage.write(students)
                return Student.model_validate(updated)
        return None

    def delete_student(self, student_id: int) -> bool:
        students = self.storage.read()
        remaining = [student for student in students if student.get("id") != student_id]
        if len(remaining) == len(students):
            return False
        self.storage.write(remaining)
        return True

    def seed_demo_data(self) -> None:
        if self.storage.read():
            return
        demo_students = [
            {
                "id": 1,
                "first_name": "Alice",
                "last_name": "Johnson",
                "email": "alice@example.com",
                "phone": "555-0101",
                "date_of_birth": date(2010, 5, 12),
                "grade_level": "10",
                "is_active": True,
            },
            {
                "id": 2,
                "first_name": "Bob",
                "last_name": "Smith",
                "email": "bob@example.com",
                "phone": "555-0102",
                "date_of_birth": date(2009, 8, 1),
                "grade_level": "11",
                "is_active": True,
            },
        ]
        self.storage.write(demo_students)
