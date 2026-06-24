from classes import Student


def test_average_grade():

    student = Student(
        "Bhavya",
        [90, 80, 100]
    )

    assert student.average_grade() == 90.0