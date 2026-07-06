from comprehensions.dictionary_comprehension import square_mapping, vowel_count


def test_square_mapping():
    assert square_mapping(5) == {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


def test_vowel_count():
    assert vowel_count("hello world") == {"a": 0, "e": 1, "i": 0, "o": 2, "u": 0}
