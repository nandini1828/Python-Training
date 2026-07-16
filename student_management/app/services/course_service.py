from app.data.database import courses, students
from app.models.course import Course
from app.services.student_service import _find_student
from app.utils.formatter import course_to_dict, student_to_dict
from app.utils.helper import next_id
from app.utils.validator import is_non_empty_text, is_valid_duration


async def get_all_courses() -> list[dict[str, object]]:
    return [course_to_dict(course) for course in courses]


async def get_course_by_id(course_id: int) -> dict[str, object] | None:
    course = await _find_course(course_id)
    if course is None:
        return None
    return course_to_dict(course)


async def add_course(course: Course) -> dict[str, object]:
    if not is_non_empty_text(course.name):
        raise ValueError("Course name is required")
    if not is_valid_duration(course.duration_weeks):
        raise ValueError("Course duration must be between 1 and 52 weeks")

    course.course_id = next_id(courses, "course_id")
    courses.append(course)
    return course_to_dict(course)


async def update_course(
    course_id: int,
    name: str | None = None,
    duration_weeks: int | None = None,
) -> dict[str, object] | None:
    course = await _find_course(course_id)
    if course is None:
        return None

    if name is not None:
        if not is_non_empty_text(name):
            raise ValueError("Course name cannot be empty")
        course.name = name

    if duration_weeks is not None:
        if not is_valid_duration(duration_weeks):
            raise ValueError("Course duration must be between 1 and 52 weeks")
        course.duration_weeks = duration_weeks

    return course_to_dict(course)


async def delete_course(course_id: int) -> bool:
    course = await _find_course(course_id)
    if course is None:
        return False

    for student in students:
        if course.name in student.courses:
            student.courses.remove(course.name)

    courses.remove(course)
    return True


async def enroll_course(course_id: int, student_id: int) -> dict[str, object] | None:
    student = await _find_student(student_id)
    course = await _find_course(course_id)

    if student is None or course is None:
        return None

    course.enroll(student.student_id)
    student.add_course(course.name)
    return {
        "course": course_to_dict(course),
        "student": student_to_dict(student),
    }


async def _find_course(course_id: int) -> Course | None:
    for course in courses:
        if course.course_id == course_id:
            return course
    return None
