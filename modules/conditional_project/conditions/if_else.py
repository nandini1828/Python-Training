"""
Examples of if-elif-else.
"""


def calculate_grade(marks: int) -> str:
    """Return grade based on marks."""

    if marks >= 90:
        return "A"

    elif marks >= 75:
        return "B"

    elif marks >= 50:
        return "C"

    return "Fail"


def insurance_plan(amount: float) -> str:
    """Return insurance plan."""

    if amount >= 100000:
        return "Gold"

    elif amount >= 50000:
        return "Silver"

    return "Bronze"


def voting_eligibility(age: int) -> str:
    """Return voting eligibility."""

    if age >= 18:
        return "Eligible"

    return "Not Eligible"


def temperature_status(temp: int) -> str:
    """Categorize temperature."""

    if temp < 20:
        return "Cold"

    elif temp <= 35:
        return "Normal"

    return "Hot"