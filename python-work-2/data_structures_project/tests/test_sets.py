from data_structures.sets import (
    contains_number,
    unique_values,
)


def test_contains_number():

    numbers = {10, 20, 30}

    assert contains_number(numbers, 20) is True


def test_contains_missing_number():

    numbers = {10, 20, 30}

    assert contains_number(numbers, 100) is False


def test_unique_values():

    numbers = [1, 2, 2, 3, 4, 4]

    assert unique_values(numbers) == {1, 2, 3, 4}