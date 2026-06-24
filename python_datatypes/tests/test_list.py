from python_datatypes.list_methods import paginate_list, unique_ordered, list_statistics


def test_unique_ordered_preserves_order() -> None:
    values = [3, 1, 3, 2, 1]
    assert unique_ordered(values) == [3, 1, 2]


def test_paginate_list_returns_page() -> None:
    values = list(range(8))
    assert paginate_list(values, page=2, page_size=3) == [3, 4, 5]


def test_list_statistics_counts_elements() -> None:
    stats = list_statistics([1, 2, 2, 3])
    assert stats["count"] == 4
    assert stats["unique"] == 3
