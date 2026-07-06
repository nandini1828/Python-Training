"""
Unit tests for iteration_helpers.zip_examples.

Run:

    pytest tests/test_zip_examples.py

Author: Python Training
"""

from __future__ import annotations

from iteration_helpers.zip_examples import (
    combine_employee_records,
    compare_lists,
    create_dictionary,
    merge_student_marks,
    parallel_sum,
    transpose_matrix,
    unzip_pairs,
    zip_lists,
    zip_longest_lists,
    zip_three_lists,
)


def test_zip_lists() -> None:
    """Zip two lists."""
    assert zip_lists(
        [1, 2],
        ["A", "B"],
    ) == [
        (1, "A"),
        (2, "B"),
    ]


def test_zip_three_lists() -> None:
    """Zip three lists."""
    assert zip_three_lists(
        [1],
        [2],
        [3],
    ) == [
        (1, 2, 3),
    ]


def test_zip_longest_lists() -> None:
    """zip_longest()."""
    assert zip_longest_lists(
        [1],
        [2, 3],
        fill_value=None,
    ) == [
        (1, 2),
        (None, 3),
    ]


def test_create_dictionary() -> None:
    """Dictionary creation."""
    assert create_dictionary(
        ["name"],
        ["Alice"],
    ) == {
        "name": "Alice",
    }


def test_unzip_pairs() -> None:
    """Unzip."""
    first, second = unzip_pairs(
        [
            ("A", 1),
            ("B", 2),
        ]
    )

    assert first == ["A", "B"]
    assert second == [1, 2]


def test_parallel_sum() -> None:
    """Parallel addition."""
    assert parallel_sum(
        [1, 2],
        [3, 4],
    ) == [4, 6]


def test_compare_lists() -> None:
    """Comparison."""
    assert compare_lists(
        [1, 2],
        [1, 3],
    ) == [True, False]


def test_merge_student_marks() -> None:
    """Merge report."""
    assert merge_student_marks(
        ["Alice"],
        [100],
    ) == [
        "Alice: 100",
    ]


def test_employee_records() -> None:
    """Employee records."""
    records = combine_employee_records(
        ["Alice"],
        ["IT"],
    )

    assert records == [
        {
            "name": "Alice",
            "department": "IT",
        }
    ]


def test_transpose_matrix() -> None:
    """Matrix transpose."""
    matrix = [
        [1, 2],
        [3, 4],
    ]

    assert transpose_matrix(matrix) == [
        (1, 3),
        (2, 4),
    ]