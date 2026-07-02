from comprehensions.set_comprehension import (
    get_unique_lowercase,
)


def test_get_unique_lowercase():

    words = [
        "Python",
        "JAVA",
        "python",
        "Java",
    ]

    expected = {
        "python",
        "java",
    }

    assert get_unique_lowercase(words) == expected