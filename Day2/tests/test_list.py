from __future__ import annotations

from list_methods.list_utils import average_values, chunk_list, find_duplicates


def test_find_duplicates() -> None:
    assert find_duplicates([1, 2, 2, 3, 3, 3]) == [2, 3]


def test_chunk_list() -> None:
    assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_average_values() -> None:
    assert average_values([1, 2, 3, 4]) == 2.5
