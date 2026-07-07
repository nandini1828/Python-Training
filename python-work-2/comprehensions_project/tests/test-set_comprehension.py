from set_comprehension import get_unique_lowercase


def test_unique_lowercase():
    words = [
        "Python",
        "JAVA",
        "python",
        "Java",
    ]

    assert get_unique_lowercase(words) == {
        "python",
        "java",
    }


def test_empty_words():
    assert get_unique_lowercase([]) == set()


def test_single_word():
    assert get_unique_lowercase(
        ["HELLO"]
    ) == {"hello"}