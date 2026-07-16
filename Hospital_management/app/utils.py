"""
utils.py

This module contains helper functions used throughout the project.

Topics Covered:
---------------
✔ Functions
✔ Type Annotations
✔ Introspection
✔ Generator
✔ Collections (Counter)
"""

from collections import Counter


def validate_age(age: int) -> bool:
    """
    Check whether the patient's age is valid.
    """

    return 0 < age <= 120


def get_next_id(data: dict | list) -> int:
    """
    Generate the next ID.

    This function works for both dictionaries
    and lists.
    """

    # If the collection is empty, start IDs from 1
    if not data:
        return 1

    # For dictionaries (patients, doctors)
    if isinstance(data, dict):
        return max(data.keys()) + 1

    # For lists (appointments)
    return len(data) + 1


def appointment_generator(appointments: list):
    """
    Generator function.

    Returns one appointment at a time.
    """

    for appointment in appointments:
        yield appointment


def inspect_object(obj):
    """
    Demonstrates Python introspection.
    """

    return {
        "type": type(obj).__name__,
        "memory_address": id(obj),
        "methods": dir(obj)
    }


def department_counter(doctors: dict):
    """
    Count the number of doctors in each department.

    Demonstrates the Counter class from collections.
    """

    specializations = [
        doctor.specialization
        for doctor in doctors.values()
    ]

    return Counter(specializations)