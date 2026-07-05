"""
Examples of logical operators:
and, or, not
"""


def loan_eligibility(age: int, salary: int) -> bool:
    """Check loan eligibility."""
    return age >= 21 and salary >= 30000


def login(username: str, password: str) -> bool:
    """Validate login credentials."""
    return username == "admin" and password == "python123"


def weekend(day: str) -> bool:
    """Check whether it is a weekend."""
    return day.lower() == "saturday" or day.lower() == "sunday"


def account_active(active: bool) -> str:
    """Check account status."""
    if not active:
        return "Account Disabled"
    return "Account Active"


def student_passed(mark: int, attendance: int) -> bool:
    """Student must satisfy both conditions."""
    return mark >= 40 and attendance >= 75