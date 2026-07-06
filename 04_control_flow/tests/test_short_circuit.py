"""
Unit tests for control_flow.short_circuit.

Run:

    pytest tests/test_short_circuit.py

Author: Python Training
"""

from __future__ import annotations

from typing import Any

import pytest

from control_flow.short_circuit import (
    cached_value_example,
    email_domain,
    first_non_empty,
    get_cached_value,
    get_configuration,
    get_nested_value,
    get_username,
    has_permission,
    is_authorized,
    is_even,
    positive_even_number,
    positive_number,
    safe_length,
    safe_upper,
    should_process,
    validate_user,
)


# ============================================================================
# cached_value_example()
# ============================================================================


def test_cached_value_example_returns_cached_value() -> None:
    """Cached value should be returned."""
    assert cached_value_example("Cached") == "Cached"


def test_cached_value_example_returns_database_result() -> None:
    """Database value should be returned when cache is missing."""
    assert cached_value_example(None) == "Database Result"


# ============================================================================
# get_cached_value()
# ============================================================================


@pytest.mark.parametrize(
    ("cached", "fallback", "expected"),
    [
        ("Cache", "Database", "Cache"),
        (None, "Database", "Database"),
        ("", "Default", "Default"),
        (0, 100, 100),
        (False, True, True),
    ],
)
def test_get_cached_value(
    cached: Any,
    fallback: Any,
    expected: Any,
) -> None:
    """Test cached value retrieval."""
    assert get_cached_value(cached, fallback) == expected


# ============================================================================
# is_authorized()
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
def test_is_authorized(
    logged_in: bool,
    admin: bool,
    expected: bool,
) -> None:
    """Test authorization."""
    assert is_authorized(logged_in, admin) is expected


# ============================================================================
# safe_upper()
# ============================================================================


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("python", "PYTHON"),
        ("ChatGPT", "CHATGPT"),
        ("", ""),
        (None, ""),
    ],
)
def test_safe_upper(
    text: str | None,
    expected: str,
) -> None:
    """Test safe uppercase conversion."""
    assert safe_upper(text) == expected


# ============================================================================
# safe_length()
# ============================================================================


@pytest.mark.parametrize(
    ("collection", "expected"),
    [
        ([1, 2, 3], 3),
        (["Python"], 1),
        ([], 0),
        (None, 0),
    ],
)
def test_safe_length(
    collection: list[Any] | None,
    expected: int,
) -> None:
    """Test safe length calculation."""
    assert safe_length(collection) == expected


# ============================================================================
# get_username()
# ============================================================================


@pytest.mark.parametrize(
    ("username", "expected"),
    [
        ("Alice", "Alice"),
        ("", "Guest"),
        (None, "Guest"),
    ],
)
def test_get_username(
    username: str | None,
    expected: str,
) -> None:
    """Test username fallback."""
    assert get_username(username) == expected


# ============================================================================
# get_configuration()
# ============================================================================


def test_configuration_prefers_environment() -> None:
    """Environment value has highest priority."""
    assert (
        get_configuration(
            "ENV",
            "CONFIG",
            "DEFAULT",
        )
        == "ENV"
    )


def test_configuration_uses_config_file() -> None:
    """Configuration file is used if environment is missing."""
    assert (
        get_configuration(
            None,
            "CONFIG",
            "DEFAULT",
        )
        == "CONFIG"
    )


def test_configuration_uses_default() -> None:
    """Default is used when nothing else exists."""
    assert (
        get_configuration(
            None,
            None,
            "DEFAULT",
        )
        == "DEFAULT"
    )


# ============================================================================
# validate_user()
# ============================================================================


@pytest.mark.parametrize(
    ("username", "password", "expected"),
    [
        ("admin", "python123", True),
        ("admin", "wrong", False),
        ("guest", "python123", False),
    ],
)
def test_validate_user(
    username: str,
    password: str,
    expected: bool,
) -> None:
    """Test login validation."""
    assert validate_user(username, password) is expected


# ============================================================================
# should_process()
# ============================================================================


@pytest.mark.parametrize(
    ("data", "expected"),
    [
        ([1], True),
        ([1, 2, 3], True),
        ([], False),
        (None, False),
    ],
)
def test_should_process(
    data: list[Any] | None,
    expected: bool,
) -> None:
    """Test data processing decision."""
    assert should_process(data) is expected


# ============================================================================
# first_non_empty()
# ============================================================================


def test_first_non_empty_returns_first_truthy_value() -> None:
    """First truthy value should be returned."""
    assert first_non_empty("", None, 0, "Python") == "Python"


def test_first_non_empty_returns_none() -> None:
    """None should be returned if everything is falsy."""
    assert first_non_empty("", None, 0, False) is None


# ============================================================================
# has_permission()
# ============================================================================


@pytest.mark.parametrize(
    ("admin", "permissions", "expected"),
    [
        (True, set(), True),
        (False, {"write"}, True),
        (False, {"read"}, False),
    ],
)
def test_has_permission(
    admin: bool,
    permissions: set[str],
    expected: bool,
) -> None:
    """Test write permission."""
    assert has_permission(admin, permissions) is expected


# ============================================================================
# get_nested_value()
# ============================================================================


def test_get_nested_value_found() -> None:
    """Existing key should be returned."""
    data = {"name": "Alice"}

    assert get_nested_value(data, "name") == "Alice"


def test_get_nested_value_missing() -> None:
    """Missing key returns None."""
    data = {"name": "Alice"}

    assert get_nested_value(data, "age") is None


def test_get_nested_value_none_dictionary() -> None:
    """None dictionary returns None."""
    assert get_nested_value(None, "name") is None


# ============================================================================
# email_domain()
# ============================================================================


def test_email_domain_valid() -> None:
    """Extract email domain."""
    assert email_domain("user@example.com") == "example.com"


def test_email_domain_none() -> None:
    """None email returns None."""
    assert email_domain(None) is None


# ============================================================================
# positive_number()
# ============================================================================


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (10, True),
        (1, True),
        (0, False),
        (-10, False),
    ],
)
def test_positive_number(
    number: int,
    expected: bool,
) -> None:
    """Test positive number detection."""
    assert positive_number(number) is expected


# ============================================================================
# is_even()
# ============================================================================


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (2, True),
        (100, True),
        (3, False),
        (-4, True),
    ],
)
def test_is_even(
    number: int,
    expected: bool,
) -> None:
    """Test even number detection."""
    assert is_even(number) is expected


# ============================================================================
# positive_even_number()
# ============================================================================


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (2, True),
        (10, True),
        (-2, False),
        (5, False),
        (0, False),
    ],
)
def test_positive_even_number(
    number: int,
    expected: bool,
) -> None:
    """Test positive even number detection."""
    assert positive_even_number(number) is expected