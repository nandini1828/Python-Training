"""
Student class demonstrating object attributes, __dict__, and __new__.
"""
from __future__ import annotations

from typing import List


class Student:
    """
    Represents a student with a name and numeric grades.

    Attributes:
        name: Student name.
        grades: List of numeric grades.
    """

    def __new__(cls, *args, **kwargs):
        """Allocate a new Student instance (demonstrates __new__)."""
        instance = super().__new__(cls)
        return instance

    def __init__(self, name: str, grades: List[float] | None = None) -> None:
        self.name = name
        self.grades = list(grades or [])

    def average_grade(self) -> float:
        """
        Compute the arithmetic mean of the student's grades.

        Returns:
            The average as a float, or 0.0 when no grades exist.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
