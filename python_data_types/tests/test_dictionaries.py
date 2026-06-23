from dictionaries import word_count, query_json


def test_word_count():
    text = "Hello hello world"
    result = word_count(text)

    assert result["hello"] == 2
    assert result["world"] == 1


def test_query_json():
    data = {"a": {"b": {"c": 10}}}

    assert query_json(data, "a.b.c") == 10
    assert query_json(data, "a.x", 0) == 0