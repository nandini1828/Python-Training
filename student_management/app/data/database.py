from app.models.address import Address
from app.models.course import Course
from app.models.student import Student

students: list[Student] = [
    Student(
        student_id=1,
        name="Asha",
        age=20,
        address=Address(city="Pune", state="Maharashtra"),
        courses=["Python Basics"],
    ),
    Student(
        student_id=2,
        name="Rahul",
        age=22,
        address=Address(city="Bengaluru", state="Karnataka"),
    ),
]

courses: list[Course] = [
    Course(course_id=1, name="Python Basics", duration_weeks=4),
    Course(course_id=2, name="FastAPI Basics", duration_weeks=3),
]
