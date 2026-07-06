"""
Unit tests for control_flow.truthy_falsy.

Run

    pytest tests/test_truthy_falsy.py

Author: Python Training
"""

from __future__ import annotations

from typing import Any

import pytest

from control_flow.truthy_falsy import (
    Playlist,
    ShoppingCart,
    all_values_truthy,
    any_value_truthy,
    default_username,
    falsy_examples,
    first_available_value,
    get_truthiness,
    has_content,
    has_items,
    is_falsy,
    is_truthy,
    is_valid_response,
    remove_falsy_values,
    safe_display_name,
    truthy_examples,
)


# =============================================================================
# is_truthy()
# =============================================================================


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (1, True),
        ("Python", True),
        ([1, 2], True),
        ({1}, True),
        ([], False),
        ("", False),
        ({}, False),
        (None, False),
        (0, False),
    ],
)
def test_is_truthy(
    value: Any,
    expected: bool,
) -> None:
    """Test truthiness detection."""
    assert is_truthy(value) is expected


# =============================================================================
# is_falsy()
# =============================================================================


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ([], True),
        ("", True),
        (0, True),
        (None, True),
        ("Python", False),
        (10, False),
    ],
)
def test_is_falsy(
    value: Any,
    expected: bool,
) -> None:
    """Test falsy detection."""
    assert is_falsy(value) is expected


# =============================================================================
# get_truthiness()
# =============================================================================


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (10, "Truthy"),
        ("Hello", "Truthy"),
        ([], "Falsy"),
        ("", "Falsy"),
    ],
)
def test_get_truthiness(
    value: Any,
    expected: str,
) -> None:
    """Test truthiness description."""
    assert get_truthiness(value) == expected


# =============================================================================
# default_username()
# =============================================================================


@pytest.mark.parametrize(
    ("username", "expected"),
    [
        ("Alice", "Alice"),
        ("", "Guest"),
        (None, "Guest"),
    ],
)
def test_default_username(
    username: str | None,
    expected: str,
) -> None:
    """Test username fallback."""
    assert default_username(username) == expected


# =============================================================================
# first_available_value()
# =============================================================================


def test_first_available_value() -> None:
    """Test first truthy value."""
    assert first_available_value("", None, 0, "Python") == "Python"


def test_first_available_value_none() -> None:
    """Return None if every value is falsy."""
    assert first_available_value("", None, [], 0) is None


# =============================================================================
# all_values_truthy()
# =============================================================================


def test_all_values_truthy_true() -> None:
    """Every value is truthy."""
    assert all_values_truthy([1, "Python", [1]]) is True


def test_all_values_truthy_false() -> None:
    """One value is falsy."""
    assert all_values_truthy([1, "", 3]) is False


# =============================================================================
# any_value_truthy()
# =============================================================================


def test_any_value_truthy_true() -> None:
    """At least one truthy value."""
    assert any_value_truthy([0, "", "Python"]) is True


def test_any_value_truthy_false() -> None:
    """Every value is falsy."""
    assert any_value_truthy([0, "", None]) is False


# =============================================================================
# safe_display_name()
# =============================================================================


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("Alice", "Alice"),
        ("", "Anonymous"),
        (None, "Anonymous"),
    ],
)
def test_safe_display_name(
    value: str | None,
    expected: str,
) -> None:
    """Test display name fallback."""
    assert safe_display_name(value) == expected


# =============================================================================
# has_items()
# =============================================================================


def test_has_items_true() -> None:
    """Non-empty collection."""
    assert has_items([1]) is True


def test_has_items_false() -> None:
    """Empty collection."""
    assert has_items([]) is False


# =============================================================================
# has_content()
# =============================================================================


def test_has_content_true() -> None:
    """Non-empty string."""
    assert has_content("Python") is True


def test_has_content_false() -> None:
    """Empty string."""
    assert has_content("") is False


# =============================================================================
# is_valid_response()
# =============================================================================


def test_is_valid_response_true() -> None:
    """Valid response."""
    assert is_valid_response({"status": "ok"}) is True


def test_is_valid_response_false() -> None:
    """Empty response."""
    assert is_valid_response({}) is False


# =============================================================================
# remove_falsy_values()
# =============================================================================


def test_remove_falsy_values() -> None:
    """Remove falsy values."""
    values = [0, "", None, 5, "Python", [], [1]]

    expected = [5, "Python", [1]]

    assert remove_falsy_values(values) == expected


# =============================================================================
# truthy_examples()
# =============================================================================


def test_truthy_examples() -> None:
    """Every truthy example should evaluate to True."""
    for value in truthy_examples():
        assert bool(value) is True


# =============================================================================
# falsy_examples()
# =============================================================================


def test_falsy_examples() -> None:
    """Every falsy example should evaluate to False."""
    for value in falsy_examples():
        assert bool(value) is False


# =============================================================================
# ShoppingCart
# =============================================================================


def test_empty_shopping_cart_is_false() -> None:
    """Empty cart should be falsy."""
    cart = ShoppingCart()

    assert bool(cart) is False


def test_shopping_cart_with_items_is_true() -> None:
    """Non-empty cart should be truthy."""
    cart = ShoppingCart(["Keyboard"])

    assert bool(cart) is True


# =============================================================================
# Playlist
# =============================================================================


def test_empty_playlist_is_false() -> None:
    """Empty playlist should be falsy."""
    playlist = Playlist()

    assert bool(playlist) is False


def test_playlist_with_songs_is_true() -> None:
    """Playlist containing songs should be truthy."""
    playlist = Playlist(["Song A"])

    assert bool(playlist) is True