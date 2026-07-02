"""
Demonstrates if-elif-else statements.
"""


def grade(score: int) -> str:
    """Return grade based on score."""

    if score >= 90:
        return "A"

    elif score >= 80:
        return "B"

    elif score >= 70:
        return "C"

    elif score >= 60:
        return "D"

    return "Fail"


def eligibility(age: int):
    if age >= 18:
        print("Eligible to Vote")
    else:
        print("Not Eligible")


def demo():
    print(grade(95))
    print(grade(74))
    eligibility(20)