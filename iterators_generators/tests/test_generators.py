from iterators_generators.generators import generate_numbers, generate_even_numbers


def test_generate_numbers_yields_expected_values():
    assert list(generate_numbers(5)) == [0, 1, 2, 3, 4]


def test_generate_even_numbers_yields_even_values():
    assert list(generate_even_numbers(10)) == [0, 2, 4, 6, 8]
