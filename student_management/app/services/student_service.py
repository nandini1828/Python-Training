from app.data.database import students
from app.models.address import Address
from app.models.student import Student
from app.utils.formatter import student_to_dict
from app.utils.helper import next_id
from app.utils.validator import is_non_empty_text, is_valid_age


async def get_all_students() -> list[dict[str, object]]:
    return [student_to_dict(student) for student in students]


async def get_student_by_id(student_id: int) -> dict[str, object] | None:
    student = await _find_student(student_id)
    if student is None:
        return None
    return student_to_dict(student)


async def add_student(student: Student) -> dict[str, object]:
    if not is_non_empty_text(student.name):
        raise ValueError("Student name is required")
    if not is_valid_age(student.age):
        raise ValueError("Student age must be between 1 and 119")

    student.student_id = next_id(students, "student_id")
    students.append(student)
    return student_to_dict(student)


async def update_student(
    student_id: int,
    name: str | None = None,
    age: int | None = None,
    city: str | None = None,
) -> dict[str, object] | None:
    student = await _find_student(student_id)
    if student is None:
        return None

    if name is not None:
        if not is_non_empty_text(name):
            raise ValueError("Student name cannot be empty")
        student.name = name

    if age is not None:
        if not is_valid_age(age):
            raise ValueError("Student age must be between 1 and 119")
        student.age = age

    if city is not None:
        if not is_non_empty_text(city):
            raise ValueError("City cannot be empty")
        student.address = Address(city=city)

    return student_to_dict(student)


async def delete_student(student_id: int) -> bool:
    for index, student in enumerate(students):
        if student.student_id == student_id:
            del students[index]
            return True
    return False


async def _find_student(student_id: int) -> Student | None:
    for student in students:
        if student.student_id == student_id:
            return student
    return None
