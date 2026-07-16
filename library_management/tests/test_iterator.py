from utilities.generators import generate_book_ids


def test_generator_yields_values():
    values = list(generate_book_ids(3))
    assert values == [1, 2, 3]
