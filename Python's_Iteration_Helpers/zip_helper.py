from itertools import zip_longest

def compare_subject_marks(students):

    print("\nMaths and Science Marks")

    maths = [student.maths for student in students]
    science = [student.science for student in students]

    for maths_mark, science_mark in zip(maths, science):
        print(f"Maths: {maths_mark}, Science: {science_mark}")


def compare_extra_subject():

    print("\nZip Longest Example")

    students = ["John", "Alice"]
    projects = ["AI Project", "ML Project", "Cloud Project"]

    for student, project in zip_longest(
        students,
        projects,
        fillvalue="Not Assigned"
    ):
        print(student, project)