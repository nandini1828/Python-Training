from section5.oop_memory import Student


def create_student_without_init():

    student = Student.__new__(Student)

    student.__dict__["name"] = "Vyshu"
    student.__dict__["grades"] = [90, 95, 85]

    return Student.average_grade(student)