"""Tests for generator-style helpers."""

from app.utils.generator_utils import number_generator, yield_names


def test_number_generator_returns_numbers() -> None:
    """The helper should build a simple list of numbers."""
    result = number_generator(5)
    assert result == [0, 1, 2, 3, 4]


def test_yield_names_returns_list() -> None:
    """The helper should return provided names."""
    assert yield_names(["Anna", "Ben"]) == ["Anna", "Ben"]
