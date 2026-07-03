from iteration_helpers.range_helper import generate_range


def test_generate_range_default_step():
    assert generate_range(1, 5) == [1, 2, 3, 4]


def test_generate_range_custom_step():
    assert generate_range(1, 10, 2) == [1, 3, 5, 7, 9]