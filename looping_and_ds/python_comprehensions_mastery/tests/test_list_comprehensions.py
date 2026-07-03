from looping_and_ds.python_comprehensions_mastery.comprehensions.list_comprehensions import (
    get_even_numbers,
    get_squared_numbers,
)


def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_get_squared_numbers():
    assert get_squared_numbers([1, 2, 3, 4]) == [1, 4, 9, 16]