"""
reversed() and sorted()
"""


class Student:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks


def demo():

    numbers = [5, 1, 7, 2]

    print(list(reversed(numbers)))

    students = [
        Student("Alice", 90),
        Student("Bob", 70),
        Student("Charlie", 80),
    ]

    sorted_students = sorted(
        students,
        key=lambda student: student.marks,
    )

    for student in sorted_students:
        print(student.name, student.marks)