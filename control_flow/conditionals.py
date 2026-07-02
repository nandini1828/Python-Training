"""
Conditional statement examples for the control_flow module.

This module demonstrates how to use Python's conditional statements
to implement common decision-making logic.

Topics covered:
- if
- if-else
- if-elif-else
- Nested conditions
- Guard clauses
- Real-world decision making

Author: Python Training
"""

from __future__ import annotations

from .utils import validate_age


def is_adult(age: int) -> bool:
    """
    Determine whether a person is an adult.

    Args:
        age:
            Person's age.

    Returns:
        True if the person is 18 years or older.

    Raises:
        ValueError:
            If the age is invalid.
    """
    if not validate_age(age):
        raise ValueError("Age must be between 0 and 150.")

    return age >= 18


def check_number(number: int) -> str:
    """
    Classify a number.

    Args:
        number:
            Integer value.

    Returns:
        Classification of the number.
    """
    if number > 0:
        return "Positive"

    if number < 0:
        return "Negative"

    return "Zero"


def calculate_grade(score: float) -> str:
    """
    Calculate a student's grade.

    Args:
        score:
            Marks between 0 and 100.

    Returns:
        Grade string.

    Raises:
        ValueError:
            If score is outside the valid range.
    """
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 90:
        return "A"

    if score >= 80:
        return "B"

    if score >= 70:
        return "C"

    if score >= 60:
        return "D"

    return "F"


def determine_discount(
    amount: float,
    is_premium_customer: bool,
) -> float:
    """
    Calculate customer discount.

    Args:
        amount:
            Purchase amount.

        is_premium_customer:
            Premium membership status.

    Returns:
        Discount percentage.
    """
    if amount <= 0:
        return 0.0

    if is_premium_customer:
        if amount >= 10000:
            return 25.0

        if amount >= 5000:
            return 20.0

        return 10.0

    if amount >= 10000:
        return 15.0

    if amount >= 5000:
        return 10.0

    return 5.0


def determine_temperature_status(
    temperature: float,
) -> str:
    """
    Classify weather temperature.

    Args:
        temperature:
            Temperature in Celsius.

    Returns:
        Temperature classification.
    """
    if temperature < 0:
        return "Freezing"

    if temperature < 15:
        return "Cold"

    if temperature < 25:
        return "Pleasant"

    if temperature < 35:
        return "Warm"

    return "Hot"


def validate_username(username: str) -> bool:
    """
    Validate a username.

    Rules:
        - At least 5 characters
        - No spaces

    Args:
        username:
            Username to validate.

    Returns:
        True if valid.
    """
    if len(username) < 5:
        return False

    if " " in username:
        return False

    return True


def can_vote(age: int, citizenship: bool) -> bool:
    """
    Determine voting eligibility.

    Args:
        age:
            Person's age.

        citizenship:
            Citizenship status.

    Returns:
        True if eligible.
    """
    if age < 18:
        return False

    if not citizenship:
        return False

    return True


def can_access_admin_panel(
    is_logged_in: bool,
    is_admin: bool,
) -> bool:
    """
    Determine administrative access.

    Args:
        is_logged_in:
            User authentication status.

        is_admin:
            Administrative privilege.

    Returns:
        True if access is granted.
    """
    if not is_logged_in:
        return False

    if not is_admin:
        return False

    return True


def loan_approval(
    salary: float,
    credit_score: int,
    has_existing_loan: bool,
) -> str:
    """
    Determine loan approval status.

    Args:
        salary:
            Applicant salary.

        credit_score:
            Credit score.

        has_existing_loan:
            Existing loan status.

    Returns:
        Loan decision.
    """
    if salary < 25000:
        return "Rejected"

    if credit_score < 650:
        return "Rejected"

    if has_existing_loan:
        return "Manual Review"

    return "Approved"


def shipping_charge(order_amount: float) -> float:
    """
    Calculate shipping charge.

    Args:
        order_amount:
            Total order amount.

    Returns:
        Shipping cost.
    """
    if order_amount >= 1000:
        return 0.0

    return 99.0


def employee_bonus(
    years_of_service: int,
    performance_rating: int,
) -> int:
    """
    Calculate employee bonus percentage.

    Args:
        years_of_service:
            Number of years worked.

        performance_rating:
            Performance rating (1-5).

    Returns:
        Bonus percentage.
    """
    if years_of_service >= 10:
        if performance_rating >= 4:
            return 30
        return 20

    if years_of_service >= 5:
        if performance_rating >= 4:
            return 20
        return 10

    if performance_rating >= 4:
        return 10

    return 5


def classify_triangle(
    side1: float,
    side2: float,
    side3: float,
) -> str:
    """
    Classify a triangle based on side lengths.

    Args:
        side1:
            First side.

        side2:
            Second side.

        side3:
            Third side.

    Returns:
        Triangle type.
    """
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return "Invalid"

    if (
        side1 + side2 <= side3
        or side1 + side3 <= side2
        or side2 + side3 <= side1
    ):
        return "Invalid"

    if side1 == side2 == side3:
        return "Equilateral"

    if side1 == side2 or side2 == side3 or side1 == side3:
        return "Isosceles"

    return "Scalene"


__all__ = [
    "is_adult",
    "check_number",
    "calculate_grade",
    "determine_discount",
    "determine_temperature_status",
    "validate_username",
    "can_vote",
    "can_access_admin_panel",
    "loan_approval",
    "shipping_charge",
    "employee_bonus",
    "classify_triangle",
]