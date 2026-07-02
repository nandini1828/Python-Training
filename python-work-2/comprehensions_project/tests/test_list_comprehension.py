from comprehensions.list_comprehension import (
    create_squares,
    get_even_numbers,
)


def test_create_squares():

    expected = [0, 1, 4, 9, 16]

    assert create_squares(5) == expected


def test_get_even_numbers():

    numbers = [1, 2, 3, 4, 5, 6]

    expected = [2, 4, 6]

    assert get_even_numbers(numbers) == expected