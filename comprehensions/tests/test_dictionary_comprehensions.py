from comprehensions.dictionary_comprehensions import dictionary_comprehension_example


def test_dictionary_comprehension_creates_squares():
    assert dictionary_comprehension_example(5) == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
