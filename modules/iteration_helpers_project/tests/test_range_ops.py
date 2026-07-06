from iterators.range_ops import generate_range


def test_generate_range():
    assert generate_range(1, 10, 2) == [1, 3, 5, 7, 9]
    assert generate_range(5) == [0, 1, 2, 3, 4]
