"""
Unit tests for control_flow.ternary_operator.

Run:

    pytest tests/test_ternary_operator.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from control_flow.ternary_operator import (
    absolute_value,
    determine_status,
    discount_percentage,
    employee_status,
    even_or_odd,
    file_permission,
    grade,
    login_message,
    maximum,
    minimum,
    pass_or_fail,
    safe_username,
    salary_category,
    shipping_charge,
    traffic_signal,
)


# ============================================================================
# determine_status()
# ============================================================================


@pytest.mark.parametrize(
    ("age", "expected"),
    [
        (18, "Adult"),
        (25, "Adult"),
        (17, "Minor"),
        (0, "Minor"),
    ],
)
def test_determine_status(
    age: int,
    expected: str,
) -> None:
    """Test adult/minor status."""
    assert determine_status(age) == expected


# ============================================================================
# absolute_value()
# ============================================================================


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (10, 10),
        (-10, 10),
        (0, 0),
        (-3.5, 3.5),
    ],
)
def test_absolute_value(
    number: int | float,
    expected: int | float,
) -> None:
    """Test absolute value."""
    assert absolute_value(number) == expected


# ============================================================================
# maximum()
# ============================================================================


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (10, 20, 20),
        (20, 10, 20),
        (5, 5, 5),
    ],
)
def test_maximum(
    first: int,
    second: int,
    expected: int,
) -> None:
    """Test maximum value."""
    assert maximum(first, second) == expected


# ============================================================================
# minimum()
# ============================================================================


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (10, 20, 10),
        (20, 10, 10),
        (5, 5, 5),
    ],
)
def test_minimum(
    first: int,
    second: int,
    expected: int,
) -> None:
    """Test minimum value."""
    assert minimum(first, second) == expected


# ============================================================================
# even_or_odd()
# ============================================================================


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (2, "Even"),
        (10, "Even"),
        (3, "Odd"),
        (-5, "Odd"),
    ],
)
def test_even_or_odd(
    number: int,
    expected: str,
) -> None:
    """Test even/odd classification."""
    assert even_or_odd(number) == expected


# ============================================================================
# pass_or_fail()
# ============================================================================


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (40, "Pass"),
        (95, "Pass"),
        (39.9, "Fail"),
        (0, "Fail"),
    ],
)
def test_pass_or_fail(
    score: float,
    expected: str,
) -> None:
    """Test pass/fail logic."""
    assert pass_or_fail(score) == expected


# ============================================================================
# login_message()
# ============================================================================


@pytest.mark.parametrize(
    ("logged_in", "expected"),
    [
        (True, "Welcome back!"),
        (False, "Please log in."),
    ],
)
def test_login_message(
    logged_in: bool,
    expected: str,
) -> None:
    """Test login message."""
    assert login_message(logged_in) == expected


# ============================================================================
# shipping_charge()
# ============================================================================


@pytest.mark.parametrize(
    ("amount", "expected"),
    [
        (1500, 0.0),
        (1000, 0.0),
        (999, 99.0),
        (100, 99.0),
    ],
)
def test_shipping_charge(
    amount: float,
    expected: float,
) -> None:
    """Test shipping calculation."""
    assert shipping_charge(amount) == expected


# ============================================================================
# salary_category()
# ============================================================================


@pytest.mark.parametrize(
    ("salary", "expected"),
    [
        (120000, "High"),
        (70000, "Medium"),
        (30000, "Low"),
    ],
)
def test_salary_category(
    salary: float,
    expected: str,
) -> None:
    """Test salary categorization."""
    assert salary_category(salary) == expected


# ============================================================================
# grade()
# ============================================================================


@pytest.mark.parametrize(
    ("score", "expected"),
    [
        (95, "A"),
        (85, "B"),
        (75, "C"),
        (65, "D"),
        (30, "F"),
    ],
)
def test_grade(
    score: float,
    expected: str,
) -> None:
    """Test grade calculation."""
    assert grade(score) == expected


# ============================================================================
# discount_percentage()
# ============================================================================


@pytest.mark.parametrize(
    ("premium", "expected"),
    [
        (True, 20),
        (False, 5),
    ],
)
def test_discount_percentage(
    premium: bool,
    expected: int,
) -> None:
    """Test customer discount."""
    assert discount_percentage(premium) == expected


# ============================================================================
# safe_username()
# ============================================================================


@pytest.mark.parametrize(
    ("username", "expected"),
    [
        ("Alice", "Alice"),
        ("", "Guest"),
        (None, "Guest"),
    ],
)
def test_safe_username(
    username: str | None,
    expected: str,
) -> None:
    """Test username fallback."""
    assert safe_username(username) == expected


# ============================================================================
# employee_status()
# ============================================================================


@pytest.mark.parametrize(
    ("active", "expected"),
    [
        (True, "Active"),
        (False, "Inactive"),
    ],
)
def test_employee_status(
    active: bool,
    expected: str,
) -> None:
    """Test employee status."""
    assert employee_status(active) == expected


# ============================================================================
# file_permission()
# ============================================================================


@pytest.mark.parametrize(
    ("admin", "expected"),
    [
        (True, "Read/Write"),
        (False, "Read Only"),
    ],
)
def test_file_permission(
    admin: bool,
    expected: str,
) -> None:
    """Test file permission."""
    assert file_permission(admin) == expected


# ============================================================================
# traffic_signal()
# ============================================================================


@pytest.mark.parametrize(
    ("color", "expected"),
    [
        ("red", "Stop"),
        ("RED", "Stop"),
        ("green", "Go"),
        ("GREEN", "Go"),
        ("yellow", "Slow Down"),
        ("blue", "Slow Down"),
    ],
)
def test_traffic_signal(
    color: str,
    expected: str,
) -> None:
    """Test traffic signal actions."""
    assert traffic_signal(color) == expected