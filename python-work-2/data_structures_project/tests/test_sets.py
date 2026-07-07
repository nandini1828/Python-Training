from data_structures.sets import (
    contains_number,
    unique_values,
)


def test_contains_number():
    numbers = {
        10,
        20,
        30,
        40,
    }

    assert contains_number(numbers, 20) is True


def test_contains_missing_number():
    numbers = {
        10,
        20,
        30,
        40,
    }

    assert contains_number(numbers, 100) is False


def test_unique_values():
    values = [1, 2, 2, 3, 4, 4]

    assert unique_values(values) == {
        1,
        2,
        3,
        4,
    }


def test_unique_values_empty():
    assert unique_values([]) == set()