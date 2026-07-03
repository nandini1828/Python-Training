from looping_and_ds.python_loops_mastery.loops.break_continue import find_first_even, skip_even_numbers


def test_find_first_even():
    assert find_first_even([1, 3, 5, 8, 10]) == 8


def test_find_first_even_returns_none():
    assert find_first_even([1, 3, 5]) is None


def test_skip_even_numbers():
    assert skip_even_numbers([1, 2, 3, 4, 5, 6]) == [1, 3, 5]