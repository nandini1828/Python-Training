from generators.generator_expressions import even_numbers, square_numbers


def test_square_numbers():
    assert list(square_numbers([1, 2, 3, 4])) == [1, 4, 9, 16]


def test_even_numbers():
    assert list(even_numbers([1, 2, 3, 4, 5])) == [2, 4]
