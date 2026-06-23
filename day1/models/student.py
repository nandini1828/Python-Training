"""
Student Model
"""
from typing import List
class Student:
    """
    Represents a student object.
    """
    def __init__(
        self,
        name: str,
        marks: int,
        grade: str
    ) -> None:
        self.name = name
        self.marks = marks
        self.grade = grade

    def display_information(self) -> None:
        print(f"Name  : {self.name}")
        print(f"Marks : {self.marks}")
        print(f"Grade : {self.grade}")

    def average_grade(
        self,
        grades: List[int]
    ) -> float:
        return sum(grades) / len(grades)