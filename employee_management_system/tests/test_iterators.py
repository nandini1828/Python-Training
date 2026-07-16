"""Tests for iterator helpers."""

from app.utils.iterator_utils import iterate_with_enumerate, iterate_with_zip


def test_enumerate_helper_returns_pairs() -> None:
    """The enumerate helper should preserve the original order."""
    result = iterate_with_enumerate(["a", "b"])
    assert result == [(0, "a"), (1, "b")]


def test_zip_helper_returns_pairs() -> None:
    """The zip helper should combine two lists."""
    result = iterate_with_zip([1, 2], ["one", "two"])
    assert result == [(1, "one"), (2, "two")]
