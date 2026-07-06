"""
Unit tests for control_flow.logical_operators.

Run:

    pytest tests/test_logical_operators.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from control_flow.logical_operators import (
    can_access_admin_panel,
    can_access_resource,
    can_apply_for_job,
    can_drive,
    can_vote,
    contains_keyword,
    evaluate_login,
    has_permission,
    is_active_user,
    is_eligible_for_loan,
    is_not_none,
    is_same_object,
    operator_precedence_example,
    requires_manual_review,
    should_send_email,
)


# ============================================================================
# can_access_admin_panel()
# ============================================================================


@pytest.mark.parametrize(
    ("logged_in", "admin", "expected"),
    [
        (True, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, False),
    ],
)
def test_can_access_admin_panel(
    logged_in: bool,
    admin: bool,
    expected: bool,
) -> None:
    """Test admin access."""
    assert can_access_admin_panel(logged_in, admin) is expected


# ============================================================================
# can_vote()
# ============================================================================


@pytest.mark.parametrize(
    ("age", "citizen", "expected"),
    [
        (18, True, True),
        (30, True, True),
        (17, True, False),
        (20, False, False),
    ],
)
def test_can_vote(
    age: int,
    citizen: bool,
    expected: bool,
) -> None:
    """Test voting eligibility."""
    assert can_vote(age, citizen) is expected


# ============================================================================
# can_drive()
# ============================================================================


@pytest.mark.parametrize(
    ("age", "license", "expected"),
    [
        (18, True, True),
        (40, True, True),
        (16, True, False),
        (25, False, False),
    ],
)
def test_can_drive(
    age: int,
    license: bool,
    expected: bool,
) -> None:
    """Test driving eligibility."""
    assert can_drive(age, license) is expected


# ============================================================================
# is_eligible_for_loan()
# ============================================================================


@pytest.mark.parametrize(
    ("salary", "credit_score", "expected"),
    [
        (50000, 750, True),
        (30000, 700, True),
        (25000, 750, False),
        (50000, 650, False),
    ],
)
def test_is_eligible_for_loan(
    salary: float,
    credit_score: int,
    expected: bool,
) -> None:
    """Test loan eligibility."""
    assert is_eligible_for_loan(
        salary,
        credit_score,
    ) is expected


# ============================================================================
# can_apply_for_job()
# ============================================================================


@pytest.mark.parametrize(
    ("experience", "degree", "expected"),
    [
        (3, False, True),
        (0, True, True),
        (3, True, True),
        (0, False, False),
    ],
)
def test_can_apply_for_job(
    experience: int,
    degree: bool,
    expected: bool,
) -> None:
    """Test job eligibility."""
    assert can_apply_for_job(experience, degree) is expected


# ============================================================================
# requires_manual_review()
# ============================================================================


@pytest.mark.parametrize(
    ("amount", "blacklisted", "expected"),
    [
        (200000, False, True),
        (50000, True, True),
        (50000, False, False),
    ],
)
def test_requires_manual_review(
    amount: float,
    blacklisted: bool,
    expected: bool,
) -> None:
    """Test manual review requirement."""
    assert requires_manual_review(amount, blacklisted) is expected


# ============================================================================
# is_active_user()
# ============================================================================


@pytest.mark.parametrize(
    ("deleted", "blocked", "expected"),
    [
        (False, False, True),
        (True, False, False),
        (False, True, False),
        (True, True, False),
    ],
)
def test_is_active_user(
    deleted: bool,
    blocked: bool,
    expected: bool,
) -> None:
    """Test user active status."""
    assert is_active_user(deleted, blocked) is expected


# ============================================================================
# should_send_email()
# ============================================================================


@pytest.mark.parametrize(
    ("verified", "opt_in", "expected"),
    [
        (True, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, False),
    ],
)
def test_should_send_email(
    verified: bool,
    opt_in: bool,
    expected: bool,
) -> None:
    """Test email sending conditions."""
    assert should_send_email(
        verified,
        opt_in,
    ) is expected


# ============================================================================
# has_permission()
# ============================================================================


@pytest.mark.parametrize(
    ("role", "permissions", "expected"),
    [
        ("admin", set(), True),
        ("developer", {"write"}, True),
        ("developer", {"read"}, False),
    ],
)
def test_has_permission(
    role: str,
    permissions: set[str],
    expected: bool,
) -> None:
    """Test permission checks."""
    assert has_permission(role, permissions) is expected


# ============================================================================
# contains_keyword()
# ============================================================================


@pytest.mark.parametrize(
    ("text", "keyword", "expected"),
    [
        ("Learn Python", "python", True),
        ("HELLO WORLD", "world", True),
        ("Java", "python", False),
    ],
)
def test_contains_keyword(
    text: str,
    keyword: str,
    expected: bool,
) -> None:
    """Test keyword search."""
    assert contains_keyword(text, keyword) is expected


# ============================================================================
# is_same_object()
# ============================================================================


def test_is_same_object_true() -> None:
    """Same object reference."""
    value = []

    assert is_same_object(value, value) is True


def test_is_same_object_false() -> None:
    """Different objects with same value."""
    first = [1]
    second = [1]

    assert is_same_object(first, second) is False


# ============================================================================
# is_not_none()
# ============================================================================


def test_is_not_none_true() -> None:
    """Non-None value."""
    assert is_not_none("Python") is True


def test_is_not_none_false() -> None:
    """None value."""
    assert is_not_none(None) is False


# ============================================================================
# operator_precedence_example()
# ============================================================================


@pytest.mark.parametrize(
    ("age", "admin", "verified", "expected"),
    [
        (20, False, True, True),
        (17, True, False, True),
        (17, False, True, False),
        (20, False, False, False),
    ],
)
def test_operator_precedence_example(
    age: int,
    admin: bool,
    verified: bool,
    expected: bool,
) -> None:
    """Test logical operator precedence."""
    assert operator_precedence_example(
        age,
        admin,
        verified,
    ) is expected


# ============================================================================
# evaluate_login()
# ============================================================================


@pytest.mark.parametrize(
    ("username", "password", "expected"),
    [
        ("admin", "python123", True),
        ("admin", "wrong", False),
        ("user", "python123", False),
    ],
)
def test_evaluate_login(
    username: str,
    password: str,
    expected: bool,
) -> None:
    """Test login evaluation."""
    assert evaluate_login(username, password) is expected


# ============================================================================
# can_access_resource()
# ============================================================================


@pytest.mark.parametrize(
    ("authenticated", "subscription", "trial", "expected"),
    [
        (True, True, False, True),
        (True, False, True, True),
        (True, False, False, False),
        (False, True, True, False),
    ],
)
def test_can_access_resource(
    authenticated: bool,
    subscription: bool,
    trial: bool,
    expected: bool,
) -> None:
    """Test protected resource access."""
    assert can_access_resource(
        authenticated,
        subscription,
        trial,
    ) is expected