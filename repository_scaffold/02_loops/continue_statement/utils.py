"""
utils.py

Reusable utility functions demonstrating continue statement usage.
"""


def skip_even(numbers: list) -> list:
    """
    Returns only odd numbers (skips even numbers).
    """
    result = []

    for num in numbers:
        if num % 2 == 0:
            continue
        result.append(num)

    return result


def skip_negatives(values: list) -> list:
    """
    Returns only non-negative numbers.
    """
    result = []

    for val in values:
        if val < 0:
            continue
        result.append(val)

    return result


def skip_empty(strings: list) -> list:
    """
    Returns list without empty strings.
    """
    result = []

    for s in strings:
        if s == "":
            continue
        result.append(s)

    return result


def skip_multiples_of_three(numbers: list) -> list:
    """
    Returns numbers excluding multiples of 3.
    """
    result = []

    for num in numbers:
        if num % 3 == 0:
            continue
        result.append(num)

    return result


def valid_emails(emails: list) -> list:
    """
    Returns only valid emails (basic validation).
    """
    result = []

    for email in emails:
        if "@" not in email:
            continue
        result.append(email)

    return result


def safe_division(numbers: list) -> list:
    """
    Divides 10 by each number, skipping zero.
    """
    result = []

    for num in numbers:
        if num == 0:
            continue
        result.append(10 / num)

    return result


def valid_students(students: list) -> list:
    """
    Returns students with valid marks (>= 0).
    """
    result = []

    for student in students:
        if student.get("marks", -1) < 0:
            continue
        result.append(student)

    return result