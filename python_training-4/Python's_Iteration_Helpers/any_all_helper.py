def distinction(students):

    print("\nAny Distinction Student?")

    result = any(
        student.average() >= 90
        for student in students
    )

    print(result)


def all_pass(students):

    print("\nDid Everyone Pass?")

    result = all(
        student.maths >= 35 and student.science >= 35
        for student in students
    )

    print(result)