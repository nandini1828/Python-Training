"""
utils.py

Reusable utility functions demonstrating the ternary operator.
"""


def adult_status(age: int) -> str:
    return "Adult" if age >= 18 else "Minor"


def even_or_odd(number: int) -> str:
    return "Even" if number % 2 == 0 else "Odd"


def larger(a: float, b: float):
    return a if a > b else b


def smaller(a: float, b: float):
    return a if a < b else b


def pass_fail(marks: int) -> str:
    return "Pass" if marks >= 40 else "Fail"


def positive_negative(number: float) -> str:
    return "Positive" if number > 0 else "Negative"


def login_message(authenticated: bool) -> str:
    return "Welcome" if authenticated else "Access Denied"


def weather_message(raining: bool) -> str:
    return "Stay Inside" if raining else "Go Outside"


def scholarship_status(marks: int) -> str:
    return "Eligible" if marks >= 90 else "Not Eligible"


def employee_bonus(rating: int) -> int:
    return 50000 if rating == 5 else 10000