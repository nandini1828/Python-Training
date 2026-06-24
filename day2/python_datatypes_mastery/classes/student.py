"""
Word counting utility
"""


class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = list(grades)

    def average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)