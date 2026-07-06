from iterators.reversed_ops import reverse_items


def test_reverse_items():
    assert reverse_items([1, 2, 3]) == [3, 2, 1]
