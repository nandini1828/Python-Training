"""
Unit tests for loop_foundations.for_else_while_else.

Run:

    pytest tests/test_for_else.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from loop_foundations.for_else_while_else import (
    authenticate_user,
    find_employee,
    first_divisible,
    is_prime,
    login_attempts,
    process_queue,
    retry_connection,
    search_item,
    validate_inventory,
    wait_for_service,
)


# ============================================================================
# search_item()
# ============================================================================


def test_search_item_found() -> None:
    """Item exists in the collection."""
    items = ["Python", "Django", "FastAPI"]

    assert search_item(items, "Django") is True


def test_search_item_not_found() -> None:
    """Item does not exist."""
    items = ["Python", "Django"]

    assert search_item(items, "Flask") is False


# ============================================================================
# find_employee()
# ============================================================================


def test_find_employee_found() -> None:
    """Employee exists."""
    employees = ["Alice", "Bob", "Charlie"]

    assert find_employee(employees, "Bob") == "Bob found."


def test_find_employee_not_found() -> None:
    """Employee does not exist."""
    employees = ["Alice", "Bob"]

    assert find_employee(employees, "David") == "David not found."


# ============================================================================
# is_prime()
# ============================================================================


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (2, True),
        (3, True),
        (5, True),
        (17, True),
        (29, True),
        (1, False),
        (0, False),
        (-5, False),
        (4, False),
        (10, False),
        (25, False),
    ],
)
def test_is_prime(
    number: int,
    expected: bool,
) -> None:
    """Test prime number detection."""
    assert is_prime(number) is expected


# ============================================================================
# login_attempts()
# ============================================================================


def test_login_attempts_success() -> None:
    """Correct password is supplied."""
    attempts = [
        "password",
        "python123",
        "admin",
    ]

    assert login_attempts(attempts, "admin") is True


def test_login_attempts_failure() -> None:
    """Correct password never supplied."""
    attempts = [
        "password",
        "python123",
    ]

    assert login_attempts(attempts, "admin") is False


# ============================================================================
# retry_connection()
# ============================================================================


def test_retry_connection_success() -> None:
    """Connection succeeds before timeout."""
    assert retry_connection(
        success_on_attempt=3,
        maximum_attempts=5,
    ) is True


def test_retry_connection_failure() -> None:
    """Connection never succeeds."""
    assert retry_connection(
        success_on_attempt=10,
        maximum_attempts=5,
    ) is False


# ============================================================================
# wait_for_service()
# ============================================================================


def test_wait_for_service_success() -> None:
    """Service becomes available."""
    assert wait_for_service(
        ready_after=2,
        timeout=5,
    ) is True


def test_wait_for_service_timeout() -> None:
    """Timeout occurs."""
    assert wait_for_service(
        ready_after=10,
        timeout=5,
    ) is False


# ============================================================================
# first_divisible()
# ============================================================================


def test_first_divisible_found() -> None:
    """Return first divisible number."""
    numbers = [5, 7, 9, 12]

    assert first_divisible(numbers, 3) == 9


def test_first_divisible_not_found() -> None:
    """Return None."""
    numbers = [5, 7, 11]

    assert first_divisible(numbers, 3) is None


# ============================================================================
# validate_inventory()
# ============================================================================


def test_validate_inventory_valid() -> None:
    """All inventory quantities are valid."""
    assert validate_inventory(
        [10, 5, 8, 1],
    ) is True


def test_validate_inventory_invalid() -> None:
    """Inventory contains invalid quantity."""
    assert validate_inventory(
        [10, 5, 0, 8],
    ) is False


# ============================================================================
# process_queue()
# ============================================================================


def test_process_queue_stop_found() -> None:
    """Queue stops at sentinel value."""
    queue = [
        "Task-1",
        "Task-2",
        "STOP",
        "Task-3",
    ]

    assert process_queue(queue, "STOP") == [
        "Task-1",
        "Task-2",
    ]


def test_process_queue_no_stop() -> None:
    """Entire queue is processed."""
    queue = [
        "Task-1",
        "Task-2",
    ]

    assert process_queue(queue, "STOP") == [
        "Task-1",
        "Task-2",
    ]


# ============================================================================
# authenticate_user()
# ============================================================================


def test_authenticate_user_success() -> None:
    """User exists."""
    users = [
        "alice",
        "bob",
        "charlie",
    ]

    assert authenticate_user(users, "bob") is True


def test_authenticate_user_failure() -> None:
    """User does not exist."""
    users = [
        "alice",
        "bob",
    ]

    assert authenticate_user(users, "david") is False