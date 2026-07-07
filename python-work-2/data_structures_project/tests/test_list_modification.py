from data_structures.list_modification import (
    remove_even_numbers,
)


def test_remove_even_numbers():
    numbers = [2, 4, 6, 7, 8]

    assert remove_even_numbers(numbers) == [7]


def test_remove_all_even():
    assert remove_even_numbers([2, 4, 6]) == []


def test_remove_no_even():
    assert remove_even_numbers([1, 3, 5]) == [1, 3, 5]


def test_remove_empty():
    assert remove_even_numbers([]) == []