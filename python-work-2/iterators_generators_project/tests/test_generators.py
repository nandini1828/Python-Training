from iterators_generators.generators import (
    countdown,
    fibonacci,
)


def test_countdown():

    assert list(countdown(5)) == [5, 4, 3, 2, 1]


def test_fibonacci():

    expected = [0, 1, 1, 2, 3, 5, 8]

    assert list(fibonacci(7)) == expected