"""
==================================================
Module: Dunder Methods
Topic: Magic / Dunder Methods
Author: Nandini

Description:
Demonstrates common dunder methods.
==================================================
"""


class Student:
    """
    Student Class
    """

    def __init__(self, name, age):
        """
        Constructor
        """

        self.name = name
        self.age = age

    def __str__(self):
        """
        Human-readable representation.
        """

        return f"Student(Name={self.name}, Age={self.age})"

    def __repr__(self):
        """
        Developer representation.
        """

        return f"Student('{self.name}', {self.age})"

    def __len__(self):
        """
        Length of student's name.
        """

        return len(self.name)