"""
Exercise Solutions - Section 5
"""

from .oop_memory import Student


def create_student_without_init():
    """
    Exercise 5.1
    Create object without calling __init__
    and invoke method using class syntax.
    """

    student = Student.__new__(Student)

    student.__dict__["name"] = "Vyshu"

    student.__dict__["grades"] = [
        90,
        95,
        85
    ]

    average = Student.average_grade(student)

    return {
        "student_data": student.__dict__,
        "average_grade": average
    }


def deconstruct_object(obj):
    """
    Exercise 5.2
    Recursively converts custom objects
    into dictionaries.
    """

    primitive_types = (
        str,
        int,
        float,
        bool,
        type(None)
    )

    if isinstance(obj, primitive_types):
        return obj

    if isinstance(obj, list):
        return [
            deconstruct_object(item)
            for item in obj
        ]

    if isinstance(obj, tuple):
        return [
            deconstruct_object(item)
            for item in obj
        ]

    if isinstance(obj, dict):

        result = {}

        for key, value in obj.items():
            result[key] = deconstruct_object(value)

        return result

    if hasattr(obj, "__dict__"):

        result = {}

        for key, value in obj.__dict__.items():
            result[key] = deconstruct_object(value)

        return result

    return obj