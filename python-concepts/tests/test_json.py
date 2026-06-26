from dictionary.exercises import (
    query_json,
    word_count
)


def test_query_json():

    data = {
        "user": {
            "name": "Alice"
        }
    }

    assert (
        query_json(
            data,
            "user.name"
        )
        == "Alice"
    )


def test_query_default():

    data = {}

    assert (
        query_json(
            data,
            "user.age",
            18
        )
        == 18
    )


def test_word_count():

    result = word_count(
        "Python Python AI"
    )

    assert result["python"] == 2
    assert result["ai"] == 1