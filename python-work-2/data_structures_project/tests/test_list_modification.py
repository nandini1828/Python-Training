from data_structures.list_modification import (
    remove_even_numbers,
)


def test_remove_even_numbers():

    numbers = [2, 4, 6, 7, 8]

    expected = [7]

    assert remove_even_numbers(numbers) == expected