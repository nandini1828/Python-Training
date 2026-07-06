from generators.generator_functions import countdown, fibonacci_numbers


def test_countdown():
    assert list(countdown(3)) == [3, 2, 1]


def test_fibonacci_numbers():
    assert list(fibonacci_numbers(6)) == [0, 1, 1, 2, 3, 5]
