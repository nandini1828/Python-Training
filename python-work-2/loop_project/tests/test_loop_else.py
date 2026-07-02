from loops.loop_else import (
    search_number,
    while_search,
)


def test_for_else_found():

    numbers = [10, 20, 30, 40]

    assert search_number(numbers, 30) == "Found"


def test_for_else_not_found():

    numbers = [10, 20, 30, 40]

    assert search_number(numbers, 100) == "Not Found"


def test_while_else_found():

    numbers = [1, 2, 3, 4]

    assert while_search(numbers, 3) == "Found"


def test_while_else_not_found():

    numbers = [1, 2, 3, 4]

    assert while_search(numbers, 10) == "Not Found"