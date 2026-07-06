"""
Unit tests for control_flow.conditionals.

Run:

    pytest tests/test_conditionals.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from control_flow.conditionals import (
    calculate_grade,
    check_number,
    classify_triangle,
    determine_discount,
    determine_temperature_status,
    employee_bonus,
    is_adult,
    loan_approval,
    shipping_charge,
    validate_username,
    can_vote,
)


# ============================================================================
# is_adult()
# ============================================================================


def test_is_adult_returns_true_for_adult() -> None:
    """Adult age should return True."""
    assert is_adult(18) is True
    assert is_adult(25) is True


def test_is_adult_returns_false_for_minor() -> None:
    """Minor age should return False."""
    assert is_adult(10) is False
    assert is_adult(17) is False


@pytest.mark.parametrize(
    "age",
    [-1, 151],
)
def test_is_adult_invalid_age(age: int) -> None:
    """Invalid ages should raise ValueError."""
    with pytest.raises(ValueError):
        is_adult(age)


# ============================================================================
# check_number()
# ============================================================================


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (10, "Positive"),
        (-5, "Negative"),
        (0, "Zero"),
    ],
)
def test_check_number(number: int, expected: str) -> None:
    """Verify number classification."""
    assert check_number(number) == expected


# ============================================================================
# calculate_grade()
# ============================================================================


@pytest.mark.parametrize(
    ("score", "grade"),
    [
        (95, "A"),
        (84, "B"),
        (72, "C"),
        (65, "D"),
        (20, "F"),
    ],
)
def test_calculate_grade(score: float, grade: str) -> None:
    """Verify grade calculation."""
    assert calculate_grade(score) == grade


@pytest.mark.parametrize(
    "score",
    [-5, 101],
)
def test_calculate_grade_invalid_score(score: float) -> None:
    """Scores outside 0-100 should raise ValueError."""
    with pytest.raises(ValueError):
        calculate_grade(score)


# ============================================================================
# determine_discount()
# ============================================================================


@pytest.mark.parametrize(
    ("amount", "premium", "expected"),
    [
        (12000, True, 25.0),
        (7000, True, 20.0),
        (2000, True, 10.0),
        (12000, False, 15.0),
        (7000, False, 10.0),
        (500, False, 5.0),
        (-100, False, 0.0),
    ],
)
def test_determine_discount(
    amount: float,
    premium: bool,
    expected: float,
) -> None:
    """Verify customer discounts."""
    assert determine_discount(amount, premium) == expected


# ============================================================================
# determine_temperature_status()
# ============================================================================


@pytest.mark.parametrize(
    ("temperature", "expected"),
    [
        (-5, "Freezing"),
        (5, "Cold"),
        (20, "Pleasant"),
        (30, "Warm"),
        (40, "Hot"),
    ],
)
def test_determine_temperature_status(
    temperature: float,
    expected: str,
) -> None:
    """Verify temperature classification."""
    assert determine_temperature_status(temperature) == expected


# ============================================================================
# validate_username()
# ============================================================================


@pytest.mark.parametrize(
    ("username", "expected"),
    [
        ("python", True),
        ("john_doe", True),
        ("abc", False),
        ("john doe", False),
    ],
)
def test_validate_username(
    username: str,
    expected: bool,
) -> None:
    """Verify username validation."""
    assert validate_username(username) is expected


# ============================================================================
# can_vote()
# ============================================================================


@pytest.mark.parametrize(
    ("age", "citizen", "expected"),
    [
        (18, True, True),
        (25, True, True),
        (17, True, False),
        (25, False, False),
    ],
)
def test_can_vote(
    age: int,
    citizen: bool,
    expected: bool,
) -> None:
    """Verify voting eligibility."""
    assert can_vote(age, citizen) is expected


# ============================================================================
# loan_approval()
# ============================================================================


@pytest.mark.parametrize(
    ("salary", "credit", "existing", "expected"),
    [
        (60000, 750, False, "Approved"),
        (20000, 750, False, "Rejected"),
        (60000, 500, False, "Rejected"),
        (60000, 750, True, "Manual Review"),
    ],
)
def test_loan_approval(
    salary: float,
    credit: int,
    existing: bool,
    expected: str,
) -> None:
    """Verify loan approval logic."""
    assert loan_approval(
        salary,
        credit,
        existing,
    ) == expected


# ============================================================================
# shipping_charge()
# ============================================================================


@pytest.mark.parametrize(
    ("amount", "expected"),
    [
        (1500, 0.0),
        (1000, 0.0),
        (999, 99.0),
        (200, 99.0),
    ],
)
def test_shipping_charge(
    amount: float,
    expected: float,
) -> None:
    """Verify shipping charge calculation."""
    assert shipping_charge(amount) == expected


# ============================================================================
# employee_bonus()
# ============================================================================


@pytest.mark.parametrize(
    ("years", "rating", "expected"),
    [
        (12, 5, 30),
        (12, 3, 20),
        (7, 5, 20),
        (7, 2, 10),
        (2, 5, 10),
        (2, 2, 5),
    ],
)
def test_employee_bonus(
    years: int,
    rating: int,
    expected: int,
) -> None:
    """Verify employee bonus calculation."""
    assert employee_bonus(years, rating) == expected


# ============================================================================
# classify_triangle()
# ============================================================================


@pytest.mark.parametrize(
    ("a", "b", "c", "expected"),
    [
        (3, 3, 3, "Equilateral"),
        (3, 3, 2, "Isosceles"),
        (3, 4, 5, "Scalene"),
        (1, 2, 10, "Invalid"),
        (0, 2, 3, "Invalid"),
    ],
)
def test_classify_triangle(
    a: float,
    b: float,
    c: float,
    expected: str,
) -> None:
    """Verify triangle classification."""
    assert classify_triangle(a, b, c) == expected