from iterators.sorted_ops import sort_items


def test_sort_items():
    assert sort_items([3, 1, 2]) == [1, 2, 3]
