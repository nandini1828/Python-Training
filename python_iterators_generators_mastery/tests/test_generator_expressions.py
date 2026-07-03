from iterators_generators.generator_expressions import (
    build_square_generator,
    build_even_generator,
)


def test_build_square_generator():
    generator = build_square_generator([1, 2, 3, 4])
    assert list(generator) == [1, 4, 9, 16]


def test_build_even_generator():
    generator = build_even_generator([1, 2, 3, 4, 5, 6])
    assert list(generator) == [2, 4, 6]