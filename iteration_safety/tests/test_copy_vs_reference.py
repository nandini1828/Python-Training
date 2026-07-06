"""
Unit tests for copy_vs_reference.py

Run:

    pytest tests/test_copy_vs_reference.py
"""

from __future__ import annotations

from iteration_safety.copy_vs_reference import (
    copy_using_list,
    copy_using_method,
    copy_using_slice,
    create_deep_copy,
    create_shallow_copy,
    demonstrate_reference,
    object_equality,
    object_identity,
)


def test_reference_assignment() -> None:
    """Reference assignment."""
    values = [1, 2, 3]

    original, reference = demonstrate_reference(values)

    assert object_identity(original, reference)
    assert object_equality(original, reference)


def test_shallow_copy() -> None:
    """Shallow copy."""
    values = [1, 2, 3]

    copied = create_shallow_copy(values)

    assert copied == values
    assert copied is not values


def test_deep_copy() -> None:
    """Deep copy."""
    values = [[1], [2]]

    copied = create_deep_copy(values)

    assert copied == values
    assert copied is not values

    copied[0].append(99)

    assert values == [[1], [2]]


def test_slice_copy() -> None:
    """Slice copy."""
    values = [1, 2, 3]

    copied = copy_using_slice(values)

    assert copied == values
    assert copied is not values


def test_list_copy() -> None:
    """list() copy."""
    values = [1, 2, 3]

    copied = copy_using_list(values)

    assert copied == values
    assert copied is not values


def test_copy_method() -> None:
    """copy() method."""
    values = [1, 2, 3]

    copied = copy_using_method(values)

    assert copied == values
    assert copied is not values


def test_object_identity() -> None:
    """Identity."""
    values = [1]

    assert object_identity(values, values)
    assert not object_identity(values, [1])


def test_object_equality() -> None:
    """Equality."""
    assert object_equality([1, 2], [1, 2])