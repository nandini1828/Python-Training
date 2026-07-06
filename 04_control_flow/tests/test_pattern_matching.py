"""
Unit tests for control_flow.pattern_matching.

Run:

    pytest tests/test_pattern_matching.py

Author: Python Training
"""

from __future__ import annotations

import pytest

from control_flow.pattern_matching import (
    User,
    authenticate_user,
    calculator,
    classify_number,
    detect_file_type,
    determine_weekend,
    extract_coordinates,
    get_http_status_message,
    identify_collection,
    parse_api_response,
    parse_command,
)


# ============================================================================
# get_http_status_message()
# ============================================================================


@pytest.mark.parametrize(
    ("status_code", "expected"),
    [
        (200, "OK"),
        (201, "Created"),
        (204, "No Content"),
        (400, "Bad Request"),
        (401, "Unauthorized"),
        (403, "Forbidden"),
        (404, "Not Found"),
        (500, "Internal Server Error"),
        (999, "Unknown Status"),
    ],
)
def test_get_http_status_message(
    status_code: int,
    expected: str,
) -> None:
    """Test HTTP status messages."""
    assert get_http_status_message(status_code) == expected


# ============================================================================
# determine_weekend()
# ============================================================================


@pytest.mark.parametrize(
    ("day", "expected"),
    [
        ("Saturday", True),
        ("Sunday", True),
        ("saturday", True),
        ("sunday", True),
        ("Monday", False),
        ("Friday", False),
    ],
)
def test_determine_weekend(
    day: str,
    expected: bool,
) -> None:
    """Test weekend detection."""
    assert determine_weekend(day) is expected


# ============================================================================
# classify_number()
# ============================================================================


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (-10, "Negative"),
        (0, "Zero"),
        (2, "Positive Even"),
        (7, "Positive Odd"),
    ],
)
def test_classify_number(
    number: int,
    expected: str,
) -> None:
    """Test number classification."""
    assert classify_number(number) == expected


# ============================================================================
# parse_command()
# ============================================================================


@pytest.mark.parametrize(
    ("command", "expected"),
    [
        (["exit"], "Exit Application"),
        (["help"], "Display Help"),
        (["delete", "notes.txt"], "Delete 'notes.txt'"),
        (
            ["copy", "a.txt", "b.txt"],
            "Copy 'a.txt' -> 'b.txt'",
        ),
        (["unknown"], "Unknown Command"),
    ],
)
def test_parse_command(
    command: list[str],
    expected: str,
) -> None:
    """Test command parsing."""
    assert parse_command(command) == expected


# ============================================================================
# extract_coordinates()
# ============================================================================


@pytest.mark.parametrize(
    ("point", "expected"),
    [
        ((0, 0), "Origin"),
        ((0, 10), "Y Axis (10)"),
        ((5, 0), "X Axis (5)"),
        ((4, 8), "Point (4, 8)"),
    ],
)
def test_extract_coordinates(
    point: tuple[int, int],
    expected: str,
) -> None:
    """Test tuple pattern matching."""
    assert extract_coordinates(point) == expected


# ============================================================================
# parse_api_response()
# ============================================================================


@pytest.mark.parametrize(
    ("response", "expected"),
    [
        (
            {
                "status": "success",
                "data": "Loaded",
            },
            "Success (Loaded)",
        ),
        (
            {
                "status": "error",
                "message": "Invalid Token",
            },
            "Error (Invalid Token)",
        ),
        (
            {},
            "Invalid Response",
        ),
    ],
)
def test_parse_api_response(
    response: dict[str, object],
    expected: str,
) -> None:
    """Test API response parsing."""
    assert parse_api_response(response) == expected


# ============================================================================
# authenticate_user()
# ============================================================================


def test_authenticate_admin() -> None:
    """Administrator access."""
    user = User(
        username="alice",
        role="admin",
        active=True,
    )

    assert authenticate_user(user) == "Administrator Access"


def test_authenticate_manager() -> None:
    """Manager access."""
    user = User(
        username="bob",
        role="manager",
        active=True,
    )

    assert authenticate_user(user) == "Manager Access"


def test_authenticate_disabled_user() -> None:
    """Disabled account."""
    user = User(
        username="charlie",
        role="developer",
        active=False,
    )

    assert authenticate_user(user) == "Account Disabled"


def test_authenticate_standard_user() -> None:
    """Standard user."""
    user = User(
        username="david",
        role="developer",
        active=True,
    )

    assert authenticate_user(user) == "Standard User"


# ============================================================================
# identify_collection()
# ============================================================================


@pytest.mark.parametrize(
    ("collection", "expected"),
    [
        ([], "Empty List"),
        ([1], "Single Item (1)"),
        ([1, 2], "Two Items (1, 2)"),
        (
            [1, 2, 3],
            "Starts With 1, Remaining 2",
        ),
        ("Python", "Unknown Collection"),
    ],
)
def test_identify_collection(
    collection: object,
    expected: str,
) -> None:
    """Test collection identification."""
    assert identify_collection(collection) == expected


# ============================================================================
# detect_file_type()
# ============================================================================


@pytest.mark.parametrize(
    ("filename", "expected"),
    [
        ("README.md", "Markdown"),
        ("image.jpg", "Image"),
        ("image.png", "Image"),
        ("script.py", "Python Source"),
        ("document.pdf", "PDF Document"),
        ("archive.zip", "Unknown File Type"),
    ],
)
def test_detect_file_type(
    filename: str,
    expected: str,
) -> None:
    """Test file type detection."""
    assert detect_file_type(filename) == expected


# ============================================================================
# calculator()
# ============================================================================


@pytest.mark.parametrize(
    ("operation", "left", "right", "expected"),
    [
        ("+", 10, 5, 15),
        ("-", 10, 5, 5),
        ("*", 10, 5, 50),
        ("/", 10, 2, 5),
    ],
)
def test_calculator(
    operation: str,
    left: float,
    right: float,
    expected: float,
) -> None:
    """Test calculator operations."""
    assert calculator(operation, left, right) == expected


def test_calculator_division_by_zero() -> None:
    """Division by zero should raise ValueError."""
    with pytest.raises(ValueError):
        calculator("/", 10, 0)


def test_calculator_invalid_operation() -> None:
    """Unsupported operations should raise ValueError."""
    with pytest.raises(ValueError):
        calculator("%", 10, 2)