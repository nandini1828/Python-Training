from comprehensions.list_comprehension import even_numbers, uppercase_words


def test_even_numbers():
    assert even_numbers([1, 2, 3, 4, 5]) == [2, 4]


def test_uppercase_words():
    assert uppercase_words(["apple", "banana"]) == ["APPLE", "BANANA"]
