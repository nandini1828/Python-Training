from utils.json_query import query_json


def test_query_simple_dict():
    data = {"user": {"name": "Alice", "address": {"city": "NY"}}}
    assert query_json(data, "user.name") == "Alice"
    assert query_json(data, "user.address.city") == "NY"


def test_query_list_index():
    data = {"employees": [{"name": "Bob"}, {"name": "Carol"}]}
    assert query_json(data, "employees.0.name") == "Bob"


def test_query_missing():
    data = {"a": 1}
    assert query_json(data, "a.b") is None
