"""
Unit tests for defensive_iteration.py

Run:

    pytest tests/test_defensive_iteration.py
"""

from __future__ import annotations

import pytest

from iteration_safety.defensive_iteration import (
    immutable_filter,
    process_if_valid,
    safe_batch_processing,
    safe_dictionary_iteration,
    safe_set_iteration,
    safe_snapshot_iteration,
    validate_numbers,
)


def test_safe_snapshot_iteration() -> None:
    """Snapshot."""
    values = [1, 2, 3]

    result = safe_snapshot_iteration(values)

    assert result == values
    assert result is not values


def test_safe_batch_processing() -> None:
    """Batching."""
    result = safe_batch_processing(
        [1, 2, 3, 4, 5],
        2,
    )

    assert result == [
        [1, 2],
        [3, 4],
        [5],
    ]


def test_safe_batch_processing_invalid() -> None:
    """Invalid batch size."""
    with pytest.raises(ValueError):
        safe_batch_processing(
            [1, 2],
            0,
        )


def test_validate_numbers() -> None:
    """Validation."""
    assert validate_numbers(
        [1, 2, 3]
    )

    assert not validate_numbers(
        [1, "two", 3]
    )


def test_immutable_filter() -> None:
    """Immutable filter."""
    assert immutable_filter(
        [-2, 5, -1, 8]
    ) == (
        5,
        8,
    )


def test_process_if_valid() -> None:
    """Valid processing."""
    assert process_if_valid(
        [1, 2, 3]
    ) == [
        2,
        4,
        6,
    ]


def test_process_if_valid_invalid() -> None:
    """Invalid processing."""
    with pytest.raises(TypeError):
        process_if_valid(
            [1, "two", 3]
        )


def test_safe_dictionary_iteration() -> None:
    """Dictionary snapshot."""
    result = safe_dictionary_iteration(
        {
            "A": 1,
            "B": 2,
        }
    )

    assert result == [
        ("A", 1),
        ("B", 2),
    ]


def test_safe_set_iteration() -> None:
    """Set snapshot."""
    result = safe_set_iteration(
        {
            1,
            2,
            3,
        }
    )

    assert sorted(result) == [
        1,
        2,
        3,
    ]