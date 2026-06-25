from __future__ import annotations

from list_methods.list_utils import (
    ListMethods,
    average_values,
    chunk_list,
    find_duplicates,
)


def test_find_duplicates() -> None:
    assert find_duplicates([1, 2, 2, 3, 3, 3]) == [2, 3]


def test_chunk_list() -> None:
    assert chunk_list([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]


def test_average_values() -> None:
    assert average_values([1, 2, 3, 4]) == 2.5


def test_list_methods_helper() -> None:
    helper = ListMethods([3, 1, 2])
    assert helper.add_item(4) == [3, 1, 2, 4]
    assert helper.sort_items() == [1, 2, 3, 4]
    assert helper.get_length() == 4
