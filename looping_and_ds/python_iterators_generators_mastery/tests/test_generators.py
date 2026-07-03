from looping_and_ds.python_iterators_generators_mastery.iterators_generators.generators import (
    generate_numbers,
    generate_even_numbers,
)


def test_generate_numbers():
    assert list(generate_numbers(5)) == [1, 2, 3, 4, 5]


def test_generate_even_numbers():
    assert list(generate_even_numbers(10)) == [2, 4, 6, 8, 10]