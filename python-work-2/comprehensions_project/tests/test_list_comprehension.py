from comprehensions.list_comprehension import (
    create_squares,
    get_even_numbers,
)


def test_create_squares():
    assert create_squares(5) == [
        0,
        1,
        4,
        9,
        16,
    ]


def test_create_squares_empty():
    assert create_squares(0) == []


def test_even_numbers():
    assert get_even_numbers(
        [1, 2, 3, 4, 5, 6]
    ) == [2, 4, 6]


def test_even_numbers_empty():
    assert get_even_numbers([]) == []